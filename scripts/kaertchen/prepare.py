import sexpdata,json,re
from pathlib import Path
base=Path(__file__).parent
symbols={}
def tag(x):return str(x[0]) if isinstance(x,list) and x else ''
def find(x,key):return next((n for n in x if tag(n)==key),None)
for p in base.glob('*.kicad_sym'):
 tree=sexpdata.loads(p.read_text())
 for node in tree:
  if tag(node)=='symbol':symbols[str(node[1])]=(node,p.name)
def get(name):
 node,lib=symbols[name];ext=find(node,'extends');pins=[]
 if ext:pins=get(str(ext[1]))[0]
 def walk(x,unit=None):
  if not isinstance(x,list):return
  if tag(x)=='symbol':unit=str(x[1])
  if tag(x)=='pin':
   num=find(x,'number');label=find(x,'name')
   if num and str(num[1]).isdigit():pins.append({'number':int(str(num[1])),'name':str(label[1]),'role':str(x[1]),'shape':str(x[2]),'unit':unit})
  for c in x:
   if isinstance(c,list):walk(c,unit)
 walk(node)
 return pins,lib
rows=[];section=''
for line in (base.resolve().parents[1]/'Bauteile.md').read_text().splitlines():
 if line.startswith('## '):section=line[3:]
 if not line.startswith('| '):continue
 cells=[c.strip() for c in line.split('|')[1:-1]]
 if cells[0].startswith(('Bezeichnung','---')):continue
 part=cells[0]
 if part in ['LH6764-20','MC1488','MC1489'] or section.endswith('SN74xx') or section.endswith('CD4xxx') or (re.match(r'DIP-\d+',cells[2]) and section in ['IC-Bestand: Diverse','Bestand: Transistoren']):
  if part.startswith('B3CA') or part=='DIP05-1A72-12L':continue
  clean=part.split(' (')[0];number=re.search(r'74(?:LS|ACT|HCT|HC)?(\d+)',clean)
  candidates=[]
  if clean.startswith('CD4'):
   num=re.match(r'CD(\d+)',clean).group(1);candidates=['CD'+num+'B',num,'HEF'+num+'B','CD'+num,'CD'+num+'UB']
  elif number:
   stem=re.sub(r'^(SN|PC|CD)','',clean);stem=re.sub(r'[NEP]$','',stem)
   candidates=[stem,stem+'A',stem+'B']
   if not 'LS' in stem and not any(t in stem for t in ['HC','ACT']):candidates+=['74LS'+number.group(1)]
   if 'HC' in stem or 'ACT' in stem:candidates+=['74LS'+number.group(1)]
  else:candidates=[clean,clean.rstrip('N'),'ULN2004A' if clean=='ULN2004AG' else clean,'ULN2803A' if clean=='ULN2803A' else clean]
  aliases={'LP324N':'LM324','SN74LS164N':'74HC164','L293NE':'L293','LM339AN':'LM339','MAX7219CNG':'MAX7219','MAX7221CNG':'MAX7221','NE555':'NE555P','PCF8574N':'PCF8574P','CD4541':'CD4541BE','MC1488':'MC1488','MC1489':'MC1489'}
  if clean in aliases:candidates.insert(0,aliases[clean])
  if clean=='NE555' and any(r['key']==clean for r in rows):continue # Herstellerbestände teilen eine Referenzkarte
  sym=next((n for n in candidates if n in symbols),None)
  pinrows,lib=get(sym) if sym else ([],None)
  r=dict(part=part,key=clean.replace('/','_'),function=cells[1],category='SN7xxx' if section.endswith('SN74xx') else 'CD4xxx' if section.endswith('CD4xxx') else 'Transistor' if section=='Bestand: Transistoren' else 'Diverse',symbol=sym,library=lib,pins=pinrows,package=cells[2],candidates=candidates)
  rows.append(r)
(base/'inventar.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
(base/'symbolnamen.json').write_text(json.dumps(list(symbols)))
for r in rows:
 nums={p['number'] for p in r['pins']};missing=[]
 if nums:missing=sorted(set(range(1,max(nums)+1))-nums)
 if not r['symbol'] or missing:print(r['key'],'symbol=',r['symbol'],'pins=',len(nums),'missing',missing,'candidates',r['candidates'])
print('Inventar',len(rows),'mit Symbol',sum(bool(r['symbol']) for r in rows))
