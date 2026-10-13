"""SN74xx cards: actual pin-connected logic and selected datasheet figures."""
from pathlib import Path
from collections import defaultdict
import json
import re
from PIL import Image as PILImage
from reportlab.graphics.shapes import Image, Path as ShapePath
from reportlab.lib import colors
from reportlab.pdfbase.pdfmetrics import stringWidth
from diverse_cards import DiverseCard
from cd_cards import GREEN, BLUE, BLACK, MM

BASE=Path(__file__).parent/'sn_logikvorlagen'
SOURCES=json.loads((BASE/'quellen.json').read_text())
NAMES={
 0:'4 NAND, je 2 Eingänge',2:'4 NOR, je 2 Eingänge',4:'6 Inverter',5:'6 Inverter, OC',
 6:'6 Inverter / Treiber, OC',7:'6 Puffer / Treiber, OC',8:'4 AND, je 2 Eingänge',
 10:'3 NAND, je 3 Eingänge',11:'3 AND, je 3 Eingänge',12:'3 NAND, 3 Eingänge, OC',
 14:'6 Schmitt-Inverter',16:'6 Inverter / Treiber, OC',20:'2 NAND, je 4 Eingänge',
 21:'2 AND, je 4 Eingänge',27:'3 NOR, je 3 Eingänge',30:'NAND mit 8 Eingängen',
 32:'4 OR, je 2 Eingänge',38:'4 NAND, 2 Eingänge, OC',40:'2 NAND, je 4 Eingänge',
 42:'BCD-zu-Dezimal-Decoder',47:'BCD / 7-Segment, OC',48:'BCD / 7-Segment, aktiv High',
 51:'2 AND-OR-INVERT-Gatter',54:'4-fach-AND-OR-INVERT',55:'2-fach-AND-OR-INVERT',
 60:'2 Expander, je 4 Eingänge',73:'2 JK-Flipflops, CLR',74:'2 D-Flipflops, PRE / CLR',
 75:'4-Bit-D-Latch',76:'2 JK-Flipflops, PRE / CLR',83:'4-Bit-Volladdierer',
 86:'4 XOR, je 2 Eingänge',87:'4-Bit-Funktionselement',90:'Dekadenzähler / 2 und 5',
 92:'Teiler durch 12 / 2 und 6',93:'4-Bit-Zähler / 2 und 8',95:'4-Bit-Schieberegister, P/S',
 107:'2 JK-Flipflops, CLR',109:'2 JK-Flipflops, PRE / CLR',112:'2 JK-Flipflops, PRE / CLR',
 138:'3-zu-8-Decoder / Demultiplexer',139:'2 × 2-zu-4-Decoder',145:'BCD-zu-Dezimal, OC',
 147:'BCD-Prioritätsencoder',148:'8-zu-3-Prioritätsencoder',151:'8-zu-1-Multiplexer',
 153:'2 × 4-zu-1-Multiplexer',155:'2 × 2-zu-4-Decoder',156:'2 × 2-zu-4-Decoder, OC',
 157:'4 × 2-zu-1-Multiplexer',160:'BCD-Zähler, asynchroner CLR',
 161:'4-Bit-Zähler, asynchroner CLR',162:'BCD-Zähler, synchroner CLR',
 163:'4-Bit-Zähler, synchroner CLR',164:'8-Bit-Schieberegister, S/P',
 165:'8-Bit-Schieberegister, P/S',166:'8-Bit-Schieberegister, P/S',
 174:'6 D-Flipflops, gemeinsamer CLR',175:'4 D-Flipflops, Q und Q inv.',
 190:'BCD-Auf-/Abwärtszähler',191:'4-Bit-Auf-/Abwärtszähler',
 192:'BCD-Zähler, getrennte Takte',193:'4-Bit-Zähler, getrennte Takte',
 194:'4-Bit-Universal-Schieberegister',240:'8 Inverter, 3-State',244:'8 Puffer, 3-State',
 245:'8-Bit-Bustransceiver, 3-State',247:'BCD / 7-Segment, OC, 6/9 alt.',
 248:'BCD / 7-Segment, 6/9 alt.',253:'2 × 4-zu-1-MUX, 3-State',
 266:'4 XNOR, 2 Eingänge, OC',273:'8 D-Flipflops, gemeinsamer CLR',
 279:'4 RS-Latches',373:'8-Bit-D-Latch, 3-State',374:'8 D-Flipflops, 3-State',
 541:'8 Puffer, 3-State',576:'8 D-FF, Q inv., 3-State',
 640:'8-Bit-Bus, invertierend, 3-State',641:'8-Bit-Bustransceiver, OC',
}


class SNCard(DiverseCard):
 def __init__(self,r):
  super().__init__(r)
  self.num=int(re.search(r'74(?:LS|ACT|HCT|HC)?(\d+)',r['key'])[1])
  self.pins={p['number']:dict(p) for p in r['pins']}
  for p in self.pins.values():
   if p['role']=='passive' and (re.fullmatch(r'/?(?:Y\d*|Q\d+|\dX)',p['name'])):p['role']='output'

 def heading(self,y,size):
  key=self.r['key'];title=NAMES[self.num]
  size=min(size,size*41*MM/stringWidth(key+' '+title,'Helvetica-Bold',size))
  width=stringWidth(key+' ','Helvetica-Bold',size)
  x=(45*MM-width-stringWidth(title,'Helvetica',size))/2/MM
  self.text(x,y,key,size,GREEN,bold=True);self.text(x+width/MM,y,title,size,BLACK)

 def display_name(self,name):
  if self.num==51:
   name={'1B':'1D','1C':'1E','1D':'1F','1E':'1C','1F':'1B'}.get(name,name)
  if self.num in (47,48,247,248) and name in ('/BI','/Rbo','/BI//RBO'):return '/BI/RBO'
  m=re.fullmatch(r'(/?)([CDJKSQR])-(\d)',name)
  if m:
   inv,signal,unit=m.groups()
   if self.num==73:unit=str(3-int(unit))
   return inv+{'C':'CLK','R':'CLR','S':'PRE'}.get(signal,signal)+unit
  return {'Cp':'CLK','/Mr':'/CLR','/Pl':'/LOAD','/Ce':'/EN','/Rc':'/RCO',
          '/Lt':'/LT','/Rbi':'/RBI','/G1':'/G1','A->B':'DIR'}.get(name,name)

 def point_for_pin(self,num):
  name=self.display_name(self.pins[num]['name']).lstrip('/')
  width=min(7.1,stringWidth(name,'Helvetica-Bold',6.4)/MM)
  return (4.3+width+.4 if num<=self.n//2 else 40.7-width-.4,self.pin_y(num))

 def stub(self,num):
  start=self.point_for_pin(num);left=num<=self.n//2
  self.line([start,(12.5 if left else 32.5,start[1])],BLUE if self.pins[num]['role'] in ('output','tri_state','open_collector') else GREEN)
  self.connections.append(num)

 def primitive_gates(self,kind):
  groups=defaultdict(list)
  for p in self.pins.values():
   m=re.fullmatch(r'(\d)([A-HY])',p['name'])
   if m:groups[int(m[1])].append(p)
  if self.num==30:
   self.rect(14.5,5.5,16,33)
   self.text(22.5,20,'&',15,anchor='middle');self.text(22.5,27,'8 Eingänge',6,anchor='middle')
   for p in self.pins.values():
    if p['name'] not in ('VCC','GND','NC'):
     left=p['number']<=self.n//2;py=self.pin_y(p['number']);edge=14.5 if left else 30.5
     if p['name'].endswith('Y'):
      self.circle(edge+.4,py,.4,width=.18);edge+=.8
     self.line([self.point_for_pin(p['number']),(edge,py)]);self.connections.append(p['number'])
   self.text(22.5,44,'Y = NAND(A..H)',5.7,BLACK,'middle')
   return
  for unit,ps in sorted(groups.items()):
   inputs=[p for p in ps if not p['name'].endswith('Y')];out=next(p for p in ps if p['name'].endswith('Y'))
   left=sum(p['number']<=self.n//2 for p in ps)>len(ps)/2
   mixed=any((p['number']<=self.n//2)!=left for p in ps)
   if mixed:
    # SN74x10/x11/x12/x27 gate 1 has two left inputs and a right input.
    # Its manufacturer pin pattern differs from the CD4023 arrangement.
    x,y=30.2,11.48;ports,output=self.gate_shape(x,y,kind,True,len(inputs),horizontal=True)
    inputs=sorted(inputs,key=lambda p:p['name'])
    for p,port in zip(inputs,ports):
     num=p['number'];start=self.point_for_pin(num)
     if num<=self.n//2:
      self.line([start,(22.5,start[1]),(26.3,port[1]),port])
     else:
      self.line([start,(35,start[1]),(35,15.5),(26.3,15.5),(26.3,port[1]),port])
     self.connections.append(num)
    self.line([output,(output[0],self.pin_y(out['number'])),self.point_for_pin(out['number'])],BLUE);self.connections.append(out['number'])
   else:
    x=15.6 if left else 29.4;y=sum(self.pin_y(p['number']) for p in ps)/len(ps)
    down=self.pin_y(out['number'])>sum(self.pin_y(p['number']) for p in inputs)/len(inputs)
    ports,output=self.gate_shape(x,y,kind,down,len(inputs))
    edge_y=sum(p[1] for p in ports)/len(ports)
    ordered=sorted(inputs,key=lambda p:abs(self.pin_y(p['number'])-edge_y))
    for rank,(p,port) in enumerate(zip(ordered,ports if left else list(reversed(ports)))):
     start=self.point_for_pin(p['number']);py=start[1];sign=1 if down else -1
     if sign*(py-port[1])<-.7:self.line([start,(port[0],py),port])
     else:
      bend=x-(4.2+rank*.4) if left else x+(4.2+rank*.4)
      approach=port[1]-sign*(1.3+rank*.5)
      self.line([start,(bend,py),(bend,approach),(port[0],approach),port])
     self.connections.append(p['number'])
    self.wire(out['number'],output)
  if len(next(iter(groups.values())))==3:
   truth={'NAND':[1,1,1,0],'AND':[0,0,0,1],'NOR':[1,0,0,0],
          'OR':[0,1,1,1],'XOR':[0,1,1,0],'XNOR':[1,0,0,1]}[kind]
   self.text(21.5,35.2,'A B | Y',5.7,BLACK,'middle',True)
   for i,v in enumerate(truth):self.text(21.5,37.7+i*2.1,f'{i//2} {i%2} | {v}',5.7,BLUE,'middle')
  else:self.text(22.5,43.2,'Y = '+kind+'(A, B, ...)',5.6,BLACK,'middle',width=28)

 def primitive_buffers(self):
  groups=defaultdict(dict)
  for p in self.pins.values():
   m=re.fullmatch(r'(\d)([AY])',p['name'])
   if m:groups[int(m[1])][m[2]]=p['number']
  inverse=self.num!=7
  for unit,ps in sorted(groups.items()):
   left=ps['A']<=self.n//2;x=15.5 if left else 29.5
   y=(self.pin_y(ps['A'])+self.pin_y(ps['Y']))/2
   sign=1 if self.pin_y(ps['Y'])>self.pin_y(ps['A']) else -1
   path=ShapePath(fillColor=colors.white,strokeColor=GREEN,strokeWidth=.25*MM)
   for i,(px,py) in enumerate(((x-1.8,y-sign*1.7),(x+1.8,y-sign*1.7),(x,y+sign*1.7))):
    (path.moveTo if i==0 else path.lineTo)(*self.xy(px,py))
   path.closePath();self.d.add(path)
   if inverse:self.circle(x,y+sign*2.1,.4,width=.18)
   if self.num==14:self.text(x,y+.4,'ST',4,anchor='middle')
   self.line([self.point_for_pin(ps['A']),(x,self.pin_y(ps['A'])),(x,y-sign*1.7)])
   self.line([self.point_for_pin(ps['Y']),(x,self.pin_y(ps['Y'])),(x,y+sign*(2.5 if inverse else 1.7))],BLUE)
   self.connections.extend((ps['A'],ps['Y']))

 def buses(self):
  transceiver=self.num in (245,640,641)
  pairs=[]
  if transceiver:
   for i in range(8):
    a=next(p['number'] for p in self.pins.values() if p['name']=='A'+str(i))
    b=next(p['number'] for p in self.pins.values() if p['name'].lstrip('/')=='B'+str(i))
    pairs.append((a,b,str(i)))
  elif self.num==541:
   for i in range(8):
    a=next(p['number'] for p in self.pins.values() if p['name']=='A'+str(i))
    b=next(p['number'] for p in self.pins.values() if p['name']=='Y'+str(i))
    pairs.append((a,b,str(i)))
  else:
   for p in self.pins.values():
    m=re.fullmatch(r'I(\d)([ab])',p['name'])
    if m:
     out=next(q['number'] for q in self.pins.values() if q['name'].lstrip('/')=='O'+m[1]+m[2])
     pairs.append((p['number'],out,m[2]+m[1]))
  pairs.sort(key=lambda t:(self.pin_y(t[0])+self.pin_y(t[1]))/2)
  used=set()
  for i,(a,b,name) in enumerate(pairs):
   y=12+i*4.5;left=a<=self.n//2
   self.rect(15,y-1.35,15,2.7)
   label=('<->' if transceiver else '->' if left else '<-')+' '+name
   if self.num in (240,640):label+=' inv.'
   self.text(22.5,y+.65,label,5.3,BLUE,'middle',width=14)
   for num in (a,b):
    self.line([self.point_for_pin(num),(15 if num<=self.n//2 else 30,y)],BLUE if self.pins[num]['role']!='input' else GREEN)
    self.connections.append(num);used.add(num)
  controls=[p for p in self.pins.values() if p['number'] not in used and p['name'] not in ('VCC','GND','NC')]
  self.text(22.5,8,' | '.join(self.display_name(p['name'])+':'+str(p['number']) for p in controls),4.5,BLACK,'middle',width=19)
  for p in controls:self.stub(p['number'])

 def flipflops(self):
  # Each block carries actual DIP pin numbers. This avoids long crossing
  # wires when the inputs and outputs of one flip-flop span both sides.
  groups=defaultdict(list)
  for p in self.pins.values():
   m=re.fullmatch(r'(/?)([CDJKRSQ])-(\d)',p['name'])
   if m:groups[int(m[3])].append(p)
  for i,(unit,ps) in enumerate(sorted(groups.items())):
   y=8+i*19;self.rect(14.5,y,16,14.5)
   shown=3-unit if self.num==73 else unit
   self.text(22.5,y+2.5,('D-FF ' if self.num==74 else 'JK-FF ')+str(shown),6.2,anchor='middle',width=10)
   ins=[p for p in ps if p['role']=='input'];outs=[p for p in ps if p['role']=='output']
   for j,p in enumerate(ins):
    py=y+5.5+j*1.9
    label=self.display_name(p['name'])+':'+str(p['number'])
    self.text(15.2,py+.55,label,4.4,BLACK,width=7.5)
    self.line([(13.5,py),(14.5,py)])
    if p['name'].lstrip('/').startswith('C-'):
     self.line([(14.5,py-.6),(15.1,py),(14.5,py+.6)],width=.15)
     if 'negative Taktflanke' in self.r['function']:self.circle(14.15,py,.3,width=.15)
   for j,p in enumerate(outs):
    py=y+6+j*4
    self.line([(30.5,py),(31.5,py)],BLUE)
    self.text(24,py+.5,self.display_name(p['name'])+':'+str(p['number']),4.6,BLUE,width=6)
   for p in ps:self.stub(p['number'])
  edge='CLK fällt' if 'negative Taktflanke' in self.r['function'] else 'CLK steigt' if 'positive Taktflanke' in self.r['function'] else 'CLK: siehe Referenz'
  self.text(22.5,45.5,edge,5.3,BLACK,'middle')

 def embedded(self):
  self.functional_ports()
  rec=SOURCES[self.r['key']];path=BASE/rec['image']
  with PILImage.open(path) as im:iw,ih=im.size
  scale=min(21.2/iw,35/ih);w=iw*scale;h=ih*scale
  self.d.add(Image((22.5-w/2)*MM,(55-8-(35+h)/2)*MM,w*MM,h*MM,str(path)))

 def functional_ports(self):
  self.rect(13,5.5,19,39.5)
  for p in self.pins.values():
   if p['name'] in ('VCC','GND','NC'):continue
   start=self.point_for_pin(p['number']);left=p['number']<=self.n//2
   self.line([start,(13 if left else 32,min(44.5,max(6,start[1])))],BLUE if p['role'] in ('output','tri_state','open_collector') else GREEN)
   self.connections.append(p['number'])

 def functional_block(self):
  self.functional_ports()
  num=self.num
  if num in (174,175,273,373,374,576):
   count=6 if num==174 else 4 if num==175 else 8
   title='D-LATCH' if num==373 else 'D-FLIPFLOPS'
   self.text(22.5,12,title,6,anchor='middle',width=17)
   for i in range(count):
    y=16+i*(3.1 if count==8 else 4.2)
    self.rect(16,y-1,13,2.6)
    self.text(22.5,y+.85,('D'+str(i+1)+' -> /Q'+str(i+1)) if num==576 else ('D'+str(i)+' -> '+('O' if num in (373,374) else 'Q')+str(i)),5.3,BLUE,'middle',width=12)
   self.text(22.5,44.1,'LE: transparent' if num==373 else 'Gemeinsamer CLK',4.8,BLACK,'middle',width=17)
  elif num==87:
   self.text(22.5,13,'4 × Funktion A -> Y',5.8,anchor='middle',width=17)
   for i,line in enumerate(('B C | Y','0 0 | /A','0 1 | A','1 0 | 1','1 1 | 0')):self.text(22.5,21+i*4,line,6.3,BLACK,'middle',i==0)
  else:
   caption={60:['2 EXPANDER','4 Eingänge je','X / X inv.'],83:['4-Bit-ADDER','A + B + Cin','-> S / Cout'],
    145:['BCD -> DEC','1 aus 10','OC-Ausgänge'],147:['PRIORITÄT','DEZ -> BCD'],148:['PRIORITÄT','8 -> 3'],
    165:['8-Bit','SCHIEBEREG.','Parallel ->','seriell'],166:['8-Bit','SCHIEBEREG.','Parallel /','seriell'],
    247:['BCD ->','7-SEGMENT','6 / 9 anders','OC'],248:['BCD ->','7-SEGMENT','6 / 9 anders'],
    253:['2 × 4:1','MULTIPLEXER','3-State'],279:['4 RS-LATCHES','S / R','aktiv Low'],
   }.get(num,[NAMES[num]])
   for i,line in enumerate(caption):self.text(22.5,18+i*4,line,6.6,BLACK,'middle',i==0,width=17)

 def draw(self):
  self.rect(.25,.25,44.5,54.5,colors.white,GREEN,.3);self.heading(3.15,8.2)
  f=self.r['function'];num=self.num;gate=None
  for g in ('XNOR','XOR','NAND','NOR','AND','OR'):
   if re.search(r'\b'+g+r'-(?:Gatter|Puffer)',f):gate=g;break
  if num in (51,54,55):gate=None
  if gate:self.primitive_gates(gate);layout='verdrahtete Gatter'
  elif num in (4,5,6,7,14,16):self.primitive_buffers();layout='verdrahtete Puffer/Inverter'
  elif num in (240,244,245,541,640,641):self.buses();layout='verdrahtete Bus-/Treiberkanäle'
  elif num in (73,74,76,107,109,112):self.flipflops();layout='Flipflops mit DIP-Pinzuordnung'
  elif self.r['key'] in SOURCES:self.embedded();layout='eingebettetes Hersteller-Logikbild mit Signalanschlüssen'
  else:self.functional_block();layout='Funktionsblöcke mit Signalanschlüssen'
  self.labels()
  if 'Open Collector' in f and num not in (145,247,266):self.text(22.5,46.2,'OC: Pull-up erforderlich',4.7,BLUE,'middle',width=26)
  if self.n==20:
   self.text(22.5,47.4,'Ref: '+self.r['reference'],4,BLACK,'middle',width=14)
   self.text(22.5,50,self.r['key'],5.2,GREEN,'middle',True,width=14)
   compact={240:'8 Inverter / 3-State',244:'8 Puffer / 3-State',245:'8-Bit-Bustransceiver',273:'8 D-FF / CLR',373:'8-Bit-Latch',374:'8 D-FF / 3-State',541:'8 Puffer / 3-State',576:'8 D-FF / Q inv.',640:'8-Bit-Bus / inv.',641:'8-Bit-Bus / OC'}[num]
   self.text(22.5,52,compact,4.6,BLACK,'middle',width=14)
   self.text(22.5,54.1,'20 Pins | Draufsicht',4,BLACK,'middle',width=14)
  else:
   self.text(22.5,48.2,'Ref: '+self.r['reference'],4.6,BLACK,'middle',width=41)
   self.heading(51.2,6.5)
   self.text(22.5,53.65,'Draufsicht | Überstrich: aktiv Low | '+str(self.n)+' Pins',4.8,BLACK,'middle',width=41)
  self.r.update(card_layout='SN7xxx im gemeinsamen Kartenstil',diagram_layout=layout,
                card_function_title=NAMES[num],first_pin_y_mm=6.4,
                wired_pin_numbers=sorted(set(self.connections)),
                card_pin_labels={str(p['number']):self.display_name(p['name']) for p in self.pins.values()})
  if self.r['key'] in SOURCES:self.r['logic_diagram_source']=SOURCES[self.r['key']]
  return self.d


def draw_sn(r):return SNCard(r).draw()
