# Schaltungsbeispiele: MOSFETs

[Übersicht](README.md) · [Gesamtsammlung](Beispielschaltungen.md) · [Recherchebedarf](Recherchebedarf.md) · [Bestand](../Bauteile.md)

16 Bauteile, 80 Linkzuordnungen. Erweiterungsstand: **25.10.2026**; Prüfdatum jeweils am Link.

Ziel sind etwa **fünf unterschiedliche Websites pro Bauteil**. Gezählt werden Websites mit Schaltungsbeispielen, übertragbaren Grundschaltungen, Modulbeispielen oder Code mit Anschlusszuordnung. Reine Funktions-/Prinzipreferenzen und Entwurfshilfen zählen zusätzlich als Quellen, aber nicht zum Beispielziel. Subdomains und bekannte Länderspiegel zählen zusammen. Mehrere Artikel derselben Website erhöhen die Zahl nicht.

**Grundschaltung** bedeutet: Das Schaltungsprinzip ist übertragbar, der Artikel verwendet gegebenenfalls ein anderes Bauteil. Sie ist keine Bestätigung der Pinbelegung oder Dimensionierung des vorhandenen Typs. **Modulbeispiele** enthalten zusätzliche Komponenten; **Funktionsreferenzen** sind keine vollständigen Nachbauschaltungen. Hinweise stehen direkt beim Bauteil und Link.

Versorgung, Pinfolge, Polarität, Logikfamilie, Freigaben, Taktflanken und Grenzwerte anhand des konkreten Datenblatts prüfen. 74LS benötigt +5 V. Pro IC üblicherweise 100 nF abblocken, Taster für Zähler entprellen. Transistor- und Diodenwerte an Last und Verlustleistung anpassen. Bei Relais gilt die tatsächliche Spulenspannung. TRIAC-Artikel können Netzspannungsschaltungen enthalten.

Pflege: [Beispielschaltungen.json](Beispielschaltungen.json). `python3 scripts/update_examples.py` erzeugt ausschließlich diese Sammlungen. Bestand und Datenbank bleiben unverändert. Bei lokalen PDFs führt „Online-Original“ zur dokumentierten Downloadquelle; neuere Revisionen können andere Seitenzahlen haben.

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
