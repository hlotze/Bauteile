# Bestandsänderungen

`Bauteile.db` ist die führende Quelle für den Bauteilbestand. Bei Abweichungen `Bauteile.md` anhand der Datenbank aktualisieren und alle dargestellten Felder abgleichen. Die Datenbank beim Abgleich nur lesend öffnen und unverändert lassen.

`scripts/build_db.py` ersetzt die Datenbank aus Markdown und Quellen. Diesen Import nur auf ausdrückliche Anweisung ausführen, nicht automatisch nach Markdown-Änderungen.
