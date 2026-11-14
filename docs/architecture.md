# Architektur (Vorschlag nach Phase-1-Recherche)

Status: **Vorschlag zur Freigabe.** Er ergänzt `project-plan.md` Kap. 3–5 und 9. Grundlage sind `research/impeccable-analysis.md` und `research/agent-skills-compatibility.md`. Einzelne Entscheidungen stehen mit Begründung in `decisions.md`.

## 1. Leitlinie

Eine Architektur ist nur dann gut, wenn jedes Element etwas leistet, das sich messen oder begründen lässt. Daraus folgt:

1. **Ein Skill, ein Einstiegspunkt, Befehle als Argumente.**
2. **`SKILL.md` ist klein und routet.** Fachwissen liegt in Referenzen, die bei Bedarf geladen werden.
3. **Nutzlast und Projekt sind getrennt.** Nur das, was ein Agent braucht, liegt im Skill-Ordner.
4. **Jede Datei hat ein Größenbudget**, das ein Test erzwingt.
5. **Nur Spec-Felder** im Frontmatter der Quelle.

## 2. Repository-Layout

```
editorial-ux-skill/                     # Repository (Kleinschreibung, siehe D-002)
├── README.md
├── LICENSE
├── CONTRIBUTING.md  CODE_OF_CONDUCT.md  CHANGELOG.md   # ab Beta
│
├── skills/
│   └── editorial-ux-skill/             # = Skill-Nutzlast; Ordnername = name (Spec)
│       ├── SKILL.md                    # Prinzipien, Befehlstabelle, Ladetabelle, Gotchas
│       ├── references/                 # Fachwissen und Befehlsanleitungen (flach)
│       │   ├── cmd-critique.md         # Befehlsanleitung
│       │   ├── methodology.md          # Dimensionen A–J, Skalenanker, Evidenzstufen
│       │   ├── principles.md
│       │   ├── anti-patterns.md
│       │   └── …                       # wächst nach Bedarf
│       ├── patterns/                   # Pattern-Bibliothek (später)
│       ├── platforms/                  # custom-backends.md, processwire.md, …
│       └── assets/
│           └── templates/              # ux-critique.md, system-profile.md, …
│
├── evals/                              # Evaluation (nicht Teil der Nutzlast)
│   ├── evals.json                      # Prompts, Erwartungen, Assertions (Spec-Format)
│   ├── trigger-queries.json            # ~20 Anfragen für die Aktivierung
│   ├── rubric-calibration.md           # Kalibrierungsfälle für die Skalenanker
│   └── fixtures/                       # Testprojekte A–D
│
├── tests/
│   ├── structural/                     # Frontmatter, Verweise, Budgets, skills-ref
│   └── behavior/                       # Läufe mit/ohne Skill, Auswertung
│
└── docs/                               # Projektplan, Recherche, Entscheidungen
```

Abweichungen vom Plan (Kap. 4.2):

| Plan | Vorschlag | Grund |
|---|---|---|
| `SKILL.md` im Wurzelverzeichnis | `skills/editorial-ux-skill/SKILL.md` | Projektdateien nicht in die Nutzlast ziehen; Namensregel unabhängig vom Repo-Namen (D-002, D-003) |
| `commands/` | `references/cmd-*.md` | `commands/` ist nicht standardisiert und mit Claude Code verwechselbar; Spec kennt `references/` (D-004) |
| `templates/` | `assets/templates/` | Spec-Konvention für statische Ressourcen |
| `evals/rubric.md` | `references/methodology.md` (Skalen) und `evals/rubric-calibration.md` (Kalibrierung) | Der Agent braucht die Skalenanker **zur Laufzeit**, die Kalibrierfälle nur zum Testen |
| `evals/scenarios`, `evals/fixtures` | `evals/evals.json`, `evals/fixtures/` | Spec-Format für Evals (D-007) |
| `tests/fixtures` | entfällt | Fixtures nur einmal, unter `evals/` |

## 3. Lademodell

```
Start der Sitzung        name + description                          (~100 Token)
Aktivierung              SKILL.md                                    (< 500 Zeilen, < 5000 Token)
Befehl ausgeführt        Dateien laut Ladetabelle für diesen Befehl  (je Datei budgetiert)
```

**Ladetabelle** (in `SKILL.md`): Je Befehl eine Zeile mit allen benötigten Dateien. Befehlsanleitungen verweisen **nicht** weiter, damit die Verweistiefe bei eins bleibt (Spec).

Beispiel (Struktur, kein Inhalt):

| Befehl | Lädt |
|---|---|
| `critique` | `references/cmd-critique.md`, `references/methodology.md`, `assets/templates/ux-critique.md` |
| `discover` | `references/cmd-discover.md`, `platforms/custom-backends.md` (+ Adapter, falls erkannt), `assets/templates/system-profile.md` |

**Budgets:** Ein Test (`tests/structural/`) erfasst Zeilen und Bytes jeder Datei und prüft sie gegen eine Budgetdatei (Muster wie bei Impeccable, siehe Analyse 3.2). Eine Erhöhung ist eine bewusste, dokumentierte Entscheidung. Zusätzlich wird **je Befehl die geladene Gesamtmenge** gemessen.

## 4. Befehle

Unverändert gegenüber Plan Kap. 5 (Matrix gilt). Neu, verbindlich für `SKILL.md`:

- **Aufruf ohne Argument:** kurzes Menü, **kein** automatisches Ausführen.
- **Unklarer Befehl:** einmal nachfragen.
- **Fehlende Profile:** mit gekennzeichneten Annahmen arbeiten oder gezielt fragen (Plan 5.3).
- **Befehle, die Code ändern** (`implement`, `improve`): nur nach den Regeln aus Plan 9.4.

*Annahme (ungeprüft):* Die Argumentübergabe `/editorial-ux-skill <befehl>` funktioniert in Claude Code wie vorgesehen. Wird vor dem Schreiben von `SKILL.md` gegen die Claude-Code-Dokumentation geprüft. Falls nicht, wäre die Alternative ein Skill je Befehl, was die Aktivierungskosten erhöht.

## 5. Qualitätssicherung als Teil der Architektur

| Ebene | Prüft | Wo |
|---|---|---|
| Struktur | Frontmatter nach Spec (`skills-ref validate`), Namens- und Verzeichnisregel, aufgelöste Verweise, Verweistiefe 1, Budgets | `tests/structural/` |
| Aktivierung | Löst die `description` bei den richtigen Anfragen aus, bei Beinahe-Treffern nicht? | `evals/trigger-queries.json` |
| Wirkung | Mit/ohne Skill auf denselben Fixtures; Trefferquote, Falschbefunde, Reproduzierbarkeit, Kontext- und Zeitaufwand | `evals/evals.json` |
| Methodik | Skalenanker kalibriert an Referenzfällen | `evals/rubric-calibration.md` |

## 6. Ehrlichkeitsmechanismen

Direkt in `SKILL.md` verankert, nicht nur in Referenzen:

1. **Evidenzstufen** (beobachtet / Hypothese / Annahme) für jede Aussage in Berichten.
2. **Degradiert-Hinweis:** Konnte eine geforderte Prüfung nicht laufen (kein Browser, kein Screenshot, kein Werkzeug), beginnt der Bericht mit einer Zeile wie `⚠️ Eingeschränkt: <Grund>`. Betroffene Aussagen werden zu Hypothesen herabgestuft. (Idee aus der Impeccable-Analyse 4, eigene Formulierung.)
3. **Keine erfundenen Benutzerbedürfnisse:** Unbekanntes wird erfragt oder als Annahme gekennzeichnet (Plan 3.2).

## 7. Was bewusst nicht Teil der Architektur ist

- Eigene Laufzeit, Binärdateien, Detektor-Engine (Plan 9.1).
- Build-Pipeline für viele Agenten in Version 1. Agentenspezifische Pakete kommen erst, wenn die Quelle stabil ist (Plan 9.2).
- Persistente Dateien im Projekt des Nutzers (z. B. ein Profil-Ordner): offen, siehe D-012.
- Mehrere Sub-Agenten für isolierte Bewertung: zurückgestellt, siehe D-013.

## 8. Ergebnis der Modularisierungsprüfung (Plan 4.4)

| Frage | Befund |
|---|---|
| Ist die Aufteilung in `references/` sinnvoll? | **Ja.** Spec und Impeccable folgen demselben Prinzip; Wirkung entsteht aber nur mit Budgets und Ladetabelle. |
| Ist die Dateizahl aus Plan 4.2 gerechtfertigt? | **Nicht vorab.** Impeccable zeigt, dass viele Dateien funktionieren können (45 Referenzdateien), aber nur mit erzwungenen Budgets und breiter Testabdeckung. Wir starten mit ca. 5 Referenzdateien und wachsen evidenzbasiert. |
| Sind fünf Säulen als Dateien nötig? | **Nein.** Die Säulen bleiben **fachliche Gliederung** innerhalb weniger Referenzdateien. Eigene Dateien je Säule erst, wenn eine Datei sein Budget sprengt. |
| Sind 8 Befehle zu viel? | **Nicht für 1.0**, wenn sie sich gemäß Matrix unterscheiden. Eingeführt werden sie stufenweise (Alpha: `critique`). |
| Braucht der Skill Skripte? | **Nein** für Alpha. Ein späterer, optionaler Struktur-Linter wäre denkbar (nur Entwicklungswerkzeug). |
