# Manuell aus den angegebenen Hersteller-PDFs abgelesene DIP-Pinfolgen.
# Reihenfolge jeweils Pin 1 bis N, Draufsicht; / kennzeichnet aktiv Low.
MANUAL={
 'CD4042':('Q4 Q1 /Q1 D1 CLK POL D2 GND /Q2 Q2 Q3 /Q3 D3 D4 /Q4 VDD','Datenblaetter/CD4xxx/CD4042_TI.pdf',1),
 'CD4043':('Q4 Q1 R1 S1 EN S2 R2 GND Q2 Q3 R3 S3 NC S4 R4 VDD','Datenblaetter/CD4xxx/CD4043_TI.pdf',1),
 'SN74LS54N':('A B C D E Y GND NC F G H I J VCC','Datenblaetter/SN7xxx/SN74LS54N_TI.pdf',1),
 '7487':('C A1 Y1 NC A2 Y2 GND B Y3 A3 NC Y4 A4 VCC','Datenblaetter/SN7xxx/7487_TI_Datenbuchauszug.pdf',1),
 '7460':('1A 1B 1C 2A 2B 2C GND 2D 2X /2X /1X 1X 1D VCC','Datenblaetter/SN7xxx/7460_TI_Referenz.pdf',1),
 '74576':('/OE D1 D2 D3 D4 D5 D6 D7 D8 GND CLK /Q8 /Q7 /Q6 /Q5 /Q4 /Q3 /Q2 /Q1 VCC','Datenblaetter/SN7xxx/74576_TI_ALS576_Referenz.pdf',1),
 'CD4015':('CLK-B Q4-B Q3-A Q2-A Q1-A RST-A DATA-A GND CLK-A Q4-A Q3-B Q2-B Q1-B RST-B DATA-B VDD','Datenblaetter/CD4xxx/CD4015_TI.pdf',1),
 'CD4026':('CLK INHIBIT DISP-EN DISP-OUT CARRY f g GND d a e b c c-RAW RESET VDD','Datenblaetter/CD4xxx/CD4026_TI.pdf',1),
 'CD4063':('B3 LT-IN EQ-IN GT-IN GT-OUT EQ-OUT LT-OUT GND B0 A0 B1 A1 A2 B2 A3 VDD','Datenblaetter/CD4xxx/CD4063_TI.pdf',1),
 'CD4503':('DIS-A D1 Q1 D2 Q2 D3 Q3 GND Q4 D4 Q5 D5 Q6 D6 DIS-B VDD','Datenblaetter/CD4xxx/CD4503_TI.pdf',1),
 'CD4513':('B C /LT /BI LE D A RBI GND RBO e d c b a g f VDD','Datenblaetter/CD4xxx/CD4513_MC14513B_onsemi_Referenz.pdf',3),
 'CD4553':('/DS2 /DS1 CIB CIA Q3 Q2 Q1 GND Q0 LE DIS CLK MR OF /DS3 VDD','Datenblaetter/CD4xxx/CD4553_MC14553B_Motorola_Referenz.pdf',1),
 'COM8126':('XTAL1 XTAL2 VCC NC GND NC NC NC ST D C B A F-OUT','Datenblaetter/Diverse/COM8126_SMC_Datenbuchauszug.pdf',1),
 'MC1488':('V- 1A 1Y 2A 2B 2Y GND 3Y 3A 3B 4Y 4A 4B V+','Datenblaetter/Diverse/MC1488_TI_Referenz.pdf',1),
 'MC1489':('1A 1CONT 1Y 2A 2CONT 2Y GND 3Y 3CONT 3A 4Y 4CONT 4A VCC','Datenblaetter/Diverse/MC1489_TI_Referenz.pdf',1),
 'PS2501-4':('A1 K1 A2 K2 A3 K3 A4 K4 E4 C4 E3 C3 E2 C2 E1 C1','Datenblaetter/Diverse/PS2501_Renesas.pdf',1),
 'UA78S40PC':('DIODE-K DIODE-A SW-E OP-OUT OP-VCC OP+ OP- REF COMP+ COMP- GND CT VCC I-SENSE DRV-C SW-C','Datenblaetter/Diverse/UA78S40_onsemi_Referenz.pdf',1),
 'MAX250CPD':('/SHDN D1 T1-LED T1-IN T2-IN T2-LED GND /EN R1-OUT R1-LED R2-LED R2-OUT D2 VCC','Datenblaetter/Diverse/MAX250_MAX251_Maxim.pdf',1),
 'MPQ2222A':('C1 B1 E1 NC E2 B2 C2 C3 B3 E3 NC E4 B4 C4','Datenblaetter/Transistor/MPQ2222A_Central.pdf',2),
}
# Keine geratenen Verdrahtungsangaben für Typen ohne belastbare Pinquelle.
UNRESOLVED={'LH6764-20':'Herstellerdatenblatt / genaue Funktion fehlen'}
