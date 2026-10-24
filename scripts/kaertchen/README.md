# Kartengenerator

Das Inventar wird aus [Bauteile.md](../../Bauteile.md) gelesen.

Aus dem Projektverzeichnis mit Python und den Paketen aus requirements.txt:

```
python scripts/kaertchen/prepare.py
python scripts/kaertchen/build.py
```

Poppler (`pdftoppm`) wird für die PNG-Ausgabe benötigt. Das Inventar, manuelle Pinfolgen und verwendete Symbolquellen liegen neben dem Generator. `images/karten.json` dokumentiert die Referenz pro Karte. Die Pinfolgen werden in Draufsicht ausgegeben; aktiv Low trägt `/`.

Die unveränderten `.kicad_sym`-Dateien stammen aus den [offiziellen KiCad-Bibliotheken, Version 9.0.4](https://gitlab.com/kicad/libraries/kicad-symbols/-/tree/9.0.4). Autoren und Lizenz: [KiCad_LICENSE.md](KiCad_LICENSE.md). Manuelle Ergänzungen stammen aus den in maps.py genannten Herstellerdokumenten. Abgeleitete Karten werden unter CC BY-SA 4.0 mit der KiCad-Ausnahme gemäß dieser Lizenz bereitgestellt.

Die 58 CD4xxx-Karten werden in `cd_cards.py` nach den alten Karten aus `images/PNG Kopie` gezeichnet: Typ und Funktion gemeinsam im Titel und Fuß, grüne Umrandung, blaue Ausgänge, Überstriche für aktiv Low sowie Gatter mit Leitungen zu den tatsächlichen DIP-Pins. Gatter, Inverter, Schalter und Funktionsblöcke sind Vektorelemente. Die vorhandenen Hersteller-Blockschaltbilder und ergänzenden Zeitdiagramme bleiben als zugeschnittene PNGs erhalten; sie werden in SVG und PDF eingebettet. Die SVGs benötigen keine externen Bilddateien.

`logikvorlagen/quellen.json` dokumentiert Originaldateien, Prüfsummen und Ausschnitte. Die zugeschnittenen Vorlagen liegen im selben Verzeichnis, sodass der Generator auch ohne den lokalen Sicherungsordner funktioniert. Pinnummern und die dokumentierte Pinreferenz bleiben maßgeblich; lesbare Signalnamen der alten Diagramme sind als `card_pin_labels` in `images/karten.json` dokumentiert. Bei CD4027 bezeichnet das übernommene TI-Schaltbild das Flipflop an Pins 9–15 als FF1.

Nur die CD4xxx-Einzelkarten neu erzeugen und den kompletten A4-Druckbogen aktualisieren:

```
python scripts/kaertchen/build.py --category CD4xxx
```

Die 24 Karten in `Diverse` verwenden denselben Stil. `diverse_cards.py` zeichnet Operationsverstärker, Komparatoren, Optokoppler, Halbbrücken, Leitungstreiber und Darlington-Stufen mit ihren zugehörigen Pinnummern und Leitungen. Versorgung, aktive Low-Signale und die engeren 2,54-mm-Pinabstände des MAX7219 werden berücksichtigt. LH6764-20 bleibt eine Identifikationskarte ohne erfundene Pinbelegung. Beim LM311 wird Pin 1 als Ausgangsemitter (`E-OUT`) dargestellt; die dokumentierte ursprüngliche Pinfolge bleibt erhalten.

Passende Schaltbilder wurden aus den lokalen Datenblättern für COM8126, MAX250, MAX7219, NE555, PCF8574 und UA78S40 ausgeschnitten. `diverse_logikvorlagen/quellen.json` nennt PDF, Seite, Abbildung, Prüfsumme und den Ausschnitt in Pixeln bei 300 dpi. Die zugeschnittenen PNGs werden direkt in SVG und PDF eingebettet. Bei COM8126 und MAX7219 ergänzen sie besser lesbare Funktionsblöcke; beim PCF8574 wird der relevante GPIO-Ausschnitt verwendet. Die Pin- und Diagrammzuordnung steht auch in `images/karten.json`.

```
python scripts/kaertchen/build.py --category Diverse
```

Eine gezielte Neuerzeugung erhält die Dateien und Metadaten der anderen Kategorien und erstellt den vollständigen A4-Druckbogen neu.

Die 87 Karten in `SN7xxx` werden von `sn_cards.py` im gleichen Stil gezeichnet. Gatter, Inverter und Buskanäle sind mit den tatsächlichen DIP-Pins verdrahtet. Flipflop-Blöcke tragen Signalnamen und Pinnummern. Für komplexere Bausteine sind 29 passende Herstellerdiagramme aus den lokalen PDFs zugeschnitten; gemeinsame Datenblätter werden nach Bausteinvariante getrennt. `sn_logikvorlagen/quellen.json` dokumentiert PDF, Seite, Abbildung, Prüfsumme und Ausschnitt bei 300 dpi. Die eingebetteten Bilder benötigen keine externen Dateien. Karten mit 20 Pins verwenden einen kompakten Fuß zwischen den Pinreihen.

```
python scripts/kaertchen/build.py --category SN7xxx
```

Einzelne Karten und den vollständigen A4-Druckbogen aktualisieren:

```
python scripts/kaertchen/build.py --part COM8126 --part LH6764-20
```

Nach jeder Bestandsänderung `Bauteile.db` mit der führenden `Bauteile.md` abgleichen; abweichende Angaben aus der Markdown-Datei übernehmen. `scripts/build_db.py` ersetzt die Datenbank vollständig und darf nur auf ausdrückliche Anweisung ausgeführt werden.

NE555-Herstellerbestände (E und TI) teilen die vorhandene NE555-Referenzkarte.

## Anschlusskarten für diskrete Bauteile und Regler

`anschlusskarten.py` erstellt eigenständige **45 × 55 mm** große Karten für Transistoren, MOSFETs, Triacs, Spannungsregler und Dioden. Oben steht das Schaltplansymbol, darunter eine schematische Gehäusezeichnung mit Anschlussnamen, Pinnummern und Blickrichtung. Die Gehäuse sind nicht maßstäblich. Die Karten enthalten keine Anwendungsbeschaltung oder Kennwerttabellen.

```sh
python3 scripts/kaertchen/anschlusskarten.py
```

Benötigt werden Python 3 (Standardbibliothek), `rsvg-convert` und `pdfunite`. Die Ausgabe liegt unter [images/Anschlusskarten](../../images/Anschlusskarten/README.md): SVG und PDF in Originalgröße, PNG mit 300 dpi, Vorschau sowie ein separater [A4-Druckbogen](../../images/Bauteil_Anschlusskarten_A4.pdf). Bei 100 % / tatsächlicher Größe drucken, ohne Seitenanpassung.

Die expliziten Pinfolgen und Ansichten stehen in [anschlusskarten.json](anschlusskarten.json). Jede Karte nennt ihre konkrete Herstellerreferenz und PDF-Seite; die Konfiguration und das Ausgabemanifest enthalten zusätzlich die SHA-256-Prüfsumme der Quelle. Bei Quellenänderungen stoppt der Generator, bis die Zuordnung erneut geprüft wurde. Vorne bedeutet: flache bzw. beschriftete Seite zum Betrachter, Anschlüsse nach unten. Die Pinliste läuft dann im Bild von links nach rechts. DIP wird in Draufsicht gezeichnet; die Liste enthält dort die normalen Pinnummern.

Die Nummern sind herstellerspezifisch: Beispielsweise steht beim GME-TIP31C vorne 1–3–2, beim ST-2SD882 3–2–1 und beim NXP-BC327 bzw. MAC97A6 ebenfalls 3–2–1. Die zugehörigen Anschlussnamen bleiben maßgeblich. TO-220-Kühlfahnen sind gesondert beschriftet; BTA06 hat eine isolierte Fahne. LM317 verwendet ADJ, TL431A REF/A/K. Nicht bestätigte Varianten (2N2222/P2N2222A, IRF510N/IRF510 sowie S-/SS-Typen) tragen einen ausdrücklichen Referenzhinweis.

Das Inventar wird ausschließlich lesend aus `Bauteile.db` übernommen. Anschließend aktualisiert der Generator gezielt **nur Karte_PNG, Karte_PDF und Karte_SVG** sowie die Kartenlinks in Markdown; erforderliche Kartenspalten werden ergänzt. Alle anderen Datenbankfelder werden vor dem Commit mit dem Ausgangsstand verglichen. Die ursprünglichen IC-Karten einschließlich der bisherigen MPQ2222A-Karte werden nicht überschrieben, der alte IC-Druckbogen bleibt erhalten.

Nur bestimmte Einzelkarten neu zeichnen (Druckbogen und Metadaten werden vollständig aktualisiert):

```sh
python3 scripts/kaertchen/anschlusskarten.py --part BC547C --part LM317
```

Neue Bestandstypen benötigen zuerst eine geprüfte Zuordnung in der JSON-Konfiguration. Der Generator prüft, dass alle erfassten Typen der fünf Kategorien abgedeckt sind und alle Quellen unverändert vorliegen.

## Ergänzung: ACT86 und LS688

SN74ACT86N verwendet die direkt aus TI SCAS534E, Seite 3, geprüfte Pinfolge anstelle der bisherigen LS86-Pinreferenz. SN74LS688N verwendet die N-Gehäusebelegung aus TI SDLS008, Seite 1, sowie die Funktionstabelle auf Seite 2. `maps.py` enthält beide Pinfolgen; `sn_cards.py` zeichnet den 8-Bit-Gleichheitsvergleich mit aktiv-Low-Freigabe /G (Pin 1) und aktiv-Low-Push-Pull-Ausgang /EQ (Pin 19). P- und Q-Leitungen sind Eingänge; es gibt keinen Größenvergleichsausgang und keine 3-State-Abschaltung. Die neue Karte und die ACT86-Karte sind im bestehenden IC-A4-Druckbogen enthalten.

TO-18- und TO-39-Metallgehäuse werden als **Unteransicht mit Nase links oben** gezeichnet; die zugehörigen Positionen stehen ausdrücklich als x/y-Koordinaten in der Pinzuordnung. BC141 und BC161 verwenden ST-Unterlagen mit Suffix -16, 2N2222A die TO-18-Referenz von ST. Bei 2N2222A bleibt die tatsächliche Bauform offen. Die Konfiguration kann in `pending` ausdrücklich noch nicht zuordenbare Bestandseinträge führen (zurzeit die Zenerdioden ohne bestätigte Typreihe/Gehäuse). Sie bekommen keine erfundene Anschlusskarte und werden im Ausgabeverzeichnis als offene Zuordnungen dokumentiert; vorhandene Kartenlinks dürfen dabei nicht verworfen werden.

## Optokoppler

PC817 (Sharp, DIP-4) wird in der eigenen Kategorie `Optokoppler` geführt. Die Karte zeigt LED und Fototransistor mit Pins 1 A, 2 K, 3 E, 4 C in Draufsicht. Referenz: Sharp OP18002EN, PDF-Seite 2; Typbezeichnung PC817 ohne Suffix; CTR ≥ 50 % bei I<sub>F</sub> = 5 mA und V<sub>CE</sub> = 5 V (T<sub>a</sub> = 25 °C). Neuerzeugung: `python scripts/kaertchen/build.py --part PC817`. Der IC-A4-Druckbogen enthält die Karte ebenfalls.
