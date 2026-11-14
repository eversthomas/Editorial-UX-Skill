# Agent Skills – Kompatibilität

Recherche zu Phase 1 (Projektplan Kap. 9, 12, 15): Was verlangt die Agent-Skills-Spezifikation, und was folgt daraus für Editorial UX Skill?

## 1. Quellen und Prüfstatus

| Quelle | Status |
|---|---|
| Offizielle Spec: Repository https://github.com/agentskills/agentskills (Datei `docs/specification.mdx`, Commit `83021e2b`, 2026-11-04, Apache-2.0) | **Im Volltext gelesen** |
| Ergänzende Seiten desselben Repos: `skill-creation/best-practices.mdx`, `evaluating-skills.mdx`, `optimizing-descriptions.mdx`, `client-implementation/adding-skills-support.mdx` | Überflogen (Überschriften, einzelne Abschnitte) |
| `agentskills.io/specification` (Website) | **Nicht abrufbar**: der Host ist im Netzwerk dieser Sitzung gesperrt. Die Inhalte stammen aus dem Quell-Repository der Website. |
| Claude-Code-Dokumentation zu Skills (Slash-Befehle, Argumente, Zusatzfelder) | **Nicht gelesen**. Alle Aussagen dazu sind unten als *Annahme* markiert. |
| Verhalten anderer Agenten (Cursor, Codex, Gemini CLI, Antigravity) | **Nicht geprüft** |

## 2. Was die Spezifikation verlangt (beobachtet)

### Verzeichnis

```
skill-name/
├── SKILL.md          # Pflicht: Metadaten + Anweisungen
├── scripts/          # optional
├── references/       # optional
├── assets/           # optional
└── ...               # beliebige weitere Dateien
```

### Frontmatter

| Feld | Pflicht | Regeln |
|---|---|---|
| `name` | ja | 1–64 Zeichen, nur Kleinbuchstaben, Ziffern, Bindestriche; nicht am Anfang/Ende; **keine doppelten Bindestriche**; **muss dem Namen des übergeordneten Verzeichnisses entsprechen** |
| `description` | ja | 1–1024 Zeichen; soll beschreiben, **was** der Skill tut **und wann** er genutzt wird; mit Schlüsselbegriffen |
| `license` | nein | Name oder Verweis auf Lizenzdatei, kurz halten |
| `compatibility` | nein | max. 500 Zeichen; nur bei besonderen Umgebungsanforderungen |
| `metadata` | nein | Map String → String, eindeutige Schlüsselnamen empfohlen |
| `allowed-tools` | nein | Leerzeichen-getrennte Liste vorab freigegebener Werkzeuge, **experimentell** |

### Progressive Disclosure

1. **Metadaten** (ca. 100 Token) werden beim Start für alle Skills geladen.
2. **Anweisungen:** `SKILL.md` wird bei Aktivierung vollständig geladen, **empfohlen < 5000 Token und unter 500 Zeilen**.
3. **Ressourcen** (`references/`, `scripts/`, `assets/`) werden nur bei Bedarf geladen.

Dateiverweise sind relative Pfade ab Skill-Wurzel. **Verweise nur eine Ebene tief** von `SKILL.md` aus, keine tiefen Verweisketten. Referenzdateien klein und fokussiert halten.

### Validierung

Das Referenzwerkzeug `skills-ref validate ./mein-skill` (Python, im Repo unter `skills-ref/`) prüft Frontmatter und Namensregeln.

### Zu Evaluation und Beschreibungen (Best Practices der Spec-Autoren)

- Evals gehören nach `evals/evals.json`: Testfälle mit `prompt`, `expected_output`, optional `files` und `assertions`.
- Jeder Fall wird **mit und ohne Skill** (oder gegen die Vorversion) in sauberem Kontext ausgeführt. Ergebnisse je Lauf: `outputs/`, `timing.json` (Tokens, Dauer), `grading.json` (Assertions mit Beleg), aggregiert in `benchmark.json`.
- Assertions müssen **prüfbar** sein; Qualitäten wie Gestaltung eignen sich besser für menschliche Durchsicht.
- Die `description` wird separat auf **Auslösung** getestet: ca. 20 Anfragen, 8–10 sollen auslösen, 8–10 nicht, bevorzugt knappe **Beinahe-Treffer** als Negativfälle. Imperativ formulieren („Use this skill when …“), an Nutzerabsicht statt Implementierung ausrichten.
- Zu umfangreiche Skills können schaden. Knappe, schrittweise Anleitung mit Beispiel schlägt erschöpfende Dokumentation.

## 3. Folgen für Editorial UX Skill

Jede Folge ist mit dem betroffenen Planabschnitt verknüpft. Vorschläge zur Entscheidung stehen in `decisions.md`.

### 3.1 Namensregel kollidiert mit der Repository-Schreibweise (Handlungsbedarf)

- Der Skill heißt `editorial-ux-skill` (Plan Kap. 1). Die Spec verlangt aber, dass `name` dem **Verzeichnisnamen** entspricht.
- Das GitHub-Repository heißt aktuell `Editorial-UX-Skill` (Großbuchstaben). Wird das Repository-Verzeichnis selbst als Skill-Ordner installiert (z. B. durch `git clone` nach `.claude/skills/`), stimmt der Verzeichnisname nicht mit dem `name` überein.
- Lösungen: (a) Repository in Kleinschreibung `editorial-ux-skill` umbenennen, oder (b) den Skill in einen Unterordner `skills/editorial-ux-skill/` legen (siehe 3.2), sodass der Repository-Name keine Rolle spielt.
- Empfehlung: **beides** (siehe D-002, D-003).

### 3.2 Projektdateien und Skill-Nutzlast trennen

- Alles unter dem Skill-Ordner kann in den Kontext eines Agenten gelangen oder zumindest installiert werden. Projektdateien (`docs/`, `tests/`, `CONTRIBUTING.md`, Recherche) gehören nicht zur Nutzlast.
- Plan Kap. 4 legt `SKILL.md` ins Repository-Wurzelverzeichnis. Damit liegt die gesamte Projektstruktur im Skill-Ordner.
- Vorschlag: Skill-Nutzlast in `skills/editorial-ux-skill/`, Projektdateien daneben (siehe `architecture.md`).

### 3.3 „Befehle“ sind kein Konzept der Spec

- Die Spec kennt keine Unterbefehle. Befehle im Stil `/editorial-ux-skill critique` sind eine Konvention: ein Skill, dessen `SKILL.md` das Argument auswertet und die passende Referenzdatei lädt (so macht es auch Impeccable).
- *Annahme (ungeprüft):* In Claude Code wird `/<skill-name> <Argumente>` dem Skill als Argument übergeben. Zu bestätigen gegen die Claude-Code-Dokumentation, bevor `SKILL.md` geschrieben wird.
- Ein Befehlsdateien-Ordner `commands/` ist als „weitere Dateien“ erlaubt, aber nicht standardisiert. Weil Claude Code unter `.claude/commands/` ein eigenes Konzept hat, ist der Name verwechselbar. Besser: Befehlsanleitungen unter `references/` ablegen (siehe `architecture.md`).

### 3.4 Verweistiefe

- Spec: Verweise **eine Ebene** tief. Unser Plan (4.3) sieht vor, dass Befehlsdateien ihre Referenzen selbst nennen (SKILL.md → Befehlsdatei → Referenz, also zwei Ebenen).
- Anpassung: Die **Ladetabelle in `SKILL.md`** nennt je Befehl **alle** benötigten Dateien. Befehlsdateien verweisen nicht weiter. Das hält die Tiefe bei eins.

### 3.5 Frontmatter-Felder

- Nur `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools` sind Spec. Felder wie `argument-hint` oder `user-invocable` (bei Impeccable zu sehen) stammen von einzelnen Agenten.
- Konsequenz: Kern-`SKILL.md` verwendet **nur Spec-Felder**. Agentenspezifische Zusatzfelder kommen in agentenspezifische Pakete (Plan 9.2), nicht in die Quelle.
- *Annahme (ungeprüft):* Unbekannte Felder werden von anderen Agenten ignoriert oder mit einer Warnung quittiert. Die Spec empfiehlt Clients lenient validation (Abschnitt „Lenient validation“ in `adding-skills-support.mdx`, nicht im Detail gelesen).

### 3.6 Größe von `SKILL.md`

- Hartes Ziel: **unter 500 Zeilen und unter 5000 Token**. Das ist ein Kriterium für den Strukturtest (`tests/structural/`).
- Ladetabelle, Prinzipien, Befehlsübersicht, Gotchas und die Regeln zur Evidenzkennzeichnung gehören hinein, alles Übrige in Referenzen.

### 3.7 `description`

- Max. 1024 Zeichen, englisch (Plan 9.5), imperativ, mit Beispielen für Situationen, in denen der Skill gilt, auch wenn der Nutzer das Wort „UX“ nicht nennt („redaktionelles Backend“, „CMS-Formular“, „Verwaltungsmaske“, „Freigabeprozess“).
- Abgrenzung nach außen (Plan 2): „Not for backend business logic, database design, or public marketing websites.“ (die Abgrenzung zu Frontend-Marketing-Seiten schützt vor Fehlaktivierung bei Nachbarskills).
- Neu im Plan: **Aktivierungs-Eval** mit ca. 20 Anfragen inkl. Beinahe-Treffern (z. B. Landingpage-Design, API-Design, Datenbankschema).

### 3.8 Evals im Spec-Format

- Unsere Ordner `evals/scenarios` und `evals/fixtures` lassen sich auf das Spec-Muster abbilden: `evals/evals.json` (Prompts, Erwartungen, Assertions), `evals/files/` (Fixtures), Arbeitsverzeichnis `…-workspace/iteration-N/{eval}/{with_skill,without_skill}`.
- Das deckt den im Plan geforderten **Vergleich mit/ohne Skill** (Kap. 10) ab, samt `timing.json` für die Kontext- und Zeitmessung.
- `grading.json` mit Beleg je Assertion passt zu unserer Evidenzkennzeichnung.

### 3.9 Strukturvalidierung

- `skills-ref validate` kann in `tests/structural/` laufen. Es ist eine **Entwicklungsabhängigkeit** (Python), keine Laufzeitabhängigkeit des Skills. Das ist mit „keine obligatorische externe Laufzeit“ (Plan 9.1) vereinbar, solange der Skill selbst ohne es funktioniert.
- *Nicht geprüft:* ob `skills-ref` in dieser Umgebung ohne Installation lauffähig ist. Das testen wir, sobald es eine `SKILL.md` gibt.

## 4. Was ungeprüft bleibt

1. Claude-Code-spezifische Auswertung von Argumenten und Slash-Aufrufen, Berechtigungen, Zusatzfelder.
2. Verhalten und Installationspfade von Cursor, Codex, Gemini CLI, Antigravity.
3. Ob `skills-ref` die Namensregel „Verzeichnisname = name“ strikt prüft (laut Spec-Text ja, nicht ausprobiert).
4. Aktuelle Version der Spec im Zeitverlauf. Die Spec ist veränderlich (Plan 7: „veränderliche Referenzen“); der gelesene Stand ist Commit `83021e2b` vom 2026-11-04.
