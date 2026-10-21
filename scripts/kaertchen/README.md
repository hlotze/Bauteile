# Kartengenerator

Das Inventar wird aus [Bauteile.md](../../Bauteile.md) gelesen.

Aus dem Projektverzeichnis mit Python und den Paketen aus requirements.txt:

```
python scripts/kaertchen/prepare.py
python scripts/kaertchen/build.py
```

Poppler (`pdftoppm`) wird für die PNG-Ausgabe benötigt. Das Inventar, manuelle Pinfolgen und verwendete Symbolquellen liegen neben dem Generator. `images/karten.json` dokumentiert die Referenz pro Karte. Die Pinfolgen werden in Draufsicht ausgegeben; aktiv Low trägt `/`.

Die unveränderten `.kicad_sym`-Dateien stammen aus den [offiziellen KiCad-Bibliotheken, Version 9.0.4](https://gitlab.com/kicad/libraries/kicad-symbols/-/tree/9.0.4). Autoren und Lizenz: [KiCad_LICENSE.md](KiCad_LICENSE.md). Manuelle Ergänzungen stammen aus den in maps.py genannten Herstellerdokumenten. Abgeleitete Karten werden unter CC BY-SA 4.0 mit der KiCad-Ausnahme gemäß dieser Lizenz bereitgestellt.

Die 56 CD4xxx-Karten werden in `cd_cards.py` nach den alten Karten aus `images/PNG Kopie` gezeichnet: Typ und Funktion gemeinsam im Titel und Fuß, grüne Umrandung, blaue Ausgänge, Überstriche für aktiv Low sowie Gatter mit Leitungen zu den tatsächlichen DIP-Pins. Gatter, Inverter, Schalter und Funktionsblöcke sind Vektorelemente. Die vorhandenen Hersteller-Blockschaltbilder und ergänzenden Zeitdiagramme bleiben als zugeschnittene PNGs erhalten; sie werden in SVG und PDF eingebettet. Die SVGs benötigen keine externen Bilddateien.

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

Die 85 Karten in `SN7xxx` werden von `sn_cards.py` im gleichen Stil gezeichnet. Gatter, Inverter und Buskanäle sind mit den tatsächlichen DIP-Pins verdrahtet. Flipflop-Blöcke tragen Signalnamen und Pinnummern. Für komplexere Bausteine sind 29 passende Herstellerdiagramme aus den lokalen PDFs zugeschnitten; gemeinsame Datenblätter werden nach Bausteinvariante getrennt. `sn_logikvorlagen/quellen.json` dokumentiert PDF, Seite, Abbildung, Prüfsumme und Ausschnitt bei 300 dpi. Die eingebetteten Bilder benötigen keine externen Dateien. Karten mit 20 Pins verwenden einen kompakten Fuß zwischen den Pinreihen.

```
python scripts/kaertchen/build.py --category SN7xxx
```

Einzelne Karten und den vollständigen A4-Druckbogen aktualisieren:

```
python scripts/kaertchen/build.py --part COM8126 --part LH6764-20
```

Nach jeder Bestandsänderung `Bauteile.md` mit der führenden `Bauteile.db` abgleichen; abweichende Angaben aus der Datenbank übernehmen. `scripts/build_db.py` überschreibt die Datenbank und darf nur auf ausdrückliche Anweisung ausgeführt werden.

NE555-Herstellerbestände (E und TI) teilen die vorhandene NE555-Referenzkarte.
