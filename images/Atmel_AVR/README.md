# Atmel AVR: DIP-Anschlusskarten

Sechs Karten im Format **45 × 55 mm**, als schematische **Draufsicht mit Kerbe oben**. Pin 1 liegt oben links; links wird nach unten, rechts nach oben gezählt. Versorgung rot, Masse hellblau. `/` kennzeichnet aktiv Low. Die Karten zeigen alle im Pinbild genannten Alternativfunktionen; ihre Verfügbarkeit hängt von Konfiguration und Fuses ab.

**Kein 5,08-mm-Boardraster:** Die Pinreihen sind für DIP-20/28/40 kompakt dargestellt, die Gehäuse sind nicht maßstäblich.

[A4-Druckbogen](AVR_Karten_A4.pdf) · [Vorschau](AVR_Karten_A4.png) · [Bestand](../../Bauteile.md#ic-bestand-atmel-avr)

Bei **100 % / tatsächlicher Größe** ohne Seitenanpassung drucken.

| Typ | Gehäuse | Vorschau | Druck | Vektor | Pinreferenz |
| --- | --- | --- | --- | --- | --- |
| ATTINY2313-20PU | DIP-20 | [PNG](ATTINY2313-20PU_karte_45x55mm.png) | [PDF](ATTINY2313-20PU_karte_45x55mm.pdf) | [SVG](ATTINY2313-20PU_karte_45x55mm.svg) | [2543M, PDF-S. 2](../../Datenblaetter/Atmel_AVR/ATtiny2313_Atmel.pdf) |
| ATMEGA8-16PU | DIP-28 | [PNG](ATMEGA8-16PU_karte_45x55mm.png) | [PDF](ATMEGA8-16PU_karte_45x55mm.pdf) | [SVG](ATMEGA8-16PU_karte_45x55mm.svg) | [2486AA, PDF-S. 2](../../Datenblaetter/Atmel_AVR/ATmega8_L_Atmel.pdf) |
| ATMEGA16-16PU | DIP-40 | [PNG](ATMEGA16-16PU_karte_45x55mm.png) | [PDF](ATMEGA16-16PU_karte_45x55mm.pdf) | [SVG](ATMEGA16-16PU_karte_45x55mm.svg) | [2466T, PDF-S. 2](../../Datenblaetter/Atmel_AVR/ATmega16_L_Atmel.pdf) |
| ATMEGA32-16PU | DIP-40 | [PNG](ATMEGA32-16PU_karte_45x55mm.png) | [PDF](ATMEGA32-16PU_karte_45x55mm.pdf) | [SVG](ATMEGA32-16PU_karte_45x55mm.svg) | [2503Q, PDF-S. 2](../../Datenblaetter/Atmel_AVR/ATmega32_L_Atmel.pdf) |
| ATMEGA32L8PI | DIP-40 | [PNG](ATMEGA32L8PI_karte_45x55mm.png) | [PDF](ATMEGA32L8PI_karte_45x55mm.pdf) | [SVG](ATMEGA32L8PI_karte_45x55mm.svg) | [2503Q, PDF-S. 2](../../Datenblaetter/Atmel_AVR/ATmega32_L_Atmel.pdf) |
| ATMEGA328P-PU | DIP-28 | [PNG](ATMEGA328P-PU_karte_45x55mm.png) | [PDF](ATMEGA328P-PU_karte_45x55mm.pdf) | [SVG](ATMEGA328P-PU_karte_45x55mm.svg) | [DS40002061B, PDF-S. 12](../../Datenblaetter/Atmel_AVR/ATmega328P_Atmel.pdf) |

ATMEGA32L8PI bleibt als Bestandsbezeichnung erhalten; Pinreferenz ist ATmega32L (zugeordnete Schreibweise ATmega32L-8PI). ATtiny2313: USCK ist der USI-Takt, im Hersteller-Pinbild steht der Druckfehler UCSK. ATmega8 und ATmega328P haben dasselbe DIP-Versorgungslayout, aber unterschiedliche Alternativfunktionen; sie besitzen eigene Karten.

Geprüfte Pinfolgen und Quellenprüfsummen: [Generator-Konfiguration](../../scripts/kaertchen/avr_pins.json), [Ausgabemanifest](karten.json). Neuerzeugung: `python3 scripts/kaertchen/avr_cards.py`.
