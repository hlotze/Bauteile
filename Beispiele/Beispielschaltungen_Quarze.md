# Schaltungsbeispiele: Quarze

[Übersicht](README.md) · [Gesamtsammlung](Beispielschaltungen.md) · [Recherchebedarf](Recherchebedarf.md) · [Bestand](../Bauteile.md)

10 Bauteile, 60 Linkzuordnungen. Erweiterungsstand: **25.10.2026**; Prüfdatum jeweils am Link.

Ziel sind etwa **fünf unterschiedliche Websites pro Bauteil**. Gezählt werden Websites mit Schaltungsbeispielen, übertragbaren Grundschaltungen, Modulbeispielen oder Code mit Anschlusszuordnung. Reine Funktions-/Prinzipreferenzen und Entwurfshilfen zählen zusätzlich als Quellen, aber nicht zum Beispielziel. Subdomains und bekannte Länderspiegel zählen zusammen. Mehrere Artikel derselben Website erhöhen die Zahl nicht.

**Grundschaltung** bedeutet: Das Schaltungsprinzip ist übertragbar, der Artikel verwendet gegebenenfalls ein anderes Bauteil. Sie ist keine Bestätigung der Pinbelegung oder Dimensionierung des vorhandenen Typs. **Modulbeispiele** enthalten zusätzliche Komponenten; **Funktionsreferenzen** sind keine vollständigen Nachbauschaltungen. Hinweise stehen direkt beim Bauteil und Link.

Versorgung, Pinfolge, Polarität, Logikfamilie, Freigaben, Taktflanken und Grenzwerte anhand des konkreten Datenblatts prüfen. 74LS benötigt +5 V. Pro IC üblicherweise 100 nF abblocken, Taster für Zähler entprellen. Transistor- und Diodenwerte an Last und Verlustleistung anpassen. Bei Relais gilt die tatsächliche Spulenspannung. TRIAC-Artikel können Netzspannungsschaltungen enthalten.

Pflege: [Beispielschaltungen.json](Beispielschaltungen.json). `python3 scripts/update_examples.py` erzeugt ausschließlich diese Sammlungen. Bestand und Datenbank bleiben unverändert. Bei lokalen PDFs führt „Online-Original“ zur dokumentierten Downloadquelle; neuere Revisionen können andere Seitenzahlen haben.

## Quarz 32,768 kHz

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Pierce-Oszillator (ST)](https://www.st.com/resource/en/application_note/an2867-guidelines-for-oscillator-design-on-stm8afals-and-stm32-mcusmpus-stmicroelectronics.pdf) — st.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [Quarzoszillator (Grundschaltung)](https://www.allaboutcircuits.com/textbook/designing-analog-chips/timers-and-oscillators/crystal-oscillators/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Quarzoszillatoren mit diskreter und IC-Verstärkung](https://www.electronics-tutorials.ws/oscillator/crystal.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [AN826: Quarzoszillator und Lastkapazität](https://ww1.microchip.com/downloads/en/appnotes/00826a.pdf) — microchip.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
- [AN14518: Quarzoszillator auslegen und messen](https://www.nxp.jp/docs/en/application-note/AN14518.pdf) — nxp.com; Entwurfshilfe; geprüft 2026-10-25.
  Hinweis: Reader-IC-spezifische Beispiele; zulässigen Frequenzbereich und Last des tatsächlichen Oszillatortreibers prüfen.
- [RC- und quarzgesteuerte Taktgeneratoren](https://learnabout-electronics.org/Digital/dig51.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundprinzip; Zielschaltung und Lastkapazitäten auf die angegebene Frequenz, Quarzart und den zulässigen Ansteuerpegel auslegen. Entwurfshilfen mit unterschiedlichen Frequenzbereichen. Eine gleiche Frequenz allein bestätigt weder Lastkapazität, Schwingmodus noch zulässige Anregungsleistung des vorhandenen Quarzes.

## Quarz 4 MHz

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Pierce-Oszillator (ST)](https://www.st.com/resource/en/application_note/an2867-guidelines-for-oscillator-design-on-stm8afals-and-stm32-mcusmpus-stmicroelectronics.pdf) — st.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [Quarzoszillator (Grundschaltung)](https://www.allaboutcircuits.com/textbook/designing-analog-chips/timers-and-oscillators/crystal-oscillators/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Quarzoszillatoren mit diskreter und IC-Verstärkung](https://www.electronics-tutorials.ws/oscillator/crystal.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [AN826: Quarzoszillator und Lastkapazität](https://ww1.microchip.com/downloads/en/appnotes/00826a.pdf) — microchip.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
- [AN14518: Quarzoszillator auslegen und messen](https://www.nxp.jp/docs/en/application-note/AN14518.pdf) — nxp.com; Entwurfshilfe; geprüft 2026-10-25.
  Hinweis: Reader-IC-spezifische Beispiele; zulässigen Frequenzbereich und Last des tatsächlichen Oszillatortreibers prüfen.
- [RC- und quarzgesteuerte Taktgeneratoren](https://learnabout-electronics.org/Digital/dig51.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundprinzip; Zielschaltung und Lastkapazitäten auf die angegebene Frequenz, Quarzart und den zulässigen Ansteuerpegel auslegen. Entwurfshilfen mit unterschiedlichen Frequenzbereichen. Eine gleiche Frequenz allein bestätigt weder Lastkapazität, Schwingmodus noch zulässige Anregungsleistung des vorhandenen Quarzes.

## Quarz 6 MHz

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Pierce-Oszillator (ST)](https://www.st.com/resource/en/application_note/an2867-guidelines-for-oscillator-design-on-stm8afals-and-stm32-mcusmpus-stmicroelectronics.pdf) — st.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [Quarzoszillator (Grundschaltung)](https://www.allaboutcircuits.com/textbook/designing-analog-chips/timers-and-oscillators/crystal-oscillators/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Quarzoszillatoren mit diskreter und IC-Verstärkung](https://www.electronics-tutorials.ws/oscillator/crystal.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [AN826: Quarzoszillator und Lastkapazität](https://ww1.microchip.com/downloads/en/appnotes/00826a.pdf) — microchip.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
- [AN14518: Quarzoszillator auslegen und messen](https://www.nxp.jp/docs/en/application-note/AN14518.pdf) — nxp.com; Entwurfshilfe; geprüft 2026-10-25.
  Hinweis: Reader-IC-spezifische Beispiele; zulässigen Frequenzbereich und Last des tatsächlichen Oszillatortreibers prüfen.
- [RC- und quarzgesteuerte Taktgeneratoren](https://learnabout-electronics.org/Digital/dig51.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundprinzip; Zielschaltung und Lastkapazitäten auf die angegebene Frequenz, Quarzart und den zulässigen Ansteuerpegel auslegen. Entwurfshilfen mit unterschiedlichen Frequenzbereichen. Eine gleiche Frequenz allein bestätigt weder Lastkapazität, Schwingmodus noch zulässige Anregungsleistung des vorhandenen Quarzes.

## Quarz 8 MHz

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Pierce-Oszillator (ST)](https://www.st.com/resource/en/application_note/an2867-guidelines-for-oscillator-design-on-stm8afals-and-stm32-mcusmpus-stmicroelectronics.pdf) — st.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [Quarzoszillator (Grundschaltung)](https://www.allaboutcircuits.com/textbook/designing-analog-chips/timers-and-oscillators/crystal-oscillators/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Quarzoszillatoren mit diskreter und IC-Verstärkung](https://www.electronics-tutorials.ws/oscillator/crystal.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [AN826: Quarzoszillator und Lastkapazität](https://ww1.microchip.com/downloads/en/appnotes/00826a.pdf) — microchip.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
- [AN14518: Quarzoszillator auslegen und messen](https://www.nxp.jp/docs/en/application-note/AN14518.pdf) — nxp.com; Entwurfshilfe; geprüft 2026-10-25.
  Hinweis: Reader-IC-spezifische Beispiele; zulässigen Frequenzbereich und Last des tatsächlichen Oszillatortreibers prüfen.
- [RC- und quarzgesteuerte Taktgeneratoren](https://learnabout-electronics.org/Digital/dig51.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundprinzip; Zielschaltung und Lastkapazitäten auf die angegebene Frequenz, Quarzart und den zulässigen Ansteuerpegel auslegen. Entwurfshilfen mit unterschiedlichen Frequenzbereichen. Eine gleiche Frequenz allein bestätigt weder Lastkapazität, Schwingmodus noch zulässige Anregungsleistung des vorhandenen Quarzes.

## Quarz 11,0592 MHz

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Pierce-Oszillator (ST)](https://www.st.com/resource/en/application_note/an2867-guidelines-for-oscillator-design-on-stm8afals-and-stm32-mcusmpus-stmicroelectronics.pdf) — st.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [Quarzoszillator (Grundschaltung)](https://www.allaboutcircuits.com/textbook/designing-analog-chips/timers-and-oscillators/crystal-oscillators/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Quarzoszillatoren mit diskreter und IC-Verstärkung](https://www.electronics-tutorials.ws/oscillator/crystal.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [AN826: Quarzoszillator und Lastkapazität](https://ww1.microchip.com/downloads/en/appnotes/00826a.pdf) — microchip.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
- [AN14518: Quarzoszillator auslegen und messen](https://www.nxp.jp/docs/en/application-note/AN14518.pdf) — nxp.com; Entwurfshilfe; geprüft 2026-10-25.
  Hinweis: Reader-IC-spezifische Beispiele; zulässigen Frequenzbereich und Last des tatsächlichen Oszillatortreibers prüfen.
- [RC- und quarzgesteuerte Taktgeneratoren](https://learnabout-electronics.org/Digital/dig51.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundprinzip; Zielschaltung und Lastkapazitäten auf die angegebene Frequenz, Quarzart und den zulässigen Ansteuerpegel auslegen. Entwurfshilfen mit unterschiedlichen Frequenzbereichen. Eine gleiche Frequenz allein bestätigt weder Lastkapazität, Schwingmodus noch zulässige Anregungsleistung des vorhandenen Quarzes.

## Quarz 12 MHz

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Pierce-Oszillator (ST)](https://www.st.com/resource/en/application_note/an2867-guidelines-for-oscillator-design-on-stm8afals-and-stm32-mcusmpus-stmicroelectronics.pdf) — st.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [Quarzoszillator (Grundschaltung)](https://www.allaboutcircuits.com/textbook/designing-analog-chips/timers-and-oscillators/crystal-oscillators/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Quarzoszillatoren mit diskreter und IC-Verstärkung](https://www.electronics-tutorials.ws/oscillator/crystal.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [AN826: Quarzoszillator und Lastkapazität](https://ww1.microchip.com/downloads/en/appnotes/00826a.pdf) — microchip.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
- [AN14518: Quarzoszillator auslegen und messen](https://www.nxp.jp/docs/en/application-note/AN14518.pdf) — nxp.com; Entwurfshilfe; geprüft 2026-10-25.
  Hinweis: Reader-IC-spezifische Beispiele; zulässigen Frequenzbereich und Last des tatsächlichen Oszillatortreibers prüfen.
- [RC- und quarzgesteuerte Taktgeneratoren](https://learnabout-electronics.org/Digital/dig51.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundprinzip; Zielschaltung und Lastkapazitäten auf die angegebene Frequenz, Quarzart und den zulässigen Ansteuerpegel auslegen. Entwurfshilfen mit unterschiedlichen Frequenzbereichen. Eine gleiche Frequenz allein bestätigt weder Lastkapazität, Schwingmodus noch zulässige Anregungsleistung des vorhandenen Quarzes.

## Quarz 13,56 MHz

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Pierce-Oszillator (ST)](https://www.st.com/resource/en/application_note/an2867-guidelines-for-oscillator-design-on-stm8afals-and-stm32-mcusmpus-stmicroelectronics.pdf) — st.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [Quarzoszillator (Grundschaltung)](https://www.allaboutcircuits.com/textbook/designing-analog-chips/timers-and-oscillators/crystal-oscillators/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Quarzoszillatoren mit diskreter und IC-Verstärkung](https://www.electronics-tutorials.ws/oscillator/crystal.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [AN826: Quarzoszillator und Lastkapazität](https://ww1.microchip.com/downloads/en/appnotes/00826a.pdf) — microchip.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
- [AN14518: Quarzoszillator auslegen und messen](https://www.nxp.jp/docs/en/application-note/AN14518.pdf) — nxp.com; Entwurfshilfe; geprüft 2026-10-25.
  Hinweis: Reader-IC-spezifische Beispiele; zulässigen Frequenzbereich und Last des tatsächlichen Oszillatortreibers prüfen.
- [RC- und quarzgesteuerte Taktgeneratoren](https://learnabout-electronics.org/Digital/dig51.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundprinzip; Zielschaltung und Lastkapazitäten auf die angegebene Frequenz, Quarzart und den zulässigen Ansteuerpegel auslegen. Entwurfshilfen mit unterschiedlichen Frequenzbereichen. Eine gleiche Frequenz allein bestätigt weder Lastkapazität, Schwingmodus noch zulässige Anregungsleistung des vorhandenen Quarzes.

## Quarz 16 MHz

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Pierce-Oszillator (ST)](https://www.st.com/resource/en/application_note/an2867-guidelines-for-oscillator-design-on-stm8afals-and-stm32-mcusmpus-stmicroelectronics.pdf) — st.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [Quarzoszillator (Grundschaltung)](https://www.allaboutcircuits.com/textbook/designing-analog-chips/timers-and-oscillators/crystal-oscillators/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Quarzoszillatoren mit diskreter und IC-Verstärkung](https://www.electronics-tutorials.ws/oscillator/crystal.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [AN826: Quarzoszillator und Lastkapazität](https://ww1.microchip.com/downloads/en/appnotes/00826a.pdf) — microchip.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
- [AN14518: Quarzoszillator auslegen und messen](https://www.nxp.jp/docs/en/application-note/AN14518.pdf) — nxp.com; Entwurfshilfe; geprüft 2026-10-25.
  Hinweis: Reader-IC-spezifische Beispiele; zulässigen Frequenzbereich und Last des tatsächlichen Oszillatortreibers prüfen.
- [RC- und quarzgesteuerte Taktgeneratoren](https://learnabout-electronics.org/Digital/dig51.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundprinzip; Zielschaltung und Lastkapazitäten auf die angegebene Frequenz, Quarzart und den zulässigen Ansteuerpegel auslegen. Entwurfshilfen mit unterschiedlichen Frequenzbereichen. Eine gleiche Frequenz allein bestätigt weder Lastkapazität, Schwingmodus noch zulässige Anregungsleistung des vorhandenen Quarzes.

## Quarz 22,1184 MHz

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Pierce-Oszillator (ST)](https://www.st.com/resource/en/application_note/an2867-guidelines-for-oscillator-design-on-stm8afals-and-stm32-mcusmpus-stmicroelectronics.pdf) — st.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [Quarzoszillator (Grundschaltung)](https://www.allaboutcircuits.com/textbook/designing-analog-chips/timers-and-oscillators/crystal-oscillators/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Quarzoszillatoren mit diskreter und IC-Verstärkung](https://www.electronics-tutorials.ws/oscillator/crystal.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [AN826: Quarzoszillator und Lastkapazität](https://ww1.microchip.com/downloads/en/appnotes/00826a.pdf) — microchip.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
- [AN14518: Quarzoszillator auslegen und messen](https://www.nxp.jp/docs/en/application-note/AN14518.pdf) — nxp.com; Entwurfshilfe; geprüft 2026-10-25.
  Hinweis: Reader-IC-spezifische Beispiele; zulässigen Frequenzbereich und Last des tatsächlichen Oszillatortreibers prüfen.
- [RC- und quarzgesteuerte Taktgeneratoren](https://learnabout-electronics.org/Digital/dig51.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundprinzip; Zielschaltung und Lastkapazitäten auf die angegebene Frequenz, Quarzart und den zulässigen Ansteuerpegel auslegen. Entwurfshilfen mit unterschiedlichen Frequenzbereichen. Eine gleiche Frequenz allein bestätigt weder Lastkapazität, Schwingmodus noch zulässige Anregungsleistung des vorhandenen Quarzes.

## Quarz 27 MHz

**5/5 Beispiel-Websites**, 6 Quellen-Websites insgesamt. Ziel erreicht.

- [Pierce-Oszillator (ST)](https://www.st.com/resource/en/application_note/an2867-guidelines-for-oscillator-design-on-stm8afals-and-stm32-mcusmpus-stmicroelectronics.pdf) — st.com; Hersteller-Anwendungshinweis; geprüft 2026-10-21.
- [Quarzoszillator (Grundschaltung)](https://www.allaboutcircuits.com/textbook/designing-analog-chips/timers-and-oscillators/crystal-oscillators/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Quarzoszillatoren mit diskreter und IC-Verstärkung](https://www.electronics-tutorials.ws/oscillator/crystal.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-25.
- [AN826: Quarzoszillator und Lastkapazität](https://ww1.microchip.com/downloads/en/appnotes/00826a.pdf) — microchip.com; Hersteller-Grundschaltung; geprüft 2026-10-25.
- [AN14518: Quarzoszillator auslegen und messen](https://www.nxp.jp/docs/en/application-note/AN14518.pdf) — nxp.com; Entwurfshilfe; geprüft 2026-10-25.
  Hinweis: Reader-IC-spezifische Beispiele; zulässigen Frequenzbereich und Last des tatsächlichen Oszillatortreibers prüfen.
- [RC- und quarzgesteuerte Taktgeneratoren](https://learnabout-electronics.org/Digital/dig51.php) — learnabout-electronics.org; Grundschaltung; geprüft 2026-10-25.

Grundprinzip; Zielschaltung und Lastkapazitäten auf die angegebene Frequenz, Quarzart und den zulässigen Ansteuerpegel auslegen. Entwurfshilfen mit unterschiedlichen Frequenzbereichen. Eine gleiche Frequenz allein bestätigt weder Lastkapazität, Schwingmodus noch zulässige Anregungsleistung des vorhandenen Quarzes.
