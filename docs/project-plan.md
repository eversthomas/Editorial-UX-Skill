# Editorial UX Skill – Projektplan

> Design the work, not just the interface.

Projektarchitektur und Entwicklungsplan (Version 3, angepasst nach Phase-1-Recherche; Begründungen in `decisions.md`)

Projektziel: Entwicklung eines universellen, eigenständigen Open-Source-Skills zur Analyse, Konzeption, Gestaltung, Implementierung und Qualitätsverbesserung von redaktionellen und administrativen Benutzeroberflächen.

| | |
|---|---|
| Name des Skills | `editorial-ux-skill` (identisch mit dem Repository-Namen) |
| Repository | `editorial-ux-skill` |
| Befehlspräfix | `/editorial-ux-skill <befehl>` |
| Lizenzvorschlag | MIT |
| Primäre Entwicklungsumgebung | Claude Code |
| Gleichrangige Zielumgebung | **Cursor** (belegt: liest `.claude/skills/` und `.agents/skills/`; D-016) |
| Weitere Zielumgebungen | Codex, Gemini CLI, Antigravity und weitere Agenten mit Skill-Unterstützung (ungeprüft) |

## Änderungen gegenüber Version 2 (Phase-1-Recherche)

Grundlage: `research/impeccable-analysis.md`, `research/agent-skills-compatibility.md`, `research/cursor-compatibility.md`, `architecture.md`, `decisions.md`.

1. **Layout:** Nutzlast in `skills/editorial-ux-skill/`, Projektdateien daneben (D-003, Kap. 4).
2. **Befehle** als `references/cmd-<name>.md` statt `commands/`; Auswertung aus dem Anfragetext, keine Platzhalter (D-004, D-017, Kap. 4, 5).
3. **Verweistiefe eins**, Ladetabelle in `SKILL.md` (D-015, Kap. 4.3).
4. **Nur Spec-Felder** im Frontmatter (D-005, Kap. 9.1).
5. **Cursor** gleichrangig, gemeinsamer Installationsort (D-016, Kap. 9.2).
6. **Verteilung:** Ordner ab Alpha, Plugin und Marketplace ab Beta (D-018, Kap. 9.2).
7. **Evals im Spec-Format** plus Aktivierungs-Eval, je Agent getrennt (D-007, Kap. 10).
8. **Größenbudgets** im Strukturtest (D-008, Kap. 4.3, 10).
9. **Evidenz- und Eingeschränkt-Regeln** in `SKILL.md` (D-009, Kap. 6.2).
10. **Offene Entscheidungen** D-011 (Skalenbreite), D-012 (Profil-Persistenz), D-013 (Isolation) werden in Phase 2/3 anhand von Messungen entschieden.
11. **Namensregel:** Ordnername = `name` = `editorial-ux-skill` (Spec, Cursor).

## Änderungen von Version 1 zu Version 2

Rückmeldungen zum ersten Entwurf:

1. Schlanker Start statt vollständiger Struktur (Kap. 4, 12, 13).
2. Befehle klar abgegrenzt, mit Befehlsmatrix (Kap. 5).
3. „test“ wird zu `walkthrough` und als Simulation gekennzeichnet (Kap. 5, 6.3).
4. Reproduzierbares Scoring durch verankerte Skalen (Kap. 6.2).
5. Joy of Use mit beobachtbaren Kriterien (Kap. 6.1 J).
6. Regel zum Umgang mit vorhandenen Designsystemen (Kap. 3.4).
7. Plattformadapter: zuerst generisch und ProcessWire (Kap. 7).
8. Leitplanken für Code-Änderungen (Kap. 9.4).
9. Namen vereinheitlicht: `editorial-ux-skill`, einheitlich Plural bei Ordnern.
10. Umgang mit Impeccable und dessen Lizenz festgelegt (Kap. 12, Phase 1).
11. Messbare Definition of Done (Kap. 14).
12. Sprachentscheidung (Kap. 9.5).
13. Evaluation läuft von Beginn an mit (Kap. 10, 12).

---

## 1. Produktvision

Editorial UX Skill befähigt KI-Coding-Agenten dazu, administrative Benutzeroberflächen und redaktionelle Arbeitsumgebungen so zu entwickeln und zu verbessern, dass Menschen gerne, effizient und intuitiv mit ihnen arbeiten.

Der Skill verbindet:

- Human-Centered Design
- Editorial UX
- Interaction Design
- Information Architecture
- Cognitive Load Management
- Visual Interface Design
- Accessibility
- Workflow Design
- Usability Engineering
- Design Systems
- Joy of Use

Der Skill ist nicht auf ein bestimmtes CMS, Framework oder Backend-System beschränkt. Er soll gleichermaßen für WordPress, ProcessWire, Drupal, Headless CMS, individuell entwickelte CMS, interne Verwaltungsanwendungen, Dashboards und andere administrative Werkzeuge funktionieren.

### Leitgedanke

Ein Backend ist nicht nur eine technische Verwaltungsoberfläche. Es ist ein Arbeitsplatz.

Seine Qualität bemisst sich nicht allein an der technischen Funktionalität oder der visuellen Gestaltung, sondern daran, wie gut es Menschen bei ihrer tatsächlichen Arbeit unterstützt.

### Drei zentrale Prinzipien

1. **Understand the System** – Zuerst das vorhandene System, seine Architektur, seine Möglichkeiten und Einschränkungen verstehen. Keine vorschnellen Designentscheidungen.
2. **Design for the User** – Die Arbeitsrealität, mentalen Modelle, Fähigkeiten und Bedürfnisse der tatsächlichen Benutzer bestimmen die Gestaltung.
3. **Joy is a Quality Criterion** – Effizienz, Verständlichkeit, Barrierefreiheit und Freude an der Benutzung sind gleichwertige Qualitätsdimensionen.

---

## 2. Abgrenzung und Geltungsbereich

Der Skill konzentriert sich auf die Benutzererfahrung innerhalb administrativer und redaktioneller Systeme.

Dazu gehören:

- CMS-Backends
- Redaktionssysteme
- Content-Management-Plattformen
- Verwaltungsoberflächen
- Interne Organisationsanwendungen
- Dashboards
- Dokumentenmanagement
- Workflow-Anwendungen
- Konfigurationsoberflächen
- Datenpflege- und Erfassungssysteme
- Individuell entwickelte Backends

Nicht Gegenstand des Skills ist die allgemeine Entwicklung von Backend-Geschäftslogik, Datenbankarchitekturen oder APIs ohne Bezug zur Benutzeroberfläche.

Technische Backend-Strukturen werden allerdings berücksichtigt, wenn sie die Gestaltung oder Benutzbarkeit der Oberfläche beeinflussen.

---

## 3. Grundarchitektur

Der Skill wird modular entwickelt. Die Architektur besteht aus fünf fachlichen Säulen. Die Säulen sind eine **fachliche Gliederung** des Wissens, keine eins-zu-eins-Entsprechung zu Befehlen oder Dateien (Zuordnung siehe Kap. 5).

### 3.1 System Intelligence

Der Agent untersucht zunächst die vorhandene technische Umgebung.

Aufgaben:

- Framework und CMS identifizieren
- Projektstruktur untersuchen
- vorhandene Komponenten erkennen
- Datenmodelle und Content-Strukturen verstehen
- Erweiterungsmöglichkeiten identifizieren
- vorhandene Designsysteme erkennen
- Berechtigungs- und Rollenkonzepte untersuchen
- technische Einschränkungen dokumentieren
- vorhandene UX-Probleme identifizieren

Ergebnis ist ein nachvollziehbares Systemprofil.

### 3.2 Editorial Experience

Diese Säule beschäftigt sich mit der redaktionellen Arbeitsrealität.

Aufgaben:

- Benutzergruppen identifizieren
- typische Aufgaben ermitteln
- Nutzungssituationen untersuchen
- redaktionelle Arbeitsabläufe verstehen
- mentale Modelle erkennen
- Informationsbedürfnisse untersuchen
- kognitive Belastung analysieren
- unnötige Arbeitsschritte identifizieren

Der Agent darf keine Benutzerbedürfnisse erfinden. Unbekannte Informationen müssen als Annahmen gekennzeichnet oder gezielt erfragt werden.

### 3.3 Interaction Design

Hier werden die konkreten Interaktionen gestaltet.

Schwerpunkte:

- Navigation
- Formulare
- Eingabefelder
- Listen und Tabellen
- Filter und Suchfunktionen
- Editoren
- Medienverwaltung
- Statusanzeigen
- Dialoge
- Kontextinformationen
- Feedback und Fehlermeldungen
- Undo und Redo
- Inline-Bearbeitung
- Bulk Actions
- Progressive Disclosure

### 3.4 Visual Experience

Diese Säule verantwortet die visuelle Qualität.

Schwerpunkte:

- Typografie
- visuelle Hierarchie
- Farbkonzepte
- Spacing
- Layout
- Informationsdichte
- Komponenten
- Icons
- Animationen
- Mikrointeraktionen
- Responsivität
- Design Tokens
- konsistente Gestaltung

Der Skill erzwingt keine universelle Designästhetik. Dafür gilt eine feste **Rangfolge**:

1. **Vorhandenes Designsystem verwenden.** Erkennt der Agent im Projekt ein Designsystem, Design Tokens oder konsistente Komponenten (System Intelligence), richtet er sich danach. Abweichungen müssen begründet und freigegeben werden.
2. **Teilweise vorhanden:** Der Agent leitet die implizite Gestaltung (Farben, Abstände, Typografie) aus dem Bestand ab, dokumentiert sie und ergänzt nur das Nötigste.
3. **Nichts vorhanden:** Der Agent schlägt ein schlankes, zurückhaltendes Token-Set vor und lässt es freigeben, bevor es angewendet wird.

Eigene Gestaltungsvorlieben des Agenten haben keinen Vorrang vor dem Bestand.

### 3.5 Quality Engineering

Die abschließende Säule prüft die Qualität.

Schwerpunkte:

- Usability
- Accessibility
- Interaktionskonsistenz
- technische Robustheit
- Fehlertoleranz
- Performance
- Responsives Verhalten
- Verständlichkeit
- Aufgaben-Effizienz
- Joy of Use

---

## 4. Repository-Struktur

Die Struktur wird **stufenweise** aufgebaut. Nicht benötigte Dateien werden nicht auf Vorrat angelegt. Eine Datei entsteht erst, wenn ein konkreter Inhalt, ein Test oder ein Befehl sie braucht.

### 4.1 Startstruktur (Alpha 0.1)

```
editorial-ux-skill/                      # Repository
├── README.md
├── LICENSE
├── skills/
│   └── editorial-ux-skill/              # Skill-Nutzlast; Ordnername = name
│       ├── SKILL.md                     # Prinzipien, Befehlstabelle, Ladetabelle, Gotchas
│       ├── references/
│       │   ├── cmd-critique.md          # Befehlsanleitung
│       │   ├── methodology.md           # Dimensionen A–J, Skalenanker, Evidenzstufen
│       │   ├── principles.md
│       │   └── anti-patterns.md
│       └── assets/
│           └── templates/
│               └── ux-critique.md
├── evals/
│   ├── evals.json                       # Prompts, Erwartungen, Assertions (Spec-Format)
│   ├── trigger-queries.json             # ca. 20 Anfragen zur Aktivierung
│   ├── rubric-calibration.md            # Kalibrierfälle für die Skalenanker
│   └── fixtures/                        # Testprojekt D
├── tests/
│   ├── structural/
│   └── behavior/
└── docs/                                # Plan, Recherche, Entscheidungen, Roadmap
```

Der Skill-Ordner enthält **nur**, was ein Agent zur Laufzeit braucht. `docs/`, `evals/` und `tests/` liegen außerhalb der Nutzlast (D-003). Die Nutzlast folgt zugleich dem Plugin-Layout `skills/<name>/SKILL.md` von Claude Code, Cursor und Agent Plugins, was die spätere Verteilung erleichtert (D-018).

### 4.2 Zielstruktur (spätestens 1.0)

Die folgende Struktur ist ein **Architekturvorschlag und eine Obergrenze**, kein Pflichtumfang. Jedes Element muss sich durch Evaluationsergebnisse oder konkreten Bedarf rechtfertigen (Eintrag in `docs/decisions.md`). Ordnernamen sind durchgehend im Plural, bis auf den Skill-Ordner selbst.

```
editorial-ux-skill/
├── README.md  LICENSE  CONTRIBUTING.md  CODE_OF_CONDUCT.md  CHANGELOG.md
│
├── skills/
│   └── editorial-ux-skill/
│       ├── SKILL.md
│       ├── references/
│       │   ├── cmd-discover.md      cmd-critique.md     cmd-audit.md
│       │   ├── cmd-improve.md       cmd-walkthrough.md  cmd-design.md
│       │   ├── cmd-implement.md     cmd-document.md
│       │   ├── principles.md        methodology.md      anti-patterns.md
│       │   ├── system-intelligence.md   editorial-experience.md
│       │   ├── interaction-design.md    information-architecture.md
│       │   ├── cognitive-load.md        visual-experience.md
│       │   ├── joy-of-use.md            accessibility.md
│       │   └── quality-assurance.md
│       ├── platforms/
│       │   ├── custom-backends.md   # Pflicht: generischer Adapter
│       │   └── processwire.md       # erster spezifischer Adapter
│       ├── patterns/                # forms, navigation, tables, content-editors,
│       │                            # media-management, search-and-filter,
│       │                            # status-feedback, workflows, bulk-actions
│       └── assets/templates/        # system-profile, editorial-profile, ux-critique,
│                                    # ux-audit, design-brief, walkthrough-report
│
├── evals/                           # evals.json, trigger-queries.json, rubric-calibration.md, fixtures/
├── tests/                           # structural/, behavior/
├── docs/
└── community/                       # Adapter-Beiträge (WordPress, Drupal, Headless, Laravel, ...)
```

Änderungen gegenüber Version 1 und 2: Nutzlast unter `skills/editorial-ux-skill/`; `commands/` wird `references/cmd-*.md`; `templates/` wird `assets/templates/`; `reference/` wird `references/`; Fixtures nur unter `evals/`; weitere Adapter in `community/` außerhalb der Nutzlast, bis sie geprüft sind. Die Säulen aus Kap. 3 bleiben **fachliche Gliederung**. Eigene Referenzdatei je Säule entsteht erst, wenn eine Datei ihr Budget sprengt (`architecture.md`, 8).

### 4.3 Kontextmanagement

Zentrale Referenzen werden bei Bedarf geladen. Der Agent soll nicht bei jeder kleinen Aufgabe sämtliche Dokumente einlesen. Konkret (Agent Skills Spec, D-008, D-015):

- **`SKILL.md` unter 500 Zeilen und unter 5 000 Token.** Die wichtigsten Regeln (Evidenzstufen, Eingeschränkt-Hinweis, Freigabe vor Codeänderungen) stehen **am Anfang**, weil Claude Code nach einer Kontext-Kompaktierung nur die ersten 5 000 Token je Skill behält.
- **Ladetabelle in `SKILL.md`:** je Befehl eine Zeile mit **allen** benötigten Dateien. Befehlsanleitungen verweisen nicht weiter (Verweistiefe eins).
- Jede Referenzdatei ist eigenständig lesbar.
- **Größenbudgets** je Datei und je Befehl (geladene Gesamtmenge) in einer Budgetdatei, vom Strukturtest erzwungen. Zahlen werden in Phase 2 an den ersten echten Dateien festgelegt, nicht vorab geraten.
- Das Kontextbudget wird in der Evaluation gemessen (`timing.json`, Kap. 10), nicht nur geschätzt.

### 4.4 Modularisierung kritisch prüfen

Ob die Aufteilung wirklich sinnvoll ist, wird in Phase 1 geprüft und als Entscheidung in `docs/decisions.md` festgehalten. Zusammenlegen oder Streichen ist ausdrücklich erlaubt, wenn Dateien klein bleiben oder sich inhaltlich überschneiden.

---

## 5. Befehle und Arbeitsmethodik

Der Skill erhält eine einheitliche Befehlsschnittstelle. Die konkrete Umsetzung muss mit dem jeweiligen Agenten kompatibel sein.

**Umsetzung (D-004, D-017):** Es gibt **einen** Skill. Die Befehle sind keine eigenen Skills, sondern Argumente: `SKILL.md` enthält die Befehlstabelle und die Ladetabelle, die Anleitung je Befehl liegt in `references/cmd-<name>.md`. `SKILL.md` verwendet **keine Platzhalter** wie `$ARGUMENTS` (nur Claude Code kennt sie). Der Agent leitet den Befehl aus dem Text der Anfrage ab (Befehlswort oder klar erkennbare Absicht). Ohne eindeutigen Befehl fragt er einmal nach. Ein Aufruf ohne Argument zeigt ein kurzes Menü und führt **nichts** automatisch aus. Ob Cursor den Text hinter `/editorial-ux-skill` in die Nachricht übernimmt, ist ungeprüft; die natürlichsprachliche Anfrage funktioniert in jedem Fall.

### 5.1 Befehle

Einige Befehle der ersten Version wurden zusammengelegt oder umbenannt, weil sie sich überschnitten:

- `analyze` geht in `discover` auf (Systemprofil **und** Editorial-Profil sind Teil der Entdeckung).
- `shape` und `design` werden zu **einem** Befehl `design` mit zwei Stufen (erst Konzept und Freigabe, dann Detailgestaltung).
- `test` heißt `walkthrough`, siehe 6.3.

| Befehl | Zweck | Stufe |
|---|---|---|
| `/editorial-ux-skill critique` | Bestehende UX nach den Dimensionen A–J bewerten (Experten-Evaluation) | Alpha 0.1 |
| `/editorial-ux-skill discover` | System und redaktionelle Arbeitsrealität untersuchen | Alpha 0.2 |
| `/editorial-ux-skill audit` | Prüfbare Qualitätskriterien abarbeiten (Accessibility, Konsistenz, Robustheit; bestanden/nicht bestanden) | Alpha 0.2 |
| `/editorial-ux-skill improve` | Kleinen, abgegrenzten Verbesserungszyklus durchführen (kritisieren → entwerfen → umsetzen → prüfen) | Alpha 0.3 |
| `/editorial-ux-skill walkthrough` | Aufgaben simuliert durchgehen (siehe 6.3) | Beta |
| `/editorial-ux-skill design` | Lösung konzipieren, dann UI und Interaktionen gestalten | Beta |
| `/editorial-ux-skill implement` | Freigegebene Gestaltung umsetzen | Beta |
| `/editorial-ux-skill document` | Ergebnisse und Designentscheidungen dokumentieren | Beta |

### 5.2 Befehlsmatrix

Jeder Befehl muss klar sagen, was er liest, erzeugt und woran er sich abgrenzt.

| Befehl | Liest (Eingabe) | Erzeugt (Ausgabe) | Verändert Code? | Abgrenzung |
|---|---|---|---|---|
| `discover` | Code, Konfiguration, ggf. Rückfragen | Systemprofil, Editorial-Profil | nein | Beschreibt, bewertet nicht |
| `critique` | UI (Code, Screenshots, Beschreibung); optional Profile | Bewertung nach A–J mit Scores, Belegen, Priorität | nein | Qualitative Experten-Bewertung, nicht bestanden/nicht bestanden |
| `audit` | UI, Code, ggf. Werkzeugergebnisse | Prüfliste mit Ergebnis je Kriterium | nein | Objektivierbare Kriterien, keine Geschmacksurteile |
| `walkthrough` | Aufgabendefinition, UI | Schrittprotokoll mit Orientierung, Entscheidungslast, Fehlerrisiko | nein | Aufgaben statt Gesamtoberfläche |
| `design` | Profile, Befunde, Ziel | Design-Brief, Konzept, Entwurf | nein | Entwirft, setzt nicht um |
| `implement` | freigegebener Entwurf | Codeänderungen | **ja** | Nur nach Freigabe (siehe 9.4) |
| `improve` | UI, Verbesserungsziel | kleiner Zyklus aus Befund, Entwurf, Umsetzung, Prüfung | **ja** | Kleiner Umfang; für große Vorhaben die Einzelbefehle nutzen |
| `document` | Ergebnisse, Entscheidungen | Entscheidungs- und Designdokumentation | nur Doku | Hält fest, entscheidet nicht |

Diese Matrix ist die verbindliche Grundlage für die Befehlsdateien. Ändert sich ein Befehl, wird die Matrix mit angepasst.

### 5.3 Standardworkflow

Der vollständige Entwicklungsprozess:

1. Discover
2. Critique / Audit
3. Walkthrough
4. Design
5. Implement
6. Critique / Audit (erneut)
7. Improve
8. Document

Die Befehle müssen auch unabhängig voneinander funktionieren. Ein Benutzer soll beispielsweise eine bestehende Oberfläche direkt mit `critique` untersuchen können, ohne vorher einen vollständigen Prozess durchlaufen zu müssen. Fehlt ein Profil, arbeitet der Befehl mit klar gekennzeichneten Annahmen oder fragt gezielt nach.

### 5.4 Grundregel

Nicht jede Aufgabe benötigt alle Schritte. Der Agent wählt den angemessenen Umfang anhand der konkreten Aufgabe. Eine kleine Formularverbesserung darf nicht unnötig zu einer vollständigen Systemanalyse führen.

---

## 6. Die redaktionelle UX-Methodik

Dies ist der wichtigste eigenständige Teil des Projekts. Der Skill benötigt eine eigene Bewertungsmethodik.

### 6.1 Editorial UX Evaluation

Folgende Dimensionen werden bewertet:

**A. Orientierung**

- Ist die aktuelle Position innerhalb des Systems erkennbar?
- Ist die Navigation verständlich?
- Sind Zusammenhänge sichtbar?

**B. Aufgabenverständlichkeit**

- Ist klar, was zu tun ist?
- Sind Aktionen eindeutig benannt?
- Ist das Ergebnis einer Aktion vorhersehbar?

**C. Informationsarchitektur**

- Entspricht die Struktur dem mentalen Modell der Benutzer?
- Sind Informationen sinnvoll gruppiert?
- Ist die Informationsdichte angemessen?

**D. Interaktionsqualität**

- Sind Eingaben intuitiv?
- Sind Zustände verständlich?
- Gibt es unmittelbares Feedback?

**E. Kognitive Belastung**

- Wie viele Entscheidungen muss der Benutzer treffen?
- Werden Informationen zum richtigen Zeitpunkt angezeigt?
- Gibt es unnötige Gedächtnisbelastung?

**F. Fehlertoleranz**

- Sind Fehler vermeidbar?
- Lassen sich Änderungen korrigieren?
- Sind Fehlermeldungen hilfreich?

**G. Arbeitsfluss**

- Wie viele Schritte sind für typische Aufgaben erforderlich?
- Gibt es unnötige Unterbrechungen?
- Werden wiederkehrende Aufgaben unterstützt?

**H. Visuelle Qualität**

- Ist die Oberfläche ruhig und konsistent?
- Sind Hierarchien verständlich?
- Ist die Informationsdichte ausgewogen?

**I. Accessibility**

- Ist die Oberfläche per Tastatur bedienbar?
- Sind Kontraste und Fokuszustände ausreichend?
- Werden semantische Strukturen und assistive Technologien berücksichtigt?

**J. Joy of Use**

Joy of Use ist eine gleichwertige Qualitätsdimension, wird aber **nur über beobachtbare Merkmale** bewertet, nicht über Geschmack. Prüfkriterien:

- **Kontrollgefühl:** Sind Aktionen rückgängig zu machen? Ist der Systemzustand jederzeit erkennbar?
- **Rückmeldungsqualität:** Bestätigen Aktionen ihr Ergebnis verständlich und im richtigen Maß?
- **Reibung:** Gibt es unnötige Unterbrechungen, Wiederholungen oder Umwege?
- **Konzentration:** Unterstützt die Oberfläche ungestörtes Arbeiten (keine unnötigen Ablenkungen, ruhige Darstellung)?
- **Souveränität:** Können erfahrene Benutzer schneller arbeiten (Tastenkürzel, Voreinstellungen, Wiederholungshilfen)?

Solange diese Kriterien nicht evaluiert wurden (Phase 6), wird J getrennt ausgewiesen und fließt nicht in einen Gesamtwert ein.

### 6.2 Bewertungssystem

Jede Dimension erhält:

- einen Score von 0 bis 5
- eine Begründung
- konkrete Beobachtungen (mit Belegen, z. B. Datei, Bildschirm, Schritt)
- Verbesserungsvorschläge
- eine Priorität

**Verankerte Skala.** Scores gelten nur mit definierten Ankern, damit Bewertungen reproduzierbar sind. Details und Beispiele je Dimension stehen in `evals/rubric.md`. Die Grundanker:

| Score | Bedeutung |
|---|---|
| 0 | Kriterium nicht erfüllt, Aufgabe wird behindert oder unmöglich |
| 1 | Gravierende Mängel, Aufgabe nur mit Umwegen oder Vorwissen lösbar |
| 2 | Deutliche Mängel, regelmäßig störend |
| 3 | Brauchbar, mit erkennbaren Schwächen |
| 4 | Gut, nur kleine Verbesserungen nötig |
| 5 | Vorbildlich, keine relevanten Mängel erkennbar |

**Evidenzstufen.** Jede Beobachtung trägt genau eine Kennzeichnung:

- **Beobachtet:** direkt im Code, in der Oberfläche oder durch ein Werkzeug belegt.
- **Hypothese:** begründet vermutet, aber nicht geprüft.
- **Annahme:** ungeprüfte Voraussetzung (z. B. über Benutzer).

Scores dürfen sich nur auf beobachtete Befunde stützen. Hypothesen und Annahmen werden getrennt aufgeführt.

**Kein verdeckender Gesamtwert.** Ein Gesamtwert darf nicht verdecken, dass beispielsweise eine schwerwiegende Accessibility-Schwäche besteht. Deshalb gilt:

- Ergebnisse werden immer je Dimension ausgewiesen.
- Erreicht eine Dimension 0 oder 1, wird sie als **Blocker** gesondert hervorgehoben, unabhängig vom Durchschnitt.
- Ein Gesamtwert ist optional und wird nie ohne die Dimensionsübersicht genannt.

**Reproduzierbarkeit.** Die Methodik gilt als reproduzierbar, wenn mehrere unabhängige Durchläufe auf denselben Fixtures in Bewertung und Priorisierung eng zusammenliegen. Die Zielwerte stehen in Kap. 14.

### 6.3 Aufgabenbasierte Prüfung

Die eigentliche Stärke soll die aufgabenbasierte Bewertung sein.

Beispiele:

- Einen neuen Inhalt erstellen.
- Einen bestehenden Inhalt bearbeiten.
- Ein Bild austauschen.
- Eine Veröffentlichung vorbereiten.
- Einen Fehler korrigieren.
- Mehrere Einträge gleichzeitig bearbeiten.
- Einen bestimmten Datensatz finden.

Der Agent untersucht, wie gut die Oberfläche diese Aufgaben unterstützt. Er bewertet nicht nur die Anzahl der Klicks, sondern auch Orientierung, Entscheidungslast, Fehlerrisiko und Verständlichkeit.

**Wichtige Einschränkung:** Ein Agent führt **keine echten Usability-Tests mit Benutzern** durch. Der Befehl `walkthrough` ist ein **simulierter, expertenbasierter Durchgang** (angelehnt an Cognitive Walkthrough). Ergebnisse gelten als Hypothesen, nicht als empirische Nutzerbefunde. Jeder Bericht weist das ausdrücklich aus und kann Empfehlungen für echte Tests mit Nutzern enthalten.

Der Begriff „Test“ ist reserviert für Tests des Skills selbst (Kap. 10).

---

## 7. Plattformadapter

Die universelle Methodik wird durch plattformspezifische Kenntnisse ergänzt.

Jeder Adapter beschreibt:

1. Grundarchitektur der Plattform.
2. Typische Content- und Datenmodelle.
3. Möglichkeiten der UI-Anpassung.
4. Vorhandene Komponenten und Interaktionsmuster.
5. Berechtigungs- und Rollenkonzepte.
6. Technische Grenzen.
7. Best Practices.
8. Typische UX-Probleme.
9. Erweiterungsmöglichkeiten.
10. Hinweise zur sicheren Implementierung.

Die Adapter sind optional. Unbekannte Systeme müssen ebenfalls analysierbar sein. Dafür gibt es den generischen Adapter `custom-backends.md`, der **zuerst** entsteht.

**Umfang:** Das Projekt liefert zunächst nur den generischen Adapter und einen spezifischen Adapter (ProcessWire, als gut bekannte Plattform). Alle weiteren (WordPress, Drupal, Headless-CMS, Frameworks) werden Community-Beiträge nach einer Adapter-Vorlage und festgelegten Qualitätskriterien. Das begrenzt den Pflegeaufwand und verhindert veraltetes Halbwissen.

Wichtig: Plattformdokumentationen müssen als veränderliche Referenzen behandelt werden. Der Agent soll bei konkreten Implementierungen die jeweils aktuelle offizielle Dokumentation prüfen, anstatt veraltete API-Annahmen zu übernehmen.

---

## 8. Design- und Interaktionsmuster

Der Skill erhält eine eigene Pattern-Bibliothek, die im Lauf des Projekts wächst und nicht vorab vollständig angelegt wird.

Sie soll nicht ausschließlich aus visuellen Beispielen bestehen, sondern erklären:

- Welches Problem wird gelöst?
- In welcher Situation ist das Muster sinnvoll?
- Welche Alternativen gibt es?
- Welche Vor- und Nachteile bestehen?
- Welche Accessibility-Anforderungen gelten?
- Welche technischen Voraussetzungen bestehen?

Beispiele:

- Intelligente Formulargruppen
- Kontextuelle Hilfestellungen
- Inline-Bearbeitung
- Autosave mit nachvollziehbarem Status
- Vorschau während der Bearbeitung
- Progressive Disclosure
- Mehrstufige Eingabeprozesse
- Bulk Editing
- Filterbare Datentabellen
- Kontextuelle Medienauswahl
- Undo- und Redo-Mechanismen
- Status- und Freigabeanzeigen
- Entwürfe und Versionshistorie

Die Pattern-Bibliothek soll im Laufe des Projekts durch reale Anwendungserfahrungen wachsen.

---

## 9. Technische Anforderungen

### 9.1 Grundprinzipien

- Keine Abhängigkeit von Impeccable.
- Keine Abhängigkeit von einem bestimmten KI-Anbieter.
- Kompatibilität mit dem Agent Skills Standard: Frontmatter der Quelle enthält **nur Spec-Felder** (`name`, `description`, `license`, `metadata`; D-005). Claude Code ignoriert Unbekanntes, der claude.ai-Upload bricht bei Zusatzfeldern ab, Cursor kennt nur eine Teilmenge. `name` ist immer gesetzt und **gleich dem Ordnernamen** (`editorial-ux-skill`; Spec und Cursor verlangen das). Offen: Cursors Umgang mit `license`/`compatibility`.
- Markdown-basierte Kernarchitektur.
- Keine obligatorischen Cloud-Dienste.
- Keine API-Schlüssel erforderlich.
- Keine obligatorische externe Laufzeit.
- Keine unnötigen Build-Abhängigkeiten.
- Keine vorgeschriebenen UI-Frameworks.
- Keine vorgeschriebenen Designsysteme.

### 9.2 Portabilität

Die zentrale Skill-Quelle bleibt agentenunabhängig. Bei Bedarf können daraus agentenspezifische Installationspakete erzeugt werden.

Die erste Version soll sich ohne Buildprozess direkt in **Claude Code und Cursor** einsetzen lassen (D-016):

- **Gemeinsamer Installationsort** `.claude/skills/editorial-ux-skill/` (alternativ `.agents/skills/`). Cursor liest laut offizieller Doku auch `.claude/skills/`. **Keine Zweitkopie** unter `.cursor/skills/`.
- **Alpha:** Ordner kopieren oder verlinken.
- **Beta:** Plugin- und Marketplace-Dateien (`.claude-plugin/marketplace.json`, `.cursor-plugin/marketplace.json`), getrennt von der Nutzlast (D-018). Das Layout `skills/<name>/SKILL.md` ist bereits plugin-kompatibel.
- **Nach 1.0, optional:** Aufnahme in den öffentlichen Cursor-Marketplace (manueller Review, Open Source Pflicht) und das Anthropic-Verzeichnis.
- Kein `npx`-Installer (widerspricht „keine Build-Abhängigkeiten“).
- Weitere Agenten (Codex, Gemini CLI, Antigravity): erst nach geprüfter Installation (Phase 6).

### 9.3 Keine unnötigen Automatisierungen

Der Skill soll zunächst auf der vorhandenen Fähigkeit des KI-Coding-Agenten aufbauen.

Browserautomatisierung, Screenshot-Analyse und automatisierte Accessibility-Tests werden unterstützt, sofern die jeweilige Umgebung entsprechende Werkzeuge bereitstellt.

Fehlende Werkzeuge dürfen nicht durch erfundene Testergebnisse ersetzt werden. Der Agent benennt, was er nicht prüfen konnte, und markiert betroffene Aussagen als Hypothese oder Annahme.

### 9.4 Leitplanken für Code-Änderungen

Da der Skill auch implementiert, gelten für `implement` und `improve` verbindliche Regeln:

1. **Freigabe zuerst:** Code wird erst nach einem freigegebenen Entwurf geändert. Bei `improve` genügt eine kurze Ankündigung des Umfangs, bei größeren Eingriffen eine ausdrückliche Zustimmung.
2. **Kleine, nachvollziehbare Schritte:** Änderungen werden in überschaubaren Einheiten umgesetzt, die sich einzeln prüfen und zurücknehmen lassen (z. B. getrennte Commits).
3. **Bestehenden Stil respektieren:** Der Agent folgt vorhandenen Konventionen, Komponenten und Designsystemen (siehe 3.4), statt neue Muster einzuführen.
4. **Keine Seiteneffekte auf Daten und Logik:** Geschäftslogik, Datenmodelle und Berechtigungen werden nur geändert, wenn das ausdrücklich Teil der Aufgabe ist.
5. **Aktuelle Plattformdokumentation prüfen** (siehe Kap. 7), bevor plattformspezifische APIs verwendet werden.
6. **Prüfung nach der Änderung:** Betroffene Bereiche werden erneut mit `critique` oder `audit` geprüft. Nicht prüfbare Punkte werden offen benannt.
7. **Sichere Voreinstellung:** Keine destruktiven Operationen (Löschen, Überschreiben, Migrationen) ohne Bestätigung.

### 9.5 Sprache

- **Skill-Inhalte** (`SKILL.md`, `references/`, `commands/`, `patterns/`, `templates/`, `evals/`) werden auf **Englisch** verfasst, weil Anweisungen für Agenten dort am zuverlässigsten funktionieren und die Zielgruppe international ist.
- **Projektdokumente** (dieser Plan, Entscheidungen, Roadmap) dürfen deutsch sein.
- **Ausgaben des Skills** richten sich nach der Sprache des Benutzers.
- Übersetzungen der Dokumentation sind ein Community-Thema (Kap. 11).
- Dies ist eine Startentscheidung und wird in `docs/decisions.md` festgehalten.

---

## 10. Qualitätssicherung und Evaluation

Der Skill darf sich nicht allein durch gute Formulierungen definieren. Es muss nachweisbar sein, dass er bessere Ergebnisse hervorbringt.

**Evaluation läuft von Beginn an mit.** Schon in Phase 2 entsteht mindestens ein Testprojekt mit Aufgaben und Erwartungen. Jede neue Fähigkeit wird gegen die Evaluation geprüft, bevor sie als fertig gilt.

**Vergleichsbasis:** Es wird immer verglichen: derselbe Agent, dieselbe Aufgabe, **mit** und **ohne** Skill. Nur so ist ein Mehrwert belegbar.

**Format (D-007):** Evals folgen dem Spec-Muster. `evals/evals.json` enthält je Fall `prompt`, `expected_output`, `files` und `assertions`. Jeder Lauf entsteht in sauberem Kontext in einem Arbeitsverzeichnis `…-workspace/iteration-N/<fall>/{with_skill,without_skill}/` mit `outputs/`, `timing.json` (Tokens, Dauer), `grading.json` (Assertion mit Beleg) und aggregiert `benchmark.json`. Assertions müssen prüfbar sein; Qualitäten wie Gestaltung werden zusätzlich menschlich durchgesehen.

**Aktivierungs-Eval:** `evals/trigger-queries.json` mit ca. 20 Anfragen (8–10 sollen auslösen, 8–10 nicht, Negativfälle als **Beinahe-Treffer**, z. B. Landingpage-Design, API-Design, Datenbankschema). Geprüft wird, ob die `description` richtig auslöst. Ziel: keine Falsch-Positive bei den Beinahe-Treffern.

**Je Agent getrennt:** Ergebnisse werden für Claude Code und Cursor getrennt ausgewiesen, damit Unterschiede sichtbar werden. Der Praxistest in Cursor (Skill unter `.claude/skills/` gefunden, Text hinter `/editorial-ux-skill` angekommen, Verhalten bei `license`/`compatibility`) gehört an das Ende von Phase 2.

### Testprojekte

**Testprojekt D: Bestehende schlechte Oberfläche** (zuerst)

Ein absichtlich ungünstig gestaltetes Backend mit **dokumentierter Liste eingebauter Probleme** (Fixture, versteckte Lösungsliste). Der Agent muss die Probleme erkennen, priorisieren und konkrete Verbesserungen durchführen. Es dient als erster Maßstab, weil sich Trefferquote und Fehlalarme direkt messen lassen.

**Testprojekt A: Klassisches CMS**

Eine typische redaktionelle Oberfläche mit:

- Seitenverwaltung
- Formularen
- Medienverwaltung
- Navigation
- Veröffentlichungsstatus

**Testprojekt B: Individuelles PHP-Backend**

Ein eigens entwickeltes Backend mit:

- Datensätzen
- Such- und Filterfunktionen
- Formularen
- Benutzerverwaltung
- Verwaltungsprozessen

**Testprojekt C: Komplexe Verwaltungsoberfläche**

Eine Anwendung mit:

- unterschiedlichen Rollen
- komplexen Arbeitsabläufen
- Statusübergängen
- Freigaben
- umfangreichen Tabellen

### Testverfahren

Jede Testumgebung wird mit definierten Aufgaben und erwarteten Ergebnissen versehen.

Bewertet werden:

- Erkennung vorhandener UX-Probleme (Trefferquote und Fehlalarme)
- Qualität der Analyse
- Angemessenheit der Konzeption
- Qualität der Implementierung
- Einhaltung technischer Rahmenbedingungen
- Verbesserung der Aufgabenbedienbarkeit
- Accessibility
- visuelle Konsistenz
- Konsistenz der Scores über mehrere Durchläufe (Reproduzierbarkeit)
- Kontext- und Zeitaufwand des Agenten

Zusätzlich werden statische Prüfungen und, soweit verfügbar, Browser- und Interaktionstests durchgeführt.

Es sollen sowohl die Ergebnisse als auch die tatsächlichen Arbeitsschritte des Agenten bewertet werden.

**Strukturtests** (`tests/structural/`) prüfen formale Eigenschaften des Skills: `skills-ref validate` (Entwicklungswerkzeug, keine Laufzeitabhängigkeit), Ordnername = `name`, nur zulässige Zeichen, `description` vorhanden und höchstens 1 024 Zeichen, keine Platzhalter im Body, aufgelöste Verweise, **Verweistiefe eins**, Größenbudgets (`SKILL.md` unter 500 Zeilen und 5 000 Token). **Verhaltenstests** (`tests/behavior/`) prüfen das Verhalten von Agenten anhand der Szenarien aus `evals/`.

---

## 11. Open-Source-Strategie

Der Skill wird von Anfang an öffentlich entwickelbar konzipiert.

### Lizenz

Vorgeschlagen wird MIT. Die Lizenz soll eine möglichst unkomplizierte Nutzung, Anpassung und Weiterverbreitung ermöglichen.

Vor Veröffentlichung müssen sämtliche übernommenen Inhalte und Drittanbieterbestandteile auf ihre Lizenzbedingungen geprüft werden.

### Repository

Öffentliches GitHub-Repository: `editorial-ux-skill` (Kleinschreibung; die Umbenennung von `Editorial-UX-Skill` steht aus und ist für die Funktion nicht blockierend, D-002). Der Skill-Name entspricht dem Repository-Namen und dem Ordnernamen der Nutzlast.

### Dokumentation

Das Projekt benötigt:

- README
- Installationsanleitung
- Architekturübersicht
- Methodendokumentation
- Befehlsreferenz
- Plattformadapter-Dokumentation
- Beispiele
- Contribution Guide
- Changelog
- Lizenzinformationen

### Contribution

Externe Entwickler sollen insbesondere beitragen können zu:

- weiteren CMS-Adaptern (nach Adapter-Vorlage, siehe Kap. 7)
- zusätzlichen Interaktionsmustern
- neuen Testfällen
- Verbesserungen der Bewertungsmethodik
- Accessibility-Regeln
- Übersetzungen
- Agent-Kompatibilität

Fachliche Qualität soll Vorrang vor der bloßen Anzahl von Beiträgen haben.

---

## 12. Entwicklungsphasen

Die Phasen sind so geschnitten, dass früh ein **vertikaler Schnitt** entsteht: eine kleine, durchgehend funktionierende und messbare Fähigkeit, die danach erweitert wird. Die Evaluation begleitet jede Phase.

### Phase 1 – Grundlagen und Recherche

Ziel: Eine belastbare fachliche Grundlage schaffen.

**Stand:** Aufgaben 1, 2, 3 (Architektur) und 8 sind erledigt, Aufgabe 9 ist nur im Entwurf (offene Skalenbreite D-011). Aufgaben 4 bis 7 und `docs/methodology.md` sind offen und hängen am Zugriff auf Primärquellen (Nielsen Norman Group, W3C/WCAG).

Aufgaben:

1. Impeccable untersuchen (Architektur, Befehle, Referenzen, Tests). **Zuerst die Lizenz klären** und festhalten, was Orientierung bedeutet: Struktur und Ansätze analysieren ja, Texte oder Beispiele übernehmen nein.
2. Agent Skills Specification recherchieren und Kompatibilität dokumentieren.
3. Architektur und Arbeitsmethodik dokumentieren.
4. Relevante Design- und UX-Prinzipien extrahieren.
5. Nielsen-Heuristiken und Cognitive-Load-Methoden einordnen.
6. Editorial UX von allgemeinem UI-Design abgrenzen.
7. Bestehende CMS- und Admin-UX-Patterns untersuchen.
8. Die Modularisierung aus Kap. 4 kritisch prüfen.
9. Bewertungsmethodik (Skalenanker) entwerfen.

Ergebnis: Fachliches Fundament und Architekturentscheidung (`docs/research/*`, `docs/architecture.md`, `docs/decisions.md`).

Wichtig: Impeccable ist eine Referenz, keine technische Abhängigkeit und keine Quelle für ungeprüftes Kopieren.

### Phase 2 – Vertikaler Schnitt

Ziel: Eine funktionsfähige erste Skill-Version, die **eine** Sache messbar gut kann.

Aufgaben:

1. Layout anlegen (`skills/editorial-ux-skill/`, `evals/`, `tests/`) und **Strukturtest** (`skills-ref validate`, Namensregel, Verweise, Verweistiefe, Budgets).
2. `references/methodology.md` mit Dimensionen A–J, verankerten Skalen, Evidenzstufen und Schweregraden; `references/principles.md`, `references/anti-patterns.md`. Jede Referenz nennt ihre **Primärquellen** (D-006).
3. Testprojekt D mit Fixture und **versteckter Lösungsliste**; **Baseline ohne Skill** (mehrere Läufe).
4. `SKILL.md` (Prinzipien und Kernregeln zuerst, Befehlstabelle, Ladetabelle, Gotchas).
5. Befehl `critique` (`references/cmd-critique.md`) samt Vorlage `ux-critique.md`.
6. **Aktivierungs-Eval** (`evals/trigger-queries.json`).
7. Lauf mit Skill gegen die Baseline (Trefferquote, Falschbefunde, Streuung, Kontext und Zeit).
8. **Kalibrierlauf Skalenbreite** 0–5 gegen 0–4 (D-011).
9. **Praxistest in Cursor** (siehe Kap. 10).

Ergebnis: Editorial UX Skill Alpha 0.1. **Entscheidungspunkt:** Bringt der Skill messbar bessere Kritik? Wenn nein, wird die Methodik überarbeitet, bevor weiter gebaut wird.

### Phase 3 – Engine

Ziel: Die eigenständige fachliche Kompetenz ausbauen.

Aufgaben:

1. Befehle `discover` und `audit`.
2. Aufgabenbasierte Analyse (Grundlage für `walkthrough`).
3. Cognitive-Load-Bewertung ausarbeiten.
4. Joy-of-Use-Kriterien erproben und kalibrieren.
5. Priorisierungssystem entwickeln.
6. Reproduzierbarkeit messen (mehrere Durchläufe).

Ergebnis: Editorial UX Skill Alpha 0.2.

### Phase 4 – Plattformintelligenz

Ziel: Das universelle Systemverständnis realisieren.

Aufgaben:

1. Generischen Backend-Adapter entwickeln.
2. ProcessWire-Adapter erstellen.
3. Adapter-Vorlage und Qualitätskriterien für Community-Adapter.
4. Technische Analyseverfahren testen.
5. Plattformübergreifende Arbeitsweise prüfen (mindestens Testprojekte A und B).
6. Befehl `improve` mit Leitplanken (9.4).

Ergebnis: Editorial UX Skill Alpha 0.3.

### Phase 5 – Implementierung und Design

Ziel: Vollständige Entwicklungsunterstützung.

Aufgaben:

1. Befehle `design`, `implement`, `walkthrough`, `document`.
2. Designmethodik ausarbeiten (Rangfolge aus 3.4).
3. Implementierungsworkflow entwickeln.
4. Visuelle Qualitätsprüfung entwickeln.
5. Accessibility-Prüfung integrieren.
6. Browsergestützte Tests ermöglichen, sofern verfügbar.
7. Pattern-Bibliothek anhand echter Befunde aufbauen.

Ergebnis: Editorial UX Skill Beta 0.5.

### Phase 6 – Evaluation und Härtung

Ziel: Die tatsächliche Qualität nachweisen und Schwächen beseitigen.

Aufgaben:

1. Testprojekte A, B und C vervollständigen.
2. Definierte Redaktionsaufgaben durchführen.
3. Analyseergebnisse vergleichen.
4. Implementierungsergebnisse bewerten.
5. Schwächen der Skill-Anweisungen identifizieren.
6. Verhaltenstests über mehrere Agenten durchführen.
7. Methodik überarbeiten.

Ergebnis: Editorial UX Skill Beta 0.8.

### Phase 7 – Open-Source-Release

Ziel: Eine stabile, öffentlich nutzbare Version veröffentlichen.

Aufgaben:

1. Dokumentation vervollständigen.
2. Lizenzprüfung durchführen.
3. Installationswege testen.
4. Agent-Kompatibilität dokumentieren.
5. Beispiele bereitstellen.
6. Contribution Guide fertigstellen.
7. Repository veröffentlichen.
8. Version 1.0 taggen.

Ergebnis: Editorial UX Skill 1.0.

---

## 13. Priorisierung

Nicht alle Funktionen müssen von Beginn an umgesetzt werden. Die erste Version konzentriert sich auf die Kernkompetenzen.

### Priorität 1 – Unverzichtbar

- Kritische UX-Bewertung (`critique`) mit verankerter Rubrik
- Evaluation mit Vergleich ohne Skill (Testprojekt D)
- Systemanalyse (`discover`)
- Redaktionelle UX-Analyse
- Qualitätsprüfung (`audit`)
- Aufgabenorientierte Konzeption und Interaktionsdesign (Grundlagen)

### Priorität 2 – Für die Beta

- Generischer Adapter und ProcessWire-Adapter
- Befehle `design`, `implement`, `walkthrough`, `document`
- Pattern-Bibliothek
- Accessibility-Automatisierung
- Visuelle Gestaltung mit Designsystem-Rangfolge
- Mehrere Agentenformate

### Priorität 3 – Spätere Erweiterungen

- Weitere CMS- und Framework-Adapter (Community)
- Umfangreiche CMS-spezifische Wissensmodule
- Visuelle Testwerkzeuge
- Erweiterte Pattern-Kataloge
- Community-Beiträge
- Zusätzliche Evaluationsverfahren

---

## 14. Definition of Done für Version 1.0

Editorial UX Skill 1.0 gilt als fertig, wenn:

- Der Skill unabhängig von Impeccable funktioniert und die Lizenzklärung dokumentiert ist.
- Die Kernmethodik dokumentiert ist.
- Ein unbekanntes Backend systematisch analysiert werden kann (generischer Adapter, erfolgreich an mindestens einem fremden System getestet).
- Bestehende CMS-Strukturen berücksichtigt werden.
- Redaktionelle Arbeitsabläufe untersucht werden können.
- UX-Konzepte erstellt werden können.
- UI-Implementierungen unterstützt werden und die Leitplanken aus 9.4 eingehalten werden.
- Visuelle und funktionale Qualitätsprüfungen möglich sind.
- **Messbare Qualitätsschwellen** erreicht sind. Die endgültigen Zahlen werden in Phase 2 und 3 festgelegt, als Zielwerte gelten vorläufig:
  - Auf Testprojekt D findet der Agent mit Skill mindestens 80 % der dokumentierten Probleme und liefert deutlich bessere Ergebnisse als derselbe Agent ohne Skill.
  - Der Anteil nachweislich falscher oder erfundener Befunde bleibt unter einer festgelegten Schwelle.
  - Bei wiederholten Durchläufen auf denselben Fixtures weichen die Dimensionsscores im Regelfall um höchstens einen Punkt voneinander ab.
  - Die Priorisierung der drei wichtigsten Befunde stimmt über Durchläufe weitgehend überein.
- Mindestens drei unterschiedliche technische Umgebungen erfolgreich getestet wurden.
- Die Kernfunktionen mit mindestens drei verschiedenen KI-Coding-Agenten getestet wurden, **darunter Claude Code und Cursor** mit getrennt ausgewiesenen Ergebnissen.
- Strukturtest grün: Spec-Validierung, Ordnername gleich `name`, Verweistiefe eins, Budgets eingehalten; Aktivierungs-Eval ohne Falsch-Positive bei den Beinahe-Treffern.
- Dokumentation und Installation für externe Benutzer verständlich sind (geprüft durch mindestens eine Person, die das Projekt nicht kennt).
- Lizenz und Drittanbieterbestandteile geprüft wurden.

---

## 15. Arbeitsauftrag für Claude Code

Claude Code soll das Projekt nicht unmittelbar vollständig implementieren. Zunächst ist eine eigenständige Recherche- und Konzeptionsphase durchzuführen (Phase 1).

### Arbeitsmodus

- Eigenständig recherchieren.
- Offizielle Dokumentationen bevorzugen.
- Aktuelle Repository-Strukturen untersuchen.
- Fachliche Behauptungen anhand von Quellen prüfen.
- Technische Annahmen kennzeichnen.
- Keine ungeprüften Implementierungsentscheidungen treffen.
- Keine unnötigen Abhängigkeiten einführen.
- Keine vorzeitige Programmierung.

### Erste konkrete Aufgaben

1. Das originale Impeccable-Repository untersuchen, **zuerst Lizenz prüfen**.
2. Die vollständige Skill-Architektur erfassen.
3. Die Befehlsstruktur und Referenzdateien analysieren.
4. Die Testarchitektur untersuchen.
5. Die Agent Skills Specification recherchieren.
6. Die Übertragbarkeit auf Editorial UX Skill bewerten.
7. Die vorgeschlagene Architektur (Kap. 4, 5) kritisch prüfen, insbesondere Modularisierung, Befehlsabgrenzung und Dateianzahl.
8. Notwendige Anpassungen dokumentieren.
9. Eine konkrete Implementierungsreihenfolge vorschlagen (Grundlage: Kap. 12).
10. Erst nach Abschluss dieser Arbeit die Umsetzung vorbereiten.

### Erwartete Rechercheergebnisse

Im Repository sollen folgende Dokumente entstehen:

- `docs/research/impeccable-analysis.md`
- `docs/research/agent-skills-compatibility.md`
- `docs/architecture.md`
- `docs/methodology.md`
- `docs/development-roadmap.md`
- `docs/decisions.md`

Jede wesentliche Architekturentscheidung wird mit Begründung in `docs/decisions.md` dokumentiert.

Claude Code soll insbesondere prüfen, ob die vorgeschlagene Modularisierung tatsächlich sinnvoll ist oder unnötige Komplexität erzeugt.

---

## 16. Abschließende Produktentscheidung

Editorial UX Skill wird als eigenständiges Open-Source-Projekt entwickelt.

Es übernimmt keine technische Abhängigkeit von Impeccable. Es verwendet dessen erfolgreiche methodische Ansätze als Orientierung und entwickelt daraus eine eigene Fachdisziplin für redaktionelle und administrative Benutzererfahrungen.

Das Projekt soll nicht einfach bessere Admin-Oberflächen erzeugen. Es soll KI-Coding-Agenten dazu befähigen, Arbeitsumgebungen zu schaffen, in denen Menschen ihre Aufgaben gerne erledigen.

**Editorial UX Skill – Design the work, not just the interface.**
