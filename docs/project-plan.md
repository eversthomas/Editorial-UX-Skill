# Editorial UX Skill – Projektplan

> Design the work, not just the interface.

Projektarchitektur und Entwicklungsplan (Version 2, überarbeitet nach Plan-Review)

Projektziel: Entwicklung eines universellen, eigenständigen Open-Source-Skills zur Analyse, Konzeption, Gestaltung, Implementierung und Qualitätsverbesserung von redaktionellen und administrativen Benutzeroberflächen.

| | |
|---|---|
| Name des Skills | `editorial-ux-skill` (identisch mit dem Repository-Namen) |
| Repository | `editorial-ux-skill` |
| Befehlspräfix | `/editorial-ux-skill <befehl>` |
| Lizenzvorschlag | MIT |
| Primäre Entwicklungsumgebung | Claude Code |
| Weitere Zielumgebungen | Cursor, Codex, Gemini CLI, Antigravity und weitere Agenten mit Skill-Unterstützung |

## Änderungen gegenüber Version 1

Diese Version setzt die Rückmeldungen zum ersten Entwurf um:

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
editorial-ux-skill/
├── SKILL.md                  # Einstieg, Prinzipien, Befehlsübersicht, Ladehinweise
├── README.md                 # Schaufenster (kurz)
├── LICENSE
├── docs/
│   ├── project-plan.md       # dieses Dokument
│   ├── architecture.md
│   ├── methodology.md
│   ├── decisions.md
│   ├── development-roadmap.md
│   └── research/
│       ├── impeccable-analysis.md
│       └── agent-skills-compatibility.md
├── references/
│   ├── principles.md
│   ├── methodology.md        # Dimensionen, Skalen, Beobachtungsarten
│   └── anti-patterns.md
├── commands/
│   └── critique.md
├── templates/
│   └── ux-critique.md
└── evals/
    ├── rubric.md
    ├── scenarios/
    └── fixtures/
```

### 4.2 Zielstruktur (spätestens 1.0)

Die folgende Struktur ist ein **Architekturvorschlag und eine Obergrenze**, kein Pflichtumfang. Jedes Element muss sich durch Evaluationsergebnisse oder konkreten Bedarf rechtfertigen (Eintrag in `docs/decisions.md`). Ordnernamen sind durchgehend im Plural.

```
editorial-ux-skill/
├── SKILL.md
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
│
├── references/
│   ├── principles.md
│   ├── methodology.md
│   ├── system-intelligence.md
│   ├── editorial-experience.md
│   ├── interaction-design.md
│   ├── information-architecture.md
│   ├── cognitive-load.md
│   ├── visual-experience.md
│   ├── joy-of-use.md
│   ├── accessibility.md
│   ├── usability-evaluation.md
│   ├── quality-assurance.md
│   └── anti-patterns.md
│
├── platforms/
│   ├── general/
│   │   └── custom-backends.md        # Pflicht: generischer Adapter
│   ├── cms/
│   │   └── processwire.md            # erster spezifischer Adapter
│   └── community/                    # WordPress, Drupal, Headless, Laravel, Django ...
│
├── commands/
│   ├── discover.md
│   ├── critique.md
│   ├── audit.md
│   ├── improve.md
│   ├── walkthrough.md
│   ├── design.md
│   ├── implement.md
│   └── document.md
│
├── patterns/
│   ├── forms.md
│   ├── navigation.md
│   ├── tables.md
│   ├── content-editors.md
│   ├── media-management.md
│   ├── search-and-filter.md
│   ├── status-feedback.md
│   ├── workflows.md
│   └── bulk-actions.md
│
├── evals/
│   ├── rubric.md
│   ├── scenarios/
│   └── fixtures/
│
├── templates/
│   ├── system-profile.md
│   ├── editorial-profile.md
│   ├── ux-critique.md
│   ├── ux-audit.md
│   ├── design-brief.md
│   └── walkthrough-report.md
│
└── tests/
    ├── structural/
    └── behavior/
```

Änderungen gegenüber Version 1: `reference/` wird `references/`; Testfixtures und Bewertungsszenarien liegen nur noch unter `evals/`; der Befehl `test` heißt `walkthrough`; Adapter außer `custom-backends` und `processwire` wandern in `platforms/community/`.

### 4.3 Kontextmanagement

Zentrale Referenzen werden bei Bedarf geladen. Der Agent soll nicht bei jeder kleinen Aufgabe sämtliche Dokumente einlesen. Konkret:

- `SKILL.md` bleibt kurz und enthält nur Prinzipien, Befehlsübersicht und eine Ladetabelle („Für Befehl X lade Dateien Y und Z“).
- Jede Befehlsdatei nennt ihre benötigten Referenzen explizit.
- Jede Referenzdatei ist eigenständig lesbar (kein Zwang, andere Dateien mitzuladen).
- Das Kontextbudget wird in der Evaluation gemessen (Kap. 10), nicht nur geschätzt.

### 4.4 Modularisierung kritisch prüfen

Ob die Aufteilung wirklich sinnvoll ist, wird in Phase 1 geprüft und als Entscheidung in `docs/decisions.md` festgehalten. Zusammenlegen oder Streichen ist ausdrücklich erlaubt, wenn Dateien klein bleiben oder sich inhaltlich überschneiden.

---

## 5. Befehle und Arbeitsmethodik

Der Skill erhält eine einheitliche Befehlsschnittstelle. Die konkrete Umsetzung muss mit dem jeweiligen Agenten kompatibel sein.

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
- Möglichst hohe Kompatibilität mit dem Agent Skills Standard.
- Markdown-basierte Kernarchitektur.
- Keine obligatorischen Cloud-Dienste.
- Keine API-Schlüssel erforderlich.
- Keine obligatorische externe Laufzeit.
- Keine unnötigen Build-Abhängigkeiten.
- Keine vorgeschriebenen UI-Frameworks.
- Keine vorgeschriebenen Designsysteme.

### 9.2 Portabilität

Die zentrale Skill-Quelle bleibt agentenunabhängig. Bei Bedarf können daraus agentenspezifische Installationspakete erzeugt werden.

Die erste Version soll sich ohne Buildprozess direkt in Claude Code einsetzen lassen. Weitere Installationsformate folgen.

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

**Strukturtests** (`tests/structural/`) prüfen formale Eigenschaften des Skills, z. B. gültiges Frontmatter, vorhandene Dateien, aufgelöste Verweise, Größenlimits für `SKILL.md`. **Verhaltenstests** (`tests/behavior/`) prüfen das Verhalten von Agenten anhand der Szenarien aus `evals/`.

---

## 11. Open-Source-Strategie

Der Skill wird von Anfang an öffentlich entwickelbar konzipiert.

### Lizenz

Vorgeschlagen wird MIT. Die Lizenz soll eine möglichst unkomplizierte Nutzung, Anpassung und Weiterverbreitung ermöglichen.

Vor Veröffentlichung müssen sämtliche übernommenen Inhalte und Drittanbieterbestandteile auf ihre Lizenzbedingungen geprüft werden.

### Repository

Öffentliches GitHub-Repository: `editorial-ux-skill`. Der Skill-Name entspricht dem Repository-Namen.

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

1. `SKILL.md` mit Prinzipien und Ladehinweisen.
2. `references/principles.md`, `references/methodology.md`, `references/anti-patterns.md`.
3. `evals/rubric.md` mit verankerten Skalen.
4. Befehl `critique` samt Template.
5. Testprojekt D mit Fixture und Lösungsliste.
6. Erste Vergleichsmessung mit und ohne Skill.

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
- Die Kernfunktionen mit mindestens drei verschiedenen KI-Coding-Agenten getestet wurden.
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
