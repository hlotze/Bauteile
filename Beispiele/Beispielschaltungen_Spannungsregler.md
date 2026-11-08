# Schaltungsbeispiele: Spannungsregler

[Übersicht](README.md) · [Gesamtsammlung](Beispielschaltungen.md) · [Recherchebedarf](Recherchebedarf.md) · [Bestand](../Bauteile.md)

18 Bauteile, 116 Linkzuordnungen. Erweiterungsstand: **25.10.2026**; Prüfdatum jeweils am Link.

Ziel sind etwa **fünf unterschiedliche Websites pro Bauteil**. Gezählt werden Websites mit Schaltungsbeispielen, übertragbaren Grundschaltungen, Modulbeispielen oder Code mit Anschlusszuordnung. Reine Funktions-/Prinzipreferenzen und Entwurfshilfen zählen zusätzlich als Quellen, aber nicht zum Beispielziel. Subdomains und bekannte Länderspiegel zählen zusammen. Mehrere Artikel derselben Website erhöhen die Zahl nicht.

**Grundschaltung** bedeutet: Das Schaltungsprinzip ist übertragbar, der Artikel verwendet gegebenenfalls ein anderes Bauteil. Sie ist keine Bestätigung der Pinbelegung oder Dimensionierung des vorhandenen Typs. **Modulbeispiele** enthalten zusätzliche Komponenten; **Funktionsreferenzen** sind keine vollständigen Nachbauschaltungen. Hinweise stehen direkt beim Bauteil und Link.

Versorgung, Pinfolge, Polarität, Logikfamilie, Freigaben, Taktflanken und Grenzwerte anhand des konkreten Datenblatts prüfen. 74LS benötigt +5 V. Pro IC üblicherweise 100 nF abblocken, Taster für Zähler entprellen. Transistor- und Diodenwerte an Last und Verlustleistung anpassen. Bei Relais gilt die tatsächliche Spulenspannung. TRIAC-Artikel können Netzspannungsschaltungen enthalten.

Pflege: [Beispielschaltungen.json](Beispielschaltungen.json). `python3 scripts/update_examples.py` erzeugt ausschließlich diese Sammlungen. Bestand und Datenbank bleiben unverändert. Bei lokalen PDFs führt „Online-Original“ zur dokumentierten Downloadquelle; neuere Revisionen können andere Seitenzahlen haben.

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

## L78S12CV

**6/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Regler-Grundbeschaltung (Hersteller) (PDF S. 7)](../Datenblaetter/Spannungsregler/L78S12CV_ST.pdf#page=7) · [Online-Original](https://www.allelcoelec.jp/datasheets.84/L78S12CV.pdf) — allelcoelec.jp; Herstellerbeispiel (lokales PDF); geprüft 2026-10-21.
- [Netzteil-Grundschaltungen und Zenerregler](https://electronicsclub.info/powersupplies.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [78xx/79xx-Regler und symmetrische Versorgung](https://learnabout-electronics.org/PSU/psu23.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.
- [Positive und negative lineare Spannungsregler](https://circuitdigest.com/electronic-circuits/voltage-regulators) — circuitdigest.com; Grundschaltung; geprüft 2026-10-25.
- [78xx-Grundschaltung und Abblockung](https://www.electronics-notes.com/articles/analogue_circuits/power-supply-electronics/7805-7812-voltage-regulator.php) — electronics-notes.com; Grundschaltung; geprüft 2026-10-25.
- [Lineare Netzteile und Regler-Grundschaltung](https://www.electronics-tutorials.ws/supplies/power-supplies-for-beginners-part-3.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.

Im Familien-Datenblatt die Werte, Pinfolge und Beschaltung der angegebenen Ausgangsspannung/Variante verwenden. Regler-Grundschaltung: Ausgangsspannung, Stromklasse (78L/78/78S), Pinbelegung, Mindestlast und vom Hersteller geforderte Kondensatoren des vorhandenen Typs verwenden.

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
