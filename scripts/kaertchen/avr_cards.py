#!/usr/bin/env python3
"""Generate schematic 45 x 55 mm AVR DIP cards from verified local pin maps."""
from pathlib import Path
import copy, hashlib, html, json, re, sqlite3, subprocess, sys

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'images/Atmel_AVR'
GREEN, INK = '#006c46', '#172b35'

def text(x, y, value, size=1.5, anchor='middle', bold=False, color=INK):
    return (f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" '
            f'font-weight="{700 if bold else 400}" fill="{color}">{html.escape(str(value))}</text>')

def rect(x, y, w, h, fill='none', stroke='none', radius=0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width=".22"/>'

def content(card):
    pins = card['pins']; n = len(pins); pitch = 36.1 / (n // 2 - 1)
    s = rect(.5,.5,44,54,'white',GREEN,1)
    s += text(22.5,3.5,card['part'],2.3,bold=True,color=GREEN)
    s += text(22.5,6.1,f"{card['package']} | Draufsicht | Kerbe oben",1.55)
    s += rect(18,8.2,9,39.9,'#f6f8f7',GREEN,.5)
    s += '<path d="M20.7,8.2 A1.8,1.8 0 0 0 24.3,8.2" fill="white" stroke="#006c46" stroke-width=".25"/>'
    s += '<circle cx="19.2" cy="9.3" r=".38" fill="#006c46"/>'
    for p in pins:
        num=p['number'];left=num<=n//2;row=num-1 if left else n-num;y=10.6+row*pitch
        name=p['name'];alt=p['alternate'];supply=name in ('VCC','AVCC');ground=name=='GND'
        if supply or ground:s += rect(1 if left else 27.8,y-1.3,16.2,1.85,'#ffd6d6' if supply else '#d8e6f5',radius=.25)
        s += rect(17.1 if left else 27,y-.45,.9,.7,'white',GREEN)
        s += text(19.4 if left else 25.6,y+.25,num,1.45,bold=True,color=GREEN)
        x=16.6 if left else 28.4;anchor='end' if left else 'start'
        if n == 40:
            label = (alt + '  ' + name) if left and alt else (name + '  ' + alt if alt else name)
            s += text(x,y+.25,label,1.48,anchor,bold=supply or ground,color=GREEN if supply or ground else INK)
            continue
        s += text(x,y,name,1.6,anchor,True,GREEN)
        if alt:
            # Fit all alternate names in the label column without omitting functions.
            size=min(1.12,15.2/(len(alt)*.62))
            s += text(x,y+.85,alt,size,anchor)
    s += text(22.5,50,'/ = aktiv Low | GPIO je nach Konfiguration',1.25)
    s += text(22.5,51.7,'Schematisch, kein 5,08-mm-Boardraster',1.25)
    s += text(22.5,53.4,f"{card['source_document']} | PDF-Seite {card['source_pdf_page']}",1.25)
    return s

def svg(body,w=45,h=55):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}mm" height="{h}mm" viewBox="0 0 {w} {h}" font-family="Arial, Helvetica, sans-serif">{body}</svg>\n'

def convert(path):
    subprocess.run(['rsvg-convert','-f','pdf','-o',str(path.with_suffix('.pdf')),str(path)],check=True)
    subprocess.run(['rsvg-convert','-f','png','-d','300','-p','300','-o',str(path.with_suffix('.png')),str(path)],check=True)

def main():
    cfg=json.loads(Path(__file__).with_name('avr_pins.json').read_text());cards=copy.deepcopy(cfg['cards'])
    sys.path.insert(0,str(ROOT/'scripts'))
    from build_db import read_inventory
    inventory=read_inventory();stock={r[1]:r for r in inventory if r[0]=='Atmel AVR'}
    assert set(stock)=={c['part'] for c in cards}
    for c in cards:
        assert hashlib.sha256((ROOT/c['source']).read_bytes()).hexdigest()==c['source_sha256'],c['part']
        assert stock[c['part']][3]==c['package']
        assert [p['number'] for p in c['pins']]==list(range(1,len(c['pins'])+1))
        assert len(c['pins'])==int(c['package'].split('-')[1])
    OUT.mkdir(parents=True,exist_ok=True)
    for c in cards:
        base=OUT/(c['part']+'_karte_45x55mm.svg');base.write_text(svg(content(c)));convert(base)
        for ext in ('svg','pdf','png'):c[ext]=str(base.with_suffix('.'+ext).relative_to(ROOT))
    # One A4 sheet, six cards at actual size and a labelled orientation key.
    body=rect(0,0,210,297,'white')+text(15,16,'Atmel AVR | DIP-Anschlusskarten 45 x 55 mm',4,'start',True,GREEN)
    body+=text(15,23,'Druck: 100 % / tatsächliche Größe, keine Seitenanpassung.',3,'start')
    body+=text(15,29,'Schematische Draufsicht; / = aktiv Low; kein 5,08-mm-Boardraster.',2.8,'start')
    for i,c in enumerate(cards):
        x=15+(i%3)*50;y=40+(i//3)*60
        body+=f'<g transform="translate({x},{y})">{content(c)}</g>'
    sheet=OUT/'AVR_Karten_A4.svg';sheet.write_text(svg(body,210,297));convert(sheet)
    (OUT/'karten.json').write_text(json.dumps(dict(view=cfg['view'],note=cfg['note'],cards=cards),ensure_ascii=False,indent=2)+'\n')
    md=ROOT/'Bauteile.md';updated=[]
    for line in md.read_text().splitlines():
        match=next((c for c in cards if line.startswith('| '+c['part']+' |')),None)
        if match:
            cells=line.split('|');cells[-2]=' '+ ' / '.join(f'[{label}]({match[ext]})' for label,ext in [('Bild','png'),('PDF','pdf'),('SVG','svg')])+' ';line='|'.join(cells)
        updated.append(line)
    md.write_text('\n'.join(updated)+'\n')
    desired=read_inventory()
    with sqlite3.connect(ROOT/'Bauteile.db') as db:
        before=list(db.execute('SELECT * FROM Bauteile ORDER BY Type,Bezeichnung'))
        for c in cards:db.execute('UPDATE Bauteile SET Karte_PNG=?,Karte_PDF=?,Karte_SVG=? WHERE Type=? AND Bezeichnung=?',(c['png'],c['pdf'],c['svg'],'Atmel AVR',c['part']))
        after=list(db.execute('SELECT * FROM Bauteile ORDER BY Type,Bezeichnung'))
        assert [r[:7]+r[10:] for r in before]==[r[:7]+r[10:] for r in after]
        assert {r[:2]:r for r in after}=={r[:2]:r for r in desired}
        assert db.execute('PRAGMA integrity_check').fetchone()==('ok',)
    readme='# Atmel AVR: DIP-Anschlusskarten\n\nSechs Karten im Format **45 × 55 mm**, als schematische **Draufsicht mit Kerbe oben**. Pin 1 liegt oben links; links wird nach unten, rechts nach oben gezählt. Versorgung rot, Masse hellblau. `/` kennzeichnet aktiv Low. Die Karten zeigen alle im Pinbild genannten Alternativfunktionen; ihre Verfügbarkeit hängt von Konfiguration und Fuses ab.\n\n**Kein 5,08-mm-Boardraster:** Die Pinreihen sind für DIP-20/28/40 kompakt dargestellt, die Gehäuse sind nicht maßstäblich.\n\n[A4-Druckbogen](AVR_Karten_A4.pdf) · [Vorschau](AVR_Karten_A4.png) · [Bestand](../../Bauteile.md#ic-bestand-atmel-avr)\n\nBei **100 % / tatsächlicher Größe** ohne Seitenanpassung drucken.\n\n| Typ | Gehäuse | Vorschau | Druck | Vektor | Pinreferenz |\n| --- | --- | --- | --- | --- | --- |\n'
    for c in cards:
        readme+=f"| {c['part']} | {c['package']} | [PNG]({Path(c['png']).name}) | [PDF]({Path(c['pdf']).name}) | [SVG]({Path(c['svg']).name}) | [{c['source_document']}, PDF-S. {c['source_pdf_page']}](../../{c['source']}) |\n"
    readme+='\nATMEGA32L8PI bleibt als Bestandsbezeichnung erhalten; Pinreferenz ist ATmega32L (zugeordnete Schreibweise ATmega32L-8PI). ATtiny2313: USCK ist der USI-Takt, im Hersteller-Pinbild steht der Druckfehler UCSK. ATmega8 und ATmega328P haben dasselbe DIP-Versorgungslayout, aber unterschiedliche Alternativfunktionen; sie besitzen eigene Karten.\n\nGeprüfte Pinfolgen und Quellenprüfsummen: [Generator-Konfiguration](../../scripts/kaertchen/avr_pins.json), [Ausgabemanifest](karten.json). Neuerzeugung: `python3 scripts/kaertchen/avr_cards.py`.\n'
    (OUT/'README.md').write_text(readme)
    print('6 AVR-Karten und A4-Druckbogen erstellt; Markdown und Datenbank abgeglichen.')

if __name__=='__main__':main()
