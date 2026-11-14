# Methodik: Primärquellen

Recherche zu Phase 1 (Projektplan Kap. 12, Aufgaben 4, 5, 9). Diese Datei hält fest, **was die Quellen tatsächlich aussagen** und **was nicht**. `methodology.md` baut darauf auf. Aussagen aus Quellen sind in eigenen Worten wiedergegeben, nicht kopiert (Urheberrecht, siehe 3).

## 1. Gelesene Quellen (Abruf 2026-11-14)

| Kürzel | Quelle | Gelesen |
|---|---|---|
| NN-H | Nielsen: „10 Usability Heuristics for User Interface Design“, 1994, zuletzt geprüft 2024-01-30. https://www.nngroup.com/articles/ten-usability-heuristics/ | vollständig |
| NN-HE | Moran, Gordon: „How to Conduct a Heuristic Evaluation“, 2023. https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/ | vollständig |
| NN-SEV | Nielsen: „Severity Ratings for Usability Problems“, 1994. https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/ | vollständig |
| NN-CW | Flaherty: „Evaluate Interface Learnability with Cognitive Walkthroughs“, 2022. https://www.nngroup.com/articles/cognitive-walkthroughs/ | vollständig |
| NN-CL | Whitenton: „Minimize Cognitive Load to Maximize Usability“, 2013. https://www.nngroup.com/articles/minimize-cognitive-load/ | vollständig |
| NN-CX | Kaplan: „10 Usability Heuristics Applied to Complex Applications“, 2021. https://www.nngroup.com/articles/usability-heuristics-complex-applications/ | Heuristiken 1 bis 6 gelesen, Rest überflogen |
| NN-SL | Laubheimer: „Slips“ (Error Prevention), 2015. https://www.nngroup.com/articles/slips/ | Einleitung und Fehlertypen |
| NN-PD | Nielsen: „Progressive Disclosure“, 2006. https://www.nngroup.com/articles/progressive-disclosure/ | Einleitung |
| NN-5 | Nielsen: „How Many Test Users in a Usability Study?“, 2012. https://www.nngroup.com/articles/how-many-test-users/ | Zusammenfassung |
| W-22 | W3C: „Web Content Accessibility Guidelines (WCAG) 2.2“, W3C Recommendation 2024-12-12. https://www.w3.org/TR/WCAG22/ | Erfolgskriterien-Liste, Stufen, ausgewählte Kriterien im Wortlaut, Konformität 5.2.1 |
| W-APG | W3C: „ARIA Authoring Practices Guide“. https://www.w3.org/WAI/ARIA/apg/ | nur Startseite (Zweck) |

Ebenfalls geladen, aber **nicht ausgewertet:** NN „Recognition and Recall“, W3C „Understanding Conformance“, ARIA-APG-Musterübersicht.

## 2. Was die Quellen belegen

### Nielsens Heuristiken (NN-H)

- Zehn allgemeine Faustregeln (kein Regelwerk), seit 1994 unverändert, 1994 aus einer Faktorenanalyse von 249 Problemen abgeleitet. Namen: Sichtbarkeit des Systemstatus; Übereinstimmung zwischen System und realer Welt; Nutzerkontrolle und Freiheit; Konsistenz und Standards; Fehlervermeidung; Wiedererkennen statt Erinnern; Flexibilität und Effizienz; Ästhetisches und minimalistisches Design; Fehler erkennen, diagnostizieren und beheben; Hilfe und Dokumentation.
- Fehler gliedern sich in **Slips** (Handlungsfehler bei Unaufmerksamkeit) und **Mistakes** (falsches mentales Modell) (NN-H, NN-SL). Slips treten gerade bei geübten Handlungen auf, was für Redaktionsarbeit mit Routineaufgaben relevant ist (NN-SL).
- Heuristik 7 verlangt Beschleuniger für Experten, die Neulingen verborgen bleiben dürfen.

### Heuristische Evaluation (NN-HE)

- Evaluatoren beurteilen eine Oberfläche gegen Heuristiken. Sie **ersetzt keine Nutzerforschung**, ergänzt sie aber.
- Eine Einzelperson übersieht Probleme; **3 bis 5 unabhängige Evaluatoren** werden empfohlen, deren Ergebnisse erst nach der eigenen Bewertung zusammengeführt werden (keine gegenseitige Beeinflussung).
- Zwei Durchgänge: zuerst Orientierung, dann gezielte Suche. Zeitrahmen etwa 1 bis 2 Stunden. Der **Umfang** wird eng gewählt: eine Aufgabe, ein Bereich, eine Nutzergruppe, ein Gerätetyp.
- **Ein Heuristikverstoß ist nicht automatisch ein Problem.** Der Kontext entscheidet (Beispiel Hamburger-Menü auf Mobilgeräten). Ausnahmen sind selten, „you should not bet that your design is one of the few exceptions“.

### Schweregrade (NN-SEV)

- Schwere setzt sich aus **Häufigkeit, Auswirkung und Persistenz** zusammen; dazu kommt der Markteinfluss.
- Skala 0 bis 4: 0 kein Problem; 1 kosmetisch; 2 geringfügig; 3 gravierend (wichtig, hohe Priorität); 4 Katastrophe (vor Veröffentlichung zwingend beheben).
- **Bewertungen einer einzelnen Person sind „too unreliable to be trusted“**; der Mittelwert dreier Bewertender gilt für viele Zwecke als ausreichend. Schweregrade werden idealerweise **nach** der Fehlersuche vergeben, nicht währenddessen.

### Cognitive Walkthrough (NN-CW)

- Aufgabenbasierte Inspektion zur **Erlernbarkeit für neue Nutzer**, ohne echte Nutzer. Je Schritt vier Fragen: Versuchen Nutzer das richtige Ergebnis zu erreichen? Bemerken sie, dass die richtige Handlung verfügbar ist? Ordnen sie die Handlung dem Ziel zu? Sehen sie nach der Handlung Fortschritt?
- Ein „Nein“ bei einer Frage markiert den ganzen Schritt als gescheitert. Die Granularität der Schritte legt das Team fest.
- Besonders geeignet für **komplexe, neue oder ungewohnte Arbeitsabläufe**; für Standardmuster wäre es übertrieben. Es bleibt eine von mehreren Methoden und ersetzt keine Tests.
- Herkunft: Lewis, Polson, Wharton, Reiman (CHI 1990); vereinfachte Version nach Wharton u. a.

### Kognitive Belastung (NN-CL)

- Kognitive Last = geistige Ressourcen, die für die Bedienung nötig sind (informell: „Plätze im Arbeitsgedächtnis“).
- **Intrinsisch** (Aufnahme neuer Information, Zielverfolgung, nicht eliminierbar) gegenüber **extraneous** (Verarbeitung ohne Nutzen, minimieren).
- Drei Hinweise: visuelles Rauschen vermeiden; auf vorhandene mentale Modelle bauen; Aufgaben abnehmen (Bilder, bereits Eingegebenes erneut anzeigen, kluge Voreinstellungen).

### Komplexe Anwendungen (NN-CX)

- Die zehn Heuristiken gelten auch für domänenspezifische, komplexe Anwendungen. Definition dort: Anwendungen für breite, unstrukturierte Ziele oder nichtlineare Abläufe geschulter Nutzer; Unternehmensanwendungen zählen dazu.
- Beispiele: bei Wartezeiten über 10 Sekunden genügt kein generisches „Bitte warten“; Versionswiederherstellung stärkt Nutzerkontrolle; interne und externe Konsistenz (Beispiel Plus-Symbol); Live-Vorschau beim Bearbeiten.

### Progressive Disclosure (NN-PD)

- Zunächst wenige wichtige Optionen zeigen, Spezialoptionen auf Anforderung. Das macht Anwendungen leichter erlernbar und weniger fehleranfällig. Nielsen weist auf das Spannungsfeld zwischen gewünschter Leistungsfähigkeit und Einfachheit hin.

### WCAG 2.2 (W-22)

- Stand: W3C Recommendation, 12. Dezember 2024. Drei Konformitätsstufen **A, AA, AAA** (5.2.1). Laut Dokument wird AAA als generelle Anforderung für ganze Websites **nicht empfohlen**, weil nicht alle AAA-Kriterien für alle Inhalte erfüllbar sind.
- Gezählt im Dokument: **31 Kriterien Stufe A, 24 Stufe AA, 31 Stufe AAA** (86 gültige; 4.1.1 Parsing ist entfallen).
- **Neu in 2.2:** 2.4.11 Focus Not Obscured (Minimum) AA; 2.4.12 Focus Not Obscured (Enhanced) AAA; 2.4.13 Focus Appearance AAA; 2.5.7 Dragging Movements AA; 2.5.8 Target Size (Minimum) AA; 3.2.6 Consistent Help A; 3.3.7 Redundant Entry A; 3.3.8 Accessible Authentication (Minimum) AA; 3.3.9 Accessible Authentication (Enhanced) AAA.
- Für Redaktionsoberflächen besonders einschlägige Kriterien (Auswahl, im Wortlaut geprüft wo vermerkt): 2.1.1 Keyboard (A); 2.4.7 Focus Visible (AA); 2.4.11 (AA, **Wortlaut geprüft**: fokussierte Komponente nicht vollständig durch vom Autor erzeugte Inhalte verdeckt); 2.5.8 (AA, **geprüft**: Zielgröße mindestens 24 × 24 CSS-Pixel mit Ausnahmen wie Abstand oder gleichwertiges Bedienelement); 3.3.1 Error Identification (A, **geprüft**); 3.3.3 Error Suggestion (AA); 3.3.4 Error Prevention (Legal, Financial, Data) (AA, **geprüft**: Eingaben, die Daten ändern oder löschen, müssen rückgängig zu machen, geprüft oder bestätigbar sein); 3.3.7 Redundant Entry (A, **geprüft**); 4.1.2 Name, Role, Value (A); 4.1.3 Status Messages (AA, **geprüft**: Statusmeldungen programmatisch bestimmbar, ohne Fokusverschiebung); 1.4.3 Contrast (AA); 1.4.11 Non-text Contrast (AA); 3.2.3 Consistent Navigation (AA).
- **WCAG ist ein Standard für Webinhalte.** Für native oder Desktop-Verwaltungsoberflächen gilt er nicht unmittelbar.

### ARIA Authoring Practices Guide (W-APG)

- Beschreibt, wie ARIA-Semantik auf gängige Muster und Widgets angewendet wird (Rollen, Zustände, Tastaturbedienung). Die Muster selbst wurden noch nicht ausgewertet; die Seite eignet sich als Quelle für `references/accessibility.md` und `patterns/*`.

### Teststärke (NN-5)

- Für qualitative Usability-Studien nennt Nielsen **5 Nutzer** als Regel mit Ausnahmen. Das ist für uns nur als Empfehlung in Berichten relevant („für echte Tests mit Nutzern“).

## 3. Nutzungsbedingungen und Zitierweise

- **NN/g:** „You may use these heuristics in your own work. Please credit Jakob Nielsen and provide the address for this page.“ Wiedergabe oder Abdruck von Seiteninhalt und Postern verlangt weitere Erlaubnis (Copyright-Hinweis). **Folge:** Wir formulieren eigenständig, nennen Nielsen und die URL und kopieren keine Texte, Beispiele oder Poster.
- **W3C:** Das Dokument verweist auf W3C-Haftungs-, Marken- und Dokumentnutzungsregeln. **Folge:** Kriterien werden nur mit Nummer, Titel und eigener Zusammenfassung genannt und verlinkt; keine Wiedergabe ganzer Kriterientexte.
- Jede Referenzdatei des Skills nennt am Ende ihre Quellen mit URL und Abrufdatum (D-006).

## 4. Was die Quellen **nicht** belegen (offen)

| Aussage / Frage | Stand |
|---|---|
| **Joy of Use** als bewertbare Dimension | Keine Primärquelle gelesen. Unsere Zusammenstellung (Kontrollgefühl, Rückmeldung, Reibung, Konzentration, Souveränität) leitet sich aus den Heuristiken 1, 3, 7, 8 ab, ist aber **eigene Konstruktion**, unvalidiert. |
| **Germane Load** (förderliche Last) | In NN-CL nicht enthalten. Nicht übernommen, bis Sweller-Primärliteratur geprüft ist. |
| Feste Schwellen („≤ 4 Elemente im Arbeitsgedächtnis“, „5–7 am Limit“) | **Nicht belegt** (Cowan, Miller nicht gelesen). Werden nicht als Regel verwendet. |
| Zuverlässigkeit von LLM-Bewertungen, Skalenanker | Keine Quelle; durch **eigene Messung** zu klären (D-011). Die Aussage von NN-SEV zu Einzelbewertungen ist ein starkes Argument für Mehrfachläufe. |
| CMS- und Admin-spezifische UX-Muster (WordPress, Drupal, ProcessWire usw.) | **Nicht recherchiert.** Nur NN-CX als allgemeine Quelle für komplexe Anwendungen. Weitere Quellen brauchen Zugriff auf die jeweiligen Doku-Hosts. |
| Rechtlicher Rahmen für Barrierefreiheit (EN 301 549, nationale Vorgaben) | Nicht gelesen. |
| Prüfbarkeit der WCAG-Kriterien ohne Browser oder Hilfstechnik | Eigene Einteilung nötig (siehe `methodology.md`, 6), nicht Teil der Quellen. |
