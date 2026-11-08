# Beispielschaltungen pro Bauteil

[Übersicht](README.md) · [Gesamtsammlung](Beispielschaltungen.md) · [Recherchebedarf](Recherchebedarf.md) · [Bestand](../Bauteile.md)

320 Bauteile, 1876 Linkzuordnungen. Erweiterungsstand: **25.10.2026**; Prüfdatum jeweils am Link.

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

## 2N2222

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## 2N3904

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## 2N3906

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## 2N5401

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## 2N5551

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## 2SA1015

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## 2SB772

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## 2SC1815

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## 2SC945

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## 2SD882

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC327

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC337

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC517

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Darlington-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC546

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC547

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC548

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC549

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC550

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC556

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC557

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC558

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BD139

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BD140

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## MPQ2222A

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Stromspiegel (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/current-mirror/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## S8050

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## S8550

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## S9012

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## S9013

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## S9014

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## S9015

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## S9018

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## TIP120

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Darlington-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## TIP121

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Darlington-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## TIP122

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Darlington-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## TIP125

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## TIP126

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## TIP127

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## TIP31C

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## TIP32C

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## TIP41C

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## TIP42C

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## IRF540

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [N-Kanal-Lastschalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [MOSFET-Schalter mit isoliertem Eingang](https://learnabout-electronics.org/Semiconductors/fet_06a.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
  Hinweis: N-Kanal-Beispiel; für P-Kanal ist eine andere Topologie und Gatepolarität nötig.
- [Magnetspule mit N-Kanal-Logic-Level-MOSFET](https://learn.adafruit.com/circuitpython-ble-remote-control-on-off/solenoid-mosfet) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
  Hinweis: Beispiel verwendet IRLB8721. Andere MOSFETs benötigen gegebenenfalls eine höhere Gate-Spannung.
- [PWM-Lastschalter mit N-Kanal-MOSFET-Modul](https://learn.sparkfun.com/tutorials/fading-with-the-mosfet-power-switch-and-buck-regulator/all) — sparkfun.com; Modulbeispiel; geprüft 2026-10-25.
  Hinweis: Low-Side-Modul mit anderem MOSFET; kein Ersatz für die Gate-Auslegung des vorhandenen Typs.

Erforderliche Gate-Spannung aus RDS(on)-Spezifikation bestimmen; IRF540/IRFZ44 nicht als Logic-Level-Typen behandeln. Polarität und Pinout des konkreten MOSFETs berücksichtigen. Grundschaltungen verwenden teils andere MOSFETs. IRF-Typen nicht allein wegen der Schwellspannung als bei 5 V voll durchgesteuert ansehen; RDS(on) bei der tatsächlich verfügbaren Gatespannung prüfen. N-Kanal-Beispiele sind keine direkte Beschaltung für P-Kanal-Typen.

## IRF9530

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [P-Kanal-High-Side (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [MOSFET-Schalter mit isoliertem Eingang](https://learnabout-electronics.org/Semiconductors/fet_06a.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
  Hinweis: Den Abschnitt „The High Side MOSFET Switch“ und die P-Kanal-Schaltung verwenden.
- [P-Kanal-High-Side-Schalter mit Schaltplan](https://thewanderingengineer.com/2016/11/14/p-channel-mosfet-high-side-switch/) — thewanderingengineer.com; Grundschaltung; geprüft 2026-10-25.
- [P-Kanal-Lastschalter mit vorgeschalteter Gate-Ansteuerung](https://developer.wildernesslabs.co/Hardware/Tutorials/Electronics/Part7/MOSFET_High-Side_Usage/) — developer.wildernesslabs.co; Grundschaltung; geprüft 2026-10-25.
- [P-Kanal-Lastschalter und High-Side-Beschaltung](https://fscdn.rohm.com/en/products/databook/applinote/discrete/transistor/mosfet/p-channel_power_mosfets_selection_guide_an-e.pdf) — fscdn.rohm.com; Hersteller-Grundschaltung; geprüft 2026-10-25.

P-Kanal-MOSFET: Source an die positive Versorgung; die Gatespannung wird relativ zu Source betrachtet. VGS-Grenze, erforderliche negative Gate-Ansteuerung und RDS(on) des konkreten Typs beachten. Quellen verwenden teilweise andere P-Kanal-Typen; keine unveränderte N-Kanal-Beschaltung übernehmen.

## IRFZ44

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [N-Kanal-Lastschalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [MOSFET-Schalter mit isoliertem Eingang](https://learnabout-electronics.org/Semiconductors/fet_06a.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
  Hinweis: N-Kanal-Beispiel; für P-Kanal ist eine andere Topologie und Gatepolarität nötig.
- [Magnetspule mit N-Kanal-Logic-Level-MOSFET](https://learn.adafruit.com/circuitpython-ble-remote-control-on-off/solenoid-mosfet) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
  Hinweis: Beispiel verwendet IRLB8721. Andere MOSFETs benötigen gegebenenfalls eine höhere Gate-Spannung.
- [PWM-Lastschalter mit N-Kanal-MOSFET-Modul](https://learn.sparkfun.com/tutorials/fading-with-the-mosfet-power-switch-and-buck-regulator/all) — sparkfun.com; Modulbeispiel; geprüft 2026-10-25.
  Hinweis: Low-Side-Modul mit anderem MOSFET; kein Ersatz für die Gate-Auslegung des vorhandenen Typs.

Erforderliche Gate-Spannung aus RDS(on)-Spezifikation bestimmen; IRF540/IRFZ44 nicht als Logic-Level-Typen behandeln. Polarität und Pinout des konkreten MOSFETs berücksichtigen. Grundschaltungen verwenden teils andere MOSFETs. IRF-Typen nicht allein wegen der Schwellspannung als bei 5 V voll durchgesteuert ansehen; RDS(on) bei der tatsächlich verfügbaren Gatespannung prüfen. N-Kanal-Beispiele sind keine direkte Beschaltung für P-Kanal-Typen.

## IRLZ44N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [N-Kanal-Lastschalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [MOSFET-Schalter mit isoliertem Eingang](https://learnabout-electronics.org/Semiconductors/fet_06a.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
  Hinweis: N-Kanal-Beispiel; für P-Kanal ist eine andere Topologie und Gatepolarität nötig.
- [Magnetspule mit N-Kanal-Logic-Level-MOSFET](https://learn.adafruit.com/circuitpython-ble-remote-control-on-off/solenoid-mosfet) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
  Hinweis: Beispiel verwendet IRLB8721. Andere MOSFETs benötigen gegebenenfalls eine höhere Gate-Spannung.
- [PWM-Lastschalter mit N-Kanal-MOSFET-Modul](https://learn.sparkfun.com/tutorials/fading-with-the-mosfet-power-switch-and-buck-regulator/all) — sparkfun.com; Modulbeispiel; geprüft 2026-10-25.
  Hinweis: Low-Side-Modul mit anderem MOSFET; kein Ersatz für die Gate-Auslegung des vorhandenen Typs.

Erforderliche Gate-Spannung aus RDS(on)-Spezifikation bestimmen; IRF540/IRFZ44 nicht als Logic-Level-Typen behandeln. Polarität und Pinout des konkreten MOSFETs berücksichtigen. Grundschaltungen verwenden teils andere MOSFETs. IRF-Typen nicht allein wegen der Schwellspannung als bei 5 V voll durchgesteuert ansehen; RDS(on) bei der tatsächlich verfügbaren Gatespannung prüfen. N-Kanal-Beispiele sind keine direkte Beschaltung für P-Kanal-Typen.

## BT134-600E

**4/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Weitere passende Beispiele gesucht.

- [TRIAC-Phasensteuerung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/semiconductors/chpt-7/the-triac/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [TRIAC-Schalter und Phasenanschnitt](https://www.electronics-tutorials.ws/power/triac.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [DIAC-TRIAC-Dimmer und Triggerung](https://learnabout-electronics.org/Semiconductors/thyristors_64.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [AN5114: TRIAC mit Optotriac ansteuern](https://www.st.com.cn/resource/en/application_note/an5114-controlling-a-triac-with-a-phototriac-stmicroelectronics.pdf) — st.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
- [AN-9745: TRIAC-Dimmer und LED-Lasten](https://www.onsemi.jp/download/application-notes/pdf/an-9745.pdf) — onsemi.com; Entwurfshilfe; geprüft 2026-10-25.

Schaltungsprinzip; Gate-Empfindlichkeit, Haltestrom und Spannungsfestigkeit des konkreten TRIACs abgleichen. Netzspannungsbeispiel. TRIAC-Grundschaltungen: Triggerquadranten, Gate-, Halte- und Einraststrom sowie Laststrom für den Typ prüfen; ein MAC97 ersetzt keinen Leistungs-TRIAC. Verlinkte Netzspannungsschaltungen sind keine Steckbrettaufbauten.

**Recherchebedarf:** Bisher sind weniger als fünf unterschiedliche Websites mit passenden Beispielen belegt. Die vorhandenen Grundschaltungen und Referenzen sind oben gekennzeichnet; es wurden keine zusätzlichen Beschaltungen erfunden.

## BTA06

**4/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Weitere passende Beispiele gesucht.

- [TRIAC-Phasensteuerung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/semiconductors/chpt-7/the-triac/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [TRIAC-Schalter und Phasenanschnitt](https://www.electronics-tutorials.ws/power/triac.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [DIAC-TRIAC-Dimmer und Triggerung](https://learnabout-electronics.org/Semiconductors/thyristors_64.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [AN5114: TRIAC mit Optotriac ansteuern](https://www.st.com.cn/resource/en/application_note/an5114-controlling-a-triac-with-a-phototriac-stmicroelectronics.pdf) — st.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
- [AN-9745: TRIAC-Dimmer und LED-Lasten](https://www.onsemi.jp/download/application-notes/pdf/an-9745.pdf) — onsemi.com; Entwurfshilfe; geprüft 2026-10-25.

Schaltungsprinzip; Gate-Empfindlichkeit, Haltestrom und Spannungsfestigkeit des konkreten TRIACs abgleichen. Netzspannungsbeispiel. TRIAC-Grundschaltungen: Triggerquadranten, Gate-, Halte- und Einraststrom sowie Laststrom für den Typ prüfen; ein MAC97 ersetzt keinen Leistungs-TRIAC. Verlinkte Netzspannungsschaltungen sind keine Steckbrettaufbauten.

**Recherchebedarf:** Bisher sind weniger als fünf unterschiedliche Websites mit passenden Beispielen belegt. Die vorhandenen Grundschaltungen und Referenzen sind oben gekennzeichnet; es wurden keine zusätzlichen Beschaltungen erfunden.

## MAC97A6

**4/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Weitere passende Beispiele gesucht.

- [TRIAC-Phasensteuerung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/semiconductors/chpt-7/the-triac/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [TRIAC-Schalter und Phasenanschnitt](https://www.electronics-tutorials.ws/power/triac.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [DIAC-TRIAC-Dimmer und Triggerung](https://learnabout-electronics.org/Semiconductors/thyristors_64.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [AN5114: TRIAC mit Optotriac ansteuern](https://www.st.com.cn/resource/en/application_note/an5114-controlling-a-triac-with-a-phototriac-stmicroelectronics.pdf) — st.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
- [AN-9745: TRIAC-Dimmer und LED-Lasten](https://www.onsemi.jp/download/application-notes/pdf/an-9745.pdf) — onsemi.com; Entwurfshilfe; geprüft 2026-10-25.

Schaltungsprinzip; Gate-Empfindlichkeit, Haltestrom und Spannungsfestigkeit des konkreten TRIACs abgleichen. Netzspannungsbeispiel. TRIAC-Grundschaltungen: Triggerquadranten, Gate-, Halte- und Einraststrom sowie Laststrom für den Typ prüfen; ein MAC97 ersetzt keinen Leistungs-TRIAC. Verlinkte Netzspannungsschaltungen sind keine Steckbrettaufbauten.

**Recherchebedarf:** Bisher sind weniger als fünf unterschiedliche Websites mit passenden Beispielen belegt. Die vorhandenen Grundschaltungen und Referenzen sind oben gekennzeichnet; es wurden keine zusätzlichen Beschaltungen erfunden.

## 78L05

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Regler-Grundbeschaltung (Hersteller) (PDF S. 17)](../Datenblaetter/Spannungsregler/L78L05_12_ST_Familie.pdf#page=17) · [Online-Original](https://datasheet4u.com/pdf/1307369/L78L05C.pdf) — datasheet4u.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [78xx/79xx-Regler und symmetrische Versorgung](https://learnabout-electronics.org/PSU/psu23.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Positive und negative lineare Spannungsregler](https://circuitdigest.com/electronic-circuits/voltage-regulators) — circuitdigest.com; Grundschaltung; geprüft 2026-10-25.
- [78xx-Grundschaltung und Abblockung](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/7805-7812-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.
- [Lineare Netzteile und Regler-Grundschaltung](https://www.electronics-tutorials.ws/supplies/power-supplies-for-beginners-part-3.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Im Familien-Datenblatt die Werte, Pinfolge und Beschaltung der angegebenen Ausgangsspannung/Variante verwenden. Regler-Grundschaltung: Ausgangsspannung, Stromklasse (78L/78/78S), Pinbelegung, Mindestlast und vom Hersteller geforderte Kondensatoren des vorhandenen Typs verwenden.

## 78L12

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Regler-Grundbeschaltung (Hersteller) (PDF S. 17)](../Datenblaetter/Spannungsregler/L78L05_12_ST_Familie.pdf#page=17) · [Online-Original](https://datasheet4u.com/pdf/1307369/L78L05C.pdf) — datasheet4u.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [78xx/79xx-Regler und symmetrische Versorgung](https://learnabout-electronics.org/PSU/psu23.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Positive und negative lineare Spannungsregler](https://circuitdigest.com/electronic-circuits/voltage-regulators) — circuitdigest.com; Grundschaltung; geprüft 2026-10-25.
- [78xx-Grundschaltung und Abblockung](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/7805-7812-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.
- [Lineare Netzteile und Regler-Grundschaltung](https://www.electronics-tutorials.ws/supplies/power-supplies-for-beginners-part-3.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Im Familien-Datenblatt die Werte, Pinfolge und Beschaltung der angegebenen Ausgangsspannung/Variante verwenden. Regler-Grundschaltung: Ausgangsspannung, Stromklasse (78L/78/78S), Pinbelegung, Mindestlast und vom Hersteller geforderte Kondensatoren des vorhandenen Typs verwenden.

## 79L05

**5/5 Beispiel-Websites**, 8 Quellen-Websites insgesamt. Ziel erreicht.

- [Regler-Grundbeschaltung (Hersteller) (PDF S. 4)](../Datenblaetter/Spannungsregler/L79L05_ST_Familie.pdf#page=4) · [Online-Original](https://datasheet4u.com/pdf/1234825/L79L05AC.pdf) — datasheet4u.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Prinzipreferenz; geprüft 2026-10-25.
- [78xx/79xx-Regler und symmetrische Versorgung](https://learnabout-electronics.org/PSU/psu23.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Positive und negative lineare Spannungsregler](https://circuitdigest.com/electronic-circuits/voltage-regulators) — circuitdigest.com; Prinzipreferenz; geprüft 2026-10-25.
- [Lineare Netzteile und Regler-Grundschaltung](https://www.electronics-tutorials.ws/supplies/power-supplies-for-beginners-part-3.html) — electronics-tutorials.ws; Prinzipreferenz; geprüft 2026-10-25.
- [79xx: negative Regler-Grundschaltung](https://www.kwcsangli.in/uploads/Electronics-Devices-and-Circuits---II.pdf) — kwcsangli.in; Grundschaltung; geprüft 2026-10-25.
- [Laborversuch mit 7805, 7809 und 7912](https://ggnindia.dronacharya.info/ECE/Downloads/Labmanuals/AC-ECE-11072023-IV.pdf) — ggnindia.dronacharya.info; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbau eines negativen 79xx-Spannungsreglers](https://snh.bsiet.org/wp-content/uploads/312314-Basic-Electronics-1.pdf) — snh.bsiet.org; Grundschaltung; geprüft 2026-10-25.

Im Familien-Datenblatt die Werte, Pinfolge und Beschaltung der angegebenen Ausgangsspannung/Variante verwenden. Regler-Grundschaltung: Ausgangsspannung, Stromklasse (78L/78/78S), Pinbelegung, Mindestlast und vom Hersteller geforderte Kondensatoren des vorhandenen Typs verwenden. Negative Regler brauchen eine ausreichend negative Eingangsspannung. Plus-/Minus-Grundschaltungen nicht durch bloßes Umstecken gleichsetzen; Pinfolge und Kondensatorpolarität prüfen.

## KA7909

**5/5 Beispiel-Websites**, 8 Quellen-Websites insgesamt. Ziel erreicht.

- [Regler-Grundbeschaltung (Hersteller) (PDF S. 15)](../Datenblaetter/Spannungsregler/KA7909_Fairchild.pdf#page=15) · [Online-Original](https://datasheet4u.com/pdf/390075/KA7909.pdf) — datasheet4u.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Prinzipreferenz; geprüft 2026-10-25.
- [78xx/79xx-Regler und symmetrische Versorgung](https://learnabout-electronics.org/PSU/psu23.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Positive und negative lineare Spannungsregler](https://circuitdigest.com/electronic-circuits/voltage-regulators) — circuitdigest.com; Prinzipreferenz; geprüft 2026-10-25.
- [Lineare Netzteile und Regler-Grundschaltung](https://www.electronics-tutorials.ws/supplies/power-supplies-for-beginners-part-3.html) — electronics-tutorials.ws; Prinzipreferenz; geprüft 2026-10-25.
- [79xx: negative Regler-Grundschaltung](https://www.kwcsangli.in/uploads/Electronics-Devices-and-Circuits---II.pdf) — kwcsangli.in; Grundschaltung; geprüft 2026-10-25.
- [Laborversuch mit 7805, 7809 und 7912](https://ggnindia.dronacharya.info/ECE/Downloads/Labmanuals/AC-ECE-11072023-IV.pdf) — ggnindia.dronacharya.info; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbau eines negativen 79xx-Spannungsreglers](https://snh.bsiet.org/wp-content/uploads/312314-Basic-Electronics-1.pdf) — snh.bsiet.org; Grundschaltung; geprüft 2026-10-25.

Im Familien-Datenblatt die Werte, Pinfolge und Beschaltung der angegebenen Ausgangsspannung/Variante verwenden. Regler-Grundschaltung: Ausgangsspannung, Stromklasse (78L/78/78S), Pinbelegung, Mindestlast und vom Hersteller geforderte Kondensatoren des vorhandenen Typs verwenden. Negative Regler brauchen eine ausreichend negative Eingangsspannung. Plus-/Minus-Grundschaltungen nicht durch bloßes Umstecken gleichsetzen; Pinfolge und Kondensatorpolarität prüfen.

## L7805CV

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Regler-Grundbeschaltung (Hersteller) (PDF S. 4)](../Datenblaetter/Spannungsregler/L78_ST.pdf#page=4) · [Online-Original](https://datasheet4u.com/pdf/1162253/L7824.pdf) — datasheet4u.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [78xx/79xx-Regler und symmetrische Versorgung](https://learnabout-electronics.org/PSU/psu23.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Positive und negative lineare Spannungsregler](https://circuitdigest.com/electronic-circuits/voltage-regulators) — circuitdigest.com; Grundschaltung; geprüft 2026-10-25.
- [78xx-Grundschaltung und Abblockung](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/7805-7812-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.
- [Lineare Netzteile und Regler-Grundschaltung](https://www.electronics-tutorials.ws/supplies/power-supplies-for-beginners-part-3.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Im Familien-Datenblatt die Werte, Pinfolge und Beschaltung der angegebenen Ausgangsspannung/Variante verwenden. Regler-Grundschaltung: Ausgangsspannung, Stromklasse (78L/78/78S), Pinbelegung, Mindestlast und vom Hersteller geforderte Kondensatoren des vorhandenen Typs verwenden.

## L7809CV

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Regler-Grundbeschaltung (Hersteller) (PDF S. 4)](../Datenblaetter/Spannungsregler/L78_ST.pdf#page=4) · [Online-Original](https://datasheet4u.com/pdf/1162253/L7824.pdf) — datasheet4u.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [78xx/79xx-Regler und symmetrische Versorgung](https://learnabout-electronics.org/PSU/psu23.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Positive und negative lineare Spannungsregler](https://circuitdigest.com/electronic-circuits/voltage-regulators) — circuitdigest.com; Grundschaltung; geprüft 2026-10-25.
- [78xx-Grundschaltung und Abblockung](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/7805-7812-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.
- [Lineare Netzteile und Regler-Grundschaltung](https://www.electronics-tutorials.ws/supplies/power-supplies-for-beginners-part-3.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Im Familien-Datenblatt die Werte, Pinfolge und Beschaltung der angegebenen Ausgangsspannung/Variante verwenden. Regler-Grundschaltung: Ausgangsspannung, Stromklasse (78L/78/78S), Pinbelegung, Mindestlast und vom Hersteller geforderte Kondensatoren des vorhandenen Typs verwenden.

## L7812CV

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Regler-Grundbeschaltung (Hersteller) (PDF S. 4)](../Datenblaetter/Spannungsregler/L78_ST.pdf#page=4) · [Online-Original](https://datasheet4u.com/pdf/1162253/L7824.pdf) — datasheet4u.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [78xx/79xx-Regler und symmetrische Versorgung](https://learnabout-electronics.org/PSU/psu23.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Positive und negative lineare Spannungsregler](https://circuitdigest.com/electronic-circuits/voltage-regulators) — circuitdigest.com; Grundschaltung; geprüft 2026-10-25.
- [78xx-Grundschaltung und Abblockung](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/7805-7812-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.
- [Lineare Netzteile und Regler-Grundschaltung](https://www.electronics-tutorials.ws/supplies/power-supplies-for-beginners-part-3.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Im Familien-Datenblatt die Werte, Pinfolge und Beschaltung der angegebenen Ausgangsspannung/Variante verwenden. Regler-Grundschaltung: Ausgangsspannung, Stromklasse (78L/78/78S), Pinbelegung, Mindestlast und vom Hersteller geforderte Kondensatoren des vorhandenen Typs verwenden.

## L7815CV

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Regler-Grundbeschaltung (Hersteller) (PDF S. 4)](../Datenblaetter/Spannungsregler/L78_ST.pdf#page=4) · [Online-Original](https://datasheet4u.com/pdf/1162253/L7824.pdf) — datasheet4u.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [78xx/79xx-Regler und symmetrische Versorgung](https://learnabout-electronics.org/PSU/psu23.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Positive und negative lineare Spannungsregler](https://circuitdigest.com/electronic-circuits/voltage-regulators) — circuitdigest.com; Grundschaltung; geprüft 2026-10-25.
- [78xx-Grundschaltung und Abblockung](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/7805-7812-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.
- [Lineare Netzteile und Regler-Grundschaltung](https://www.electronics-tutorials.ws/supplies/power-supplies-for-beginners-part-3.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Im Familien-Datenblatt die Werte, Pinfolge und Beschaltung der angegebenen Ausgangsspannung/Variante verwenden. Regler-Grundschaltung: Ausgangsspannung, Stromklasse (78L/78/78S), Pinbelegung, Mindestlast und vom Hersteller geforderte Kondensatoren des vorhandenen Typs verwenden.

## L7824CV

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Regler-Grundbeschaltung (Hersteller) (PDF S. 4)](../Datenblaetter/Spannungsregler/L78_ST.pdf#page=4) · [Online-Original](https://datasheet4u.com/pdf/1162253/L7824.pdf) — datasheet4u.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [78xx/79xx-Regler und symmetrische Versorgung](https://learnabout-electronics.org/PSU/psu23.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Positive und negative lineare Spannungsregler](https://circuitdigest.com/electronic-circuits/voltage-regulators) — circuitdigest.com; Grundschaltung; geprüft 2026-10-25.
- [78xx-Grundschaltung und Abblockung](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/7805-7812-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.
- [Lineare Netzteile und Regler-Grundschaltung](https://www.electronics-tutorials.ws/supplies/power-supplies-for-beginners-part-3.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Im Familien-Datenblatt die Werte, Pinfolge und Beschaltung der angegebenen Ausgangsspannung/Variante verwenden. Regler-Grundschaltung: Ausgangsspannung, Stromklasse (78L/78/78S), Pinbelegung, Mindestlast und vom Hersteller geforderte Kondensatoren des vorhandenen Typs verwenden.

## L7905CV

**5/5 Beispiel-Websites**, 8 Quellen-Websites insgesamt. Ziel erreicht.

- [Regler-Grundbeschaltung (Hersteller) (PDF S. 11)](../Datenblaetter/Spannungsregler/L79_ST.pdf#page=11) · [Online-Original](https://datasheet4u.com/pdf/973913/L79.pdf) — datasheet4u.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Prinzipreferenz; geprüft 2026-10-25.
- [78xx/79xx-Regler und symmetrische Versorgung](https://learnabout-electronics.org/PSU/psu23.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Positive und negative lineare Spannungsregler](https://circuitdigest.com/electronic-circuits/voltage-regulators) — circuitdigest.com; Prinzipreferenz; geprüft 2026-10-25.
- [Lineare Netzteile und Regler-Grundschaltung](https://www.electronics-tutorials.ws/supplies/power-supplies-for-beginners-part-3.html) — electronics-tutorials.ws; Prinzipreferenz; geprüft 2026-10-25.
- [79xx: negative Regler-Grundschaltung](https://www.kwcsangli.in/uploads/Electronics-Devices-and-Circuits---II.pdf) — kwcsangli.in; Grundschaltung; geprüft 2026-10-25.
- [Laborversuch mit 7805, 7809 und 7912](https://ggnindia.dronacharya.info/ECE/Downloads/Labmanuals/AC-ECE-11072023-IV.pdf) — ggnindia.dronacharya.info; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbau eines negativen 79xx-Spannungsreglers](https://snh.bsiet.org/wp-content/uploads/312314-Basic-Electronics-1.pdf) — snh.bsiet.org; Grundschaltung; geprüft 2026-10-25.

Im Familien-Datenblatt die Werte, Pinfolge und Beschaltung der angegebenen Ausgangsspannung/Variante verwenden. Regler-Grundschaltung: Ausgangsspannung, Stromklasse (78L/78/78S), Pinbelegung, Mindestlast und vom Hersteller geforderte Kondensatoren des vorhandenen Typs verwenden. Negative Regler brauchen eine ausreichend negative Eingangsspannung. Plus-/Minus-Grundschaltungen nicht durch bloßes Umstecken gleichsetzen; Pinfolge und Kondensatorpolarität prüfen.

## L7912CV

**5/5 Beispiel-Websites**, 8 Quellen-Websites insgesamt. Ziel erreicht.

- [Regler-Grundbeschaltung (Hersteller) (PDF S. 11)](../Datenblaetter/Spannungsregler/L79_ST.pdf#page=11) · [Online-Original](https://datasheet4u.com/pdf/973913/L79.pdf) — datasheet4u.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Prinzipreferenz; geprüft 2026-10-25.
- [78xx/79xx-Regler und symmetrische Versorgung](https://learnabout-electronics.org/PSU/psu23.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Positive und negative lineare Spannungsregler](https://circuitdigest.com/electronic-circuits/voltage-regulators) — circuitdigest.com; Prinzipreferenz; geprüft 2026-10-25.
- [Lineare Netzteile und Regler-Grundschaltung](https://www.electronics-tutorials.ws/supplies/power-supplies-for-beginners-part-3.html) — electronics-tutorials.ws; Prinzipreferenz; geprüft 2026-10-25.
- [79xx: negative Regler-Grundschaltung](https://www.kwcsangli.in/uploads/Electronics-Devices-and-Circuits---II.pdf) — kwcsangli.in; Grundschaltung; geprüft 2026-10-25.
- [Laborversuch mit 7805, 7809 und 7912](https://ggnindia.dronacharya.info/ECE/Downloads/Labmanuals/AC-ECE-11072023-IV.pdf) — ggnindia.dronacharya.info; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbau eines negativen 79xx-Spannungsreglers](https://snh.bsiet.org/wp-content/uploads/312314-Basic-Electronics-1.pdf) — snh.bsiet.org; Grundschaltung; geprüft 2026-10-25.

Im Familien-Datenblatt die Werte, Pinfolge und Beschaltung der angegebenen Ausgangsspannung/Variante verwenden. Regler-Grundschaltung: Ausgangsspannung, Stromklasse (78L/78/78S), Pinbelegung, Mindestlast und vom Hersteller geforderte Kondensatoren des vorhandenen Typs verwenden. Negative Regler brauchen eine ausreichend negative Eingangsspannung. Plus-/Minus-Grundschaltungen nicht durch bloßes Umstecken gleichsetzen; Pinfolge und Kondensatorpolarität prüfen.

## LM317

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Regler-Grundbeschaltung (Hersteller) (PDF S. 15)](../Datenblaetter/Spannungsregler/LM317_TI.pdf#page=15) · [Online-Original](https://www.ti.com/lit/ds/symlink/lm317.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [0–30-V-Regler (TI) (PDF S. 17)](../Datenblaetter/Spannungsregler/LM317_TI.pdf#page=17) · [Online-Original](https://www.ti.com/lit/ds/symlink/lm317.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [LM317-Grundschaltung und Spannungseinstellung](https://www.electronics-notes.com/articles/component-data/voltage-regulators/LM317.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.
- [Einstellbares LM317-Netzteil](https://circuitdigest.com/electronic-circuits/lm317-variable-voltage-regulator-circuit-diagram) — circuitdigest.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [Einstellbarer Regler mit LM317](https://electronicsarea.com/lm317-variable-voltage-regulator-circuit-diagram/) — electronicsarea.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [Lineare Netzteile und LM317](https://www.electronics-tutorials.ws/supplies/power-supplies-for-beginners-part-3.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Im Familien-Datenblatt die Werte, Pinfolge und Beschaltung der angegebenen Ausgangsspannung/Variante verwenden.

## TL431A

**4/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Weitere passende Beispiele gesucht.

- [Regler-Grundbeschaltung (Hersteller) (PDF S. 26)](../Datenblaetter/Spannungsregler/TL431_TI.pdf#page=26) · [Online-Original](https://www.ti.com/lit/ds/symlink/tl431.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Komparator mit Referenz (TI) (PDF S. 23)](../Datenblaetter/Spannungsregler/TL431_TI.pdf#page=23) · [Online-Original](https://www.ti.com/lit/ds/symlink/tl431.pdf) — ti.com; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [TL431: Shuntregler, Stromsenke und Regelkreis](https://assets.nexperia.com/documents/data-sheet/TL431-Q_FAM.pdf) — assets.nexperia.com; Herstellerbeispiel; geprüft 2026-10-25.
  Hinweis: Nexperia-Referenzvariante: Pinfolge, Stabilitätsbedingungen und Strombereich abgleichen.
- [TL431 und Optokoppler im Rückkopplungszweig](https://www.controleng.com/gain-consideration-using-a-shunt-regulator-and-optocoupler-feedback/) — controleng.com; Entwurfshilfe; geprüft 2026-10-25.
- [TL431 als einstellbare 3,3-V-Referenz](https://docs.devoltapp.com/parts/comparators-and-references) — docs.devoltapp.com; Grundschaltung; geprüft 2026-10-25.
- [Tech Ideas: TL431 als Batterie-Unterspannungsanzeige](https://www.youtube.com/watch?v=t99GakIhhoE) — youtube.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.

Im Familien-Datenblatt die Werte, Pinfolge und Beschaltung der angegebenen Ausgangsspannung/Variante verwenden. TL431-Grundschaltung: Kathoden-Mindeststrom und Stabilität mit Ausgangskapazität beachten; A-Suffix und Hersteller-Pinfolge abgleichen.

**Recherchebedarf:** Bisher sind weniger als fünf unterschiedliche Websites mit passenden Beispielen belegt. Die vorhandenen Grundschaltungen und Referenzen sind oben gekennzeichnet; es wurden keine zusätzlichen Beschaltungen erfunden.

## 1N4001

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Brückengleichrichter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/full-wave-bridge-rectifier/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Einweggleichrichter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/half-wave-rectifier/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gleichrichter, Schutz- und Begrenzerschaltungen](https://learn.sparkfun.com/tutorials/diodes/diode-applications) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [Gleichrichtung, Schutzdioden und Diodentester](https://electronicsclub.info/diodes.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Brückengleichrichter und Siebung](https://www.electronics-tutorials.ws/diode/diode_6.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Einweg-, Zweiweg- und Brückengleichrichtung](https://learnabout-electronics.org/PSU/psu11.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Spannungs-, Strom- und Frequenzgrenzen des konkreten Diodentyps beachten. Grundschaltung: Sperrspannung, Dauer-/Stoßstrom und Verlustleistung prüfen; SY356 ist nicht allein durch den Link als 1N400x-Ersatz bestätigt.

## 1N4002

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Brückengleichrichter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/full-wave-bridge-rectifier/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Einweggleichrichter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/half-wave-rectifier/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gleichrichter, Schutz- und Begrenzerschaltungen](https://learn.sparkfun.com/tutorials/diodes/diode-applications) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [Gleichrichtung, Schutzdioden und Diodentester](https://electronicsclub.info/diodes.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Brückengleichrichter und Siebung](https://www.electronics-tutorials.ws/diode/diode_6.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Einweg-, Zweiweg- und Brückengleichrichtung](https://learnabout-electronics.org/PSU/psu11.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Spannungs-, Strom- und Frequenzgrenzen des konkreten Diodentyps beachten. Grundschaltung: Sperrspannung, Dauer-/Stoßstrom und Verlustleistung prüfen; SY356 ist nicht allein durch den Link als 1N400x-Ersatz bestätigt.

## 1N4003

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Brückengleichrichter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/full-wave-bridge-rectifier/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Einweggleichrichter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/half-wave-rectifier/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gleichrichter, Schutz- und Begrenzerschaltungen](https://learn.sparkfun.com/tutorials/diodes/diode-applications) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [Gleichrichtung, Schutzdioden und Diodentester](https://electronicsclub.info/diodes.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Brückengleichrichter und Siebung](https://www.electronics-tutorials.ws/diode/diode_6.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Einweg-, Zweiweg- und Brückengleichrichtung](https://learnabout-electronics.org/PSU/psu11.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Spannungs-, Strom- und Frequenzgrenzen des konkreten Diodentyps beachten. Grundschaltung: Sperrspannung, Dauer-/Stoßstrom und Verlustleistung prüfen; SY356 ist nicht allein durch den Link als 1N400x-Ersatz bestätigt.

## 1N4004

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Brückengleichrichter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/full-wave-bridge-rectifier/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Einweggleichrichter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/half-wave-rectifier/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gleichrichter, Schutz- und Begrenzerschaltungen](https://learn.sparkfun.com/tutorials/diodes/diode-applications) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [Gleichrichtung, Schutzdioden und Diodentester](https://electronicsclub.info/diodes.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Brückengleichrichter und Siebung](https://www.electronics-tutorials.ws/diode/diode_6.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Einweg-, Zweiweg- und Brückengleichrichtung](https://learnabout-electronics.org/PSU/psu11.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Spannungs-, Strom- und Frequenzgrenzen des konkreten Diodentyps beachten. Grundschaltung: Sperrspannung, Dauer-/Stoßstrom und Verlustleistung prüfen; SY356 ist nicht allein durch den Link als 1N400x-Ersatz bestätigt.

## SY356

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Brückengleichrichter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/full-wave-bridge-rectifier/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Einweggleichrichter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/half-wave-rectifier/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gleichrichter, Schutz- und Begrenzerschaltungen](https://learn.sparkfun.com/tutorials/diodes/diode-applications) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [Gleichrichtung, Schutzdioden und Diodentester](https://electronicsclub.info/diodes.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Brückengleichrichter und Siebung](https://www.electronics-tutorials.ws/diode/diode_6.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Einweg-, Zweiweg- und Brückengleichrichtung](https://learnabout-electronics.org/PSU/psu11.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Spannungs-, Strom- und Frequenzgrenzen des konkreten Diodentyps beachten. Grundschaltung: Sperrspannung, Dauer-/Stoßstrom und Verlustleistung prüfen; SY356 ist nicht allein durch den Link als 1N400x-Ersatz bestätigt.

## 1N4148

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Signalbegrenzer (Grundschaltung)](https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/clipper-circuits/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Freilaufdiode (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/commutating-diode/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Gleichrichter, Schutz- und Begrenzerschaltungen](https://learn.sparkfun.com/tutorials/diodes/diode-applications) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [Gleichrichtung, Schutzdioden und Diodentester](https://electronicsclub.info/diodes.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Signalbegrenzung mit Dioden](https://www.electronics-tutorials.ws/diode/diode-clipping-circuits.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Einweg-, Zweiweg- und Brückengleichrichtung](https://learnabout-electronics.org/PSU/psu11.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Spannungs-, Strom- und Frequenzgrenzen des konkreten Diodentyps beachten. 1N4148 nur für geeignete Signal-/Kleinlastströme einsetzen; die Gleichrichterquelle erläutert das Prinzip und ist kein Leistungsnetzteil mit 1N4148.

## Quarz 32,768 kHz

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Pierce-Oszillator (ST)](https://www.st.com/resource/en/application_note/an2867-guidelines-for-oscillator-design-on-stm8afals-and-stm32-mcusmpus-stmicroelectronics.pdf) — st.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [Quarzoszillator (Grundschaltung)](https://www.allaboutcircuits.com/textbook/designing-analog-chips/timers-and-oscillators/crystal-oscillators/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Quarzoszillatoren mit diskreter und IC-Verstärkung](https://www.electronics-tutorials.ws/oscillator/crystal.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [AN826: Quarzoszillator und Lastkapazität](https://ww1.microchip.com/downloads/en/appnotes/00826a.pdf) — microchip.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
- [AN14518: Quarzoszillator auslegen und messen](https://www.nxp.jp/docs/en/application-note/AN14518.pdf) — nxp.com; Entwurfshilfe; geprüft 2026-10-25.
  Hinweis: Reader-IC-spezifische Beispiele; zulässigen Frequenzbereich und Last des tatsächlichen Oszillatortreibers prüfen.
- [RC- und quarzgesteuerte Taktgeneratoren](https://learnabout-electronics.org/Digital/dig51.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundprinzip; Zielschaltung und Lastkapazitäten auf die angegebene Frequenz, Quarzart und den zulässigen Ansteuerpegel auslegen. Entwurfshilfen mit unterschiedlichen Frequenzbereichen. Eine gleiche Frequenz allein bestätigt weder Lastkapazität, Schwingmodus noch zulässige Anregungsleistung des vorhandenen Quarzes.

## Quarz 4 MHz

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Pierce-Oszillator (ST)](https://www.st.com/resource/en/application_note/an2867-guidelines-for-oscillator-design-on-stm8afals-and-stm32-mcusmpus-stmicroelectronics.pdf) — st.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [Quarzoszillator (Grundschaltung)](https://www.allaboutcircuits.com/textbook/designing-analog-chips/timers-and-oscillators/crystal-oscillators/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Quarzoszillatoren mit diskreter und IC-Verstärkung](https://www.electronics-tutorials.ws/oscillator/crystal.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [AN826: Quarzoszillator und Lastkapazität](https://ww1.microchip.com/downloads/en/appnotes/00826a.pdf) — microchip.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
- [AN14518: Quarzoszillator auslegen und messen](https://www.nxp.jp/docs/en/application-note/AN14518.pdf) — nxp.com; Entwurfshilfe; geprüft 2026-10-25.
  Hinweis: Reader-IC-spezifische Beispiele; zulässigen Frequenzbereich und Last des tatsächlichen Oszillatortreibers prüfen.
- [RC- und quarzgesteuerte Taktgeneratoren](https://learnabout-electronics.org/Digital/dig51.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundprinzip; Zielschaltung und Lastkapazitäten auf die angegebene Frequenz, Quarzart und den zulässigen Ansteuerpegel auslegen. Entwurfshilfen mit unterschiedlichen Frequenzbereichen. Eine gleiche Frequenz allein bestätigt weder Lastkapazität, Schwingmodus noch zulässige Anregungsleistung des vorhandenen Quarzes.

## Quarz 6 MHz

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Pierce-Oszillator (ST)](https://www.st.com/resource/en/application_note/an2867-guidelines-for-oscillator-design-on-stm8afals-and-stm32-mcusmpus-stmicroelectronics.pdf) — st.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [Quarzoszillator (Grundschaltung)](https://www.allaboutcircuits.com/textbook/designing-analog-chips/timers-and-oscillators/crystal-oscillators/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Quarzoszillatoren mit diskreter und IC-Verstärkung](https://www.electronics-tutorials.ws/oscillator/crystal.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [AN826: Quarzoszillator und Lastkapazität](https://ww1.microchip.com/downloads/en/appnotes/00826a.pdf) — microchip.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
- [AN14518: Quarzoszillator auslegen und messen](https://www.nxp.jp/docs/en/application-note/AN14518.pdf) — nxp.com; Entwurfshilfe; geprüft 2026-10-25.
  Hinweis: Reader-IC-spezifische Beispiele; zulässigen Frequenzbereich und Last des tatsächlichen Oszillatortreibers prüfen.
- [RC- und quarzgesteuerte Taktgeneratoren](https://learnabout-electronics.org/Digital/dig51.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundprinzip; Zielschaltung und Lastkapazitäten auf die angegebene Frequenz, Quarzart und den zulässigen Ansteuerpegel auslegen. Entwurfshilfen mit unterschiedlichen Frequenzbereichen. Eine gleiche Frequenz allein bestätigt weder Lastkapazität, Schwingmodus noch zulässige Anregungsleistung des vorhandenen Quarzes.

## Quarz 8 MHz

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Pierce-Oszillator (ST)](https://www.st.com/resource/en/application_note/an2867-guidelines-for-oscillator-design-on-stm8afals-and-stm32-mcusmpus-stmicroelectronics.pdf) — st.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [Quarzoszillator (Grundschaltung)](https://www.allaboutcircuits.com/textbook/designing-analog-chips/timers-and-oscillators/crystal-oscillators/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Quarzoszillatoren mit diskreter und IC-Verstärkung](https://www.electronics-tutorials.ws/oscillator/crystal.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [AN826: Quarzoszillator und Lastkapazität](https://ww1.microchip.com/downloads/en/appnotes/00826a.pdf) — microchip.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
- [AN14518: Quarzoszillator auslegen und messen](https://www.nxp.jp/docs/en/application-note/AN14518.pdf) — nxp.com; Entwurfshilfe; geprüft 2026-10-25.
  Hinweis: Reader-IC-spezifische Beispiele; zulässigen Frequenzbereich und Last des tatsächlichen Oszillatortreibers prüfen.
- [RC- und quarzgesteuerte Taktgeneratoren](https://learnabout-electronics.org/Digital/dig51.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundprinzip; Zielschaltung und Lastkapazitäten auf die angegebene Frequenz, Quarzart und den zulässigen Ansteuerpegel auslegen. Entwurfshilfen mit unterschiedlichen Frequenzbereichen. Eine gleiche Frequenz allein bestätigt weder Lastkapazität, Schwingmodus noch zulässige Anregungsleistung des vorhandenen Quarzes.

## Quarz 11,0592 MHz

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Pierce-Oszillator (ST)](https://www.st.com/resource/en/application_note/an2867-guidelines-for-oscillator-design-on-stm8afals-and-stm32-mcusmpus-stmicroelectronics.pdf) — st.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [Quarzoszillator (Grundschaltung)](https://www.allaboutcircuits.com/textbook/designing-analog-chips/timers-and-oscillators/crystal-oscillators/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Quarzoszillatoren mit diskreter und IC-Verstärkung](https://www.electronics-tutorials.ws/oscillator/crystal.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [AN826: Quarzoszillator und Lastkapazität](https://ww1.microchip.com/downloads/en/appnotes/00826a.pdf) — microchip.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
- [AN14518: Quarzoszillator auslegen und messen](https://www.nxp.jp/docs/en/application-note/AN14518.pdf) — nxp.com; Entwurfshilfe; geprüft 2026-10-25.
  Hinweis: Reader-IC-spezifische Beispiele; zulässigen Frequenzbereich und Last des tatsächlichen Oszillatortreibers prüfen.
- [RC- und quarzgesteuerte Taktgeneratoren](https://learnabout-electronics.org/Digital/dig51.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundprinzip; Zielschaltung und Lastkapazitäten auf die angegebene Frequenz, Quarzart und den zulässigen Ansteuerpegel auslegen. Entwurfshilfen mit unterschiedlichen Frequenzbereichen. Eine gleiche Frequenz allein bestätigt weder Lastkapazität, Schwingmodus noch zulässige Anregungsleistung des vorhandenen Quarzes.

## Quarz 12 MHz

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Pierce-Oszillator (ST)](https://www.st.com/resource/en/application_note/an2867-guidelines-for-oscillator-design-on-stm8afals-and-stm32-mcusmpus-stmicroelectronics.pdf) — st.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [Quarzoszillator (Grundschaltung)](https://www.allaboutcircuits.com/textbook/designing-analog-chips/timers-and-oscillators/crystal-oscillators/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Quarzoszillatoren mit diskreter und IC-Verstärkung](https://www.electronics-tutorials.ws/oscillator/crystal.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [AN826: Quarzoszillator und Lastkapazität](https://ww1.microchip.com/downloads/en/appnotes/00826a.pdf) — microchip.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
- [AN14518: Quarzoszillator auslegen und messen](https://www.nxp.jp/docs/en/application-note/AN14518.pdf) — nxp.com; Entwurfshilfe; geprüft 2026-10-25.
  Hinweis: Reader-IC-spezifische Beispiele; zulässigen Frequenzbereich und Last des tatsächlichen Oszillatortreibers prüfen.
- [RC- und quarzgesteuerte Taktgeneratoren](https://learnabout-electronics.org/Digital/dig51.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundprinzip; Zielschaltung und Lastkapazitäten auf die angegebene Frequenz, Quarzart und den zulässigen Ansteuerpegel auslegen. Entwurfshilfen mit unterschiedlichen Frequenzbereichen. Eine gleiche Frequenz allein bestätigt weder Lastkapazität, Schwingmodus noch zulässige Anregungsleistung des vorhandenen Quarzes.

## Quarz 13,56 MHz

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Pierce-Oszillator (ST)](https://www.st.com/resource/en/application_note/an2867-guidelines-for-oscillator-design-on-stm8afals-and-stm32-mcusmpus-stmicroelectronics.pdf) — st.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [Quarzoszillator (Grundschaltung)](https://www.allaboutcircuits.com/textbook/designing-analog-chips/timers-and-oscillators/crystal-oscillators/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Quarzoszillatoren mit diskreter und IC-Verstärkung](https://www.electronics-tutorials.ws/oscillator/crystal.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [AN826: Quarzoszillator und Lastkapazität](https://ww1.microchip.com/downloads/en/appnotes/00826a.pdf) — microchip.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
- [AN14518: Quarzoszillator auslegen und messen](https://www.nxp.jp/docs/en/application-note/AN14518.pdf) — nxp.com; Entwurfshilfe; geprüft 2026-10-25.
  Hinweis: Reader-IC-spezifische Beispiele; zulässigen Frequenzbereich und Last des tatsächlichen Oszillatortreibers prüfen.
- [RC- und quarzgesteuerte Taktgeneratoren](https://learnabout-electronics.org/Digital/dig51.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundprinzip; Zielschaltung und Lastkapazitäten auf die angegebene Frequenz, Quarzart und den zulässigen Ansteuerpegel auslegen. Entwurfshilfen mit unterschiedlichen Frequenzbereichen. Eine gleiche Frequenz allein bestätigt weder Lastkapazität, Schwingmodus noch zulässige Anregungsleistung des vorhandenen Quarzes.

## Quarz 16 MHz

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Pierce-Oszillator (ST)](https://www.st.com/resource/en/application_note/an2867-guidelines-for-oscillator-design-on-stm8afals-and-stm32-mcusmpus-stmicroelectronics.pdf) — st.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [Quarzoszillator (Grundschaltung)](https://www.allaboutcircuits.com/textbook/designing-analog-chips/timers-and-oscillators/crystal-oscillators/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Quarzoszillatoren mit diskreter und IC-Verstärkung](https://www.electronics-tutorials.ws/oscillator/crystal.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [AN826: Quarzoszillator und Lastkapazität](https://ww1.microchip.com/downloads/en/appnotes/00826a.pdf) — microchip.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
- [AN14518: Quarzoszillator auslegen und messen](https://www.nxp.jp/docs/en/application-note/AN14518.pdf) — nxp.com; Entwurfshilfe; geprüft 2026-10-25.
  Hinweis: Reader-IC-spezifische Beispiele; zulässigen Frequenzbereich und Last des tatsächlichen Oszillatortreibers prüfen.
- [RC- und quarzgesteuerte Taktgeneratoren](https://learnabout-electronics.org/Digital/dig51.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundprinzip; Zielschaltung und Lastkapazitäten auf die angegebene Frequenz, Quarzart und den zulässigen Ansteuerpegel auslegen. Entwurfshilfen mit unterschiedlichen Frequenzbereichen. Eine gleiche Frequenz allein bestätigt weder Lastkapazität, Schwingmodus noch zulässige Anregungsleistung des vorhandenen Quarzes.

## Quarz 22,1184 MHz

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Pierce-Oszillator (ST)](https://www.st.com/resource/en/application_note/an2867-guidelines-for-oscillator-design-on-stm8afals-and-stm32-mcusmpus-stmicroelectronics.pdf) — st.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [Quarzoszillator (Grundschaltung)](https://www.allaboutcircuits.com/textbook/designing-analog-chips/timers-and-oscillators/crystal-oscillators/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Quarzoszillatoren mit diskreter und IC-Verstärkung](https://www.electronics-tutorials.ws/oscillator/crystal.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [AN826: Quarzoszillator und Lastkapazität](https://ww1.microchip.com/downloads/en/appnotes/00826a.pdf) — microchip.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
- [AN14518: Quarzoszillator auslegen und messen](https://www.nxp.jp/docs/en/application-note/AN14518.pdf) — nxp.com; Entwurfshilfe; geprüft 2026-10-25.
  Hinweis: Reader-IC-spezifische Beispiele; zulässigen Frequenzbereich und Last des tatsächlichen Oszillatortreibers prüfen.
- [RC- und quarzgesteuerte Taktgeneratoren](https://learnabout-electronics.org/Digital/dig51.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundprinzip; Zielschaltung und Lastkapazitäten auf die angegebene Frequenz, Quarzart und den zulässigen Ansteuerpegel auslegen. Entwurfshilfen mit unterschiedlichen Frequenzbereichen. Eine gleiche Frequenz allein bestätigt weder Lastkapazität, Schwingmodus noch zulässige Anregungsleistung des vorhandenen Quarzes.

## Quarz 27 MHz

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Pierce-Oszillator (ST)](https://www.st.com/resource/en/application_note/an2867-guidelines-for-oscillator-design-on-stm8afals-and-stm32-mcusmpus-stmicroelectronics.pdf) — st.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [Quarzoszillator (Grundschaltung)](https://www.allaboutcircuits.com/textbook/designing-analog-chips/timers-and-oscillators/crystal-oscillators/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Quarzoszillatoren mit diskreter und IC-Verstärkung](https://www.electronics-tutorials.ws/oscillator/crystal.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [AN826: Quarzoszillator und Lastkapazität](https://ww1.microchip.com/downloads/en/appnotes/00826a.pdf) — microchip.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
- [AN14518: Quarzoszillator auslegen und messen](https://www.nxp.jp/docs/en/application-note/AN14518.pdf) — nxp.com; Entwurfshilfe; geprüft 2026-10-25.
  Hinweis: Reader-IC-spezifische Beispiele; zulässigen Frequenzbereich und Last des tatsächlichen Oszillatortreibers prüfen.
- [RC- und quarzgesteuerte Taktgeneratoren](https://learnabout-electronics.org/Digital/dig51.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundprinzip; Zielschaltung und Lastkapazitäten auf die angegebene Frequenz, Quarzart und den zulässigen Ansteuerpegel auslegen. Entwurfshilfen mit unterschiedlichen Frequenzbereichen. Eine gleiche Frequenz allein bestätigt weder Lastkapazität, Schwingmodus noch zulässige Anregungsleistung des vorhandenen Quarzes.

## L78S12CV

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Regler-Grundbeschaltung (Hersteller) (PDF S. 7)](../Datenblaetter/Spannungsregler/L78S12CV_ST.pdf#page=7) · [Online-Original](https://www.allelcoelec.jp/datasheets.84/L78S12CV.pdf) — allelcoelec.jp; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [78xx/79xx-Regler und symmetrische Versorgung](https://learnabout-electronics.org/PSU/psu23.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Positive und negative lineare Spannungsregler](https://circuitdigest.com/electronic-circuits/voltage-regulators) — circuitdigest.com; Grundschaltung; geprüft 2026-10-25.
- [78xx-Grundschaltung und Abblockung](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/7805-7812-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.
- [Lineare Netzteile und Regler-Grundschaltung](https://www.electronics-tutorials.ws/supplies/power-supplies-for-beginners-part-3.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Im Familien-Datenblatt die Werte, Pinfolge und Beschaltung der angegebenen Ausgangsspannung/Variante verwenden. Regler-Grundschaltung: Ausgangsspannung, Stromklasse (78L/78/78S), Pinbelegung, Mindestlast und vom Hersteller geforderte Kondensatoren des vorhandenen Typs verwenden.

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

## L78S05CV

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Regler-Grundbeschaltung (Hersteller) (PDF S. 7)](../Datenblaetter/Spannungsregler/L78S12CV_ST.pdf#page=7) · [Online-Original](https://www.allelcoelec.jp/datasheets.84/L78S12CV.pdf) — allelcoelec.jp; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [78xx/79xx-Regler und symmetrische Versorgung](https://learnabout-electronics.org/PSU/psu23.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Positive und negative lineare Spannungsregler](https://circuitdigest.com/electronic-circuits/voltage-regulators) — circuitdigest.com; Grundschaltung; geprüft 2026-10-25.
- [78xx-Grundschaltung und Abblockung](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/7805-7812-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.
- [Lineare Netzteile und Regler-Grundschaltung](https://www.electronics-tutorials.ws/supplies/power-supplies-for-beginners-part-3.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Im Familien-Datenblatt die Werte, Pinfolge und Beschaltung der angegebenen Ausgangsspannung/Variante verwenden. Regler-Grundschaltung: Ausgangsspannung, Stromklasse (78L/78/78S), Pinbelegung, Mindestlast und vom Hersteller geforderte Kondensatoren des vorhandenen Typs verwenden.

## TS7805

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Regler-Grundbeschaltung (Hersteller) (PDF S. 1)](../Datenblaetter/Spannungsregler/TS7805_TSC_Familie.pdf#page=1) · [Online-Original](https://cdn-reichelt.de/documents/datenblatt/A200/TS7800~TSC.pdf) — cdn-reichelt.de; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [78xx/79xx-Regler und symmetrische Versorgung](https://learnabout-electronics.org/PSU/psu23.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Positive und negative lineare Spannungsregler](https://circuitdigest.com/electronic-circuits/voltage-regulators) — circuitdigest.com; Grundschaltung; geprüft 2026-10-25.
- [78xx-Grundschaltung und Abblockung](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/7805-7812-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.
- [Lineare Netzteile und Regler-Grundschaltung](https://www.electronics-tutorials.ws/supplies/power-supplies-for-beginners-part-3.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Im Familien-Datenblatt die Werte, Pinfolge und Beschaltung der angegebenen Ausgangsspannung/Variante verwenden. Regler-Grundschaltung: Ausgangsspannung, Stromklasse (78L/78/78S), Pinbelegung, Mindestlast und vom Hersteller geforderte Kondensatoren des vorhandenen Typs verwenden.

## UA741CN

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Nichtinvertierender Verstärker (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-6/noninverting-amplifier/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Spannungsfolger (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-6/precision-voltage-follower/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Invertierender/nichtinvertierender Verstärker und Komparator](https://www.renesas.com/en/support/engineer-school/electronic-circuits-03-op-amps-comparator-circuit) — renesas.com; Grundschaltung; geprüft 2026-10-25.
- [OPV-Anwendungen und Schaltungsgrenzen](https://wiki.analog.com/university/courses/electronics/text/chapter-4) — analog.com; Grundschaltung; geprüft 2026-10-25.
- [Laboraufbau: Spannungsfolger und nichtinvertierender Verstärker](https://physicslabs.colorado.edu/courses/phys-3330/lab-guides/lab4/) — physicslabs.colorado.edu; Grundschaltung; geprüft 2026-10-25.
- [OPV-Verstärker mit Gegenkopplung](https://learnabout-electronics.org/Amplifiers/amplifiers66.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundschaltungen: Versorgung, Eingangsspannungsbereich, Ausgangshub und Verstärkerpins an den konkreten OPV anpassen; insbesondere UA741 nicht wie einen Rail-to-Rail-OPV behandeln. OPV-Grundschaltung mit anderen Referenztypen: Versorgung, Eingangs-Gleichtaktbereich und Ausgangshub prüfen. UA741 ist kein für allgemeine 5-V-Einversorgung geeigneter Ersatz für LM358.

## L78S09CV

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Regler-Grundbeschaltung (Hersteller) (PDF S. 7)](../Datenblaetter/Spannungsregler/L78S12CV_ST.pdf#page=7) · [Online-Original](https://www.allelcoelec.jp/datasheets.84/L78S12CV.pdf) — allelcoelec.jp; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [78xx/79xx-Regler und symmetrische Versorgung](https://learnabout-electronics.org/PSU/psu23.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Positive und negative lineare Spannungsregler](https://circuitdigest.com/electronic-circuits/voltage-regulators) — circuitdigest.com; Grundschaltung; geprüft 2026-10-25.
- [78xx-Grundschaltung und Abblockung](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/7805-7812-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.
- [Lineare Netzteile und Regler-Grundschaltung](https://www.electronics-tutorials.ws/supplies/power-supplies-for-beginners-part-3.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Im Familien-Datenblatt die Werte, Pinfolge und Beschaltung der angegebenen Ausgangsspannung/Variante verwenden. Regler-Grundschaltung: Ausgangsspannung, Stromklasse (78L/78/78S), Pinbelegung, Mindestlast und vom Hersteller geforderte Kondensatoren des vorhandenen Typs verwenden.

## KA7809

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Regler-Grundbeschaltung (Hersteller) (PDF S. 21)](../Datenblaetter/Spannungsregler/KA7809_Fairchild.pdf#page=21) · [Online-Original](https://www.haje.nl/pub/pdf/electronica/halfgeleiders/ka78xx.pdf) — haje.nl; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [78xx/79xx-Regler und symmetrische Versorgung](https://learnabout-electronics.org/PSU/psu23.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Positive und negative lineare Spannungsregler](https://circuitdigest.com/electronic-circuits/voltage-regulators) — circuitdigest.com; Grundschaltung; geprüft 2026-10-25.
- [78xx-Grundschaltung und Abblockung](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/7805-7812-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.
- [Lineare Netzteile und Regler-Grundschaltung](https://www.electronics-tutorials.ws/supplies/power-supplies-for-beginners-part-3.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Im Familien-Datenblatt die Werte, Pinfolge und Beschaltung der angegebenen Ausgangsspannung/Variante verwenden. Regler-Grundschaltung: Ausgangsspannung, Stromklasse (78L/78/78S), Pinbelegung, Mindestlast und vom Hersteller geforderte Kondensatoren des vorhandenen Typs verwenden.

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

## CD74HCT85E

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [4-Bit-Vergleich/Kaskadierung (Grundschaltung)](https://www.electronics-tutorials.ws/combination/comb_8.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Binärvergleich und kaskadierte Komparatoren](https://www.learnabout-electronics.org/Digital/dig43.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [7485: 4-/8-Bit-Vergleich im virtuellen Labor](https://dec-iitkgp.vlabs.ac.in/exp/digital-comparators/theory.html) — dec-iitkgp.vlabs.ac.in; Grundschaltung; geprüft 2026-10-25.
- [7485 mit Schaltern und Ergebnisanzeige](https://faculty-web.msoe.edu/tritt/JohnDeere/jddig02.html) — faculty-web.msoe.edu; Grundschaltung; geprüft 2026-10-25.
- [7485-Kaskadierung zum 24-Bit-Vergleicher](https://tams.informatik.uni-hamburg.de/applets/hades/webdemos/20-arithmetic/45-compare/7485-demo_print.html) — tams.informatik.uni-hamburg.de; Simulationsbeispiel; geprüft 2026-10-25.

Bei Grundschaltungen Eingangs-/Ausgangspolarität, Anzahl der Kanäle, Versorgung und Pinfolge für die dokumentierte Logikfamilie abgleichen. 7485-Beispiele zeigen das Vergleichsprinzip. CD4063 und HCT85 unterscheiden sich in Pinfolge und elektrischen Kennwerten; Kaskadiereingänge typgerecht setzen.

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

## BC556B

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC557B

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC558B

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## MPS2907A

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC547C

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC546B

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC548B

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BDX54C

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## IRFZ44N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [N-Kanal-Lastschalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [MOSFET-Schalter mit isoliertem Eingang](https://learnabout-electronics.org/Semiconductors/fet_06a.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
  Hinweis: N-Kanal-Beispiel; für P-Kanal ist eine andere Topologie und Gatepolarität nötig.
- [Magnetspule mit N-Kanal-Logic-Level-MOSFET](https://learn.adafruit.com/circuitpython-ble-remote-control-on-off/solenoid-mosfet) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
  Hinweis: Beispiel verwendet IRLB8721. Andere MOSFETs benötigen gegebenenfalls eine höhere Gate-Spannung.
- [PWM-Lastschalter mit N-Kanal-MOSFET-Modul](https://learn.sparkfun.com/tutorials/fading-with-the-mosfet-power-switch-and-buck-regulator/all) — sparkfun.com; Modulbeispiel; geprüft 2026-10-25.
  Hinweis: Low-Side-Modul mit anderem MOSFET; kein Ersatz für die Gate-Auslegung des vorhandenen Typs.

Erforderliche Gate-Spannung aus RDS(on)-Spezifikation bestimmen; IRF540/IRFZ44 nicht als Logic-Level-Typen behandeln. Polarität und Pinout des konkreten MOSFETs berücksichtigen. Grundschaltungen verwenden teils andere MOSFETs. IRF-Typen nicht allein wegen der Schwellspannung als bei 5 V voll durchgesteuert ansehen; RDS(on) bei der tatsächlich verfügbaren Gatespannung prüfen. N-Kanal-Beispiele sind keine direkte Beschaltung für P-Kanal-Typen.

## IRF510N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [N-Kanal-Lastschalter (Grundschaltung, nur IRF510-Referenz)](https://www.electronics-tutorials.ws/transistor/tran_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [MOSFET-Schalter mit isoliertem Eingang](https://learnabout-electronics.org/Semiconductors/fet_06a.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
  Hinweis: N-Kanal-Beispiel; für P-Kanal ist eine andere Topologie und Gatepolarität nötig.
- [Magnetspule mit N-Kanal-Logic-Level-MOSFET](https://learn.adafruit.com/circuitpython-ble-remote-control-on-off/solenoid-mosfet) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
  Hinweis: Beispiel verwendet IRLB8721. Andere MOSFETs benötigen gegebenenfalls eine höhere Gate-Spannung.
- [PWM-Lastschalter mit N-Kanal-MOSFET-Modul](https://learn.sparkfun.com/tutorials/fading-with-the-mosfet-power-switch-and-buck-regulator/all) — sparkfun.com; Modulbeispiel; geprüft 2026-10-25.
  Hinweis: Low-Side-Modul mit anderem MOSFET; kein Ersatz für die Gate-Auslegung des vorhandenen Typs.

Erforderliche Gate-Spannung aus RDS(on)-Spezifikation bestimmen; IRF540/IRFZ44 nicht als Logic-Level-Typen behandeln. Polarität und Pinout des konkreten MOSFETs berücksichtigen. Grundschaltungen verwenden teils andere MOSFETs. IRF-Typen nicht allein wegen der Schwellspannung als bei 5 V voll durchgesteuert ansehen; RDS(on) bei der tatsächlich verfügbaren Gatespannung prüfen. N-Kanal-Beispiele sind keine direkte Beschaltung für P-Kanal-Typen.

## IRF520N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [N-Kanal-Lastschalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [MOSFET-Schalter mit isoliertem Eingang](https://learnabout-electronics.org/Semiconductors/fet_06a.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
  Hinweis: N-Kanal-Beispiel; für P-Kanal ist eine andere Topologie und Gatepolarität nötig.
- [Magnetspule mit N-Kanal-Logic-Level-MOSFET](https://learn.adafruit.com/circuitpython-ble-remote-control-on-off/solenoid-mosfet) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
  Hinweis: Beispiel verwendet IRLB8721. Andere MOSFETs benötigen gegebenenfalls eine höhere Gate-Spannung.
- [PWM-Lastschalter mit N-Kanal-MOSFET-Modul](https://learn.sparkfun.com/tutorials/fading-with-the-mosfet-power-switch-and-buck-regulator/all) — sparkfun.com; Modulbeispiel; geprüft 2026-10-25.
  Hinweis: Low-Side-Modul mit anderem MOSFET; kein Ersatz für die Gate-Auslegung des vorhandenen Typs.

Erforderliche Gate-Spannung aus RDS(on)-Spezifikation bestimmen; IRF540/IRFZ44 nicht als Logic-Level-Typen behandeln. Polarität und Pinout des konkreten MOSFETs berücksichtigen. Grundschaltungen verwenden teils andere MOSFETs. IRF-Typen nicht allein wegen der Schwellspannung als bei 5 V voll durchgesteuert ansehen; RDS(on) bei der tatsächlich verfügbaren Gatespannung prüfen. N-Kanal-Beispiele sind keine direkte Beschaltung für P-Kanal-Typen.

## IRF530N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [N-Kanal-Lastschalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [MOSFET-Schalter mit isoliertem Eingang](https://learnabout-electronics.org/Semiconductors/fet_06a.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
  Hinweis: N-Kanal-Beispiel; für P-Kanal ist eine andere Topologie und Gatepolarität nötig.
- [Magnetspule mit N-Kanal-Logic-Level-MOSFET](https://learn.adafruit.com/circuitpython-ble-remote-control-on-off/solenoid-mosfet) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
  Hinweis: Beispiel verwendet IRLB8721. Andere MOSFETs benötigen gegebenenfalls eine höhere Gate-Spannung.
- [PWM-Lastschalter mit N-Kanal-MOSFET-Modul](https://learn.sparkfun.com/tutorials/fading-with-the-mosfet-power-switch-and-buck-regulator/all) — sparkfun.com; Modulbeispiel; geprüft 2026-10-25.
  Hinweis: Low-Side-Modul mit anderem MOSFET; kein Ersatz für die Gate-Auslegung des vorhandenen Typs.

Erforderliche Gate-Spannung aus RDS(on)-Spezifikation bestimmen; IRF540/IRFZ44 nicht als Logic-Level-Typen behandeln. Polarität und Pinout des konkreten MOSFETs berücksichtigen. Grundschaltungen verwenden teils andere MOSFETs. IRF-Typen nicht allein wegen der Schwellspannung als bei 5 V voll durchgesteuert ansehen; RDS(on) bei der tatsächlich verfügbaren Gatespannung prüfen. N-Kanal-Beispiele sind keine direkte Beschaltung für P-Kanal-Typen.

## IRF540N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [N-Kanal-Lastschalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [MOSFET-Schalter mit isoliertem Eingang](https://learnabout-electronics.org/Semiconductors/fet_06a.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
  Hinweis: N-Kanal-Beispiel; für P-Kanal ist eine andere Topologie und Gatepolarität nötig.
- [Magnetspule mit N-Kanal-Logic-Level-MOSFET](https://learn.adafruit.com/circuitpython-ble-remote-control-on-off/solenoid-mosfet) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
  Hinweis: Beispiel verwendet IRLB8721. Andere MOSFETs benötigen gegebenenfalls eine höhere Gate-Spannung.
- [PWM-Lastschalter mit N-Kanal-MOSFET-Modul](https://learn.sparkfun.com/tutorials/fading-with-the-mosfet-power-switch-and-buck-regulator/all) — sparkfun.com; Modulbeispiel; geprüft 2026-10-25.
  Hinweis: Low-Side-Modul mit anderem MOSFET; kein Ersatz für die Gate-Auslegung des vorhandenen Typs.

Erforderliche Gate-Spannung aus RDS(on)-Spezifikation bestimmen; IRF540/IRFZ44 nicht als Logic-Level-Typen behandeln. Polarität und Pinout des konkreten MOSFETs berücksichtigen. Grundschaltungen verwenden teils andere MOSFETs. IRF-Typen nicht allein wegen der Schwellspannung als bei 5 V voll durchgesteuert ansehen; RDS(on) bei der tatsächlich verfügbaren Gatespannung prüfen. N-Kanal-Beispiele sind keine direkte Beschaltung für P-Kanal-Typen.

## IRF640N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [N-Kanal-Lastschalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [MOSFET-Schalter mit isoliertem Eingang](https://learnabout-electronics.org/Semiconductors/fet_06a.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
  Hinweis: N-Kanal-Beispiel; für P-Kanal ist eine andere Topologie und Gatepolarität nötig.
- [Magnetspule mit N-Kanal-Logic-Level-MOSFET](https://learn.adafruit.com/circuitpython-ble-remote-control-on-off/solenoid-mosfet) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
  Hinweis: Beispiel verwendet IRLB8721. Andere MOSFETs benötigen gegebenenfalls eine höhere Gate-Spannung.
- [PWM-Lastschalter mit N-Kanal-MOSFET-Modul](https://learn.sparkfun.com/tutorials/fading-with-the-mosfet-power-switch-and-buck-regulator/all) — sparkfun.com; Modulbeispiel; geprüft 2026-10-25.
  Hinweis: Low-Side-Modul mit anderem MOSFET; kein Ersatz für die Gate-Auslegung des vorhandenen Typs.

Erforderliche Gate-Spannung aus RDS(on)-Spezifikation bestimmen; IRF540/IRFZ44 nicht als Logic-Level-Typen behandeln. Polarität und Pinout des konkreten MOSFETs berücksichtigen. Grundschaltungen verwenden teils andere MOSFETs. IRF-Typen nicht allein wegen der Schwellspannung als bei 5 V voll durchgesteuert ansehen; RDS(on) bei der tatsächlich verfügbaren Gatespannung prüfen. N-Kanal-Beispiele sind keine direkte Beschaltung für P-Kanal-Typen.

## IRF740

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [N-Kanal-Lastschalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [MOSFET-Schalter mit isoliertem Eingang](https://learnabout-electronics.org/Semiconductors/fet_06a.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
  Hinweis: N-Kanal-Beispiel; für P-Kanal ist eine andere Topologie und Gatepolarität nötig.
- [Magnetspule mit N-Kanal-Logic-Level-MOSFET](https://learn.adafruit.com/circuitpython-ble-remote-control-on-off/solenoid-mosfet) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
  Hinweis: Beispiel verwendet IRLB8721. Andere MOSFETs benötigen gegebenenfalls eine höhere Gate-Spannung.
- [PWM-Lastschalter mit N-Kanal-MOSFET-Modul](https://learn.sparkfun.com/tutorials/fading-with-the-mosfet-power-switch-and-buck-regulator/all) — sparkfun.com; Modulbeispiel; geprüft 2026-10-25.
  Hinweis: Low-Side-Modul mit anderem MOSFET; kein Ersatz für die Gate-Auslegung des vorhandenen Typs.

Erforderliche Gate-Spannung aus RDS(on)-Spezifikation bestimmen; IRF540/IRFZ44 nicht als Logic-Level-Typen behandeln. Polarität und Pinout des konkreten MOSFETs berücksichtigen. Grundschaltungen verwenden teils andere MOSFETs. IRF-Typen nicht allein wegen der Schwellspannung als bei 5 V voll durchgesteuert ansehen; RDS(on) bei der tatsächlich verfügbaren Gatespannung prüfen. N-Kanal-Beispiele sind keine direkte Beschaltung für P-Kanal-Typen.

## IRF840

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [N-Kanal-Lastschalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [MOSFET-Schalter mit isoliertem Eingang](https://learnabout-electronics.org/Semiconductors/fet_06a.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
  Hinweis: N-Kanal-Beispiel; für P-Kanal ist eine andere Topologie und Gatepolarität nötig.
- [Magnetspule mit N-Kanal-Logic-Level-MOSFET](https://learn.adafruit.com/circuitpython-ble-remote-control-on-off/solenoid-mosfet) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
  Hinweis: Beispiel verwendet IRLB8721. Andere MOSFETs benötigen gegebenenfalls eine höhere Gate-Spannung.
- [PWM-Lastschalter mit N-Kanal-MOSFET-Modul](https://learn.sparkfun.com/tutorials/fading-with-the-mosfet-power-switch-and-buck-regulator/all) — sparkfun.com; Modulbeispiel; geprüft 2026-10-25.
  Hinweis: Low-Side-Modul mit anderem MOSFET; kein Ersatz für die Gate-Auslegung des vorhandenen Typs.

Erforderliche Gate-Spannung aus RDS(on)-Spezifikation bestimmen; IRF540/IRFZ44 nicht als Logic-Level-Typen behandeln. Polarität und Pinout des konkreten MOSFETs berücksichtigen. Grundschaltungen verwenden teils andere MOSFETs. IRF-Typen nicht allein wegen der Schwellspannung als bei 5 V voll durchgesteuert ansehen; RDS(on) bei der tatsächlich verfügbaren Gatespannung prüfen. N-Kanal-Beispiele sind keine direkte Beschaltung für P-Kanal-Typen.

## IRF3205

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [N-Kanal-Lastschalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [MOSFET-Schalter mit isoliertem Eingang](https://learnabout-electronics.org/Semiconductors/fet_06a.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
  Hinweis: N-Kanal-Beispiel; für P-Kanal ist eine andere Topologie und Gatepolarität nötig.
- [Magnetspule mit N-Kanal-Logic-Level-MOSFET](https://learn.adafruit.com/circuitpython-ble-remote-control-on-off/solenoid-mosfet) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
  Hinweis: Beispiel verwendet IRLB8721. Andere MOSFETs benötigen gegebenenfalls eine höhere Gate-Spannung.
- [PWM-Lastschalter mit N-Kanal-MOSFET-Modul](https://learn.sparkfun.com/tutorials/fading-with-the-mosfet-power-switch-and-buck-regulator/all) — sparkfun.com; Modulbeispiel; geprüft 2026-10-25.
  Hinweis: Low-Side-Modul mit anderem MOSFET; kein Ersatz für die Gate-Auslegung des vorhandenen Typs.

Erforderliche Gate-Spannung aus RDS(on)-Spezifikation bestimmen; IRF540/IRFZ44 nicht als Logic-Level-Typen behandeln. Polarität und Pinout des konkreten MOSFETs berücksichtigen. Grundschaltungen verwenden teils andere MOSFETs. IRF-Typen nicht allein wegen der Schwellspannung als bei 5 V voll durchgesteuert ansehen; RDS(on) bei der tatsächlich verfügbaren Gatespannung prüfen. N-Kanal-Beispiele sind keine direkte Beschaltung für P-Kanal-Typen.

## IRF9540N

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [P-Kanal-High-Side (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [MOSFET-Schalter mit isoliertem Eingang](https://learnabout-electronics.org/Semiconductors/fet_06a.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
  Hinweis: Den Abschnitt „The High Side MOSFET Switch“ und die P-Kanal-Schaltung verwenden.
- [P-Kanal-High-Side-Schalter mit Schaltplan](https://thewanderingengineer.com/2016/11/14/p-channel-mosfet-high-side-switch/) — thewanderingengineer.com; Grundschaltung; geprüft 2026-10-25.
- [P-Kanal-Lastschalter mit vorgeschalteter Gate-Ansteuerung](https://developer.wildernesslabs.co/Hardware/Tutorials/Electronics/Part7/MOSFET_High-Side_Usage/) — developer.wildernesslabs.co; Grundschaltung; geprüft 2026-10-25.
- [P-Kanal-Lastschalter und High-Side-Beschaltung](https://fscdn.rohm.com/en/products/databook/applinote/discrete/transistor/mosfet/p-channel_power_mosfets_selection_guide_an-e.pdf) — fscdn.rohm.com; Hersteller-Grundschaltung; geprüft 2026-10-25.

P-Kanal-MOSFET: Source an die positive Versorgung; die Gatespannung wird relativ zu Source betrachtet. VGS-Grenze, erforderliche negative Gate-Ansteuerung und RDS(on) des konkreten Typs beachten. Quellen verwenden teilweise andere P-Kanal-Typen; keine unveränderte N-Kanal-Beschaltung übernehmen.

## IRF9530PBF

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [P-Kanal-High-Side (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [MOSFET-Schalter mit isoliertem Eingang](https://learnabout-electronics.org/Semiconductors/fet_06a.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
  Hinweis: Den Abschnitt „The High Side MOSFET Switch“ und die P-Kanal-Schaltung verwenden.
- [P-Kanal-High-Side-Schalter mit Schaltplan](https://thewanderingengineer.com/2016/11/14/p-channel-mosfet-high-side-switch/) — thewanderingengineer.com; Grundschaltung; geprüft 2026-10-25.
- [P-Kanal-Lastschalter mit vorgeschalteter Gate-Ansteuerung](https://developer.wildernesslabs.co/Hardware/Tutorials/Electronics/Part7/MOSFET_High-Side_Usage/) — developer.wildernesslabs.co; Grundschaltung; geprüft 2026-10-25.
- [P-Kanal-Lastschalter und High-Side-Beschaltung](https://fscdn.rohm.com/en/products/databook/applinote/discrete/transistor/mosfet/p-channel_power_mosfets_selection_guide_an-e.pdf) — fscdn.rohm.com; Hersteller-Grundschaltung; geprüft 2026-10-25.

P-Kanal-MOSFET: Source an die positive Versorgung; die Gatespannung wird relativ zu Source betrachtet. VGS-Grenze, erforderliche negative Gate-Ansteuerung und RDS(on) des konkreten Typs beachten. Quellen verwenden teilweise andere P-Kanal-Typen; keine unveränderte N-Kanal-Beschaltung übernehmen.

## IRF520NPBF

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [N-Kanal-Lastschalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [MOSFET-Schalter mit isoliertem Eingang](https://learnabout-electronics.org/Semiconductors/fet_06a.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
  Hinweis: N-Kanal-Beispiel; für P-Kanal ist eine andere Topologie und Gatepolarität nötig.
- [Magnetspule mit N-Kanal-Logic-Level-MOSFET](https://learn.adafruit.com/circuitpython-ble-remote-control-on-off/solenoid-mosfet) — adafruit.com; Grundschaltung; geprüft 2026-10-25.
  Hinweis: Beispiel verwendet IRLB8721. Andere MOSFETs benötigen gegebenenfalls eine höhere Gate-Spannung.
- [PWM-Lastschalter mit N-Kanal-MOSFET-Modul](https://learn.sparkfun.com/tutorials/fading-with-the-mosfet-power-switch-and-buck-regulator/all) — sparkfun.com; Modulbeispiel; geprüft 2026-10-25.
  Hinweis: Low-Side-Modul mit anderem MOSFET; kein Ersatz für die Gate-Auslegung des vorhandenen Typs.

Erforderliche Gate-Spannung aus RDS(on)-Spezifikation bestimmen; IRF540/IRFZ44 nicht als Logic-Level-Typen behandeln. Polarität und Pinout des konkreten MOSFETs berücksichtigen. Grundschaltungen verwenden teils andere MOSFETs. IRF-Typen nicht allein wegen der Schwellspannung als bei 5 V voll durchgesteuert ansehen; RDS(on) bei der tatsächlich verfügbaren Gatespannung prüfen. N-Kanal-Beispiele sind keine direkte Beschaltung für P-Kanal-Typen.

## SN74LS688N

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Freigabe / Gleichheitsvergleich (Funktionstabelle, TI) (PDF S. 2)](../Datenblaetter/SN7xxx/SN74LS688N_TI.pdf#page=2) · [Online-Original](https://www.ti.com/lit/ds/symlink/sn74ls688.pdf) — ti.com; Funktionstabelle / Referenz; geprüft 2026-10-23.
- [74LS688 zur Byteprüfung in einem EPROM-Kopierer](https://github.com/yoyoberenguer/EPROM) — github.com; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [74LS688 zur Adressauswahl einer TI-99-IDE-Karte](https://www.unige.ch/medecine/nouspikel/ti99/ide.htm) — unige.ch; Konkretes Schaltungsbeispiel; geprüft 2026-10-25.
- [Speicheradressierung mit 8-Bit-Gleichheitskomparator](https://courses.minia.edu.eg/Attach/993412-%20Memory.pdf) — courses.minia.edu.eg; Grundschaltung; geprüft 2026-10-25.
- [74HC688 als Gleichheitsprüfer und Adressdecoder](https://nucleus.iaea.org/sites/nuclear-instrumentation/Shared%20Documents/Digital%20Electronics/DigitalText.pdf) — nucleus.iaea.org; Grundschaltung; geprüft 2026-10-25.
- [74LS245 als Buspuffer in einer 8255-Schnittstelle](https://tiij.org/issues/issues/4_1/4_1s.html) — tiij.org; Grundschaltung; geprüft 2026-10-25.

TI-Funktionstabelle als Referenz, keine Anwendungsschaltung. /G=0 aktiviert, /EQ=0 bedeutet P=Q; Push-Pull-Ausgang. Gleichheitskomparator mit aktivem Low-Ergebnis; LS688 führt keinen Größer-/Kleiner-Vergleich aus. Die HC688-Grundschaltung erfordert einen Abgleich der Logikpegel.

## ZD 2,7

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zener-Shuntregler und Spannungsreferenz](https://learnabout-electronics.org/Semiconductors/diodes_24.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Vorwiderstand](https://www.electronics-tutorials.ws/diode/diode_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler im Batterieexperiment](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/voltage-regulator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Last und Vorwiderstand](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/zener-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.

Zenerfunktion und Nennspannung laut Nutzerangabe bekannt; Typreihe, Hersteller, Gehäuse und passende Referenzschaltung noch nicht bestätigt. Zener-Grundschaltung, kein typgleicher Aufbau. Vorwiderstand aus Eingangsspannung, Zenerspannung, Mindeststrom und Last berechnen; zulässige Verlustleistung prüfen. Bei Zenerspannungen über 5 V ist mit einer 5-V-Versorgung keine Stabilisierung auf die Nennspannung möglich.

## ZD 3,3

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zener-Shuntregler und Spannungsreferenz](https://learnabout-electronics.org/Semiconductors/diodes_24.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Vorwiderstand](https://www.electronics-tutorials.ws/diode/diode_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler im Batterieexperiment](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/voltage-regulator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Last und Vorwiderstand](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/zener-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.

Zenerfunktion und Nennspannung laut Nutzerangabe bekannt; Typreihe, Hersteller, Gehäuse und passende Referenzschaltung noch nicht bestätigt. Zener-Grundschaltung, kein typgleicher Aufbau. Vorwiderstand aus Eingangsspannung, Zenerspannung, Mindeststrom und Last berechnen; zulässige Verlustleistung prüfen. Bei Zenerspannungen über 5 V ist mit einer 5-V-Versorgung keine Stabilisierung auf die Nennspannung möglich.

## ZD 3,9

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zener-Shuntregler und Spannungsreferenz](https://learnabout-electronics.org/Semiconductors/diodes_24.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Vorwiderstand](https://www.electronics-tutorials.ws/diode/diode_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler im Batterieexperiment](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/voltage-regulator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Last und Vorwiderstand](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/zener-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.

Zenerfunktion und Nennspannung laut Nutzerangabe bekannt; Typreihe, Hersteller, Gehäuse und passende Referenzschaltung noch nicht bestätigt. Zener-Grundschaltung, kein typgleicher Aufbau. Vorwiderstand aus Eingangsspannung, Zenerspannung, Mindeststrom und Last berechnen; zulässige Verlustleistung prüfen. Bei Zenerspannungen über 5 V ist mit einer 5-V-Versorgung keine Stabilisierung auf die Nennspannung möglich.

## ZD 5,6

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zener-Shuntregler und Spannungsreferenz](https://learnabout-electronics.org/Semiconductors/diodes_24.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Vorwiderstand](https://www.electronics-tutorials.ws/diode/diode_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler im Batterieexperiment](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/voltage-regulator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Last und Vorwiderstand](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/zener-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.

Zenerfunktion und Nennspannung laut Nutzerangabe bekannt; Typreihe, Hersteller, Gehäuse und passende Referenzschaltung noch nicht bestätigt. Zener-Grundschaltung, kein typgleicher Aufbau. Vorwiderstand aus Eingangsspannung, Zenerspannung, Mindeststrom und Last berechnen; zulässige Verlustleistung prüfen. Bei Zenerspannungen über 5 V ist mit einer 5-V-Versorgung keine Stabilisierung auf die Nennspannung möglich.

## ZD 8,2

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zener-Shuntregler und Spannungsreferenz](https://learnabout-electronics.org/Semiconductors/diodes_24.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Vorwiderstand](https://www.electronics-tutorials.ws/diode/diode_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler im Batterieexperiment](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/voltage-regulator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Last und Vorwiderstand](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/zener-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.

Zenerfunktion und Nennspannung laut Nutzerangabe bekannt; Typreihe, Hersteller, Gehäuse und passende Referenzschaltung noch nicht bestätigt. Zener-Grundschaltung, kein typgleicher Aufbau. Vorwiderstand aus Eingangsspannung, Zenerspannung, Mindeststrom und Last berechnen; zulässige Verlustleistung prüfen. Bei Zenerspannungen über 5 V ist mit einer 5-V-Versorgung keine Stabilisierung auf die Nennspannung möglich.

## ZD 10

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zener-Shuntregler und Spannungsreferenz](https://learnabout-electronics.org/Semiconductors/diodes_24.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Vorwiderstand](https://www.electronics-tutorials.ws/diode/diode_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler im Batterieexperiment](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/voltage-regulator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Last und Vorwiderstand](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/zener-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.

Zenerfunktion und Nennspannung laut Nutzerangabe bekannt; Typreihe, Hersteller, Gehäuse und passende Referenzschaltung noch nicht bestätigt. Zener-Grundschaltung, kein typgleicher Aufbau. Vorwiderstand aus Eingangsspannung, Zenerspannung, Mindeststrom und Last berechnen; zulässige Verlustleistung prüfen. Bei Zenerspannungen über 5 V ist mit einer 5-V-Versorgung keine Stabilisierung auf die Nennspannung möglich.

## ZD 12

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zener-Shuntregler und Spannungsreferenz](https://learnabout-electronics.org/Semiconductors/diodes_24.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Vorwiderstand](https://www.electronics-tutorials.ws/diode/diode_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler im Batterieexperiment](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/voltage-regulator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Last und Vorwiderstand](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/zener-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.

Zenerfunktion und Nennspannung laut Nutzerangabe bekannt; Typreihe, Hersteller, Gehäuse und passende Referenzschaltung noch nicht bestätigt. Zener-Grundschaltung, kein typgleicher Aufbau. Vorwiderstand aus Eingangsspannung, Zenerspannung, Mindeststrom und Last berechnen; zulässige Verlustleistung prüfen. Bei Zenerspannungen über 5 V ist mit einer 5-V-Versorgung keine Stabilisierung auf die Nennspannung möglich.

## ZD 18

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zener-Shuntregler und Spannungsreferenz](https://learnabout-electronics.org/Semiconductors/diodes_24.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Vorwiderstand](https://www.electronics-tutorials.ws/diode/diode_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler im Batterieexperiment](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/voltage-regulator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Last und Vorwiderstand](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/zener-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.

Zenerfunktion und Nennspannung laut Nutzerangabe bekannt; Typreihe, Hersteller, Gehäuse und passende Referenzschaltung noch nicht bestätigt. Zener-Grundschaltung, kein typgleicher Aufbau. Vorwiderstand aus Eingangsspannung, Zenerspannung, Mindeststrom und Last berechnen; zulässige Verlustleistung prüfen. Bei Zenerspannungen über 5 V ist mit einer 5-V-Versorgung keine Stabilisierung auf die Nennspannung möglich.

## ZD 22

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zener-Shuntregler und Spannungsreferenz](https://learnabout-electronics.org/Semiconductors/diodes_24.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Vorwiderstand](https://www.electronics-tutorials.ws/diode/diode_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler im Batterieexperiment](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/voltage-regulator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Last und Vorwiderstand](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/zener-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.

Zenerfunktion und Nennspannung laut Nutzerangabe bekannt; Typreihe, Hersteller, Gehäuse und passende Referenzschaltung noch nicht bestätigt. Zener-Grundschaltung, kein typgleicher Aufbau. Vorwiderstand aus Eingangsspannung, Zenerspannung, Mindeststrom und Last berechnen; zulässige Verlustleistung prüfen. Bei Zenerspannungen über 5 V ist mit einer 5-V-Versorgung keine Stabilisierung auf die Nennspannung möglich.

## ZD 27

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zener-Shuntregler und Spannungsreferenz](https://learnabout-electronics.org/Semiconductors/diodes_24.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Vorwiderstand](https://www.electronics-tutorials.ws/diode/diode_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler im Batterieexperiment](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/voltage-regulator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Last und Vorwiderstand](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/zener-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.

Zenerfunktion und Nennspannung laut Nutzerangabe bekannt; Typreihe, Hersteller, Gehäuse und passende Referenzschaltung noch nicht bestätigt. Zener-Grundschaltung, kein typgleicher Aufbau. Vorwiderstand aus Eingangsspannung, Zenerspannung, Mindeststrom und Last berechnen; zulässige Verlustleistung prüfen. Bei Zenerspannungen über 5 V ist mit einer 5-V-Versorgung keine Stabilisierung auf die Nennspannung möglich.

## ZD 33

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zener-Shuntregler und Spannungsreferenz](https://learnabout-electronics.org/Semiconductors/diodes_24.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Vorwiderstand](https://www.electronics-tutorials.ws/diode/diode_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler im Batterieexperiment](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/voltage-regulator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Last und Vorwiderstand](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/zener-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.

Zenerfunktion und Nennspannung laut Nutzerangabe bekannt; Typreihe, Hersteller, Gehäuse und passende Referenzschaltung noch nicht bestätigt. Zener-Grundschaltung, kein typgleicher Aufbau. Vorwiderstand aus Eingangsspannung, Zenerspannung, Mindeststrom und Last berechnen; zulässige Verlustleistung prüfen. Bei Zenerspannungen über 5 V ist mit einer 5-V-Versorgung keine Stabilisierung auf die Nennspannung möglich.

## ZD 39

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zener-Shuntregler und Spannungsreferenz](https://learnabout-electronics.org/Semiconductors/diodes_24.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Vorwiderstand](https://www.electronics-tutorials.ws/diode/diode_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler im Batterieexperiment](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/voltage-regulator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Last und Vorwiderstand](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/zener-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.

Zenerfunktion und Nennspannung laut Nutzerangabe bekannt; Typreihe, Hersteller, Gehäuse und passende Referenzschaltung noch nicht bestätigt. Zener-Grundschaltung, kein typgleicher Aufbau. Vorwiderstand aus Eingangsspannung, Zenerspannung, Mindeststrom und Last berechnen; zulässige Verlustleistung prüfen. Bei Zenerspannungen über 5 V ist mit einer 5-V-Versorgung keine Stabilisierung auf die Nennspannung möglich.

## ZD 47

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zener-Shuntregler und Spannungsreferenz](https://learnabout-electronics.org/Semiconductors/diodes_24.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Vorwiderstand](https://www.electronics-tutorials.ws/diode/diode_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler im Batterieexperiment](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/voltage-regulator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Last und Vorwiderstand](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/zener-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.

Zenerfunktion und Nennspannung laut Nutzerangabe bekannt; Typreihe, Hersteller, Gehäuse und passende Referenzschaltung noch nicht bestätigt. Zener-Grundschaltung, kein typgleicher Aufbau. Vorwiderstand aus Eingangsspannung, Zenerspannung, Mindeststrom und Last berechnen; zulässige Verlustleistung prüfen. Bei Zenerspannungen über 5 V ist mit einer 5-V-Versorgung keine Stabilisierung auf die Nennspannung möglich.

## ZD 51

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zener-Shuntregler und Spannungsreferenz](https://learnabout-electronics.org/Semiconductors/diodes_24.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Vorwiderstand](https://www.electronics-tutorials.ws/diode/diode_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler im Batterieexperiment](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/voltage-regulator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Last und Vorwiderstand](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/zener-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.

Zenerfunktion und Nennspannung laut Nutzerangabe bekannt; Typreihe, Hersteller, Gehäuse und passende Referenzschaltung noch nicht bestätigt. Zener-Grundschaltung, kein typgleicher Aufbau. Vorwiderstand aus Eingangsspannung, Zenerspannung, Mindeststrom und Last berechnen; zulässige Verlustleistung prüfen. Bei Zenerspannungen über 5 V ist mit einer 5-V-Versorgung keine Stabilisierung auf die Nennspannung möglich.

## ZD 56

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zener-Shuntregler und Spannungsreferenz](https://learnabout-electronics.org/Semiconductors/diodes_24.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Vorwiderstand](https://www.electronics-tutorials.ws/diode/diode_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler im Batterieexperiment](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/voltage-regulator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Last und Vorwiderstand](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/zener-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.

Zenerfunktion und Nennspannung laut Nutzerangabe bekannt; Typreihe, Hersteller, Gehäuse und passende Referenzschaltung noch nicht bestätigt. Zener-Grundschaltung, kein typgleicher Aufbau. Vorwiderstand aus Eingangsspannung, Zenerspannung, Mindeststrom und Last berechnen; zulässige Verlustleistung prüfen. Bei Zenerspannungen über 5 V ist mit einer 5-V-Versorgung keine Stabilisierung auf die Nennspannung möglich.

## ZD 75

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zener-Shuntregler und Spannungsreferenz](https://learnabout-electronics.org/Semiconductors/diodes_24.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Vorwiderstand](https://www.electronics-tutorials.ws/diode/diode_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler im Batterieexperiment](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/voltage-regulator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Last und Vorwiderstand](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/zener-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.

Zenerfunktion und Nennspannung laut Nutzerangabe bekannt; Typreihe, Hersteller, Gehäuse und passende Referenzschaltung noch nicht bestätigt. Zener-Grundschaltung, kein typgleicher Aufbau. Vorwiderstand aus Eingangsspannung, Zenerspannung, Mindeststrom und Last berechnen; zulässige Verlustleistung prüfen. Bei Zenerspannungen über 5 V ist mit einer 5-V-Versorgung keine Stabilisierung auf die Nennspannung möglich.

## BC141

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC161

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC559

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC560

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC639

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC640

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC879

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Darlington-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC238B

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## KSP44

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BD135-10

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## 2N2222A

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

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

## 1N5349B

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zener-Shuntregler und Spannungsreferenz](https://learnabout-electronics.org/Semiconductors/diodes_24.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Vorwiderstand](https://www.electronics-tutorials.ws/diode/diode_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler im Batterieexperiment](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/voltage-regulator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Last und Vorwiderstand](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/zener-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.

Zener-Grundschaltung, kein typgleicher Aufbau. Vorwiderstand aus Eingangsspannung, Zenerspannung, Mindeststrom und Last berechnen; zulässige Verlustleistung prüfen. Bei Zenerspannungen über 5 V ist mit einer 5-V-Versorgung keine Stabilisierung auf die Nennspannung möglich.

## 1N5359B

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zener-Shuntregler und Spannungsreferenz](https://learnabout-electronics.org/Semiconductors/diodes_24.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Vorwiderstand](https://www.electronics-tutorials.ws/diode/diode_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler im Batterieexperiment](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/voltage-regulator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Last und Vorwiderstand](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/zener-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.

Zener-Grundschaltung, kein typgleicher Aufbau. Vorwiderstand aus Eingangsspannung, Zenerspannung, Mindeststrom und Last berechnen; zulässige Verlustleistung prüfen. Bei Zenerspannungen über 5 V ist mit einer 5-V-Versorgung keine Stabilisierung auf die Nennspannung möglich.

## 1N5339B

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zener-Shuntregler und Spannungsreferenz](https://learnabout-electronics.org/Semiconductors/diodes_24.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Vorwiderstand](https://www.electronics-tutorials.ws/diode/diode_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler im Batterieexperiment](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/voltage-regulator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Last und Vorwiderstand](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/zener-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.

Zener-Grundschaltung, kein typgleicher Aufbau. Vorwiderstand aus Eingangsspannung, Zenerspannung, Mindeststrom und Last berechnen; zulässige Verlustleistung prüfen. Bei Zenerspannungen über 5 V ist mit einer 5-V-Versorgung keine Stabilisierung auf die Nennspannung möglich.

## 1N5340B

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zener-Shuntregler und Spannungsreferenz](https://learnabout-electronics.org/Semiconductors/diodes_24.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Vorwiderstand](https://www.electronics-tutorials.ws/diode/diode_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler im Batterieexperiment](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/voltage-regulator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Last und Vorwiderstand](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/zener-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.

Zener-Grundschaltung, kein typgleicher Aufbau. Vorwiderstand aus Eingangsspannung, Zenerspannung, Mindeststrom und Last berechnen; zulässige Verlustleistung prüfen. Bei Zenerspannungen über 5 V ist mit einer 5-V-Versorgung keine Stabilisierung auf die Nennspannung möglich.

## 1N5342B

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zener-Shuntregler und Spannungsreferenz](https://learnabout-electronics.org/Semiconductors/diodes_24.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Vorwiderstand](https://www.electronics-tutorials.ws/diode/diode_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler im Batterieexperiment](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/voltage-regulator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Last und Vorwiderstand](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/zener-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.

Zener-Grundschaltung, kein typgleicher Aufbau. Vorwiderstand aus Eingangsspannung, Zenerspannung, Mindeststrom und Last berechnen; zulässige Verlustleistung prüfen. Bei Zenerspannungen über 5 V ist mit einer 5-V-Versorgung keine Stabilisierung auf die Nennspannung möglich.

## 1N5346B

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Zener-Shuntregler und Spannungsreferenz](https://learnabout-electronics.org/Semiconductors/diodes_24.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Vorwiderstand](https://www.electronics-tutorials.ws/diode/diode_7.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler im Batterieexperiment](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/voltage-regulator/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [Zenerregler mit Last und Vorwiderstand](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/zener-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.

Zener-Grundschaltung, kein typgleicher Aufbau. Vorwiderstand aus Eingangsspannung, Zenerspannung, Mindeststrom und Last berechnen; zulässige Verlustleistung prüfen. Bei Zenerspannungen über 5 V ist mit einer 5-V-Versorgung keine Stabilisierung auf die Nennspannung möglich.

## PC817

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Fotokoppler-Anwendungen (Renesas)](https://www.renesas.com/en/products/interface/optoelectronics/how-photocouplers-optocouplers-are-used) — renesas.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [Fototransistorkoppler: Pegelwandler und Widerstände](https://toshiba.semicon-storage.com/eu/semiconductor/knowledge/e-learning/discrete/chap5/chap5-13.html) — toshiba.semicon-storage.com; Grundschaltung; geprüft 2026-10-25.
- [PC817: isolierter Logikeingang und Lastansteuerung](https://www.learnabout-electronics.org/Semiconductors/opto_52.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Optische Eingangskopplung und Pegelanpassung](https://www.electronics-tutorials.ws/io/input-interfacing-circuits.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [PC817-Modul als Arduino-Eingang](https://mschoeffler.com/2021/04/30/arduino-tutorial-hy-m154-817-pc817-optocoupler-module/) — mschoeffler.com; Modulbeispiel; geprüft 2026-10-25.
  Hinweis: Fertiges Modul mit zusätzlichen Bauteilen; keine direkte Pinbeschaltung des einzelnen Kopplers.

LED-Vorwiderstand, minimalen CTR, Pull-up und Schaltgeschwindigkeit auslegen; PS2501-4 hat vier Kanäle und andere Gehäuseanschlüsse als PC817.

## MCP23S17-E/SP

**0/5 Beispiel-Websites**, 0 Quellen-Websites insgesamt. Weitere passende Beispiele gesucht.

Noch kein belastbares Schaltungsbeispiel zugeordnet.

Neu im Bestand am 02.11.2026 erfasst; noch keine geprüften Schaltungsbeispiele zugeordnet.

**Recherchebedarf:** Etwa fünf unterschiedliche Websites mit passenden Beispielen recherchieren; konkrete IC- bzw. Modulvariante und Anschlussbelegung beachten.

## ATMEGA328P-PU

**0/5 Beispiel-Websites**, 0 Quellen-Websites insgesamt. Weitere passende Beispiele gesucht.

Noch kein belastbares Schaltungsbeispiel zugeordnet.

Neu im Bestand am 02.11.2026 erfasst; noch keine geprüften Schaltungsbeispiele zugeordnet.

**Recherchebedarf:** Etwa fünf unterschiedliche Websites mit passenden Beispielen recherchieren; konkrete IC- bzw. Modulvariante und Anschlussbelegung beachten.

## PCA9685

**0/5 Beispiel-Websites**, 0 Quellen-Websites insgesamt. Weitere passende Beispiele gesucht.

Noch kein belastbares Schaltungsbeispiel zugeordnet.

Neu im Bestand am 02.11.2026 erfasst; noch keine geprüften Schaltungsbeispiele zugeordnet.

**Recherchebedarf:** Etwa fünf unterschiedliche Websites mit passenden Beispielen recherchieren; konkrete IC- bzw. Modulvariante und Anschlussbelegung beachten.
