# Datenblätter: Triacs und Thyristoren

**3 Typen, 3 PDF-Dateien.** Erfasst am 13.10.2026. Mehrere Typen teilen sich ein Familien-Datenblatt. Hersteller und Varianten der Sortimentsbauteile sind überwiegend nicht bestätigt; die zugeordneten Herstellerunterlagen dienen als Typreferenz. Gehäuse, Pinbelegung und Kennwerte sind am vorhandenen Bauteil zu prüfen.

Die [Fotoauswertung](../../Quellen/Transistoren_und_Aehnliche/Auswertung.md) dokumentiert alle zehn Quellen und unklare Beschriftungen. Die Dateiquellen und SHA-256-Prüfsummen stehen in [quellen.json](quellen.json).

| Typ | Funktion | Gehäuse laut Quelle | Datenblatt | Dokumenthersteller | Zuordnung | Karte |
| --- | --- | --- | --- | --- | --- | --- |
| BT134-600E | Triac | SOT-82 / TO-126-ähnlich | [PDF](BT134_600E_NXP.pdf) | NXP | Typreferenz; Hersteller am Bauteil noch zu prüfen | – |
| BTA06 | Triac | TO-220 | [PDF](BTA06_ST_Familie.pdf) | STMicroelectronics | Typreferenz; Hersteller am Bauteil noch zu prüfen | – |
| MAC97A6 | Triac | TO-92 | [PDF](MAC97A6_NXP.pdf) | NXP | Typreferenz; Hersteller am Bauteil noch zu prüfen | – |

## Hinweise pro Typ

- **BT134-600E:** Kitaufkleber nennt TO-126; die NXP-Referenz nennt SOT-82. Konkretes Gehäuse und Anschlussbelegung am Bauteil prüfen. Nachweis: [Foto-PDF](../../Quellen/Transistoren_und_Aehnliche/Transistoren_und_Aehnliche_2.pdf#page=1). [Downloadquelle](https://datasheet4u.com/pdf/121545/BT134-600E.pdf).
- **BTA06:** Aufkleber nennt nur BTA06. Spannungs- und Gate-Empfindlichkeitssuffix fehlen; Familienreferenz, keine genaue BTA06-600-Ausführung bestätigt. Nachweis: [Foto-PDF](../../Quellen/Transistoren_und_Aehnliche/Transistoren_und_Aehnliche_2.pdf#page=1). [Downloadquelle](https://datasheet4u.com/pdf/122146/BTA06D.pdf).
- **MAC97A6:** Triac, kein einzelner Thyristor. Nachweis: [Foto-PDF](../../Quellen/Transistoren_und_Aehnliche/Transistoren_und_Aehnliche_2.pdf#page=1). [Downloadquelle](https://datasheet4u.com/pdf/1245934/MAC97A6.pdf).

Alle drei erkannten Typen sind Triacs. Ein zusätzlicher einzelner Thyristor wurde nicht bestätigt. Die Bezeichnungen Emitter/Base auf dem Kitaufkleber sind für Triacs ungeeignet; maßgeblich sind MT1/MT2/Gate laut passender Ausführung.
