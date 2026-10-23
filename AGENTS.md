# Bestandsänderungen

`Bauteile.md` ist die führende Quelle für den Bauteilbestand. Bei Abweichungen `Bauteile.db` anhand der Markdown-Datei aktualisieren und alle Bestandsfelder abgleichen.

`scripts/build_db.py` ersetzt die Datenbank aus Markdown und Quellen. Diesen Import nur auf ausdrückliche Anweisung ausführen, da er die Datenbank vollständig ersetzt.

Beispielschaltungen werden in `Quellen/Beispielschaltungen.json` gepflegt. `python3 scripts/update_examples.py` aktualisiert ausschließlich die Beispielspalte in Markdown und Datenbank und erhält alle übrigen Bestandsfelder. Links auf Grundschaltungen und andere Referenztypen müssen als solche erkennbar sein; ungeklärten Typen keine erfundene Beschaltung zuordnen.
