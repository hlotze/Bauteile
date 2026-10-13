# Bauteil-Sammlung

Lokale Dokumentation meiner ICs aus den Familien **SN74xx** und **CD4xxx** sowie **Transistoren, MOSFETs, Triacs, Spannungsreglern** und weiterer Bauteile unter **Diverse**, vorbereitet für eine spätere Veröffentlichung auf GitHub.

Alle Datenblattkategorien: [Datenblattverzeichnis](Datenblaetter/README.md).

## IC-Bestand: SN74xx

**83 Einträge** einschließlich unterschiedlicher Logikfamilien aus der ursprünglichen Pinbelegungsübersicht und der ergänzenden [Foto-PDF](Quellen/weitere_SN7xxx_ICs.pdf). Die ursprünglichen 64 Bezeichnungen gehören zur **74LS-Familie**; `N` bezeichnet dort das Kunststoff-DIP-Gehäuse. Die Ergänzungen enthalten auch Standard-TTL, HC, HCT und ACT sowie Grundnummern ohne bestätigte Logikfamilie. Stückzahlen sind noch offen. Die Bezeichnungen werden wie im Bild übernommen; bei mehreren Typen führen die Herstellerdatenblätter zusätzlich eine A- oder B-Variante, die in der Tabelle vermerkt ist. Diese Zuordnung bestätigt noch nicht die genaue Variante eines tatsächlich vorhandenen Bausteins.

Die bisher mit Herstellerdatenblättern dokumentierten 74LS-Typen sind für **+5 V** vorgesehen (empfohlener VCC-Bereich der kommerziellen 74LS-Versionen: **4,75 bis 5,25 V**). Höhere zulässige Spannungen einzelner Treiberausgänge sind keine höheren Versorgungsspannungen des ICs. Quellen und Zuordnungen stehen im [Datenblattverzeichnis](Datenblaetter/SN7xxx/README.md).

Die Ergänzungen und unsicheren Lesarten sind im [Erkennungsprotokoll](Quellen/weitere_SN7xxx_Auswertung.md) dokumentiert. Eine Grundnummer ohne Familienzusatz bestätigt keine LS-Ausführung. Weitere Quellen, darunter die Kartenreferenzen für 7460, 7487 und 74576, sind in den Tabellen verlinkt.

Die [Experimentierkarten](images/README.md) enthalten Pinbelegung und Funktion im Format **45 × 55 mm**. [A4-Druckbogen](images/IC_Karten_A4.pdf), bei **100 % / tatsächlicher Größe** drucken.

| Bezeichnung laut Bild | Typ / Funktion | Gehäuse | Anzahl | +5 V / Besonderheiten | Datenblatt | Karte |
| --- | --- | --- | --- | --- | --- | --- |
| SN74LS00N | 4 NAND-Gatter mit je 2 Eingängen | DIP-14 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS00N_TI.pdf) | [Bild](images/SN7xxx/SN74LS00N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS00N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS00N_karte_45x55mm.svg) |
| SN74LS02N | 4 NOR-Gatter mit je 2 Eingängen | DIP-14 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS02N_TI.pdf) | [Bild](images/SN7xxx/SN74LS02N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS02N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS02N_karte_45x55mm.svg) |
| SN74LS04N | 6 Inverter | DIP-14 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS04N_TI.pdf) | [Bild](images/SN7xxx/SN74LS04N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS04N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS04N_karte_45x55mm.svg) |
| SN74LS05N | 6 Inverter mit Open-Collector-Ausgängen | DIP-14 | offen | +5 V; Pull-up bzw. geeignete Last nötig | [PDF](Datenblaetter/SN7xxx/SN74LS05N_TI.pdf) | [Bild](images/SN7xxx/SN74LS05N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS05N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS05N_karte_45x55mm.svg) |
| SN74LS06N | 6 invertierende Puffer/Treiber mit Open-Collector-Ausgängen | DIP-14 | offen | +5 V; Pull-up bzw. geeignete Last nötig | [PDF](Datenblaetter/SN7xxx/SN74LS06N_TI.pdf) | [Bild](images/SN7xxx/SN74LS06N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS06N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS06N_karte_45x55mm.svg) |
| SN74LS07N | 6 nichtinvertierende Puffer/Treiber mit Open-Collector-Ausgängen | DIP-14 | offen | +5 V; Pull-up bzw. geeignete Last nötig | [PDF](Datenblaetter/SN7xxx/SN74LS07N_TI.pdf) | [Bild](images/SN7xxx/SN74LS07N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS07N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS07N_karte_45x55mm.svg) |
| SN74LS08N | 4 AND-Gatter mit je 2 Eingängen | DIP-14 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS08N_TI.pdf) | [Bild](images/SN7xxx/SN74LS08N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS08N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS08N_karte_45x55mm.svg) |
| SN74LS10N | 3 NAND-Gatter mit je 3 Eingängen | DIP-14 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS10N_TI.pdf) | [Bild](images/SN7xxx/SN74LS10N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS10N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS10N_karte_45x55mm.svg) |
| SN74LS11N | 3 AND-Gatter mit je 3 Eingängen | DIP-14 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS11N_TI.pdf) | [Bild](images/SN7xxx/SN74LS11N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS11N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS11N_karte_45x55mm.svg) |
| 7412 | 3 NAND-Gatter mit je 3 Eingängen, Open-Collector-Ausgänge | offen | offen | Grundnummer laut Übersicht, S. 1; Familie, Gehäuse und Datenblatt noch zu prüfen | noch offen | [Bild](images/SN7xxx/7412_karte_45x55mm.png) / [PDF](images/SN7xxx/7412_karte_45x55mm.pdf) / [SVG](images/SN7xxx/7412_karte_45x55mm.svg) |
| SN74LS14N | 6 Schmitt-Trigger-Inverter | DIP-14 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS14N_TI.pdf) | [Bild](images/SN7xxx/SN74LS14N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS14N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS14N_karte_45x55mm.svg) |
| 7416 | 6 invertierende Puffer/Treiber mit Open-Collector-Ausgängen | offen | offen | Grundnummer laut Übersicht, S. 1; Familie, Gehäuse und Datenblatt noch zu prüfen | noch offen | [Bild](images/SN7xxx/7416_karte_45x55mm.png) / [PDF](images/SN7xxx/7416_karte_45x55mm.pdf) / [SVG](images/SN7xxx/7416_karte_45x55mm.svg) |
| SN74LS20N | 2 NAND-Gatter mit je 4 Eingängen | DIP-14 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS20N_TI.pdf) | [Bild](images/SN7xxx/SN74LS20N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS20N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS20N_karte_45x55mm.svg) |
| SN74LS21N | 2 AND-Gatter mit je 4 Eingängen | DIP-14 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS21N_TI.pdf) | [Bild](images/SN7xxx/SN74LS21N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS21N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS21N_karte_45x55mm.svg) |
| SN74LS27N | 3 NOR-Gatter mit je 3 Eingängen | DIP-14 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS27N_TI.pdf) | [Bild](images/SN7xxx/SN74LS27N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS27N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS27N_karte_45x55mm.svg) |
| SN74LS30N | 1 NAND-Gatter mit 8 Eingängen | DIP-14 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS30N_TI.pdf) | [Bild](images/SN7xxx/SN74LS30N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS30N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS30N_karte_45x55mm.svg) |
| SN74LS32N | 4 OR-Gatter mit je 2 Eingängen | DIP-14 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS32N_TI.pdf) | [Bild](images/SN7xxx/SN74LS32N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS32N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS32N_karte_45x55mm.svg) |
| 7438 | 4 NAND-Puffer mit je 2 Eingängen, Open-Collector-Ausgänge | offen | offen | Grundnummer laut Übersicht, S. 1; Familie, Gehäuse und Datenblatt noch zu prüfen | noch offen | [Bild](images/SN7xxx/7438_karte_45x55mm.png) / [PDF](images/SN7xxx/7438_karte_45x55mm.pdf) / [SVG](images/SN7xxx/7438_karte_45x55mm.svg) |
| 7440 | 2 NAND-Puffer mit je 4 Eingängen | offen | offen | Grundnummer laut Übersicht, S. 1; Familie, Gehäuse und Datenblatt noch zu prüfen | noch offen | [Bild](images/SN7xxx/7440_karte_45x55mm.png) / [PDF](images/SN7xxx/7440_karte_45x55mm.pdf) / [SVG](images/SN7xxx/7440_karte_45x55mm.svg) |
| SN74LS42N | BCD-zu-Dezimal-Decoder (1 aus 10) | DIP-16 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS42N_TI.pdf) | [Bild](images/SN7xxx/SN74LS42N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS42N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS42N_karte_45x55mm.svg) |
| SN74LS47N | BCD-zu-7-Segment-Decoder/Treiber, aktive Low-Ausgänge, Open-Collector-Ausgänge | DIP-16 | offen | +5 V; Pull-up bzw. geeignete Last nötig | [PDF](Datenblaetter/SN7xxx/SN74LS47N_TI.pdf) | [Bild](images/SN7xxx/SN74LS47N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS47N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS47N_karte_45x55mm.svg) |
| SN74LS48N | BCD-zu-7-Segment-Decoder/Treiber, aktive High-Ausgänge | DIP-16 | offen | +5 V; interne Pull-ups; Segmentstrom beachten | [PDF](Datenblaetter/SN7xxx/SN74LS48N_TI.pdf) | [Bild](images/SN7xxx/SN74LS48N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS48N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS48N_karte_45x55mm.svg) |
| SN74LS51N | 2 AND-OR-INVERT-Gatter (unterschiedliche Eingangszahl) | DIP-14 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS51N_TI.pdf) | [Bild](images/SN7xxx/SN74LS51N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS51N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS51N_karte_45x55mm.svg) |
| SN74LS54N | 1 AND-OR-INVERT-Gatter mit 4 AND-Gruppen | DIP-14 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS54N_TI.pdf) | [Bild](images/SN7xxx/SN74LS54N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS54N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS54N_karte_45x55mm.svg) |
| SN74LS55N | 1 AND-OR-INVERT-Gatter mit 2 AND-Gruppen mit je 4 Eingängen | DIP-14 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS55N_Motorola.pdf) | [Bild](images/SN7xxx/SN74LS55N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS55N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS55N_karte_45x55mm.svg) |
| 7460 | 2 Expander mit je 4 Eingängen | offen | offen | Grundnummer laut Übersicht, S. 1; Familie, Gehäuse und Datenblatt noch zu prüfen; Kartenreferenz: TI SN7460 | [PDF](Datenblaetter/SN7xxx/7460_TI_Referenz.pdf) | [Bild](images/SN7xxx/7460_karte_45x55mm.png) / [PDF](images/SN7xxx/7460_karte_45x55mm.pdf) / [SVG](images/SN7xxx/7460_karte_45x55mm.svg) |
| SN74LS73N | 2 JK-Flipflops mit Löschen, negative Taktflanke | DIP-14 | offen | +5 V; Referenz: SN74LS73A | [PDF](Datenblaetter/SN7xxx/SN74LS73N_TI.pdf) | [Bild](images/SN7xxx/SN74LS73N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS73N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS73N_karte_45x55mm.svg) |
| SN74LS74N | 2 D-Flipflops mit Setzen/Löschen, positive Taktflanke | DIP-14 | offen | +5 V; Referenz: SN74LS74A | [PDF](Datenblaetter/SN7xxx/SN74LS74N_TI.pdf) | [Bild](images/SN7xxx/SN74LS74N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS74N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS74N_karte_45x55mm.svg) |
| SN74LS75N | 4-Bit-D-Latch, transparent, 2 Enable-Gruppen | DIP-16 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS75N_TI.pdf) | [Bild](images/SN7xxx/SN74LS75N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS75N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS75N_karte_45x55mm.svg) |
| SN74LS76N | 2 JK-Flipflops mit Setzen/Löschen | DIP-16 | offen | +5 V; Referenz: SN74LS76A; LS76A: negative Taktflanke | [PDF](Datenblaetter/SN7xxx/SN74LS76N_TI.pdf) | [Bild](images/SN7xxx/SN74LS76N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS76N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS76N_karte_45x55mm.svg) |
| SN74LS83N | 4-Bit-Binär-Volladdierer mit schnellem Übertrag | DIP-16 | offen | +5 V; Referenz: SN74LS83A; Versorgung an Pin 5/12; andere Pinbelegung als LS283 | [PDF](Datenblaetter/SN7xxx/SN74LS83N_TI.pdf) | [Bild](images/SN7xxx/SN74LS83N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS83N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS83N_karte_45x55mm.svg) |
| SN74ACT86N | 4 XOR-Gatter mit je 2 Eingängen | DIP-14 | offen | ACT-Ausführung; Aufdruck, S. 2; Datenblatt noch zu prüfen | noch offen | [Bild](images/SN7xxx/SN74ACT86N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74ACT86N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74ACT86N_karte_45x55mm.svg) |
| SN74LS86N | 4 XOR-Gatter mit je 2 Eingängen | DIP-14 | offen | +5 V; Referenz: SN74LS86A | [PDF](Datenblaetter/SN7xxx/SN74LS86N_TI.pdf) | [Bild](images/SN7xxx/SN74LS86N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS86N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS86N_karte_45x55mm.svg) |
| 7487 | 4-Bit-Funktionselement: direkt, invertiert, Null oder Eins | offen | offen | Grundnummer laut Übersicht, S. 1; Familie, Gehäuse und Datenblatt noch zu prüfen; Kartenreferenz: TI SN74H87; Referenzfamilie H | [PDF](Datenblaetter/SN7xxx/7487_TI_Datenbuchauszug.pdf) | [Bild](images/SN7xxx/7487_karte_45x55mm.png) / [PDF](images/SN7xxx/7487_karte_45x55mm.pdf) / [SVG](images/SN7xxx/7487_karte_45x55mm.svg) |
| SN74LS90N | Asynchroner Dekadenzähler (Teiler durch 2 und 5) | DIP-14 | offen | +5 V; Versorgungspins laut Datenblatt | [PDF](Datenblaetter/SN7xxx/SN74LS90N_TI.pdf) | [Bild](images/SN7xxx/SN74LS90N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS90N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS90N_karte_45x55mm.svg) |
| SN74LS92N | Asynchroner Teiler durch 12 (Teiler durch 2 und 6) | DIP-14 | offen | +5 V; Versorgungspins laut Datenblatt | [PDF](Datenblaetter/SN7xxx/SN74LS92N_TI.pdf) | [Bild](images/SN7xxx/SN74LS92N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS92N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS92N_karte_45x55mm.svg) |
| SN74LS93N | Asynchroner 4-Bit-Binärzähler (Teiler durch 2 und 8) | DIP-14 | offen | +5 V; Versorgungspins laut Datenblatt | [PDF](Datenblaetter/SN7xxx/SN74LS93N_TI.pdf) | [Bild](images/SN7xxx/SN74LS93N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS93N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS93N_karte_45x55mm.svg) |
| SN74LS95N | 4-Bit-Schieberegister mit parallelem Laden | DIP-14 | offen | +5 V; Referenz: SN74LS95B; Versorgungspins laut Datenblatt | [PDF](Datenblaetter/SN7xxx/SN74LS95N_TI.pdf) | [Bild](images/SN7xxx/SN74LS95N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS95N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS95N_karte_45x55mm.svg) |
| SN74LS107N | 2 JK-Flipflops mit Löschen, negative Taktflanke | DIP-14 | offen | +5 V; Referenz: SN74LS107A | [PDF](Datenblaetter/SN7xxx/SN74LS107N_TI.pdf) | [Bild](images/SN7xxx/SN74LS107N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS107N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS107N_karte_45x55mm.svg) |
| 74109 | 2 JK-Flipflops mit Setzen/Löschen, positive Taktflanke | offen | offen | Grundnummer laut Übersicht, S. 1; Familie, Gehäuse und Datenblatt noch zu prüfen | noch offen | [Bild](images/SN7xxx/74109_karte_45x55mm.png) / [PDF](images/SN7xxx/74109_karte_45x55mm.pdf) / [SVG](images/SN7xxx/74109_karte_45x55mm.svg) |
| SN74LS112N | 2 JK-Flipflops mit Setzen/Löschen, negative Taktflanke | DIP-16 | offen | +5 V; Referenz: SN74LS112A | [PDF](Datenblaetter/SN7xxx/SN74LS112N_TI.pdf) | [Bild](images/SN7xxx/SN74LS112N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS112N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS112N_karte_45x55mm.svg) |
| SN74LS138N | 3-zu-8-Decoder/Demultiplexer, aktive Low-Ausgänge | DIP-16 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS138N_TI.pdf) | [Bild](images/SN7xxx/SN74LS138N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS138N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS138N_karte_45x55mm.svg) |
| SN74LS139N | 2 unabhängige 2-zu-4-Decoder/Demultiplexer, aktive Low-Ausgänge | DIP-16 | offen | +5 V; Referenz: SN74LS139A | [PDF](Datenblaetter/SN7xxx/SN74LS139N_TI.pdf) | [Bild](images/SN7xxx/SN74LS139N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS139N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS139N_karte_45x55mm.svg) |
| SN74LS145N | BCD-zu-Dezimal-Decoder/Treiber, Open-Collector-Ausgänge | DIP-16 | offen | +5 V; Pull-up bzw. geeignete Last nötig | [PDF](Datenblaetter/SN7xxx/SN74LS145N_TI.pdf) | [Bild](images/SN7xxx/SN74LS145N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS145N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS145N_karte_45x55mm.svg) |
| SN74LS147N | Dezimal-zu-BCD-Prioritätsencoder, aktive Low-Ein-/Ausgänge | DIP-16 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS147N_TI.pdf) | [Bild](images/SN7xxx/SN74LS147N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS147N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS147N_karte_45x55mm.svg) |
| SN74LS148N | 8-zu-3-Prioritätsencoder, aktive Low-Ein-/Ausgänge | DIP-16 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS148N_TI.pdf) | [Bild](images/SN7xxx/SN74LS148N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS148N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS148N_karte_45x55mm.svg) |
| SN74LS151N | 8-zu-1-Multiplexer | DIP-16 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS151N_TI.pdf) | [Bild](images/SN7xxx/SN74LS151N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS151N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS151N_karte_45x55mm.svg) |
| SN74LS153N | 2 unabhängige 4-zu-1-Multiplexer | DIP-16 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS153N_TI.pdf) | [Bild](images/SN7xxx/SN74LS153N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS153N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS153N_karte_45x55mm.svg) |
| SN74LS155N | 2 2-zu-4-Decoder/Demultiplexer, alternativ als 3-zu-8-Decoder nutzbar | DIP-16 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS155N_TI.pdf) | [Bild](images/SN7xxx/SN74LS155N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS155N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS155N_karte_45x55mm.svg) |
| SN74LS156N | 2 2-zu-4-Decoder/Demultiplexer, Open-Collector-Ausgänge | DIP-16 | offen | +5 V; Pull-up bzw. geeignete Last nötig | [PDF](Datenblaetter/SN7xxx/SN74LS156N_TI.pdf) | [Bild](images/SN7xxx/SN74LS156N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS156N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS156N_karte_45x55mm.svg) |
| SN74LS157N | 4 unabhängige 2-zu-1-Multiplexer | DIP-16 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS157N_TI.pdf) | [Bild](images/SN7xxx/SN74LS157N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS157N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS157N_karte_45x55mm.svg) |
| SN74LS160N | Synchroner BCD-Zähler, asynchrones Löschen | DIP-16 | offen | +5 V; Referenz: SN74LS160A | [PDF](Datenblaetter/SN7xxx/SN74LS160N_TI.pdf) | [Bild](images/SN7xxx/SN74LS160N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS160N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS160N_karte_45x55mm.svg) |
| SN74LS161N | Synchroner 4-Bit-Binärzähler, asynchrones Löschen | DIP-16 | offen | +5 V; Referenz: SN74LS161A | [PDF](Datenblaetter/SN7xxx/SN74LS161N_TI.pdf) | [Bild](images/SN7xxx/SN74LS161N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS161N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS161N_karte_45x55mm.svg) |
| SN74LS162N | Synchroner BCD-Zähler, synchrones Löschen | DIP-16 | offen | +5 V; Referenz: SN74LS162A | [PDF](Datenblaetter/SN7xxx/SN74LS162N_TI.pdf) | [Bild](images/SN7xxx/SN74LS162N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS162N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS162N_karte_45x55mm.svg) |
| SN74LS163N | Synchroner 4-Bit-Binärzähler, synchrones Löschen | DIP-16 | offen | +5 V; Referenz: SN74LS163A | [PDF](Datenblaetter/SN7xxx/SN74LS163N_TI.pdf) | [Bild](images/SN7xxx/SN74LS163N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS163N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS163N_karte_45x55mm.svg) |
| SN74LS164N | 8-Bit-Schieberegister, serieller Eingang / parallele Ausgänge | DIP-14 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS164N_TI.pdf) | [Bild](images/SN7xxx/SN74LS164N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS164N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS164N_karte_45x55mm.svg) |
| CD74HC165E | 8-Bit-Schieberegister, parallele Eingänge / serieller Ausgang | DIP-16 | offen | HC-Ausführung; Aufdruck, S. 2; Datenblatt noch zu prüfen | noch offen | [Bild](images/SN7xxx/CD74HC165E_karte_45x55mm.png) / [PDF](images/SN7xxx/CD74HC165E_karte_45x55mm.pdf) / [SVG](images/SN7xxx/CD74HC165E_karte_45x55mm.svg) |
| SN74LS165N | 8-Bit-Schieberegister, parallele Eingänge / serieller Ausgang | DIP-16 | offen | +5 V; Referenz: SN74LS165A | [PDF](Datenblaetter/SN7xxx/SN74LS165N_TI.pdf) | [Bild](images/SN7xxx/SN74LS165N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS165N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS165N_karte_45x55mm.svg) |
| 74166 | 8-Bit-Schieberegister mit parallelem Laden | offen | offen | Grundnummer laut Übersicht, S. 1; Familie, Gehäuse und Datenblatt noch zu prüfen | noch offen | [Bild](images/SN7xxx/74166_karte_45x55mm.png) / [PDF](images/SN7xxx/74166_karte_45x55mm.pdf) / [SVG](images/SN7xxx/74166_karte_45x55mm.svg) |
| 74174N | 6 D-Flipflops mit gemeinsamem Löschen | DIP-16 | offen | Standard-TTL; Aufdruck, S. 4; Datenblatt noch zu prüfen | noch offen | [Bild](images/SN7xxx/74174N_karte_45x55mm.png) / [PDF](images/SN7xxx/74174N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/74174N_karte_45x55mm.svg) |
| PC74HCT174P | 6 D-Flipflops mit gemeinsamem Löschen | DIP-16 | offen | HCT-Ausführung; Aufdruck, S. 4; Datenblatt noch zu prüfen | noch offen | [Bild](images/SN7xxx/PC74HCT174P_karte_45x55mm.png) / [PDF](images/SN7xxx/PC74HCT174P_karte_45x55mm.pdf) / [SVG](images/SN7xxx/PC74HCT174P_karte_45x55mm.svg) |
| SN74LS174N | 6 D-Flipflops mit gemeinsamem Löschen, positive Taktflanke | DIP-16 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS174N_TI.pdf) | [Bild](images/SN7xxx/SN74LS174N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS174N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS174N_karte_45x55mm.svg) |
| SN74LS175N | 4 D-Flipflops mit Q und invertiertem Q sowie gemeinsamem Löschen, positive Taktflanke | DIP-16 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS175N_TI.pdf) | [Bild](images/SN7xxx/SN74LS175N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS175N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS175N_karte_45x55mm.svg) |
| SN74LS190N | Synchroner BCD-Auf-/Abwärtszähler mit parallelem Laden | DIP-16 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS190N_TI.pdf) | [Bild](images/SN7xxx/SN74LS190N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS190N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS190N_karte_45x55mm.svg) |
| SN74LS191N | Synchroner 4-Bit-Binär-Auf-/Abwärtszähler mit parallelem Laden | DIP-16 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS191N_TI.pdf) | [Bild](images/SN7xxx/SN74LS191N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS191N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS191N_karte_45x55mm.svg) |
| SN74LS192N | Synchroner BCD-Auf-/Abwärtszähler mit getrennten Takteingängen | DIP-16 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS192N_TI.pdf) | [Bild](images/SN7xxx/SN74LS192N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS192N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS192N_karte_45x55mm.svg) |
| SN74LS193N | Synchroner 4-Bit-Binär-Auf-/Abwärtszähler mit getrennten Takteingängen | DIP-16 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS193N_TI.pdf) | [Bild](images/SN7xxx/SN74LS193N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS193N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS193N_karte_45x55mm.svg) |
| SN74LS194N | 4-Bit-Universal-Schieberegister mit parallelem Laden, bidirektional | DIP-16 | offen | +5 V; Referenz: SN74LS194A | [PDF](Datenblaetter/SN7xxx/SN74LS194N_TI.pdf) | [Bild](images/SN7xxx/SN74LS194N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS194N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS194N_karte_45x55mm.svg) |
| 74240 | 8 invertierende Puffer mit 3-State-Ausgängen | offen | offen | Grundnummer laut Übersicht, S. 3; Familie, Gehäuse und Datenblatt noch zu prüfen | noch offen | [Bild](images/SN7xxx/74240_karte_45x55mm.png) / [PDF](images/SN7xxx/74240_karte_45x55mm.pdf) / [SVG](images/SN7xxx/74240_karte_45x55mm.svg) |
| SN74LS244N | 8 nichtinvertierende Puffer/Treiber mit 3-State-Ausgängen | DIP-20 | offen | +5 V; Enable beachten | [PDF](Datenblaetter/SN7xxx/SN74LS244N_TI.pdf) | [Bild](images/SN7xxx/SN74LS244N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS244N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS244N_karte_45x55mm.svg) |
| SN74LS245N | 8-Bit-Bustransceiver, bidirektional, 3-State-Ausgänge | DIP-20 | offen | +5 V; Enable beachten | [PDF](Datenblaetter/SN7xxx/SN74LS245N_TI.pdf) | [Bild](images/SN7xxx/SN74LS245N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS245N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS245N_karte_45x55mm.svg) |
| SN74LS247N | BCD-zu-7-Segment-Decoder/Treiber, Open-Collector-Ausgänge, andere Darstellung von 6 und 9 als LS47 | DIP-16 | offen | +5 V; Pull-up bzw. geeignete Last nötig | [PDF](Datenblaetter/SN7xxx/SN74LS247N_TI.pdf) | [Bild](images/SN7xxx/SN74LS247N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS247N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS247N_karte_45x55mm.svg) |
| SN74LS248N | BCD-zu-7-Segment-Decoder/Treiber, aktive High-Ausgänge, andere Darstellung von 6 und 9 als LS48 | DIP-16 | offen | +5 V; interne Pull-ups; Segmentstrom beachten | [PDF](Datenblaetter/SN7xxx/SN74LS248N_TI.pdf) | [Bild](images/SN7xxx/SN74LS248N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS248N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS248N_karte_45x55mm.svg) |
| 74253 | 2 4-zu-1-Multiplexer, 3-State-Ausgänge | offen | offen | Grundnummer laut Übersicht, S. 3; Familie, Gehäuse und Datenblatt noch zu prüfen | noch offen | [Bild](images/SN7xxx/74253_karte_45x55mm.png) / [PDF](images/SN7xxx/74253_karte_45x55mm.pdf) / [SVG](images/SN7xxx/74253_karte_45x55mm.svg) |
| SN74LS266N | 4 XNOR-Gatter mit je 2 Eingängen, Open-Collector-Ausgänge | DIP-14 | offen | +5 V; Pull-up bzw. geeignete Last nötig | [PDF](Datenblaetter/SN7xxx/SN74LS266N_TI.pdf) | [Bild](images/SN7xxx/SN74LS266N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS266N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS266N_karte_45x55mm.svg) |
| SN74LS273N | 8 D-Flipflops mit gemeinsamem Löschen, positive Taktflanke | DIP-20 | offen | +5 V | [PDF](Datenblaetter/SN7xxx/SN74LS273N_TI.pdf) | [Bild](images/SN7xxx/SN74LS273N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS273N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS273N_karte_45x55mm.svg) |
| 74LS279 | 4 RS-Latches | offen | offen | Handschriftlich 74LS279, S. 3; Gehäuse und Datenblatt noch zu prüfen | noch offen | [Bild](images/SN7xxx/74LS279_karte_45x55mm.png) / [PDF](images/SN7xxx/74LS279_karte_45x55mm.pdf) / [SVG](images/SN7xxx/74LS279_karte_45x55mm.svg) |
| SN74LS373N | 8-Bit-D-Latch mit 3-State-Ausgängen, transparent | DIP-20 | offen | +5 V; Enable beachten | [PDF](Datenblaetter/SN7xxx/SN74LS373N_TI.pdf) | [Bild](images/SN7xxx/SN74LS373N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS373N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS373N_karte_45x55mm.svg) |
| SN74LS374N | 8 D-Flipflops mit 3-State-Ausgängen, positive Taktflanke | DIP-20 | offen | +5 V; Enable beachten | [PDF](Datenblaetter/SN7xxx/SN74LS374N_TI.pdf) | [Bild](images/SN7xxx/SN74LS374N_karte_45x55mm.png) / [PDF](images/SN7xxx/SN74LS374N_karte_45x55mm.pdf) / [SVG](images/SN7xxx/SN74LS374N_karte_45x55mm.svg) |
| 74541 | 8 nichtinvertierende Puffer mit 3-State-Ausgängen | offen | offen | Grundnummer laut Übersicht, S. 3; Familie, Gehäuse und Datenblatt noch zu prüfen | noch offen | [Bild](images/SN7xxx/74541_karte_45x55mm.png) / [PDF](images/SN7xxx/74541_karte_45x55mm.pdf) / [SVG](images/SN7xxx/74541_karte_45x55mm.svg) |
| 74576 | 8 D-Flipflops mit invertierenden 3-State-Ausgängen | offen | offen | Grundnummer laut Übersicht, S. 3; Familie, Gehäuse und Datenblatt noch zu prüfen; Kartenreferenz: TI SN74ALS576B; Referenzfamilie ALS | [PDF](Datenblaetter/SN7xxx/74576_TI_ALS576_Referenz.pdf) | [Bild](images/SN7xxx/74576_karte_45x55mm.png) / [PDF](images/SN7xxx/74576_karte_45x55mm.pdf) / [SVG](images/SN7xxx/74576_karte_45x55mm.svg) |
| 74640 | 8-Bit-Bustransceiver, invertierend, 3-State-Ausgänge | offen | offen | Grundnummer laut Übersicht, S. 3; Familie, Gehäuse und Datenblatt noch zu prüfen | noch offen | [Bild](images/SN7xxx/74640_karte_45x55mm.png) / [PDF](images/SN7xxx/74640_karte_45x55mm.pdf) / [SVG](images/SN7xxx/74640_karte_45x55mm.svg) |
| 74641 | 8-Bit-Bustransceiver, nichtinvertierend, Open-Collector-Ausgänge | offen | offen | Grundnummer laut Übersicht, S. 3; Familie, Gehäuse und Datenblatt noch zu prüfen | noch offen | [Bild](images/SN7xxx/74641_karte_45x55mm.png) / [PDF](images/SN7xxx/74641_karte_45x55mm.pdf) / [SVG](images/SN7xxx/74641_karte_45x55mm.svg) |

## IC-Bestand: CD4xxx

**56 IC-Typen** aus der ursprünglichen Pinbelegungsübersicht und der ergänzenden [Foto-PDF](Quellen/weitere_CD4xxx_ICs.pdf). Die Bezeichnungen im Bild enthalten keine vollständigen Hersteller-/Gehäusesuffixe. Die angegebenen DIP-Gehäuse entsprechen der Übersicht; Stückzahlen bleiben offen. Farbmarkierungen und handschriftliche Zeichen wurden nicht als Stückzahlen interpretiert.

Die Referenzdatenblätter beschreiben überwiegend **CD4xxxB**, beim **CD4049** und **CD4069** die ungepufferten **UB**-Varianten. Die tatsächlichen Aufdrucke sind vor Verwendung abzugleichen. Für **CD4553** liegt eine ausdrücklich gekennzeichnete **Motorola-MC14553B-Referenz** vor; ein exaktes CD4553-Herstellerdatenblatt ist noch nicht zugeordnet.

Die zehn Ergänzungen aus der Foto-PDF sind im [Erkennungsprotokoll](Quellen/weitere_CD4xxx_Auswertung.md) mit Seitenangabe dokumentiert. Bei den Ergänzungen sind Herstellerdatenblätter und 5-V-Kennwerte teilweise noch offen; für CD4513 liegt die MC14513B-Referenz vor. CD4538 ist anhand von Beschriftung und Pinbelegung zugeordnet; der IC-Aufdruck bleibt zu prüfen.

**+5 V ist für die bereits dokumentierten Referenztypen geeignet.** Kennwerte für Strom, Geschwindigkeit, Analogschalter und Oszillatoren sind aus den 5-V-Tabellen zu entnehmen. Quellen und Zuordnungen: [Datenblattverzeichnis CD4xxx](Datenblaetter/CD4xxx/README.md).

| Bezeichnung laut Bild | Typ / Funktion | Gehäuse | Anzahl | +5 V / Besonderheiten | Datenblatt | Karte |
| --- | --- | --- | --- | --- | --- | --- |
| CD4001 | 4 NOR-Gatter mit je 2 Eingängen | DIP-14 | offen | +5 V; CMOS-Pegel | [PDF](Datenblaetter/CD4xxx/CD4001_TI.pdf) | [Bild](images/CD4xxx/CD4001_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4001_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4001_karte_45x55mm.svg) |
| CD4002 (Grundtyp; Aufdruck PC74HC4002P) | 2 NOR-Gatter mit je 4 Eingängen | DIP-14 | offen | Vorhandene HC-Ausführung; Datenblatt / 5-V-Kennwerte noch zu prüfen | noch offen | [Bild](images/CD4xxx/CD4002_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4002_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4002_karte_45x55mm.svg) |
| CD4009 | 6 invertierende Puffer/Pegelwandler | DIP-16 | offen | Datenblatt / 5-V-Kennwerte noch zu prüfen | noch offen | [Bild](images/CD4xxx/CD4009_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4009_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4009_karte_45x55mm.svg) |
| CD4011 | 4 NAND-Gatter mit je 2 Eingängen | DIP-14 | offen | +5 V; CMOS-Pegel | [PDF](Datenblaetter/CD4xxx/CD4011_TI.pdf) | [Bild](images/CD4xxx/CD4011_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4011_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4011_karte_45x55mm.svg) |
| CD4012 | 2 NAND-Gatter mit je 4 Eingängen | DIP-14 | offen | Datenblatt / 5-V-Kennwerte noch zu prüfen | noch offen | [Bild](images/CD4xxx/CD4012_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4012_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4012_karte_45x55mm.svg) |
| CD4013 | 2 D-Flipflops mit Setzen/Löschen, positive Taktflanke | DIP-14 | offen | +5 V | [PDF](Datenblaetter/CD4xxx/CD4013_TI.pdf) | [Bild](images/CD4xxx/CD4013_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4013_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4013_karte_45x55mm.svg) |
| CD4015 | 2 unabhängige 4-Bit-Schieberegister, serieller Eingang / parallele Ausgänge | DIP-16 | offen | +5 V | [PDF](Datenblaetter/CD4xxx/CD4015_TI.pdf) | [Bild](images/CD4xxx/CD4015_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4015_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4015_karte_45x55mm.svg) |
| CD4016 | 4 bilaterale Analogschalter | DIP-14 | offen | +5 V; Analogsignale innerhalb der Versorgung; Einschaltwiderstand bei 5 V beachten | [PDF](Datenblaetter/CD4xxx/CD4016_TI.pdf) | [Bild](images/CD4xxx/CD4016_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4016_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4016_karte_45x55mm.svg) |
| CD4017 | Dekadenzähler mit 10 dekodierten Ausgängen | DIP-16 | offen | +5 V; Ein Ausgang aktiv (1 aus 10) | [PDF](Datenblaetter/CD4xxx/CD4017_TI.pdf) | [Bild](images/CD4xxx/CD4017_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4017_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4017_karte_45x55mm.svg) |
| CD4019 | 4 AND-OR-Gatter / 4-Bit-Datenselektor | DIP-16 | offen | Datenblatt / 5-V-Kennwerte noch zu prüfen | noch offen | [Bild](images/CD4xxx/CD4019_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4019_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4019_karte_45x55mm.svg) |
| CD4021 | 8-Bit-Schieberegister mit parallelem Laden, parallele Eingänge / serieller Ausgang | DIP-16 | offen | +5 V | [PDF](Datenblaetter/CD4xxx/CD4021_TI.pdf) | [Bild](images/CD4xxx/CD4021_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4021_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4021_karte_45x55mm.svg) |
| CD4022 | Oktalzähler mit 8 dekodierten Ausgängen | DIP-16 | offen | +5 V; Ein Ausgang aktiv (1 aus 8) | [PDF](Datenblaetter/CD4xxx/CD4022_TI.pdf) | [Bild](images/CD4xxx/CD4022_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4022_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4022_karte_45x55mm.svg) |
| CD4023 | 3 NAND-Gatter mit je 3 Eingängen | DIP-14 | offen | +5 V; CMOS-Pegel | [PDF](Datenblaetter/CD4xxx/CD4023_TI.pdf) | [Bild](images/CD4xxx/CD4023_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4023_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4023_karte_45x55mm.svg) |
| CD4024 | 7-Bit-Binärzähler | DIP-14 | offen | +5 V; Asynchroner Zähler; negative Taktflanke | [PDF](Datenblaetter/CD4xxx/CD4024_TI.pdf) | [Bild](images/CD4xxx/CD4024_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4024_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4024_karte_45x55mm.svg) |
| CD4025 | 3 NOR-Gatter mit je 3 Eingängen | DIP-14 | offen | +5 V; CMOS-Pegel | [PDF](Datenblaetter/CD4xxx/CD4025_TI.pdf) | [Bild](images/CD4xxx/CD4025_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4025_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4025_karte_45x55mm.svg) |
| CD4026 | Dekadenzähler mit 7-Segment-Decoder | DIP-16 | offen | +5 V; Für gemeinsame Kathode; Segmentstrom bei 5 V beachten | [PDF](Datenblaetter/CD4xxx/CD4026_TI.pdf) | [Bild](images/CD4xxx/CD4026_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4026_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4026_karte_45x55mm.svg) |
| CD4027 | 2 JK-Flipflops mit Setzen/Löschen, positive Taktflanke | DIP-16 | offen | +5 V | [PDF](Datenblaetter/CD4xxx/CD4027_TI.pdf) | [Bild](images/CD4xxx/CD4027_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4027_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4027_karte_45x55mm.svg) |
| CD4028 | BCD-zu-Dezimal-Decoder | DIP-16 | offen | +5 V; Aktive High-Ausgänge | [PDF](Datenblaetter/CD4xxx/CD4028_TI.pdf) | [Bild](images/CD4xxx/CD4028_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4028_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4028_karte_45x55mm.svg) |
| CD4029 | Voreinstellbarer 4-Bit-Binär-/BCD-Auf-/Abwärtszähler | DIP-16 | offen | +5 V; Zählmodus und Richtung wählbar | [PDF](Datenblaetter/CD4xxx/CD4029_TI.pdf) | [Bild](images/CD4xxx/CD4029_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4029_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4029_karte_45x55mm.svg) |
| CD4030 | 4 XOR-Gatter mit je 2 Eingängen | DIP-14 | offen | Datenblatt / 5-V-Kennwerte noch zu prüfen | noch offen | [Bild](images/CD4xxx/CD4030_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4030_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4030_karte_45x55mm.svg) |
| CD4033 | Dekadenzähler mit 7-Segment-Decoder | DIP-16 | offen | +5 V; Für gemeinsame Kathode; Nullunterdrückung; Segmentstrom bei 5 V beachten | [PDF](Datenblaetter/CD4xxx/CD4033_TI.pdf) | [Bild](images/CD4xxx/CD4033_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4033_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4033_karte_45x55mm.svg) |
| CD4042 | 4-Bit-D-Latch | DIP-16 | offen | +5 V; Gemeinsame Takt-/Polaritätssteuerung | [PDF](Datenblaetter/CD4xxx/CD4042_TI.pdf) | [Bild](images/CD4xxx/CD4042_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4042_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4042_karte_45x55mm.svg) |
| CD4043 | 4 NOR-RS-Latches mit 3-State-Ausgängen | DIP-16 | offen | +5 V; Gemeinsame Ausgangsfreigabe beachten | [PDF](Datenblaetter/CD4xxx/CD4043_TI.pdf) | [Bild](images/CD4xxx/CD4043_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4043_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4043_karte_45x55mm.svg) |
| CD4046 | PLL mit VCO und 2 Phasenkomparatoren | DIP-16 | offen | +5 V; VCO-Frequenz bei 5 V anhand externer R/C bestimmen | [PDF](Datenblaetter/CD4xxx/CD4046_TI.pdf) | [Bild](images/CD4xxx/CD4046_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4046_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4046_karte_45x55mm.svg) |
| CD4047 | Astabiler oder monostabiler Multivibrator | DIP-14 | offen | +5 V; Zeit/Frequenz durch externe R/C | [PDF](Datenblaetter/CD4xxx/CD4047_TI.pdf) | [Bild](images/CD4xxx/CD4047_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4047_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4047_karte_45x55mm.svg) |
| CD4049 | 6 invertierende Puffer/Pegelwandler | DIP-16 | offen | +5 V; VCC Pin 1, GND Pin 8; erhöhte Eingangsspannung nur innerhalb der Datenblattgrenzen; Referenz CD4049UB | [PDF](Datenblaetter/CD4xxx/CD4049_TI.pdf) | [Bild](images/CD4xxx/CD4049_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4049_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4049_karte_45x55mm.svg) |
| CD4050 | 6 nichtinvertierende Puffer/Pegelwandler | DIP-16 | offen | +5 V; VCC Pin 1, GND Pin 8; erhöhte Eingangsspannung nur innerhalb der Datenblattgrenzen | [PDF](Datenblaetter/CD4xxx/CD4050_TI.pdf) | [Bild](images/CD4xxx/CD4050_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4050_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4050_karte_45x55mm.svg) |
| CD4051 | 8-Kanal-Analogmultiplexer/-demultiplexer | DIP-16 | offen | +5 V; VEE bei unipolarem Betrieb an GND; Signalbereich und Einschaltwiderstand beachten | [PDF](Datenblaetter/CD4xxx/CD4051_TI.pdf) | [Bild](images/CD4xxx/CD4051_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4051_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4051_karte_45x55mm.svg) |
| CD4052 | 2 gekoppelte 4-Kanal-Analogmultiplexer/-demultiplexer | DIP-16 | offen | +5 V; VEE bei unipolarem Betrieb an GND; Signalbereich und Einschaltwiderstand beachten | [PDF](Datenblaetter/CD4xxx/CD4052_TI.pdf) | [Bild](images/CD4xxx/CD4052_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4052_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4052_karte_45x55mm.svg) |
| CD4053 | 3 unabhängige 2-Kanal-Analogmultiplexer/-demultiplexer | DIP-16 | offen | +5 V; VEE bei unipolarem Betrieb an GND; Signalbereich und Einschaltwiderstand beachten | [PDF](Datenblaetter/CD4xxx/CD4053_TI.pdf) | [Bild](images/CD4xxx/CD4053_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4053_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4053_karte_45x55mm.svg) |
| CD4060 | 14-stufiger Binärzähler mit Oszillator | DIP-16 | offen | +5 V; Nicht alle Zählerstufen herausgeführt; externe R/C oder Quarz | [PDF](Datenblaetter/CD4xxx/CD4060_TI.pdf) | [Bild](images/CD4xxx/CD4060_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4060_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4060_karte_45x55mm.svg) |
| CD4063 | 4-Bit-Größenkomparator | DIP-16 | offen | +5 V; Ausgänge A größer, gleich oder kleiner B; kaskadierbar | [PDF](Datenblaetter/CD4xxx/CD4063_TI.pdf) | [Bild](images/CD4xxx/CD4063_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4063_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4063_karte_45x55mm.svg) |
| CD4066 | 4 bilaterale Analogschalter | DIP-14 | offen | +5 V; Analogsignale innerhalb der Versorgung; Einschaltwiderstand bei 5 V beachten | [PDF](Datenblaetter/CD4xxx/CD4066_TI.pdf) | [Bild](images/CD4xxx/CD4066_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4066_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4066_karte_45x55mm.svg) |
| CD4068 | AND-/NAND-Gatter mit 8 Eingängen | DIP-14 | offen | Datenblatt / 5-V-Kennwerte noch zu prüfen | noch offen | [Bild](images/CD4xxx/CD4068_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4068_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4068_karte_45x55mm.svg) |
| CD4069 | 6 Inverter | DIP-14 | offen | +5 V; Ungepufferte Variante als Datenblattreferenz; Referenz CD4069UB | [PDF](Datenblaetter/CD4xxx/CD4069_TI.pdf) | [Bild](images/CD4xxx/CD4069_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4069_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4069_karte_45x55mm.svg) |
| CD4070 | 4 XOR-Gatter mit je 2 Eingängen | DIP-14 | offen | +5 V; CMOS-Pegel | [PDF](Datenblaetter/CD4xxx/CD4070_TI.pdf) | [Bild](images/CD4xxx/CD4070_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4070_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4070_karte_45x55mm.svg) |
| CD4071 | 4 OR-Gatter mit je 2 Eingängen | DIP-14 | offen | +5 V; CMOS-Pegel | [PDF](Datenblaetter/CD4xxx/CD4071_TI.pdf) | [Bild](images/CD4xxx/CD4071_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4071_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4071_karte_45x55mm.svg) |
| CD4072 | 2 OR-Gatter mit je 4 Eingängen | DIP-14 | offen | +5 V; CMOS-Pegel | [PDF](Datenblaetter/CD4xxx/CD4072_TI.pdf) | [Bild](images/CD4xxx/CD4072_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4072_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4072_karte_45x55mm.svg) |
| CD4073 | 3 AND-Gatter mit je 3 Eingängen | DIP-14 | offen | +5 V; CMOS-Pegel | [PDF](Datenblaetter/CD4xxx/CD4073_TI.pdf) | [Bild](images/CD4xxx/CD4073_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4073_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4073_karte_45x55mm.svg) |
| CD4075 | 3 OR-Gatter mit je 3 Eingängen | DIP-14 | offen | +5 V; CMOS-Pegel | [PDF](Datenblaetter/CD4xxx/CD4075_TI.pdf) | [Bild](images/CD4xxx/CD4075_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4075_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4075_karte_45x55mm.svg) |
| CD4077 | 4 XNOR-Gatter mit je 2 Eingängen | DIP-14 | offen | +5 V; CMOS-Pegel | [PDF](Datenblaetter/CD4xxx/CD4077_TI.pdf) | [Bild](images/CD4xxx/CD4077_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4077_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4077_karte_45x55mm.svg) |
| CD4081 | 4 AND-Gatter mit je 2 Eingängen | DIP-14 | offen | +5 V; CMOS-Pegel | [PDF](Datenblaetter/CD4xxx/CD4081_TI.pdf) | [Bild](images/CD4xxx/CD4081_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4081_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4081_karte_45x55mm.svg) |
| CD4082 | 2 AND-Gatter mit je 4 Eingängen | DIP-14 | offen | +5 V; CMOS-Pegel | [PDF](Datenblaetter/CD4xxx/CD4082_TI.pdf) | [Bild](images/CD4xxx/CD4082_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4082_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4082_karte_45x55mm.svg) |
| CD4093 | 4 Schmitt-Trigger-NAND-Gatter mit je 2 Eingängen | DIP-14 | offen | +5 V; Hysterese; eigene Schaltschwellen bei 5 V | [PDF](Datenblaetter/CD4xxx/CD4093_TI.pdf) | [Bild](images/CD4xxx/CD4093_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4093_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4093_karte_45x55mm.svg) |
| CD4094 | 8-Bit-Schieberegister mit Ausgangslatch und 3-State-Ausgängen | DIP-16 | offen | +5 V; Strobe und Ausgangsfreigabe beachten | [PDF](Datenblaetter/CD4xxx/CD4094_TI.pdf) | [Bild](images/CD4xxx/CD4094_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4094_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4094_karte_45x55mm.svg) |
| CD4098 | 2 monostabile Multivibratoren | DIP-16 | offen | Datenblatt / 5-V-Kennwerte noch zu prüfen | noch offen | [Bild](images/CD4xxx/CD4098_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4098_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4098_karte_45x55mm.svg) |
| CD4503 | 6 nichtinvertierende Puffer mit 3-State-Ausgängen | DIP-16 | offen | +5 V; Ausgangsfreigaben beachten | [PDF](Datenblaetter/CD4xxx/CD4503_TI.pdf) | [Bild](images/CD4xxx/CD4503_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4503_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4503_karte_45x55mm.svg) |
| CD4511 | BCD-Latch mit 7-Segment-Decoder/LED-Treiber | DIP-16 | offen | +5 V; Für gemeinsame Kathode; Segmentstrom und Vorwiderstände beachten | [PDF](Datenblaetter/CD4xxx/CD4511_TI.pdf) | [Bild](images/CD4xxx/CD4511_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4511_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4511_karte_45x55mm.svg) |
| CD4513 | BCD-Latch mit 7-Segment-Decoder (MC14513B-Referenz) | DIP-18 | offen | Datenblatt / 5-V-Kennwerte noch zu prüfen; Kartenreferenz: onsemi MC14513B, DIP-18 | [PDF](Datenblaetter/CD4xxx/CD4513_MC14513B_onsemi_Referenz.pdf) | [Bild](images/CD4xxx/CD4513_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4513_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4513_karte_45x55mm.svg) |
| CD4518 | 2 BCD-Zähler | DIP-16 | offen | +5 V; Takt-/Enable-Beschaltung beachten | [PDF](Datenblaetter/CD4xxx/CD4518_TI.pdf) | [Bild](images/CD4xxx/CD4518_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4518_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4518_karte_45x55mm.svg) |
| CD4520 | 2 4-Bit-Binärzähler | DIP-16 | offen | +5 V; Takt-/Enable-Beschaltung beachten | [PDF](Datenblaetter/CD4xxx/CD4520_TI.pdf) | [Bild](images/CD4xxx/CD4520_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4520_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4520_karte_45x55mm.svg) |
| CD4528 | 2 monostabile Multivibratoren | DIP-16 | offen | Datenblatt / 5-V-Kennwerte noch zu prüfen | noch offen | [Bild](images/CD4xxx/CD4528_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4528_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4528_karte_45x55mm.svg) |
| CD4538 | 2 monostabile Multivibratoren (Präzisions-Monoflops) | DIP-16 | offen | Datenblatt / 5-V-Kennwerte noch zu prüfen; Typzuordnung vorläufig | noch offen | [Bild](images/CD4xxx/CD4538_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4538_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4538_karte_45x55mm.svg) |
| CD4541 | Programmierbarer Timer mit Oszillator und Binärteiler | DIP-14 | offen | +5 V; Bei 5 V externen Master-Reset vorsehen; zuverlässiger automatischer Einschalt-Reset laut Datenblatt erst oberhalb 5 V | [PDF](Datenblaetter/CD4xxx/CD4541_TI.pdf) | [Bild](images/CD4xxx/CD4541_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4541_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4541_karte_45x55mm.svg) |
| CD4543 | BCD-Latch mit 7-Segment-Decoder/Treiber | DIP-16 | offen | +5 V; Phasensteuerung; für LCD bzw. geeignete Anzeige-Beschaltung | [PDF](Datenblaetter/CD4xxx/CD4543_TI.pdf) | [Bild](images/CD4xxx/CD4543_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4543_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4543_karte_45x55mm.svg) |
| CD4553 | 3-stelliger BCD-Zähler mit Multiplex-Ausgängen | DIP-16 | offen | +5 V; Referenz MC14553B: genaue Hersteller-/Typzuordnung am IC prüfen; externer Decoder/Anzeigetreiber erforderlich | [PDF](Datenblaetter/CD4xxx/CD4553_MC14553B_Motorola_Referenz.pdf) | [Bild](images/CD4xxx/CD4553_karte_45x55mm.png) / [PDF](images/CD4xxx/CD4553_karte_45x55mm.pdf) / [SVG](images/CD4xxx/CD4553_karte_45x55mm.svg) |

## IC-Bestand: Diverse

**21 Einträge** aus der Diverse- und SN7xxx-Fotoauswertung. Die acht Spannungsregler und das MPQ2222A-Transistorarray stehen jetzt in den entsprechenden Kategorien. Relais und weitere ICs bleiben hier; Stückzahlen bleiben offen.

Die Versorgung ist bausteinspezifisch. Bei Spannungsreglern nennt die Funktion die **Ausgangsspannung**, nicht die Eingangsspannung. Für 20 Einträge liegen lokale Datenblätter bzw. gekennzeichnete Referenzen im [Datenblattverzeichnis Diverse](Datenblaetter/Diverse/README.md) vor. Für LH6764-20 ist noch keine belastbare Zuordnung gefunden. Unsichere Lesarten stehen im [Erkennungsprotokoll](Quellen/weitere_diverse_Auswertung.md).

| Bezeichnung laut Aufdruck / Übersicht | Typ / Funktion | Gehäuse | Anzahl | Nachweis / Hinweise | Datenblatt | Karte |
| --- | --- | --- | --- | --- | --- | --- |
| B3CA4.5Z | Signalrelais, 2 Wechsler; Referenz FTR-B3CA4.5Z | Relais-Bauform, 8 Pins | offen | Diverse-PDF, S. 3; Familienzuordnung vorläufig; kein IC | [PDF / Referenz](Datenblaetter/Diverse/B3CA4_5Z_FTR_B3_FCL_Referenz.pdf) | – |
| COM8126 | Baudratengenerator / programmierbarer Frequenzteiler | DIP-14 | offen | SN7xxx-PDF, S. 4; SMC-Aufdruck | [PDF](Datenblaetter/Diverse/COM8126_SMC_Datenbuchauszug.pdf) | [Bild](images/Diverse/COM8126_karte_45x55mm.png) / [PDF](images/Diverse/COM8126_karte_45x55mm.pdf) / [SVG](images/Diverse/COM8126_karte_45x55mm.svg) |
| DIP05-1A72-12L | Reedrelais, MEDER electronic | DIP-Bauform | offen | Diverse-PDF, S. 3; Relais; kein IC; Anschlussbelegung im Datenblatt | [PDF](Datenblaetter/Diverse/DIP05_1A72_12L_MEDER.pdf) | – |
| L293D | 4 Halbbrücken / Motortreiber | DIP-16 | offen | Diverse-PDF, S. 1 | [PDF / Referenz](Datenblaetter/Diverse/L293_TI.pdf) | [Bild](images/Diverse/L293D_karte_45x55mm.png) / [PDF](images/Diverse/L293D_karte_45x55mm.pdf) / [SVG](images/Diverse/L293D_karte_45x55mm.svg) |
| L293NE | 4 Halbbrücken / Motortreiber | DIP-16 | offen | Diverse-PDF, S. 1; Aufdruck bei mehreren Exemplaren gleich; TI-L293-DIP-Ausführung | [PDF](Datenblaetter/Diverse/L293_TI.pdf) | [Bild](images/Diverse/L293NE_karte_45x55mm.png) / [PDF](images/Diverse/L293NE_karte_45x55mm.pdf) / [SVG](images/Diverse/L293NE_karte_45x55mm.svg) |
| LH6764-20 | Funktion noch zu prüfen | DIP-Bauform | offen | SN7xxx-PDF, S. 4; Sharp-Aufdruck | offen: Zuordnung ungeklärt | [Bild](images/Diverse/LH6764-20_karte_45x55mm.png) / [PDF](images/Diverse/LH6764-20_karte_45x55mm.pdf) / [SVG](images/Diverse/LH6764-20_karte_45x55mm.svg) |
| LM311N | Komparator | DIP-8 | offen | Diverse-PDF, S. 1 | [PDF](Datenblaetter/Diverse/LM311_ST_Historisch.pdf) | [Bild](images/Diverse/LM311N_karte_45x55mm.png) / [PDF](images/Diverse/LM311N_karte_45x55mm.pdf) / [SVG](images/Diverse/LM311N_karte_45x55mm.svg) |
| LM324N | 4 Operationsverstärker | DIP-14 | offen | Diverse-PDF, S. 1 | [PDF](Datenblaetter/Diverse/LM324_ST.pdf) | [Bild](images/Diverse/LM324N_karte_45x55mm.png) / [PDF](images/Diverse/LM324N_karte_45x55mm.pdf) / [SVG](images/Diverse/LM324N_karte_45x55mm.svg) |
| LM339AN | 4 Komparatoren | DIP-14 | offen | Diverse-PDF, S. 1 | [PDF](Datenblaetter/Diverse/LM339_ST_Historisch.pdf) | [Bild](images/Diverse/LM339AN_karte_45x55mm.png) / [PDF](images/Diverse/LM339AN_karte_45x55mm.pdf) / [SVG](images/Diverse/LM339AN_karte_45x55mm.svg) |
| LM358 | 2 Operationsverstärker | DIP-8 | offen | Diverse-PDF, S. 1; Hersteller-/Gehäusesuffix nicht lesbar | [PDF / Referenz](Datenblaetter/Diverse/LM358_TI_Referenz.pdf) | [Bild](images/Diverse/LM358_karte_45x55mm.png) / [PDF](images/Diverse/LM358_karte_45x55mm.pdf) / [SVG](images/Diverse/LM358_karte_45x55mm.svg) |
| MAX250CPD | Baustein für isolierte RS-232-Schnittstelle | DIP-14 | offen | Diverse-PDF, S. 3; Teil eines MAX250/MAX251-Chipsatzes; Lesart und Gehäuse korrigiert | [PDF](Datenblaetter/Diverse/MAX250_MAX251_Maxim.pdf) | [Bild](images/Diverse/MAX250CPD_karte_45x55mm.png) / [PDF](images/Diverse/MAX250CPD_karte_45x55mm.pdf) / [SVG](images/Diverse/MAX250CPD_karte_45x55mm.svg) |
| MAX7219CNG | LED-Anzeigetreiber mit serieller Schnittstelle | DIP-24 | offen | Diverse-PDF, S. 3 | [PDF](Datenblaetter/Diverse/MAX7219_Maxim.pdf) | [Bild](images/Diverse/MAX7219CNG_karte_45x55mm.png) / [PDF](images/Diverse/MAX7219CNG_karte_45x55mm.pdf) / [SVG](images/Diverse/MAX7219CNG_karte_45x55mm.svg) |
| MC1488 | 4 Leitungstreiber laut Übersicht | offen | offen | SN7xxx-PDF, S. 3; Übersicht | [PDF / Referenz](Datenblaetter/Diverse/MC1488_TI_Referenz.pdf) | [Bild](images/Diverse/MC1488_karte_45x55mm.png) / [PDF](images/Diverse/MC1488_karte_45x55mm.pdf) / [SVG](images/Diverse/MC1488_karte_45x55mm.svg) |
| MC1489 | 4 Leitungsempfänger laut Übersicht | offen | offen | SN7xxx-PDF, S. 3; Übersicht | [PDF / Referenz](Datenblaetter/Diverse/MC1489_TI_Referenz.pdf) | [Bild](images/Diverse/MC1489_karte_45x55mm.png) / [PDF](images/Diverse/MC1489_karte_45x55mm.pdf) / [SVG](images/Diverse/MC1489_karte_45x55mm.svg) |
| NE555 | Timer, astabiler oder monostabiler Multivibrator | DIP-8 | offen | Diverse-PDF, S. 1; Vollständigen Typzusatz prüfen | [PDF / Referenz](Datenblaetter/Diverse/NE555_TI.pdf) | [Bild](images/Diverse/NE555_karte_45x55mm.png) / [PDF](images/Diverse/NE555_karte_45x55mm.pdf) / [SVG](images/Diverse/NE555_karte_45x55mm.svg) |
| PCF8574N | 8-Bit-I/O-Expander für I²C | DIP-16 | offen | Diverse-PDF, S. 2 | [PDF](Datenblaetter/Diverse/PCF8574_TI_Referenz.pdf) | [Bild](images/Diverse/PCF8574N_karte_45x55mm.png) / [PDF](images/Diverse/PCF8574N_karte_45x55mm.pdf) / [SVG](images/Diverse/PCF8574N_karte_45x55mm.svg) |
| PS2501-4 | 4-fach-Optokoppler mit Transistorausgängen | DIP-16 | offen | Diverse-PDF, S. 2 | [PDF](Datenblaetter/Diverse/PS2501_Renesas.pdf) | [Bild](images/Diverse/PS2501-4_karte_45x55mm.png) / [PDF](images/Diverse/PS2501-4_karte_45x55mm.pdf) / [SVG](images/Diverse/PS2501-4_karte_45x55mm.svg) |
| UA78S40PC | Schaltregler-Steuerbaustein | DIP-16 | offen | Diverse-PDF, S. 1 | [PDF / Referenz](Datenblaetter/Diverse/UA78S40_onsemi_Referenz.pdf) | [Bild](images/Diverse/UA78S40PC_karte_45x55mm.png) / [PDF](images/Diverse/UA78S40PC_karte_45x55mm.pdf) / [SVG](images/Diverse/UA78S40PC_karte_45x55mm.svg) |
| ULN2004A | 7 Darlington-Treiber | DIP-16 | offen | Diverse-PDF, S. 3 | [PDF / Referenz](Datenblaetter/Diverse/ULN2004A_TI_Referenz.pdf) | [Bild](images/Diverse/ULN2004A_karte_45x55mm.png) / [PDF](images/Diverse/ULN2004A_karte_45x55mm.pdf) / [SVG](images/Diverse/ULN2004A_karte_45x55mm.svg) |
| ULN2004AG | 7 Darlington-Treiber | DIP-16 | offen | Diverse-PDF, S. 3; Hersteller-/Gehäusevariante getrennt erfasst | [PDF / Referenz](Datenblaetter/Diverse/ULN2004A_TI_Referenz.pdf) | [Bild](images/Diverse/ULN2004AG_karte_45x55mm.png) / [PDF](images/Diverse/ULN2004AG_karte_45x55mm.pdf) / [SVG](images/Diverse/ULN2004AG_karte_45x55mm.svg) |
| ULN2803A | 8 Darlington-Treiber | DIP-18 | offen | Diverse-PDF, S. 3 | [PDF](Datenblaetter/Diverse/ULN2803A_ST.pdf) | [Bild](images/Diverse/ULN2803A_karte_45x55mm.png) / [PDF](images/Diverse/ULN2803A_karte_45x55mm.pdf) / [SVG](images/Diverse/ULN2803A_karte_45x55mm.svg) |


## Bestand: Transistoren

**41 Typen.** Datenblätter und Variantenhinweise: [Transistoren](Datenblaetter/Transistor/README.md). Die Sortimentsangaben bestätigen noch nicht den Hersteller jedes vorhandenen Bauteils; Stückzahlen bleiben offen.

| Bezeichnung | Typ / Funktion | Gehäuse | Anzahl | Datenblatt | Karte |
| --- | --- | --- | --- | --- | --- |
| 2N2222 | NPN-Bipolartransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/2N2222_P2N2222A_onsemi_Referenz.pdf) | – |
| 2N3904 | NPN-Bipolartransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/2N3904_ST.pdf) | – |
| 2N3906 | PNP-Bipolartransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/2N3906_Fairchild.pdf) | – |
| 2N5401 | PNP-Bipolartransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/2N5401_Fairchild.pdf) | – |
| 2N5551 | NPN-Bipolartransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/2N5551_KEC.pdf) | – |
| 2SA1015 | PNP-Bipolartransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/2SA1015_Toshiba.pdf) | – |
| 2SB772 | PNP-Bipolartransistor | TO-126 | offen | [PDF / Referenz](Datenblaetter/Transistor/2SB772_MCC.pdf) | – |
| 2SC1815 | NPN-Bipolartransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/2SC1815_UTC.pdf) | – |
| 2SC945 | NPN-Bipolartransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/2SC945_NEC.pdf) | – |
| 2SD882 | NPN-Bipolartransistor | TO-126 | offen | [PDF / Referenz](Datenblaetter/Transistor/2SD882_ST.pdf) | – |
| BC327 | PNP-Bipolartransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/BC327_NXP.pdf) | – |
| BC337 | NPN-Bipolartransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/BC337_onsemi.pdf) | – |
| BC517 | NPN-Darlington-Transistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/BC517_onsemi.pdf) | – |
| BC546 | NPN-Kleinsignaltransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/BC546_547_548_549_550_onsemi.pdf) | – |
| BC547 | NPN-Kleinsignaltransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/BC546_547_548_549_550_onsemi.pdf) | – |
| BC548 | NPN-Kleinsignaltransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/BC546_547_548_549_550_onsemi.pdf) | – |
| BC549 | NPN-Kleinsignaltransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/BC546_547_548_549_550_onsemi.pdf) | – |
| BC550 | NPN-Kleinsignaltransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/BC546_547_548_549_550_onsemi.pdf) | – |
| BC556 | PNP-Kleinsignaltransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/BC556_557_558_onsemi.pdf) | – |
| BC557 | PNP-Kleinsignaltransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/BC556_557_558_onsemi.pdf) | – |
| BC558 | PNP-Kleinsignaltransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/BC556_557_558_onsemi.pdf) | – |
| BD139 | NPN-Bipolartransistor | TO-126 | offen | [PDF / Referenz](Datenblaetter/Transistor/BD139_140_Fairchild.pdf) | – |
| BD140 | PNP-Bipolartransistor | TO-126 | offen | [PDF / Referenz](Datenblaetter/Transistor/BD140_Fairchild.pdf) | – |
| MPQ2222A | 4 unabhängige NPN-Bipolartransistoren | DIP-14 | offen | [PDF / Referenz](Datenblaetter/Transistor/MPQ2222A_Central.pdf) | [Bild](images/Transistor/MPQ2222A_karte_45x55mm.png) / [PDF](images/Transistor/MPQ2222A_karte_45x55mm.pdf) / [SVG](images/Transistor/MPQ2222A_karte_45x55mm.svg) |
| S8050 | NPN-Bipolartransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/S8050_SS8050_Fairchild_Referenz.pdf) | – |
| S8550 | PNP-Bipolartransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/S8550_SS8550_Fairchild_Referenz.pdf) | – |
| S9012 | PNP-Bipolartransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/S9012_SS9012_Fairchild_Referenz.pdf) | – |
| S9013 | NPN-Bipolartransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/S9013_SS9013_Fairchild_Referenz.pdf) | – |
| S9014 | NPN-Bipolartransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/S9014_SS9014_Fairchild_Referenz.pdf) | – |
| S9015 | PNP-Bipolartransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/S9015_SS9015_Fairchild_Referenz.pdf) | – |
| S9018 | NPN-Bipolartransistor | TO-92 | offen | [PDF / Referenz](Datenblaetter/Transistor/S9018_SS9018_Fairchild_Referenz.pdf) | – |
| TIP120 | NPN-Leistungs-Darlingtontransistor | TO-220 | offen | [PDF / Referenz](Datenblaetter/Transistor/TIP120_121_122_ST.pdf) | – |
| TIP121 | NPN-Leistungs-Darlingtontransistor | TO-220 | offen | [PDF / Referenz](Datenblaetter/Transistor/TIP120_121_122_ST.pdf) | – |
| TIP122 | NPN-Leistungs-Darlingtontransistor | TO-220 | offen | [PDF / Referenz](Datenblaetter/Transistor/TIP120_121_122_ST.pdf) | – |
| TIP125 | PNP-Leistungs-Darlingtontransistor | TO-220 | offen | [PDF / Referenz](Datenblaetter/Transistor/TIP125_126_127_Fairchild.pdf) | – |
| TIP126 | PNP-Leistungs-Darlingtontransistor | TO-220 | offen | [PDF / Referenz](Datenblaetter/Transistor/TIP125_126_127_Fairchild.pdf) | – |
| TIP127 | PNP-Leistungs-Darlingtontransistor | TO-220 | offen | [PDF / Referenz](Datenblaetter/Transistor/TIP125_126_127_Fairchild.pdf) | – |
| TIP31C | NPN-Leistungstransistor | TO-220 | offen | [PDF / Referenz](Datenblaetter/Transistor/TIP31C_GME.pdf) | – |
| TIP32C | PNP-Leistungstransistor | TO-220 | offen | [PDF / Referenz](Datenblaetter/Transistor/TIP32C_Fairchild.pdf) | – |
| TIP41C | NPN-Leistungstransistor | TO-220 | offen | [PDF / Referenz](Datenblaetter/Transistor/TIP41C_ST.pdf) | – |
| TIP42C | PNP-Leistungstransistor | TO-220 | offen | [PDF / Referenz](Datenblaetter/Transistor/TIP41C_ST.pdf) | – |


## Bestand: MOSFETs

**4 Typen.** Datenblätter und Variantenhinweise: [MOSFETs](Datenblaetter/MOSFET/README.md). Die Sortimentsangaben bestätigen noch nicht den Hersteller jedes vorhandenen Bauteils; Stückzahlen bleiben offen.

| Bezeichnung | Typ / Funktion | Gehäuse | Anzahl | Datenblatt | Karte |
| --- | --- | --- | --- | --- | --- |
| IRF540 | N-Kanal-Leistungs-MOSFET | TO-220 | offen | [PDF / Referenz](Datenblaetter/MOSFET/IRF540_ST.pdf) | – |
| IRF9530 | P-Kanal-Leistungs-MOSFET | TO-220 | offen | [PDF / Referenz](Datenblaetter/MOSFET/IRF9530_Vishay.pdf) | – |
| IRFZ44 | N-Kanal-Leistungs-MOSFET | TO-220 | offen | [PDF / Referenz](Datenblaetter/MOSFET/IRFZ44_Thinki.pdf) | – |
| IRLZ44N | N-Kanal-Leistungs-MOSFET | TO-220 | offen | [PDF / Referenz](Datenblaetter/MOSFET/IRLZ44N_Infineon.pdf) | – |


## Bestand: Triacs und Thyristoren

**3 Typen.** Datenblätter und Variantenhinweise: [Triacs und Thyristoren](Datenblaetter/Triac_Thyristor/README.md). Die Sortimentsangaben bestätigen noch nicht den Hersteller jedes vorhandenen Bauteils; Stückzahlen bleiben offen.

| Bezeichnung | Typ / Funktion | Gehäuse | Anzahl | Datenblatt | Karte |
| --- | --- | --- | --- | --- | --- |
| BT134-600E | Triac | SOT-82 / TO-126-ähnlich | offen | [PDF / Referenz](Datenblaetter/Triac_Thyristor/BT134_600E_NXP.pdf) | – |
| BTA06 | Triac | TO-220 | offen | [PDF / Referenz](Datenblaetter/Triac_Thyristor/BTA06_ST_Familie.pdf) | – |
| MAC97A6 | Triac | TO-92 | offen | [PDF / Referenz](Datenblaetter/Triac_Thyristor/MAC97A6_NXP.pdf) | – |


## Bestand: Spannungsregler und Spannungsreferenzen

**13 Typen.** Datenblätter und Variantenhinweise: [Spannungsregler und Spannungsreferenzen](Datenblaetter/Spannungsregler/README.md). Die Sortimentsangaben bestätigen noch nicht den Hersteller jedes vorhandenen Bauteils; Stückzahlen bleiben offen.

| Bezeichnung | Typ / Funktion | Gehäuse | Anzahl | Datenblatt | Karte |
| --- | --- | --- | --- | --- | --- |
| 78L05 | Positiver Festspannungsregler, Ausgangsspannung +5 V | TO-92 | offen | [PDF / Referenz](Datenblaetter/Spannungsregler/L78L05_12_ST_Familie.pdf) | – |
| 78L12 | Positiver Festspannungsregler, Ausgangsspannung +12 V | TO-92 | offen | [PDF / Referenz](Datenblaetter/Spannungsregler/L78L05_12_ST_Familie.pdf) | – |
| 79L05 | Negativer Festspannungsregler, Ausgangsspannung -5 V | TO-92 | offen | [PDF / Referenz](Datenblaetter/Spannungsregler/L79L05_ST_Familie.pdf) | – |
| KA7909 | Negativer Festspannungsregler, Ausgangsspannung -9 V | TO-220 | offen | [PDF / Referenz](Datenblaetter/Spannungsregler/KA7909_Fairchild.pdf) | – |
| L7805CV | Positiver Festspannungsregler, Ausgangsspannung +5 V | TO-220 | offen | [PDF / Referenz](Datenblaetter/Spannungsregler/L78_ST.pdf) | – |
| L7809CV | Positiver Festspannungsregler, Ausgangsspannung +9 V | TO-220 | offen | [PDF / Referenz](Datenblaetter/Spannungsregler/L78_ST.pdf) | – |
| L7812CV | Positiver Festspannungsregler, Ausgangsspannung +12 V | TO-220 | offen | [PDF / Referenz](Datenblaetter/Spannungsregler/L78_ST.pdf) | – |
| L7815CV | Positiver Festspannungsregler, Ausgangsspannung +15 V | TO-220 | offen | [PDF / Referenz](Datenblaetter/Spannungsregler/L78_ST.pdf) | – |
| L7824CV | Positiver Festspannungsregler, Ausgangsspannung +24 V | TO-220 | offen | [PDF / Referenz](Datenblaetter/Spannungsregler/L78_ST.pdf) | – |
| L7905CV | Negativer Festspannungsregler, Ausgangsspannung -5 V | TO-220 | offen | [PDF / Referenz](Datenblaetter/Spannungsregler/L79_ST.pdf) | – |
| L7912CV | Negativer Festspannungsregler, Ausgangsspannung -12 V | TO-220 | offen | [PDF / Referenz](Datenblaetter/Spannungsregler/L79_ST.pdf) | – |
| LM317 | Einstellbarer positiver Spannungsregler | TO-220 | offen | [PDF / Referenz](Datenblaetter/Spannungsregler/LM317_TI.pdf) | – |
| TL431A | Einstellbare Shunt-Spannungsreferenz | TO-92 | offen | [PDF / Referenz](Datenblaetter/Spannungsregler/TL431_TI.pdf) | – |


## Ungeklärte Bauteilbeschriftungen

Die handschriftlichen Lesarten **MPS2507A** und **2N5501** sind nicht als gesicherte Typen eingeordnet. Details und mögliche Verwechslungen stehen in der [Fotoauswertung](Quellen/Transistoren_und_Aehnliche/Auswertung.md).

## Verwendung bei +5 V

Meine Bastelprojekte laufen überwiegend mit **+5 V**. Höhere Versorgungsspannungen wie 10 V oder 15 V werden bei CD4xxx normalerweise nicht genutzt. Für CD4xxx sind die Kennwerte der dokumentierten Referenztypen bei 5 V maßgeblich.

- Bei 74LS sind HIGH-Eingangspegel typischerweise ab 2,0 V und LOW-Pegel bis 0,8 V definiert; Schmitt-Trigger haben eigene Schaltschwellen. Maßgeblich ist jeweils das Datenblatt.
- Beim Verbinden mit CD4xxx oder 74HC müssen die garantierten Ausgangs- und Eingangspegel geprüft werden. Ein 74LS-HIGH erfüllt nicht automatisch den benötigten CMOS-HIGH-Pegel bei 5 V.
- Open-Collector-Ausgänge benötigen einen Pull-up oder eine passende Last. Strom und Spannung müssen zum konkreten Treiber passen.
- Unbenutzte Eingänge auf definierte Pegel legen; bei 3-State-Bausteinen die Freigabeeingänge beachten.
- Versorgung und Pinbelegung vor dem Aufbau prüfen: Nicht jeder DIP-14 hat GND an Pin 7 und VCC an Pin 14. Pro IC ist ein 100-nF-Abblockkondensator nahe den Versorgungspins sinnvoll.

## Verzeichnisstruktur

```text
IC_Dokumentation/
├── README.md
├── Datenblaetter/
│   ├── SN7xxx/       # Hersteller-PDFs, Quellen und Zuordnungen
│   ├── CD4xxx/
│   ├── Diverse/      # Weitere ICs und Bauteile, Datenblätter und Referenzen
│   ├── Transistor/
│   ├── MOSFET/
│   ├── Triac_Thyristor/
│   └── Spannungsregler/
└── images/
    ├── SN7xxx/       # Experimentierkarten als PNG, SVG und PDF
    ├── CD4xxx/
    ├── Diverse/
    ├── Transistor/
    └── IC_Karten_A4.pdf
```

Dateinamen beginnen mit der IC-Bezeichnung. Relative Links funktionieren auch nach der späteren Übernahme nach GitHub. Die bereitgestellte Übersicht wurde inhaltlich ausgewertet; die ursprüngliche Bilddatei ist noch nicht lokal abgelegt.
