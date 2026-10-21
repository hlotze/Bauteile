#!/usr/bin/env python3
"""Erstellt Bauteile.db aus der Hauptliste und den Datenblattquellen."""
import json
from pathlib import Path
import re
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    'Bestand: Quarze': ('Quarz', 'Quarze'),
    'Bestand: Dioden': ('Diode', 'Dioden'),
    'IC-Bestand: SN74xx': ('IC SN7xxx', 'SN7xxx'),
    'IC-Bestand: CD4xxx': ('IC CD4xxx', 'CD4xxx'),
    'IC-Bestand: Diverse': ('IC diverse', 'Diverse'),
    'Bestand: Transistoren': ('Transitor', 'Transistor'),
    'Bestand: MOSFETs': ('MOSFET', 'MOSFET'),
    'Bestand: Triacs und Thyristoren': ('Triac_Thyristor', 'Triac_Thyristor'),
    'Bestand: Spannungsregler und Spannungsreferenzen': ('Spannungsregler', 'Spannungsregler'),
}
LINK = re.compile(r'\[([^]]+)\]\(([^)]+)\)')


def plain(value):
    return LINK.sub(r'\1', value).replace('`', '').strip()


def main():
    sources = {
        folder: {entry['part']: entry for entry in json.loads(
            (ROOT / 'Datenblaetter' / folder / 'quellen.json').read_text())}
        if (ROOT / 'Datenblaetter' / folder / 'quellen.json').is_file() else {}
        for _, folder in CATEGORIES.values()
    }
    rows = []
    category = None
    headers = None
    for line in (ROOT / 'Bauteile.md').read_text().splitlines():
        if line.startswith('## '):
            category = CATEGORIES.get(line[3:])
            headers = None
        if not category or not line.startswith('|'):
            continue
        cells = [cell.strip() for cell in re.split(r'(?<!\\)\|', line)[1:-1]]
        if headers is None:
            headers = cells
            continue
        if all(re.fullmatch(r':?-+:?', cell) for cell in cells):
            continue
        if len(cells) != len(headers):
            raise ValueError(f'Ungültige Tabellenzeile: {line}')
        values = dict(zip(headers, cells))
        name = plain(cells[0])
        source = sources[category[1]].get(name, {})
        notes = [plain(values.get('+5 V / Besonderheiten', values.get('Nachweis / Hinweise', '')))]
        notes.extend(str(source.get(key, '')) for key in ('assignment', 'variant', 'note'))
        notes = list(dict.fromkeys(note for note in notes if note))
        paths = [path for _, path in LINK.findall(values['Datenblatt'])]
        cards = {Path(path).suffix: path for _, path in LINK.findall(values.get('Karte', ''))}
        for path in paths + list(cards.values()):
            if not (ROOT / path).is_file():
                raise ValueError(f'Datei fehlt: {path}')
        rows.append((category[0], name, plain(values['Typ / Funktion']),
                     plain(values['Gehäuse']), plain(values['Anzahl']),
                     '\n'.join(notes), '\n'.join(paths) or None,
                     cards.get('.png'), cards.get('.pdf'), cards.get('.svg'),
                     source.get('manufacturer'), source.get('url'),
                     values.get('Beispielschaltungen', '')))
    if {row[0] for row in rows} != {category[0] for category in CATEGORIES.values()}:
        raise ValueError('Nicht alle Kategorien wurden eingelesen')
    with sqlite3.connect(ROOT / 'Bauteile.db') as db:
        db.execute('DROP TABLE IF EXISTS Bauteile')
        db.execute('''CREATE TABLE Bauteile (
            Type TEXT NOT NULL,
            Bezeichnung TEXT NOT NULL,
            Funktion TEXT NOT NULL,
            Gehaeuse TEXT,
            Anzahl TEXT,
            Hinweise TEXT,
            Datenblatt TEXT,
            Karte_PNG TEXT,
            Karte_PDF TEXT,
            Karte_SVG TEXT,
            Hersteller_Referenz TEXT,
            Quelle_URL TEXT,
            Beispielschaltungen TEXT NOT NULL DEFAULT '',
            PRIMARY KEY (Type, Bezeichnung)
        )''')
        db.executemany('INSERT INTO Bauteile VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', rows)
        assert db.execute('PRAGMA integrity_check').fetchone() == ('ok',)
        assert db.execute('SELECT COUNT(*) FROM Bauteile').fetchone()[0] == len(rows)
        for category, count in db.execute('SELECT Type, COUNT(*) FROM Bauteile GROUP BY Type'):
            print(f'{category}: {count}')
        print(f'Gesamt: {len(rows)} — {ROOT / "Bauteile.db"}')


if __name__ == '__main__':
    main()
