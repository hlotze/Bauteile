# Beispielschaltungen

Die letzte Spalte in [Bauteile.md](../Bauteile.md) enthält pro zuordenbarem Bauteil ein bis drei ausgewählte Links. Stand: **21.10.2026**. Insgesamt sind 257 der 258 Einträge mit 361 Links versehen. Für **LH6764-20** bleibt die Spalte offen, weil Funktion und Datenblatt weiterhin ungeklärt sind.

Die Links führen zu konkreten Herstellerbeschaltungen, Anwendungshinweisen oder von den Autoren veröffentlichten Lehrschaltungen. Lokale Datenblätter sind mit der PDF-Seite verlinkt; die Seite steht zusätzlich im Linktitel, falls der PDF-Betrachter den Sprung nicht unterstützt. Verweise auf bloße Suchergebnisse wurden nicht aufgenommen.

**Grundschaltung** bedeutet: Das Beispiel zeigt das passende Schaltungsprinzip, verwendet aber gegebenenfalls einen anderen Baustein. Versorgung, Pinfolge, Signalpolarität, Widerstände und Grenzwerte müssen zum vorhandenen Typ passen. Das betrifft beispielsweise TTL gegenüber CMOS, PNP gegenüber NPN, Open-Collector-Ausgänge, invertierende Buspuffer sowie die gemeinsame Anode oder Kathode von Anzeigen. Bei Familien-Datenblättern ist die passende Variante maßgeblich. Die Links sind keine Bestätigung eines ungeklärten Herstelleraufdrucks.

Bei Quarzen sind die Beispiele Entwurfshilfen: Frequenzbereich, Lastkapazität und Ansteuerung müssen zum Quarz und Oszillatortreiber passen. Bei Relais gilt die Spulenspannung des vorhandenen Relais. Die TRIAC-Beispiele enthalten Netzspannungsschaltungen.

Einige besondere Zuordnungen:

- **7460:** Die TI-Unterlage beschreibt die Erweiterung passender 7450/7423/7453-Gatter über deren Expanderanschlüsse. Die Anschlüsse sind keine gewöhnlichen Logikausgänge. Referenzfamilie abgleichen.
- **7487:** Die TI-Referenz SN74H87 zeigt die Ansteuerung für Durchreichen, Invertieren und konstante 0/1. Die genaue Familie des vorhandenen ICs bleibt offen.
- **CD4528/CD4538:** Die Links verwenden ausdrücklich gekennzeichnete MC14528B-/CD14538B-Referenzen. Trigger, Pinfolge und Zeitformeln abgleichen.
- **ULN2004/ULN2803:** Das gemeinsame Treiberprinzip gilt; Eingangsnetzwerke, Kanalzahl und Pinfolge unterscheiden sich.
- **MAX250:** Das Schnittstellenbeispiel benötigt weitere Bauteile, insbesondere MAX251, Optokoppler und eine isolierte Versorgung.
- **LH6764-20:** Keine Ersatztypenbeschaltung zugeordnet.

Die maschinenlesbare Zuordnung steht in [Beispielschaltungen.json](Beispielschaltungen.json). `sources` nennt URL, Quellenart und Prüfdatum; `parts` ordnet Links und Anpassungshinweise jedem Bestandseintrag zu. Die Quellen sind unter anderem TI, ST, onsemi, Maxim, SMC, Renesas, Adafruit und die Lehrbücher von All About Circuits sowie Electronics Tutorials. Schaltbilder und Artikeltexte werden nicht kopiert.

Mit `python3 scripts/update_examples.py` werden ausschließlich die Beispielspalte in Markdown und das Feld `Beispielschaltungen` der vorhandenen SQLite-Tabelle aktualisiert. Die Bestandsdaten bleiben erhalten. Das Feld enthält dieselben Markdown-Links wie die Tabelle. Das Skript ergänzt die Spalte bei älteren Datenbanken ohne Ersetzen der Tabelle.

Der vollständige Import `scripts/build_db.py` unterstützt die neue Spalte ebenfalls, ersetzt aber weiterhin die Datenbanktabelle und darf nur auf ausdrückliche Anweisung ausgeführt werden.
