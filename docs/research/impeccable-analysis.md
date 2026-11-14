# Impeccable – Analyse

Recherche zu Phase 1 (Projektplan Kap. 12 und 15). Ziel: Impeccable als **Referenz** verstehen, nicht als Vorlage zum Kopieren.

## 1. Untersuchungsgrundlage

| | |
|---|---|
| Repository | https://github.com/pbakaus/impeccable |
| Geprüfter Stand | Commit `61e73eeb` (shallow clone, 2026-11-13) |
| Methode | Direkte Lektüre des Quellcodes: `LICENSE`, `NOTICE.md`, `README.md`, `skill/SKILL.src.md`, ausgewählte `skill/reference/*.md`, `scripts/token-budget.json`, `docs/DEVELOP.md`, `tests/` (Struktur und Kopf von `activation.eval.mjs`) |
| Zusätzlich gelesen (Nachtrag) | `skill/reference/operate.md`, `shape.md`, `harden.md` (Anfang), `critique-rubric.md` (Cognitive Load, Heuristik-Skalen, Personas) und die Bänder in `critique.md` |
| Nicht gelesen | Rust-Engine (`crates/`), Browser-Extension, VS-Code-Extension, Live-Modus im Detail, übrige Referenzdateien im Volltext (u. a. `new-work*.md`, `document.md`, `onboard.md`, `clarify.md`) |

Aussagen unten sind **beobachtet** (im Quelltext gesehen), sofern nicht als *Hypothese* gekennzeichnet.

## 2. Lizenz (zuerst geklärt, wie im Plan gefordert)

- **Beobachtet:** `LICENSE` ist die Apache License 2.0. Das Frontmatter der Skill-Datei nennt `license: Apache 2.0`.
- **Beobachtet:** `NOTICE.md` führt eine Drittquelle: `skill/reference/ios.md` und `android.md` sind aus ehmo/`platform-design-skills` (MIT) abgeleitet.
- **Abweichung vom Plan:** Der Projektplan (Kap. 11) nennt MIT für *dieses* Projekt. Das ist unabhängig von Impeccable möglich, solange kein Impeccable-Inhalt übernommen wird.

Folgen:

1. **Ideen, Methoden und Strukturprinzipien** lassen sich frei als Orientierung nutzen. Das Urheberrecht schützt konkrete Ausdrucksformen (Texte, Code), keine Konzepte.
2. **Textübernahme oder enge Paraphrase** von Impeccable-Dateien ist für uns ausgeschlossen. Täte man es, müssten Apache-Lizenztext, Urhebervermerke, Änderungshinweise und ggf. NOTICE-Einträge mitgeführt werden, und die Datei bliebe Apache-lizenziert. Das würde das MIT-Ziel verwässern.
3. **Der Name „Impeccable“** wird nicht verwendet. Apache-2.0 gewährt keine Markenrechte (Abschnitt 6 der Lizenz).
4. Beim Anlegen eigener Referenzen gilt: aus allgemein zugänglichen Primärquellen (Nielsen Norman Group, WCAG, WAI-ARIA Authoring Practices) schreiben, nicht aus Impeccable-Dateien ableiten. Eine Herkunftsangabe pro Referenzdatei wird Pflicht (siehe `decisions.md`, D-006).

Dies ist keine Rechtsberatung. Vor dem Release (Phase 7) wird die Lizenzprüfung ohnehin wiederholt.

## 3. Architektur

### 3.1 Ein Skill, viele Befehle

- **Beobachtet:** Impeccable ist **ein einziger Skill** (`name: impeccable`) mit einem Einstiegspunkt. Unterbefehle (`critique`, `audit`, `polish`, …) sind **Argumente**, keine eigenen Skills. `SKILL.src.md` enthält eine Befehlstabelle (24 Befehle in den Kategorien Build, Evaluate, Refine, Enhance, Fix, Iterate), die auf je eine Referenzdatei verweist.
- **Beobachtet:** Ohne Argument liest der Agent `routing.md` und zeigt ein kontextabhängiges Menü. Er führt **nie** automatisch einen Befehl aus.
- **Beobachtet:** `SKILL.src.md` ist nur 93 Zeilen lang. Die eigentliche Arbeit steckt in `skill/reference/` (45 Dateien, zusammen ca. 458 KB).

### 3.2 Progressive Disclosure mit hartem Budget

- **Beobachtet:** `scripts/token-budget.json` legt für **jede** LLM-sichtbare Datei ein Byte-Limit fest (z. B. `SKILL.src.md` 12 750 Bytes, `critique.md` 30 500). Die Einhaltung wird im Build erzwungen. Jedes Limit gilt als „reviewte Entscheidung“, eine Erhöhung braucht eine Begründung.
- **Beobachtet:** Zusätzlich gibt es Budgets pro gängigem Nutzungsfall („was wird vor der ersten Änderung geladen“).
- **Beobachtet:** Das Setup lädt Referenzen schrittweise („Load the request's playbook“), nicht alles auf einmal.

### 3.3 Projektkontext als Dateien

- **Beobachtet:** `init` schreibt `PRODUCT.md` (Zielgruppe, Zweck, Rahmenbedingungen), `document` schreibt `DESIGN.md` (visuelles System). Jeder spätere Befehl liest sie. Ein `doctor`-Befehl prüft veraltete Kontextdateien.
- **Beobachtet:** Ein Launcher-Skript (`impeccable context`) lädt diese Dateien deterministisch.

### 3.4 Modi

- **Beobachtet:** Impeccable unterscheidet vier Modi: **Persuade, Operate, Read, Experience**. Admin-UIs, Editoren und Dashboards fallen unter **Operate**: „Scanability, consistency, native expectations … outrank expression.“
- **Beobachtet (`operate.md`, 5 KB):** Die Operate-Anleitung ist **kurz und fast rein visuell**: Typografie (eine Schriftfamilie, feste rem-Skala), Farbe (zurückhaltend, Statusvokabular), Layout (strukturelle Responsivität), Komponenten (alle Zustände, Skeleton-Loading, Empty States, konsistente Affordanzen), Bewegung (150–250 ms), Verbote (z. B. „Modal as first thought“) und „Product permissions“ (Dichte, Standardnavigation). Das Leitbild ist: „The tool should disappear into the task.“
- **Beobachtet:** `operate.md` enthält **nichts** zu Rollen, Freigabeprozessen, Veröffentlichungsstatus, Mehrfachbearbeitung, Datenpflege-Arbeitsabläufen, Berechtigungskonzepten oder zu Besonderheiten bestimmter CMS.
- **Beobachtet (`shape.md`, 3,5 KB):** `shape` ist ein **Discovery-Interview** (zwei Runden, Fragen zu Zweck, Personen, Zuständen, Grenzen), das mit einem bestätigten **Design-Brief ohne Code** endet. Ohne menschliche Antwortmöglichkeit werden Annahmen „plainly“ markiert. Das entspricht in Teilen unserem `design` (Konzeptstufe) und der Regel „Annahmen kennzeichnen“.
- **Beobachtet (`harden.md`):** Härtung gegen Randfälle (lange Texte, Fehler, Internationalisierung) mit viel CSS-Beispielcode; Schwerpunkt Produktionsreife von Oberflächen, nicht Arbeitsabläufe.
- **Schluss:** Die Hypothese ist damit **bestätigt**: Impeccable behandelt Admin-UIs als Modus mit visuellem und Komponenten-Schwerpunkt. Aufgabenfluss, Rollen und redaktionelle Arbeit sind **nicht Gegenstand** der gelesenen Dateien.

### 3.5 Verteilung

- **Beobachtet:** Eine Build-Pipeline erzeugt aus einer Quelle die Formate für sehr viele Agenten (Verzeichnisse wie `.claude`, `.cursor`, `.codex`, `.gemini`, `.kiro` usw.). Platzhalter wie `{{command_prefix}}` werden pro Anbieter ersetzt.
- **Beobachtet:** Zusätzlich gibt es eine Rust-Engine mit 62 deterministischen Regeln (`impeccable detect`), eine Browser-Extension, ein VS-Code-Plugin und einen Live-Modus. Der Skill nutzt ein mitgeliefertes Binary.

## 4. Befehle und Bewertung

### critique

- **Beobachtet:** Zwei **voneinander isolierte** Assessments als getrennte Sub-Agents: A (Design-Review) und B (Detektor und Browser-Evidenz). A muss fertig sein, bevor B-Ergebnisse in den Hauptkontext gelangen, damit B das Urteil nicht „verankert“.
- **Beobachtet:** Läuft das im Einzelkontext (kein Sub-Agent-Werkzeug), muss die **erste Zeile** des Berichts lauten: `⚠️ DEGRADED: single-context (<Grund>)`. Ein stilles Degradieren gilt als fehlgeschlagener Lauf.
- **Beobachtet:** Bewertung nach Nielsens 10 Heuristiken, je 0–4, Summe max. 40, Bänder (36–40 „Excellent“, 28–35 „Good“, 20–27 „Acceptable“, 12–19 „Poor“, 0–11 „Critical“), Probleme mit Schweregrad **P0–P3**. Heuristiken dürfen als `n/a` markiert werden; dann zählt der Prozentwert (90 %+ Excellent usw.).
- **Beobachtet (`critique-rubric.md`, 20 KB):** (1) Cognitive-Load-Teil mit drei Lastarten (intrinsisch, extraneous, germane), einer 8-Punkte-Checkliste (Ergebnis nach Anzahl der Fehlpunkte) und der „Working Memory Rule“ (≤ 4 Elemente, mit Verweis auf Cowan 2001), (2) je Heuristik **Prüfpunkte und eine eigene 0–4-Skala mit Ankern** (z. B. 0 „No feedback; user is guessing what happened“, 4 „every action confirms, progress is always visible“), (3) fünf **Personas** (z. B. „Impatient Power User“, „Confused First-Timer“, „Accessibility-Dependent User“, „Deliberate Stress Tester“, „Distracted Mobile User“) mit der Möglichkeit projektspezifischer Personas.
- **Beobachtet (Unterschied zu uns):** Impeccable bildet eine **Gesamtsumme mit Bandbezeichnung**. Eine einzelne schwere Schwäche (z. B. Accessibility) kann darin untergehen; Schweregrade P0–P3 mildern das nur auf Befundebene. Unser Plan (6.2) verlangt ausdrücklich, dass ein Gesamtwert eine schwere Schwäche nicht verdeckt (Blocker-Regel). Das ist ein **bewusster methodischer Unterschied**.
- **Hinweis zur Quellenlage:** Die Rubrik stellt feste Schwellen (z. B. „≤ 4 Items“, „German is often 30 % longer“) als Tatsachen dar. Für unsere Methodik gilt: Solche Zahlen nur übernehmen, wenn sie aus Primärquellen belegt sind (D-006), und als Richtwerte kennzeichnen.
- **Beobachtet:** Das Ergebnis wird als Snapshot persistiert, der Chat-Bericht ist das Hauptergebnis. Die abschließende Rückfrage steht immer **zuletzt**.

### audit

- **Beobachtet:** Rein **technisch**, behebt nichts. Fünf Dimensionen (Accessibility, Performance, Theming, Responsive, Anti-Patterns), je 0–4 mit Ankern, Befunde als P0–P3. Native Plattformen laufen über eine eigene Datei.

### polish, harden, …

- **Beobachtet:** Viele „Verfeinerungsbefehle“ (bolder, quieter, distill, harden, onboard …), die jeweils eine konkrete Veränderungsrichtung beschreiben. Der Schwerpunkt liegt auf visueller Gestaltung und Interface-Verbesserung.

## 5. Tests und Evaluation

- **Beobachtet:** `tests/` ist umfangreich und enthält klar getrennte Arten von Tests:
  - **Skill-Aktivierung:** `skill-behavior/activation.eval.mjs` simuliert, ob ein Modell den Skill **allein anhand der Frontmatter-`description`** lädt. 54 Fälle × 2 Samples × 2 Modelle, gemessen werden Recall, Falsch-Positive und Fehlschläge je Kategorie, mit Gates (null Falsch-Positive, Mindest-Recall pro Modell).
  - **Verhalten:** `skill-behavior/scenarios.test.mjs`, `skill-workflow/*` (Ende-zu-Ende), `new-work-e2e/`.
  - **Struktur und Budget:** `skill-reference.test.mjs`, `token-budget.test.mjs`.
  - **Fixtures** (`tests/fixtures/`) und ein „Oracle“.
- **Beobachtet:** Evals brauchen API-Schlüssel (`.env`), sind also nicht Teil des normalen Entwickler-Laufs, sondern ein separater Suite-Lauf.
- *Hypothese:* Es gibt keinen systematischen **Vergleich mit/ohne Skill** zur Wirkungsmessung wie im Plan Kap. 10 vorgesehen. Die Aktivierungs-Evals messen, **ob** der Skill lädt, nicht, **ob das Ergebnis besser ist**. Ich habe nicht alle Testdateien gelesen.

## 6. Übertragbarkeit auf Editorial UX Skill

### Übernehmen (als Idee)

| Prinzip | Warum |
|---|---|
| Ein Skill, Befehle als Argumente, Befehlstabelle in `SKILL.md` | Passt zur Spec, hält den Aktivierungsaufwand klein |
| Kurzer `SKILL.md`, schwere Inhalte in Referenzen | Entspricht der Spec-Empfehlung (Kap. 4.3 im Plan) |
| Dateibudgets, im Test erzwungen | Verhindert schleichendes Wachsen, belegt Kontextsparsamkeit |
| Isolierte Bewertung und das **DEGRADED-Banner** | Deckt sich mit unserem Grundsatz „keine erfundenen Ergebnisse“ |
| Schweregrade P0–P3 neben Scores | Trennt Priorität von Qualität |
| Aktivierungs-Eval für die `description` | Fehlt in unserem Plan bisher |
| Kein automatisches Ausführen bei leerem Aufruf | Verträgt sich mit unserer Freigabe-Leitplanke |
| Persistierte Kontextdateien als gemeinsames Gedächtnis der Befehle | Löst „Befehle müssen unabhängig und trotzdem informiert sein“ |

### Nicht übernehmen

| Element | Grund |
|---|---|
| Mitgeliefertes Binary / Rust-Engine / Detektor | Widerspricht „keine externe Laufzeit“ (Plan 9.1). Optional später als Script, nie als Pflicht. |
| 24 Befehle | Viele sind visuelle Feinsteuerung (bolder, quieter, overdrive). Das ist nicht unser Fokus. |
| Der Anspruch „bessere Ästhetik“, Anti-AI-Slop-Fokus | Wir erzwingen keine Ästhetik (Plan 3.4) |
| Browser-Extension, Live-Modus, Multi-Provider-Build | Für 1.0 unverhältnismäßig |
| Visuelle Welten und Persuade/Experience-Modi | Außerhalb unseres Geltungsbereichs |

### Abgrenzung (Hypothese, noch zu schärfen)

Impeccable ist ein **Interface-Gestaltungs- und Review-Skill** mit starkem visuellen Fokus, der Admin-UIs als Modus „Operate“ mitbehandelt. Editorial UX Skill setzt **Aufgaben, Rollen, Arbeitsabläufe und Fehlertoleranz im redaktionellen Alltag** an die erste Stelle und behandelt Visuelles als eine von zehn Dimensionen. Belegt durch `operate.md`, `shape.md`, `harden.md` und `critique-rubric.md` (Abschnitt 3.4). Ungelesen: `onboard.md`, `clarify.md`, `document.md`; sie ändern die Abgrenzung voraussichtlich nicht.

## 7. Offene Punkte

1. ~~`operate.md`, `shape.md`, `harden.md`, `critique-rubric.md` lesen~~ (erledigt, siehe 3.4 und 4).
2. Prüfen, ob Impeccable irgendwo Wirkungsvergleiche (mit/ohne Skill) veröffentlicht. **Offen.**
3. Die Nielsen-Heuristiken und Cognitive-Load-Methoden aus **Primärquellen** einordnen (Plan Phase 1, Aufgabe 5), nicht über Impeccable. **Offen**, Quellen (nngroup.com, w3.org) sind in dieser Sitzung noch nicht zugänglich.
