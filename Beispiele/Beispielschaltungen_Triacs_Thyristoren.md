# Schaltungsbeispiele: Triacs_Thyristoren

[Übersicht](README.md) · [Gesamtsammlung](Beispielschaltungen.md) · [Recherchebedarf](Recherchebedarf.md) · [Bestand](../Bauteile.md)

3 Bauteile, 15 Linkzuordnungen. Erweiterungsstand: **25.10.2026**; Prüfdatum jeweils am Link.

Ziel sind etwa **fünf unterschiedliche Websites pro Bauteil**. Gezählt werden Websites mit Schaltungsbeispielen, übertragbaren Grundschaltungen, Modulbeispielen oder Code mit Anschlusszuordnung. Reine Funktions-/Prinzipreferenzen und Entwurfshilfen zählen zusätzlich als Quellen, aber nicht zum Beispielziel. Subdomains und bekannte Länderspiegel zählen zusammen. Mehrere Artikel derselben Website erhöhen die Zahl nicht.

**Grundschaltung** bedeutet: Das Schaltungsprinzip ist übertragbar, der Artikel verwendet gegebenenfalls ein anderes Bauteil. Sie ist keine Bestätigung der Pinbelegung oder Dimensionierung des vorhandenen Typs. **Modulbeispiele** enthalten zusätzliche Komponenten; **Funktionsreferenzen** sind keine vollständigen Nachbauschaltungen. Hinweise stehen direkt beim Bauteil und Link.

Versorgung, Pinfolge, Polarität, Logikfamilie, Freigaben, Taktflanken und Grenzwerte anhand des konkreten Datenblatts prüfen. 74LS benötigt +5 V. Pro IC üblicherweise 100 nF abblocken, Taster für Zähler entprellen. Transistor- und Diodenwerte an Last und Verlustleistung anpassen. Bei Relais gilt die tatsächliche Spulenspannung. TRIAC-Artikel können Netzspannungsschaltungen enthalten.

Pflege: [Beispielschaltungen.json](Beispielschaltungen.json). `python3 scripts/update_examples.py` erzeugt ausschließlich diese Sammlungen. Bestand und Datenbank bleiben unverändert. Bei lokalen PDFs führt „Online-Original“ zur dokumentierten Downloadquelle; neuere Revisionen können andere Seitenzahlen haben.

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
