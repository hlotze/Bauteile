# Datenblätter: MOSFETs

**16 Typen, 14 PDF-Dateien.** Erfasst am 13.10.2026. Mehrere Typen teilen sich ein Familien-Datenblatt. Hersteller und Varianten der Sortimentsbauteile sind überwiegend nicht bestätigt; die zugeordneten Herstellerunterlagen dienen als Typreferenz. Gehäuse, Pinbelegung und Kennwerte sind am vorhandenen Bauteil zu prüfen.

Die [Fotoauswertung](../../Quellen/Transistoren_und_Aehnliche/Auswertung.md) dokumentiert alle zehn Quellen und unklare Beschriftungen. Die Dateiquellen und SHA-256-Prüfsummen stehen in [quellen.json](quellen.json).

| Typ | Funktion | Gehäuse laut Quelle | Datenblatt | Dokumenthersteller | Zuordnung | Karte |
| --- | --- | --- | --- | --- | --- | --- |
| IRF540 | N-Kanal-Leistungs-MOSFET | TO-220 | [PDF](IRF540_ST.pdf) | STMicroelectronics | Typreferenz; Hersteller am Bauteil noch zu prüfen | – |
| IRF9530 | P-Kanal-Leistungs-MOSFET | TO-220 | [PDF](IRF9530_Vishay.pdf) | Vishay Siliconix | Typreferenz; Hersteller am Bauteil noch zu prüfen | – |
| IRFZ44 | N-Kanal-Leistungs-MOSFET | TO-220 | [PDF](IRFZ44_Thinki.pdf) | Thinki Semiconductor | Typreferenz; Hersteller am Bauteil noch zu prüfen | – |
| IRLZ44N | N-Kanal-Leistungs-MOSFET | TO-220 | [PDF](IRLZ44N_Infineon.pdf) | Infineon / International Rectifier | Hersteller International Rectifier laut Nutzerangabe | – |
| IRFZ44N | N-Kanal-Leistungs-MOSFET | TO-220AB (Typreferenz) | [PDF](IRFZ44N_Infineon.pdf) | Infineon / International Rectifier | Nutzerangabe 23.10.2026; Hersteller prüfen | – |
| IRF510N | N-Kanal-Leistungs-MOSFET | TO-220AB (Typreferenz) | [PDF / IRF510-Referenz](IRF510N_Vishay_IRF510_Referenz.pdf) | Vishay Siliconix | N-Suffix ungeklärt; nur IRF510-Referenz | – |
| IRF520N | N-Kanal-Leistungs-MOSFET | TO-220AB (Typreferenz) | [PDF](IRF520N_Infineon.pdf) | Infineon / International Rectifier | Nutzerangabe 23.10.2026; Hersteller prüfen | – |
| IRF530N | N-Kanal-Leistungs-MOSFET | TO-220AB (Typreferenz) | [PDF](IRF530N_Infineon.pdf) | Infineon / International Rectifier | Nutzerangabe 23.10.2026; Hersteller prüfen | – |
| IRF540N | N-Kanal-Leistungs-MOSFET | TO-220AB (Typreferenz) | [PDF](IRF540N_Infineon.pdf) | Infineon / International Rectifier | Nutzerangabe 23.10.2026; Hersteller prüfen | – |
| IRF640N | N-Kanal-Leistungs-MOSFET | TO-220AB (Typreferenz) | [PDF](IRF640N_Infineon.pdf) | Infineon / International Rectifier | Nutzerangabe 23.10.2026; Hersteller prüfen | – |
| IRF740 | N-Kanal-Leistungs-MOSFET | TO-220AB (Typreferenz) | [PDF](IRF740_Vishay.pdf) | Vishay Siliconix | Nutzerangabe 23.10.2026; Hersteller prüfen | – |
| IRF840 | N-Kanal-Leistungs-MOSFET | TO-220AB (Typreferenz) | [PDF](IRF840_Vishay.pdf) | Vishay Siliconix | Nutzerangabe 23.10.2026; Hersteller prüfen | – |
| IRF3205 | N-Kanal-Leistungs-MOSFET | TO-220AB (Typreferenz) | [PDF](IRF3205_Infineon.pdf) | Infineon / International Rectifier | Nutzerangabe 23.10.2026; Hersteller prüfen | – |
| IRF9540N | P-Kanal-Leistungs-MOSFET | TO-220AB (Typreferenz) | [PDF](IRF9540N_Infineon.pdf) | Infineon / International Rectifier | Nutzerangabe 23.10.2026; Hersteller prüfen | – |
| IRF9530PBF | P-Kanal-Leistungs-MOSFET | TO-220 | [PDF](IRF9530_Vishay.pdf) | Vishay Siliconix | Vollständige PbF-Bezeichnung laut Nutzerangabe; 12 Stück | – |
| IRF520NPBF | N-Kanal-Leistungs-MOSFET | TO-220 | [PDF](IRF520N_Infineon.pdf) | Infineon / International Rectifier | Vollständige PbF-Bezeichnung laut Nutzerangabe; 12 Stück | – |

## Hinweise pro Typ

- **IRF540:** Kein Logikpegel-MOSFET; RDS(on) bei der tatsächlichen Gatespannung prüfen. Nachweis: [Foto-PDF](../../Quellen/Transistoren_und_Aehnliche/Transistoren_und_Aehnliche_2.pdf#page=1). [Downloadquelle](https://datasheet4u.com/pdf/1595928/IRF540.pdf).
- **IRF9530:** Verpackungsaufkleber nennt IRF9530PBF; bleifreie Ausführung des Grundtyps, keine N-Variante unterstellen. Nachweis: [Foto-PDF](../../Quellen/Transistoren_und_Aehnliche/Transistoren_und_Aehnliche_9.pdf#page=1). [Downloadquelle](https://datasheet4u.com/pdf/951206/IRF9530.pdf).
- **IRFZ44:** Sortiment nennt IRFZ44 ohne N; IRFZ44N wird nicht zusätzlich unterstellt. Nachweis: [Foto-PDF](../../Quellen/Transistoren_und_Aehnliche/Transistoren_und_Aehnliche_2.pdf#page=1). [Downloadquelle](https://datasheet4u.com/pdf/1134157/IRFZ44.pdf).
- **IRLZ44N:** 30 Stück von International Rectifier laut Nutzerangabe vom 23.10.2026. Das vorhandene IRLZ44NPbF-Datenblatt dient als Referenz für den Grundtyp; PbF-Suffix am Bestand nicht bestätigt.

Die Gate-Schwellenspannung beschreibt nicht das vollständige Durchschalten. Für die gewünschte Ansteuerung den garantierten RDS(on) bei der tatsächlichen Gatespannung prüfen.

Ergänzung vom 23.10.2026: je 5 Stück für zehn weitere Bezeichnungen laut Nutzerangabe. IRFZ44N und IRF540N werden getrennt von IRFZ44 und IRF540 geführt. Für IRF510N liegt nur das IRF510-Datenblatt ohne N als ausdrücklich ungeklärte Typreferenz vor. Die Grenzwerte folgen den jeweils gespeicherten PDF-Versionen; neuere Herstellerrevisionen können abweichen.

Ergänzung vom 23.10.2026: IRF9530PBF und IRF520NPBF mit je 12 Stück separat erfasst. IRF520NPBF: Nutzerangabe 7 A; das verlinkte Datenblatt spezifiziert 9,7 A bei TC=25 °C und 6,8 A bei TC=100 °C.
