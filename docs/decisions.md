# Entscheidungen

Jede wesentliche Architekturentscheidung mit Begründung. Status:

- **Akzeptiert:** Aus dem Projektplan oder einer Nutzerentscheidung übernommen, oder durch Recherche belegt. Der Projektverantwortliche hat die Empfehlungen zu D-002 bis D-005, D-007 bis D-009 und D-015 ausdrücklich übernommen (2026-11-14).
- **Übernommen (Phase 1):** Von Claude vorgeschlagen und mit dem Abschluss von Phase 1 **vorläufig** übernommen, ohne dass jede Entscheidung einzeln bestätigt wurde. Die Prüfung erfolgt in Phase 2 (Praxistest, Kalibrierung). Der Projektverantwortliche kann jede dieser Entscheidungen jederzeit ändern.
- **Offen:** Noch nicht entscheidbar; benennt, was dafür fehlt.

**Maßgeblich ist die Tabelle.** Im Text der einzelnen Entscheidungen steht teils noch „Vorschlag“ als historische Formulierung.

Nummern bleiben stabil. Geänderte Entscheidungen werden ergänzt, nicht überschrieben.

| ID | Thema | Status |
|---|---|---|
| D-001 | Skill-Name entspricht dem Repository-Namen | Akzeptiert |
| D-002 | Repository und Skill-Ordner in Kleinschreibung | Akzeptiert (Umbenennung steht aus) |
| D-003 | Skill-Nutzlast in `skills/editorial-ux-skill/` | Akzeptiert |
| D-004 | Ein Skill, Befehle als Argumente, Anleitungen unter `references/` | Akzeptiert |
| D-005 | Nur Spec-Felder im Frontmatter der Quelle | Akzeptiert |
| D-006 | Lizenz MIT; kein Impeccable-Inhalt; Herkunft je Referenz | Akzeptiert |
| D-007 | Evals im Spec-Format plus Aktivierungs-Eval | Akzeptiert |
| D-008 | Größenbudgets im Strukturtest | Akzeptiert |
| D-009 | Evidenzkennzeichnung und Eingeschränkt-Hinweis in `SKILL.md` | Akzeptiert |
| D-010 | Keine Laufzeit und kein Detektor im Kern | Akzeptiert |
| D-011 | Skalenbreite 0–5 oder 0–4 | Offen |
| D-012 | Persistenz von Profilen im Nutzerprojekt | Offen |
| D-013 | Isolierte Sub-Agent-Bewertung | Offen (zurückgestellt) |
| D-014 | Sprache der Skill-Inhalte: Englisch | Akzeptiert |
| D-015 | Verweistiefe eins; Ladetabelle in `SKILL.md` | Akzeptiert |
| D-016 | Cursor als gleichrangige Zielumgebung; eine gemeinsame Installation | Übernommen (Phase 1) |
| D-017 | Keine Argument-Platzhalter; Befehl aus dem Anfragetext ableiten | Übernommen (Phase 1) |
| D-018 | Verteilung: Ordnerinstallation ab Alpha, Plugin/Marketplace ab Beta | Übernommen (Phase 1) |
| D-019 | Schweregrad nach Nielsen (0–4) statt P0–P3; zwei Phasen | Übernommen (Phase 1) |
| D-020 | Accessibility: WCAG 2.2 Stufe AA, Prüfbarkeitsklassen | Übernommen (Phase 1) |
| D-021 | Zitierweise: eigene Formulierung, Quelle und URL, kein Abdruck | Übernommen (Phase 1) |
| D-022 | Gestaltprinzipien als Wahrnehmungsprüfung (A, C, E, H; Walkthrough Frage 2 und 3) | Übernommen (Phase 1) |
| D-023 | Joy of Use als Dimension gestrichen | Akzeptiert |
| D-024 | Zwei Einsatzszenarien; alles visuell gestaltbar | Akzeptiert |
| D-025 | Erster spezifischer Adapter: WordPress (Meta-Boxen, Block-Editor); ProcessWire nachrangig | Akzeptiert |
| D-026 | WordPress-Adapter zunächst aus Modellwissen, als Annahme gekennzeichnet; Quellenrecherche zurückgestellt | Akzeptiert |
| D-027 | Phase 1 abgeschlossen; Übergabe offener Punkte | Akzeptiert |
| D-028 | Alpha-0.1-Umfang: `critique` und `design` (Konzeptstufe) | Übernommen (Phase 2) |

---

## D-001 – Skill-Name entspricht dem Repository-Namen

**Entscheidung:** Der Skill heißt `editorial-ux-skill`, Befehle folgen `/editorial-ux-skill <befehl>`.
**Begründung:** Vorgabe des Projektverantwortlichen; ein Name vermeidet Verwechslung zwischen Repository und Skill.
**Folge:** Die Spec verlangt Übereinstimmung mit dem Ordnernamen (D-002, D-003).

## D-002 – Repository und Skill-Ordner in Kleinschreibung

**Vorschlag:** Das GitHub-Repository von `Editorial-UX-Skill` zu `editorial-ux-skill` umbenennen.
**Begründung:** Die Spec (`docs/specification.mdx`) **und die offizielle Cursor-Doku** („Must match the parent folder name“) verlangen, dass `name` dem übergeordneten Verzeichnis entspricht (Claude Code nicht) und nur Kleinbuchstaben, Ziffern und Bindestriche enthält. Bei `git clone` in einen Skill-Ordner entstünde sonst ein Verzeichnis mit Großbuchstaben.
**Alternativen:** (a) Nichts umbenennen und nur D-003 umsetzen. Das reicht technisch, lässt aber installierte Klone fehlerhaft benannt. (b) Namen mit Großbuchstaben: von der Spec ausgeschlossen.
**Folge:** GitHub leitet alte URLs weiter; Umbenennung ist **Aktion des Repository-Inhabers**, nicht von Claude. Wegen D-003 ist sie für die Funktion **nicht blockierend**.

## D-003 – Skill-Nutzlast in `skills/editorial-ux-skill/`

**Vorschlag:** `SKILL.md` und alle vom Agenten geladenen Dateien liegen in `skills/editorial-ux-skill/`. `docs/`, `evals/`, `tests/` liegen daneben.
**Begründung:** Installation und Kontext sollen nur die Nutzlast enthalten (Spec, Progressive Disclosure). Der Ordnername ist unabhängig vom Repository-Namen kontrollierbar. Impeccable trennt ebenfalls `skill/` von Projektdateien.
**Gegenargument:** Ein verschachteltes Layout ist etwas weniger direkt als `SKILL.md` im Wurzelverzeichnis. Das Plan-Ziel „direkt in Claude Code einsetzbar ohne Buildprozess“ (Plan 9.2) bleibt erfüllt (Kopieren oder Verlinken des Ordners).
**Änderung am Plan:** Kap. 4 wird nach Freigabe angepasst.

## D-004 – Ein Skill, Befehle als Argumente, Anleitungen unter `references/`

**Vorschlag:** Ein Skill mit Befehlstabelle in `SKILL.md`. Befehlsanleitungen als `references/cmd-<name>.md`.
**Begründung:** Die Spec kennt keine Befehle. Ein Skill hält die Aktivierungskosten klein (Metadaten nur einmal). `commands/` ist nicht standardisiert und kollidiert begrifflich mit Claude Codes eigenen Slash-Befehlen. Impeccable wählt dasselbe Muster.
**Stand nach Prüfung der Claude-Code-Doku:** Argumente werden dem Skill übergeben (`$ARGUMENTS`, sonst automatisch als `ARGUMENTS: …` angehängt). Für Cursor ungeprüft, siehe D-017.

## D-005 – Nur Spec-Felder im Frontmatter der Quelle

**Vorschlag:** `name`, `description`, `license`, `compatibility` (falls nötig), `metadata`. Agentenspezifische Felder (`argument-hint`, `user-invocable`) nur in agentenspezifischen Paketen.
**Begründung:** Portabilität (Plan 9.1, 9.2); die Spec nennt nur die genannten Felder. Cursor listet nur `name`, `description`, `metadata` (u. a.), Claude Code ignoriert Unbekanntes, claude.ai-Upload bricht bei Zusatzfeldern ab. Offen: Cursors Umgang mit `license`/`compatibility`. Impeccable erzeugt agentenspezifische Varianten per Build, das übernehmen wir erst, wenn nötig.

## D-006 – Lizenz MIT; kein Impeccable-Inhalt; Herkunft je Referenz

**Entscheidung:** Eigene Inhalte unter MIT. Impeccable steht unter **Apache-2.0** (belegt in `LICENSE`); wir übernehmen weder Text noch Code noch Namen.
**Begründung:** Siehe `research/impeccable-analysis.md` Abschnitt 2.
**Regeln:** (1) Jede Referenzdatei nennt am Ende ihre fachlichen **Primärquellen** (z. B. NN/g, WCAG). (2) Keine Ableitung aus Impeccable-Dateien. (3) Beitragende bestätigen das in `CONTRIBUTING.md`. (4) Lizenzprüfung vor Release (Phase 7).

## D-007 – Evals im Spec-Format plus Aktivierungs-Eval

**Vorschlag:** `evals/evals.json` mit `prompt`, `expected_output`, `files`, `assertions`; Läufe mit/ohne Skill mit `timing.json`, `grading.json`, `benchmark.json`. Zusätzlich `evals/trigger-queries.json` (ca. 20 Anfragen, Beinahe-Treffer als Negativfälle).
**Begründung:** Spec-Best-Practices decken den geforderten Vergleich mit/ohne Skill (Plan Kap. 10) ab. Eine Aktivierungsprüfung fehlte im Plan; Impeccable zeigt, dass sie sich lohnt (Falsch-Positive und Recall sind messbar).
**Grenze:** Nicht jede Qualität lässt sich als Assertion prüfen (Spec: menschliche Durchsicht für Gestaltung).

## D-008 – Größenbudgets im Strukturtest

**Vorschlag:** `SKILL.md` < 500 Zeilen und < 5000 Token (Spec-Empfehlung). Jede Referenzdatei hat ein Byte-Limit in einer Budgetdatei. Zusätzlich Gesamtbudget je Befehl.
**Begründung:** Spec: zu umfangreiche Skills schaden. Impeccable erzwingt Budgets im Build und führt sie als „reviewte Entscheidung“.
**Offen:** konkrete Zahlen. Sie werden in Phase 2 anhand der ersten echten Dateien festgelegt, nicht vorab geraten.

## D-009 – Evidenzkennzeichnung und Eingeschränkt-Hinweis in `SKILL.md`

**Vorschlag:** Die Regeln „beobachtet / Hypothese / Annahme“ und die Kopfzeile `⚠️ Eingeschränkt: <Grund>` stehen in `SKILL.md`, nicht nur in einer Referenz.
**Begründung:** Passt zu Plan 6.2 und 9.3. Impeccable macht ein stilles Degradieren zu einem Fehlerfall; wir übernehmen den Grundgedanken (nicht den Wortlaut). Regeln in `SKILL.md` werden bei jeder Aktivierung gelesen (Spec-Hinweis zu „Gotchas“ in `SKILL.md`).

## D-010 – Keine Laufzeit und kein Detektor im Kern

**Entscheidung:** Der Kern ist reines Markdown. Ein deterministischer Regelprüfer wie bei Impeccable wird nicht mitgeliefert.
**Begründung:** Plan 9.1 („keine obligatorische externe Laufzeit“). Ein Prüfer wäre später ein optionales, getrennt versioniertes Werkzeug.

## D-011 – Skalenbreite 0–5 oder 0–4 (offen)

**Stand:** Plan: 0–5. Impeccable nutzt 0–4 für Heuristiken und Audit-Dimensionen.
**Abwägung:** Mehr Stufen erhöhen die Streuung bei LLM-Bewertungen (Plan 14, Reproduzierbarkeit). Weniger Stufen lassen sich leichter verankern.
**Entscheidung:** In Phase 2 anhand von Kalibrierläufen: beide Skalen auf demselben Fixture mehrfach laufen lassen und die Streuung vergleichen. Bis dahin bleibt 0–5 im Plan. **Neu:** Der Score soll nach `methodology.md` (5) per Deckelungsregel aus belegten Befunden und deren Schweregrad abgeleitet werden; NN/g hält Einzelbewertungen für unzuverlässig, das stützt Ableitung statt freier Schätzung.

## D-012 – Persistenz von Profilen im Nutzerprojekt (offen)

**Frage:** Sollen `discover`-Ergebnisse (Systemprofil, Editorial-Profil) als Dateien im Projekt des Nutzers liegen, damit spätere Befehle sie lesen (wie bei Impeccable `PRODUCT.md`/`DESIGN.md`)?
**Pro:** Befehle sind unabhängig und trotzdem informiert; Profile sind prüfbar und versionierbar. **Contra:** Schreibt Dateien in fremde Projekte; Pflege veralteter Profile.
**Entscheidung:** vertagt bis Phase 3 (`discover`). Bis dahin liefern Befehle Profile nur im Bericht.

## D-013 – Isolierte Sub-Agent-Bewertung (offen, zurückgestellt)

**Frage:** Soll `critique` Beobachtung und Bewertung isolieren, wie es Impeccable verbindlich tut (A ohne Sicht auf B)?
**Pro:** Verhindert Verankerung; stützt Reproduzierbarkeit. **Contra:** Setzt Sub-Agenten voraus, kostet Zeit und Token, nicht in allen Agenten verfügbar.
**Entscheidung:** In Phase 3 empirisch klären (gleiche Fixtures mit und ohne Isolation, Streuung messen). Alpha läuft im Einzelkontext, mit Eingeschränkt-Hinweis nach D-009 bei fehlenden Werkzeugen.
**Neu (Quelle):** NN/g empfiehlt 3 bis 5 **unabhängige** Evaluatoren und hält Schweregrade einzelner Personen für unzuverlässig (`research/methodology-sources.md`). Das spricht für einen vertieften Lauf mit mindestens drei unabhängigen Durchläufen. Cursor kann Sub-Agenten laut Zweitquelle nicht verlässlich aus Skills starten; Alternative: getrennte Läufe oder Wiederholung durch den Nutzer.

## D-014 – Sprache der Skill-Inhalte: Englisch

**Entscheidung:** Skill-Inhalte englisch, Projektdokumente deutsch, Ausgaben in der Sprache des Nutzers (Plan 9.5).
**Begründung:** Zielgruppe international; die Spec-Beispiele und -Hinweise zur `description` setzen auf Englisch.

## D-015 – Verweistiefe eins; Ladetabelle in `SKILL.md`

**Vorschlag:** Verweise nur von `SKILL.md` aus, eine Ebene tief; die Ladetabelle nennt je Befehl alle Dateien.
**Begründung:** Spec: „Keep file references one level deep … Avoid deeply nested reference chains.“
**Folge:** Der Plan (4.3: Befehlsdateien nennen ihre Referenzen selbst) wird entsprechend angepasst.

## D-016 – Cursor als gleichrangige Zielumgebung; eine gemeinsame Installation

**Vorschlag:** Claude Code und Cursor sind beide Zielumgebungen. Die Installation erfolgt in **einen** gemeinsamen Ordner `.claude/skills/editorial-ux-skill/` (alternativ `.agents/skills/`), ohne Build.
**Begründung:** Die offizielle Cursor-Doku nennt `.claude/skills/` und `.agents/skills/` ausdrücklich als gelesene Pfade (`research/cursor-compatibility.md`, 2.1, 4.1). Das passt zu Plan 9.2.
**Grenze:** Praxistest in Cursor steht aus. Keine Zweitkopie unter `.cursor/skills/` (Verhalten bei Namensdopplung nicht dokumentiert).

## D-017 – Keine Argument-Platzhalter; Befehl aus dem Anfragetext ableiten

**Vorschlag:** `SKILL.md` verwendet weder `$ARGUMENTS` noch andere Platzhalter. Der Agent leitet den Befehl aus dem Text der Anfrage ab (Befehlswort oder klar erkennbare Absicht).
**Begründung:** Platzhalter gibt es nur in Claude Code; ohne Platzhalter hängt Claude Code ohnehin `ARGUMENTS: …` an. Cursor dokumentiert keinen Argumentmechanismus (primär belegt). Befehle müssen zudem natürlichsprachlich funktionieren.
**Offen:** Ob Text hinter `/editorial-ux-skill` in Cursor mitgeschickt wird (Praxistest).

## D-018 – Verteilung: Ordnerinstallation ab Alpha, Plugin/Marketplace ab Beta

**Vorschlag:** Alpha wird durch Kopieren oder Verlinken des Ordners installiert. Plugin-Manifeste und Marketplace-Dateien kommen frühestens in Beta, getrennt von der Nutzlast. Öffentlicher Cursor-Marketplace und Anthropic-Verzeichnis sind optional nach 1.0.
**Begründung:** Cursor kennt keinen Direktimport einzelner Skills aus GitHub; dafür sind Plugin und `.cursor-plugin/marketplace.json` nötig, die Aufnahme in den öffentlichen Marketplace ist ein manueller Review. Claude Code hat eigenes Format (`.claude-plugin/marketplace.json`). Unser Layout `skills/<name>/SKILL.md` ist bereits plugin-kompatibel (`research/cursor-compatibility.md`, 4.8), der spätere Aufwand bleibt gering.
**Offen:** gemeinsames Manifest für beide Agenten, Befehlsname unter Claude-Code-Plugin-Namespace (`/plugin:skill`).

## D-019 – Schweregrad nach Nielsen (0–4) statt P0–P3; zwei Phasen

**Vorschlag:** Schweregrad 0 bis 4 (kein Problem, kosmetisch, geringfügig, gravierend, Katastrophe) aus Häufigkeit, Auswirkung und Persistenz, vergeben **nach** der Befundphase. Schweregrade aus einem Durchlauf tragen den Hinweis „Einzelurteil“.
**Begründung:** Primärquelle NN-SEV und NN-HE (`research/methodology-sources.md`, `methodology.md` 4). Impeccables P0–P3 ist nicht an einer Primärquelle verankert und bleibt kein Vorbild.
**Anpassung:** Markteinfluss entfällt für interne Oberflächen; stattdessen Schaden bei Fehlbedienung.

## D-020 – Accessibility: WCAG 2.2 Stufe AA, Prüfbarkeitsklassen

**Vorschlag:** Referenz ist WCAG 2.2, Zielstufe AA. Jedes Kriterium wird einer von drei Prüfbarkeitsklassen zugeordnet (aus Code, mit gerenderter Oberfläche oder Werkzeug, nur mit Hilfstechnik oder Menschen). Ergebnisse tragen die Klasse; ohne Werkzeug gibt es Einschränkung statt Schätzung.
**Begründung:** W3C-Dokument selbst rät davon ab, AAA allgemein zu verlangen (5.2.1). WCAG gilt für Webinhalte, nicht unmittelbar für native Oberflächen. Die Einteilung ist Eigenentwurf.

## D-021 – Zitierweise: eigene Formulierung, Quelle und URL, kein Abdruck

**Vorschlag:** Fachinhalte aus NN/g und W3C werden in eigenen Worten wiedergegeben, mit Autor, Titel, URL und Abrufdatum. Kein Abdruck von Seitentexten, Beispielen oder Postern. Das gilt für `docs/` und für Referenzdateien des Skills.
**Begründung:** NN/g erlaubt die Nutzung der Heuristiken mit Nennung von Jakob Nielsen und Adresse, Wiedergabe von Seiteninhalt verlangt weitere Erlaubnis. W3C verweist auf Dokumentnutzungsregeln. Ergänzt D-006.

## D-022 – Gestaltprinzipien als Wahrnehmungsprüfung

**Vorschlag:** Nähe, Ähnlichkeit, gemeinsame Region und visuelle Hierarchie werden als Prüfvokabular in den Dimensionen A, C, E und H sowie als Erweiterung des Walkthroughs (Frage 2 und 3) genutzt. Kennzeichnung im Bericht als Erweiterung (Eigenentwurf). Wahrnehmungsaussagen ohne Rendering sind Hypothesen.
**Begründung:** Primärquellen NN-GP, NN-GS, NN-CR, NN-VH (`research/methodology-sources.md`). Die Prinzipien erklären, warum Nutzer Elemente übersehen oder falsch zuordnen.
**Grenzen:** Praxisartikel, Originalliteratur nicht gelesen. Weitere klassische Prinzipien (Geschlossenheit, Kontinuität, Figur und Grund, Prägnanz) nicht belegt und nicht Teil des Skills. Nicht geeignet als Maß für Freude.

## D-023 – Joy of Use als Dimension gestrichen

**Entscheidung (Projektverantwortlicher, 2026-11-14): Dimension J wird gestrichen.** Gründe: (1) Keine Primärquelle macht Freude messbar; (2) die fünf Kriterien sind Eigenentwurf und bestehen aus Merkmalen, die ohnehin in D (Rückmeldung), E (Ruhe, Rauschen), F (Kontrolle, Rückgängigmachen) und G (Souveränität, Reibung) liegen; (3) NN/g warnt, dass Gefallen Probleme verdecken kann, eine Bewertung von „Freude“ würde das Risiko erhöhen; (4) ein Agent kann Empfinden nicht beobachten, J bliebe stets Hypothese und wäre im Gesamtwert ohnehin ausgeschlossen.
**Was bleibt:** Das Leitbild „Menschen arbeiten gerne damit“ bleibt als Produktziel, aber über **messbare Stellvertreter** (Kontrolle, Ruhe, Souveränität, geringe Reibung), nicht als eigene Note. Für echte Freude wäre ein Test mit Nutzern nötig; der Bericht darf dies als Empfehlung nennen.
**Umgesetzt in:** Plan (Kap. 1 Prinzip 3, 3.5, 4.2, 6.1, Phase 3), `methodology.md` (Abschnitte 2, 9, 11), README, Roadmap. Der Name der Referenzdatei `joy-of-use.md` entfällt. **Neun Dimensionen A–I.** Prinzip 3 heißt jetzt „Good Work is the Measure“.

## D-024 – Zwei Einsatzszenarien; alles visuell gestaltbar

**Entscheidung (Projektverantwortlicher, 2026-11-14):**
1. **Eingebettete Redaktionsoberflächen in einem Host-CMS.** Hauptfall WordPress: der Entwickler baut hoch spezialisierte Seiten und im Backend pflegbare individuelle Felder, vor allem **Meta-Boxen und Block-Editor**. Der Skill hilft, diese für Redakteure zu gestalten, und schreibt das Host-Backend nicht um.
2. **Vollständige Backends unabhängig von einem CMS.**
In beiden Fällen ist **alles visuell gestaltbar**: Entwurf und Umsetzung (Markup, Styles, Komponenten).
**Folgen:**
- Szenario 1: Host-Designsystem hat Vorrang, Erweiterung nur über offizielle Erweiterungspunkte (Plan 3.4, 9.4 Punkt 8). Die Methodik passt direkt: Gruppierung und Reihenfolge von Feldern (Nähe, gemeinsame Region), Progressive Disclosure für seltene Felder, Beschriftungen und Anweisungen (WCAG 3.3.2), Fehlerkennzeichnung (WCAG 3.3.1), Fachsprache statt Datenbanknamen (Heuristik 2).
- Szenario 2: eigene Rangfolge mit freigegebenen Tokens (Plan 3.4).
- `design` und `implement` erzeugen visuelle Ergebnisse, nicht nur Empfehlungen; die Leitplanken aus Plan 9.4 gelten.
- Fallstudien und Testprojekt A nutzen idealerweise ein echtes, anonymisiertes Beispiel aus der Praxis des Projektverantwortlichen.
**Offen:** Welche Feld-Werkzeuge (ACF, Meta Box, Carbon Fields) zusätzlich unterstützt werden; bisher genannt: Meta-Boxen und Block-Editor. Ob Redaktions-Fachsprache, Rollen und Berechtigungen als Teil des Editorial-Profils erhoben werden.

## D-025 – Erster spezifischer Adapter: WordPress (Meta-Boxen, Block-Editor); ProcessWire nachrangig

**Entscheidung (Projektverantwortlicher, 2026-11-14):** WordPress ersetzt ProcessWire als erster spezifischer Adapter, begrenzt auf Meta-Boxen und Block-Editor, **nicht** die gesamte Admin-Oberfläche. ProcessWire bleibt im Plan, aber nachrangig.
**Begründung:** Der Hauptfall des Projektverantwortlichen sind spezialisierte WordPress-Sites mit individuellen Feldern. Ein begrenzter Adapter ist wartbar und veraltet langsamer.
**Folge:** Quellen für den Adapter sind die offizielle WordPress-Entwicklerdokumentation zu Meta-Boxen und Block-Editor. Der Abruf ist noch nicht erfolgt (Hostfreigabe im Freigabedialog abgelehnt, Stand 2026-11-14).
**Ersetzt:** den Vorschlag in Plan Version 2 (zuerst ProcessWire als „gut bekannte Plattform“; das war eine Annahme).

## D-026 – WordPress-Adapter zunächst aus Modellwissen, als Annahme gekennzeichnet

**Entscheidung (Projektverantwortlicher, 2026-11-14):** Die Quellenrecherche zu WordPress (Meta-Boxen, Block-Editor) wird zurückgestellt. Der Projektverantwortliche vermutet, dass das allgemeine Wissen des Modells über WordPress für den Anfang genügt, und testet das praktisch mit einem hypothetischen Backend auf seinem Rechner.
**Folgen:**
- Aussagen zu WordPress, die im Skill oder in Referenzen stehen und nicht aus der offiziellen Doku belegt sind, tragen die Evidenzstufe **Annahme** und den Hinweis „aus Modellwissen, nicht gegen die aktuelle Doku geprüft“.
- Bei konkreter Implementierung gilt weiter Plan Kap. 7 und 9.4 Punkt 5: Plattformdokumentation ist veränderlich, der Agent prüft die aktuelle offizielle Dokumentation, soweit verfügbar, statt veraltete API-Annahmen zu übernehmen.
- Nach dem Praxistest entscheidet sich, ob eine gezielte Quellenprüfung nötig ist (Hostfreigabe für `developer.wordpress.org` liegt dann neu vor).
- **Risiko:** WordPress-APIs und Block-Editor-Komponenten ändern sich schnell; Modellwissen kann veraltet sein. Der Praxistest soll das sichtbar machen, nicht verdecken.

## D-027 – Phase 1 abgeschlossen; Übergabe offener Punkte

**Entscheidung (Projektverantwortlicher, 2026-11-14):** Phase 1 wird abgeschlossen. Offene Punkte stehen in `development-roadmap.md` (Abschnitt „Mit Phase 1 mitgenommene offene Punkte“).
**Hinweis:** Vor dem Praxistest mit einem WordPress-Backend muss ein lauffähiger Skill existieren (Phase 2, Schritt 4 und 5).

## D-028 – Alpha-0.1-Umfang: `critique` und `design` (Konzeptstufe)

**Stand (2026-11-14):** Der testbare Skill enthält `critique` und `design` als Konzeptstufe (Brief und Wireframe, kein Code) sowie `references/wordpress.md` als Annahmen aus Modellwissen (D-026). Damit weicht Alpha 0.1 vom ursprünglichen Plan (nur `critique`) ab: `design` kam hinzu, weil der Hauptanwendungsfall (Felder für Redakteure gestalten) sonst nicht testbar wäre.
**Prüfung:** Strukturtest und ein informeller Rauchtest (`evals/results/2026-11-14-smoke-critique.md`, 16 von 17 eingebauten Problemen gefunden, ohne Messung und ohne Baseline). Die Wirksamkeit gegenüber ohne Skill ist **nicht belegt**; das ist der Entscheidungspunkt am Ende von Phase 2.
**Änderungen aus dem Rauchtest:** Zusammenfassung am Berichtsanfang, eine Evidenzstufe je Befund, klarere Abgrenzung der Scores 0 und 1, „nicht bewertbar“ für A und H bei Einzelkomponenten, Abschnitt für Beobachtungen außerhalb des UX-Umfangs.
