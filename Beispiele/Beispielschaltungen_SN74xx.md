# Schaltungsbeispiele: SN74xx

[Übersicht](README.md) · [Gesamtsammlung](Beispielschaltungen.md) · [Recherchebedarf](Recherchebedarf.md) · [Bestand](../Bauteile.md)

91 Bauteile, 553 Linkzuordnungen. Erweiterungsstand: **25.10.2026**; Prüfdatum jeweils am Link.

Ziel sind etwa **fünf unterschiedliche Websites pro Bauteil**. Gezählt werden Websites mit Schaltungsbeispielen, übertragbaren Grundschaltungen, Modulbeispielen oder Code mit Anschlusszuordnung. Reine Funktions-/Prinzipreferenzen und Entwurfshilfen zählen zusätzlich als Quellen, aber nicht zum Beispielziel. Subdomains und bekannte Länderspiegel zählen zusammen. Mehrere Artikel derselben Website erhöhen die Zahl nicht.

**Grundschaltung** bedeutet: Das Schaltungsprinzip ist übertragbar, der Artikel verwendet gegebenenfalls ein anderes Bauteil. Sie ist keine Bestätigung der Pinbelegung oder Dimensionierung des vorhandenen Typs. **Modulbeispiele** enthalten zusätzliche Komponenten; **Funktionsreferenzen** sind keine vollständigen Nachbauschaltungen. Hinweise stehen direkt beim Bauteil und Link.

Versorgung, Pinfolge, Polarität, Logikfamilie, Freigaben, Taktflanken und Grenzwerte anhand des konkreten Datenblatts prüfen. 74LS benötigt +5 V. Pro IC üblicherweise 100 nF abblocken, Taster für Zähler entprellen. Transistor- und Diodenwerte an Last und Verlustleistung anpassen. Bei Relais gilt die tatsächliche Spulenspannung. TRIAC-Artikel können Netzspannungsschaltungen enthalten.

Pflege: [Beispielschaltungen.json](Beispielschaltungen.json). `python3 scripts/update_examples.py` erzeugt ausschließlich diese Sammlungen. Bestand und Datenbank bleiben unverändert. Bei lokalen PDFs führt „Online-Original“ zur dokumentierten Downloadquelle; neuere Revisionen können andere Seitenzahlen haben.

## SN74LS00N

**7/5 Beispiel-Websites**, 8 Quellen-Websites insgesamt. Ziel erreicht.

- [Fehlererkennung (TI) (PDF S. 11)](../Datenblaetter/SN7xxx/SN74LS00N_TI.pdf#page=11) · [Online-Original](https://www.ti.com/lit/ds/symlink/sn74ls00.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## SN74LS02N

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

## SN74LS04N

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## SN74LS05N

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Open-Collector-Ansteuerung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-3/special-output-gates/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Open-Collector-Schalter und Pull-up-Auslegung](https://cfi.iitm.ac.in/elec-club/articles/pages/Basics/PullUp-Down%20Resistors.html) — cfi.iitm.ac.in; Grundschaltung; geprüft 2026-10-25.
- [Open-Collector-Verknüpfung und Busbeispiele](https://nucleus.iaea.org/sites/nuclear-instrumentation/Shared%20Documents/Digital%20Electronics/DigitalText.pdf) — nucleus.iaea.org; Grundschaltung; geprüft 2026-10-25.
- [Open-Collector-Lastschalter und Pegelanpassung](https://www.electronics-tutorials.ws/transistor/open-collector-outputs.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Ausgangsstufen, Busfreigabe und Logikpegel](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Funktionsreferenz; geprüft 2026-10-25.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Open-Collector-Grundschaltung: zulässige Ausgangsspannung und Senkstrom typbezogen prüfen; Logikfunktion (Inverter, NAND, XNOR) bleibt die des vorhandenen ICs. Die Transistorschalter-Quelle zeigt die externe Lastbeschaltung einer Senkstufe; sie ersetzt nicht die Logikfunktion des ICs.

## SN74LS06N

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Lastansteuerung (TI) (PDF S. 9)](../Datenblaetter/SN7xxx/SN74LS06N_TI.pdf#page=9) · [Online-Original](https://www.ti.com/lit/ds/symlink/sn74ls06.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Open-Collector-Ansteuerung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-3/special-output-gates/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Open-Collector-Schalter und Pull-up-Auslegung](https://cfi.iitm.ac.in/elec-club/articles/pages/Basics/PullUp-Down%20Resistors.html) — cfi.iitm.ac.in; Grundschaltung; geprüft 2026-10-25.
- [Open-Collector-Verknüpfung und Busbeispiele](https://nucleus.iaea.org/sites/nuclear-instrumentation/Shared%20Documents/Digital%20Electronics/DigitalText.pdf) — nucleus.iaea.org; Grundschaltung; geprüft 2026-10-25.
- [Open-Collector-Lastschalter und Pegelanpassung](https://www.electronics-tutorials.ws/transistor/open-collector-outputs.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Ausgangsstufen, Busfreigabe und Logikpegel](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Funktionsreferenz; geprüft 2026-10-25.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Open-Collector-Grundschaltung: zulässige Ausgangsspannung und Senkstrom typbezogen prüfen; Logikfunktion (Inverter, NAND, XNOR) bleibt die des vorhandenen ICs. Die Transistorschalter-Quelle zeigt die externe Lastbeschaltung einer Senkstufe; sie ersetzt nicht die Logikfunktion des ICs.

## SN74LS07N

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Lastansteuerung (TI) (PDF S. 8)](../Datenblaetter/SN7xxx/SN74LS07N_TI.pdf#page=8) · [Online-Original](https://www.ti.com/lit/ds/symlink/sn74ls07.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Open-Collector-Ansteuerung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-3/special-output-gates/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Open-Collector-Schalter und Pull-up-Auslegung](https://cfi.iitm.ac.in/elec-club/articles/pages/Basics/PullUp-Down%20Resistors.html) — cfi.iitm.ac.in; Grundschaltung; geprüft 2026-10-25.
- [Open-Collector-Verknüpfung und Busbeispiele](https://nucleus.iaea.org/sites/nuclear-instrumentation/Shared%20Documents/Digital%20Electronics/DigitalText.pdf) — nucleus.iaea.org; Grundschaltung; geprüft 2026-10-25.
- [Open-Collector-Lastschalter und Pegelanpassung](https://www.electronics-tutorials.ws/transistor/open-collector-outputs.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Ausgangsstufen, Busfreigabe und Logikpegel](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Funktionsreferenz; geprüft 2026-10-25.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Open-Collector-Grundschaltung: zulässige Ausgangsspannung und Senkstrom typbezogen prüfen; Logikfunktion (Inverter, NAND, XNOR) bleibt die des vorhandenen ICs. Die Transistorschalter-Quelle zeigt die externe Lastbeschaltung einer Senkstufe; sie ersetzt nicht die Logikfunktion des ICs.

## SN74LS08N

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## SN74LS10N

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## SN74LS11N

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## 7412

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Open-Collector-Ansteuerung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-3/special-output-gates/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Open-Collector-Schalter und Pull-up-Auslegung](https://cfi.iitm.ac.in/elec-club/articles/pages/Basics/PullUp-Down%20Resistors.html) — cfi.iitm.ac.in; Grundschaltung; geprüft 2026-10-25.
- [Open-Collector-Verknüpfung und Busbeispiele](https://nucleus.iaea.org/sites/nuclear-instrumentation/Shared%20Documents/Digital%20Electronics/DigitalText.pdf) — nucleus.iaea.org; Grundschaltung; geprüft 2026-10-25.
- [Open-Collector-Lastschalter und Pegelanpassung](https://www.electronics-tutorials.ws/transistor/open-collector-outputs.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Ausgangsstufen, Busfreigabe und Logikpegel](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Funktionsreferenz; geprüft 2026-10-25.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Open-Collector-Grundschaltung: zulässige Ausgangsspannung und Senkstrom typbezogen prüfen; Logikfunktion (Inverter, NAND, XNOR) bleibt die des vorhandenen ICs. Die Transistorschalter-Quelle zeigt die externe Lastbeschaltung einer Senkstufe; sie ersetzt nicht die Logikfunktion des ICs.

## SN74LS14N

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Signalaufbereitung (TTL-Referenz) (PDF S. 14)](../Datenblaetter/SN7xxx/SN74LS14N_TI.pdf#page=14) · [Online-Original](https://www.ti.com/lit/ds/symlink/sn74ls14.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [74LS14-Oszillator mit gemessenen RC-Varianten](https://leap.tardate.com/electronics101/74ls14/schmittoscillator/) — leap.tardate.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [74LS14-RC-Oszillator und Taktteiler](https://electronics-course.com/schmitt-trigger-oscillator) — electronics-course.com; Grundschaltung; geprüft 2026-10-25.
- [74LS14-Oszillator mit Pull-up und RC-Netzwerk](https://www.kennethkuhn.com/students/ee431/oscillator_hw.pdf) — kennethkuhn.com; Grundschaltung; geprüft 2026-10-25.
- [w2aew: Schmitt-Trigger-Taktgenerator mit 74AC14](https://www.youtube.com/watch?v=NuXitMK3HSA) — youtube.com; Grundschaltung; geprüft 2026-10-25.
  Hinweis: Video des Autors; CMOS-Referenz, RC-Werte nicht ungeprüft auf LS14 übertragen.
- [Schmitt-Trigger-Inverter als Signalaufbereitung](https://www.electronics-tutorials.ws/logic/logic_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Bei LS14 sind wegen des TTL-Eingangsstroms deutlich kleinere RC-Widerstände erforderlich als bei CMOS-Schmitt-Triggern.

## 7416

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Open-Collector-Ansteuerung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-3/special-output-gates/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Open-Collector-Schalter und Pull-up-Auslegung](https://cfi.iitm.ac.in/elec-club/articles/pages/Basics/PullUp-Down%20Resistors.html) — cfi.iitm.ac.in; Grundschaltung; geprüft 2026-10-25.
- [Open-Collector-Verknüpfung und Busbeispiele](https://nucleus.iaea.org/sites/nuclear-instrumentation/Shared%20Documents/Digital%20Electronics/DigitalText.pdf) — nucleus.iaea.org; Grundschaltung; geprüft 2026-10-25.
- [Open-Collector-Lastschalter und Pegelanpassung](https://www.electronics-tutorials.ws/transistor/open-collector-outputs.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Ausgangsstufen, Busfreigabe und Logikpegel](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Funktionsreferenz; geprüft 2026-10-25.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Open-Collector-Grundschaltung: zulässige Ausgangsspannung und Senkstrom typbezogen prüfen; Logikfunktion (Inverter, NAND, XNOR) bleibt die des vorhandenen ICs. Die Transistorschalter-Quelle zeigt die externe Lastbeschaltung einer Senkstufe; sie ersetzt nicht die Logikfunktion des ICs.

## SN74LS20N

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## SN74LS21N

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## SN74LS27N

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

## SN74LS30N

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## SN74LS32N

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## 7438

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Open-Collector-Ansteuerung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-3/special-output-gates/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Open-Collector-Schalter und Pull-up-Auslegung](https://cfi.iitm.ac.in/elec-club/articles/pages/Basics/PullUp-Down%20Resistors.html) — cfi.iitm.ac.in; Grundschaltung; geprüft 2026-10-25.
- [Open-Collector-Verknüpfung und Busbeispiele](https://nucleus.iaea.org/sites/nuclear-instrumentation/Shared%20Documents/Digital%20Electronics/DigitalText.pdf) — nucleus.iaea.org; Grundschaltung; geprüft 2026-10-25.
- [Open-Collector-Lastschalter und Pegelanpassung](https://www.electronics-tutorials.ws/transistor/open-collector-outputs.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Ausgangsstufen, Busfreigabe und Logikpegel](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Funktionsreferenz; geprüft 2026-10-25.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Open-Collector-Grundschaltung: zulässige Ausgangsspannung und Senkstrom typbezogen prüfen; Logikfunktion (Inverter, NAND, XNOR) bleibt die des vorhandenen ICs. Die Transistorschalter-Quelle zeigt die externe Lastbeschaltung einer Senkstufe; sie ersetzt nicht die Logikfunktion des ICs.

## 7440

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## SN74LS42N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Adress-/Leitungsdecoder (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-9/decoder/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Signalverteilung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-9/demultiplexers/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Binärdecoder und Leitungsauswahl](https://www.electronics-tutorials.ws/combination/comb_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Encoder, Decoder und Adressauswahl](https://www.learnabout-electronics.org/Digital/dig44.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Decoder, Multiplexer und Addierer](https://learn.adafruit.com/combinational-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Multiplexer und Decoder aus Gattern](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Ergänzte Lehrschaltung: Kanalzahl, Taktflanke, Freigaben und aktive Pegel mit dem konkreten IC abgleichen.

## SN74LS47N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [7-Segment-Anzeige (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/7-segment-display/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [BCD-Zähler mit 74LS90 und 74LS47](https://www.electronics-tutorials.ws/counter/bcd-counter-circuit.html) — electronics-tutorials.ws; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [7-Segment-Anzeige und zweistelliger Zähler](https://www.electronics-tutorials.ws/counter/7-segment-display.html) — electronics-tutorials.ws; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [BCD-Eingabe mit CD4511 und 7-Segment-Anzeige](https://circuitdigest.com/electronic-circuits/7-segment-display-driver-using-ic-cd4511) — circuitdigest.com; Grundschaltung; geprüft 2026-10-25.
- [CD4511-Anzeige auf dem Steckbrett](https://www.circuits-diy.com/how-to-drive-a-7-segment-display-using-bcd-driver-ic-cd4511) — circuits-diy.com; Grundschaltung; geprüft 2026-10-25.
- [Zweistelliger Zähler mit CD4026](https://www.eleccircuit.com/simple-two-digits-counter-using-cd4026/) — eleccircuit.com; Grundschaltung; geprüft 2026-10-25.

Grundschaltung mit 4511: Segmentwiderstände, gemeinsame Anode/Kathode, Ausgangspolarität und Pinfolge an den vorhandenen Treiber anpassen. Anzeige-Grundschaltungen mit anderen ICs: BCD-Decoder und Zähler nicht verwechseln. Anzeigeart (gemeinsame Anode/Kathode bzw. LCD), aktive Ausgangspegel, Segmentwiderstände und Multiplexsteuerung passend zum Typ wählen. Insbesondere CD4543 kann LCD-Phasenansteuerung verwenden; eine LED-Schaltung ist dafür keine direkte Vorlage.

## SN74LS48N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [7-Segment-Anzeige (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/7-segment-display/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [BCD-Eingabe mit CD4511 und 7-Segment-Anzeige](https://circuitdigest.com/electronic-circuits/7-segment-display-driver-using-ic-cd4511) — circuitdigest.com; Grundschaltung; geprüft 2026-10-25.
- [CD4511-Anzeige auf dem Steckbrett](https://www.circuits-diy.com/how-to-drive-a-7-segment-display-using-bcd-driver-ic-cd4511) — circuits-diy.com; Grundschaltung; geprüft 2026-10-25.
- [Zweistelliger Zähler mit CD4026](https://www.eleccircuit.com/simple-two-digits-counter-using-cd4026/) — eleccircuit.com; Grundschaltung; geprüft 2026-10-25.
- [BCD-Decoder und 7-Segment-Zähler](https://www.electronics-tutorials.ws/counter/7-segment-display.html) — electronics-tutorials.ws; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.

Grundschaltung mit 4511: Segmentwiderstände, gemeinsame Anode/Kathode, Ausgangspolarität und Pinfolge an den vorhandenen Treiber anpassen. Anzeige-Grundschaltungen mit anderen ICs: BCD-Decoder und Zähler nicht verwechseln. Anzeigeart (gemeinsame Anode/Kathode bzw. LCD), aktive Ausgangspegel, Segmentwiderstände und Multiplexsteuerung passend zum Typ wählen. Insbesondere CD4543 kann LCD-Phasenansteuerung verwenden; eine LED-Schaltung ist dafür keine direkte Vorlage.

## SN74LS51N

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Verknüpfungslogik (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-7/circuit-simplification-examples/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## SN74LS54N

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Verknüpfungslogik (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-7/circuit-simplification-examples/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## SN74LS55N

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Verknüpfungslogik (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-7/circuit-simplification-examples/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## 7460

**1/5 Beispiel-Websites**, 1 Quellen-Websites insgesamt. Weitere passende Beispiele gesucht.

- [Gattererweiterung an 7450 (TI-Referenz) (PDF S. 1)](../Datenblaetter/SN7xxx/7460_TI_Referenz.pdf#page=1) · [Online-Original](https://sapr.asvcorp.ru/datasheets/33/02/00000000233.pdf) — sapr.asvcorp.ru; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.

Dokument beschreibt den Anschluss an X/X-invertiert eines passenden SN7450/7423/7453. Referenzfamilien beachten; kein gewöhnlicher Logikausgang und nicht ungeprüft an LS-Gatter anschließen.

**Recherchebedarf:** Spezial-Expander für passende 7450/7423/7453. Es ist bislang nur die Herstellerbeschaltung belegt; gewöhnliche Gatterbeispiele sind kein Ersatz.

## SN74LS73N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [JK-Flipflop/Teiler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-10/j-k-flip-flop/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Binärzähler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/asynchronous-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [JK-Flipflop und Master-Slave-Prinzip](https://www.electronics-tutorials.ws/sequential/seq_2.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Ergänzte Lehrschaltung: Kanalzahl, Taktflanke, Freigaben und aktive Pegel mit dem konkreten IC abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## SN74LS74N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [D-Flipflop (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-10/edge-triggered-latches-flip-flops/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Registeraufbau (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-12/parallel-in-parallel-out-universal-shift-register/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [D-Flipflop als Speicher und Frequenzteiler](https://www.electronics-tutorials.ws/sequential/seq_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Serielle und parallele Schieberegister](https://www.electronics-tutorials.ws/sequential/seq_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Ergänzte Lehrschaltung: Kanalzahl, Taktflanke, Freigaben und aktive Pegel mit dem konkreten IC abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## SN74LS75N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Daten zwischenspeichern (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-10/d-latch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [D-Flipflop als Speicher und Teiler](https://www.electronics-tutorials.ws/sequential/seq_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## SN74LS76N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [JK-Flipflop/Teiler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-10/j-k-flip-flop/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Binärzähler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/asynchronous-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [JK-Flipflop und Master-Slave-Prinzip](https://www.electronics-tutorials.ws/sequential/seq_2.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Ergänzte Lehrschaltung: Kanalzahl, Taktflanke, Freigaben und aktive Pegel mit dem konkreten IC abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## SN74LS83N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Binäraddition (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-9/full-adder/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Binäraddierer und Addierer/Subtrahierer](https://www.learnabout-electronics.org/Digital/dig41.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [7483 als 4-/8-Bit-Addierer und Subtrahierer](https://dec-iitkgp.vlabs.ac.in/exp/arithmetic-expressions/theory.html) — dec-iitkgp.vlabs.ac.in; Grundschaltung; geprüft 2026-10-25.
- [Laborversuch: 7483 mit XOR als Subtrahierer](https://www.calstatela.edu/sites/default/files/2449_pre2017_ex8.pdf) — calstatela.edu; Grundschaltung; geprüft 2026-10-25.
- [7483 mit 74161 und Schaltern als Operanden](https://www.eng.auburn.edu/~niuguof/2210lab/ex04_adders_multisim.pdf) — eng.auburn.edu; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. 74LS83A hat andere Versorgungsanschlüsse als 74LS283; Pinfolge des vorhandenen Typs beachten.

## SN74ACT86N

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Vergleich/Parität (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-7/the-exclusive-or-function-xor/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## SN74LS86N

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Vergleich/Parität (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-7/the-exclusive-or-function-xor/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## 7487

**0/5 Beispiel-Websites**, 1 Quellen-Websites insgesamt. Weitere passende Beispiele gesucht.

- [Direkt/Invertiert/0/1 (TI-Referenz) (PDF S. 1)](../Datenblaetter/SN7xxx/7487_TI_Datenbuchauszug.pdf#page=1) · [Online-Original](https://bitsavers.org/components/ti/_dataBooks/1985_TI_The_TTL_Data_Book_Vol_2.pdf) — bitsavers.org; Funktionsreferenz (lokales PDF); geprüft 2026-10-21.

Ansteuerbeispiel anhand Funktionstabelle der Referenz SN74H87; tatsächliche Familie weiterhin abgleichen.

**Recherchebedarf:** Bisher ist nur die TI-Funktionsreferenz belegt; keine fünf unabhängigen Aufbauten zugeordnet. Genaue Logikfamilie am Bauteil klären.

## SN74LS90N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zähler kaskadieren (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/asynchronous-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Modulo-/Frequenzteiler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/counter-modulus/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [BCD-Zähler mit 74LS90 und 74LS47](https://www.electronics-tutorials.ws/counter/bcd-counter-circuit.html) — electronics-tutorials.ws; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [7-Segment-Anzeige und zweistelliger Zähler](https://www.electronics-tutorials.ws/counter/7-segment-display.html) — electronics-tutorials.ws; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## SN74LS92N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zähler kaskadieren (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/asynchronous-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Modulo-/Frequenzteiler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/counter-modulus/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## SN74LS93N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zähler kaskadieren (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/asynchronous-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Modulo-/Frequenzteiler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/counter-modulus/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## SN74LS95N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Paralleles Laden/Schieben (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-12/parallel-in-parallel-out-universal-shift-register/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Serielle und parallele Schieberegister](https://www.electronics-tutorials.ws/sequential/seq_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## SN74LS107N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [JK-Flipflop/Teiler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-10/j-k-flip-flop/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Binärzähler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/asynchronous-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [JK-Flipflop und Master-Slave-Prinzip](https://www.electronics-tutorials.ws/sequential/seq_2.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Ergänzte Lehrschaltung: Kanalzahl, Taktflanke, Freigaben und aktive Pegel mit dem konkreten IC abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## 74109

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [JK-Flipflop/Teiler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-10/j-k-flip-flop/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Binärzähler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/asynchronous-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [JK-Flipflop und Master-Slave-Prinzip](https://www.electronics-tutorials.ws/sequential/seq_2.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Ergänzte Lehrschaltung: Kanalzahl, Taktflanke, Freigaben und aktive Pegel mit dem konkreten IC abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## SN74LS112N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [JK-Flipflop/Teiler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-10/j-k-flip-flop/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Binärzähler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/asynchronous-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [JK-Flipflop und Master-Slave-Prinzip](https://www.electronics-tutorials.ws/sequential/seq_2.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Ergänzte Lehrschaltung: Kanalzahl, Taktflanke, Freigaben und aktive Pegel mit dem konkreten IC abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## SN74LS138N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Adress-/Leitungsdecoder (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-9/decoder/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Signalverteilung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-9/demultiplexers/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Binärdecoder und Leitungsauswahl](https://www.electronics-tutorials.ws/combination/comb_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Encoder, Decoder und Adressauswahl](https://www.learnabout-electronics.org/Digital/dig44.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Decoder, Multiplexer und Addierer](https://learn.adafruit.com/combinational-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Multiplexer und Decoder aus Gattern](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Ergänzte Lehrschaltung: Kanalzahl, Taktflanke, Freigaben und aktive Pegel mit dem konkreten IC abgleichen.

## SN74LS139N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Adress-/Leitungsdecoder (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-9/decoder/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Signalverteilung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-9/demultiplexers/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Binärdecoder und Leitungsauswahl](https://www.electronics-tutorials.ws/combination/comb_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Encoder, Decoder und Adressauswahl](https://www.learnabout-electronics.org/Digital/dig44.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Decoder, Multiplexer und Addierer](https://learn.adafruit.com/combinational-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Multiplexer und Decoder aus Gattern](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Ergänzte Lehrschaltung: Kanalzahl, Taktflanke, Freigaben und aktive Pegel mit dem konkreten IC abgleichen.

## SN74LS145N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Adress-/Leitungsdecoder (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-9/decoder/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Signalverteilung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-9/demultiplexers/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Binärdecoder und Leitungsauswahl](https://www.electronics-tutorials.ws/combination/comb_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Encoder, Decoder und Adressauswahl](https://www.learnabout-electronics.org/Digital/dig44.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Decoder, Multiplexer und Addierer](https://learn.adafruit.com/combinational-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Multiplexer und Decoder aus Gattern](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Ergänzte Lehrschaltung: Kanalzahl, Taktflanke, Freigaben und aktive Pegel mit dem konkreten IC abgleichen.

## SN74LS147N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Tastencodierung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-9/encoder/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Prioritätsencoder und Eingangscodierung](https://www.electronics-tutorials.ws/combination/comb_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Encoder, Decoder und Adressauswahl](https://www.learnabout-electronics.org/Digital/dig44.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Decoder, Multiplexer und Addierer](https://learn.adafruit.com/combinational-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Multiplexer und Decoder aus Gattern](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Ergänzte Lehrschaltung: Kanalzahl, Taktflanke, Freigaben und aktive Pegel mit dem konkreten IC abgleichen.

## SN74LS148N

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Encoder-Kaskadierung (TI) (PDF S. 13)](../Datenblaetter/SN7xxx/SN74LS148N_TI.pdf#page=13) · [Online-Original](https://www.ti.com/lit/ds/symlink/sn74ls148.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Tastencodierung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-9/encoder/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Prioritätsencoder und Eingangscodierung](https://www.electronics-tutorials.ws/combination/comb_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Encoder, Decoder und Adressauswahl](https://www.learnabout-electronics.org/Digital/dig44.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Decoder, Multiplexer und Addierer](https://learn.adafruit.com/combinational-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Multiplexer und Decoder aus Gattern](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Ergänzte Lehrschaltung: Kanalzahl, Taktflanke, Freigaben und aktive Pegel mit dem konkreten IC abgleichen.

## SN74LS151N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Datenauswahl (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-9/multiplexers/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Signalauswahl mit Multiplexern](https://www.electronics-tutorials.ws/combination/comb_2.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Datenauswahl und Multiplexer](https://www.learnabout-electronics.org/Digital/dig42.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Decoder, Multiplexer und Addierer](https://learn.adafruit.com/combinational-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Multiplexer und Decoder aus Gattern](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Ergänzte Lehrschaltung: Kanalzahl, Taktflanke, Freigaben und aktive Pegel mit dem konkreten IC abgleichen.

## SN74LS153N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Datenauswahl (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-9/multiplexers/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Signalauswahl mit Multiplexern](https://www.electronics-tutorials.ws/combination/comb_2.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Datenauswahl und Multiplexer](https://www.learnabout-electronics.org/Digital/dig42.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Decoder, Multiplexer und Addierer](https://learn.adafruit.com/combinational-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Multiplexer und Decoder aus Gattern](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Ergänzte Lehrschaltung: Kanalzahl, Taktflanke, Freigaben und aktive Pegel mit dem konkreten IC abgleichen.

## SN74LS155N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Adress-/Leitungsdecoder (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-9/decoder/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Signalverteilung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-9/demultiplexers/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Binärdecoder und Leitungsauswahl](https://www.electronics-tutorials.ws/combination/comb_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Encoder, Decoder und Adressauswahl](https://www.learnabout-electronics.org/Digital/dig44.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Decoder, Multiplexer und Addierer](https://learn.adafruit.com/combinational-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Multiplexer und Decoder aus Gattern](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Ergänzte Lehrschaltung: Kanalzahl, Taktflanke, Freigaben und aktive Pegel mit dem konkreten IC abgleichen.

## SN74LS156N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Adress-/Leitungsdecoder (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-9/decoder/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Signalverteilung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-9/demultiplexers/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Binärdecoder und Leitungsauswahl](https://www.electronics-tutorials.ws/combination/comb_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Encoder, Decoder und Adressauswahl](https://www.learnabout-electronics.org/Digital/dig44.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Decoder, Multiplexer und Addierer](https://learn.adafruit.com/combinational-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Multiplexer und Decoder aus Gattern](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Ergänzte Lehrschaltung: Kanalzahl, Taktflanke, Freigaben und aktive Pegel mit dem konkreten IC abgleichen.

## SN74LS157N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Datenauswahl (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-9/multiplexers/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Signalauswahl mit Multiplexern](https://www.electronics-tutorials.ws/combination/comb_2.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Datenauswahl und Multiplexer](https://www.learnabout-electronics.org/Digital/dig42.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Decoder, Multiplexer und Addierer](https://learn.adafruit.com/combinational-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Multiplexer und Decoder aus Gattern](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Ergänzte Lehrschaltung: Kanalzahl, Taktflanke, Freigaben und aktive Pegel mit dem konkreten IC abgleichen.

## SN74LS160N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zähler kaskadieren (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/synchronous-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Modulo-/Frequenzteiler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/counter-modulus/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## SN74LS161N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zähler kaskadieren (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/synchronous-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Modulo-/Frequenzteiler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/counter-modulus/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## SN74LS162N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zähler kaskadieren (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/synchronous-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Modulo-/Frequenzteiler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/counter-modulus/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## SN74LS163N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zähler kaskadieren (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/synchronous-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Modulo-/Frequenzteiler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/counter-modulus/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## SN74LS164N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [LED-Ausgänge erweitern (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-12/serial-in-parallel-out-shift-register/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Serielle und parallele Schieberegister](https://www.electronics-tutorials.ws/sequential/seq_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## CD74HC165E

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Taster seriell einlesen (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-12/parallel-in-serial-out-shift-register/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Serielle und parallele Schieberegister](https://www.electronics-tutorials.ws/sequential/seq_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## SN74LS165N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Taster seriell einlesen (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-12/parallel-in-serial-out-shift-register/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Serielle und parallele Schieberegister](https://www.electronics-tutorials.ws/sequential/seq_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## 74166

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Taster seriell einlesen (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-12/parallel-in-serial-out-shift-register/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Serielle und parallele Schieberegister](https://www.electronics-tutorials.ws/sequential/seq_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## 74174N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [D-Flipflop (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-10/edge-triggered-latches-flip-flops/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Registeraufbau (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-12/parallel-in-parallel-out-universal-shift-register/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Serielle und parallele Schieberegister](https://www.electronics-tutorials.ws/sequential/seq_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [D-Flipflop als Speicher und Teiler](https://www.electronics-tutorials.ws/sequential/seq_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## PC74HCT174P

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [D-Flipflop (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-10/edge-triggered-latches-flip-flops/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Registeraufbau (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-12/parallel-in-parallel-out-universal-shift-register/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Serielle und parallele Schieberegister](https://www.electronics-tutorials.ws/sequential/seq_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [D-Flipflop als Speicher und Teiler](https://www.electronics-tutorials.ws/sequential/seq_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## SN74LS174N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [D-Flipflop (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-10/edge-triggered-latches-flip-flops/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Registeraufbau (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-12/parallel-in-parallel-out-universal-shift-register/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Serielle und parallele Schieberegister](https://www.electronics-tutorials.ws/sequential/seq_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [D-Flipflop als Speicher und Teiler](https://www.electronics-tutorials.ws/sequential/seq_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## SN74LS175N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [D-Flipflop (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-10/edge-triggered-latches-flip-flops/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Registeraufbau (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-12/parallel-in-parallel-out-universal-shift-register/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Serielle und parallele Schieberegister](https://www.electronics-tutorials.ws/sequential/seq_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [D-Flipflop als Speicher und Teiler](https://www.electronics-tutorials.ws/sequential/seq_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## SN74LS190N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zähler kaskadieren (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/synchronous-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Modulo-/Frequenzteiler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/counter-modulus/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## SN74LS191N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zähler kaskadieren (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/synchronous-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Modulo-/Frequenzteiler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/counter-modulus/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## SN74LS192N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zähler kaskadieren (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/synchronous-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Modulo-/Frequenzteiler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/counter-modulus/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## SN74LS193N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zähler kaskadieren (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/synchronous-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Modulo-/Frequenzteiler (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-11/counter-modulus/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## SN74LS194N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Paralleles Laden/Schieben (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-12/parallel-in-parallel-out-universal-shift-register/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Serielle und parallele Schieberegister](https://www.electronics-tutorials.ws/sequential/seq_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## 74240

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [74244/74245 als Buspuffer](https://learn.adafruit.com/digital-circuits-6-eprom-emulator/the-74244-octal-tristate-buffer) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Praktischer Versuch mit bidirektionalem 74LS245](https://electronique-et-informatique.fr/anglais/Digit/Pratique/Digit_12PS.php) — electronique-et-informatique.fr; Grundschaltung; geprüft 2026-10-25.
- [Geteilte Datenleitung mit Tri-State-Puffern](https://www.cs.emory.edu/~cheung/Courses/355/Syllabus/3-memory/tri-state.html) — cs.emory.edu; Simulationsbeispiel; geprüft 2026-10-25.
- [Puffer mit Freigabe und Tri-State-Bus](https://www.electronics-tutorials.ws/logic/logic_9.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Ausgangsstufen, Busfreigabe und Logikpegel](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Funktionsreferenz; geprüft 2026-10-25.
- [74LS245 als Buspuffer in einer 8255-Schnittstelle](https://tiij.org/issues/issues/4_1/4_1s.html) — tiij.org; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Tri-State-Grundschaltung mit 74244/74245 als Referenz. Invertierende Typen liefern umgekehrte Daten; Richtung und aktive Freigabe des tatsächlichen Typs prüfen. Keine Open-Collector-Verdrahtung annehmen.

## SN74LS244N

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Buspuffer (TI) (PDF S. 14)](../Datenblaetter/SN7xxx/SN74LS244N_TI.pdf#page=14) · [Online-Original](https://www.ti.com/lit/ds/symlink/sn74ls244.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [74244/74245 als Buspuffer](https://learn.adafruit.com/digital-circuits-6-eprom-emulator/the-74244-octal-tristate-buffer) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Praktischer Versuch mit bidirektionalem 74LS245](https://electronique-et-informatique.fr/anglais/Digit/Pratique/Digit_12PS.php) — electronique-et-informatique.fr; Grundschaltung; geprüft 2026-10-25.
- [Geteilte Datenleitung mit Tri-State-Puffern](https://www.cs.emory.edu/~cheung/Courses/355/Syllabus/3-memory/tri-state.html) — cs.emory.edu; Simulationsbeispiel; geprüft 2026-10-25.
- [Puffer mit Freigabe und Tri-State-Bus](https://www.electronics-tutorials.ws/logic/logic_9.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Ausgangsstufen, Busfreigabe und Logikpegel](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Funktionsreferenz; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Tri-State-Grundschaltung mit 74244/74245 als Referenz. Invertierende Typen liefern umgekehrte Daten; Richtung und aktive Freigabe des tatsächlichen Typs prüfen. Keine Open-Collector-Verdrahtung annehmen.

## SN74LS245N

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Bidirektionaler Bus (TI) (PDF S. 10)](../Datenblaetter/SN7xxx/SN74LS245N_TI.pdf#page=10) · [Online-Original](https://www.ti.com/lit/ds/symlink/sn74ls245.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [74244/74245 als Buspuffer](https://learn.adafruit.com/digital-circuits-6-eprom-emulator/the-74244-octal-tristate-buffer) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Praktischer Versuch mit bidirektionalem 74LS245](https://electronique-et-informatique.fr/anglais/Digit/Pratique/Digit_12PS.php) — electronique-et-informatique.fr; Grundschaltung; geprüft 2026-10-25.
- [Geteilte Datenleitung mit Tri-State-Puffern](https://www.cs.emory.edu/~cheung/Courses/355/Syllabus/3-memory/tri-state.html) — cs.emory.edu; Simulationsbeispiel; geprüft 2026-10-25.
- [Puffer mit Freigabe und Tri-State-Bus](https://www.electronics-tutorials.ws/logic/logic_9.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Ausgangsstufen, Busfreigabe und Logikpegel](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Funktionsreferenz; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Tri-State-Grundschaltung mit 74244/74245 als Referenz. Invertierende Typen liefern umgekehrte Daten; Richtung und aktive Freigabe des tatsächlichen Typs prüfen. Keine Open-Collector-Verdrahtung annehmen.

## SN74LS247N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [7-Segment-Anzeige (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/7-segment-display/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [BCD-Eingabe mit CD4511 und 7-Segment-Anzeige](https://circuitdigest.com/electronic-circuits/7-segment-display-driver-using-ic-cd4511) — circuitdigest.com; Grundschaltung; geprüft 2026-10-25.
- [CD4511-Anzeige auf dem Steckbrett](https://www.circuits-diy.com/how-to-drive-a-7-segment-display-using-bcd-driver-ic-cd4511) — circuits-diy.com; Grundschaltung; geprüft 2026-10-25.
- [Zweistelliger Zähler mit CD4026](https://www.eleccircuit.com/simple-two-digits-counter-using-cd4026/) — eleccircuit.com; Grundschaltung; geprüft 2026-10-25.
- [BCD-Decoder und 7-Segment-Zähler](https://www.electronics-tutorials.ws/counter/7-segment-display.html) — electronics-tutorials.ws; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.

Grundschaltung mit 4511: Segmentwiderstände, gemeinsame Anode/Kathode, Ausgangspolarität und Pinfolge an den vorhandenen Treiber anpassen. Anzeige-Grundschaltungen mit anderen ICs: BCD-Decoder und Zähler nicht verwechseln. Anzeigeart (gemeinsame Anode/Kathode bzw. LCD), aktive Ausgangspegel, Segmentwiderstände und Multiplexsteuerung passend zum Typ wählen. Insbesondere CD4543 kann LCD-Phasenansteuerung verwenden; eine LED-Schaltung ist dafür keine direkte Vorlage.

## SN74LS248N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [7-Segment-Anzeige (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/7-segment-display/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [BCD-Eingabe mit CD4511 und 7-Segment-Anzeige](https://circuitdigest.com/electronic-circuits/7-segment-display-driver-using-ic-cd4511) — circuitdigest.com; Grundschaltung; geprüft 2026-10-25.
- [CD4511-Anzeige auf dem Steckbrett](https://www.circuits-diy.com/how-to-drive-a-7-segment-display-using-bcd-driver-ic-cd4511) — circuits-diy.com; Grundschaltung; geprüft 2026-10-25.
- [Zweistelliger Zähler mit CD4026](https://www.eleccircuit.com/simple-two-digits-counter-using-cd4026/) — eleccircuit.com; Grundschaltung; geprüft 2026-10-25.
- [BCD-Decoder und 7-Segment-Zähler](https://www.electronics-tutorials.ws/counter/7-segment-display.html) — electronics-tutorials.ws; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.

Grundschaltung mit 4511: Segmentwiderstände, gemeinsame Anode/Kathode, Ausgangspolarität und Pinfolge an den vorhandenen Treiber anpassen. Anzeige-Grundschaltungen mit anderen ICs: BCD-Decoder und Zähler nicht verwechseln. Anzeigeart (gemeinsame Anode/Kathode bzw. LCD), aktive Ausgangspegel, Segmentwiderstände und Multiplexsteuerung passend zum Typ wählen. Insbesondere CD4543 kann LCD-Phasenansteuerung verwenden; eine LED-Schaltung ist dafür keine direkte Vorlage.

## 74253

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Datenauswahl (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-9/multiplexers/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Signalauswahl mit Multiplexern](https://www.electronics-tutorials.ws/combination/comb_2.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Datenauswahl und Multiplexer](https://www.learnabout-electronics.org/Digital/dig42.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Decoder, Multiplexer und Addierer](https://learn.adafruit.com/combinational-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Multiplexer und Decoder aus Gattern](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Ergänzte Lehrschaltung: Kanalzahl, Taktflanke, Freigaben und aktive Pegel mit dem konkreten IC abgleichen.

## SN74LS266N

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Open-Collector-Ansteuerung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-3/special-output-gates/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Open-Collector-Schalter und Pull-up-Auslegung](https://cfi.iitm.ac.in/elec-club/articles/pages/Basics/PullUp-Down%20Resistors.html) — cfi.iitm.ac.in; Grundschaltung; geprüft 2026-10-25.
- [Open-Collector-Verknüpfung und Busbeispiele](https://nucleus.iaea.org/sites/nuclear-instrumentation/Shared%20Documents/Digital%20Electronics/DigitalText.pdf) — nucleus.iaea.org; Grundschaltung; geprüft 2026-10-25.
- [Open-Collector-Lastschalter und Pegelanpassung](https://www.electronics-tutorials.ws/transistor/open-collector-outputs.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Ausgangsstufen, Busfreigabe und Logikpegel](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Funktionsreferenz; geprüft 2026-10-25.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Open-Collector-Grundschaltung: zulässige Ausgangsspannung und Senkstrom typbezogen prüfen; Logikfunktion (Inverter, NAND, XNOR) bleibt die des vorhandenen ICs. Die Transistorschalter-Quelle zeigt die externe Lastbeschaltung einer Senkstufe; sie ersetzt nicht die Logikfunktion des ICs.

## SN74LS273N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [D-Flipflop (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-10/edge-triggered-latches-flip-flops/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Registeraufbau (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-12/parallel-in-parallel-out-universal-shift-register/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Serielle und parallele Schieberegister](https://www.electronics-tutorials.ws/sequential/seq_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [D-Flipflop als Speicher und Teiler](https://www.electronics-tutorials.ws/sequential/seq_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## 74LS279

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Setzen/Rücksetzen (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/nor-gate-s-r-latch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [D-Flipflop als Speicher und Teiler](https://www.electronics-tutorials.ws/sequential/seq_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei NAND-RS-Latches aktive Low-Eingänge und Ausgangsfreigaben abgleichen; NOR-Beispiel zeigt das Speicherprinzip. RS-Speicherprinzip: 74LS279 mit aktiven Low-Eingängen und CD4043 mit anderen Freigaben nicht wie ein D-Flipflop beschalten. D-Flipflop-Link erläutert nur den Unterschied der Speicherarten.

## SN74LS373N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Daten zwischenspeichern (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-10/d-latch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [D-Flipflop als Speicher und Teiler](https://www.electronics-tutorials.ws/sequential/seq_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## SN74LS374N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [D-Flipflop (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-10/edge-triggered-latches-flip-flops/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Registeraufbau (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-12/parallel-in-parallel-out-universal-shift-register/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Serielle und parallele Schieberegister](https://www.electronics-tutorials.ws/sequential/seq_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [D-Flipflop als Speicher und Teiler](https://www.electronics-tutorials.ws/sequential/seq_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## 74541

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [74244/74245 als Buspuffer](https://learn.adafruit.com/digital-circuits-6-eprom-emulator/the-74244-octal-tristate-buffer) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Praktischer Versuch mit bidirektionalem 74LS245](https://electronique-et-informatique.fr/anglais/Digit/Pratique/Digit_12PS.php) — electronique-et-informatique.fr; Grundschaltung; geprüft 2026-10-25.
- [Geteilte Datenleitung mit Tri-State-Puffern](https://www.cs.emory.edu/~cheung/Courses/355/Syllabus/3-memory/tri-state.html) — cs.emory.edu; Simulationsbeispiel; geprüft 2026-10-25.
- [Puffer mit Freigabe und Tri-State-Bus](https://www.electronics-tutorials.ws/logic/logic_9.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Ausgangsstufen, Busfreigabe und Logikpegel](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Funktionsreferenz; geprüft 2026-10-25.
- [74LS245 als Buspuffer in einer 8255-Schnittstelle](https://tiij.org/issues/issues/4_1/4_1s.html) — tiij.org; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Tri-State-Grundschaltung mit 74244/74245 als Referenz. Invertierende Typen liefern umgekehrte Daten; Richtung und aktive Freigabe des tatsächlichen Typs prüfen. Keine Open-Collector-Verdrahtung annehmen.

## 74576

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [D-Flipflop (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-10/edge-triggered-latches-flip-flops/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Registeraufbau (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-12/parallel-in-parallel-out-universal-shift-register/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Serielle und parallele Schieberegister](https://www.electronics-tutorials.ws/sequential/seq_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [D-Flipflop als Speicher und Teiler](https://www.electronics-tutorials.ws/sequential/seq_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## 74640

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [74244/74245 als Buspuffer](https://learn.adafruit.com/digital-circuits-6-eprom-emulator/the-74244-octal-tristate-buffer) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Praktischer Versuch mit bidirektionalem 74LS245](https://electronique-et-informatique.fr/anglais/Digit/Pratique/Digit_12PS.php) — electronique-et-informatique.fr; Grundschaltung; geprüft 2026-10-25.
- [Geteilte Datenleitung mit Tri-State-Puffern](https://www.cs.emory.edu/~cheung/Courses/355/Syllabus/3-memory/tri-state.html) — cs.emory.edu; Simulationsbeispiel; geprüft 2026-10-25.
- [Puffer mit Freigabe und Tri-State-Bus](https://www.electronics-tutorials.ws/logic/logic_9.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Ausgangsstufen, Busfreigabe und Logikpegel](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Funktionsreferenz; geprüft 2026-10-25.
- [74LS245 als Buspuffer in einer 8255-Schnittstelle](https://tiij.org/issues/issues/4_1/4_1s.html) — tiij.org; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Tri-State-Grundschaltung mit 74244/74245 als Referenz. Invertierende Typen liefern umgekehrte Daten; Richtung und aktive Freigabe des tatsächlichen Typs prüfen. Keine Open-Collector-Verdrahtung annehmen.

## 74641

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [74244/74245 als Buspuffer](https://learn.adafruit.com/digital-circuits-6-eprom-emulator/the-74244-octal-tristate-buffer) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Praktischer Versuch mit bidirektionalem 74LS245](https://electronique-et-informatique.fr/anglais/Digit/Pratique/Digit_12PS.php) — electronique-et-informatique.fr; Grundschaltung; geprüft 2026-10-25.
- [Geteilte Datenleitung mit Tri-State-Puffern](https://www.cs.emory.edu/~cheung/Courses/355/Syllabus/3-memory/tri-state.html) — cs.emory.edu; Simulationsbeispiel; geprüft 2026-10-25.
- [Puffer mit Freigabe und Tri-State-Bus](https://www.electronics-tutorials.ws/logic/logic_9.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Ausgangsstufen, Busfreigabe und Logikpegel](https://www.renesas.com/us/en/support/engineer-school/digital-circuits-02-digital-ics-combinational-logic) — renesas.com; Funktionsreferenz; geprüft 2026-10-25.
- [74LS245 als Buspuffer in einer 8255-Schnittstelle](https://tiij.org/issues/issues/4_1/4_1s.html) — tiij.org; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Tri-State-Grundschaltung mit 74244/74245 als Referenz. Invertierende Typen liefern umgekehrte Daten; Richtung und aktive Freigabe des tatsächlichen Typs prüfen. Keine Open-Collector-Verdrahtung annehmen.

## SN74HC595

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Schieberegister-Anwendung (TI) (PDF S. 13)](../Datenblaetter/SN7xxx/SN74HC595_TI.pdf#page=13) · [Online-Original](https://www.ti.com/lit/ds/symlink/sn74hc595.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Seriell nach parallel (Grundschaltung)](https://www.allaboutcircuits.com/textbook/digital/chpt-12/serial-in-parallel-out-shift-register/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Acht LEDs mit Arduino und 74HC595](https://learn.adafruit.com/adafruit-arduino-lesson-4-eight-leds/overview) — adafruit.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Serielle und parallele Schieberegister](https://www.electronics-tutorials.ws/sequential/seq_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Sequenzielle Grundschaltung: Speichertyp, Taktflanke, Reset/Set und Lade-/Freigabesignale des vorhandenen ICs beachten.

## CD74HCT85E

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [4-Bit-Vergleich/Kaskadierung (Grundschaltung)](https://www.electronics-tutorials.ws/combination/comb_8.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Binärvergleich und kaskadierte Komparatoren](https://www.learnabout-electronics.org/Digital/dig43.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [7485: 4-/8-Bit-Vergleich im virtuellen Labor](https://dec-iitkgp.vlabs.ac.in/exp/digital-comparators/theory.html) — dec-iitkgp.vlabs.ac.in; Grundschaltung; geprüft 2026-10-25.
- [7485 mit Schaltern und Ergebnisanzeige](https://faculty-web.msoe.edu/tritt/JohnDeere/jddig02.html) — faculty-web.msoe.edu; Grundschaltung; geprüft 2026-10-25.
- [7485-Kaskadierung zum 24-Bit-Vergleicher](https://tams.informatik.uni-hamburg.de/applets/hades/webdemos/20-arithmetic/45-compare/7485-demo_print.html) — tams.informatik.uni-hamburg.de; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. 7485-Beispiele zeigen das Vergleichsprinzip. CD4063 und HCT85 unterscheiden sich in Pinfolge und elektrischen Kennwerten; Kaskadiereingänge typgerecht setzen.

## PC74HCT08P

**6/5 Beispiel-Websites**, 7 Quellen-Websites insgesamt. Ziel erreicht.

- [Gatter mit Tastern/LED (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-7/basic-gate-function/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gatter kombinieren und Eingangszahl anpassen](https://electronicsclub.info/gates.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Logikgatter und 74er-Funktionen](https://www.learnabout-electronics.org/Digital/dig21.php) — learnabout-electronics.org; Funktionsreferenz; geprüft 2026-10-25.
- [Logikverknüpfungen und praktischer Gatterversuch](https://learn.adafruit.com/binary-boolean-and-logic?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen mit NAND und NOR](https://www.electronics-tutorials.ws/logic/universal-gates.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbauten: NOR, NAND, XOR und AND-OR-INVERT](https://people.utm.my/nelidya/wp-content/uploads/sites/1001/2018/11/MergedFile_Digital-Lab.pdf) — people.utm.my; Grundschaltung; geprüft 2026-10-25.
- [Gatterverknüpfungen im virtuellen Labor](https://de-iitr.vlabs.ac.in/exp/truth-table-gates/theory.html) — de-iitr.vlabs.ac.in; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. Es handelt sich um Logikprinzipien; eine gezeigte Verknüpfung kann zusätzliche Gatter benötigen. Eingangszahl und invertierte Ausgänge abgleichen.

## SN74LS688N

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Freigabe / Gleichheitsvergleich (Funktionstabelle, TI) (PDF S. 2)](../Datenblaetter/SN7xxx/SN74LS688N_TI.pdf#page=2) · [Online-Original](https://www.ti.com/lit/ds/symlink/sn74ls688.pdf) — ti.com; Funktionstabelle / Referenz; geprüft 2026-10-23.
- [74LS688 zur Byteprüfung in einem EPROM-Kopierer](https://github.com/yoyoberenguer/EPROM) — github.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [74LS688 zur Adressauswahl einer TI-99-IDE-Karte](https://www.unige.ch/medecine/nouspikel/ti99/ide.htm) — unige.ch; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [Speicheradressierung mit 8-Bit-Gleichheitskomparator](https://courses.minia.edu.eg/Attach/993412-%20Memory.pdf) — courses.minia.edu.eg; Grundschaltung; geprüft 2026-10-25.
- [74HC688 als Gleichheitsprüfer und Adressdecoder](https://nucleus.iaea.org/sites/nuclear-instrumentation/Shared%20Documents/Digital%20Electronics/DigitalText.pdf) — nucleus.iaea.org; Grundschaltung; geprüft 2026-10-25.
- [74LS245 als Buspuffer in einer 8255-Schnittstelle](https://tiij.org/issues/issues/4_1/4_1s.html) — tiij.org; Grundschaltung; geprüft 2026-10-25.

TI-Funktionstabelle als Referenz, keine Anwendungsschaltung. /G=0 aktiviert, /EQ=0 bedeutet P=Q; Push-Pull-Ausgang. Gleichheitskomparator mit aktivem Low-Ergebnis; LS688 führt keinen Größer-/Kleiner-Vergleich aus. Die HC688-Grundschaltung erfordert einen Abgleich der Logikpegel.

## SN74HCT165N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Parallel einlesen, seriell ausgeben](https://www.allaboutcircuits.com/textbook/digital/chpt-12/parallel-in-serial-out-shift-register/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Serielle und parallele Schieberegister](https://www.electronics-tutorials.ws/sequential/seq_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Übertragbares Logikprinzip. Den konkreten Funktionsumfang und die Pinbelegung dieses Typs aus seinem Datenblatt übernehmen.

## SN74LS195N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Register laden und schieben](https://www.allaboutcircuits.com/textbook/digital/chpt-12/parallel-in-parallel-out-universal-shift-register/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Serielle und parallele Schieberegister](https://www.electronics-tutorials.ws/sequential/seq_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Übertragbares Logikprinzip. Den konkreten Funktionsumfang und die Pinbelegung dieses Typs aus seinem Datenblatt übernehmen.

## SN74LS290N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zählerschaltung als Grundprinzip](https://www.allaboutcircuits.com/textbook/digital/chpt-11/asynchronous-counters/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Asynchroner Binärzähler und Taktteilung](https://www.electronics-tutorials.ws/counter/count_1.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Übertragbares Logikprinzip. Den konkreten Funktionsumfang und die Pinbelegung dieses Typs aus seinem Datenblatt übernehmen.

## SN74LS574N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Getakteter D-Speicher](https://www.allaboutcircuits.com/textbook/digital/chpt-10/edge-triggered-latches-flip-flops/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Simulationsschaltungen: Flipflops, Zähler und Register](https://www.learnabout-electronics.org/Digital/dig510extra.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Flipflops, Schieberegister und Zählerschaltungen](https://learn.adafruit.com/digital-circuits-4-sequential-circuits?view=all) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
- [Speicher, D-Flipflops und Taktteilung](https://www.renesas.com/en/support/engineer-school/digital-circuits-03-sequential-logic) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [Serielle und parallele Schieberegister](https://www.electronics-tutorials.ws/sequential/seq_5.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Übertragbares Logikprinzip. Den konkreten Funktionsumfang und die Pinbelegung dieses Typs aus seinem Datenblatt übernehmen.
