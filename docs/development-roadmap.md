# Entwicklungs-Roadmap

Konkrete Implementierungsreihenfolge, abgeleitet aus `project-plan.md` Kap. 12 und den Ergebnissen der Phase-1-Recherche. Bezeichnungen wie D-002 verweisen auf `decisions.md`.

Prinzip: **vertikaler Schnitt zuerst.** Erst wenn eine kleine Fähigkeit messbar besser ist als dieselbe Aufgabe ohne Skill, wird erweitert.

## Phase 1 – Fundament (abgeschlossen am 2026-11-14)

| Aufgabe | Stand |
|---|---|
| Impeccable untersuchen, Lizenz klären | **erledigt** (`research/impeccable-analysis.md`; Apache-2.0, nichts übernommen) |
| Agent Skills Spec recherchieren | **erledigt** (`research/agent-skills-compatibility.md`) |
| Cursor- und Claude-Code-Skills und Plugins | **erledigt**, Primärquellen (`research/cursor-compatibility.md`) |
| Architektur prüfen und anpassen | **erledigt** (`architecture.md`, `decisions.md`) |
| Implementierungsreihenfolge | dieses Dokument |
| Nielsen-Heuristiken, Cognitive Load, WCAG, Walkthrough, Gestaltprinzipien aus Primärquellen | **erledigt** (`research/methodology-sources.md`) |
| Editorial UX von allgemeinem UI-Design abgrenzen | **erledigt** (`research/impeccable-analysis.md`, 3.4 und 6) |
| Bewertungsmethodik entwerfen | **erledigt als Entwurf** (`methodology.md`); Kalibrierung in Phase 2 |
| Einsatzszenarien und Adapter-Zuschnitt festlegen | **erledigt** (D-024, D-025) |
| Bestehende CMS- und Admin-UX-Patterns untersuchen, WordPress-Adapter | **bewusst zurückgestellt** (D-026) |

### Ergebnisse (Dokumente)

`docs/project-plan.md` (Version 3), `docs/architecture.md`, `docs/methodology.md`, `docs/decisions.md` (D-001 bis D-026), `docs/development-roadmap.md`, `docs/research/` mit `impeccable-analysis.md`, `agent-skills-compatibility.md`, `cursor-compatibility.md`, `methodology-sources.md`.

### Mit Phase 1 mitgenommene offene Punkte

| Punkt | Wo geklärt | Verantwortlich |
|---|---|---|
| Repository in Kleinschreibung umbenennen (D-002), nicht blockierend | jederzeit | Projektverantwortlicher |
| Skalenbreite 0–5 oder 0–4 (D-011), Deckelungsregel | Phase 2, Kalibrierlauf | Claude, mit Messung |
| Profil-Persistenz (D-012), isolierte Mehrfachläufe (D-013) | Phase 3 | Claude, mit Messung |
| Praxistest in Cursor (Fund unter `.claude/skills/`, Text hinter `/editorial-ux-skill`, `license`-Feld) | Ende Phase 2 | Projektverantwortlicher oder Claude |
| WordPress-Adapter (Meta-Boxen, Block-Editor): Quellenprüfung, falls Modellwissen nicht genügt (D-026) | nach dem Praxistest | beide |
| CMS- und Admin-UX-Patterns, ARIA-Muster, WCAG-Prüfbarkeitstabelle, EN 301 549 | Phase 2 und 4 | Claude |
| Claude-Code-Plugin-Review-Kriterien, gemeinsames Plugin-Manifest | Beta | Claude |
| Wirkungsvergleiche zu Impeccable (mit/ohne Skill) | optional | Claude |

### Hinweis zum geplanten WordPress-Test

Ein Test mit einem hypothetischen WordPress-Backend setzt voraus, dass es **einen lauffähigen Skill gibt**. Der erste Stand entsteht in Phase 2 (Schritt 4 und 5: `SKILL.md` und `critique`). Bis dahin existiert nur die Dokumentation. Der Test sollte mit dem Baseline-Vergleich aus Phase 2 verzahnt werden: dieselbe Aufgabe mit und ohne Skill, protokolliert nach dem Format aus `project-plan.md` Kap. 10.

## Phase 2 – Vertikaler Schnitt (Alpha 0.1)

Reihenfolge (jeder Schritt ist einzeln prüfbar):

| # | Schritt | Prüfung |
|---|---|---|
| 1 | Layout anlegen (`skills/editorial-ux-skill/…`, `evals/`, `tests/`) | Struktur entspricht `architecture.md` |
| 2 | Strukturtest: `skills-ref validate`, Namensregel, Verweise, Budgets (zuerst mit Platzhalterdateien) | Test läuft grün/rot, wie erwartet |
| 3 | `references/methodology.md`: Dimensionen A–I, Skalenanker, Evidenzstufen, Schweregrade | Anker für jede Stufe vorhanden |
| 4 | Testprojekt D als Fixture mit **versteckter Lösungsliste** (eingebaute Probleme je Dimension) | Liste von einer zweiten Person gegengelesen |
| 5 | **Baseline ohne Skill** auf Testprojekt D (mehrere Läufe) | `grading.json`, `timing.json` liegen vor |
| 6 | `SKILL.md` (nur Prinzipien, Befehlstabelle, Ladetabelle, Gotchas) | < 500 Zeilen, < 5000 Token |
| 7 | `references/cmd-critique.md` und Vorlage `ux-critique.md` | Bericht enthält Evidenzstufen, Blocker-Markierung |
| 8 | Aktivierungs-Eval (`description`, ca. 20 Anfragen) | Ziel: keine Falsch-Positive bei Beinahe-Treffern |
| 9 | Lauf **mit Skill** auf Testprojekt D, Vergleich mit Baseline | Trefferquote, Falschbefunde, Streuung, Kontext/Zeit |
| 10 | Kalibrierlauf der Skala (D-011): 0–5 gegen 0–4 | Streuung gemessen, Entscheidung dokumentiert |

**Entscheidungspunkt (Plan Kap. 12):** Bringt der Skill messbar bessere Kritik? Falls nein, wird die Methodik überarbeitet, bevor weitere Befehle entstehen.

Nicht in Phase 2: `discover`, `audit`, Adapter, Pattern-Bibliothek, Skripte.

## Phase 3 – Engine (Alpha 0.2)

1. `discover` und `audit`, jeweils mit eigener Befehlsanleitung und Vorlage.
2. Entscheidung zu D-012 (Profil-Persistenz) und D-013 (Isolation) anhand von Messungen.
3. Aufgabenbasierte Analyse (Grundlage für `walkthrough`), Cognitive-Load-Bewertung und beobachtbare Arbeitsqualität (Kontrolle, Ruhe, Souveränität, Reibung) kalibrieren.
4. Reproduzierbarkeit messen (mehrere Läufe, Streuung der Dimensionsscores und der Top-3-Priorisierung).

## Phase 4–7

Unverändert nach Projektplan. Änderungen aus der Recherche:

- **Phase 4:** Adapter-Vorlage zusätzlich zu `custom-backends` und `wordpress` (Meta-Boxen, Block-Editor); ProcessWire nachrangig (D-025). Agentenspezifische Pakete erst planen, wenn die Quelle stabil ist.
- **Phase 2/6:** Cursor ist Zielumgebung (D-016). Ein kurzer Praxistest in Cursor (Skill unter `.claude/skills/` gefunden? Text hinter `/editorial-ux-skill` angekommen?) gehört schon an das Ende von Phase 2, der volle Verhaltenstest in Phase 6. Agentenvergleich nur mit Agenten, deren Skill-Installation tatsächlich geprüft wurde (bisher ungeprüft: Codex, Gemini CLI, Antigravity).
- **Phase 7:** Lizenzprüfung erneut, inklusive Abgleich aller Referenzdateien auf ihre Primärquellen (D-006).

## Risiken

| Risiko | Gegenmaßnahme |
|---|---|
| Wirkung des Skills lässt sich nicht nachweisen | Entscheidungspunkt am Ende von Phase 2; keine Erweiterung ohne Nachweis |
| LLM-Scores streuen stark | Verankerte Skalen, Kalibrierfälle, Messung in Phase 2 und 3 |
| Aktivierung unzuverlässig | Aktivierungs-Eval, `description` iterativ verbessern |
| Spec oder Agenten ändern sich | Spec-Stand mit Commit dokumentiert; Prüfung vor Release wiederholen |
| Versehentliche Übernahme fremder Inhalte | Primärquellenangabe je Referenz (D-006) |
| Skill wird zu groß | Budgets im Test, evidenzbasiertes Wachstum |
