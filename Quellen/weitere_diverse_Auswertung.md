# Auswertung: weitere diverse ICs und Bauteile

Quelle: [weitere_diverse_ICs.pdf](weitere_diverse_ICs.pdf), drei gescannte Fotoseiten. Visuell ausgewertet am 13.10.2026. Die PDF enthält keine Textschicht. Vergrößerte Ausschnitte wurden zur Prüfung schwacher Aufdrucke verwendet; sie liegen nur temporär außerhalb der images-Verzeichnisse.

26 neue Bezeichnungen wurden erfasst. Die vier bereits vorhandenen diversen Typen MC1488, MC1489, LH6764-20 und COM8126 wurden in dieselbe Rubrik verschoben. Die Rubrik enthält damit 30 eindeutige Einträge.

| Seite | Neu erfasste Bezeichnungen |
| --- | --- |
| 1 | LM324N, LM339AN, LM358, LM311N, NE555, UA78S40PC, L7805CV, L7809CV, L7812CV, L7815CV, L7824CV, L7905CV, KA7909, L7912CV, L293D, L293NE |
| 2 | PCF8574N, PS2501-4 |
| 3 | MAX7219CNG, MAX250CPD, ULN2004A, ULN2004AG, ULN2803A, MPQ2222A, DIP05-1A72-12L, B3CA4.5Z |

## Lesarten und offene Punkte

- Auf Seite 1 befindet sich rechts ein ST-Leistungsbaustein mit Metalllasche und einer Reihe Anschlüsse. Seine Typnummer bleibt trotz Vergrößerung nicht eindeutig lesbar. Er wurde nicht mit einer geratenen Typnummer aufgenommen.
- LM358 und NE555 sind als Grundtypen lesbar; zusätzliche Suffixe werden nicht erfunden.
- L293NE ist auf mehreren TI-Bausteinen lesbar. L293D bleibt als eigene Ausführung erhalten.
- PS2501-4 ist auf dem dunklen Baustein auf Seite 2 nach Vergrößerung lesbar; ein weiterer Fertigungsaufdruck ist kein eigener Typ.
- Die beiden MAX7219CNG auf Seite 3 unterscheiden sich nur in Fertigungs-/Chargenmarkierungen. Nur ein Eintrag wurde aufgenommen.
- ULN2004A (ST) und ULN2004AG (anderer Herstelleraufdruck) stehen getrennt in der Tabelle, damit die vorhandenen Ausführungen nachvollziehbar bleiben. Mehrfachvorkommen identischer Bezeichnungen wurden zusammengefasst.
- Der Central-Aufdruck lautet MPQ2222A. Dies ist ein Array aus vier NPN-Transistoren im DIP-14, kein einzelner PN2222A.
- MEDER DIP05-1A72-12L sind Relais, keine ICs. Sie werden als solche gekennzeichnet.
- Die kleinen Keramikbauteile tragen eine Lesart wie B3CA4.5Z. Bezeichnung und Funktion bleiben vorläufig; sie sind nicht als Relais oder IC bestätigt.
- Stückzahlen, elektrische Kennwerte und vollständige Datenblattzuordnungen bleiben offen. Verdeckte Bauteile unter weißen Zetteln wurden nicht geraten.

## Herstellerquellen zur Funktionszuordnung

- [Central Semiconductor: MPQ2222 / MPQ2222A](https://my.centralsemi.com/datasheets/mpq2222.PDF): vier unabhängige NPN-Transistoren, DIP-14.
- [Renesas: PS2501-4](https://www.renesas.com/en/products/ps2501-4): Optokopplerfamilie mit Transistorausgang.
- [Analog Devices: MAX250](https://www.analog.com/en/products/max250.html): Baustein des MAX250/MAX251-Chipsatzes für isolierte RS-232-Schnittstellen.
- [Analog Devices: MAX7219](https://www.analog.com/en/products/max7219.html): serieller LED-Anzeigetreiber.
- [NXP: PCF8574 / PCF8574A](https://www.nxp.com/docs/en/data-sheet/PCF8574_PCF8574A.pdf): 8-Bit-I/O-Expander für I²C.
- [ST: L78](https://www.st.com/resource/en/datasheet/l78.pdf) und [L79](https://www.st.com/en/power-management/l79.html): positive bzw. negative Festspannungsregler.
- [ST: Darlington-Arrays](https://www.st.com/en/interfaces-and-transceivers/darlington-arrays/products.html): ULN-Treiberfamilien.

Diese Quellen unterstützen die Funktionszuordnung; lokal heruntergeladene und für alle konkreten Aufdrucke geprüfte Herstellerdatenblätter liegen für die neuen Einträge noch nicht vor. Bilderverzeichnisse bleiben leer und Bildlinks wurden nicht ergänzt.

## Ergänzung: lokale Datenblätter

Am 13.10.2026 wurden lokale Datenblätter bzw. gekennzeichnete Referenzen für 29 der 30 Einträge ergänzt: [Datenblattverzeichnis Diverse](../Datenblaetter/Diverse/README.md). Die vorherigen offenen Angaben dokumentieren den Stand der ersten Fotoauswertung.

Beim Abgleich wurden MAX250CPD (statt MAX250CPP) und DIP-14 (statt DIP-16) korrigiert. B3CA4.5Z ist anhand der Bestellbezeichnung als Signalrelais der FTR-B3-Familie eingeordnet; die Hersteller-/Typzuordnung am vorhandenen Bauteil bleibt vorläufig. Für LH6764-20 fehlt weiterhin eine belastbare Quelle. Die images-Verzeichnisse bleiben leer.

## Kategorien ergänzt

Acht Spannungsregler und MPQ2222A stehen inzwischen in den Kategorien [Spannungsregler](../Datenblaetter/Spannungsregler/README.md) bzw. [Transistor](../Datenblaetter/Transistor/README.md). Ihre vorherige Aufnahme unter Diverse ist hier als Verlauf dokumentiert.
