# Entwicklungs-Roadmap

Konkrete Implementierungsreihenfolge, abgeleitet aus `project-plan.md` Kap. 12 und den Ergebnissen der Phase-1-Recherche. Bezeichnungen wie D-002 verweisen auf `decisions.md`.

Prinzip: **vertikaler Schnitt zuerst.** Erst wenn eine kleine Fähigkeit messbar besser ist als dieselbe Aufgabe ohne Skill, wird erweitert.

## Phase 1 – Fundament (Stand)

| Aufgabe | Stand |
|---|---|
| Impeccable untersuchen, Lizenz klären | **erledigt** (`research/impeccable-analysis.md`) |
| Agent Skills Spec recherchieren | **erledigt**, mit Lücken (`research/agent-skills-compatibility.md`) |
| Architektur prüfen und anpassen | **Vorschlag** (`architecture.md`, `decisions.md`) |
| Implementierungsreihenfolge | dieses Dokument |
| Nielsen-Heuristiken, Cognitive-Load-Methoden aus Primärquellen einordnen | **erledigt** (`research/methodology-sources.md`) |
| Editorial UX von allgemeinem UI-Design abgrenzen | **erledigt** (`research/impeccable-analysis.md`, 3.4 und 6) |
| Bestehende CMS- und Admin-UX-Patterns untersuchen | **offen** |
| `docs/methodology.md` | **Entwurf** zur Freigabe (Dimensionen, Evidenz, Schweregrad, Deckelungsregel, Walkthrough) |

### Vor Abschluss von Phase 1 zu klären

1. **Entscheidungen freigeben:** D-002, D-003, D-004, D-005, D-007, D-008, D-009, D-015.
2. **Claude-Code-Dokumentation lesen:** erledigt für Skills (`research/cursor-compatibility.md`); Plugin-Seiten offen. **Cursor-Doku (Skills, Plugins) und Claude-Code-Plugin-Seiten:** erledigt, siehe `research/cursor-compatibility.md`.
3. **Repository umbenennen** (D-002): Aktion des Inhabers.
4. **Primärquellen-Recherche** für die Methodik: NN/g-Heuristiken, WCAG 2.2, Cognitive Walkthrough, Cognitive-Load-Literatur; Nachweis je Aussage.

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

- **Phase 4:** Adapter-Vorlage zusätzlich zu `custom-backends` und ProcessWire. Agentenspezifische Pakete erst planen, wenn die Quelle stabil ist.
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
