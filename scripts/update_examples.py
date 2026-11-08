#!/usr/bin/env python3
"""Erzeugt separate Linksammlungen; verändert weder Bestand noch Datenbank."""
import json
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'Beispiele'
GROUPS = [
    ('IC SN7xxx', 'SN74xx'), ('IC CD4xxx', 'CD4xxx'), ('IC diverse', 'Diverse'),
    ('Transitor', 'Transistoren'), ('MOSFET', 'MOSFETs'),
    ('Triac_Thyristor', 'Triacs_Thyristoren'), ('Spannungsregler', 'Spannungsregler'),
    ('Diode', 'Dioden'), ('Quarz', 'Quarze'), ('Optokoppler', 'Optokoppler'),
    ('Mikroprozessorbasteleien', 'Mikroprozessorbasteleien'),
]
# Referenzen nicht als zusätzliche Schaltungsbeispiele zählen.
REFERENCE_KINDS = ('referenz', 'entwurfshilfe', 'funktions', 'prinzip')


def website(source):
    """Subdomains und Länderspiegel eines Anbieters zählen zusammen."""
    host = urlsplit(source.get('online_url') or source['url']).hostname
    if not host:
        return None
    host = host.removeprefix('www.')
    aliases = {
        'ti.com.cn': 'ti.com', 'tij.co.jp': 'ti.com', 'st.com.cn': 'st.com',
        'onsemi.jp': 'onsemi.com', 'nxp.jp': 'nxp.com',
        'toshiba-semicon-storage.com': 'toshiba.semicon-storage.com',
        'digikey.in': 'digikey.com', 'digikey.jp': 'digikey.com',
    }
    for ending in ('adafruit.com', 'sparkfun.com', 'analog.com', 'ti.com',
                   'renesas.com', 'microchip.com', 'onsemi.com', 'st.com',
                   'github.com', 'learnabout-electronics.org'):
        if host == ending or host.endswith('.' + ending):
            return ending
    return aliases.get(host, host)


def counts(part, sources):
    all_sites, example_sites = set(), set()
    for link in part['links']:
        source = sources[link['source']]
        site = website(source)
        kind = link.get('kind', source['kind']).lower()
        if site:
            all_sites.add(site)
            if not any(term in kind for term in REFERENCE_KINDS):
                example_sites.add(site)
    return len(example_sites), len(all_sites)


def navigation():
    return ('[Übersicht](README.md) · [Gesamtsammlung](Beispielschaltungen.md) · '
            '[Recherchebedarf](Recherchebedarf.md) · [Bestand](../Bauteile.md)')


def render(parts, sources, title):
    lines = [f'# {title}', '', navigation(), '',
             f'{len(parts)} Bauteile, {sum(len(p["links"]) for p in parts)} Linkzuordnungen. '
             'Erweiterungsstand: **25.10.2026**; Prüfdatum jeweils am Link.', '',
             'Ziel sind etwa **fünf unterschiedliche Websites pro Bauteil**. Gezählt werden '
             'Websites mit Schaltungsbeispielen, übertragbaren Grundschaltungen, Modulbeispielen '
             'oder Code mit Anschlusszuordnung. Reine Funktions-/Prinzipreferenzen und '
             'Entwurfshilfen zählen zusätzlich als Quellen, aber nicht zum Beispielziel. '
             'Subdomains und bekannte Länderspiegel zählen zusammen. Mehrere Artikel derselben '
             'Website erhöhen die Zahl nicht.', '',
             '**Grundschaltung** bedeutet: Das Schaltungsprinzip ist übertragbar, der Artikel '
             'verwendet gegebenenfalls ein anderes Bauteil. Sie ist keine Bestätigung der '
             'Pinbelegung oder Dimensionierung des vorhandenen Typs. **Modulbeispiele** '
             'enthalten zusätzliche Komponenten; **Funktionsreferenzen** sind keine '
             'vollständigen Nachbauschaltungen. Hinweise stehen direkt beim Bauteil und Link.', '',
             'Versorgung, Pinfolge, Polarität, Logikfamilie, Freigaben, Taktflanken und '
             'Grenzwerte anhand des konkreten Datenblatts prüfen. 74LS benötigt +5 V. '
             'Pro IC üblicherweise 100 nF abblocken, Taster für Zähler entprellen. '
             'Transistor- und Diodenwerte an Last und Verlustleistung anpassen. '
             'Bei Relais gilt die tatsächliche Spulenspannung. TRIAC-Artikel können '
             'Netzspannungsschaltungen enthalten.', '',
             'Pflege: [Beispielschaltungen.json](Beispielschaltungen.json). '
             '`python3 scripts/update_examples.py` erzeugt ausschließlich diese Sammlungen. '
             'Bestand und Datenbank bleiben unverändert. Bei lokalen PDFs führt '
             '„Online-Original“ zur dokumentierten Downloadquelle; neuere Revisionen '
             'können andere Seitenzahlen haben.', '']
    for part in parts:
        example_count, total_count = counts(part, sources)
        lines += [f'## {part["part"]}', '',
                  f'**{example_count}/5 Beispiel-Websites**, {total_count} Quellen-Websites insgesamt. '
                  + ('Ziel erreicht.' if example_count >= 5 else 'Weitere passende Beispiele gesucht.'), '']
        for link in part['links']:
            source = sources[link['source']]
            url, label = source['url'], link['label']
            if not url.startswith('https://'):
                target, _, fragment = url.partition('#')
                if not (ROOT / target).is_file():
                    raise ValueError(f'Datei fehlt: {target}')
                url = '../' + url
                if fragment.startswith('page='):
                    label += f' (PDF S. {fragment[5:]})'
            host = website(source) or 'lokales Dokument'
            online = (f' · [Online-Original]({source["online_url"]})'
                      if source.get('online_url') else '')
            lines += [f'- [{label}]({url}){online} — {host}; '
                      f'{link.get("kind", source["kind"])}; '
                      f'geprüft {source.get("checked_on", "offen")}.']
            adaptation = link.get('adaptation', source.get('adaptation'))
            if adaptation:
                lines += [f'  Hinweis: {adaptation}']
        if not part['links']:
            lines += ['Noch kein belastbares Schaltungsbeispiel zugeordnet.']
        if part.get('note'):
            lines += ['', part['note']]
        if example_count < 5:
            lines += ['', '**Recherchebedarf:** ' + part.get('research_note',
                'Bisher sind weniger als fünf unterschiedliche Websites mit passenden Beispielen '
                'belegt. Die vorhandenen Grundschaltungen und Referenzen sind oben gekennzeichnet; '
                'es wurden keine zusätzlichen Beschaltungen erfunden.')]
        lines += ['']
    return '\n'.join(lines)


def main():
    catalog = json.loads((OUTPUT / 'Beispielschaltungen.json').read_text())
    parts, sources = catalog['parts'], catalog['sources']
    keys = [(p['type'], p['part']) for p in parts]
    if len(keys) != len(set(keys)):
        raise ValueError('Doppelte Bauteilzuordnung')
    if set(p['type'] for p in parts) != set(t for t, _ in GROUPS):
        raise ValueError('Unbekannte oder fehlende Bauteilgruppe')
    for part in parts:
        if not part['links'] and not part.get('note'):
            raise ValueError(f'Fehlende Begründung: {part["part"]}')
        ids = [link['source'] for link in part['links']]
        if len(ids) != len(set(ids)):
            raise ValueError(f'Doppelter Link: {part["part"]}')
        for link in part['links']:
            if link['source'] not in sources:
                raise ValueError(f'Unbekannte Quelle: {link["source"]}')
    index = ['# Schaltungsbeispiele', '', navigation(), '',
             f'Separate Sammlungen für alle **{len(parts)} Bestandseinträge**. Stand: **25.10.2026**.', '',
             'Ziel: etwa fünf verschiedene Websites mit Beispielen pro Bauteil. '
             'Grundschaltungen mit anderen Typen sind ausdrücklich gekennzeichnet; '
             'Funktionsreferenzen zählen nicht als Schaltungsbeispiel. '
             'Offene Fälle stehen im [Recherchebedarf](Recherchebedarf.md).', '',
             '| Gruppe | Bauteile | Mit mindestens fünf Beispiel-Websites |',
             '| --- | ---: | ---: |']
    for kind, name in GROUPS:
        selection = [p for p in parts if p['type'] == kind]
        filename = f'Beispielschaltungen_{name}.md'
        (OUTPUT / filename).write_text(render(selection, sources, f'Schaltungsbeispiele: {name}'))
        reached = sum(counts(p, sources)[0] >= 5 for p in selection)
        index += [f'| [{name}]({filename}) | {len(selection)} | {reached} |']
    reached = sum(counts(p, sources)[0] >= 5 for p in parts)
    index += ['', f'**{reached} von {len(parts)} Bauteilen** erreichen das Ziel. '
              f'Insgesamt {sum(len(p["links"]) for p in parts)} Linkzuordnungen; '
              'ein Artikel kann mehreren passenden Bauteilen zugeordnet sein.', '',
              '[Alle Bauteile in einer Datei](Beispielschaltungen.md) · '
              '[Maschinenlesbare Zuordnungen](Beispielschaltungen.json)', '',
              'Die Prüfungen betreffen die veröffentlichten Quellen und ihre fachliche '
              'Zuordnung. Die Schaltungen wurden hier nicht aufgebaut. Bestehende Quellen '
              'behalten ihr individuelles Prüfdatum. Links und Texte fremder Autoren '
              'werden referenziert; Schaltbilder werden nicht kopiert.', '']
    (OUTPUT / 'README.md').write_text('\n'.join(index))
    (OUTPUT / 'Beispielschaltungen.md').write_text(render(parts, sources, 'Beispielschaltungen pro Bauteil'))
    gaps = ['# Recherchebedarf', '', navigation(), '',
            'Diese Einträge erreichen noch keine fünf unterschiedlichen Websites mit '
            'Schaltungsbeispielen. Reine Referenzen sind in der zweiten Zahl enthalten. '
            'Eine Lücke wird nicht mit einem unpassenden Ersatztypen aufgefüllt.', '',
            '| Gruppe | Bauteil | Beispiel-Websites | Alle Quellen-Websites |',
            '| --- | --- | ---: | ---: |']
    for kind, name in GROUPS:
        for part in parts:
            examples, total = counts(part, sources)
            if part['type'] == kind and examples < 5:
                gaps += [f'| [{name}](Beispielschaltungen_{name}.md) | {part["part"]} | {examples}/5 | {total} |']
    (OUTPUT / 'Recherchebedarf.md').write_text('\n'.join(gaps) + '\n')
    print(f'{len(parts)} Bauteile; {reached} mit mindestens fünf Beispiel-Websites; '
          f'{len(parts)-reached} mit weiterem Recherchebedarf.')


if __name__ == '__main__':
    main()
