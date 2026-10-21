#!/usr/bin/env python3
"""Überträgt kuratierte Schaltungslinks in Markdown und die bestehende DB.

Alle bisherigen Datenbankspalten bleiben unverändert. Der vollständige
Bestandsimport build_db.py wird hierbei ausdrücklich nicht ausgeführt.
"""
import json
from pathlib import Path
import re
import sqlite3

from build_db import CATEGORIES, plain

ROOT = Path(__file__).resolve().parents[1]


def main():
    catalog = json.loads((ROOT / 'Quellen/Beispielschaltungen.json').read_text())
    sources = catalog['sources']
    examples = {}
    for part in catalog['parts']:
        key = (part['type'], part['part'])
        if key in examples:
            raise ValueError(f'Doppelter Eintrag: {key}')
        if len(part['links']) > 5 or (not part['links'] and not part.get('note')):
            raise ValueError(f'Fehlende Beispiele ohne Begründung: {key}')
        links = []
        for link in part['links']:
            url = sources[link['source']]['url']
            label = link['label']
            if not url.startswith('https://'):
                target, _, fragment = url.partition('#')
                if not (ROOT / target).is_file():
                    raise ValueError(f'Datei fehlt: {target}')
                if fragment.startswith('page='):
                    label += f" (PDF S. {fragment[5:]})"
            if '|' in label or '\n' in label or ')' in url:
                raise ValueError(f'Nicht unterstütztes Linkformat: {link}')
            links.append(f'[{label}]({url})')
        examples[key] = '<br>'.join(links) or 'Noch offen: Funktion ungeklärt'

    path = ROOT / 'Bauteile.md'
    lines = path.read_text().splitlines()
    category = None
    headers = None
    found = set()
    for i, line in enumerate(lines):
        if line.startswith('## '):
            category = CATEGORIES.get(line[3:])
            headers = None
        if not category or not line.startswith('|'):
            continue
        cells = [v.strip() for v in re.split(r'(?<!\\)\|', line)[1:-1]]
        if headers is None:
            headers = cells.copy()
            if 'Beispielschaltungen' not in headers:
                cells.append('Beispielschaltungen')
        elif all(re.fullmatch(r':?-+:?', v) for v in cells):
            if 'Beispielschaltungen' not in headers:
                cells.append('---')
        else:
            key = (category[0], plain(cells[0]))
            if key not in examples:
                raise ValueError(f'Keine Zuordnung für {key}')
            if key in found:
                raise ValueError(f'Doppelter Markdown-Eintrag: {key}')
            found.add(key)
            if 'Beispielschaltungen' in headers:
                cells[headers.index('Beispielschaltungen')] = examples[key]
            else:
                cells.append(examples[key])
        lines[i] = '| ' + ' | '.join(cells) + ' |'
    if found != set(examples):
        raise ValueError(f'Nicht in Markdown: {set(examples) - found}')

    with sqlite3.connect(ROOT / 'Bauteile.db') as db:
        columns = [r[1] for r in db.execute('PRAGMA table_info(Bauteile)')]
        old_columns = [name for name in columns if name != 'Beispielschaltungen']
        projection = ', '.join(old_columns)
        before = db.execute(f'SELECT {projection} FROM Bauteile ORDER BY Type, Bezeichnung').fetchall()
        keys = set(db.execute('SELECT Type, Bezeichnung FROM Bauteile'))
        if keys != set(examples):
            raise ValueError('Datenbankbestand und Schaltungszuordnungen unterscheiden sich')
        if 'Beispielschaltungen' not in columns:
            db.execute("ALTER TABLE Bauteile ADD COLUMN Beispielschaltungen TEXT NOT NULL DEFAULT ''")
        for (kind, part), value in examples.items():
            db.execute('UPDATE Bauteile SET Beispielschaltungen=? WHERE Type=? AND Bezeichnung=?',
                       (value, kind, part))
        after = db.execute(f'SELECT {projection} FROM Bauteile ORDER BY Type, Bezeichnung').fetchall()
        if before != after or db.execute('PRAGMA integrity_check').fetchone() != ('ok',):
            raise RuntimeError('Bestands- oder Integritätsprüfung fehlgeschlagen')
        path.write_text('\n'.join(lines) + '\n')
    print(f'{len(examples)} Einträge aktualisiert; bisherige Bestandsdaten unverändert.')


if __name__ == '__main__':
    main()
