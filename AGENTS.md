# Bestandsänderungen

`Bauteile.md` ist die führende Quelle für den Bauteilbestand. Bei Abweichungen `Bauteile.db` anhand der Markdown-Datei aktualisieren und alle Bestandsfelder abgleichen.

`scripts/build_db.py` ersetzt die Datenbank aus Markdown und Quellen. Diesen Import nur auf ausdrückliche Anweisung ausführen, da er die Datenbank vollständig ersetzt.

Beispielschaltungen werden in `Beispiele/Beispielschaltungen.json` gepflegt. `python3 scripts/update_examples.py` erzeugt ausschließlich die separaten Linksammlungen `Beispiele/Beispielschaltungen.md`, die Gruppendateien `Beispiele/Beispielschaltungen_*.md` sowie Übersicht und Recherchebedarf in `Beispiele/`. Beispielschaltungen gehören nicht in die Bestandstabellen von `Bauteile.md` und `Bauteile.db`. Links auf Grundschaltungen und andere Referenztypen müssen als solche erkennbar sein; ungeklärten Typen keine erfundene Beschaltung zuordnen.

Ziel sind etwa fünf unterschiedliche Websites mit Beispielen pro Bauteil. Subdomains und Länderspiegel desselben Anbieters zählen zusammen; reine Funktions-/Prinzipreferenzen und Entwurfshilfen zählen nicht als Schaltungsbeispiele. Lücken ausdrücklich dokumentieren.
