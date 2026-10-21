"""Diverse cards: pin-connected symbols and embedded datasheet diagrams."""
from pathlib import Path
import json
import re
from PIL import Image as PILImage
from reportlab.graphics.shapes import Image, Path as ShapePath
from reportlab.lib import colors
from reportlab.pdfbase.pdfmetrics import stringWidth
from cd_cards import Card, MM, GREEN, BLUE, BLACK

BASE=Path(__file__).parent/'diverse_logikvorlagen'
SOURCES=json.loads((BASE/'quellen.json').read_text())
TITLES={
 'MC1455':'Timer / Multivibrator',
 'MCP3008-I_P':'8-Kanal-ADC, 10 Bit / SPI',
 'UA741CN':'Operationsverstärker / Offset',
 'COM8126':'Baudraten- / Frequenzgenerator', 'L293D':'4 Halbbrücken / Motortreiber',
 'L293NE':'4 Halbbrücken / Motortreiber', 'LH6764-20':'Identifikation offen',
 'LP324N':'4 Micropower-Operationsverstärker',
 'LM311N':'Komparator, offener Kollektor', 'LM324N':'4 Operationsverstärker',
 'LM339AN':'4 Komparatoren, offener Kollektor', 'LM358':'2 Operationsverstärker',
 'MAX250CPD':'Isolierte RS-232-Schnittstelle', 'MAX7219CNG':'8-stelliger LED-Treiber', 'MAX7221CNG':'8-stelliger SPI-LED-Treiber',
 'MC1488':'4 RS-232-Leitungstreiber', 'MC1489':'4 RS-232-Leitungsempfänger',
 'NE555':'Timer / Multivibrator', 'PCF8574N':'8-Bit-I/O-Expander, I2C',
 'PS2501-4':'4 Optokoppler', 'UA78S40PC':'Schaltregler-Steuerbaustein',
 'ULN2004A':'7 Darlington-Treiber', 'ULN2004AG':'7 Darlington-Treiber',
 'ULN2803A':'8 Darlington-Treiber',
}


class DiverseCard(Card):
 def pin_y(self,number):
  return 6.4+(number-1 if number<=self.n//2 else self.n-number)*self.r['pitch_mm']

 def heading(self,y,size):
  key=self.r['key'];title=TITLES[key];key=key.replace('_','/')
  size=min(size,size*41*MM/stringWidth(key+' '+title,'Helvetica-Bold',size))
  key_width=stringWidth(key+' ','Helvetica-Bold',size)
  x=(45*MM-key_width-stringWidth(title,'Helvetica',size))/2/MM
  self.text(x,y,key,size,GREEN,bold=True)
  self.text(x+key_width/MM,y,title,size,BLACK)

 def display_name(self,name):
  if self.r['key']=='LM311N' and name=='GND':return 'E-OUT'
  if self.r['key']=='LM311N' and name=='1Y':return 'C-OUT'
  return {'DIG_0':'DIG0','DIG_1':'DIG1','DIG_2':'DIG2','DIG_3':'DIG3',
          'DIG_4':'DIG4','DIG_5':'DIG5','DIG_6':'DIG6','DIG_7':'DIG7',
          'SEG_A':'a','SEG_B':'b','SEG_C':'c','SEG_D':'d','SEG_E':'e',
          'SEG_F':'f','SEG_G':'g','SEG_DP':'DP','/R':'/RESET',
          'XTAL1':'XTAL1','XTAL2':'XTAL2'}.get(name,name)

 def labels(self):
  compact=self.n==24
  for p in self.pins.values():
   num=p['number'];left=num<=self.n//2;y=self.pin_y(num);name=self.display_name(p['name'])
   supply=bool(re.fullmatch(r'V(?:DD|CC\d*|EE|\+|-)',name)) or name=='OP-VCC'
   ground=name in ('GND','AGND','DGND')
   output=p['role'] in ('output','tri_state','open_collector') or bool(re.match(r'^/?(?:\dY|Q$|O\d|R\d-OUT|OP-OUT|F-OUT|DOUT|DIG\d|[a-g]$|DP$)',name))
   if self.r['key']=='PS2501-4' and re.fullmatch('[CE][1-4]',name):output=True
   if self.r['key']=='LM311N' and name=='E-OUT':output=True
   if self.r['key']=='PCF8574N' and re.fullmatch('P[0-7]',name):output=True
   color=BLUE if output else GREEN
   if supply or ground:self.rect(.65 if left else 33,y-(.95 if compact else 1.25),11.35,1.9 if compact else 2.5,colors.HexColor('#ffa3a3') if supply else colors.HexColor('#c6d9ef'),None)
   x=2.2 if left else 42.8;size=5.3 if compact else 6.4
   self.circle(x,y,1.05 if compact else 1.65,width=.22 if compact else .28)
   self.text(x,y+(.52 if compact else .72),str(num),5.2 if compact else 7,GREEN,'middle',True)
   shown=name.lstrip('/');size=min(size,size*7.1*MM/max(stringWidth(shown,'Helvetica-Bold',size),.01))
   tx=4.3 if left else 40.7;self.text(tx,y+.6,shown,size,color,'start' if left else 'end',True)
   if name.startswith('/'):
    span=stringWidth(shown,'Helvetica-Bold',size)/MM
    self.line([(tx if left else tx-span,y-.85),(tx+span if left else tx,y-.85)],color,.14)

 def source_image(self,x,y,width,height,detail=False):
  rec=SOURCES[self.r['key']];path=BASE/rec['detail_image' if detail else 'image']
  with PILImage.open(path) as im:iw,ih=im.size
  scale=min(width/iw,height/ih);w=iw*scale;h=ih*scale
  self.d.add(Image((x+(width-w)/2)*MM,(55-y-(height+h)/2)*MM,w*MM,h*MM,str(path)))

 def triangle(self,x,y,left=False,width=6,height=6):
  sign=-1 if left else 1;back=x-sign*width/2;tip=x+sign*width/2
  path=ShapePath(fillColor=colors.white,strokeColor=GREEN,strokeWidth=.25*MM)
  path.moveTo(*self.xy(back,y-height/2));path.lineTo(*self.xy(tip,y));path.lineTo(*self.xy(back,y+height/2));path.closePath();self.d.add(path)
  return ((back,y-1.55),(back,y+1.55)),(tip,y)

 def amplifiers(self):
  key=self.r['key'];groups={}
  for p in self.pins.values():
   inp=re.fullmatch(r'IN(\d)([+-])',p['name']);out=re.fullmatch(r'(\d)Y',p['name'])
   if inp:groups.setdefault(int(inp[1]),{})[inp[2]]=p['number']
   if out:groups.setdefault(int(out[1]),{})['Y']=p['number']
  for unit,ps in sorted(groups.items()):
   left=ps['+']<=self.n//2;x=16 if left else 29
   y=(self.pin_y(ps['+'])+self.pin_y(ps['-']))/2
   ports,output=self.triangle(x,y,not left)
   for symbol,port in zip(sorted(('+','-'),key=lambda s:self.pin_y(ps[s])),ports):
    self.text(port[0]+(1 if left else -1),port[1]+.55,symbol,5.5,anchor='middle')
    self.wire(ps[symbol],port)
   self.text(x,y+.6,str(unit),5,anchor='middle')
   num=ps['Y'];py=self.pin_y(num);lane=x+(4.5+unit*.35) if left else x-(4.5+unit*.35)
   label_width=stringWidth(self.display_name(self.pins[num]['name']),'Helvetica-Bold',6.4)/MM
   end=4.3+label_width+.4 if num<=self.n//2 else 40.7-label_width-.4
   self.line([output,(lane,output[1]),(lane,py),(end,py)],BLUE)
   self.connections.append(num)
   if key=='LM339AN':self.text(x,y+4,'OC',4.5,BLUE,'middle')
  supply=' | '.join(p['name']+': '+str(p['number']) for p in self.pins.values() if p['name'] in ('V+','V-'))
  self.text(22.5,44,supply,5.4,BLACK,'middle',width=24)
  if key=='LM324N':self.text(22.5,46,'ST | Versorgung: 3 bis 30 V',5,BLACK,'middle',width=28)
  if key=='LP324N':self.text(22.5,46,'Iq gesamt: 85 uA typ. (Ref.)',4.8,BLACK,'middle',width=28)
  if key=='LM339AN':self.text(22.5,46,'OC: Pull-up am Ausgang',5.2,BLUE,'middle',width=27)

 def mc1455(self):
  self.pins[3]['role']='output';self.pins[7]['role']='open_collector'
  self.rect(13,8,19,17)
  self.text(22.5,11,'555-TIMER',6.5,anchor='middle',bold=True)
  self.text(22.5,15,'Komparatoren',5.3,anchor='middle')
  self.text(22.5,19,'RS-Speicher',5.5,anchor='middle')
  self.text(22.5,23,'Ausgang / Entladen',4.8,anchor='middle',width=18)
  for num in (2,3,4):self.wire(num,(13,self.pin_y(num)))
  for num in (5,6,7):self.wire(num,(32,self.pin_y(num)))
  self.text(22.5,31,'Astabil / Monostabil',6,anchor='middle',width=35)
  self.text(22.5,36,'Externe R / C bestimmen Zeit',5.3,anchor='middle',width=38)
  self.text(22.5,41,'CTRL: Steuerspannung',5.3,anchor='middle',width=35)
  self.text(22.5,45,'DISCH: Entladeausgang',5.3,anchor='middle',width=35)

 def ua741(self):
  self.pins[6]['role']='output'
  ports,out=self.triangle(22.5,15,width=13,height=12)
  self.text(17,14,'-',6,anchor='middle');self.text(17,17,'+',6,anchor='middle')
  self.wire(2,ports[0]);self.wire(3,ports[1]);self.wire(6,out)
  self.rect(13,29,19,8)
  self.text(22.5,32.3,'Offset-Abgleich',5.8,anchor='middle',width=18)
  self.text(22.5,35.3,'NULL1 / NULL2',5.3,anchor='middle')
  self.wire(1,(13,31));self.wire(5,(32,35))
  self.text(22.5,41,'V+: Pin 7 | V-: Pin 4',5.5,anchor='middle',width=30)
  self.text(22.5,45,'Pin 8: nicht beschalten',5.3,anchor='middle',width=30)

 def comparator(self):
  ports,out=self.triangle(22,14,width=7,height=8)
  self.text(19.6,13,'+',6,anchor='middle');self.text(19.6,16.1,'-',6,anchor='middle')
  self.wire(2,ports[0]);self.wire(3,ports[1])
  self.line([out,(28.4,14)])
  self.line([(28.4,12.5),(28.4,15.5)])
  self.line([(28.4,13.3),(30.5,11.7),(30.5,10.5),(35.2,10.5),(35.2,self.pin_y(7)),(36.2,self.pin_y(7))],BLUE)
  self.line([(28.4,14.7),(30.5,16.3),(30.5,19.3)],BLUE)
  self.line([(29.4,15.65),(30.5,16.3),(30.15,15.1)],BLUE,.15)
  self.text(30.5,21.1,'E: Pin 1',4.7,BLUE,'middle')
  self.text(27.6,9.2,'C: Pin 7',4.7,BLUE,'middle')
  self.connections.append(7)
  self.text(22.5,28,'BAL: 5 | STRB: 6',5.6,BLACK,'middle')
  self.text(22.5,32,'V+: 8 | V-: 4',5.6,BLACK,'middle')
  self.text(22.5,38,'Offener Kollektor',6.2,BLUE,'middle')
  self.text(22.5,41,'Pull-up am Ausgang',5.6,BLUE,'middle')
  self.text(22.5,45,'Emitter separat (Pin 1)',5.2,BLACK,'middle')

 def optocouplers(self):
  for i in range(4):
   a=1+2*i;k=a+1;c=16-2*i;e=c-1;y=(self.pin_y(a)+self.pin_y(k))/2
   self.rect(12.7,y-4.2,19.6,8.4)
   # LED and isolated phototransistor; no electrical connection across
   # the optical path in the middle.
   path=ShapePath(fillColor=None,strokeColor=GREEN,strokeWidth=.22*MM)
   path.moveTo(*self.xy(15.3,y-1.1));path.lineTo(*self.xy(17.7,y-1.1));path.lineTo(*self.xy(16.5,y+1.1));path.closePath();self.d.add(path)
   self.line([(15.2,y+1.2),(17.8,y+1.2)])
   self.line([(9.2,self.pin_y(a)),(16.5,self.pin_y(a)),(16.5,y-1.1)])
   self.line([(9.2,self.pin_y(k)),(16.5,self.pin_y(k)),(16.5,y+1.2)])
   for dy in (-1.0,.7):
    self.line([(19,y+dy),(22,y+dy+.7)]);self.line([(21.2,y+dy),(22,y+dy+.7),(21,y+dy+.85)],width=.16)
   self.line([(25.5,y-1.3),(25.5,y+1.3)])
   self.line([(25.5,y-.65),(28,y-1.8),(28,self.pin_y(c)),(36.2,self.pin_y(c))],BLUE)
   self.line([(25.5,y+.65),(28,y+1.8),(28,self.pin_y(e)),(36.2,self.pin_y(e))],BLUE)
   self.line([(26.9,y+1.65),(28,y+1.8),(27.45,y+.7)],BLUE,.16)
   self.text(22.5,y+3.8,str(i+1),4.8,anchor='middle')
   self.connections.extend((a,k,c,e))

 def darlingtons(self):
  count=8 if self.n==18 else 7
  for i in range(count):
   inp=i+1;out=self.n-i;y=self.pin_y(inp)
   self.line([(8.8,y),(15.8,y)])
   self.rect(14.2,y-.45,1.5,.9,colors.white,width=.15)
   self.line([(15.8,y),(16.7,y)])
   self.line([(16.7,y-.65),(16.7,y+.65)])
   self.line([(16.7,y-.35),(18.3,y-.95),(20.8,y-.95),(25.8,y-.95),(25.8,y),(36.2,y)],BLUE)
   self.line([(16.7,y+.35),(18.3,y+.95),(19.7,y+.95),(19.7,y)])
   self.line([(19.7,y-.65),(19.7,y+.65)])
   self.line([(19.7,y-.35),(20.8,y-.95)],BLUE)
   self.line([(19.7,y+.35),(21.4,y+1.1),(23.3,y+1.1)])
   self.line([(17.7,y+.8),(18.3,y+.95),(18.1,y+.4)],width=.15)
   self.line([(20.7,y+.95),(21.4,y+1.1),(21.05,y+.4)],width=.15)
   # Clamp diode branches off the output to the shared COM rail.
   self.line([(25.8,y),(25.8,y-1.8),(27.1,y-1.8)])
   path=ShapePath(fillColor=GREEN,strokeColor=GREEN,strokeWidth=.12*MM)
   path.moveTo(*self.xy(27.1,y-2.3));path.lineTo(*self.xy(28.1,y-1.8));path.lineTo(*self.xy(27.1,y-1.3));path.closePath();self.d.add(path)
   self.line([(28.1,y-2.35),(28.1,y-1.25)]);self.line([(28.1,y-1.8),(30.3,y-1.8)])
   self.circle(25.8,y,.18,fill=BLUE,color=BLUE,width=.1)
   self.text(13.8,y+1.7,str(i+1),4.4,anchor='middle')
   self.connections.extend((inp,out))
  ground=count+1;com=count+2
  self.line([(23.3,7.5),(23.3,self.pin_y(ground)),(10,self.pin_y(ground))])
  self.line([(30.3,4.6),(30.3,self.pin_y(com)),(35.3,self.pin_y(com))])
  self.connections.extend((ground,com))
  if self.n==16:self.text(22.5,46.1,'COM: Freilaufdioden',4.8,BLACK,'middle',width=23)

 def motor_drivers(self):
  for i,(a,out,en) in enumerate(((2,3,1),(7,6,1),(10,11,9),(15,14,9))):
   left=a<=self.n//2;x=16 if left else 29;y=(self.pin_y(a)+self.pin_y(out))/2
   sign=1 if self.pin_y(out)>self.pin_y(a) else -1
   path=ShapePath(fillColor=colors.white,strokeColor=GREEN,strokeWidth=.25*MM)
   for j,(px,py) in enumerate(((x-2,y-sign*1.8),(x+2,y-sign*1.8),(x,y+sign*1.8))):
    (path.moveTo if j==0 else path.lineTo)(*self.xy(px,py))
   path.closePath();self.d.add(path)
   start=8.8 if left else 36.2
   self.line([(start,self.pin_y(a)),(x,self.pin_y(a)),(x,y-sign*1.8)])
   self.line([(start,self.pin_y(out)),(x,self.pin_y(out)),(x,y+sign*1.8)],BLUE)
   rail=22 if left else 24
   self.line([(rail,y),(x+1 if left else x-1,y)])
   self.text(x,y+.5,str(i+1),4.6,anchor='middle')
   self.connections.extend((a,out,en))
  self.line([(8.8,self.pin_y(1)),(22,self.pin_y(1)),(22,35)])
  self.line([(36.2,self.pin_y(9)),(24,self.pin_y(9)),(24,13)])
  self.text(22.5,43.8,'VCC1: Logik / VCC2: Last',4.8,BLACK,'middle',width=22)
  self.text(22.5,46,'Freilaufdioden integriert' if self.r['key']=='L293D' else 'Externe Freilaufdioden',5,BLACK,'middle',width=28)

 def line_receivers(self):
  for i,(a,ctrl,out) in enumerate(((1,2,3),(4,5,6),(10,9,8),(13,12,11))):
   left=a<=self.n//2;x=16 if left else 29
   y=(self.pin_y(a)+self.pin_y(out))/2
   ports,tip=self.triangle(x,y,not left,width=5,height=4)
   back=x-2.5 if left else x+2.5
   sign=1 if left else -1
   self.circle(tip[0]+sign*.4,y,.4,width=.18)
   self.wire(a,(back,y));self.wire(out,(tip[0]+sign*.8,y))
   self.text(x,y+.55,'ST',4.4,anchor='middle')
   bend=x-4.5 if left else x+4.5
   self.line([(10.7 if left else 34.3,self.pin_y(ctrl)),(bend,self.pin_y(ctrl)),(bend,y+3),(x,y+3),(x,y+1)])
   self.connections.append(ctrl)
   self.text(x,y+3.8,str(i+1),4.4,anchor='middle')
  self.text(22.5,45,'CONT: Schwellwert / Antwort',4.9,BLACK,'middle',width=29)

 def embedded_block(self):
  key=self.r['key'];top=6 if self.n!=24 else 5;bottom=44 if self.n!=24 else 37
  self.rect(12,top,21,bottom-top,stroke=GREEN,width=.17)
  for p in self.pins.values():
   name=p['name'];num=p['number'];left=num<=self.n//2
   if name=='NC' or re.fullmatch(r'V(?:DD|CC\d*|EE|\+|-)',name) or name in ('GND','OP-VCC'):continue
   py=self.pin_y(num);sy=min(bottom-.4,max(top+.4,py))
   self.line([(11.5 if left else 33.5,py),(12 if left else 33,sy)],width=.2)
   self.connections.append(num)
  if key=='NE555':
   self.text(22.5,11,'555',9,anchor='middle',bold=True)
   self.text(22.5,17,'TR / THR',6,anchor='middle');self.text(22.5,22,'RS-Latch / OUT',5.6,anchor='middle')
   # An 8-pin package leaves room below the pin rows for a larger figure.
   self.rect(11.9,23.4,21.2,20.7,colors.white,None)
   self.source_image(4,25.2,37,21.4)
  else:
   self.source_image(12.4,top+1.2,20.2,bottom-top-2.4)
   if key=='MAX7219CNG':
    self.text(22.5,40,'DIN / CLK / LOAD -> Register',4.9,BLACK,'middle',width=30)
    self.text(22.5,43,'DIG: Stellen | a..g, DP: Segmente',4.9,BLACK,'middle',width=32)
    self.text(22.5,46,'ISET: Segmentstrom',5.2,BLACK,'middle')
   elif key=='PCF8574N':self.text(22.5,46.5,'P0..P7: bidirektional',5.1,BLUE,'middle')

 def baud_generator(self):
  self.rect(12.5,5.5,8,10)
  self.text(16.5,9.2,'XTAL',5.7,anchor='middle');self.text(16.5,12.4,'OSC',5.7,anchor='middle')
  self.wire(1,(12.5,self.pin_y(1)));self.wire(2,(12.5,self.pin_y(2)))
  self.rect(22.5,9.5,7.5,24)
  for i,t in enumerate(('D-Latch','Decoder','Frequenz-','ROM')):self.text(26.2,15+i*3.4,t,4.9,anchor='middle',width=6.7)
  for num in (9,10,11,12,13):self.wire(num,(30,self.pin_y(num)))
  self.rect(12.5,22,8,10);self.text(16.5,26,'Teiler',5.8,anchor='middle');self.text(16.5,29,'/ 2',5.8,anchor='middle')
  self.line([(16.5,15.5),(16.5,22)])
  self.line([(22.5,27),(20.5,27)])
  self.line([(16.5,32),(16.5,35),(32,35),(32,self.pin_y(14)),(34.4,self.pin_y(14))],BLUE)
  self.connections.append(14)
  self.source_image(11.5,37,22,9.5)

 def led_driver(self):
  # Reflow the manufacturer's wide figure into legible card-sized stages.
  self.rect(18,5.1,9,7)
  self.text(22.5,7.7,'16-Bit',5.5,anchor='middle',bold=True)
  self.text(22.5,10,'Schiebe-Reg.',4.5,anchor='middle',width=8)
  self.wire(1,(18,self.pin_y(1)));self.wire(24,(27,self.pin_y(24)))
  self.rect(18,15,9,14)
  for i,t in enumerate(('Register','8 × 8 RAM','Decoder','PWM / Scan')):self.text(22.5,18+i*3,t,4.7,anchor='middle',width=8)
  self.line([(22.5,12.1),(22.5,15)])
  self.text(22.5,13.8,'CLK:13 / CS:12' if self.r['key']=='MAX7221CNG' else 'CLK:13 / LOAD:12',4.1,BLACK,'middle',width=15)
  self.line([(11.4,self.pin_y(12)),(17,self.pin_y(12))]);self.connections.append(12)
  self.line([(33.6,self.pin_y(13)),(28,self.pin_y(13))]);self.connections.append(13)
  for p in self.pins.values():
   num=p['number'];y=self.pin_y(num);name=self.display_name(p['name'])
   if name.startswith('DIG'):
    self.rect(12.2,y-.7,4.3,1.4)
    self.text(14.35,y+.43,name.replace('DIG','D'),4.1,BLUE,'middle')
    self.line([(9.3,y),(12.2,y)],BLUE)
    self.line([(16.5,y),(17.2,y)])
    self.connections.append(num)
   elif name in tuple('abcdefg')+('DP',):
    self.rect(28.5,y-.7,4.3,1.4)
    self.text(30.65,y+.43,name,4.1,BLUE,'middle')
    self.line([(32.8,y),(35,y)],BLUE)
    self.line([(27.8,y),(28.5,y)])
    self.connections.append(num)
  self.line([(17.2,8.94),(17.2,31.8),(18,27)])
  self.line([(27.8,8.94),(27.8,31.8),(27,27)])
  self.text(22.5,31.6,'ISET:18',4.5,BLACK,'middle')
  self.wire(18,(27,self.pin_y(18)))
  self.text(22.5,36.2,'DIG: Stellen | SEG: Segmente',4.8,BLACK,'middle',width=28)
  self.source_image(12,37,21,9.5)

 def io_expander(self):
  self.rect(13,5.5,19,13)
  self.text(22.5,9,'I2C-Interface',6,anchor='middle')
  self.text(22.5,13,'Adresse: A0..A2',5.6,anchor='middle')
  self.text(22.5,16.8,'SCL / SDA',5.7,anchor='middle')
  for num in (1,2,3):self.wire(num,(13,self.pin_y(num)))
  for num in (14,15):self.wire(num,(32,self.pin_y(num)))
  self.rect(13,20,19,23.5)
  self.text(22.5,22.9,'8-Bit-Register / GPIO',5.5,anchor='middle',width=18)
  self.line([(22.5,18.5),(22.5,20)])
  self.wire(13,(32,self.pin_y(13)))
  for num in range(4,8):self.wire(num,(13,max(25,self.pin_y(num))))
  for num in range(9,13):self.wire(num,(32,self.pin_y(num)))
  self.source_image(15,25,15,17.5,detail=True)
  self.text(22.5,46,'P0..P7: bidirektional',5.2,BLUE,'middle')

 def adc3008(self):
  self.rect(12,5.8,7,37)
  self.text(15.5,18,'8:1',6,anchor='middle')
  self.text(15.5,22,'MUX',5.5,anchor='middle')
  for num in range(1,9):self.wire(num,(12,self.pin_y(num)))
  self.rect(21,17,8,12)
  for i,t in enumerate(('S/H','10-Bit','SAR-ADC')):self.text(25,20+i*3,t,5,anchor='middle')
  self.line([(19,24),(21,24)])
  self.rect(21,32,8,10)
  self.text(25,36,'SPI',6,anchor='middle')
  self.line([(25,29),(25,32)])
  for num,y in ((10,40),(11,38),(12,36),(13,34)):self.wire(num,(29,y))
  self.wire(15,(29,18));self.wire(16,(29,15))
  self.text(22.5,46,'2,7..5,5 V | AGND + DGND verbinden',4.8,BLACK,'middle',width=40)

 def draw(self):
  self.rect(.25,.25,44.5,54.5,colors.white,GREEN,.3);self.heading(3.15,8.2)
  key=self.r['key']
  if not self.n:
   self.rect(3,11,39,28,colors.HexColor('#fff1dc'),colors.HexColor('#ae6514'))
   self.text(22.5,18,'ZUORDNUNG OFFEN',8,BLACK,'middle',True)
   self.text(22.5,25,'Keine dokumentierte Pinbelegung',6.1,BLACK,'middle')
   self.text(22.5,32,'Nicht zum Verdrahten verwenden',6.1,BLACK,'middle')
   if self.r.get('marking'):self.text(22.5,36.5,'Aufdruck: '+self.r['marking'],5.8,BLACK,'middle')
   layout='Identifikationskarte'
  elif key in ('LM324N','LP324N','LM339AN','LM358'):self.amplifiers();layout='verdrahtete Verstärker-/Komparatorsymbole'
  elif key=='MCP3008-I_P':self.adc3008();layout='Analog-Multiplexer, SAR-ADC und SPI mit Pinzuordnung'
  elif key=='MC1455':self.mc1455();layout='Timer-Funktionsblock mit DIP-Pinzuordnung'
  elif key=='UA741CN':self.ua741();layout='Operationsverstärker mit Offset-Abgleich und DIP-Pins'
  elif key=='LM311N':self.comparator();layout='Komparator mit Ausgangstransistor'
  elif key=='PS2501-4':self.optocouplers();layout='verdrahtete Optokoppler'
  elif key.startswith('ULN'):self.darlingtons();layout='verdrahtete Darlington-Stufen mit Freilaufdioden'
  elif key in ('L293D','L293NE'):self.motor_drivers();layout='verdrahtete Halbbrücken mit Enable'
  elif key=='MC1489':self.line_receivers();layout='verdrahtete Leitungsempfänger'
  elif key=='COM8126':self.baud_generator();layout='verdrahteter Frequenzgenerator und Datenblatt-Diagramm'
  elif key in ('MAX7219CNG','MAX7221CNG'):self.led_driver();layout='LED-Treiberstufen und Datenblatt-Diagramm'
  elif key=='PCF8574N':self.io_expander();layout='I2C-Interface und Datenblatt-GPIO-Diagramm'
  elif key=='MC1488':
   # The native pin-connected logic is equivalent to the manufacturer's
   # inverter plus three NAND stages, with bipolar line-driver outputs.
   groups=((2,3),(4,5,6),(9,10,8),(12,13,11))
   for i,ps in enumerate(groups):
    left=ps[0]<=self.n//2;x=16 if left else 29;y=sum(self.pin_y(n) for n in ps)/len(ps)
    self.rect(x-3,y-3,6,6)
    self.text(x,y+.6,'INV' if i==0 else 'NAND',4.8,anchor='middle')
    for j,num in enumerate(ps):self.wire(num,(x-3 if num<=self.n//2 else x+3,y-1.5+j*1.5))
   self.text(22.5,45,'TTL -> RS-232',5.6,BLUE,'middle');layout='verdrahtete RS-232-Leitungstreiber'
  else:self.embedded_block();layout='eingebettetes Datenblatt-Schaltbild mit Signalanschlüssen'
  if self.n:self.labels();self.text(22.5,49.2 if self.n==18 else 48.2,'Ref: '+self.r['reference'],4.6,BLACK,'middle',width=41)
  self.heading(52 if self.n==18 else 51.2,6 if self.n==18 else 6.5)
  self.text(22.5,54.1 if self.n==18 else 53.65,'Draufsicht | Überstrich: aktiv Low'+(' | '+str(self.n)+' Pins' if self.n else ''),4.5 if self.n==18 else 4.8,BLACK,'middle',width=41)
  self.r.update(card_layout='Diverse im Stil der CD4xxx-Karten',diagram_layout=layout,
                card_function_title=TITLES[key],wired_pin_numbers=sorted(set(self.connections)),
                card_pin_labels={str(p['number']):self.display_name(p['name']) for p in self.pins.values()})
  if self.n:self.r['first_pin_y_mm']=6.4
  if key in SOURCES:self.r['logic_diagram_source']=SOURCES[key]
  return self.d


def draw_diverse(r):return DiverseCard(r).draw()
