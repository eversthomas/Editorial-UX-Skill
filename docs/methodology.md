# Editorial UX Methodik (Entwurf)

Status: **Entwurf zur Freigabe.** Er konkretisiert `project-plan.md` Kap. 6 anhand der Primärquellen in `research/methodology-sources.md`. Jedes Element trägt eine Herkunftsmarke:

- **[Quelle]**: aus einer gelesenen Primärquelle abgeleitet (Kürzel siehe dort).
- **[Eigenentwurf]**: unsere Konstruktion, **unvalidiert**, wird in Phase 2 und 3 kalibriert und gemessen.

Diese Datei ist **Projektdokument** (deutsch). Die Skill-Fassung (`skills/editorial-ux-skill/references/methodology.md`, englisch, knapp) wird erst in Phase 2 daraus abgeleitet.

## 1. Ausgangspunkt

Editorial UX Skill ist eine **Inspektionsmethode** im Sinne der Usability-Forschung: Ein Agent prüft eine Oberfläche gegen etablierte Kriterien. Er testet nicht mit Nutzern [Quelle: NN-HE, NN-CW]. Daraus folgen drei Grundsätze:

1. **Befunde sind Hypothesen über Probleme**, keine empirischen Nutzerbefunde. Ein Heuristikverstoß ist nicht automatisch ein Problem; der Kontext entscheidet [Quelle: NN-HE].
2. **Eine einzelne Bewertung ist unzuverlässig.** Das gilt laut NN/g für Schweregrade einer einzelnen Person; Mehrfachbewertung stabilisiert [Quelle: NN-SEV, NN-HE]. Für einen Agenten heißt das: Wiederholte, unabhängige Durchläufe sind die Methode der Wahl, wo Verlässlichkeit zählt (Abschnitt 10).
3. **Der Umfang wird eng gewählt:** eine Aufgabe, ein Bereich, eine Nutzergruppe, ein Gerätetyp [Quelle: NN-HE]. Das entspricht unserer Grundregel „nicht jede Aufgabe braucht alle Schritte“.

## 2. Dimensionen A–J und ihre Verankerung

Die Dimensionen aus dem Projektplan werden Quellen zugeordnet. Alle zehn Heuristiken von Nielsen sind abgedeckt.

| Dim. | Name | Nielsen-Heuristik (NN-H) | Weitere Quellen |
|---|---|---|---|
| A | Orientierung | 1 Systemstatus (Position), 4 Konsistenz | WCAG 2.4.2, 2.4.5, 2.4.6, 3.2.3 |
| B | Aufgabenverständlichkeit | 2 System und reale Welt, 10 Hilfe | WCAG 3.3.2, 2.5.3 |
| C | Informationsarchitektur | 2, 4, 8 | WCAG 1.3.1; mentale Modelle (NN-CL) |
| D | Interaktionsqualität | 1 Systemstatus, 4, 7 | WCAG 4.1.3, 3.2.1, 3.2.2; NN-CX (Wartezeiten > 10 s) |
| E | Kognitive Belastung | 6 Wiedererkennen, 8 | NN-CL (intrinsisch/extraneous), NN-PD; WCAG 3.3.7 |
| F | Fehlertoleranz | 3 Nutzerkontrolle, 5 Fehlervermeidung, 9 Fehlerbehebung | NN-SL (Slips/Mistakes); WCAG 3.3.1, 3.3.3, 3.3.4 |
| G | Arbeitsfluss | 7 Flexibilität und Effizienz | NN-CW (Aufgabenschritte); WCAG 3.3.7 |
| H | Visuelle Qualität | 8, 4 | WCAG 1.4.3, 1.4.11 |
| I | Accessibility | (keine; eigener Standard) | WCAG 2.2, Zielstufe AA; ARIA APG |
| J | Joy of Use | 1, 3, 7, 8 (nur indirekt) | **keine Primärquelle** |

Die Prüffragen je Dimension stehen im Projektplan (6.1). Sie sind Leitfragen, keine vollständige Checkliste.

**Hinweis zu J:** Joy of Use ist eine **Eigenkonstruktion** [Eigenentwurf]. Die fünf Kriterien (Kontrollgefühl, Rückmeldungsqualität, Reibung, Konzentration, Souveränität) lassen sich auf Heuristiken zurückführen, aber nicht auf eine Quelle, die „Freude“ belegbar messbar macht. Deshalb: **J wird getrennt ausgewiesen und fließt in keinen Gesamtwert ein**, bis die Kalibrierung zeigt, dass die Bewertung stabil ist (D-011 ff.).

## 3. Evidenzstufen [Eigenentwurf, gestützt auf NN-HE]

Jeder Befund trägt genau eine Stufe:

| Stufe | Bedeutung | Beispiel |
|---|---|---|
| **Beobachtet** | Direkt im Code, in der Oberfläche oder durch ein Werkzeug belegt (mit Fundstelle) | „`<input>` ohne Label in `edit.php:42`“ |
| **Hypothese** | Begründet aus Beobachtungen abgeleitet, nicht geprüft | „Redakteure übersehen die Bildersetzen-Funktion“ |
| **Annahme** | Ungeprüfte Voraussetzung, vor allem über Nutzer und Kontext | „Die meisten Nutzer arbeiten am Desktop“ |

Regeln:

1. Scores und Schweregrade stützen sich nur auf **beobachtete** Befunde. Hypothesen und Annahmen werden separat aufgeführt.
2. Jeder Befund nennt den **Kontext** (Aufgabe, Nutzergruppe, Gerät), weil ein Verstoß nur dort ein Problem ist [Quelle: NN-HE].
3. Konnte eine geforderte Prüfung nicht laufen (kein Browser, kein Screenshot, kein Werkzeug), beginnt der Bericht mit `⚠️ Eingeschränkt: <Grund>` und betroffene Aussagen werden zu Hypothesen herabgestuft (D-009).
4. Fehlt die Grundlage für eine Dimension, lautet das Ergebnis **„nicht bewertbar“**, nicht eine geschätzte Zahl.

## 4. Befunde und Schweregrade

### Zwei Phasen [Quelle: NN-SEV, NN-HE]

1. **Befundphase:** Probleme finden, belegen, der Heuristik zuordnen; noch keine Schwere vergeben. Zwei Durchgänge: erst Orientierung im System oder in der Aufgabe, dann gezielte Suche.
2. **Bewertungsphase:** Schweregrade für die gesammelte Liste vergeben, nicht während der Suche.

### Schweregrad [Quelle: NN-SEV]

Skala 0 bis 4: 0 kein Problem; 1 kosmetisch; 2 geringfügig; 3 gravierend; 4 Katastrophe (vor Auslieferung beheben). Die Schwere ergibt sich aus **Häufigkeit**, **Auswirkung** und **Persistenz**.

Angepasst für Redaktionsarbeit [Eigenentwurf]:

- **Häufigkeit:** Wie oft betrifft es die Aufgabe im Redaktionsalltag (täglich/wöchentlich/selten)?
- **Auswirkung:** Verlust von Inhalten, falsche Veröffentlichung, Blockade oder bloße Verzögerung?
- **Persistenz:** Stört es dauerhaft oder nur beim ersten Mal?
- **Markteinfluss** (NN-SEV) entfällt für interne Oberflächen; stattdessen zählt der **Schaden bei Fehlbedienung** (z. B. versehentlich veröffentlichte Inhalte).

**Einzelurteil-Kennzeichnung:** Schweregrade aus einem einzelnen Durchlauf tragen den Hinweis „Einzelurteil“, weil einzelne Bewertungen laut NN/g unzuverlässig sind [Quelle: NN-SEV].

Dieser Entwurf **ersetzt** das P0 bis P3 aus früheren Überlegungen (D-019).

## 5. Scoring je Dimension [Eigenentwurf, zu kalibrieren]

Der Projektplan verlangt Scores von 0 bis 5 mit Ankern (6.2). Ziel der Anker ist Reproduzierbarkeit. Statt freier Schätzung wird der Score **aus den belegten Befunden** abgeleitet:

| Score | Bedingung (Deckelungsregel) |
|---|---|
| 0 | Mindestens ein **Schweregrad-4-Befund**, der eine typische Aufgabe der Dimension unmöglich macht |
| 1 | Mindestens ein Schweregrad-4-Befund |
| 2 | Mindestens ein Schweregrad-3-Befund |
| 3 | Mehrere Schweregrad-2-Befunde oder wiederkehrende Muster |
| 4 | Höchstens vereinzelte Schweregrad-1/2-Befunde |
| 5 | Keine relevanten Befunde **und** ausreichende Prüfabdeckung der Dimension |

Weitere Regeln:

- Der **niedrigste zutreffende Wert** gilt. Ein Schweregrad-4-Befund begrenzt den Score auf 1, egal wie viele gute Aspekte es sonst gibt.
- Ohne ausreichende Abdeckung ist 5 nicht vergebbar (höchstens 4) und bei fehlender Grundlage gilt „nicht bewertbar“.
- **Blocker:** Jede Dimension mit Score 0 oder 1 wird im Bericht gesondert hervorgehoben.
- **Kein verdeckender Gesamtwert:** Ergebnisse stehen immer je Dimension. Ein Gesamtwert ist optional und wird nie ohne die Dimensionsübersicht genannt (Plan 6.2). Bewusste Abweichung von Impeccable, dessen Gesamtsumme mit Bandbezeichnung (siehe `impeccable-analysis.md`) schwere Einzelmängel verdecken kann.
- **Offene Frage D-011:** 0–5 oder 0–4. Die Deckelungsregel funktioniert mit beiden; die Kalibrierung klärt, welche Breite stabiler ist.
- Die Bedingungen müssen in Phase 2 mit Kalibrierfällen geprüft werden: Passen sie zu menschlichen Urteilen auf denselben Fällen? Streuen sie über Läufe?

## 6. Accessibility (Dimension I) [Quelle: W-22; Einteilung Eigenentwurf]

- **Referenz:** WCAG 2.2, **Zielstufe AA** (alle Kriterien A und AA: 31 + 24 laut Dokument). AAA wird nicht als allgemeine Anforderung gesetzt, weil das Dokument selbst davon abrät, es für ganze Sites zu verlangen (5.2.1 Hinweis 2) [Quelle: W-22].
- **Geltungsbereich:** WCAG gilt für Webinhalte. Für native oder Desktop-Oberflächen ist es nur sinngemäß anwendbar; der Bericht sagt das.
- **Neu in 2.2 und für Redaktionsoberflächen relevant:** Fokus nicht verdeckt (2.4.11), Ziehen-Alternativen (2.5.7, z. B. Sortieren per Drag-and-drop), Zielgröße (2.5.8), konsistente Hilfe (3.2.6), keine doppelte Eingabe (3.3.7), barrierefreie Authentifizierung (3.3.8).
- **Prüfbarkeit** [Eigenentwurf]: Ein Agent kann nicht alles prüfen. Jedes Kriterium wird einer Klasse zugeordnet (Tabelle entsteht in Phase 2):
  1. **Aus Code oder Markup prüfbar** (z. B. fehlende Labels, Rollen, Überschriftenstruktur).
  2. **Nur mit gerenderter Oberfläche oder Werkzeug prüfbar** (z. B. Kontrastverhältnis, Zielgröße, Fokusverdeckung, Reflow).
  3. **Nur mit Hilfstechnik oder Menschen prüfbar** (z. B. Verständlichkeit für Screenreader-Nutzer).
- **Folge für die Berichtsform:** Ergebnisse tragen die Klasse. Klasse-1-Befunde sind „beobachtet“. Fehlt Werkzeug für Klasse 2, wird das als Einschränkung genannt, und nichts wird erfunden (Plan 9.3). Klasse 3 ergibt höchstens Hypothesen mit der Empfehlung eines echten Tests.
- **ARIA-Muster:** Für Widgets (Tabs, Dialoge, Menüs, Tabellen) dient der ARIA Authoring Practices Guide als Quelle [Quelle: W-APG]. Seine Muster sind noch auszuwerten.

## 7. Kognitive Belastung (Dimension E) [Quelle: NN-CL; Rest Eigenentwurf]

Grundlage:

- Kognitive Last ist der Bedarf an geistigen Ressourcen. **Intrinsische** Last ergibt sich aus der Aufgabe selbst und ist nicht eliminierbar; **extraneous** Last ist unnötig und zu minimieren [Quelle: NN-CL].
- Drei Prüfrichtungen [Quelle: NN-CL]: visuelles Rauschen, Anknüpfen an vorhandene mentale Modelle, Aufgaben abnehmen (Voreinstellungen, bereits Eingegebenes wieder anzeigen).
- Progressive Disclosure als Gegenmittel zu Überladung [Quelle: NN-PD], mit dem Spannungsfeld zwischen Leistungsfähigkeit und Einfachheit.

Nicht übernommen:

- **Feste Zahlenschwellen** („≤ 4 Optionen“) und **germane Load**: nicht aus Primärquellen belegt (`methodology-sources.md`, 4). Bis dahin gilt als Prüffrage „Wie viele Entscheidungen und Merkpunkte verlangt dieser Schritt?“ **ohne** feste Grenze. Bei der Aufgabenanalyse werden Entscheidungen und Merkpunkte **gezählt und berichtet**, nicht gegen eine Schwelle bewertet.

## 8. Aufgabenbasierte Prüfung: `walkthrough` [Quelle: NN-CW; Erweiterungen Eigenentwurf]

**Kern aus der Quelle:** Aufgabe in Schritte zerlegen. Je Schritt vier Fragen, aus Sicht einer festgelegten Persona:

1. Wird die Persona das richtige Ergebnis anstreben?
2. Bemerkt sie, dass die richtige Handlung verfügbar ist?
3. Ordnet sie die Handlung dem Ziel zu?
4. Sieht sie nach der Handlung Fortschritt?

Ein „Nein“ lässt den Schritt scheitern. Die Methode zielt auf **Erlernbarkeit für neue Nutzer** und eignet sich besonders für komplexe oder ungewohnte Abläufe [Quelle: NN-CW].

**Anpassung an Redaktionsarbeit [Eigenentwurf]:**

- Redakteure nutzen Systeme **täglich**; Erlernbarkeit ist nur ein Teil. Deshalb ergänzt jeder Schritt (nicht Teil der Originalmethode, im Bericht als Erweiterung gekennzeichnet): **Effizienz** (Anzahl der Handlungen und Wechsel), **Entscheidungslast** (Anzahl der Entscheidungen und Merkpunkte), **Fehlerrisiko** (Slip- und Mistake-Potenzial, NN-SL) und **Rückgängigmachbarkeit**.
- **Personas** kommen aus dem Editorial-Profil (`discover`). Fehlt es, werden sie als **Annahme** gekennzeichnet; keine erfundenen Nutzer.
- Der Agent ersetzt den **Workshop** (mehrere Rollen, Moderator, Protokollant). Das Ergebnis ist **ein** simulierter Durchgang und damit eine Hypothese. Der Bericht empfiehlt echte Tests mit Nutzern; die Quelle nennt für qualitative Tests als Regel 5 Teilnehmende [Quelle: NN-5].
- Für Standardmuster ist die Methode überdimensioniert [Quelle: NN-CW]. `walkthrough` konzentriert sich auf **abweichende, komplexe oder fehleranfällige Abläufe** (Veröffentlichen, Mehrfachbearbeitung, Freigaben).

## 9. Joy of Use (Dimension J) [Eigenentwurf]

Beobachtbare Merkmale (Plan 6.1 J), jeweils an Heuristiken rückgebunden:

| Merkmal | Rückbindung |
|---|---|
| Kontrollgefühl (Undo, erkennbarer Zustand) | NN-H 3, 1 |
| Rückmeldungsqualität | NN-H 1, 9 |
| Reibung (Umwege, Wiederholungen) | NN-H 7, 8 |
| Konzentration (Ablenkungsfreiheit) | NN-H 8; NN-CL |
| Souveränität (Beschleuniger, Voreinstellungen) | NN-H 7 |

Status: **keine Quelle für Messbarkeit.** Bis zur Kalibrierung wird J als eigene Spalte ausgewiesen, nicht verrechnet.

## 10. Reproduzierbarkeit [Quelle: NN-HE, NN-SEV; Messung Eigenentwurf]

NN/g empfiehlt 3 bis 5 **unabhängige** Evaluatoren, deren Ergebnisse erst danach zusammengeführt werden, und hält Schweregrade einzelner Personen für unzuverlässig [Quelle]. Für den Skill folgt:

- **Standardlauf:** Ein Durchlauf. Ergebnisse tragen „Einzelurteil“.
- **Vertiefter Lauf (Beta, D-013):** Mindestens drei unabhängige Durchläufe ohne Sicht auf die anderen, danach Zusammenführung (Befunde clustern, Schweregrad aus mehreren Urteilen). Ob Sub-Agenten, getrennte Sitzungen oder Wiederholungen des Nutzers die Isolation sicherstellen, hängt vom Agenten ab (Cursor: Sub-Agenten nicht verlässlich skill-gesteuert, siehe `cursor-compatibility.md`).
- **Metriken in der Evaluation** (Plan Kap. 10, 14): Trefferquote gegenüber der Lösungsliste, Falschbefundrate, Streuung der Dimensionsscores über Läufe, Übereinstimmung der drei wichtigsten Befunde, Kontext- und Zeitaufwand.
- **Kalibrierung:** Anker (Abschnitt 5) werden gegen Referenzfälle in `evals/rubric-calibration.md` geprüft. Passt der Skill nicht zu den Referenzurteilen, wird die Methode angepasst, nicht der Maßstab.

## 11. Berichtsaufbau

Jeder Bericht (`critique`) enthält, in dieser Reihenfolge:

1. Kopfzeile mit Umfang (Aufgabe, Nutzergruppe, Gerät) und ggf. `⚠️ Eingeschränkt`.
2. Dimensionsübersicht A–J: Score oder „nicht bewertbar“, Blocker markiert, J getrennt.
3. Befunde mit Evidenzstufe, Fundstelle, Heuristik/Kriterium, Kontext, Schweregrad (mit „Einzelurteil“-Hinweis).
4. Hypothesen und Annahmen getrennt.
5. Verbesserungsvorschläge priorisiert nach Schweregrad.
6. Empfehlung für echte Tests mit Nutzern, wo Hypothesen entscheidend sind.

## 12. Offene Punkte

| Punkt | Wie geklärt |
|---|---|
| Skalenbreite 0–5 oder 0–4 (D-011) | Kalibrierlauf in Phase 2 |
| Deckelungsregel (Abschnitt 5) | Vergleich mit Referenzurteilen und Streuung in Phase 2 |
| Joy of Use messbar? | Phase 3, Messung der Streuung; ggf. streichen oder als Perspektive führen |
| Germane Load, Arbeitsgedächtnis-Schwellen | Primärliteratur prüfen oder verzichten |
| WCAG-Prüfbarkeitstabelle | Phase 2, mit `references/accessibility.md` |
| ARIA-Muster | APG-Seiten auswerten |
| CMS- und Admin-Muster, Plattformwissen | Quellen je Plattform, braucht weitere Host-Freigaben; nicht Teil dieser Runde |
| Rechtlicher Rahmen (EN 301 549 u. a.) | Quellen lesen, falls im Skill relevant |
| Mehrfachläufe im Skill (D-013) | Phase 3, Messung mit und ohne Isolation |
