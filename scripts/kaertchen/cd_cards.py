"""CD4000 cards in the layout of the user's old cards.

Gate wires use the inventory's actual pin numbers. Complex diagrams are
preserved as cropped, embedded PNGs from the old cards, not redrawn guesses.
"""
from pathlib import Path
from collections import defaultdict
import json
import re

from PIL import Image as PILImage
from reportlab.graphics.shapes import Drawing, Rect, Circle, Line, String, Path as ShapePath, Image
from reportlab.lib import colors
from reportlab.pdfbase.pdfmetrics import stringWidth

MM = 72 / 25.4
GREEN = colors.HexColor('#19472c')
BLUE = colors.HexColor('#0075c9')
BLACK = colors.black
BASE = Path(__file__).parent / 'logikvorlagen'
SOURCES = json.loads((BASE / 'quellen.json').read_text())

TITLES = {
 'MC14521BCP':'24-stufiger Frequenzteiler',
 'CD40194BE':'4-Bit-Universal-Schieberegister',
 'CD4001':'4 NOR-Gatter, je 2 Eingänge', 'CD4002':'2 NOR-Gatter, je 4 Eingänge',
 'CD4009':'6 Inverter / Pegelwandler', 'CD4011':'4 NAND-Gatter, je 2 Eingänge',
 'CD4012':'2 NAND-Gatter, je 4 Eingänge', 'CD4013':'2 D-Flipflops',
 'CD4015':'2 × 4-Bit-Schieberegister', 'CD4016':'4 Analogschalter',
 'CD4017':'Dekadenzähler, 10 Ausgänge', 'CD4019':'4 AND-OR-Datenselektoren',
 'CD4021':'8-Bit-Schieberegister, P/S', 'CD4022':'Oktalzähler, 8 Ausgänge',
 'CD4023':'3 NAND-Gatter, je 3 Eingänge', 'CD4024':'7-Bit-Binärzähler',
 'CD4025':'3 NOR-Gatter, je 3 Eingänge', 'CD4026':'Dekadenzähler / 7-Segment',
 'CD4027':'2 JK-Flipflops', 'CD4028':'BCD-zu-Dezimal-Decoder',
 'CD4029':'4-Bit-Zähler, Binär/BCD, auf/ab', 'CD4030':'4 XOR-Gatter, je 2 Eingänge',
 'CD4033':'Dekadenzähler / 7-Segment', 'CD4042':'4-Bit-D-Latch',
 'CD4043':'4 RS-Latches, 3-State', 'CD4046':'PLL / VCO',
 'CD4047':'Astabiler / monostabiler Timer', 'CD4049':'6 Inverter / Pegelwandler',
 'CD4050':'6 Puffer / Pegelwandler', 'CD4051':'8-Kanal-Analog-Multiplexer',
 'CD4052':'2 × 4-Kanal-Analog-Multiplexer', 'CD4053':'3 × 2-Kanal-Analog-Multiplexer',
 'CD4060':'14-Bit-Zähler / Oszillator', 'CD4063':'4-Bit-Komparator',
 'CD4066':'4 Analogschalter', 'CD4068':'8-Eingang-AND / NAND',
 'CD4069':'6 Inverter', 'CD4070':'4 XOR-Gatter, je 2 Eingänge',
 'CD4071':'4 OR-Gatter, je 2 Eingänge', 'CD4072':'2 OR-Gatter, je 4 Eingänge',
 'CD4073':'3 AND-Gatter, je 3 Eingänge', 'CD4075':'3 OR-Gatter, je 3 Eingänge',
 'CD4077':'4 XNOR-Gatter, je 2 Eingänge', 'CD4081':'4 AND-Gatter, je 2 Eingänge',
 'CD4082':'2 AND-Gatter, je 4 Eingänge', 'CD4093':'4 Schmitt-NAND, je 2 Eingänge',
 'CD4094':'8-Bit-Schieberegister / Latch', 'CD4098':'2 Monoflops',
 'CD4503':'6 Puffer, 3-State', 'CD4511':'BCD-Latch / 7-Segment-LED',
 'CD4513':'BCD-Latch / 7-Segment (18 Pins)', 'CD4518':'2 BCD-Zähler',
 'CD4520':'2 × 4-Bit-Binärzähler', 'CD4528':'2 Monoflops',
 'CD4538':'2 Präzisions-Monoflops', 'CD4541':'Programmierbarer Timer',
 'CD4543':'BCD-Latch / 7-Segment', 'CD4553':'3-stelliger BCD-Zähler',
}


class Card:
 def __init__(self, r):
  self.r = r
  self.d = Drawing(45 * MM, 55 * MM)
  self.n = r['pin_count']
  self.pins = {p['number']: p for p in r['pins']}
  self.connections = []

 def xy(self, x, y): return x * MM, (55 - y) * MM

 def line(self, points, color=GREEN, width=.23):
  for a, b in zip(points, points[1:]):
   self.d.add(Line(*self.xy(*a), *self.xy(*b), strokeColor=color, strokeWidth=width * MM))

 def rect(self, x, y, w, h, fill=None, stroke=GREEN, width=.23):
  self.d.add(Rect(x * MM, (55-y-h) * MM, w * MM, h * MM,
                  fillColor=fill, strokeColor=stroke, strokeWidth=width * MM))

 def circle(self, x, y, radius, fill=colors.white, color=GREEN, width=.23):
  self.d.add(Circle(*self.xy(x,y), radius*MM, fillColor=fill, strokeColor=color, strokeWidth=width*MM))

 def text(self, x, y, value, size=6.5, color=GREEN, anchor='start', bold=False, width=None):
  font = 'Helvetica-Bold' if bold else 'Helvetica'
  if width:
   size = min(size, size * width * MM / max(stringWidth(value,font,size), .01))
  self.d.add(String(*self.xy(x,y), value, fontName=font, fontSize=size,
                    fillColor=color, textAnchor=anchor))

 def pin_y(self, number):
  return 6.4 + (number-1 if number <= self.n//2 else self.n-number) * 5.08

 def wire(self, number, port, bend=None):
  left = number <= self.n//2
  name = self.display_name(self.pins[number]['name'])
  # Wires begin immediately after the short gate labels, or at the outer
  # edge of the central panel for longer block labels.
  length = min(7.1, stringWidth(name.lstrip('/'),'Helvetica-Bold',6.4)/MM)
  x = 4.3 + length + .4 if left else 40.7-length-.4
  y = self.pin_y(number)
  if bend is None: bend = x + (1.1 if left else -1.1)
  self.line([(x,y),(bend,y),(port[0],port[1])])
  self.connections.append(number)

 def display_name(self, name):
  key=self.r['key']
  if key in ('CD4013','CD4027'):
   match=re.fullmatch(r'(/?Q|C|R|S|D|J|K)-(\d)',name)
   if match:
    signal,unit=match.groups()
    # The old TI diagram names the JK flip-flop at pins 9..15 FF1.
    if key=='CD4027':unit=str(3-int(unit))
    return {'C':'CLK','R':'RST','S':'SET'}.get(signal,signal)+unit
  if key in ('CD4021','CD4024') and re.fullmatch(r'Q\d',name):return 'Q'+str(int(name[1:])+1)
  if key=='CD4094' and re.fullmatch(r'QP\d',name):return 'Q'+str(int(name[2:])+1)
  aliases = {'CLOCK':'CLK','CLOCK_INHIBIT':'INHIBIT','RIPPLE_BLANKING_IN':'RBI',
             'RIPPLE_BLANKING_OUT':'RBO','CARRY_OUT':'CARRY','LAMP_TEST':'LT',
             'RC_COMMON':'R/C','EXT_RESET':'RESET','OUTPUT/Q':'Q',
             'Q//Q_SELECT':'Q-SEL','Enable-1':'EN1','Enable-2':'EN2'}
  return aliases.get(name,name)

 def labels(self):
  for p in self.pins.values():
   num=p['number'];left=num<=self.n//2;y=self.pin_y(num)
   name=self.display_name(p['name']);power=name.upper() in ('VDD',"VDD'",'VCC','VEE','V+','V-')
   ground=name in ('GND',"GND'")
   output=p['role'] in ('output','tri_state','open_collector') or bool(re.match(r'^/?(?:\dY|Q|[a-g]$|CARRY|.*OUT)',name))
   color=BLUE if output else GREEN
   if power or ground:
    self.rect(.65 if left else 32,y-1.25,12.35,2.5,
              colors.HexColor('#ffa3a3') if power else colors.HexColor('#c6d9ef'),None)
   x=2.2 if left else 42.8
   self.circle(x,y,1.65,width=.28)
   self.text(x,y+.72,str(num),7,GREEN,'middle',True)
   # Active-low signals get the overbar used on the old cards.
   shown=name.lstrip('/')
   width=7.1 if self.r['key'] in SOURCES else 8.5
   size=min(6.4,6.4*width*MM/max(stringWidth(shown,'Helvetica-Bold',6.4),.01))
   tx=4.3 if left else 40.7
   self.text(tx,y+.65,shown,size,color,'start' if left else 'end',True)
   if name.startswith('/'):
    span=stringWidth(shown,'Helvetica-Bold',size)/MM
    self.line([(tx if left else tx-span,y-1.1),(tx+span if left else tx,y-1.1)],color,.15)

 def heading(self, y, size):
  key=self.r['key'];function=TITLES[key];full=key+' '+function
  size=min(size,size*41*MM/stringWidth(full,'Helvetica',size))
  width_key=stringWidth(key+' ','Helvetica-Bold',size)
  width_all=width_key+stringWidth(function,'Helvetica',size)
  x=(45*MM-width_all)/2/MM
  self.text(x,y,key,size,GREEN,bold=True)
  self.text(x+width_key/MM,y,function,size,BLACK)

 def diagram(self, files, x=11.0, y=7.1, width=23, height=38.6):
  images=[(BASE/rec['file'],PILImage.open(BASE/rec['file']).size) for rec in files]
  # Preserve each image's aspect ratio, stacking supplementary diagrams.
  max_width=max(s[0] for _,s in images)
  total_height=sum(s[1] for _,s in images)
  scale=min(width/max_width,(height-(len(images)-1)*.9)/total_height)
  actual_height=total_height*scale+(len(images)-1)*.9
  cy=y+(height-actual_height)/2
  for path,(iw,ih) in images:
   w=iw*scale;h=ih*scale
   self.d.add(Image((x+(width-w)/2)*MM,(55-cy-h)*MM,w*MM,h*MM,str(path)))
   cy+=h+.9

 def gate_shape(self, x, y, kind, down=True, inputs=2, schmitt=False, horizontal=False):
  sign=1 if down else -1
  def position(a,b):return (x+sign*b,y+a) if horizontal else (x+a,y+sign*b)
  def point(a,b):return self.xy(*position(a,b))
  path=ShapePath(fillColor=colors.white,strokeColor=GREEN,strokeWidth=.28*MM)
  path.moveTo(*point(-3,-2.5))
  or_gate=kind in ('OR','NOR','XOR','XNOR')
  if or_gate:
   path.curveTo(*point(-1,-1.3),*point(1,-1.3),*point(3,-2.5))
   path.curveTo(*point(3,.1),*point(1.6,2.3),*point(0,3))
   path.curveTo(*point(-1.6,2.3),*point(-3,.1),*point(-3,-2.5))
  else:
   path.lineTo(*point(3,-2.5));path.lineTo(*point(3,0))
   path.curveTo(*point(3,1.657),*point(1.657,3),*point(0,3))
   path.curveTo(*point(-1.657,3),*point(-3,1.657),*point(-3,0))
  path.closePath();self.d.add(path)
  if kind in ('XOR','XNOR'):
   extra=ShapePath(fillColor=None,strokeColor=GREEN,strokeWidth=.23*MM)
   extra.moveTo(*point(-3,-3.1));extra.curveTo(*point(-1,-1.9),*point(1,-1.9),*point(3,-3.1));self.d.add(extra)
  if schmitt:
   self.line([(x-1.1,y+sign*.6),(x-.3,y+sign*.6),(x-.3,y-sign*.7),(x+1.1,y-sign*.7)],width=.18)
   self.line([(x-1.1,y+sign*1.1),(x+.3,y+sign*1.1),(x+.3,y-sign*.2),(x+1.1,y-sign*.2)],width=.18)
  inv=kind in ('NAND','NOR','XNOR')
  if inv:self.circle(*position(0,3.45),.45,width=.2)
  ports=[]
  for i in range(inputs):
   a=-1.65+3.3*i/(inputs-1) if inputs>1 else 0
   t=(a+3)/6
   b=-2.5+3*1.2*t*(1-t) if or_gate else -2.5
   ports.append(position(a,b))
  return ports,position(0,3.9 if inv else 3)

 def three_input_gates(self, kind):
  # Match the old three-gate arrangement. Gate 1 has inputs on both sides
  # of the DIP; separate lanes keep its long wires away from gate 3.
  for unit,x,y,right in ((1,33,31.8,True),(2,13,21.64,True),(3,33,16.56,False)):
   ps={p['name'][-1]:p['number'] for p in self.pins.values() if re.fullmatch(str(unit)+r'[ABCY]',p['name'])}
   ports,out=self.gate_shape(x,y,kind,right,3,horizontal=True)
   if unit==1:
    a,b,c=ps['A'],ps['B'],ps['C']
    self.line([(8.8,self.pin_y(a)),(14,self.pin_y(a)),(25.5,16.8),(25.5,26.5),(29,ports[0][1]),ports[0]])
    self.line([(8.8,self.pin_y(b)),(15.5,self.pin_y(b)),(21.5,17.8),(21.5,26.8),(26,ports[1][1]),ports[1]])
    self.line([(36.2,self.pin_y(c)),(28.7,self.pin_y(c)),(28.7,ports[2][1]),ports[2]])
    self.connections.extend((a,b,c))
    self.wire(ps['Y'],out,bend=38)
   elif unit==2:
    for name,port in zip(('A','B','C'),ports):
     number=ps[name];py=self.pin_y(number)
     self.line([(8.8,py),(9.2,py),(9.2,port[1]),port]);self.connections.append(number)
    self.line([out,(17.6,out[1]),(17.6,29.2),(11.3,self.pin_y(ps['Y'])),(8.8,self.pin_y(ps['Y']))]);self.connections.append(ps['Y'])
   else:
    # Sort by physical height, rather than symbolic A/B/C order.
    for number,port in zip(sorted((ps[n] for n in ('A','B','C')),key=self.pin_y),ports):
     py=self.pin_y(number);self.line([(36.2,py),(37.1,py),(37.1,port[1]),port]);self.connections.append(number)
    self.line([out,(28.1,out[1]),(28.1,24.2),(32,self.pin_y(ps['Y'])),(36.2,self.pin_y(ps['Y']))]);self.connections.append(ps['Y'])
  self.text(20.1,30.3,'A B C | Y',4.8,BLACK,'middle',True)
  for i in range(8):
   bits=[i>>2,(i>>1)&1,i&1]
   result=int(all(bits)) if kind in ('AND','NAND') else int(any(bits))
   if kind in ('NAND','NOR'):result=1-result
   self.text(20.1,32.4+i*1.8,' '.join(map(str,bits))+' | '+str(result),4.8,BLUE,'middle')

 def gates(self, kind):
  if 'je 3 Eingängen' in self.r['function']:
   self.three_input_gates(kind)
   return
  groups=defaultdict(list)
  for p in self.pins.values():
   m=re.fullmatch(r'(\d+)([A-HY])',p['name'])
   if m:groups[int(m[1])].append(p)
  for unit,ps in groups.items():
   inputs=sorted((p for p in ps if not p['name'].endswith('Y')),key=lambda p:p['name'])
   output=next(p for p in ps if p['name'].endswith('Y'))
   left=sum(p['number']<=self.n//2 for p in ps)>len(ps)/2
   x=15.6 if left else 29.4
   ys=[self.pin_y(p['number']) for p in ps]
   same_side=all((p['number']<=self.n//2)==left for p in ps)
   y=sum(ys)/len(ys) if same_side else (11.5 if unit==1 else 26.7 if unit==2 else 16.6)
   down=self.pin_y(output['number'])>sum(self.pin_y(p['number']) for p in inputs)/len(inputs)
   ports,out=self.gate_shape(x,y,kind,down,len(inputs),self.r['key']=='CD4093')
   # The pin nearest the input edge uses the outermost gate terminal.
   # Approach input terminals from outside the body of the gate.
   edge_y=sum(port[1] for port in ports)/len(ports)
   ordered=sorted(inputs,key=lambda p:abs(self.pin_y(p['number'])-edge_y))
   for rank,(p,port) in enumerate(zip(ordered,ports if left else list(reversed(ports)))):
    num=p['number']
    if (num<=self.n//2)!=left:
     py=self.pin_y(num);self.line([(36 if num>self.n//2 else 9,py),(23,py),(23,port[1]-1),(port[0],port[1]-1),port])
     self.connections.append(num)
    else:
     py=self.pin_y(num);sign=1 if down else -1
     start=8.8 if left else 36.2
     if sign*(py-port[1])<-.7:
      self.line([(start,py),(port[0],py),port])
     else:
      bend=x-(4.2+rank*.45) if left else x+(4.2+rank*.45)
      approach=port[1]-sign*(1.3+rank*.5)
      self.line([(start,py),(bend,py),(bend,approach),(port[0],approach),port])
     self.connections.append(num)
   self.wire(output['number'],out)
  if len(next(iter(groups.values())))==3:
   truth={'NAND':[1,1,1,0],'AND':[0,0,0,1],'NOR':[1,0,0,0],
          'OR':[0,1,1,1],'XOR':[0,1,1,0],'XNOR':[1,0,0,1]}[kind]
   self.text(22.5,35.5,'A B | Y',6,BLACK,'middle',True)
   for i,v in enumerate(truth):self.text(22.5,38+i*2.3,f'{i//2} {i%2} | {v}',6,BLUE,'middle')
  else:
   self.text(22.5,44,'Y = '+kind+'(A, B, ...)',5.8,BLACK,'middle')

 def buffers(self):
  groups=defaultdict(dict)
  for p in self.pins.values():
   m=re.fullmatch(r'(\d+)([AY])',p['name'])
   if m:groups[int(m[1])][m[2]]=p['number']
  invert=self.r['key']!='CD4050'
  for unit,ps in groups.items():
   left=ps['A']<=self.n//2;x=15.5 if left else 29.5
   y=(self.pin_y(ps['A'])+self.pin_y(ps['Y']))/2
   down=self.pin_y(ps['Y'])>self.pin_y(ps['A']);sign=1 if down else -1
   path=ShapePath(fillColor=colors.white,strokeColor=GREEN,strokeWidth=.26*MM)
   for i,point in enumerate(((x-1.8,y-sign*1.7),(x+1.8,y-sign*1.7),(x,y+sign*1.7))):
    (path.moveTo if i==0 else path.lineTo)(*self.xy(*point))
   path.closePath();self.d.add(path)
   if invert:self.circle(x,y+sign*2.1,.4,width=.2)
   self.wire(ps['A'],(x,y-sign*1.7));self.wire(ps['Y'],(x,y+sign*(2.5 if invert else 1.7)))
  if self.r['key']=='CD4050':self.diagram(SOURCES['CD4050']['diagrams'],16,39,13,8)

 def switches(self):
  # Four analogue switches, each with its actual A/B/control pin number.
  pairs=[(1,2,13),(3,4,5),(6,8,9),(10,11,12)]
  for i,(a,b,c) in enumerate(pairs):
   x=15.5 if i<2 else 29.5;y=(8.5,18.5,31.8,21.64)[i]
   self.rect(x-3,y-2,6,4)
   self.line([(x-3,y),(x-.8,y),(x+.8,y-.9)])
   self.line([(x+.8,y),(x+3,y)])
   self.circle(x-.8,y,.2,fill=GREEN,width=.1)
   self.circle(x+.8,y,.2,fill=GREEN,width=.1)
   self.text(x,y+1.3,'SW'+str(i+1),4.3,anchor='middle')
   # Approach both analogue terminals from outside the switch symbol.
   if a<=self.n//2:self.wire(a,(x-3,y))
   else:
    self.line([(36.3,self.pin_y(a)),(x-4,self.pin_y(a)),(x-4,y),(x-3,y)])
    self.connections.append(a)
   if b>self.n//2:self.wire(b,(x+3,y))
   else:
    self.line([(8.8,self.pin_y(b)),(x+4,self.pin_y(b)),(x+4,y),(x+3,y)])
    self.connections.append(b)
   py=self.pin_y(c);top=py<y or i in (0,2);port_y=y-2 if top else y+2
   lane=y-3.6 if top else y+4.2
   bend=35 if i==2 else 22.5
   self.line([(8.8 if c<=self.n//2 else 36.3,py),(bend,py),(bend,lane),(x,lane),(x,port_y)])
   self.connections.append(c)
  self.diagram(SOURCES[self.r['key']]['diagrams'],15,39,15,7.3)

 def flipflops(self):
  for unit,y in ((1,14),(2,32)):
   self.rect(17,y-5,11,10)
   self.text(22.5,y+.7,'D-FF'+str(unit),7,anchor='middle',bold=True)
   self.text(22.5,y-6,'SET'+str(unit),5.6,anchor='middle')
   self.text(22.5,y+7,'RST'+str(unit),5.6,anchor='middle')
   self.line([(22.5,y-5),(22.5,y-6)]);self.line([(22.5,y+5),(22.5,y+6)])
   for p in self.pins.values():
    if p['name'].endswith('-'+str(unit)):
     name=p['name'].split('-')[0]
     px,py={'D':(17,y-2),'C':(17,y+2),'S':(22.5,y-5),'R':(22.5,y+5),
            'Q':(28,y+2),'/Q':(28,y-2)}[name]
     self.line([(px-1 if px==17 else px,py),(px if px==17 else px+1 if px==28 else px,py)])
     self.text(15.7 if px==17 else 29.3 if px==28 else px,py+.6,
               str(p['number']),4.5,BLUE if 'Q' in name else GREEN,
               'end' if px==17 else 'start' if px==28 else 'middle')
     if name=='C':self.line([(17,y+1),(18,y+2),(17,y+3)])
     if name=='/Q':self.circle(28.4,py,.4,width=.15)
   self.text(22.5,45,'CLK steigt: Q = D',5.8,BLACK,'middle')

 def connected_block(self):
  # Cards for which the old set has no diagram: a functional block wired
  # directly to every signal pin, using the existing validated inventory.
  self.rect(15,8.1,15,37.6)
  caption={
   'MC14521BCP':['OSC / CLK','24 STUFEN','TEILER','Q18..Q24'],
   'CD40194BE':['4 Bit','UNIVERSAL','SHIFT L / R','PARALLEL','REGISTER'],
   'CD4019':['AND-OR','Qn =','(An & SA) |','(Bn & SB)'],
   'CD4046':['PLL','VCO','Phasen-','komparator','I / II'],
   'CD4047':['Timer','ASTABIL /','MONOSTABIL'],
   'CD4052':['2 × 4:1','ANALOG','MUX','A / B','INHIBIT'],
   'CD4068':['&','8 Eingänge','Y / Y inv.'],
   'CD4098':['2 ×','MONOFLOP'], 'CD4528':['2 ×','MONOFLOP'],
   'CD4538':['2 ×','MONOFLOP'],
   'CD4513':['BCD','LATCH','7-SEGMENT','MC14513B'],
  }[self.r['key']]
  for i,t in enumerate(caption):self.text(22.5,20+i*3.2,t,6.5,BLACK,'middle',i==0,width=13)
  for p in self.pins.values():
   if p['name'] in ('VDD','VCC','VEE','GND','NC'):continue
   num=p['number'];left=num<=self.n//2;y=self.pin_y(num)
   port=(15 if left else 30,min(45,max(8.3,y)))
   # Short horizontal paths avoid crossings and make each port explicit.
   self.line([(12 if left else 33,y),port]);self.connections.append(num)
   if p.get('shape') in ('clock','inverted_clock'):
    sign=1 if left else -1
    self.line([(port[0],port[1]-.7),(port[0]+sign*.9,port[1]),(port[0],port[1]+.7)],width=.15)

 def draw(self):
  self.rect(.25,.25,44.5,54.5,colors.white,GREEN,.3)
  self.heading(3.15,8.2)
  key=self.r['key'];function=self.r['function'];gate=None
  for g in ('XNOR','XOR','NAND','NOR','AND','OR'):
   if re.search(r'\b'+g+r'-Gatter',function):gate=g;break
  if key in ('CD4019','CD4068'):gate=None
  if gate:self.gates(gate);layout='verdrahtete Gatter'
  elif key in ('CD4009','CD4049','CD4050','CD4069'):self.buffers();layout='verdrahtete Puffer/Inverter'
  elif key in ('CD4016','CD4066'):self.switches();layout='verdrahtete Analogschalter und Originalskizze'
  elif key=='CD4013':self.flipflops();layout='D-Flipflops mit Pinnummern'
  elif key in SOURCES and SOURCES[key]['diagrams']:self.diagram(SOURCES[key]['diagrams']);layout='Original-Logikskizze'
  else:self.connected_block();layout='verdrahteter Funktionsblock'
  self.labels()
  self.text(22.5,48,'Ref: '+self.r['reference'],4.6,BLACK,'middle',width=41)
  self.heading(51.2,6.5)
  self.text(22.5,53.65,'Draufsicht | Überstrich: aktiv Low | '+str(self.n)+' Pins',4.8,BLACK,'middle',width=41)
  self.r['first_pin_y_mm']=6.4
  self.r['card_layout']='CD4xxx nach PNG Kopie'
  self.r['diagram_layout']=layout
  self.r['wired_pin_numbers']=sorted(set(self.connections))
  self.r['card_function_title']=TITLES[key]
  self.r['card_pin_labels']={str(p['number']):self.display_name(p['name']) for p in self.pins.values()}
  if key in SOURCES:self.r['logic_diagram_source']=SOURCES[key]
  return self.d


def draw_cd(r):
 return Card(r).draw()
