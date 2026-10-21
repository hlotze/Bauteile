# Bestandsänderungen

`Bauteile.db` ist die führende Quelle für den Bauteilbestand. Bei Abweichungen `Bauteile.md` anhand der Datenbank aktualisieren und alle dargestellten Felder abgleichen. Die Datenbank beim Abgleich nur lesend öffnen und unverändert lassen.

`scripts/build_db.py` ersetzt die Datenbank aus Markdown und Quellen. Diesen Import nur auf ausdrückliche Anweisung ausführen, nicht automatisch nach Markdown-Änderungen.

Beispielschaltungen werden in `Quellen/Beispielschaltungen.json` gepflegt. `python3 scripts/update_examples.py` aktualisiert ausschließlich die Beispielspalte in Markdown und Datenbank und erhält alle übrigen Bestandsfelder. Links auf Grundschaltungen und andere Referenztypen müssen als solche erkennbar sein; ungeklärten Typen keine erfundene Beschaltung zuordnen.
