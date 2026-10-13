# Datenblätter: MOSFETs

**4 Typen, 4 PDF-Dateien.** Erfasst am 13.10.2026. Mehrere Typen teilen sich ein Familien-Datenblatt. Hersteller und Varianten der Sortimentsbauteile sind überwiegend nicht bestätigt; die zugeordneten Herstellerunterlagen dienen als Typreferenz. Gehäuse, Pinbelegung und Kennwerte sind am vorhandenen Bauteil zu prüfen.

Die [Fotoauswertung](../../Quellen/Transistoren_und_Aehnliche/Auswertung.md) dokumentiert alle zehn Quellen und unklare Beschriftungen. Die Dateiquellen und SHA-256-Prüfsummen stehen in [quellen.json](quellen.json).

| Typ | Funktion | Gehäuse laut Quelle | Datenblatt | Dokumenthersteller | Zuordnung | Karte |
| --- | --- | --- | --- | --- | --- | --- |
| IRF540 | N-Kanal-Leistungs-MOSFET | TO-220 | [PDF](IRF540_ST.pdf) | STMicroelectronics | Typreferenz; Hersteller am Bauteil noch zu prüfen | – |
| IRF9530 | P-Kanal-Leistungs-MOSFET | TO-220 | [PDF](IRF9530_Vishay.pdf) | Vishay Siliconix | Typreferenz; Hersteller am Bauteil noch zu prüfen | – |
| IRFZ44 | N-Kanal-Leistungs-MOSFET | TO-220 | [PDF](IRFZ44_Thinki.pdf) | Thinki Semiconductor | Typreferenz; Hersteller am Bauteil noch zu prüfen | – |
| IRLZ44N | N-Kanal-Leistungs-MOSFET | TO-220 | [PDF](IRLZ44N_Infineon.pdf) | Infineon / International Rectifier | Typreferenz; Hersteller am Bauteil noch zu prüfen | – |

## Hinweise pro Typ

- **IRF540:** Kein Logikpegel-MOSFET; RDS(on) bei der tatsächlichen Gatespannung prüfen. Nachweis: [Foto-PDF](../../Quellen/Transistoren_und_Aehnliche/Transistoren_und_Aehnliche_2.pdf#page=1). [Downloadquelle](https://datasheet4u.com/pdf/1595928/IRF540.pdf).
- **IRF9530:** Verpackungsaufkleber nennt IRF9530PBF; bleifreie Ausführung des Grundtyps, keine N-Variante unterstellen. Nachweis: [Foto-PDF](../../Quellen/Transistoren_und_Aehnliche/Transistoren_und_Aehnliche_9.pdf#page=1). [Downloadquelle](https://datasheet4u.com/pdf/951206/IRF9530.pdf).
- **IRFZ44:** Sortiment nennt IRFZ44 ohne N; IRFZ44N wird nicht zusätzlich unterstellt. Nachweis: [Foto-PDF](../../Quellen/Transistoren_und_Aehnliche/Transistoren_und_Aehnliche_2.pdf#page=1). [Downloadquelle](https://datasheet4u.com/pdf/1134157/IRFZ44.pdf).
- **IRLZ44N:** Nur abgedrucktes Datenblatt erkennbar; vorhandenen Bauteilaufdruck prüfen. Referenz IRLZ44NPbF; Logikpegel-Gate, Kennwerte bei 4/5 V prüfen. Nachweis: [Foto-PDF](../../Quellen/Transistoren_und_Aehnliche/Transistoren_und_Aehnliche_8.pdf#page=1). [Downloadquelle](https://www.infineon.com/assets/row/public/documents/24/49/infineon-irlz44n-datasheet-en.pdf).

Die Gate-Schwellenspannung beschreibt nicht das vollständige Durchschalten. Für die gewünschte Ansteuerung den garantierten RDS(on) bei der tatsächlichen Gatespannung prüfen.
