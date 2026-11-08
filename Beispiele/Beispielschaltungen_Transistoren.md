# Schaltungsbeispiele: Transistoren

[Übersicht](README.md) · [Gesamtsammlung](Beispielschaltungen.md) · [Recherchebedarf](Recherchebedarf.md) · [Bestand](../Bauteile.md)

60 Bauteile, 360 Linkzuordnungen. Erweiterungsstand: **25.10.2026**; Prüfdatum jeweils am Link.

Ziel sind etwa **fünf unterschiedliche Websites pro Bauteil**. Gezählt werden Websites mit Schaltungsbeispielen, übertragbaren Grundschaltungen, Modulbeispielen oder Code mit Anschlusszuordnung. Reine Funktions-/Prinzipreferenzen und Entwurfshilfen zählen zusätzlich als Quellen, aber nicht zum Beispielziel. Subdomains und bekannte Länderspiegel zählen zusammen. Mehrere Artikel derselben Website erhöhen die Zahl nicht.

**Grundschaltung** bedeutet: Das Schaltungsprinzip ist übertragbar, der Artikel verwendet gegebenenfalls ein anderes Bauteil. Sie ist keine Bestätigung der Pinbelegung oder Dimensionierung des vorhandenen Typs. **Modulbeispiele** enthalten zusätzliche Komponenten; **Funktionsreferenzen** sind keine vollständigen Nachbauschaltungen. Hinweise stehen direkt beim Bauteil und Link.

Versorgung, Pinfolge, Polarität, Logikfamilie, Freigaben, Taktflanken und Grenzwerte anhand des konkreten Datenblatts prüfen. 74LS benötigt +5 V. Pro IC üblicherweise 100 nF abblocken, Taster für Zähler entprellen. Transistor- und Diodenwerte an Last und Verlustleistung anpassen. Bei Relais gilt die tatsächliche Spulenspannung. TRIAC-Artikel können Netzspannungsschaltungen enthalten.

Pflege: [Beispielschaltungen.json](Beispielschaltungen.json). `python3 scripts/update_examples.py` erzeugt ausschließlich diese Sammlungen. Bestand und Datenbank bleiben unverändert. Bei lokalen PDFs führt „Online-Original“ zur dokumentierten Downloadquelle; neuere Revisionen können andere Seitenzahlen haben.

## 2N2222

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## 2N3904

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## 2N3906

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## 2N5401

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## 2N5551

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## 2SA1015

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## 2SB772

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## 2SC1815

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## 2SC945

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## 2SD882

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC327

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC337

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC517

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Darlington-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC546

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC547

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC548

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC549

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC550

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC556

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC557

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC558

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BD139

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BD140

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## MPQ2222A

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Stromspiegel (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/current-mirror/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## S8050

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## S8550

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## S9012

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## S9013

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## S9014

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## S9015

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## S9018

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## TIP120

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Darlington-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## TIP121

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Darlington-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## TIP122

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Darlington-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## TIP125

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## TIP126

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## TIP127

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## TIP31C

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## TIP32C

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## TIP41C

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## TIP42C

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC556B

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC557B

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC558B

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## MPS2907A

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC547C

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC546B

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC548B

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BDX54C

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC141

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC161

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC559

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC560

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC639

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC640

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [PNP-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC879

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [Darlington-Schalter (Grundschaltung)](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Dämmerungsschalter mit BC557](https://www.build-electronic-circuits.com/pnp-transistor) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [PNP-Stromspiegel und komplementäre Ausgangsstufen](https://www.allaboutcircuits.com/technical-articles/pnp-transistor-characteristics-applications/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-25.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BC238B

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## KSP44

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## BD135-10

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.

## 2N2222A

**5/5 Beispiel-Websites**, 5 Quellen-Websites insgesamt. Ziel erreicht.

- [NPN-Schalter (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/transistor-as-a-switch/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Emitterschaltung (Grundschaltung)](https://www.allaboutcircuits.com/textbook/experiments/chpt-5/common-emitter-amplifier1/) — allaboutcircuits.com; Grundschaltung; geprüft 2026-10-21.
- [Transistorschalter, Relaistreiber und Verstärker](https://electronicsclub.info/transistorcircuits.htm) — electronicsclub.info; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP-Schalter und Verstärkerstufen](https://learn.sparkfun.com/tutorials/transistors/all) — sparkfun.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und MOSFET-Schalter](https://www.build-electronic-circuits.com/transistor-as-a-switch/) — build-electronic-circuits.com; Grundschaltung; geprüft 2026-10-25.
- [NPN-/PNP- und Darlington-Lastschalter](https://www.electronics-tutorials.ws/transistor/tran_4.html) — electronics-tutorials.ws; Grundschaltung; geprüft 2026-10-21.

Pinbelegung, Polarität, Strom und Widerstände für den vorhandenen Transistortyp auslegen; Grundschaltungen sind keine unveränderten Ersatztypenempfehlungen. NPN-Grundschaltungen: Basiswiderstand, Pinfolge, zulässigen Kollektorstrom und Verlustleistung für diesen Typ dimensionieren. Bei Darlington-Typen zusätzliche Basis-Emitter-Spannung und höhere Sättigungsspannung berücksichtigen; bei PNP die PNP-Schaltung der Quelle verwenden, keine unveränderte NPN-Beschaltung.
