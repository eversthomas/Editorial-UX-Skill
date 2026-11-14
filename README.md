# Editorial-UX-Skill
Design the work, not just the interface.

Editorial UX

Projektarchitektur und Entwicklungsplan

Projektziel: Entwicklung eines universellen, eigenständigen Open-Source-Skills zur Analyse, Konzeption, Gestaltung, Implementierung und Qualitätsverbesserung von redaktionellen und administrativen Benutzeroberflächen.

Arbeitstitel: Editorial UX
Repository: "editorial-ux-skill"
Lizenzvorschlag: MIT
Primäre Entwicklungsumgebung: Claude Code
Weitere Zielumgebungen: Cursor, Codex, Gemini CLI, Antigravity und weitere Agenten mit Skill-Unterstützung.

---

1. Produktvision

Editorial UX befähigt KI-Coding-Agenten dazu, administrative Benutzeroberflächen und redaktionelle Arbeitsumgebungen so zu entwickeln und zu verbessern, dass Menschen gerne, effizient und intuitiv mit ihnen arbeiten.

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

Editorial UX ist nicht auf ein bestimmtes CMS, Framework oder Backend-System beschränkt.

Es soll gleichermaßen für WordPress, ProcessWire, Drupal, Headless CMS, individuell entwickelte CMS, interne Verwaltungsanwendungen, Dashboards und andere administrative Werkzeuge funktionieren.

Leitgedanke

Ein Backend ist nicht nur eine technische Verwaltungsoberfläche. Es ist ein Arbeitsplatz.

Seine Qualität bemisst sich nicht allein an der technischen Funktionalität oder der visuellen Gestaltung, sondern daran, wie gut es Menschen bei ihrer tatsächlichen Arbeit unterstützt.

Drei zentrale Prinzipien

1. Understand the System

Zuerst das vorhandene System, seine Architektur, seine Möglichkeiten und Einschränkungen verstehen. Keine vorschnellen Designentscheidungen.

2. Design for the User

Die Arbeitsrealität, mentalen Modelle, Fähigkeiten und Bedürfnisse der tatsächlichen Benutzer bestimmen die Gestaltung.

3. Joy is a Quality Criterion

Effizienz, Verständlichkeit, Barrierefreiheit und Freude an der Benutzung sind gleichwertige Qualitätsdimensionen.

---

2. Abgrenzung und Geltungsbereich

Editorial UX konzentriert sich auf die Benutzererfahrung innerhalb administrativer und redaktioneller Systeme.

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

3. Grundarchitektur

Editorial UX wird als modularer Skill entwickelt.

Die Architektur besteht aus fünf fachlichen Säulen.

3.1 System Intelligence

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

3.2 Editorial Experience

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

3.3 Interaction Design

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

3.4 Visual Experience

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

Die Gestaltung soll sich an der jeweiligen Anwendung orientieren. Editorial UX soll keine universelle Designästhetik erzwingen.

3.5 Quality Engineering

Die abschließende Säule prüft die Qualität.

Schwerpunkte:

- Usability
- Accessibility
- Interaktionskonsistenz
- technische Robustheit
- Fehlertoleranz
- Performance
- Responsive Verhalten
- Verständlichkeit
- Aufgaben-Effizienz
- Joy of Use

---

4. Modulare Repository-Struktur

Vorgeschlagene Struktur:

editorial-ux/
│
├── SKILL.md
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
│
├── reference/
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
│   ├── usability-testing.md
│   ├── quality-assurance.md
│   └── anti-patterns.md
│
├── platforms/
│   ├── cms/
│   │   ├── wordpress.md
│   │   ├── processwire.md
│   │   ├── drupal.md
│   │   └── headless-cms.md
│   │
│   ├── frameworks/
│   │   ├── laravel.md
│   │   ├── django.md
│   │   ├── rails.md
│   │   └── custom-php.md
│   │
│   └── general/
│       ├── custom-backends.md
│       └── internal-tools.md
│
├── commands/
│   ├── discover.md
│   ├── analyze.md
│   ├── shape.md
│   ├── design.md
│   ├── implement.md
│   ├── critique.md
│   ├── audit.md
│   ├── improve.md
│   ├── test.md
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
├── evaluations/
│   ├── rubric.md
│   ├── scenarios/
│   └── fixtures/
│
├── templates/
│   ├── system-profile.md
│   ├── editorial-profile.md
│   ├── ux-audit.md
│   ├── design-brief.md
│   └── test-report.md
│
└── tests/
    ├── structural/
    ├── fixtures/
    └── behavior/

Die Struktur ist ein Architekturvorschlag und wird während der Entwicklung überprüft.

Wichtig: Die zentralen Referenzen werden bei Bedarf geladen. Der Agent soll nicht bei jeder kleinen Aufgabe sämtliche Dokumente einlesen müssen.

---

5. Skill-Befehle und Arbeitsmethodik

Editorial UX erhält eine einheitliche Befehlsschnittstelle.

Die konkrete Implementierung muss mit den jeweiligen Agenten kompatibel sein.

Befehl| Funktion
"/editorial-ux discover"| System und Umgebung untersuchen
"/editorial-ux analyze"| Bestehende UX analysieren
"/editorial-ux shape"| Lösung konzipieren
"/editorial-ux design"| UI und Interaktionen gestalten
"/editorial-ux implement"| Gestaltung umsetzen
"/editorial-ux critique"| Kritische UX-Bewertung
"/editorial-ux audit"| Umfassende Qualitätsprüfung
"/editorial-ux improve"| Bestehende Oberfläche verbessern
"/editorial-ux test"| Bedienbarkeit anhand konkreter Aufgaben prüfen
"/editorial-ux document"| Ergebnisse und Designentscheidungen dokumentieren

Standardworkflow

Der vollständige Entwicklungsprozess:

1. Discover
2. Analyze
3. Shape
4. Design
5. Implement
6. Critique
7. Test
8. Improve
9. Document

Die Befehle müssen auch unabhängig voneinander funktionieren.

Ein Benutzer soll beispielsweise eine bestehende Oberfläche direkt mit "critique" untersuchen können, ohne vorher einen vollständigen Entwicklungsprozess durchlaufen zu müssen.

Grundregel

Nicht jede Aufgabe benötigt alle Schritte.

Der Agent wählt den angemessenen Umfang anhand der konkreten Aufgabe. Eine kleine Formularverbesserung darf nicht unnötig zu einer vollständigen Systemanalyse führen.

---

6. Die redaktionelle UX-Methodik

Dies ist der wichtigste eigenständige Teil des Projekts.

Editorial UX benötigt eine eigene Bewertungsmethodik.

6.1 Editorial UX Evaluation

Folgende Dimensionen werden bewertet:

A. Orientierung

- Ist die aktuelle Position innerhalb des Systems erkennbar?
- Ist die Navigation verständlich?
- Sind Zusammenhänge sichtbar?

B. Aufgabenverständlichkeit

- Ist klar, was zu tun ist?
- Sind Aktionen eindeutig benannt?
- Ist das Ergebnis einer Aktion vorhersehbar?

C. Informationsarchitektur

- Entspricht die Struktur dem mentalen Modell der Benutzer?
- Sind Informationen sinnvoll gruppiert?
- Ist die Informationsdichte angemessen?

D. Interaktionsqualität

- Sind Eingaben intuitiv?
- Sind Zustände verständlich?
- Gibt es unmittelbares Feedback?

E. Kognitive Belastung

- Wie viele Entscheidungen muss der Benutzer treffen?
- Werden Informationen zum richtigen Zeitpunkt angezeigt?
- Gibt es unnötige Gedächtnisbelastung?

F. Fehlertoleranz

- Sind Fehler vermeidbar?
- Lassen sich Änderungen korrigieren?
- Sind Fehlermeldungen hilfreich?

G. Arbeitsfluss

- Wie viele Schritte sind für typische Aufgaben erforderlich?
- Gibt es unnötige Unterbrechungen?
- Werden wiederkehrende Aufgaben unterstützt?

H. Visuelle Qualität

- Ist die Oberfläche ruhig und konsistent?
- Sind Hierarchien verständlich?
- Ist die Informationsdichte ausgewogen?

I. Accessibility

- Ist die Oberfläche per Tastatur bedienbar?
- Sind Kontraste und Fokuszustände ausreichend?
- Werden semantische Strukturen und assistive Technologien berücksichtigt?

J. Joy of Use

- Fühlt sich die Bedienung angenehm an?
- Vermittelt die Oberfläche Sicherheit und Kontrolle?
- Unterstützt sie konzentriertes Arbeiten?
- Gibt es unnötige Reibung?

6.2 Bewertungssystem

Jede Dimension erhält:

- einen Score von 0 bis 5
- eine Begründung
- konkrete Beobachtungen
- Verbesserungsvorschläge
- eine Priorität

Die Bewertung muss zwischen tatsächlich beobachteten Problemen, begründeten Hypothesen und noch ungeprüften Annahmen unterscheiden.

Ein Gesamtwert darf nicht verdecken, dass beispielsweise eine schwerwiegende Accessibility-Schwäche besteht.

6.3 Aufgabenbasierte Prüfung

Die eigentliche Stärke soll die aufgabenbasierte Bewertung sein.

Beispiele:

- Einen neuen Inhalt erstellen.
- Einen bestehenden Inhalt bearbeiten.
- Ein Bild austauschen.
- Eine Veröffentlichung vorbereiten.
- Einen Fehler korrigieren.
- Mehrere Einträge gleichzeitig bearbeiten.
- Einen bestimmten Datensatz finden.

Der Agent untersucht, wie gut die Oberfläche diese Aufgaben unterstützt.

Er bewertet nicht nur die Anzahl der Klicks, sondern auch Orientierung, Entscheidungslast, Fehlerrisiko und Verständlichkeit.

---

7. Plattformadapter

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

Die Adapter sind optional.

Unbekannte Systeme müssen ebenfalls analysierbar sein. Dafür gibt es den generischen Adapter "custom-backends.md".

Wichtig: Plattformdokumentationen müssen als veränderliche Referenzen behandelt werden. Der Agent soll bei konkreten Implementierungen die jeweils aktuelle offizielle Dokumentation prüfen, anstatt veraltete API-Annahmen zu übernehmen.

---

8. Design- und Interaktionsmuster

Editorial UX erhält eine eigene Pattern-Bibliothek.

Diese soll nicht ausschließlich aus visuellen Beispielen bestehen, sondern erklären:

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

9. Technische Anforderungen

9.1 Grundprinzipien

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

9.2 Portabilität

Die zentrale Skill-Quelle bleibt agentenunabhängig.

Bei Bedarf können daraus agentenspezifische Installationspakete erzeugt werden.

Die erste Version soll sich ohne Buildprozess direkt in Claude Code einsetzen lassen.

Weitere Installationsformate folgen.

9.3 Keine unnötigen Automatisierungen

Der Skill soll zunächst auf der vorhandenen Fähigkeit des KI-Coding-Agenten aufbauen.

Browserautomatisierung, Screenshot-Analyse und automatisierte Accessibility-Tests werden unterstützt, sofern die jeweilige Umgebung entsprechende Werkzeuge bereitstellt.

Fehlende Werkzeuge dürfen nicht durch erfundene Testergebnisse ersetzt werden.

---

10. Qualitätssicherung und Evaluation

Editorial UX darf sich nicht allein durch gute Formulierungen definieren.

Es muss nachweisbar sein, dass der Skill bessere Ergebnisse hervorbringt.

Dafür werden Testprojekte angelegt.

Testprojekt A: Klassisches CMS

Eine typische redaktionelle Oberfläche mit:

- Seitenverwaltung
- Formularen
- Medienverwaltung
- Navigation
- Veröffentlichungsstatus

Testprojekt B: Individuelles PHP-Backend

Ein eigens entwickeltes Backend mit:

- Datensätzen
- Such- und Filterfunktionen
- Formularen
- Benutzerverwaltung
- Verwaltungsprozessen

Testprojekt C: Komplexe Verwaltungsoberfläche

Eine Anwendung mit:

- unterschiedlichen Rollen
- komplexen Arbeitsabläufen
- Statusübergängen
- Freigaben
- umfangreichen Tabellen

Testprojekt D: Bestehende schlechte Oberfläche

Ein absichtlich ungünstig gestaltetes Backend.

Der Agent muss die Probleme erkennen, priorisieren und konkrete Verbesserungen durchführen.

Testverfahren

Jede Testumgebung wird mit definierten Aufgaben und erwarteten Ergebnissen versehen.

Bewertet werden:

- Erkennung vorhandener UX-Probleme
- Qualität der Analyse
- Angemessenheit der Konzeption
- Qualität der Implementierung
- Einhaltung technischer Rahmenbedingungen
- Verbesserung der Aufgabenbedienbarkeit
- Accessibility
- visuelle Konsistenz

Zusätzlich werden statische Prüfungen und, soweit verfügbar, Browser- und Interaktionstests durchgeführt.

Es sollen sowohl die Ergebnisse als auch die tatsächlichen Arbeitsschritte des Agenten bewertet werden.

---

11. Open-Source-Strategie

Editorial UX wird von Anfang an öffentlich entwickelbar konzipiert.

Lizenz

Vorgeschlagen wird MIT.

Die Lizenz soll eine möglichst unkomplizierte Nutzung, Anpassung und Weiterverbreitung ermöglichen.

Vor Veröffentlichung müssen sämtliche übernommenen Inhalte und Drittanbieterbestandteile auf ihre Lizenzbedingungen geprüft werden.

Repository

Öffentliches GitHub-Repository:

"editorial-ux"

Dokumentation

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

Contribution

Externe Entwickler sollen insbesondere beitragen können zu:

- weiteren CMS-Adaptern
- zusätzlichen Interaktionsmustern
- neuen Testfällen
- Verbesserungen der Bewertungsmethodik
- Accessibility-Regeln
- Übersetzungen
- Agent-Kompatibilität

Fachliche Qualität soll Vorrang vor der bloßen Anzahl von Beiträgen haben.

---

12. Entwicklungsphasen

Phase 1 – Grundlagen und Recherche

Ziel: Eine belastbare fachliche Grundlage schaffen.

Aufgaben:

1. Impeccable vollständig untersuchen.
2. Architektur und Arbeitsmethodik dokumentieren.
3. Relevante Design- und UX-Prinzipien extrahieren.
4. Nielsen-Heuristiken und Cognitive-Load-Methoden einordnen.
5. Editorial UX von allgemeinem UI-Design abgrenzen.
6. Bestehende CMS- und Admin-UX-Patterns untersuchen.
7. Bewertungsmethodik entwickeln.

Ergebnis: Fachliches Fundament und Architekturentscheidung.

Wichtig: Impeccable ist eine Referenz, keine technische Abhängigkeit und keine Quelle für ungeprüftes Kopieren.

Phase 2 – Skill-Grundgerüst

Ziel: Eine funktionsfähige erste Skill-Version erstellen.

Aufgaben:

1. Repository anlegen.
2. SKILL.md erstellen.
3. Grundprinzipien definieren.
4. Referenzstruktur implementieren.
5. Befehle definieren.
6. Kontextmanagement entwickeln.
7. Templates erstellen.

Ergebnis: Editorial UX Alpha 0.1.

Phase 3 – Editorial UX Engine

Ziel: Die eigenständige fachliche Kompetenz entwickeln.

Aufgaben:

1. Editorial UX Evaluation implementieren.
2. Aufgabenbasierte Analyse entwickeln.
3. Cognitive-Load-Bewertung ausarbeiten.
4. Joy-of-Use-Kriterien definieren.
5. Interaction-Patterns erstellen.
6. Usability-Testmethodik integrieren.
7. Priorisierungssystem entwickeln.

Ergebnis: Editorial UX Alpha 0.2.

Phase 4 – Plattformintelligenz

Ziel: Das universelle Systemverständnis realisieren.

Aufgaben:

1. Generischen Backend-Adapter entwickeln.
2. ProcessWire-Adapter erstellen.
3. WordPress-Adapter erstellen.
4. Headless-CMS-Adapter erstellen.
5. Technische Analyseverfahren testen.
6. Plattformübergreifende Arbeitsweise prüfen.

Ergebnis: Editorial UX Alpha 0.3.

Phase 5 – Implementierung und Design

Ziel: Vollständige Entwicklungsunterstützung.

Aufgaben:

1. Designmethodik ausarbeiten.
2. Implementierungsworkflow entwickeln.
3. Designsystem-Dokumentation integrieren.
4. Visuelle Qualitätsprüfung entwickeln.
5. Accessibility-Prüfung integrieren.
6. Browsergestützte Tests ermöglichen.

Ergebnis: Editorial UX Beta 0.5.

Phase 6 – Evaluation

Ziel: Die tatsächliche Qualität nachweisen.

Aufgaben:

1. Vier Testumgebungen aufbauen.
2. Definierte Redaktionsaufgaben durchführen.
3. Analyseergebnisse vergleichen.
4. Implementierungsergebnisse bewerten.
5. Schwächen der Skill-Anweisungen identifizieren.
6. Verhaltenstests über mehrere Agenten durchführen.
7. Methodik überarbeiten.

Ergebnis: Editorial UX Beta 0.8.

Phase 7 – Open-Source-Release

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

Ergebnis: Editorial UX 1.0.

---

13. Priorisierung

Nicht alle Funktionen müssen von Beginn an umgesetzt werden.

Die erste Version soll sich auf folgende Kernkompetenzen konzentrieren:

Priorität 1 – Unverzichtbar

- Systemanalyse
- Redaktionelle UX-Analyse
- Aufgabenorientierte Konzeption
- Interaktionsdesign
- Visuelle Gestaltung
- Kritische UX-Bewertung
- Qualitätsprüfung

Priorität 2 – Für die Beta

- Plattformadapter
- Pattern-Bibliothek
- Aufgabenbasierte Tests
- Accessibility-Automatisierung
- Mehrere Agentenformate

Priorität 3 – Spätere Erweiterungen

- Umfangreiche CMS-spezifische Wissensmodule
- Visuelle Testwerkzeuge
- Erweiterte Pattern-Kataloge
- Community-Beiträge
- Zusätzliche Evaluationsverfahren

---

14. Definition of Done für Version 1.0

Editorial UX 1.0 gilt als fertig, wenn:

- Der Skill unabhängig von Impeccable funktioniert.
- Die Kernmethodik dokumentiert ist.
- Ein unbekanntes Backend systematisch analysiert werden kann.
- Bestehende CMS-Strukturen berücksichtigt werden.
- Redaktionelle Arbeitsabläufe untersucht werden können.
- UX-Konzepte erstellt werden können.
- UI-Implementierungen unterstützt werden.
- Visuelle und funktionale Qualitätsprüfungen möglich sind.
- Die Bewertungsmethodik reproduzierbar angewendet werden kann.
- Mindestens drei unterschiedliche technische Umgebungen erfolgreich getestet wurden.
- Die Kernfunktionen mit mehreren KI-Coding-Agenten getestet wurden.
- Dokumentation und Installation für externe Benutzer verständlich sind.
- Lizenz und Drittanbieterbestandteile geprüft wurden.

---

15. Arbeitsauftrag für Claude Code

Claude Code soll das Projekt nicht unmittelbar vollständig implementieren.

Zunächst ist eine eigenständige Recherche- und Konzeptionsphase durchzuführen.

Arbeitsmodus

- Eigenständig recherchieren.
- Offizielle Dokumentationen bevorzugen.
- Aktuelle Repository-Strukturen untersuchen.
- Fachliche Behauptungen anhand von Quellen prüfen.
- Technische Annahmen kennzeichnen.
- Keine ungeprüften Implementierungsentscheidungen treffen.
- Keine unnötigen Abhängigkeiten einführen.
- Keine vorzeitige Programmierung.

Erste konkrete Aufgaben

1. Das originale Impeccable-Repository untersuchen.
2. Die vollständige Skill-Architektur erfassen.
3. Die Befehlsstruktur und Referenzdateien analysieren.
4. Die Testarchitektur untersuchen.
5. Die Agent Skills Specification recherchieren.
6. Die Übertragbarkeit auf Editorial UX bewerten.
7. Die vorgeschlagene Architektur kritisch prüfen.
8. Notwendige Anpassungen dokumentieren.
9. Eine konkrete Implementierungsreihenfolge vorschlagen.
10. Erst nach Abschluss dieser Arbeit die Umsetzung vorbereiten.

Erwartete Rechercheergebnisse

Im Repository sollen folgende Dokumente entstehen:

- "docs/research/impeccable-analysis.md"
- "docs/research/agent-skills-compatibility.md"
- "docs/architecture.md"
- "docs/methodology.md"
- "docs/development-roadmap.md"
- "docs/decisions.md"

Jede wesentliche Architekturentscheidung wird mit Begründung dokumentiert.

Claude Code soll insbesondere prüfen, ob die vorgeschlagene Modularisierung tatsächlich sinnvoll ist oder unnötige Komplexität erzeugt.

---

16. Abschließende Produktentscheidung

Editorial UX wird als eigenständiges Open-Source-Projekt entwickelt.

Es übernimmt keine technische Abhängigkeit von Impeccable.

Es verwendet dessen erfolgreiche methodische Ansätze als Orientierung und entwickelt daraus eine eigene Fachdisziplin für redaktionelle und administrative Benutzererfahrungen.

Das Projekt soll nicht einfach bessere Admin-Oberflächen erzeugen.

Es soll KI-Coding-Agenten dazu befähigen, Arbeitsumgebungen zu schaffen, in denen Menschen ihre Aufgaben gerne erledigen.

Editorial UX – Design the work, not just the interface.
