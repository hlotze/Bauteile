# Schaltungsbeispiele: Optokoppler

[Übersicht](README.md) · [Gesamtsammlung](Beispielschaltungen.md) · [Recherchebedarf](Recherchebedarf.md) · [Bestand](../Bauteile.md)

1 Bauteile, 5 Linkzuordnungen. Erweiterungsstand: **25.10.2026**; Prüfdatum jeweils am Link.

Ziel sind etwa **fünf unterschiedliche Websites pro Bauteil**. Gezählt werden Websites mit Schaltungsbeispielen, übertragbaren Grundschaltungen, Modulbeispielen oder Code mit Anschlusszuordnung. Reine Funktions-/Prinzipreferenzen und Entwurfshilfen zählen zusätzlich als Quellen, aber nicht zum Beispielziel. Subdomains und bekannte Länderspiegel zählen zusammen. Mehrere Artikel derselben Website erhöhen die Zahl nicht.

**Grundschaltung** bedeutet: Das Schaltungsprinzip ist übertragbar, der Artikel verwendet gegebenenfalls ein anderes Bauteil. Sie ist keine Bestätigung der Pinbelegung oder Dimensionierung des vorhandenen Typs. **Modulbeispiele** enthalten zusätzliche Komponenten; **Funktionsreferenzen** sind keine vollständigen Nachbauschaltungen. Hinweise stehen direkt beim Bauteil und Link.

Versorgung, Pinfolge, Polarität, Logikfamilie, Freigaben, Taktflanken und Grenzwerte anhand des konkreten Datenblatts prüfen. 74LS benötigt +5 V. Pro IC üblicherweise 100 nF abblocken, Taster für Zähler entprellen. Transistor- und Diodenwerte an Last und Verlustleistung anpassen. Bei Relais gilt die tatsächliche Spulenspannung. TRIAC-Artikel können Netzspannungsschaltungen enthalten.

Pflege: [Beispielschaltungen.json](Beispielschaltungen.json). `python3 scripts/update_examples.py` erzeugt ausschließlich diese Sammlungen. Bestand und Datenbank bleiben unverändert. Bei lokalen PDFs führt „Online-Original“ zur dokumentierten Downloadquelle; neuere Revisionen können andere Seitenzahlen haben.

## PC817

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Fotokoppler-Anwendungen (Renesas)](https://www.renesas.com/en/products/interface/optoelectronics/how-photocouplers-optocouplers-are-used) — renesas.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [Fototransistorkoppler: Pegelwandler und Widerstände](https://toshiba.semicon-storage.com/eu/semiconductor/knowledge/e-learning/discrete/chap5/chap5-13.html) — toshiba.semicon-storage.com; Grundschaltung; geprüft 2026-10-25.
- [PC817: isolierter Logikeingang und Lastansteuerung](https://www.learnabout-electronics.org/Semiconductors/opto_52.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Optische Eingangskopplung und Pegelanpassung](https://www.electronics-tutorials.ws/io/input-interfacing-circuits.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [PC817-Modul als Arduino-Eingang](https://mschoeffler.com/2021/04/30/arduino-tutorial-hy-m154-817-pc817-optocoupler-module/) — mschoeffler.com; Modulbeispiel; geprüft 2026-10-25.
  Hinweis: Fertiges Modul mit zusätzlichen Bauteilen; keine direkte Pinbeschaltung des einzelnen Kopplers.

LED-Vorwiderstand, minimalen CTR, Pull-up und Schaltgeschwindigkeit auslegen; PS2501-4 hat vier Kanäle und andere Gehäuseanschlüsse als PC817.
