# Schaltungsbeispiele: CD4xxx

[Übersicht](README.md) · [Gesamtsammlung](Beispielschaltungen.md) · [Recherchebedarf](Recherchebedarf.md) · [Bestand](../Bauteile.md)

59 Bauteile, 365 Linkzuordnungen. Erweiterungsstand: **25.10.2026**; Prüfdatum jeweils am Link.

Ziel sind etwa **fünf unterschiedliche Websites pro Bauteil**. Gezählt werden Websites mit Schaltungsbeispielen, übertragbaren Grundschaltungen, Modulbeispielen oder Code mit Anschlusszuordnung. Reine Funktions-/Prinzipreferenzen und Entwurfshilfen zählen zusätzlich als Quellen, aber nicht zum Beispielziel. Subdomains und bekannte Länderspiegel zählen zusammen. Mehrere Artikel derselben Website erhöhen die Zahl nicht.

**Grundschaltung** bedeutet: Das Schaltungsprinzip ist übertragbar, der Artikel verwendet gegebenenfalls ein anderes Bauteil. Sie ist keine Bestätigung der Pinbelegung oder Dimensionierung des vorhandenen Typs. **Modulbeispiele** enthalten zusätzliche Komponenten; **Funktionsreferenzen** sind keine vollständigen Nachbauschaltungen. Hinweise stehen direkt beim Bauteil und Link.

Versorgung, Pinfolge, Polarität, Logikfamilie, Freigaben, Taktflanken und Grenzwerte anhand des konkreten Datenblatts prüfen. 74LS benötigt +5 V. Pro IC üblicherweise 100 nF abblocken, Taster für Zähler entprellen. Transistor- und Diodenwerte an Last und Verlustleistung anpassen. Bei Relais gilt die tatsächliche Spulenspannung. TRIAC-Artikel können Netzspannungsschaltungen enthalten.

Pflege: [Beispielschaltungen.json](Beispielschaltungen.json). `python3 scripts/update_examples.py` erzeugt ausschließlich diese Sammlungen. Bestand und Datenbank bleiben unverändert. Bei lokalen PDFs führt „Online-Original“ zur dokumentierten Downloadquelle; neuere Revisionen können andere Seitenzahlen haben.

## CD4001

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [RS-Speicher (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/nor-gate-s-r-latch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## CD4002 (Grundtyp; Aufdruck PC74HCT4002P)

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [RS-Speicher (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/nor-gate-s-r-latch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## CD4009

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## CD4011

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## CD4012

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## CD4013

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Toggle-/Zähler-Anwendung (TI) (PDF S. 11)](../Datenblaetter/CD4xxx/CD4013_TI.pdf#page=11) · [Online-Original](https://www.ti.com/lit/ds/symlink/cd4013b.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [D-Flipflop (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-10/edge-triggered-latches-flip-flops/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [D-Flipflop als Speicher und Teiler](https://www.electronics-tutorials.ws/sequential/seq_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## CD4015

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [LED-Ausgänge erweitern (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-12/serial-in-parallel-out-shift-register/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Serielle und parallele Schieberegister](https://www.electronics-tutorials.ws/sequential/seq_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## CD4016

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Analogsignal schalten (TI-Referenz) (PDF S. 16)](../Datenblaetter/CD4xxx/CD4066_TI.pdf#page=16) · [Online-Original](https://www.ti.com/lit/ds/symlink/cd4066b.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Analoge Schalter und Multiplexer als Grundschaltung](https://www.electronics-tutorials.ws/combination/comb_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [CD4066 als schaltbarer Effekt-Bypass](https://subdecay.com/wp-content/uploads/2024/09/Web-user-guide-EZ-MIDI-1-01.pdf) — subdecay.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [CD4066 im Analog-Synthesizer](https://www.ece.ucf.edu/seniordesign/fa2012sp2013/g06/documents/Term2Paper.pdf) — ece.ucf.edu; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [CD4066 als Analogschalter im Funkgerät](https://collinsradio.org/archives/manuals/KWM380_Self_Study_.pdf) — collinsradio.org; Anwendungsreferenz; geprüft 2026-10-25.
- [CD4016 als elektrisch steuerbarer Analogschalter](https://www.build-electronic-circuits.com/4000-series-integrated-circuits/ic-4016/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.

CD4066B-Referenzschaltung; für CD4016B insbesondere R_on, Leckstrom und zulässige Signalpegel abgleichen. CD4066-Beispiele sind für CD4016 nur Grundschaltungen: Einschaltwiderstand, Signalbereich und Pinbelegung abgleichen.

## CD4017

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Lauflicht/Ringzähler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-12/ring-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

CD4022 hat acht statt zehn dekodierte Ausgänge; Verdrahtung und Reset entsprechend anpassen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## CD4019

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Datenauswahl (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-9/multiplexers/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Datenauswahl und Multiplexer](https://www.learnabout-electronics.org/Digital/dig42.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Decoder, Multiplexer und Addierer](https://learn.adafruit.com/combinational-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Multiplexer und Decoder aus Gattern](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Signalauswahl mit Multiplexern](https://www.electronics-tutorials.ws/combination/comb_2.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen.

## CD4021

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Taster seriell einlesen (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-12/parallel-in-serial-out-shift-register/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Serielle und parallele Schieberegister](https://www.electronics-tutorials.ws/sequential/seq_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [CD4094/CD4021: LEDs ausgeben und Taster einlesen](https://friendlywire.com/tutorials/cd4094-cd4021/) — friendlywire.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## CD4022

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Lauflicht/Ringzähler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-12/ring-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

CD4022 hat acht statt zehn dekodierte Ausgänge; Verdrahtung und Reset entsprechend anpassen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## CD4023

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## CD4024

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zähler kaskadieren (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/asynchronous-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Modulo-/Frequenzteiler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/counter-modulus/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## CD4025

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [RS-Speicher (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/nor-gate-s-r-latch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## CD4026

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Anzeige-Ansteuerung (Hersteller) (PDF S. 5)](../Datenblaetter/CD4xxx/CD4026_TI.pdf#page=5) · [Online-Original](https://www.ti.com/lit/ds/symlink/cd4026b.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [BCD-Eingabe mit CD4511 und 7-Segment-Anzeige](https://circuitdigest.com/electronic-circuits/7-segment-display-driver-using-ic-cd4511) — circuitdigest.com; Grundschaltung; geprüft 2026-10-25.
- [CD4511-Anzeige auf dem Steckbrett](https://www.circuits-diy.com/how-to-drive-a-7-segment-display-using-bcd-driver-ic-cd4511) — circuits-diy.com; Grundschaltung; geprüft 2026-10-25.
- [Zweistelliger Zähler mit CD4026](https://www.eleccircuit.com/simple-two-digits-counter-using-cd4026/) — eleccircuit.com; Grundschaltung; geprüft 2026-10-25.
- [BCD-Decoder und 7-Segment-Zähler](https://www.electronics-tutorials.ws/counter/7-segment-display.html) — electronics-tutorials.ws; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [7-Segment-Anzeige als Grundschaltung](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/7-segment-display/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.

Anzeigeart und Ausgangspolarität beachten; CD4513/4553 verwenden dokumentierte Motorola/onsemi-Referenzen. Anzeige-Grundschaltungen mit anderen ICs: BCD-Decoder und Zähler nicht verwechseln. Anzeigeart (gemeinsame Anode/Kathode bzw. LCD), aktive Ausgangspegel, Segmentwiderstände und Multiplexsteuerung passend zum Typ wählen. Insbesondere CD4543 kann LCD-Phasenansteuerung verwenden; eine LED-Schaltung ist dafür keine direkte Vorlage.

## CD4027

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [JK-Flipflop/Teiler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-10/j-k-flip-flop/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Binärzähler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/asynchronous-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [JK-Flipflop und Teilerprinzip](https://www.electronics-tutorials.ws/sequential/seq_2.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## CD4028

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Adress-/Leitungsdecoder (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-9/decoder/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Signalverteilung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-9/demultiplexers/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Encoder, Decoder und Adressauswahl](https://www.learnabout-electronics.org/Digital/dig44.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Decoder, Multiplexer und Addierer](https://learn.adafruit.com/combinational-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Multiplexer und Decoder aus Gattern](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Binärdecoder und Leitungsauswahl](https://www.electronics-tutorials.ws/combination/comb_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen.

## CD4029

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zähler kaskadieren (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/synchronous-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Modulo-/Frequenzteiler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/counter-modulus/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## CD4030

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Vergleich/Parität (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-7/the-exclusive-or-function-xor/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## CD4033

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Anzeige-Ansteuerung (Hersteller) (PDF S. 5)](../Datenblaetter/CD4xxx/CD4033_TI.pdf#page=5) · [Online-Original](https://www.ti.com/lit/ds/symlink/cd4033b.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [BCD-Eingabe mit CD4511 und 7-Segment-Anzeige](https://circuitdigest.com/electronic-circuits/7-segment-display-driver-using-ic-cd4511) — circuitdigest.com; Grundschaltung; geprüft 2026-10-25.
- [CD4511-Anzeige auf dem Steckbrett](https://www.circuits-diy.com/how-to-drive-a-7-segment-display-using-bcd-driver-ic-cd4511) — circuits-diy.com; Grundschaltung; geprüft 2026-10-25.
- [Zweistelliger Zähler mit CD4026](https://www.eleccircuit.com/simple-two-digits-counter-using-cd4026/) — eleccircuit.com; Grundschaltung; geprüft 2026-10-25.
- [BCD-Decoder und 7-Segment-Zähler](https://www.electronics-tutorials.ws/counter/7-segment-display.html) — electronics-tutorials.ws; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [7-Segment-Anzeige als Grundschaltung](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/7-segment-display/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.

Anzeigeart und Ausgangspolarität beachten; CD4513/4553 verwenden dokumentierte Motorola/onsemi-Referenzen. Anzeige-Grundschaltungen mit anderen ICs: BCD-Decoder und Zähler nicht verwechseln. Anzeigeart (gemeinsame Anode/Kathode bzw. LCD), aktive Ausgangspegel, Segmentwiderstände und Multiplexsteuerung passend zum Typ wählen. Insbesondere CD4543 kann LCD-Phasenansteuerung verwenden; eine LED-Schaltung ist dafür keine direkte Vorlage.

## CD4042

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Daten zwischenspeichern (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-10/d-latch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [D-Flipflop als Speicher und Teiler](https://www.electronics-tutorials.ws/sequential/seq_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## CD4043

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Setzen/Rücksetzen (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/nor-gate-s-r-latch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [D-Flipflop als Speicher und Teiler](https://www.electronics-tutorials.ws/sequential/seq_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei NAND-RS-Latches aktive Low-Eingänge und Ausgangsfreigaben abgleichen; NOR-Beispiel zeigt das Speicherprinzip. RS-Speicherprinzip: 74LS279 mit aktiven Low-Eingängen und CD4043 mit anderen Freigaben nicht wie ein D-Flipflop beschalten. D-Flipflop-Link erläutert nur den Unterschied der Speicherarten.

## CD4046

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PLL-/VCO-Anwendungen (TI)](https://www.ti.com/lit/an/scha002a/scha002a.pdf) — ti.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [CD4046: VCO und geschlossener PLL-Laborversuch](https://my.ece.utah.edu/~ece3510/Lab_PLL_Basic_S19.pdf) — my.ece.utah.edu; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
  Hinweis: Laborbeispiel nutzt 12 V; bei 5 V VCO-Werte und Signalpegel neu auslegen.
- [CD4046 auf ein 2-kHz-Signal einrasten lassen](https://www.ibiblio.org/kuphaldt/socratic/model/mod_pll.pdf) — ibiblio.org; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [CD4046 als Rampengenerator](https://leap.tardate.com/electronics101/cd4046/rampgenerator/) — leap.tardate.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [CD4046: eigenständiger VCO und Phasenvergleich](https://davidmorrin.com/notes/components/integrated-circuits/CD4046/) — davidmorrin.com; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen.

## CD4047

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Astabil-/Monoflop-Beschaltung (TI) (PDF S. 1)](../Datenblaetter/CD4xxx/CD4047_TI.pdf#page=1) · [Online-Original](https://www.ti.com/lit/ds/symlink/cd4047b.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [CD4047 als Taktgenerator und Monoflop](https://tronixstuff.com/2011/02/11/review-cd4047-astablemonostable-multivibrator/) — tronixstuff.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
  Hinweis: Autorenkorrektur beachten: Pin 14 im Monoflop-Schaltbild zusätzlich an +5 V.
- [CD4047-Monoflop und Impulslänge](https://www.bristolwatch.com/geiger/monostable.htm) — bristolwatch.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [Monoflop und Impulsverlängerung als Prinzip](https://www.electronics-tutorials.ws/waveforms/monostable.html) — electronics-tutorials.ws; Prinzipreferenz; geprüft 2026-10-25.
- [CD4047 in astabilen und monostabilen Betriebsarten](https://circuitdigest.com/tutorial/cd4047-multifunctional-multivibrator-ic-circuit-simulation-working-modes) — circuitdigest.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [CD4047-Rechteckgenerator mit Ausgängen für einen Inverter](https://www.circuitsdiy.com/cd4047-based-squarewave-inverter-oscillator/) — circuitsdiy.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. CD4047-Beispiele sind bei anderen Monoflops nur Prinzipreferenzen; Triggerpolarität, Retriggerbarkeit, RC-Pins und Zeitformeln des jeweiligen ICs übernehmen.

## CD4049

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Pegelwandler (TI) (PDF S. 17)](../Datenblaetter/CD4xxx/CD4049_TI.pdf#page=17) · [Online-Original](https://www.ti.com/lit/ds/symlink/cd4049ub.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [CD4049 als invertierender Pegelwandler](https://www.build-electronic-circuits.com/4000-series-integrated-circuits/ic-4049/) — build-electronic-circuits.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Pegelwandlung mit CD4049 ist invertierend. Gatterbeispiele sind Grundschaltungen; ungewöhnliche Versorgungspins 1/8 beachten.

## CD4050

**2/5 Beispiel-Websites**, 2 Quellen-Websites insgesamt. Weitere passende Beispiele gesucht.

- [Pegelwandler (TI) (PDF S. 17)](../Datenblaetter/CD4xxx/CD4050_TI.pdf#page=17) · [Online-Original](https://www.ti.com/lit/ds/symlink/cd4050b.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [CD4050 als nichtinvertierender Pegelwandler](https://www.build-electronic-circuits.com/4000-series-integrated-circuits/ic-4050/) — build-electronic-circuits.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.

Nichtinvertierender Pegelwandler; Versorgung liegt an Pin 1/8. Zulässige Eingangsspannung, Ausgangsstrom und Pinbelegung der Variante prüfen. Keine Tri-State-Freigabe vorhanden.

**Recherchebedarf:** Zwei typbezogene Pegelwandlerquellen vorhanden. Weitere passende Beschaltungen wurden noch nicht ausreichend belegt.

## CD4051

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Analoger Kanalumschalter (TI) (PDF S. 18)](../Datenblaetter/CD4xxx/CD4051_TI.pdf#page=18) · [Online-Original](https://www.ti.com/lit/ds/symlink/cd4051b.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [CD405x am ADALM1000 als Analogkanalumschalter](https://wiki.analog.com/university/tools/m1k/alice-cd4051-analog-mux-ug) — analog.com; Grundschaltung; geprüft 2026-10-25.
- [74HC4051-Modul für LEDs und Potentiometer](https://learn.sparkfun.com/tutorials/multiplexer-breakout-hookup-guide/introduction) — sparkfun.com; Modulbeispiel; geprüft 2026-10-25.
- [CD4051: mehrere Potentiometer am ADC](https://daisy.audio/blogs/seeds-n-circuits/what-the-mux-a-guided-tutorial-for-using-multiplexers-with-daisy) — daisy.audio; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [Analoge Schalter und Multiplexer als Grundschaltung](https://www.electronics-tutorials.ws/combination/comb_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. 4051-Beispiele zeigen das Umschaltprinzip. CD4052 hat zwei Vierfachkanäle, CD4053 drei Zweifachkanäle; Adressen, Kanalzahl und Pinfolge unterscheiden sich. Analogsignale innerhalb VEE bis VDD halten; Einschaltwiderstand beachten.

## CD4052

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Analoger Kanalumschalter (TI) (PDF S. 18)](../Datenblaetter/CD4xxx/CD4052_TI.pdf#page=18) · [Online-Original](https://www.ti.com/lit/ds/symlink/cd4052b.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [CD405x am ADALM1000 als Analogkanalumschalter](https://wiki.analog.com/university/tools/m1k/alice-cd4051-analog-mux-ug) — analog.com; Grundschaltung; geprüft 2026-10-25.
- [74HC4051-Modul für LEDs und Potentiometer](https://learn.sparkfun.com/tutorials/multiplexer-breakout-hookup-guide/introduction) — sparkfun.com; Modulbeispiel; geprüft 2026-10-25.
- [CD4051: mehrere Potentiometer am ADC](https://daisy.audio/blogs/seeds-n-circuits/what-the-mux-a-guided-tutorial-for-using-multiplexers-with-daisy) — daisy.audio; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [Analoge Schalter und Multiplexer als Grundschaltung](https://www.electronics-tutorials.ws/combination/comb_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. 4051-Beispiele zeigen das Umschaltprinzip. CD4052 hat zwei Vierfachkanäle, CD4053 drei Zweifachkanäle; Adressen, Kanalzahl und Pinfolge unterscheiden sich. Analogsignale innerhalb VEE bis VDD halten; Einschaltwiderstand beachten.

## CD4053

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Analoger Kanalumschalter (TI) (PDF S. 18)](../Datenblaetter/CD4xxx/CD4053_TI.pdf#page=18) · [Online-Original](https://www.ti.com/lit/ds/symlink/cd4053b.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [CD405x am ADALM1000 als Analogkanalumschalter](https://wiki.analog.com/university/tools/m1k/alice-cd4051-analog-mux-ug) — analog.com; Grundschaltung; geprüft 2026-10-25.
- [74HC4051-Modul für LEDs und Potentiometer](https://learn.sparkfun.com/tutorials/multiplexer-breakout-hookup-guide/introduction) — sparkfun.com; Modulbeispiel; geprüft 2026-10-25.
- [CD4051: mehrere Potentiometer am ADC](https://daisy.audio/blogs/seeds-n-circuits/what-the-mux-a-guided-tutorial-for-using-multiplexers-with-daisy) — daisy.audio; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [Analoge Schalter und Multiplexer als Grundschaltung](https://www.electronics-tutorials.ws/combination/comb_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. 4051-Beispiele zeigen das Umschaltprinzip. CD4052 hat zwei Vierfachkanäle, CD4053 drei Zweifachkanäle; Adressen, Kanalzahl und Pinfolge unterscheiden sich. Analogsignale innerhalb VEE bis VDD halten; Einschaltwiderstand beachten.

## CD4060

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [RC-/Quarzoszillator mit Teiler (TI) (PDF S. 3)](../Datenblaetter/CD4xxx/CD4060_TI.pdf#page=3) · [Online-Original](https://www.ti.com/lit/ds/symlink/cd4060b.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [CD4060-Zeitgeber mit Schaltplan und Platine](https://github.com/jonathanrjpereira/CD4060-Timer) — github.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [CD4060-Timer mit RC-Oszillator](https://dmohankumar.wordpress.com/2012/05/13/design-your-circuit-part-ii-cd-4060-timer/) — dmohankumar.wordpress.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. CD4060-Schaltung bei CD4541/MC14521 nur als Prinzip von Oszillator plus Zähler nutzen. Teilerstufen, Reset, Zeitformeln und Pinfolge müssen dem jeweiligen Datenblatt folgen.

## CD4063

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [4-Bit-Vergleich/Kaskadierung (Grundschaltung)](https://www.electronics-tutorials.ws/combination/comb_8.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Binärvergleich und kaskadierte Komparatoren](https://www.learnabout-electronics.org/Digital/dig43.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [7485: 4-/8-Bit-Vergleich im virtuellen Labor](https://dec-iitkgp.vlabs.ac.in/exp/digital-comparators/theory.html) — dec-iitkgp.vlabs.ac.in; Grundschaltung; geprüft 2026-10-25.
- [7485 mit Schaltern und Ergebnisanzeige](https://faculty-web.msoe.edu/tritt/JohnDeere/jddig02.html) — faculty-web.msoe.edu; Grundschaltung; geprüft 2026-10-25.
- [7485-Kaskadierung zum 24-Bit-Vergleicher](https://tams.informatik.uni-hamburg.de/applets/hades/webdemos/20-arithmetic/45-compare/7485-demo_print.html) — tams.informatik.uni-hamburg.de; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. 7485-Beispiele zeigen das Vergleichsprinzip. CD4063 und HCT85 unterscheiden sich in Pinfolge und elektrischen Kennwerten; Kaskadiereingänge typgerecht setzen.

## CD4066

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Analogsignal schalten (TI-Referenz) (PDF S. 16)](../Datenblaetter/CD4xxx/CD4066_TI.pdf#page=16) · [Online-Original](https://www.ti.com/lit/ds/symlink/cd4066b.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Analoge Schalter und Multiplexer als Grundschaltung](https://www.electronics-tutorials.ws/combination/comb_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [CD4066 als schaltbarer Effekt-Bypass](https://subdecay.com/wp-content/uploads/2024/09/Web-user-guide-EZ-MIDI-1-01.pdf) — subdecay.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [CD4066 im Analog-Synthesizer](https://www.ece.ucf.edu/seniordesign/fa2012sp2013/g06/documents/Term2Paper.pdf) — ece.ucf.edu; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [CD4066 als Analogschalter im Funkgerät](https://collinsradio.org/archives/manuals/KWM380_Self_Study_.pdf) — collinsradio.org; Anwendungsreferenz; geprüft 2026-10-25.
- [CD4016 als elektrisch steuerbarer Analogschalter](https://www.build-electronic-circuits.com/4000-series-integrated-circuits/ic-4016/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.

CD4066B-Referenzschaltung; für CD4016B insbesondere R_on, Leckstrom und zulässige Signalpegel abgleichen. CD4066-Beispiele sind für CD4016 nur Grundschaltungen: Einschaltwiderstand, Signalbereich und Pinbelegung abgleichen.

## CD4068

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## CD4069

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Inverter-Anwendung (TI) (PDF S. 14)](../Datenblaetter/CD4xxx/CD4069_TI.pdf#page=14) · [Online-Original](https://www.ti.com/lit/ds/symlink/cd4069ub.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Quarzoszillator (TI) (PDF S. 11)](../Datenblaetter/CD4xxx/CD4069_TI.pdf#page=11) · [Online-Original](https://www.ti.com/lit/ds/symlink/cd4069ub.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [CD4069 als hochohmiger Verstärker](https://www.build-electronic-circuits.com/4000-series-integrated-circuits/ic-4069/) — build-electronic-circuits.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [LC-Oszillator mit ungebuffertem CMOS-Inverter](https://wiki.analog.com/university/courses/electronics/electronics-lab-21) — analog.com; Grundschaltung; geprüft 2026-10-25.
- [IMSAI Guy: CD4069-RC-Oszillator](https://www.youtube.com/watch?v=wbjmd8vyJQU) — youtube.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [RC-Oszillatoren mit CMOS-Invertern](https://www.doritique.fr/Articles/View_Article.php?num_article=115) — doritique.fr; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Analoge Verstärker- und Oszillatorschaltungen benötigen die ungebufferte UB-Ausführung; den Aufdruck prüfen.

## CD4070

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Vergleich/Parität (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-7/the-exclusive-or-function-xor/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## CD4071

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## CD4072

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## CD4073

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## CD4075

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## CD4077

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Vergleich/Parität (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-7/the-exclusive-or-function-xor/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## CD4081

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## CD4082

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## CD4093

**7/5 Beispiel-Websites**, 8 Quellen-Websites insgesamt. Ziel erreicht.

- [Schmitt-Gatter testen (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Vier Audio-Oszillatoren mit CD4093](https://andreassiagian.wordpress.com/2013/02/22/quad-oscillator-using-4093-tutorial/) — andreassiagian.wordpress.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## CD4094

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Kaskadierte Schieberegister (TI) (PDF S. 3)](../Datenblaetter/CD4xxx/CD4094_TI.pdf#page=3) · [Online-Original](https://www.ti.com/lit/ds/symlink/cd4094b.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Serielle und parallele Schieberegister](https://www.electronics-tutorials.ws/sequential/seq_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [CD4094/CD4021: LEDs ausgeben und Taster einlesen](https://friendlywire.com/tutorials/cd4094-cd4021/) — friendlywire.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## CD4098

**5/5 Beispiel-Websites**, 8 Quellen-Websites insgesamt. Ziel erreicht.

- [RC-Monoflop (Herstellerreferenz)](https://www.ti.com/lit/ds/symlink/cd4098b.pdf#page=1) — ti.com; Hersteller-Grundbeschaltung; geprüft 2026-10-21.
- [Monoflop und Impulsverlängerung als Prinzip](https://www.electronics-tutorials.ws/waveforms/monostable.html) — electronics-tutorials.ws; Prinzipreferenz; geprüft 2026-10-25.
- [CD4047 als Taktgenerator und Monoflop](https://tronixstuff.com/2011/02/11/review-cd4047-astablemonostable-multivibrator/) — tronixstuff.com; Prinzipreferenz; geprüft 2026-10-25.
  Hinweis: Autorenkorrektur beachten: Pin 14 im Monoflop-Schaltbild zusätzlich an +5 V.
- [CD4047-Monoflop und Impulslänge](https://www.bristolwatch.com/geiger/monostable.htm) — bristolwatch.com; Prinzipreferenz; geprüft 2026-10-25.
- [Versuche mit CD4528 und retriggerbaren Monoflops](https://electronique-et-informatique.fr/anglais/Digit/Pratique/Digit_6PS1.php) — electronique-et-informatique.fr; Grundschaltung; geprüft 2026-10-25.
- [CD4538 als Präzisions-Monoflop](https://www.edn.com/precision-monostable/) — edn.com; Grundschaltung; geprüft 2026-10-25.
- [CD4538-Zeitgeber mit Taster und Reset](https://www.homemade-circuits.com/accurate-monostable-timer-circuit-using-ic-4538-cmos/) — homemade-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [CD4538 als einstellbare Impulsverzögerung im Synthesizer](https://www.yusynth.net/Modular/EN/PULSEDELAY/index.html) — yusynth.net; Grundschaltung; geprüft 2026-10-25.
  Hinweis: CD4538-Prinzip; RC-Anschlüsse, Zeitformel und Triggerung nicht unverändert auf diesen Typ übernehmen.

CD4528: MC14528B-Referenz; CD4538: CD14538B-Referenz. Nicht ungeprüft austauschen; Triggerpolarität, Zeitformel und Pinbelegung der konkreten Variante abgleichen. CD4047-Beispiele sind bei anderen Monoflops nur Prinzipreferenzen; Triggerpolarität, Retriggerbarkeit, RC-Pins und Zeitformeln des jeweiligen ICs übernehmen. CD4528-/CD4538-Aufbauten sind bei anderen Monoflops Grundschaltungen; die genaue Zeitformel und Retriggerfunktion sind nicht austauschbar.

## CD4503

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [74244/74245 als Buspuffer](https://learn.adafruit.com/digital-circuits-6-eprom-emulator/the-74244-octal-tristate-buffer) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Praktischer Versuch mit bidirektionalem 74LS245](https://electronique-et-informatique.fr/anglais/Digit/Pratique/Digit_12PS.php) — electronique-et-informatique.fr; Grundschaltung; geprüft 2026-10-25.
- [Geteilte Datenleitung mit Tri-State-Puffern](https://www.cs.emory.edu/~cheung/Courses/355/Syllabus/3-memory/tri-state.html) — cs.emory.edu; Simulationsbeispiel; geprüft 2026-10-25.
- [Puffer mit Freigabe und Tri-State-Bus](https://www.electronics-tutorials.ws/logic/logic_9.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Ausgangsstufen, Busfreigabe und Logikpegel](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Funktionsreferenz; geprüft 2026-10-25.
- [74LS245 als Buspuffer in einer 8255-Schnittstelle](https://tiij.org/issues/issues/4_1/4_1s.html) — tiij.org; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Tri-State-Grundschaltung mit 74244/74245 als Referenz. Invertierende Typen liefern umgekehrte Daten; Richtung und aktive Freigabe des tatsächlichen Typs prüfen. Keine Open-Collector-Verdrahtung annehmen.

## CD4511

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Anzeige-Ansteuerung (Hersteller) (PDF S. 5)](../Datenblaetter/CD4xxx/CD4511_TI.pdf#page=5) · [Online-Original](https://www.ti.com/lit/ds/symlink/cd4511b.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [BCD-Eingabe mit CD4511 und 7-Segment-Anzeige](https://circuitdigest.com/electronic-circuits/7-segment-display-driver-using-ic-cd4511) — circuitdigest.com; Grundschaltung; geprüft 2026-10-25.
- [CD4511-Anzeige auf dem Steckbrett](https://www.circuits-diy.com/how-to-drive-a-7-segment-display-using-bcd-driver-ic-cd4511) — circuits-diy.com; Grundschaltung; geprüft 2026-10-25.
- [Zweistelliger Zähler mit CD4026](https://www.eleccircuit.com/simple-two-digits-counter-using-cd4026/) — eleccircuit.com; Grundschaltung; geprüft 2026-10-25.
- [BCD-Decoder und 7-Segment-Zähler](https://www.electronics-tutorials.ws/counter/7-segment-display.html) — electronics-tutorials.ws; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [7-Segment-Anzeige als Grundschaltung](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/7-segment-display/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.

Anzeigeart und Ausgangspolarität beachten; CD4513/4553 verwenden dokumentierte Motorola/onsemi-Referenzen. Anzeige-Grundschaltungen mit anderen ICs: BCD-Decoder und Zähler nicht verwechseln. Anzeigeart (gemeinsame Anode/Kathode bzw. LCD), aktive Ausgangspegel, Segmentwiderstände und Multiplexsteuerung passend zum Typ wählen. Insbesondere CD4543 kann LCD-Phasenansteuerung verwenden; eine LED-Schaltung ist dafür keine direkte Vorlage.

## CD4513

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Anzeige-Ansteuerung (Hersteller) (PDF S. 7)](../Datenblaetter/CD4xxx/CD4513_MC14513B_onsemi_Referenz.pdf#page=7) · [Online-Original](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/935/MC14513B-Rev2006.pdf) — mm.digikey.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [BCD-Eingabe mit CD4511 und 7-Segment-Anzeige](https://circuitdigest.com/electronic-circuits/7-segment-display-driver-using-ic-cd4511) — circuitdigest.com; Grundschaltung; geprüft 2026-10-25.
- [CD4511-Anzeige auf dem Steckbrett](https://www.circuits-diy.com/how-to-drive-a-7-segment-display-using-bcd-driver-ic-cd4511) — circuits-diy.com; Grundschaltung; geprüft 2026-10-25.
- [Zweistelliger Zähler mit CD4026](https://www.eleccircuit.com/simple-two-digits-counter-using-cd4026/) — eleccircuit.com; Grundschaltung; geprüft 2026-10-25.
- [BCD-Decoder und 7-Segment-Zähler](https://www.electronics-tutorials.ws/counter/7-segment-display.html) — electronics-tutorials.ws; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [7-Segment-Anzeige als Grundschaltung](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/7-segment-display/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.

Anzeigeart und Ausgangspolarität beachten; CD4513/4553 verwenden dokumentierte Motorola/onsemi-Referenzen. Anzeige-Grundschaltungen mit anderen ICs: BCD-Decoder und Zähler nicht verwechseln. Anzeigeart (gemeinsame Anode/Kathode bzw. LCD), aktive Ausgangspegel, Segmentwiderstände und Multiplexsteuerung passend zum Typ wählen. Insbesondere CD4543 kann LCD-Phasenansteuerung verwenden; eine LED-Schaltung ist dafür keine direkte Vorlage.

## CD4518

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zähler kaskadieren (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/asynchronous-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Modulo-/Frequenzteiler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/counter-modulus/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## CD4520

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zähler kaskadieren (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/asynchronous-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Modulo-/Frequenzteiler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/counter-modulus/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## CD4528

**5/5 Beispiel-Websites**, 8 Quellen-Websites insgesamt. Ziel erreicht.

- [RC-Zeitglied und Trigger (onsemi-Typreferenz) (PDF S. 2)](../Datenblaetter/CD4xxx/MC14528B_onsemi.pdf#page=2) · [Online-Original](https://www.onsemi.com/download/data-sheet/pdf/mc14528b-d.pdf) — onsemi.com; Herstellerbeschaltung; geprüft 2026-10-21.
- [Monoflop und Impulsverlängerung als Prinzip](https://www.electronics-tutorials.ws/waveforms/monostable.html) — electronics-tutorials.ws; Prinzipreferenz; geprüft 2026-10-25.
- [CD4047 als Taktgenerator und Monoflop](https://tronixstuff.com/2011/02/11/review-cd4047-astablemonostable-multivibrator/) — tronixstuff.com; Prinzipreferenz; geprüft 2026-10-25.
  Hinweis: Autorenkorrektur beachten: Pin 14 im Monoflop-Schaltbild zusätzlich an +5 V.
- [CD4047-Monoflop und Impulslänge](https://www.bristolwatch.com/geiger/monostable.htm) — bristolwatch.com; Prinzipreferenz; geprüft 2026-10-25.
- [Versuche mit CD4528 und retriggerbaren Monoflops](https://electronique-et-informatique.fr/anglais/Digit/Pratique/Digit_6PS1.php) — electronique-et-informatique.fr; Grundschaltung; geprüft 2026-10-25.
- [CD4538 als Präzisions-Monoflop](https://www.edn.com/precision-monostable/) — edn.com; Grundschaltung; geprüft 2026-10-25.
- [CD4538-Zeitgeber mit Taster und Reset](https://www.homemade-circuits.com/accurate-monostable-timer-circuit-using-ic-4538-cmos/) — homemade-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [CD4538 als einstellbare Impulsverzögerung im Synthesizer](https://www.yusynth.net/Modular/EN/PULSEDELAY/index.html) — yusynth.net; Grundschaltung; geprüft 2026-10-25.
  Hinweis: CD4538-Prinzip; RC-Anschlüsse, Zeitformel und Triggerung nicht unverändert auf diesen Typ übernehmen.

Aufdruck MC14528BCP, Hersteller onsemi vom Nutzer bestätigt. onsemi-Herstellerdatenblatt zur MC14528B-Familie; aktuelle Ausgabe zeigt SOIC, vorhandene CP-Ausführung ist DIP-16. Pins 1, 8 und 15: VSS/GND; externe Zeitglieder laut Datenblatt anschließen. CD4047-Beispiele sind bei anderen Monoflops nur Prinzipreferenzen; Triggerpolarität, Retriggerbarkeit, RC-Pins und Zeitformeln des jeweiligen ICs übernehmen. CD4528-/CD4538-Aufbauten sind bei anderen Monoflops Grundschaltungen; die genaue Zeitformel und Retriggerfunktion sind nicht austauschbar.

## CD4538

**5/5 Beispiel-Websites**, 9 Quellen-Websites insgesamt. Ziel erreicht.

- [RC-Zeitglied und Trigger (onsemi-Typreferenz) (PDF S. 2)](../Datenblaetter/CD4xxx/MC14538B_onsemi.pdf#page=2) · [Online-Original](https://www.onsemi.com/download/data-sheet/pdf/mc14538b-d.pdf) — onsemi.com; Nachfolger-/Typreferenz; geprüft 2026-10-21.
- [Monoflop und Impulsverlängerung als Prinzip](https://www.electronics-tutorials.ws/waveforms/monostable.html) — electronics-tutorials.ws; Prinzipreferenz; geprüft 2026-10-25.
- [CD4047 als Taktgenerator und Monoflop](https://tronixstuff.com/2011/02/11/review-cd4047-astablemonostable-multivibrator/) — tronixstuff.com; Prinzipreferenz; geprüft 2026-10-25.
  Hinweis: Autorenkorrektur beachten: Pin 14 im Monoflop-Schaltbild zusätzlich an +5 V.
- [CD4047-Monoflop und Impulslänge](https://www.bristolwatch.com/geiger/monostable.htm) — bristolwatch.com; Prinzipreferenz; geprüft 2026-10-25.
- [Versuche mit CD4528 und retriggerbaren Monoflops](https://electronique-et-informatique.fr/anglais/Digit/Pratique/Digit_6PS1.php) — electronique-et-informatique.fr; Grundschaltung; geprüft 2026-10-25.
- [CD4538 als Präzisions-Monoflop](https://www.edn.com/precision-monostable/) — edn.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [CD4538-Zeitgeber mit Taster und Reset](https://www.homemade-circuits.com/accurate-monostable-timer-circuit-using-ic-4538-cmos/) — homemade-circuits.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [CD4538 als einstellbare Impulsverzögerung im Synthesizer](https://www.yusynth.net/Modular/EN/PULSEDELAY/index.html) — yusynth.net; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
  Hinweis: Modul arbeitet mit höheren Versorgungsspannungen; Zeiten und Pegel bei 5 V neu auslegen.
- [CD4538: retriggerbare und nicht retriggerbare Monoflops](https://www.hxymos.com/web/userfiles/productfile/Adatasheet/Other/SOP_16_CD4538.pdf) — hxymos.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
  Hinweis: Andere Herstellervariante im SOP-Gehäuse. Hersteller-Pinbelegung und RC-Grenzen prüfen.

Aufdruck MC14538BCP, Hersteller Motorola vom Nutzer bestätigt. onsemi-Datenblatt als Nachfolger-/Typreferenz; vorhandene Motorola-CP-Ausführung ist DIP-16, keine Bestätigung der aktuellen Gehäusevarianten. Pins 1, 8 und 15: VSS/GND; externe Zeitglieder laut Datenblatt anschließen. CD4047-Beispiele sind bei anderen Monoflops nur Prinzipreferenzen; Triggerpolarität, Retriggerbarkeit, RC-Pins und Zeitformeln des jeweiligen ICs übernehmen. CD4528-/CD4538-Aufbauten sind bei anderen Monoflops Grundschaltungen; die genaue Zeitformel und Retriggerfunktion sind nicht austauschbar.

## CD4541

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Digitaler Timer (TI) (PDF S. 5)](../Datenblaetter/CD4xxx/CD4541_TI.pdf#page=5) · [Online-Original](https://www.ti.com/lit/ds/symlink/cd4541b.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [CD4060-Zeitgeber mit Schaltplan und Platine](https://github.com/jonathanrjpereira/CD4060-Timer) — github.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [CD4060-Timer mit RC-Oszillator](https://dmohankumar.wordpress.com/2012/05/13/design-your-circuit-part-ii-cd-4060-timer/) — dmohankumar.wordpress.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. CD4060-Schaltung bei CD4541/MC14521 nur als Prinzip von Oszillator plus Zähler nutzen. Teilerstufen, Reset, Zeitformeln und Pinfolge müssen dem jeweiligen Datenblatt folgen.

## CD4543

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [BCD-Anzeige (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/7-segment-display/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [BCD-Eingabe mit CD4511 und 7-Segment-Anzeige](https://circuitdigest.com/electronic-circuits/7-segment-display-driver-using-ic-cd4511) — circuitdigest.com; Grundschaltung; geprüft 2026-10-25.
- [CD4511-Anzeige auf dem Steckbrett](https://www.circuits-diy.com/how-to-drive-a-7-segment-display-using-bcd-driver-ic-cd4511) — circuits-diy.com; Grundschaltung; geprüft 2026-10-25.
- [Zweistelliger Zähler mit CD4026](https://www.eleccircuit.com/simple-two-digits-counter-using-cd4026/) — eleccircuit.com; Grundschaltung; geprüft 2026-10-25.
- [BCD-Decoder und 7-Segment-Zähler](https://www.electronics-tutorials.ws/counter/7-segment-display.html) — electronics-tutorials.ws; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.

Grundprinzip der BCD-Anzeige; für CD4543 Anzeigetyp, Phaseneingang, Segmentwiderstände und Pinfolge gemäß seinem Datenblatt anpassen. Die 4511-Verdrahtung nicht unverändert übernehmen. Anzeige-Grundschaltungen mit anderen ICs: BCD-Decoder und Zähler nicht verwechseln. Anzeigeart (gemeinsame Anode/Kathode bzw. LCD), aktive Ausgangspegel, Segmentwiderstände und Multiplexsteuerung passend zum Typ wählen. Insbesondere CD4543 kann LCD-Phasenansteuerung verwenden; eine LED-Schaltung ist dafür keine direkte Vorlage.

## CD4553

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Anzeige-Ansteuerung (Hersteller) (PDF S. 6)](../Datenblaetter/CD4xxx/CD4553_MC14553B_Motorola_Referenz.pdf#page=6) · [Online-Original](https://datasheet4u.com/pdf/556632/MC14553B.pdf) — datasheet4u.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [BCD-Eingabe mit CD4511 und 7-Segment-Anzeige](https://circuitdigest.com/electronic-circuits/7-segment-display-driver-using-ic-cd4511) — circuitdigest.com; Grundschaltung; geprüft 2026-10-25.
- [CD4511-Anzeige auf dem Steckbrett](https://www.circuits-diy.com/how-to-drive-a-7-segment-display-using-bcd-driver-ic-cd4511) — circuits-diy.com; Grundschaltung; geprüft 2026-10-25.
- [Zweistelliger Zähler mit CD4026](https://www.eleccircuit.com/simple-two-digits-counter-using-cd4026/) — eleccircuit.com; Grundschaltung; geprüft 2026-10-25.
- [BCD-Decoder und 7-Segment-Zähler](https://www.electronics-tutorials.ws/counter/7-segment-display.html) — electronics-tutorials.ws; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [7-Segment-Anzeige als Grundschaltung](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/7-segment-display/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.

Anzeigeart und Ausgangspolarität beachten; CD4513/4553 verwenden dokumentierte Motorola/onsemi-Referenzen. Anzeige-Grundschaltungen mit anderen ICs: BCD-Decoder und Zähler nicht verwechseln. Anzeigeart (gemeinsame Anode/Kathode bzw. LCD), aktive Ausgangspegel, Segmentwiderstände und Multiplexsteuerung passend zum Typ wählen. Insbesondere CD4543 kann LCD-Phasenansteuerung verwenden; eine LED-Schaltung ist dafür keine direkte Vorlage.

## CD40194BE

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Universelles Schieberegister (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-12/parallel-in-parallel-out-universal-shift-register/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Serielle und parallele Schieberegister](https://www.electronics-tutorials.ws/sequential/seq_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Grundschaltung, Pinbelegung und Logikpegel am vorhandenen Typ prüfen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## 40098

**5/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [3-State-Enable: Funktionsreferenz HEF40098B](https://assets.nexperia.com/documents/data-sheet/HEF40098B.pdf#page=2) — assets.nexperia.com; Funktionsreferenz, keine vollständige Beispielschaltung; geprüft 2026-10-21.
- [74244/74245 als Buspuffer](https://learn.adafruit.com/digital-circuits-6-eprom-emulator/the-74244-octal-tristate-buffer) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Praktischer Versuch mit bidirektionalem 74LS245](https://electronique-et-informatique.fr/anglais/Digit/Pratique/Digit_12PS.php) — electronique-et-informatique.fr; Grundschaltung; geprüft 2026-10-25.
- [Geteilte Datenleitung mit Tri-State-Puffern](https://www.cs.emory.edu/~cheung/Courses/355/Syllabus/3-memory/tri-state.html) — cs.emory.edu; Simulationsbeispiel; geprüft 2026-10-25.
- [Puffer mit Freigabe und Tri-State-Bus](https://www.electronics-tutorials.ws/logic/logic_9.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Ausgangsstufen, Busfreigabe und Logikpegel](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Funktionsreferenz; geprüft 2026-10-25.
- [74LS245 als Buspuffer in einer 8255-Schnittstelle](https://tiij.org/issues/issues/4_1/4_1s.html) — tiij.org; Grundschaltung; geprüft 2026-10-25.

Typreferenz mit Funktions-/Logikdiagramm, keine vollständige Beispielschaltung. Genaue Herstellervariante ungeklärt. Tri-State-Grundschaltung mit 74244/74245 als Referenz. Invertierende Typen liefern umgekehrte Daten; Richtung und aktive Freigabe des tatsächlichen Typs prüfen. Keine Open-Collector-Verdrahtung annehmen.

## MC14521BCP

**4/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Weitere passende Beispiele gesucht.

- [Quarzoszillator (onsemi-Nachfolgerreferenz) (PDF S. 5)](../Datenblaetter/CD4xxx/MC14521B_onsemi.pdf#page=5) · [Online-Original](https://www.onsemi.com/download/data-sheet/pdf/mc14521b-d.pdf) — onsemi.com; Nachfolger-/Typreferenz; geprüft 2026-10-21.
- [CD4060-Zeitgeber mit Schaltplan und Platine](https://github.com/jonathanrjpereira/CD4060-Timer) — github.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [CD4060-Timer mit RC-Oszillator](https://dmohankumar.wordpress.com/2012/05/13/design-your-circuit-part-ii-cd-4060-timer/) — dmohankumar.wordpress.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Aufdruck MC14521BCP, Hersteller Motorola vom Nutzer bestätigt. onsemi-Datenblatt als Nachfolger-/Typreferenz; vorhandene Motorola-CP-Ausführung ist DIP-16, keine Bestätigung der aktuellen Gehäusevarianten. CD4060-Schaltung bei CD4541/MC14521 nur als Prinzip von Oszillator plus Zähler nutzen. Teilerstufen, Reset, Zeitformeln und Pinfolge müssen dem jeweiligen Datenblatt folgen.

**Recherchebedarf:** Bisher sind weniger als fünf unterschiedliche Websites mit passenden Beispielen belegt. Die vorhandenen Grundschaltungen und Referenzen sind oben gekennzeichnet; es wurden keine zusätzlichen Beschaltungen erfunden.
