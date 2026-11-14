# editorial-ux-skill

> Design the work, not just the interface.

**editorial-ux-skill** ist ein offener Skill für KI-Coding-Agenten. Er hilft dabei, redaktionelle und administrative Oberflächen zu analysieren, zu gestalten und zu verbessern, sodass Menschen damit effizient, sicher und mit Kontrolle über ihre Arbeit arbeiten.

Ein Backend ist nicht nur eine technische Verwaltungsoberfläche. Es ist ein Arbeitsplatz.

## Status

**Alpha 0.1: testbar, noch nicht gemessen.** Phase 1 (Recherche und Konzeption) ist abgeschlossen. Der Skill enthält die Befehle `critique` und `design` (Konzeptstufe) sowie WordPress-Hinweise (Meta-Boxen, Block-Editor), die bisher aus Modellwissen stammen und als Annahme gekennzeichnet sind. Es gibt einen ersten informellen Rauchtest ([Ergebnis](evals/results/2026-11-14-smoke-critique.md)), aber noch keine Vergleichsmessung mit und ohne Skill. Details: [Roadmap](docs/development-roadmap.md).

### Ausprobieren

1. Ordner `skills/editorial-ux-skill` nach `.claude/skills/editorial-ux-skill/` in Ihrem Projekt kopieren (Claude Code und Cursor lesen diesen Ordner, laut offizieller Dokumentation). Der Ordnername muss genau so lauten.
2. Neue Sitzung starten und zum Beispiel fragen: „Prüfe diese Meta-Box aus Sicht der Redakteure“ oder „Plane die Felder für einen Event-Inhaltstyp“.
3. Zum Testen gibt es ein absichtlich schlechtes Beispiel und eine Anleitung für den Vergleich mit und ohne Skill: [evals/README.md](evals/README.md).
4. Struktur prüfen: `python3 tests/structural/check_skill.py`.

## Einsatzszenarien

1. **Eingebettete Redaktionsoberflächen in einem Host-CMS.** Hauptfall ist WordPress mit **Meta-Boxen und Block-Editor**: Der Skill hilft, vom Entwickler gebaute Felder und Blöcke für Redakteure zu gestalten. Er schreibt das Host-Backend nicht um und arbeitet nur über dessen offizielle Erweiterungspunkte.
2. **Vollständige Backends unabhängig von einem CMS:** individuell entwickelte Verwaltungsoberflächen, interne Werkzeuge, Dashboards.

In beiden Fällen ist alles visuell gestaltbar: Entwurf und Umsetzung (Markup, Styles, Komponenten).

## Idee in drei Sätzen

1. **Understand the System:** Erst das vorhandene System verstehen, dann gestalten.
2. **Design for the User:** Die tatsächliche Arbeitsrealität der Benutzer bestimmt die Gestaltung.
3. **Good Work is the Measure:** Effizienz, Verständlichkeit, Barrierefreiheit und Kontrolle über die eigene Arbeit sind gleichwertig. Gerne arbeiten zeigt sich an Kontrolle, Ruhe und Souveränität.

## Befehle

Befehle folgen dem Muster `/editorial-ux-skill <befehl>`. Sie sollen auch einzeln nutzbar sein und werden aus dem Text der Anfrage abgeleitet (keine Platzhalter, damit derselbe Skill in mehreren Agenten läuft).

| Befehl | Zweck | Stand |
|---|---|---|
| `critique` | Bestehende UX nach den Dimensionen A bis I bewerten | **Alpha 0.1, verfügbar** |
| `design` | Lösung konzipieren (Struktur, Felder, Beschriftung, Zustände, Wireframe); ohne Code | **Alpha 0.1, verfügbar (Konzeptstufe)** |
| `discover` | System und redaktionelle Arbeitsrealität untersuchen | Alpha 0.2 |
| `audit` | Prüfbare Qualitätskriterien abarbeiten (z. B. Barrierefreiheit) | Alpha 0.2 |
| `improve` | Kleinen Verbesserungszyklus durchführen | Alpha 0.3 |
| `walkthrough` | Aufgaben als simulierten Durchgang prüfen | Beta |
| `implement` | Freigegebene Gestaltung umsetzen | Beta |
| `document` | Ergebnisse und Entscheidungen dokumentieren | Beta |

## Methodik in Kürze

Grundlage sind **Primärquellen**: Nielsens zehn Heuristiken, Nielsens Schweregrade, Cognitive Walkthrough, Cognitive-Load-Forschung der Nielsen Norman Group, Gestaltprinzipien und WCAG 2.2 (Zielstufe AA). Die Details stehen in der [Methodik](docs/methodology.md).

- **Neun Dimensionen A bis I:** Orientierung, Aufgabenverständlichkeit, Informationsarchitektur, Interaktionsqualität, kognitive Belastung, Fehlertoleranz, Arbeitsfluss, visuelle Qualität, Accessibility.
- **Evidenzstufen:** Jeder Befund ist *beobachtet*, eine *Hypothese* oder eine *Annahme*. Scores stützen sich nur auf Beobachtetes.
- **Schweregrad 0 bis 4** nach Häufigkeit, Auswirkung und Persistenz, vergeben nach der Befundphase.
- **Kein verdeckender Gesamtwert:** Eine schwere Schwäche (etwa bei Barrierefreiheit) bleibt als Blocker sichtbar.
- **Ehrlichkeit statt Schätzung:** Fehlende Werkzeuge oder Quellen führen zu „nicht bewertbar“ und einem Hinweis, nicht zu erfundenen Ergebnissen.
- **Inspektion, kein Nutzertest:** Ergebnisse sind Hypothesen. Wo es zählt, empfiehlt der Bericht Tests mit echten Nutzern.

Dies ist ein **Entwurf**; Skalen und Regeln werden in Phase 2 gemessen und kalibriert.

## Zielumgebungen

- **Claude Code** und **Cursor** (beide lesen laut offizieller Dokumentation `.claude/skills/`). Geplante Installation in Alpha: Ordner `editorial-ux-skill` nach `.claude/skills/editorial-ux-skill/` kopieren oder verlinken, ohne Buildprozess.
- Weitere Agenten (Codex, Gemini CLI, Antigravity) sind nicht geprüft.
- Plugin und Marketplace sind frühestens ab der Beta geplant.
- Der Skill folgt dem offenen [Agent Skills](https://github.com/agentskills/agentskills)-Format und braucht keine Cloud-Dienste, API-Schlüssel oder Laufzeit.

## Dokumentation

| Dokument | Inhalt |
|---|---|
| [Projektplan](docs/project-plan.md) | Vision, Geltungsbereich, Architektur, Methodik, Phasen, Definition of Done |
| [Architektur](docs/architecture.md) | Layout, Lademodell, Qualitätssicherung, Modularisierungsprüfung |
| [Methodik](docs/methodology.md) | Dimensionen, Evidenzstufen, Schweregrad, Scoring, Walkthrough (Entwurf) |
| [Entscheidungen](docs/decisions.md) | D-001 bis D-028 mit Begründung und Status |
| [Roadmap](docs/development-roadmap.md) | Umsetzungsreihenfolge, offene Punkte, Risiken |
| [Evals und Testanleitung](evals/README.md) | Testbeispiel mit versteckter Lösungsliste, Vergleich mit/ohne Skill, [Rauchtest](evals/results/2026-11-14-smoke-critique.md) |
| [Recherche: Impeccable](docs/research/impeccable-analysis.md) | Architektur und Lizenz des Referenzprojekts |
| [Recherche: Agent Skills](docs/research/agent-skills-compatibility.md) | Spezifikation und Folgen |
| [Recherche: Cursor und Claude Code](docs/research/cursor-compatibility.md) | Installation, Frontmatter, Plugins |
| [Recherche: Methodikquellen](docs/research/methodology-sources.md) | Was die Primärquellen belegen und was nicht |

## Entwicklungsphasen

1. Grundlagen und Recherche: **abgeschlossen**
2. Vertikaler Schnitt (`critique`, `design`, Testbeispiel, Vergleich mit/ohne Skill): **läuft**, Alpha 0.1 testbar, Messung steht aus
3. Engine (`discover`, `audit`, Mehrfachläufe)
4. Plattformintelligenz (generischer und WordPress-Adapter)
5. Implementierung und Design
6. Evaluation und Härtung
7. Open-Source-Release (1.0)

## Herkunft und Lizenz

Vorgesehen ist die **MIT-Lizenz**; sie wird vor der Veröffentlichung geprüft und finalisiert.

[Impeccable](https://github.com/pbakaus/impeccable) (Apache-2.0) diente nur als **Referenz für Architekturideen**. Es wurden weder Text noch Code noch der Name übernommen. Inhalte aus Nielsen Norman Group und W3C sind in eigenen Worten wiedergegeben und mit Quelle belegt (siehe [Zitierweise](docs/decisions.md)).
