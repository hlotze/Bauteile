from pathlib import Path
import json,re,math,textwrap,hashlib,sys,subprocess
import argparse,base64
from collections import defaultdict,Counter
from reportlab.graphics.shapes import Drawing,Group,Rect,Circle,Line,String,Polygon,Path as GPath
from reportlab.graphics import renderPDF,renderSVG
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib import colors
sys.path.insert(0,str(Path(__file__).parent));from maps import MANUAL,UNRESOLVED
from cd_cards import draw_cd
from diverse_cards import draw_diverse
from sn_cards import draw_sn
MM=72/25.4;W=45*MM;H=55*MM;ROOT=Path(__file__).resolve().parents[2]
rows=json.loads((Path(__file__).parent/'inventar.json').read_text())
BLACK=colors.HexColor('#14212b');BLUE=colors.HexColor('#12649b');RED=colors.HexColor('#a52c31');GREY=colors.HexColor('#64717a')
WARN=colors.HexColor('#ae6514')
primary={}
for p in (ROOT/'Datenblaetter').rglob('quellen.json'):
 for rec in json.loads(p.read_text()):
  if rec.get('pdf'):primary[rec['part']]=str((p.parent/rec['pdf']).relative_to(ROOT))
def label(raw):
 raw=re.sub(r'_\{([^}]+)\}',r'\1',raw)
 raw=re.sub(r'~\{([^}]+)\}',r'/\1',raw)
 return raw.replace('Vss','GND').replace('VSS','GND').replace('Vdd','VDD').replace('~','/').replace('Rx1_Cx1','R/C1').replace('Rx2_Cx2','R/C2').replace('RxCx','R/C').replace('Clock','CLK').replace('Reset','RST')
def power(name):return name.upper() in ['VCC','VDD','V+','V-','VEE','GND','OP-VCC']
for r in rows:
 key=r['key'];r['reference']=r.get('symbol') or key;r['sources']=[];r['status']='Referenzkarte'
 if key in MANUAL:
  names,src,page=MANUAL[key];r['pins']=[dict(number=i+1,name=n,role='passive',unit='manual') for i,n in enumerate(names.split())];r['sources']=[dict(file=src,page=page)];r['reference']={'CD4528':'onsemi MC14528BCP','CD4538':'Motorola MC14538BCP (onsemi Ref.)','MC14521BCP':'Motorola MC14521BCP (onsemi Ref.)','MCP3008-I_P':'Microchip MCP3008-I/P','UA741CN':'ST UA741CN (Ref.)','LM324N':'ST LM324N','LP324N':'TI/National LP324N (Ref.)','7487':'SN74H87','CD4513':'MC14513B','74576':'SN74ALS576B','CD4553':'MC14553B'}.get(key,key)
 elif key in UNRESOLVED:r['pins']=[];r['status']='Identifikationskarte';r['unresolved']=UNRESOLVED[key]
 elif r['pins']:
  unique={}
  for p in r['pins']:
   if p['number'] not in unique or len(p['name'])>len(unique[p['number']]['name']):unique[p['number']]=dict(p)
  pins=list(unique.values())
  for p in pins:p['unnamed']=p['name'] in ['~','']
  # Unbenannte Gate-Pins erhalten Einheitenbezeichnungen, z.B. 1A,1B,1Y.
  groups=defaultdict(list)
  for p in pins:
   m=re.search(r'_(\d+)_\d+$',str(p['unit']));u=int(m.group(1)) if m else 1
   groups[u].append(p)
  for u,ps in groups.items():
   inp=sorted([p for p in ps if p['name'] in ['~',''] and p['role'] in ['input','passive']],key=lambda p:p['number'])
   out=[p for p in ps if p['name'] in ['~',''] and p['role'] in ['output','open_collector','tri_state']]
   for j,p in enumerate(inp):p['name']=str(u)+chr(65+j)
   for p in out:p['name']=str(u)+'Y'
  duplicates=Counter(p['name'] for p in pins if p['name'] not in ['~','NC','VSS','VDD','Vdd','Vss','VCC','GND'])
  for p in pins:
   if duplicates[p['name']]>1:
    m=re.search(r'_(\d+)_\d+$',str(p['unit']));p['name']+='-'+(m.group(1) if m else '1')
   if p.get('shape') in ['inverted','inverted_clock'] and (p['role']=='input' or not p.get('unnamed')) and not p['name'].startswith(('~','/')):p['name']='/'+p['name']
   if p['name'] in ['+','-'] or re.match(r'^[+-]-\d+$',p['name']):
    pol=p['name'][0];unit=p['name'].split('-')[-1] if len(p['name'])>1 else '';p['name']='IN'+unit+pol
   p['name']=label(p['name'])
  expected=int(re.search(r'DIP-(\d+)',r['package']).group(1)) if re.search(r'DIP-(\d+)',r['package']) else math.ceil(max(p['number'] for p in pins)/2)*2
  for i in range(1,expected+1):
   if i not in unique:pins.append(dict(number=i,name='NC',role='no_connect',unit='NC'))
  r['pins']=sorted(pins,key=lambda p:p['number'])
  r['sources']=[dict(file='scripts/kaertchen/'+r['library'],symbol=r['symbol'])]
  if key in primary:r['sources'].append(dict(file=primary[key]))
  if 'HC' in str(r['symbol']) and 'LS' in key:r['reference']=re.sub(r'N$','',key)+' (Pinref. '+r['symbol']+')'
 if not r['pins'] and key not in UNRESOLVED:raise RuntimeError('Ohne Pinquelle: '+key)
 if r['pins']:
  r['pin_count']=len(r['pins']);assert {p['number'] for p in r['pins']}==set(range(1,r['pin_count']+1)),key
  assert r['pin_count']%2==0 and r['pin_count']<=24,(key,r['pin_count'])
  assert not any(p['name'] in ['~','/',''] for p in r['pins']),(key,r['pins'])
 else:r['pin_count']=0
 if key=='CD4068':
  for p in r['pins']:
   if p['number']==1:p['name']='/Y'
   if p['number']==13:p['name']='Y'
 r['pitch_mm']=2.54 if r['pin_count']==24 else 5.08
 r['svg']=f"images/{r['category']}/{key}_karte_45x55mm.svg";r['pdf']=r['svg'].replace('.svg','.pdf')

def draw(r):
 if r['category']=='CD4xxx':return draw_cd(r)
 if r['category']=='Diverse':return draw_diverse(r)
 if r['category']=='SN7xxx':return draw_sn(r)
 d=Drawing(W,H)
 def rect(x,y,w,h,fill=None,stroke=BLACK,width=.2):d.add(Rect(x*MM,(55-y-h)*MM,w*MM,h*MM,fillColor=fill,strokeColor=stroke,strokeWidth=width*MM))
 def line(x,y,x2,y2,c=BLACK,width=.18):d.add(Line(x*MM,(55-y)*MM,x2*MM,(55-y2)*MM,strokeColor=c,strokeWidth=width*MM))
 def text(x,y,t,size=6.5,c=BLACK,anchor='start',bold=False):
  d.add(String(x*MM,(55-y)*MM,t,fontName='Helvetica-Bold' if bold else 'Helvetica',fontSize=size,fillColor=c,textAnchor=anchor))
 def fit(x,y,t,width,size=6.5,c=BLACK,anchor='start',bold=False):
  font='Helvetica-Bold' if bold else 'Helvetica'
  size=min(size,width*MM/max(stringWidth(t,font,size),.01)*size);text(x,y,t,size,c,anchor,bold)
 rect(.25,.25,44.5,54.5,colors.white,colors.HexColor('#bac4cc'),.1)
 fit(22.5,3.4,r['key'],41,10,anchor='middle',bold=True)
 # The title is repeated at the bottom as on the user's example cards.
 fit(22.5,53.9,r['key']+' | '+str(r['pin_count'])+' Pins' if r['pins'] else r['key'],13 if r['pin_count']>=20 else 41,6.2,anchor='middle',bold=True)
 if not r['pins']:
  rect(3,10,39,31,colors.HexColor('#fff1dc'),WARN)
  text(22.5,17,'ZUORDNUNG OFFEN',8,WARN,'middle',True)
  text(22.5,24,'Keine Pinbelegung',7.5,BLACK,'middle')
  text(22.5,29,'Nicht zum Verdrahten verwenden',6.7,BLACK,'middle')
  for j,l in enumerate(textwrap.wrap(r['unresolved'],27)):text(22.5,35+j*3,l,6,GREY,'middle')
  return d
 n=r['pin_count'];half=n//2;pitch=r['pitch_mm'];first=6.4
 r['first_pin_y_mm']=first
 for p in r['pins']:
  num=p['number'];left=num<=half;row=num-1 if left else n-num;y=first+row*pitch;name=p['name'];role=p['role']
  ground=name.upper()=='GND';supply=power(name) and not ground;output=role in ['output','open_collector','open_emitter','tri_state'] or bool(re.match(r'^/?(Q\d|\dY|[a-g]$|CARRY|OF|F-OUT|.*-OUT)',name))
  c=BLUE if output else GREY if name=='NC' else BLACK
  fill=colors.HexColor('#ffdfdf') if supply else colors.HexColor('#d8edf8') if ground else None
  if fill:rect(.5 if left else 31,y-1.5,13.5,3.1,fill,None)
  x=2.2 if left else 42.8
  d.add(Circle(x*MM,(55-y)*MM,(1.05 if n==24 else 1.5)*MM,strokeColor=RED if supply else BLUE if ground else BLACK,strokeWidth=.25*MM,fillColor=colors.white))
  text(x,y+(.55 if n==24 else .7),str(num),5 if n==24 else 6.5,RED if supply else BLUE if ground else BLACK,'middle',True)
  fit(4.3 if left else 40.7,y+.7,name,10.6,6.7,c,'start' if left else'end',True)
  line(3.7 if left else 41.3,y,4.1 if left else 40.9,y)
 # Center function content. IEC gate symbols plus truth table where applicable.
 f=r['function'];gate=None
 for g in ['XNOR','XOR','NAND','NOR','AND','OR']:
  if re.search(r'\b'+g+r'-Gatter',f):gate=g;break
 if 'AND-OR' in f or r['key']=='CD4068':gate=None
 if gate:
  m=re.search(r'^(\d+)',f);count=int(m.group(1)) if m else 1;count=min(count,4)
  cy=11
  for i in range(count):
   y=cy+i*5.1;rect(18,y-2,9,4,None,BLACK)
   text(22.5,y+.8,{'AND':'&','NAND':'&','OR':'>=1','NOR':'>=1','XOR':'=1','XNOR':'=1'}[gate],8,BLACK,'middle')
   line(16.5,y-1,18,y-1);line(16.5,y+1,18,y+1);line(27,y,28.5,y)
   if gate in ['NAND','NOR','XNOR']:d.add(Circle(27.5*MM,(55-y)*MM,.5*MM,fillColor=colors.white,strokeColor=BLACK,strokeWidth=.15*MM))
   text(15.9,y+.7,str(i+1),5,GREY,'end')
  text(22.5,34,'A B | Y',6.5,BLACK,'middle',True)
  truth={'NAND':[1,1,1,0],'AND':[0,0,0,1],'NOR':[1,0,0,0],'OR':[0,1,1,1],'XOR':[0,1,1,0],'XNOR':[1,0,0,1]}[gate]
  for i,v in enumerate(truth):text(22.5,37+i*2.6,f'{i//2} {i%2} | {v}',6.2,BLACK,'middle')
  # A two-input table is inappropriate for gates with more than two inputs.
  if 'je 2 Eingängen' not in f:
   d=draw_block_replacement(d,r,gate)
 elif r['key']=='7487':
  for i,t in enumerate(['B C | Y','0 0 | /A','0 1 | A','1 0 | 1','1 1 | 0']):text(22.5,17+i*4,t,6.8,BLACK,'middle',i==0)
 elif r['key']=='CD4015':
  for y,unit in [(13,'A'),(28,'B')]:
   rect(16,y,13,10,colors.HexColor('#f5f8fa'));text(22.5,y+3,'4-Bit '+unit,7,BLACK,'middle',True)
   fit(22.5,y+6,'DATA -> Q1..Q4',12,5.3,BLUE,'middle');text(22.5,y+9,'CLK / RST',6,BLACK,'middle')
   line(15,y+5,16,y+5);line(29,y+5,30,y+5)
  fit(22.5,42,'CLK steigt: schieben',13,5.2,BLACK,'middle');text(22.5,45,'RST=1: Q=0',6,BLACK,'middle')
 else:
  rect(16,11,13,30,colors.HexColor('#f5f8fa'),colors.HexColor('#8796a1'),.15)
  short=f.replace('mit je','je').replace('nichtinvertierende','nichtinv.').replace('invertierende','invert.').replace('unabhängige','separate').replace('Schieberegister','Schiebe-Reg.').replace('Ausgänge','Ausg.').replace('positive Taktflanke','CLK steigt').replace('negative Taktflanke','CLK fällt')
  lines=textwrap.wrap(short,13,break_long_words=True)[:8]
  for i,t in enumerate(lines):fit(22.5,15+i*3,t,12,6.1,anchor='middle',bold=(i==0))
  # Compact operation notes are metadata-backed; do not invent timing truth tables.
  if 'Open Collector' in f:text(22.5,45,'OC: Pull-up nötig',5.6,BLUE,'middle')
  elif '3-State' in f and r['key']=='CD4043':fit(22.5,45,'EN=0: hochohmig',13,5.3,BLUE,'middle')
  elif '3-State' in f:fit(22.5,45,'OE sperrt: hochohmig',13,5.3,BLUE,'middle')
  elif 'Analog' in f:fit(22.5,45,'Signalgrenzen prüfen',13,5.3,BLACK,'middle')
  elif 'Zähler' in f:fit(22.5,45,'CLK / RESET beachten',13,5.3,BLACK,'middle')
  elif 'RS-Latch' in f:fit(22.5,45,'S/R aktiv wie markiert',13,5.1,BLACK,'middle')
 if n<20:
  fit(22.5,49.5,'Ref: '+r['reference'],40,4.8,GREY,'middle')
 else:fit(22.5,49,'Ref: '+r['reference'],13,4.5,GREY,'middle')
 return d

def draw_block_replacement(d,r,gate):
 # Remove central graphics and recreate a correct multi-input functional block.
 # Keep only the frame, title and all pin decorations up to the start of center content.
 n=r['pin_count'];keep=3+sum(5+(1 if power(p['name']) else 0) for p in r['pins'])
 # central two-input table replaced by a white center cover, no changes to pin columns.
 d.add(Rect(15*MM,6*MM,15*MM,40*MM,fillColor=colors.white,strokeColor=None))
 for i,t in enumerate(textwrap.wrap(r['function'],15)):
  d.add(String(22.5*MM,(55-13-i*3)*MM,t,fontName='Helvetica',fontSize=6.2,fillColor=BLACK,textAnchor='middle'))
 d.add(String(22.5*MM,12*MM,'Y = '+gate+'(A..)',fontName='Helvetica',fontSize=6.3,fillColor=BLACK,textAnchor='middle'))
 return d

if __name__=='__main__':
 parser=argparse.ArgumentParser(description='Experimentierkarten und A4-Druckbogen erstellen')
 parser.add_argument('--category',help='Nur Einzelkarten dieser Kategorie neu schreiben; A4 enthält weiterhin alle Karten')
 parser.add_argument('--part',action='append',help='Nur diese Einzelkarte neu schreiben; mehrfach verwendbar; A4 enthält alle Karten')
 args=parser.parse_args()
 existing={r['key']:r for r in json.loads((ROOT/'images/karten.json').read_text())} if (ROOT/'images/karten.json').exists() else {}
 for r in rows:
  if r['pins']:r['first_pin_y_mm']=6.4
  r['png']=r['svg'].replace('.svg','.png')
  if (args.category and r['category']!=args.category) or (args.part and r['key'] not in args.part):
   if r['key'] in existing:r.update(existing[r['key']])
   r['sha256_svg']=hashlib.sha256((ROOT/r['svg']).read_bytes()).hexdigest()
   continue
  d=draw(r);p=ROOT/r['svg'];p.parent.mkdir(parents=True,exist_ok=True)
  svg=renderSVG.drawToString(d)
  # ReportLab links raster diagrams by filename. Embed them so each SVG is
  # self-contained and can be moved or opened outside the repository.
  def embed_image(match):
   if match.group(2).startswith('data:'):return match.group(0)
   path=Path(match.group(2))
   if path.is_file():
    data=base64.b64encode(path.read_bytes()).decode('ascii')
    return match.group(1)+'data:image/png;base64,'+data+match.group(3)
   return match.group(0)
  svg=re.sub(r'((?:xlink:)?href=")([^"]+)(")',embed_image,svg)
  svg=re.sub(r'<svg\s+', '<svg ',svg,count=1)
  svg=re.sub(r'width="[^"]+"', 'width="45mm"',svg,count=1);svg=re.sub(r'height="[^"]+"','height="55mm"',svg,count=1)
  svg=re.sub(r'viewBox="[^"]+"',f'viewBox="0 0 {W:.9f} {H:.9f}"',svg,count=1)
  p.write_text(svg);renderPDF.drawToFile(d,str(ROOT/r['pdf']))
  subprocess.run(['pdftoppm','-singlefile','-r','300','-png',str(ROOT/r['pdf']),str((ROOT/r['png']).with_suffix(''))],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
  from PIL import Image
  im=Image.open(ROOT/r['png']);im.save(ROOT/r['png'],dpi=(300,300))
  r['sha256_svg']=hashlib.sha256(p.read_bytes()).hexdigest()
 (ROOT/'images/karten.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
 # A4 print sheets: 4 columns x 4 rows; no page scaling required.
 out=ROOT/'images/IC_Karten_A4.pdf';c=canvas.Canvas(str(out),pagesize=(210*MM,297*MM))
 for i,r in enumerate(rows):
  j=i%16
  if j==0:
   if i:c.showPage()
   c.setFont('Helvetica',8);c.drawString(15*MM,285*MM,'IC-Karten 45 x 55 mm | Druck: 100 % / tatsächliche Größe')
  col=j%4;row=j//4;x=(15+col*46)*MM;y=(297-22-(row+1)*56)*MM
  renderPDF.draw(draw(r),c,x,y)
  c.setStrokeColor(colors.HexColor('#c4c4c4'));c.setLineWidth(.25)
  for dx,dy in [(0,0),(W,0),(0,H),(W,H)]:
   c.line(x+dx-2,y+dy,x+dx+2,y+dy);c.line(x+dx,y+dy-2,x+dx,y+dy+2)
 c.save()
 print(len(rows),'Karten erstellt; davon',sum(r['status']=='Identifikationskarte' for r in rows),'Identifikationskarten.')
