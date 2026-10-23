#!/usr/bin/env python3
"""45 x 55 mm symbol/package cards. Read stock from SQLite; update card links only."""
from pathlib import Path
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import argparse,base64,hashlib,html,json,re,sqlite3,subprocess,tempfile

ROOT=Path(__file__).resolve().parents[2]
CONFIG=Path(__file__).with_name('anschlusskarten.json')
OUT=ROOT/'images/Anschlusskarten'
FOLDERS={'Transitor':'Transistor','MOSFET':'MOSFET','Spannungsregler':'Spannungsregler','Triac_Thyristor':'Triac_Thyristor','Diode':'Dioden'}
GREEN='#006c46';BLUE='#155e87';INK='#172b35';GRAY='#53646b';WARN='#a1540b'

def esc(s):return html.escape(str(s),quote=True)

def text(x,y,value,size=2,color=INK,bold=False,anchor='middle'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{700 if bold else 400}" text-anchor="{anchor}">{esc(value)}</text>'

def line(x1,y1,x2,y2,color=INK,width=.35):
    return f'<path d="M{x1},{y1} L{x2},{y2}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round"/>'

def path(d,fill='none',stroke=INK,width=.35):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round"/>'

def rect(x,y,w,h,fill,stroke='none',radius=0,width=.25):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>'

def circle(x,y,r,fill='white',stroke=INK,width=.3):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>'

def arrow(a,b,color=INK,size=1.4):
    import math
    dx=b[0]-a[0];dy=b[1]-a[1];length=math.hypot(dx,dy);ux=dx/length;uy=dy/length
    p=(b[0]-size*ux,b[1]-size*uy);off=size*.42
    return path(f'M{b[0]},{b[1]} L{p[0]-off*uy},{p[1]+off*ux} L{p[0]+off*uy},{p[1]-off*ux} Z',color,color,.12)

def bjt(pnp=False):
    s=circle(22.5,16.2,6.2,'none',GREEN,.28)
    s+=line(19.8,12.1,19.8,20.3,width=.65)+line(12,16.2,19.8,16.2)
    s+=path('M19.8,14 L25.5,10.8 L25.5,8.7')+path('M19.8,18.4 L25.5,21.7 L25.5,24')
    s+=arrow((24.5,21.1),(21.6,19.45)) if pnp else arrow((21,19.1),(24.8,21.3))
    return s+text(10.5,17,'B',2.2,GREEN,True)+text(29,10.5,'C',2.2,BLUE,True)+text(29,24,'E',2.2,INK,True)

def darlington(pnp=False):
    s=path('M12,14 L17,14 M17,10.5 L17,17.5 M17,12 L20.5,9.5 L28,9.5 L28,8.5 M17,16 L20.5,18.5 L23,18.5 M23,15 L23,22 M23,16.5 L28,13 L28,9.5 M23,20.5 L28,23.5 L28,24.5')
    s+=arrow((20,18.1),(18,16.7),size=1.2) if pnp else arrow((18,16.7),(20.1,18.2),size=1.2)
    s+=arrow((27.3,23.1),(24,21.1),size=1.3) if pnp else arrow((24,21.1),(27.3,23.1),size=1.3)
    return s+text(10.5,14.8,'B',2.2,GREEN,True)+text(31,10,'C',2.2,BLUE,True)+text(31,24.5,'E',2.2,INK,True)

def mosfet(pmos=False):
    s=line(12,17.5,20,17.5)+line(20,12.5,20,21,width=.6)
    for y in (11.2,15.7,20.2):s+=line(22.3,y,22.3,y+2.6,width=.55)
    s+=path('M22.3,12.5 L28.2,12.5 L28.2,8.8 M22.3,21.5 L28.2,21.5 L28.2,24 M22.3,17 L26.1,17 L26.1,21.5')
    s+=arrow((22.8,17),(25.9,17)) if pmos else arrow((25.8,17),(22.5,17))
    return s+text(10.5,18.3,'G',2.2,GREEN,True)+text(31,10,'D',2.2,BLUE,True)+text(31,24,'S',2.2,INK,True)

def regulator(adjust=False):
    s=rect(16,12.5,13,8.8,'white',GREEN,1,.4)+line(9,16.5,16,16.5)+line(29,16.5,36,16.5)+line(22.5,21.3,22.5,24)
    return s+text(9.5,14.5,'IN',2,GREEN,True)+text(35,14.5,'OUT',2,BLUE,True)+text(22.5,19,'REG',2,INK,True)+text(22.5,26,'ADJ' if adjust else 'GND',1.8,INK,True)

def shunt():
    s=path('M24,8.7 L24,13 M21,13 L27,13 L28,11.8 M21,13 L20,14.2 M21,21 L27,21 L24,14 Z M24,21 L24,24 M12,18.5 L20.2,18.5 L22,17.8')
    return s+text(29,10,'K',2.2,BLUE,True)+text(29,24,'A',2.2,INK,True)+text(10,19.2,'REF',1.9,GREEN,True)

def triac():
    s=path('M24,8.7 L24,11 M19.5,11 L28.5,11 M19.5,21.5 L28.5,21.5 M24,21.5 L24,24 M19.5,11 L23.5,11 L21.5,20.7 Z M24.5,21.5 L28.5,21.5 L26.5,11.8 Z M12,20.5 L18,20.5 L21.05,18.5')
    return s+text(31.5,10,'MT2',1.9,BLUE,True)+text(31.5,24,'MT1',1.9,INK,True)+text(10.5,21.2,'G',2.2,GREEN,True)

def diode():
    return path('M10,16 L19,16 M19,12 L19,20 L26,16 Z M26,11.8 L26,20.2 M26,16 L35,16')+text(10,12,'A',2.2,GREEN,True)+text(35,12,'K',2.2,BLUE,True)

def symbol(r):
    k=r['kind']
    if k=='quad-npn':
        s=''
        for i,x in enumerate([-2.8,7.8,18.4,29]):
            s+=f'<g transform="translate({x},7.5) scale(.45)">{bjt()}</g>'+text(x+10,21.5,'Q'+str(i+1),1.6,GRAY)
        return s
    if k.endswith('-darlington'):return darlington(k.startswith('pnp'))
    if k in ('npn','pnp'):return bjt(k=='pnp')
    if k in ('nmos','pmos'):return mosfet(k=='pmos')
    if k=='regulator':return regulator(r['part']=='LM317')
    return {'triac':triac,'shunt':shunt,'diode':diode}[k]()

def package(r):
    pkg=r['package'];pins=r['pins'];s=''
    if pkg in ('TO-18','TO-39'):
        # ST bottom view, locating tab at upper left. Lead positions are explicit
        # in the reviewed mapping; they must never be inferred from a TO-92 row.
        s+=path('M17.8,33.6 L15.8,31.6 L14.8,32.6 L16.7,34.5', '#bdc9ce',INK,.25)
        s+=circle(22.5,38,6.4,'#cad4d9',INK,.35)+circle(22.5,38,5.7,'#e8edf0','#8b9da6',.2)
        for p in pins:
            x,y=p['x'],p['y'];s+=circle(x,y,.7,'#71838d',INK,.2)
            if p['signal']=='E':s+=line(x-.8,y,13,y,GRAY,.22)+text(11.4,y+.6,f'{p["number"]} E',2.15,GREEN,True,'end')
            elif p['signal']=='B':s+=line(x+.8,y,32,y,GRAY,.22)+text(33,y+.6,f'{p["number"]} B',2.15,GREEN,True,'start')
            else:s+=line(x-.8,y,13,y,GRAY,.22)+text(11.4,y+.6,f'{p["number"]} C',2.15,BLUE,True,'end')
        s+=text(22.5,48,'Metallgehäuse · Kollektor',1.65,GRAY)
        return s
    if pkg=='DIP-14':
        s+=rect(17,31.5,11,16,'#263841',INK,.7)+path('M20.8,31.5 A1.7,1.7 0 0 0 24.2,31.5','none','#c6d1d7',.3)
        for p in pins:
            n=p['number'];left=n<=7;y=33+(n-1 if left else 14-n)*2
            s+=rect(15 if left else 28,y-.4,2,.8,'#b6c1c7',INK,0,.13)
            s+=text(14 if left else 31,y+.6,f'{n} {p["signal"]}' if left else f'{p["signal"]} {n}',1.6,BLUE,True,'end' if left else 'start')
        return s
    if r['kind']=='diode':
        s+=line(7,36.5,17,36.5,'#7a858b',.8)+line(28,36.5,38,36.5,'#7a858b',.8)
        s+=rect(17,33.8,11,5.4,'#df9c54' if pkg=='DO-35' else '#303d43',INK,1,.3)
        s+=rect(25.5,33.9,1.2,5.2,'#1a2024' if pkg=='DO-35' else '#d0dce3')
        s+=text(9,44,'A',2.7,GREEN,True)+text(36,44,'K',2.7,BLUE,True)+text(26.1,42,'Ring = K',1.7,GRAY)
        return s
    positions=[16.7,22.5,28.3]
    if pkg=='TO-92':
        s+=path('M16,40 L16,34 Q16,31 19,31 L26,31 Q29,31 29,34 L29,40 Z','#273b45',INK,.35)
        s+=path('M17,33 Q22.5,30.8 28,33','none','#60757f',.45)+line(17,39,28,39,'#5f747e',.25)
    elif pkg in ('TO-126','SOT-82'):
        s+=rect(15.6,31,13.8,9,'#293c46',INK,.6,.35)
        if pkg=='TO-126':s+=circle(22.5,33.5,1.3,'white','#80929a',.45)
        else:s+=rect(17,31.7,11,3.2,'#9caeb6',INK,.4,.2)
    else:
        s+=rect(15.4,31,14.2,7,'#b9c6cc',INK,.35,.3)+circle(22.5,33.4,1.4,'white','#647985',.3)
        s+=rect(15.4,35.1,14.2,5.1,'#263a44',INK,.3,.35)+line(16.5,36.3,28.5,36.3,'#536b77',.3)
    for x,p in zip(positions,pins):
        s+=rect(x-.4,40,.8,4.4,'#afbdc5',INK,0,.15)
        s+=text(x,46,str(p['number']),1.65,GRAY)
        s+=text(x,49,p['signal'],2.15 if len(p['signal'])>2 else 2.4,BLUE if p['signal'] in ('C','D','OUT','K','MT2') else GREEN if p['signal'] in ('B','G','IN','REF','ADJ') else INK,True)
    if r['tab']:
        s+=line(27,32.2,33,32.2,GRAY,.18)+text(35,34.4,'Fahne',1.3,GRAY)+text(35,36.5,r['tab'],1.4,GRAY,True)
    return s

TITLES={'npn':'NPN','pnp':'PNP','npn-darlington':'NPN-Darlington','pnp-darlington':'PNP-Darlington','quad-npn':'4 × NPN','nmos':'N-Kanal-MOSFET','pmos':'P-Kanal-MOSFET','regulator':'Spannungsregler','shunt':'Shuntreferenz','triac':'TRIAC','diode':'Diode'}

def card_body(r):
    s=rect(.3,.3,44.4,54.4,'white',GREEN,1,.3)
    s+=text(22.5,4.6,r['part'],3.15,GREEN,True)+text(22.5,7.5,TITLES[r['kind']],1.85,GRAY)
    s+=symbol(r)+line(3,27.5,42,27.5,'#c6d9d1',.18)
    caption=f'{r["package"]} · {r["view"]}'
    s+=text(22.5,30,caption,1.45,GRAY)+package(r)
    footer=f'Ref.: {r["reference"]} · PDF S. {r["source_page"]}'
    # The exact PDF/page and hash are also in the machine-readable manifest.
    s+=text(22.5,51.2,footer,min(1.45,59/max(len(footer),1)),GRAY)
    warnings=r['warnings'] or ['Hersteller / Variante abgleichen']
    for i,w in enumerate(warnings[:2]):s+=text(22.5,52.8+i*1.35,w,min(1.4,61/max(len(w),1)),WARN)
    return s

def svg_document(body,width=45,height=55):
    return f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{width}mm" height="{height}mm" viewBox="0 0 {width} {height}"><g font-family="DejaVu Sans, sans-serif">{body}</g></svg>\n'

def render(r):
    folder=OUT/FOLDERS[r['type']];folder.mkdir(parents=True,exist_ok=True)
    base=folder/(r['part']+'_anschluss_45x55mm');svg=base.with_suffix('.svg');svg.write_text(svg_document(card_body(r)))
    for fmt in ['pdf','png']:
        cmd=['rsvg-convert','-f',fmt]
        if fmt=='png':cmd+=['-d','300','-p','300']
        subprocess.run(cmd+[str(svg),'-o',str(base.with_suffix('.'+fmt))],check=True,stderr=subprocess.PIPE)
    return {fmt:str(base.with_suffix('.'+fmt).relative_to(ROOT)) for fmt in ['svg','pdf','png']}

def print_sheets(records):
    out=ROOT/'images/Bauteil_Anschlusskarten_A4.pdf'
    with tempfile.TemporaryDirectory(prefix='anschlusskarten-') as tmp:
        pages=[]
        for page,start in enumerate(range(0,len(records),16)):
            body=rect(0,0,210,297,'white')+text(10.5,15,'Anschlusskarten · 45 × 55 mm',4,GREEN,True,'start')+text(10.5,21,'Druck: 100 % / tatsächliche Größe · keine Seitenanpassung',2.4,GRAY,False,'start')
            for j,r in enumerate(records[start:start+16]):
                x=10.5+(j%4)*48;y=30+(j//4)*58
                body+=f'<g transform="translate({x},{y})">{card_body(r)}</g>'
                for cx,cy in [(x,y),(x+45,y),(x,y+55),(x+45,y+55)]:
                    body+=line(cx-1,cy,cx+1,cy,'#a2b5ad',.13)+line(cx,cy-1,cx,cy+1,'#a2b5ad',.13)
            body+=text(10.5,280,'Pinfolge gilt für die genannte Referenz und Ansicht. Nicht maßstäbliche Gehäusebilder.',2.1,GRAY,False,'start')+text(199.5,280,f'{page+1} / {(len(records)+15)//16}',2.1,GRAY,False,'end')
            svg=Path(tmp)/f'sheet{page}.svg';pdf=svg.with_suffix('.pdf');svg.write_text(svg_document(body,210,297));subprocess.run(['rsvg-convert','-f','pdf',str(svg),'-o',str(pdf)],check=True,stderr=subprocess.PIPE);pages.append(str(pdf))
        subprocess.run(['pdfunite',*pages,str(out)],check=True,stderr=subprocess.PIPE)
    return out

def update_links(records,paths,before,columns):
    lookup={(r['type'],r['part']):paths[r['part']] for r in records};md=ROOT/'Bauteile.md';old=md.read_text();lines=[];category=None;headers=None;seen=set()
    categories={'Bestand: Transistoren':'Transitor','Bestand: MOSFETs':'MOSFET','Bestand: Triacs und Thyristoren':'Triac_Thyristor','Bestand: Spannungsregler und Spannungsreferenzen':'Spannungsregler','Bestand: Dioden':'Diode'}
    insert=False;card_index=None
    for line0 in old.splitlines():
        line1=line0
        if line1.startswith('## '):category=categories.get(line1[3:]);headers=None
        if category and line1.startswith('|'):
            cells=[c.strip() for c in re.split(r'(?<!\\)\|',line1)[1:-1]]
            if headers is None:
                headers=cells.copy();insert='Karte' not in headers;card_index=headers.index('Beispielschaltungen') if insert else headers.index('Karte')
                if insert:cells.insert(card_index,'Karte')
            elif all(re.fullmatch(r':?-+:?',c) for c in cells):
                if insert:cells.insert(card_index,'---')
            else:
                assert len(cells)==len(headers),(category,cells[0]);key=(category,cells[0]);links=lookup[key];seen.add(key)
                v=' / '.join(f'[{label}]({links[ext]})' for ext,label in [('png','Bild'),('pdf','PDF'),('svg','SVG')])
                if insert:cells.insert(card_index,v)
                else:cells[card_index]=v
            line1='| '+' | '.join(cells)+' |'
        lines.append(line1)
    assert seen==set(lookup),(set(lookup)-seen)
    newmd='\n'.join(lines)+'\n'
    # Only the three card link fields may change in SQLite.
    with sqlite3.connect(ROOT/'Bauteile.db') as db:
        for key,links in lookup.items():
            assert db.execute('UPDATE Bauteile SET Karte_PNG=?,Karte_PDF=?,Karte_SVG=? WHERE Type=? AND Bezeichnung=?',(links['png'],links['pdf'],links['svg'],*key)).rowcount==1
        after={r[:2]:r for r in db.execute('SELECT * FROM Bauteile')};assert before.keys()==after.keys()
        for key,row in before.items():
            target=list(row)
            if key in lookup:
                for col,ext in [('Karte_PNG','png'),('Karte_PDF','pdf'),('Karte_SVG','svg')]:target[columns.index(col)]=lookup[key][ext]
            assert after[key]==tuple(target),key
        assert db.execute('PRAGMA integrity_check').fetchone()==('ok',)
        md.write_text(newmd)
    return len(seen)

def write_index(records,paths,pending):
    s=['# Anschlusskarten 45 × 55 mm','','[A4-Druckbogen](../Bauteil_Anschlusskarten_A4.pdf) · **100 % / tatsächliche Größe** · keine Seitenanpassung.','','Oben steht ausschließlich das Schaltplansymbol, darunter eine schematische Gehäusezeichnung mit Anschlussnamen und Pinnummern. Die Gehäuse sind nicht maßstäblich. „Vorne, flache Seite“ heißt: Beschriftung bzw. abgeflachte Gehäuseseite zum Betrachter, Anschlussdrähte nach unten. Bei DIP gilt die Draufsicht.','','Die konkrete Datenblattreferenz und Blickrichtung bestimmen die Pinfolge. Pinnummern können sich zwischen Herstellern unterscheiden, auch bei gleicher physischer Anschlussfolge. Kollektor-/Drainfahnen sowie Ein-/Ausgangsverbindungen von Reglerfahnen sind beschriftet.','','**Ungeklärte Zuordnungen:** 2N2222 zeigt ausdrücklich nur P2N2222A, IRF510N nur IRF510 ohne N. S8050/S8550/S901x zeigen SS-Referenzen. Diese Karten bestätigen keine Pinbelegung eines anders beschrifteten oder unbekannten Herstellertyps. Bei BTA06 bleibt das fehlende Suffix offen; bei TS7805 wird die TO-220-CZ-Referenz mit Hinweis auf die isolierte CI-Bauform gezeigt.','','TL431A ist eine Shuntreferenz mit REF, A und K; LM317 hat ADJ anstelle von GND. Triacs tragen MT1, MT2 und G (MT1/MT2 entsprechen A1/A2). Bei Dioden bezeichnet K die durch einen Ring markierte Kathode.','','Alle Bestandsdaten bleiben erhalten; der Generator aktualisiert ausschließlich Kartenlinks. Quellen, Seiten, Pinfolgen und PDF-Prüfsummen: [karten.json](karten.json). [Generator und Zuordnungen](../../scripts/kaertchen/README.md).','',f'**{len(records)} Karten**, jeweils als SVG, PDF und PNG (300 dpi).','','| Typ | Symbol / Gehäuse | Vorschau | Druck | Vektor | Pinreferenz |','| --- | --- | --- | --- | --- | --- |']
    for r in records:
        ps=paths[r['part']];rel=lambda e:str(Path(ps[e]).relative_to('images/Anschlusskarten'))
        s.append(f'| {r["part"]} | {TITLES[r["kind"]]} / {r["package"]} | [PNG]({rel("png")}) | [PDF]({rel("pdf")}) | [SVG]({rel("svg")}) | [{r["reference"]}, S. {r["source_page"]}](../../{r["source_file"]}#page={r["source_page"]}) |')
    if pending:
        s+=['','## Noch ohne geprüfte Anschlusskarte','',f'{len(pending)} weitere Bestandseinträge haben noch keine bestätigte Gehäuse-/Pinreferenz. Mengen und Kennwerte stehen weiterhin in Bauteile.md und der Datenbank. [Offene Zuordnungen](offene_zuordnungen.json).']
    (OUT/'README.md').write_text('\n'.join(s)+'\n')

def preview(records):
    chosen=['BC141','BC161','BC238B','2N2222A','BC639','BC640','BC879','KSP44','BD135-10','IRLZ44N','L7805CV','TL431A']
    byname={r['part']:r for r in records};body=rect(0,0,192,188,'#eef4f0')
    for i,name in enumerate(chosen):body+=f'<g transform="translate({2+(i%4)*48},{2+(i//4)*62})">{card_body(byname[name])}</g>'
    svg=OUT/'Vorschau.svg';svg.write_text(svg_document(body,192,188));subprocess.run(['rsvg-convert','-w','1536',str(svg),'-o',str(OUT/'Vorschau.png')],check=True,stderr=subprocess.PIPE)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--part',action='append',help='Nur ausgewählte Einzelkarten neu zeichnen; Metadaten/Druckbogen enthalten alle Karten');args=parser.parse_args()
    config=json.loads(CONFIG.read_text());records=config['cards'];pending=config.get('pending',[])
    order={'Transitor':0,'MOSFET':1,'Triac_Thyristor':2,'Spannungsregler':3,'Diode':4}
    records.sort(key=lambda r:(order[r['type']],r['part']))
    assert len({(r['type'],r['part']) for r in records})==len(records)
    with sqlite3.connect('file:'+str(ROOT/'Bauteile.db')+'?mode=ro',uri=True) as db:
        before={r[:2]:r for r in db.execute('SELECT * FROM Bauteile')};columns=[r[1] for r in db.execute('PRAGMA table_info(Bauteile)')]
    expected={key for key in before if key[0] in FOLDERS}
    mapped={(r['type'],r['part']) for r in records};deferred={(r['type'],r['part']) for r in pending}
    assert len(deferred)==len(pending) and not mapped&deferred
    assert expected==mapped|deferred,'Inventar und Zuordnungen abgleichen'
    for key in deferred:
        assert all(before[key][columns.index(c)] is None for c in ('Karte_PNG','Karte_PDF','Karte_SVG')),'Offene Zuordnung hat bereits Kartenlinks'
    for r in records:
        assert hashlib.sha256((ROOT/r['source_file']).read_bytes()).hexdigest()==r['source_sha256'],r['part']
        if r['package']!='DIP-14' and r['kind']!='diode':assert len(r['pins'])==3
        assert len({p['number'] for p in r['pins']})==len(r['pins']) or r['kind']=='diode'
    paths={};selected=[]
    for r in records:
        base=OUT/FOLDERS[r['type']]/(r['part']+'_anschluss_45x55mm');paths[r['part']]={ext:str(base.with_suffix('.'+ext).relative_to(ROOT)) for ext in ['svg','pdf','png']}
        if not args.part or r['part'] in args.part:selected.append(r)
        else:assert all((ROOT/p).is_file() for p in paths[r['part']].values()),r['part']
    with ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(render,selected))
    out=print_sheets(records);write_index(records,paths,pending);preview(records)
    (OUT/'offene_zuordnungen.json').write_text(json.dumps(pending,ensure_ascii=False,indent=2)+'\n')
    manifest=[dict(r,files=paths[r['part']],sha256_svg=hashlib.sha256((ROOT/paths[r['part']]['svg']).read_bytes()).hexdigest()) for r in records]
    (OUT/'karten.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    count=update_links(records,paths,before,columns)
    print(f'{len(selected)} Einzelkarten gezeichnet, {count} Karten verlinkt. A4: {out.relative_to(ROOT)}. Bestand unverändert; DB-Integrität ok.')

if __name__=='__main__':main()
