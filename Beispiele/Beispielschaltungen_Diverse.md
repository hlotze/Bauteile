# Schaltungsbeispiele: Diverse

[Übersicht](README.md) · [Gesamtsammlung](Beispielschaltungen.md) · [Recherchebedarf](Recherchebedarf.md) · [Bestand](../Bauteile.md)

31 Bauteile, 170 Linkzuordnungen. Erweiterungsstand: **25.10.2026**; Prüfdatum jeweils am Link.

Ziel sind etwa **fünf unterschiedliche Websites pro Bauteil**. Gezählt werden Websites mit Schaltungsbeispielen, übertragbaren Grundschaltungen, Modulbeispielen oder Code mit Anschlusszuordnung. Reine Funktions-/Prinzipreferenzen und Entwurfshilfen zählen zusätzlich als Quellen, aber nicht zum Beispielziel. Subdomains und bekannte Länderspiegel zählen zusammen. Mehrere Artikel derselben Website erhöhen die Zahl nicht.

**Grundschaltung** bedeutet: Das Schaltungsprinzip ist übertragbar, der Artikel verwendet gegebenenfalls ein anderes Bauteil. Sie ist keine Bestätigung der Pinbelegung oder Dimensionierung des vorhandenen Typs. **Modulbeispiele** enthalten zusätzliche Komponenten; **Funktionsreferenzen** sind keine vollständigen Nachbauschaltungen. Hinweise stehen direkt beim Bauteil und Link.

Versorgung, Pinfolge, Polarität, Logikfamilie, Freigaben, Taktflanken und Grenzwerte anhand des konkreten Datenblatts prüfen. 74LS benötigt +5 V. Pro IC üblicherweise 100 nF abblocken, Taster für Zähler entprellen. Transistor- und Diodenwerte an Last und Verlustleistung anpassen. Bei Relais gilt die tatsächliche Spulenspannung. TRIAC-Artikel können Netzspannungsschaltungen enthalten.

Pflege: [Beispielschaltungen.json](Beispielschaltungen.json). `python3 scripts/update_examples.py` erzeugt ausschließlich diese Sammlungen. Bestand und Datenbank bleiben unverändert. Bei lokalen PDFs führt „Online-Original“ zur dokumentierten Downloadquelle; neuere Revisionen können andere Seitenzahlen haben.

## B3CA4.5Z

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Relais mit Treiberarray (TI) (PDF S. 16)](../Datenblaetter/Diverse/ULN2004A_TI_Referenz.pdf#page=16) · [Online-Original](https://www.ti.com/lit/ds/symlink/uln2004a.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.

Treiberbeispiel auf Spulennennspannung und -strom des vorhandenen Relais auslegen; keine direkte Gleichsetzung mit der Beispielspule. Relaistreiber-Grundschaltungen: Spulennennspannung, Spulenstrom und Anschlussbild des vorhandenen Relais verwenden; Freilaufdiode nur bei Gleichstromspulen. Referenzrelais der Quelle ist nicht der vorhandene Typ.

## COM8126

**1/5 Beispiel-Websites**, 1 Quellen-Websites insgesamt. Weitere passende Beispiele gesucht.

- [Quarz-/Takteingang (SMC) (PDF S. 17)](../Datenblaetter/Diverse/COM8126_COM8146_SMC.pdf#page=17) · [Online-Original](https://electrickery.hosting.philpem.me.uk/comp/divcomp/doc/SMC_BaudGen.pdf) — electrickery.hosting.philpem.me.uk; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.

**Recherchebedarf:** Herstellerbeschaltung und Teilerzuordnung vorhanden; weitere Fundstellen waren überwiegend Kopien desselben Datenbuchs und werden nicht als unabhängige Beispiele gezählt.

## DIP05-1A72-12L

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Relais mit Treiberarray (TI) (PDF S. 16)](../Datenblaetter/Diverse/ULN2004A_TI_Referenz.pdf#page=16) · [Online-Original](https://www.ti.com/lit/ds/symlink/uln2004a.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.

Treiberbeispiel auf Spulennennspannung und -strom des vorhandenen Relais auslegen; keine direkte Gleichsetzung mit der Beispielspule. Relaistreiber-Grundschaltungen: Spulennennspannung, Spulenstrom und Anschlussbild des vorhandenen Relais verwenden; Freilaufdiode nur bei Gleichstromspulen. Referenzrelais der Quelle ist nicht der vorhandene Typ.

## L293D

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [DC-Motorsteuerung (TI) (PDF S. 9)](../Datenblaetter/Diverse/L293_TI.pdf#page=9) · [Online-Original](https://www.ti.com/lit/ds/symlink/l293.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [L293D auf dem Steckbrett mit Schrittmotor](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-10-stepper-motors/hardware-l293d) — adafruit.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [Zwei Gleichstrommotoren mit L293D und Arduino](https://blog.codebender.cc/2015/08/09/tutorial-how-to-use-the-l293d-motor-driver-ic/) — blog.codebender.cc; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [L293D/L298N: Drehrichtung und PWM mit 8051](https://technobyte.org/8051-dc-motor-interfacing-l293d-l298n-pwm/) — technobyte.org; Grundschaltung; geprüft 2026-10-25.
- [Motorsteuerung mit L298N und Arduino](https://www.learnrobotics.org/blog/how-to-use-l298n-motor-driver/) — learnrobotics.org; Grundschaltung; geprüft 2026-10-25.
- [L298N-Modul: PWM und Drehrichtung mit ESP32](https://randomnerdtutorials.com/esp32-dc-motor-l298n-motor-driver-control-speed-direction/) — randomnerdtutorials.com; Modulbeispiel; geprüft 2026-10-25.

L293 benötigt externe Freilaufdioden; L293D enthält Schutzdioden. Passende Variante des gemeinsamen Datenblatts verwenden. H-Brücken-Grundschaltungen mit unterschiedlichen Treibern: Versorgung, Enable, Pinfolge und Stromgrenzen separat prüfen. L293NE und L298N benötigen externe Freilaufdioden; L293D integriert diese. Ein L298N-Modul enthält zusätzliche Bauteile und ist nicht mit dem nackten IC gleichzusetzen.

## L293NE

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [DC-Motorsteuerung (TI) (PDF S. 9)](../Datenblaetter/Diverse/L293_TI.pdf#page=9) · [Online-Original](https://www.ti.com/lit/ds/symlink/l293.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [L293D auf dem Steckbrett mit Schrittmotor](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-10-stepper-motors/hardware-l293d) — adafruit.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [Zwei Gleichstrommotoren mit L293D und Arduino](https://blog.codebender.cc/2015/08/09/tutorial-how-to-use-the-l293d-motor-driver-ic/) — blog.codebender.cc; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [L293D/L298N: Drehrichtung und PWM mit 8051](https://technobyte.org/8051-dc-motor-interfacing-l293d-l298n-pwm/) — technobyte.org; Grundschaltung; geprüft 2026-10-25.
- [Motorsteuerung mit L298N und Arduino](https://www.learnrobotics.org/blog/how-to-use-l298n-motor-driver/) — learnrobotics.org; Grundschaltung; geprüft 2026-10-25.
- [L298N-Modul: PWM und Drehrichtung mit ESP32](https://randomnerdtutorials.com/esp32-dc-motor-l298n-motor-driver-control-speed-direction/) — randomnerdtutorials.com; Modulbeispiel; geprüft 2026-10-25.

L293 benötigt externe Freilaufdioden; L293D enthält Schutzdioden. Passende Variante des gemeinsamen Datenblatts verwenden. H-Brücken-Grundschaltungen mit unterschiedlichen Treibern: Versorgung, Enable, Pinfolge und Stromgrenzen separat prüfen. L293NE und L298N benötigen externe Freilaufdioden; L293D integriert diese. Ein L298N-Modul enthält zusätzliche Bauteile und ist nicht mit dem nackten IC gleichzusetzen.

## LH6764-20

**0/5 Beispiel-Websites**, 0 Quellen-Websites insgesamt. Weitere passende Beispiele gesucht.

Noch kein belastbares Schaltungsbeispiel zugeordnet.

Kein seriöses Schaltungsbeispiel zuordenbar: Typfunktion und Herstellerdatenblatt weiterhin ungeklärt.

**Recherchebedarf:** Funktion und Typzuordnung ungeklärt. Deshalb keine Ersatztypen-Schaltung zugeordnet.

## LM311N

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Schwellwertschalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-6/voltage-comparator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Komparator-Beispiele (ST-Referenz) (PDF S. 7)](../Datenblaetter/Diverse/LM339_ST_Historisch.pdf#page=7) · [Online-Original](https://docs.rs-online.com/fbf7/0900766b80ecccbe.pdf) — docs.rs-online.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Invertierender/nichtinvertierender Verstärker und Komparator](https://www.renesas.com/en/support/engineer-school/electronic-circuits-03-op-amps-comparator-circuit) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Schwellwertschalter und Komparator mit Hysterese](https://learnabout-electronics.org/Amplifiers/amplifiers62.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Komparatorschaltungen und Grenzen von OPVs](https://www.electronics-notes.com/articles/analogue_circuits/operational-amplifier-op-amp/comparator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.
- [Komparator, Hysterese und Ausgangsbeschaltung](https://www.analog.com/en/resources/technical-articles/selecting-the-right-comparator.html) — analog.com; Entwurfshilfe; geprüft 2026-10-25.

Komparator-Grundschaltungen: Open-Collector-Pull-up und beim LM311 den separaten Ausgangsemitter berücksichtigen. Komparatoren mit Open-Collector-Ausgang benötigen einen Pull-up. LM311/LM339 nicht als lineare Operationsverstärker beschalten.

## LM324N

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Single-Supply-Beispiele (ST) (PDF S. 9)](../Datenblaetter/Diverse/LM324_ST.pdf#page=9) · [Online-Original](https://chipdatasheet.com/wp-content/uploads/2023/02/STMICROELECTRONICS-LM324.pdf) — chipdatasheet.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Nichtinvertierender Verstärker (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-6/noninverting-amplifier/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Spannungsfolger (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-6/precision-voltage-follower/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Invertierender/nichtinvertierender Verstärker und Komparator](https://www.renesas.com/en/support/engineer-school/electronic-circuits-03-op-amps-comparator-circuit) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [OPV-Anwendungen und Schaltungsgrenzen](https://wiki.analog.com/university/courses/electronics/text/chapter-4) — analog.com; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbau: Spannungsfolger und nichtinvertierender Verstärker](https://physicslabs.colorado.edu/courses/phys-3330/lab-guides/lab4/) — physicslabs.colorado.edu; Grundschaltung; geprüft 2026-10-25.
- [OPV-Verstärker mit Gegenkopplung](https://learnabout-electronics.org/Amplifiers/amplifiers66.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundschaltungen: Versorgung, Eingangsspannungsbereich, Ausgangshub und Verstärkerpins an den konkreten OPV anpassen; insbesondere UA741 nicht wie einen Rail-to-Rail-OPV behandeln. OPV-Grundschaltung mit anderen Referenztypen: Versorgung, Eingangs-Gleichtaktbereich und Ausgangshub prüfen. UA741 ist kein für allgemeine 5-V-Einversorgung geeigneter Ersatz für LM358.

## LP324N

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Micropower-Beispiele (TI) (PDF S. 7)](../Datenblaetter/Diverse/LP324N_TI_National.pdf#page=7) · [Online-Original](https://www.ti.com/lit/ds/symlink/lp324-n.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Nichtinvertierender Verstärker (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-6/noninverting-amplifier/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Spannungsfolger (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-6/precision-voltage-follower/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Invertierender/nichtinvertierender Verstärker und Komparator](https://www.renesas.com/en/support/engineer-school/electronic-circuits-03-op-amps-comparator-circuit) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [OPV-Anwendungen und Schaltungsgrenzen](https://wiki.analog.com/university/courses/electronics/text/chapter-4) — analog.com; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbau: Spannungsfolger und nichtinvertierender Verstärker](https://physicslabs.colorado.edu/courses/phys-3330/lab-guides/lab4/) — physicslabs.colorado.edu; Grundschaltung; geprüft 2026-10-25.
- [OPV-Verstärker mit Gegenkopplung](https://learnabout-electronics.org/Amplifiers/amplifiers66.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundschaltungen: Versorgung, Eingangsspannungsbereich, Ausgangshub und Verstärkerpins an den konkreten OPV anpassen; insbesondere UA741 nicht wie einen Rail-to-Rail-OPV behandeln. OPV-Grundschaltung mit anderen Referenztypen: Versorgung, Eingangs-Gleichtaktbereich und Ausgangshub prüfen. UA741 ist kein für allgemeine 5-V-Einversorgung geeigneter Ersatz für LM358.

## LM339AN

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Schwellwertschalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-6/voltage-comparator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Komparator-Beispiele (ST-Referenz) (PDF S. 7)](../Datenblaetter/Diverse/LM339_ST_Historisch.pdf#page=7) · [Online-Original](https://docs.rs-online.com/fbf7/0900766b80ecccbe.pdf) — docs.rs-online.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Invertierender/nichtinvertierender Verstärker und Komparator](https://www.renesas.com/en/support/engineer-school/electronic-circuits-03-op-amps-comparator-circuit) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Schwellwertschalter und Komparator mit Hysterese](https://learnabout-electronics.org/Amplifiers/amplifiers62.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Komparatorschaltungen und Grenzen von OPVs](https://www.electronics-notes.com/articles/analogue_circuits/operational-amplifier-op-amp/comparator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.
- [Komparator, Hysterese und Ausgangsbeschaltung](https://www.analog.com/en/resources/technical-articles/selecting-the-right-comparator.html) — analog.com; Entwurfshilfe; geprüft 2026-10-25.

Komparator-Grundschaltungen: Open-Collector-Pull-up und beim LM311 den separaten Ausgangsemitter berücksichtigen. Komparatoren mit Open-Collector-Ausgang benötigen einen Pull-up. LM311/LM339 nicht als lineare Operationsverstärker beschalten.

## LM358

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Anwendungsschaltung (TI) (PDF S. 27)](../Datenblaetter/Diverse/LM358_TI_Referenz.pdf#page=27) · [Online-Original](https://www.ti.com/lit/ds/symlink/lm358.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Nichtinvertierender Verstärker (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-6/noninverting-amplifier/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Spannungsfolger (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-6/precision-voltage-follower/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Invertierender/nichtinvertierender Verstärker und Komparator](https://www.renesas.com/en/support/engineer-school/electronic-circuits-03-op-amps-comparator-circuit) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [OPV-Anwendungen und Schaltungsgrenzen](https://wiki.analog.com/university/courses/electronics/text/chapter-4) — analog.com; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbau: Spannungsfolger und nichtinvertierender Verstärker](https://physicslabs.colorado.edu/courses/phys-3330/lab-guides/lab4/) — physicslabs.colorado.edu; Grundschaltung; geprüft 2026-10-25.
- [OPV-Verstärker mit Gegenkopplung](https://learnabout-electronics.org/Amplifiers/amplifiers66.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundschaltungen: Versorgung, Eingangsspannungsbereich, Ausgangshub und Verstärkerpins an den konkreten OPV anpassen; insbesondere UA741 nicht wie einen Rail-to-Rail-OPV behandeln. OPV-Grundschaltung mit anderen Referenztypen: Versorgung, Eingangs-Gleichtaktbereich und Ausgangshub prüfen. UA741 ist kein für allgemeine 5-V-Einversorgung geeigneter Ersatz für LM358.

## MAX250CPD

**3/5 Beispiel-Websites**, 3 Quellen-Websites insgesamt. Weitere passende Beispiele gesucht.

- [Isolierte RS-232-Schnittstelle (Maxim) (PDF S. 8)](../Datenblaetter/Diverse/MAX250_MAX251_Maxim.pdf#page=8) · [Online-Original](https://datasheet4u.com/pdf/448364/MAX251.pdf) — datasheet4u.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [MAX250/MAX251 als isolierte Schnittstelle im Zählerprojekt](https://mtn.sun.ac.za/files/2014/04/Smart3PhaseMeter_Brink.pdf) — mtn.sun.ac.za; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [MAX250/MAX251 im optisch isolierten Telepräsenz-Link](https://www.krafti.co.uk/steve/pdfs/msc_main.pdf) — krafti.co.uk; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.

Beispiel benötigt MAX250/MAX251, Optokoppler und isolierte Versorgung wie im Datenblatt.

**Recherchebedarf:** Bisher sind weniger als fünf unterschiedliche Websites mit passenden Beispielen belegt. Die vorhandenen Grundschaltungen und Referenzen sind oben gekennzeichnet; es wurden keine zusätzlichen Beschaltungen erfunden.

## MAX7219CNG

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [8-stellige LED-Anzeige (Maxim) (PDF S. 1)](../Datenblaetter/Diverse/MAX7219_Maxim.pdf#page=1) · [Online-Original](https://datasheet4u.com/pdf/1474108/MAX7219.pdf) — datasheet4u.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [MAX7219/MAX7221: Anzeige- und Kaskadierbeschaltung](https://www.analog.com/media/en/technical-documentation/data-sheets/MAX7219-MAX7221.pdf) — analog.com; Herstellerbeispiel; geprüft 2026-10-25.
- [MAX7219-Matrix: Laufschrift und Animationen](https://www.makerguides.com/max7219-led-dot-matrix-display-arduino-tutorial/) — makerguides.com; Modulbeispiel; geprüft 2026-10-25.
- [MAX7219-Matrix an Arduino und mehrere Module](https://lastminuteengineers.com/max7219-dot-matrix-arduino-tutorial/) — lastminuteengineers.com; Modulbeispiel; geprüft 2026-10-25.
- [MAX7219-Matrix mit Arduino und Visuino](https://www.digikey.com/en/maker/projects/control-led-matrix-max7219-with-arduino/11a2f1722b0045a6bc0d96d34c480d30) — digikey.com; Modulbeispiel; geprüft 2026-10-25.
- [MAX7219/MAX7221: SPI-Anschluss und Beispielcode](https://gist.github.com/nrdobie/8193350) — github.com; Code mit Anschlusszuordnung; geprüft 2026-10-25.

MAX7219-Modulbeispiele bei MAX7221 als Übertragungsgrundlage nutzen; Unterschiede der seriellen Schnittstelle beachten. Beim nackten IC ISET-Widerstand, Abblockung und gemeinsame Kathode gemäß Herstellerbeschaltung vorsehen.

## MC1488

**4/5 Beispiel-Websites**, 4 Quellen-Websites insgesamt. Weitere passende Beispiele gesucht.

- [RS-232-Schnittstelle (TI) (PDF S. 7)](../Datenblaetter/Diverse/MC1488_TI_Referenz.pdf#page=7) · [Online-Original](https://www.ti.com/lit/ds/symlink/mc1488.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [MC1488/MC1489 in der SR620-Schnittstelle (Schaltplan 2/16)](https://www.thinksrs.com/downloads/pdfs/manuals/SR620m.pdf) — thinksrs.com; Geräteschaltplan; geprüft 2026-10-25.
- [Sichtbarer optischer RS-232-Link mit MC1488/MC1489 (9. Januar 2003)](https://www.edn.com/wp-content/uploads/EDN_Design_Ideas_2003_.pdf) — edn.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [MC1488/MC1489: RS-232-Verbindungsbeschaltung](https://www.onsemi.com/download/data-sheet/pdf/mc1488-d.pdf) — onsemi.com; Hersteller-Grundschaltung; geprüft 2026-10-25.

Gemeinsames Systembeispiel für Leitungstreiber/-empfänger; Versorgung und Signalrichtung des jeweiligen Bausteins beachten. MC1488 benötigt positive und negative Versorgung; MC1489 empfängt RS-232 an +5 V. RS-232-Signale nicht direkt an einen Mikrocontroller-Eingang legen. Gerätepläne sind Anwendungsbeispiele mit zusätzlichen Schaltungsblöcken.

**Recherchebedarf:** Mehrere Websites mit Hersteller- und Gerätebeschaltungen belegt; die genaue Anzahl steht oben. Weitere unabhängige Beispiele fehlen; Datenblattspiegel werden nicht zusätzlich gezählt.

## MC1489

**3/5 Beispiel-Websites**, 3 Quellen-Websites insgesamt. Weitere passende Beispiele gesucht.

- [RS-232-Empfänger (onsemi)](https://www.onsemi.com/pdf/datasheet/mc1489-d.pdf#page=7) — onsemi.com; Herstellerbeispiel; geprüft 2026-10-21.
- [MC1488/MC1489 in der SR620-Schnittstelle (Schaltplan 2/16)](https://www.thinksrs.com/downloads/pdfs/manuals/SR620m.pdf) — thinksrs.com; Geräteschaltplan; geprüft 2026-10-25.
- [Sichtbarer optischer RS-232-Link mit MC1488/MC1489 (9. Januar 2003)](https://www.edn.com/wp-content/uploads/EDN_Design_Ideas_2003_.pdf) — edn.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [MC1488/MC1489: RS-232-Verbindungsbeschaltung](https://www.onsemi.com/download/data-sheet/pdf/mc1488-d.pdf) — onsemi.com; Hersteller-Grundschaltung; geprüft 2026-10-25.

Gemeinsames Systembeispiel für Leitungstreiber/-empfänger; Versorgung und Signalrichtung des jeweiligen Bausteins beachten. MC1488 benötigt positive und negative Versorgung; MC1489 empfängt RS-232 an +5 V. RS-232-Signale nicht direkt an einen Mikrocontroller-Eingang legen. Gerätepläne sind Anwendungsbeispiele mit zusätzlichen Schaltungsblöcken.

**Recherchebedarf:** Mehrere Websites mit Hersteller- und Gerätebeschaltungen belegt; die genaue Anzahl steht oben. Weitere unabhängige Beispiele fehlen; Datenblattspiegel werden nicht zusätzlich gezählt.

## PCF8574N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [I²C-Taster/LEDs (Adafruit)](https://learn.adafruit.com/adafruit-pcf8574?view=all) — adafruit.com; Projekt; geprüft 2026-10-21.
- [PCF8574: LEDs und Eingänge an Arduino/ESP32](https://www.digikey.com/en/maker/projects/how-to-use-pcf8574-gpio-extender-with-arduino-or-esp32/03a5059f8e014a089f0247e8645edc30) — digikey.com; Modulbeispiel; geprüft 2026-10-25.
- [PCF8574 als MIDI-Tastencontroller](https://diyelectromusic.com/2023/06/04/arduino-pcf8574-midi-controller/) — diyelectromusic.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [PCF8574: Anschluss, Interrupt und Bibliotheksbeispiele](https://github.com/xreef/PCF8574_library/blob/master/README.md) — github.com; Code mit Anschlusszuordnung; geprüft 2026-10-25.
- [Gadget Reboot: PCF8574-Ein-/Ausgänge und Interrupts](https://www.youtube.com/watch?v=mXMkgQf3fqU) — youtube.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.

Quasi-bidirektionale Ports: vor dem Einlesen eine 1 schreiben. Adresse und I2C-Pull-ups prüfen; 5-V-Pull-ups nicht direkt an nicht tolerante 3,3-V-Eingänge anschließen.

## PS2501-4

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Optokoppler-Ansteuerung (Renesas)](https://www.renesas.com/en/products/interface/optoelectronics/how-photocouplers-optocouplers-are-used) — renesas.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [Fototransistorkoppler: Pegelwandler und Widerstände](https://toshiba.semicon-storage.com/eu/semiconductor/knowledge/e-learning/discrete/chap5/chap5-13.html) — toshiba.semicon-storage.com; Grundschaltung; geprüft 2026-10-25.
- [PC817: isolierter Logikeingang und Lastansteuerung](https://www.learnabout-electronics.org/Semiconductors/opto_52.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Optische Eingangskopplung und Pegelanpassung](https://www.electronics-tutorials.ws/io/input-interfacing-circuits.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [PC817-Modul als Arduino-Eingang](https://mschoeffler.com/2021/04/30/arduino-tutorial-hy-m154-817-pc817-optocoupler-module/) — mschoeffler.com; Modulbeispiel; geprüft 2026-10-25.
  Hinweis: Fertiges Modul mit zusätzlichen Bauteilen; keine direkte Pinbeschaltung des einzelnen Kopplers.

Auf vier Kanäle und Pinfolge des PS2501-4 übertragen; LED-Vorwiderstand und CTR auslegen. LED-Vorwiderstand, minimalen CTR, Pull-up und Schaltgeschwindigkeit auslegen; PS2501-4 hat vier Kanäle und andere Gehäuseanschlüsse als PC817.

## UA78S40PC

**2/5 Beispiel-Websites**, 3 Quellen-Websites insgesamt. Weitere passende Beispiele gesucht.

- [Abwärtswandler (onsemi) (PDF S. 6)](../Datenblaetter/Diverse/UA78S40_onsemi_Referenz.pdf#page=6) · [Online-Original](https://datasheet4u.com/pdf/502453/UA78S40.pdf) — datasheet4u.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Aufwärts-/Invertierwandler (onsemi) (PDF S. 5)](../Datenblaetter/Diverse/UA78S40_onsemi_Referenz.pdf#page=5) · [Online-Original](https://datasheet4u.com/pdf/502453/UA78S40.pdf) — datasheet4u.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [78S40-Boost-Konstantstromtreiber für eine Leistungs-LED](https://www.sciencetronics.com/greenphotons/?lang=en&p=717) — sciencetronics.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [Programmierbarer DC/DC-Wandler: Regelungsprinzip](https://www.nutsvolts.com/magazine/article/designing-a-programmable-dc-to-dc-converter) — nutsvolts.com; Prinzipreferenz; geprüft 2026-10-25.
  Hinweis: Andere Reglerbeschaltung möglich; keine bestätigte Pinvorlage für UA78S40.

**Recherchebedarf:** Bisher sind weniger als fünf unterschiedliche Websites mit passenden Beispielen belegt. Die vorhandenen Grundschaltungen und Referenzen sind oben gekennzeichnet; es wurden keine zusätzlichen Beschaltungen erfunden.

## ULN2004A

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Relais-/Motoransteuerung (TI) (PDF S. 16)](../Datenblaetter/Diverse/ULN2004A_TI_Referenz.pdf#page=16) · [Online-Original](https://www.ti.com/lit/ds/symlink/uln2004a.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [ULN2803 steuert mehrere Relais](https://www.disca.upv.es/aperles/web51/modulos/modulo10/m_reles.html) — disca.upv.es; Grundschaltung; geprüft 2026-10-25.
- [ULN2803 als unipolarer Schrittmotortreiber](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-10-stepper-motors/hardware-uln2803) — adafruit.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [ULN2803-Last- und Relaistreiber im SMS-Controller](https://www.siliconchip.com.au/Issue/2004/October/SMS%2BController%2C%2BPt.1) — siliconchip.com.au; Anwendungsreferenz; geprüft 2026-10-25.
- [ULN2803A: Relaisspule und COM-Anschluss](https://www.flux.ai/lcsc/uln2803a~i9jk/files/uln2803a-application-and-usage-guide~os) — flux.ai; Grundschaltung; geprüft 2026-10-25.
- [Open-Collector-Lastschalter und Pegelanpassung](https://www.electronics-tutorials.ws/transistor/open-collector-outputs.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Familien-Grundschaltung: Eingangsnetzwerk für ULN2004 gegenüber ULN2003 abgleichen; bei ULN2803 außerdem acht Kanäle und andere Pinfolge beachten. ULN2803-Beispiele sind für ULN2004 nur Grundschaltungen: ULN2004 hat sieben Kanäle und eine andere Eingangsbeschaltung; seine Ansteuerung bei 5 V anhand des Datenblatts nachweisen. COM führt zu den Klemmdioden und ist kein VCC-Pin. Die Open-Collector-Quelle zeigt die Lastseite eines Kanals; Eingangswiderstände und Klemmdioden des Arrays gemäß Herstellerunterlage verwenden.

## ULN2004AG

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Relais-/Motoransteuerung (TI) (PDF S. 16)](../Datenblaetter/Diverse/ULN2004A_TI_Referenz.pdf#page=16) · [Online-Original](https://www.ti.com/lit/ds/symlink/uln2004a.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [ULN2803 steuert mehrere Relais](https://www.disca.upv.es/aperles/web51/modulos/modulo10/m_reles.html) — disca.upv.es; Grundschaltung; geprüft 2026-10-25.
- [ULN2803 als unipolarer Schrittmotortreiber](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-10-stepper-motors/hardware-uln2803) — adafruit.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [ULN2803-Last- und Relaistreiber im SMS-Controller](https://www.siliconchip.com.au/Issue/2004/October/SMS%2BController%2C%2BPt.1) — siliconchip.com.au; Anwendungsreferenz; geprüft 2026-10-25.
- [ULN2803A: Relaisspule und COM-Anschluss](https://www.flux.ai/lcsc/uln2803a~i9jk/files/uln2803a-application-and-usage-guide~os) — flux.ai; Grundschaltung; geprüft 2026-10-25.
- [Open-Collector-Lastschalter und Pegelanpassung](https://www.electronics-tutorials.ws/transistor/open-collector-outputs.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Familien-Grundschaltung: Eingangsnetzwerk für ULN2004 gegenüber ULN2003 abgleichen; bei ULN2803 außerdem acht Kanäle und andere Pinfolge beachten. ULN2803-Beispiele sind für ULN2004 nur Grundschaltungen: ULN2004 hat sieben Kanäle und eine andere Eingangsbeschaltung; seine Ansteuerung bei 5 V anhand des Datenblatts nachweisen. COM führt zu den Klemmdioden und ist kein VCC-Pin. Die Open-Collector-Quelle zeigt die Lastseite eines Kanals; Eingangswiderstände und Klemmdioden des Arrays gemäß Herstellerunterlage verwenden.

## ULN2803A

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Relais-/Motoransteuerung (TI) (PDF S. 16)](../Datenblaetter/Diverse/ULN2004A_TI_Referenz.pdf#page=16) · [Online-Original](https://www.ti.com/lit/ds/symlink/uln2004a.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [ULN2803 steuert mehrere Relais](https://www.disca.upv.es/aperles/web51/modulos/modulo10/m_reles.html) — disca.upv.es; Grundschaltung; geprüft 2026-10-25.
- [ULN2803 als unipolarer Schrittmotortreiber](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-10-stepper-motors/hardware-uln2803) — adafruit.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [ULN2803-Last- und Relaistreiber im SMS-Controller](https://www.siliconchip.com.au/Issue/2004/October/SMS%2BController%2C%2BPt.1) — siliconchip.com.au; Anwendungsreferenz; geprüft 2026-10-25.
- [ULN2803A: Relaisspule und COM-Anschluss](https://www.flux.ai/lcsc/uln2803a~i9jk/files/uln2803a-application-and-usage-guide~os) — flux.ai; Grundschaltung; geprüft 2026-10-25.
- [Open-Collector-Lastschalter und Pegelanpassung](https://www.electronics-tutorials.ws/transistor/open-collector-outputs.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Familien-Grundschaltung: Eingangsnetzwerk für ULN2004 gegenüber ULN2003 abgleichen; bei ULN2803 außerdem acht Kanäle und andere Pinfolge beachten. ULN2803-Beispiele sind für ULN2004 nur Grundschaltungen: ULN2004 hat sieben Kanäle und eine andere Eingangsbeschaltung; seine Ansteuerung bei 5 V anhand des Datenblatts nachweisen. COM führt zu den Klemmdioden und ist kein VCC-Pin. Die Open-Collector-Quelle zeigt die Lastseite eines Kanals; Eingangswiderstände und Klemmdioden des Arrays gemäß Herstellerunterlage verwenden.

## LM358P

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Anwendungsschaltung (TI) (PDF S. 27)](../Datenblaetter/Diverse/LM358_TI_Referenz.pdf#page=27) · [Online-Original](https://www.ti.com/lit/ds/symlink/lm358.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Nichtinvertierender Verstärker (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-6/noninverting-amplifier/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Spannungsfolger (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-6/precision-voltage-follower/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Invertierender/nichtinvertierender Verstärker und Komparator](https://www.renesas.com/en/support/engineer-school/electronic-circuits-03-op-amps-comparator-circuit) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [OPV-Anwendungen und Schaltungsgrenzen](https://wiki.analog.com/university/courses/electronics/text/chapter-4) — analog.com; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbau: Spannungsfolger und nichtinvertierender Verstärker](https://physicslabs.colorado.edu/courses/phys-3330/lab-guides/lab4/) — physicslabs.colorado.edu; Grundschaltung; geprüft 2026-10-25.
- [OPV-Verstärker mit Gegenkopplung](https://learnabout-electronics.org/Amplifiers/amplifiers66.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundschaltungen: Versorgung, Eingangsspannungsbereich, Ausgangshub und Verstärkerpins an den konkreten OPV anpassen; insbesondere UA741 nicht wie einen Rail-to-Rail-OPV behandeln. OPV-Grundschaltung mit anderen Referenztypen: Versorgung, Eingangs-Gleichtaktbereich und Ausgangshub prüfen. UA741 ist kein für allgemeine 5-V-Einversorgung geeigneter Ersatz für LM358.

## UA741CN

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Nichtinvertierender Verstärker (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-6/noninverting-amplifier/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Spannungsfolger (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-6/precision-voltage-follower/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Invertierender/nichtinvertierender Verstärker und Komparator](https://www.renesas.com/en/support/engineer-school/electronic-circuits-03-op-amps-comparator-circuit) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [OPV-Anwendungen und Schaltungsgrenzen](https://wiki.analog.com/university/courses/electronics/text/chapter-4) — analog.com; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbau: Spannungsfolger und nichtinvertierender Verstärker](https://physicslabs.colorado.edu/courses/phys-3330/lab-guides/lab4/) — physicslabs.colorado.edu; Grundschaltung; geprüft 2026-10-25.
- [OPV-Verstärker mit Gegenkopplung](https://learnabout-electronics.org/Amplifiers/amplifiers66.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundschaltungen: Versorgung, Eingangsspannungsbereich, Ausgangshub und Verstärkerpins an den konkreten OPV anpassen; insbesondere UA741 nicht wie einen Rail-to-Rail-OPV behandeln. OPV-Grundschaltung mit anderen Referenztypen: Versorgung, Eingangs-Gleichtaktbereich und Ausgangshub prüfen. UA741 ist kein für allgemeine 5-V-Einversorgung geeigneter Ersatz für LM358.

## NE555 (E)

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Astabiler Oszillator (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-6/555-audio-oscillator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Monoflop (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-8/555-monostable-multivibrator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [PWM-Steuerung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-6/pwm-power-controller/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [555: Blinker, Zeitgeber und Lastansteuerung](https://www.build-electronic-circuits.com/555-timer/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [555: astabiler, monostabiler und bistabiler Betrieb](https://learn.adafruit.com/getting-to-know-the-555/applications) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [LED-Helligkeitsregelung mit 555-PWM](https://learn.sparkfun.com/tutorials/led-light-bar-hookup/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [555-Oszillator und Tastverhältnis](https://www.electronics-tutorials.ws/waveforms/555_oscillator.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bipolare 555-Timer-Grundschaltungen; Versorgung, Pinbelegung und Grenzwerte der vorhandenen Variante abgleichen.

## NE555 (TI)

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Astabiler Oszillator (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-6/555-audio-oscillator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Monoflop (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-8/555-monostable-multivibrator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [PWM-Steuerung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-6/pwm-power-controller/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [555: Blinker, Zeitgeber und Lastansteuerung](https://www.build-electronic-circuits.com/555-timer/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [555: astabiler, monostabiler und bistabiler Betrieb](https://learn.adafruit.com/getting-to-know-the-555/applications) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [LED-Helligkeitsregelung mit 555-PWM](https://learn.sparkfun.com/tutorials/led-light-bar-hookup/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [555-Oszillator und Tastverhältnis](https://www.electronics-tutorials.ws/waveforms/555_oscillator.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bipolare 555-Timer-Grundschaltungen; Versorgung, Pinbelegung und Grenzwerte der vorhandenen Variante abgleichen.

## MC1455

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Astabiler Oszillator (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-6/555-audio-oscillator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Monoflop (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-8/555-monostable-multivibrator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [PWM-Steuerung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-6/pwm-power-controller/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [555: Blinker, Zeitgeber und Lastansteuerung](https://www.build-electronic-circuits.com/555-timer/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [555: astabiler, monostabiler und bistabiler Betrieb](https://learn.adafruit.com/getting-to-know-the-555/applications) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [LED-Helligkeitsregelung mit 555-PWM](https://learn.sparkfun.com/tutorials/led-light-bar-hookup/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [555-Oszillator und Tastverhältnis](https://www.electronics-tutorials.ws/waveforms/555_oscillator.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bipolare 555-Timer-Grundschaltungen; Versorgung, Pinbelegung und Grenzwerte der vorhandenen Variante abgleichen.

## L298N

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Motor-/Schrittmotorschaltung (ST) (PDF S. 10)](../Datenblaetter/Diverse/L298N_ST.pdf#page=10) · [Online-Original](https://www.datasheets.com/stmicroelectronics/L298N/datasheet.pdf) — datasheets.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [L293D auf dem Steckbrett mit Schrittmotor](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-10-stepper-motors/hardware-l293d) — adafruit.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [Zwei Gleichstrommotoren mit L293D und Arduino](https://blog.codebender.cc/2015/08/09/tutorial-how-to-use-the-l293d-motor-driver-ic/) — blog.codebender.cc; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [L293D/L298N: Drehrichtung und PWM mit 8051](https://technobyte.org/8051-dc-motor-interfacing-l293d-l298n-pwm/) — technobyte.org; Grundschaltung; geprüft 2026-10-25.
- [Motorsteuerung mit L298N und Arduino](https://www.learnrobotics.org/blog/how-to-use-l298n-motor-driver/) — learnrobotics.org; Grundschaltung; geprüft 2026-10-25.
- [L298N-Modul: PWM und Drehrichtung mit ESP32](https://randomnerdtutorials.com/esp32-dc-motor-l298n-motor-driver-control-speed-direction/) — randomnerdtutorials.com; Modulbeispiel; geprüft 2026-10-25.

H-Brücken-Grundschaltungen mit unterschiedlichen Treibern: Versorgung, Enable, Pinfolge und Stromgrenzen separat prüfen. L293NE und L298N benötigen externe Freilaufdioden; L293D integriert diese. Ein L298N-Modul enthält zusätzliche Bauteile und ist nicht mit dem nackten IC gleichzusetzen.

## MAX7221CNG

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [8-stellige LED-Anzeige (Maxim) (PDF S. 1)](../Datenblaetter/Diverse/MAX7219_Maxim.pdf#page=1) · [Online-Original](https://datasheet4u.com/pdf/1474108/MAX7219.pdf) — datasheet4u.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [MAX7219/MAX7221: Anzeige- und Kaskadierbeschaltung](https://www.analog.com/media/en/technical-documentation/data-sheets/MAX7219-MAX7221.pdf) — analog.com; Herstellerbeispiel; geprüft 2026-10-25.
- [MAX7219-Matrix: Laufschrift und Animationen](https://www.makerguides.com/max7219-led-dot-matrix-display-arduino-tutorial/) — makerguides.com; Modulbeispiel; geprüft 2026-10-25.
- [MAX7219-Matrix an Arduino und mehrere Module](https://lastminuteengineers.com/max7219-dot-matrix-arduino-tutorial/) — lastminuteengineers.com; Modulbeispiel; geprüft 2026-10-25.
- [MAX7219-Matrix mit Arduino und Visuino](https://www.digikey.com/en/maker/projects/control-led-matrix-max7219-with-arduino/11a2f1722b0045a6bc0d96d34c480d30) — digikey.com; Modulbeispiel; geprüft 2026-10-25.
- [MAX7219/MAX7221: SPI-Anschluss und Beispielcode](https://gist.github.com/nrdobie/8193350) — github.com; Code mit Anschlusszuordnung; geprüft 2026-10-25.

MAX7219-Modulbeispiele bei MAX7221 als Übertragungsgrundlage nutzen; Unterschiede der seriellen Schnittstelle beachten. Beim nackten IC ISET-Widerstand, Abblockung und gemeinsame Kathode gemäß Herstellerbeschaltung vorsehen.

## DS18B20

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [1-Wire mit externer Versorgung (Maxim-Typreferenz) (PDF S. 6)](../Datenblaetter/Diverse/DS18B20_Maxim_Referenz.pdf#page=6) · [Online-Original](https://cdn-shop.adafruit.com/datasheets/DS18B20.pdf) — adafruit.com; Grundschaltung (Typreferenz Maxim); geprüft 2026-10-21.
- [DS18B20 mit CircuitPython und OneWire](https://learn.adafruit.com/using-ds18b20-temperature-sensor-with-circuitpython?view=all) — adafruit.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [Ein oder mehrere DS18B20 an Arduino](https://randomnerdtutorials.com/guide-for-ds18b20-temperature-sensor-with-arduino/) — randomnerdtutorials.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [DS18B20: Verdrahtung und Messwertausgabe](https://www.makerguides.com/ds18b20-arduino-tutorial/) — makerguides.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [DS18B20 am Raspberry Pi](https://pimylifeup.com/raspberry-pi-temperature-sensor/) — pimylifeup.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [OneWire-Temperaturmessung mit DS18B20](https://arduino-tutorials.net/tutorial/reading-1-wire-ds18b20-temperature-sensor-with-arduino) — arduino-tutorials.net; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.

Fremdherstellerreferenz; Zuordnung des Aufdrucks 7Q.TeK ungeklärt.

## 36.11.9.005.0000

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Relais mit Treiberarray (Grundschaltung) (PDF S. 16)](../Datenblaetter/Diverse/ULN2004A_TI_Referenz.pdf#page=16) · [Online-Original](https://www.ti.com/lit/ds/symlink/uln2004a.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.

Treiber und Freilaufdiode für die 5-V-DC-Spule dimensionieren; Treibereingangspegel beachten. Relaistreiber-Grundschaltungen: Spulennennspannung, Spulenstrom und Anschlussbild des vorhandenen Relais verwenden; Freilaufdiode nur bei Gleichstromspulen. Referenzrelais der Quelle ist nicht der vorhandene Typ.

## MCP3008-I/P

**4/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Weitere passende Beispiele gesucht.

- [Eingangsfilter (MCP3004-Familienreferenz) (PDF S. 23)](../Datenblaetter/Diverse/MCP3008_Microchip.pdf#page=23) · [Online-Original](https://ww1.microchip.com/downloads/aemDocuments/documents/MSLD/ProductDocuments/DataSheets/MCP3004-MCP3008-Data-Sheet-DS20001295.pdf) — microchip.com; Familienreferenz: Eingangsfilter am MCP3004; geprüft 2026-10-21.
- [MCP3008 an Raspberry Pi mit SPI](https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008) — adafruit.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [Analogsensoren mit MCP3008 einlesen](https://pimylifeup.com/raspberry-pi-adc/) — pimylifeup.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [MCP3008-Potentiometer als Radiobedienung](https://www.raspberrypi.com/news/build-an-internet-radio/) — raspberrypi.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [MCP3008: Potentiometer und LED-Balken mit GPIO Zero](https://gpiozero.readthedocs.io/en/stable/recipes.html#potentiometer) — gpiozero.readthedocs.io; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.

Herstellerbeispiel am MCP3004; Eingangsfilter auf einen Kanal des MCP3008 übertragbar, Pinzahlen unterscheiden sich. Bei Raspberry Pi 3,3-V-Logik und passende VREF verwenden; analoge Eingangssignale nicht oberhalb VREF einspeisen.

**Recherchebedarf:** Bisher sind weniger als fünf unterschiedliche Websites mit passenden Beispielen belegt. Die vorhandenen Grundschaltungen und Referenzen sind oben gekennzeichnet; es wurden keine zusätzlichen Beschaltungen erfunden.
