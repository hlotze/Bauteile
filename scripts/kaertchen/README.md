# Kartengenerator

Das Inventar wird aus [Bauteile.md](../../Bauteile.md) gelesen.

Aus dem Projektverzeichnis mit Python und den Paketen aus requirements.txt:

```
python scripts/kaertchen/prepare.py
python scripts/kaertchen/build.py
```

Poppler (`pdftoppm`) wird für die PNG-Ausgabe benötigt. Das Inventar, manuelle Pinfolgen und verwendete Symbolquellen liegen neben dem Generator. `images/karten.json` dokumentiert die Referenz pro Karte. Die Pinfolgen werden in Draufsicht ausgegeben; aktiv Low trägt `/`.

Die unveränderten `.kicad_sym`-Dateien stammen aus den [offiziellen KiCad-Bibliotheken, Version 9.0.4](https://gitlab.com/kicad/libraries/kicad-symbols/-/tree/9.0.4). Autoren und Lizenz: [KiCad_LICENSE.md](KiCad_LICENSE.md). Manuelle Ergänzungen stammen aus den in maps.py genannten Herstellerdokumenten. Abgeleitete Karten werden unter CC BY-SA 4.0 mit der KiCad-Ausnahme gemäß dieser Lizenz bereitgestellt.
