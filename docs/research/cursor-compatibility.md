# Cursor- und Claude-Code-Kompatibilität

Recherche zur Frage: Was ist nötig, damit `editorial-ux-skill` neben Claude Code auch in **Cursor** funktioniert? Ergänzt `agent-skills-compatibility.md`.

## 1. Quellen und Prüfstatus

| Quelle | Status |
|---|---|
| Claude Code: https://code.claude.com/docs/en/skills | **Direkt gelesen** (zwei Abrufe; Teile als Modell-Zusammenfassung geliefert, im Text markiert) |
| Cursor: https://cursor.com/docs/context/skills (offizielle Doku) | **Nicht gelesen.** Der Abruf scheiterte zunächst an der Netzwerkfreigabe. Nach der Freigabe wurde ein erneuter Abruf vom Auto-Mode-Klassifikator abgelehnt und nicht umgangen. |
| Cursor-Aussagen unten | **Zweitquellen:** (a) Zusammenfassung einer Websuche, die auf die offiziellen Cursor-Seiten verweist (Seiten selbst nicht geöffnet); (b) Tabelle `docs/HARNESSES.md` und `docs/CURSOR-PLUGIN.md` im Impeccable-Repository, Stand Commit `61e73eeb`, vom dortigen Autor gepflegt. |

**Alle Cursor-Angaben sind damit nicht an der Originalquelle verifiziert.** Sie sind als *Annahme* zu behandeln, bis die offizielle Seite gelesen ist. Die Websuche selbst warnt, dass sich Felder und Suchpfade zwischen Cursor-Versionen ändern.

## 2. Cursor (Zweitquellen, ungeprüft)

| Thema | Angabe | Quelle |
|---|---|---|
| Ordnerformat | Ein Skill ist ein Ordner mit `SKILL.md`; optional `scripts/`, `references/`, `assets/` | Websuche |
| Projektpfad | `.cursor/skills/<name>/SKILL.md` | Websuche, Impeccable |
| Weitere gelesene Pfade | `.agents/skills/`, `.claude/skills/`, `.codex/skills/` sowie nutzerweite Entsprechungen | Websuche, Impeccable (`.agents/`, `.claude/`) |
| Rekursion | Cursor durchsucht das Skill-Wurzelverzeichnis rekursiv; verschachtelte Projektordner begrenzen den Geltungsbereich | Websuche |
| Entdeckung | Skills werden beim Start entdeckt; der Agent entscheidet kontextabhängig, wann er sie nutzt | Websuche |
| Aufruf | Manuell per `/` im Agent-Chat | Websuche |
| Frontmatter | Unterstützt: `name`, `description`, `license`, `compatibility`, `metadata`, `disable-model-invocation`. **Nicht** unterstützt: `allowed-tools`, `user-invocable`, `argument-hint`, `model`, `effort` | Impeccable-Tabelle |
| Ordnername = `name` | Drittquelle behauptet: muss übereinstimmen (wie die Spec) | Websuche (Drittanbieter-Anleitung) |
| Argumentersetzung | Keine; laut Impeccable unterstützt nur Claude Code Platzhalter wie `$ARGUMENTS` in `SKILL.md` | Impeccable |
| Sub-Agenten | Vom Agenten oder per `/name` ausgelöst, **nicht verlässlich durch einen Skill startbar** | Impeccable |
| Plugins | Es gibt ein Cursor-Plugin-System mit Marketplace (`cursor.com/docs/plugins`); Impeccable bereitet ein Cursor-Plugin vor (`cursor-plugin/`, `.cursor-plugin/marketplace.json`), Veröffentlichung über `cursor.com/marketplace/publish` | Impeccable (Plugin war dort noch nicht veröffentlicht; Test nur unter macOS, Cursor 3.15.6) |
| Hooks | Cursor kennt `.cursor/hooks.json` (`preToolUse`) | Impeccable; für uns nicht relevant (D-010) |

## 3. Claude Code (direkt gelesen)

Wichtige Abweichungen von der Agent-Skills-Spec und von Cursor:

| Thema | Claude Code |
|---|---|
| Pfade | Projekt `.claude/skills/<name>/SKILL.md`, nutzerweit `~/.claude/skills/`, Plugins `<plugin>/skills/<name>/SKILL.md`, verschachtelt `<subdir>/.claude/skills/` |
| Frontmatter | „All fields are optional. Only `description` is recommended.“ Unbekannte Felder werden **ohne Meldung ignoriert**. Zusätzlich zur Spec u. a. `argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `model`, `effort`, `context`, `when_to_use`, `paths`, `hooks` |
| `name` = Ordnername? | **Nein, nicht erforderlich.** `name` setzt den Befehlsnamen, standardmäßig der Ordnername; „The directory name also invokes the skill.“ Das ist lockerer als die Spec. |
| Argumente | `/skill-name <args>`: `$ARGUMENTS`, `$0…$N`, benannte `$name`. Enthält der Body **keinen** Platzhalter, hängt Claude Code „`ARGUMENTS: <your input>`“ an den Skill-Inhalt an. |
| Größe | „Keep `SKILL.md` under 500 lines.“ `description` + `when_to_use` werden bei **1 536 Zeichen** gekappt, „Put the key use case first.“ (strenger als die 1024 der Spec: Spec-Wert bleibt maßgeblich) |
| Beschreibungsbudget | Listenbudget skaliert mit ca. 1 % des Kontextfensters; selten genutzte Beschreibungen werden zuerst gekürzt, Namen bleiben (Zusammenfassung, nicht wörtlich) |
| Kompaktierung | Nach Kontext-Kompaktierung bleiben je Skill nur die **ersten 5 000 Token** erhalten, alle wieder angehängten Skills teilen ein Budget von 25 000 Token |
| Supporting Files | Nicht vorgeladen; sie müssen aus `SKILL.md` referenziert werden („so Claude knows what each file contains and when to load it“) |
| claude.ai-Upload | Außerhalb von Claude Code gelten nur die sechs Spec-Felder; ein weiteres Feld führt beim claude.ai-Upload zu einem **harten Fehler** |

## 4. Folgen für Editorial UX Skill

### 4.1 Ein Quellordner für beide Agenten reicht (Annahme für Cursor)

Cursor liest laut beiden Zweitquellen auch `.claude/skills/` und `.agents/skills/`. Wenn das stimmt, genügt **eine Installation** unter `.claude/skills/editorial-ux-skill/` (oder `.agents/skills/…`) für beide Agenten, ohne Build und ohne zweite Kopie. Das passt zur Vorgabe „zentrale Quelle, Claude Code ohne Buildprozess“ (Plan 9.2). Offene Einzelheit: Sehen Cursor-Nutzer den Skill dort **doppelt**, falls sie zusätzlich `.cursor/skills/` befüllen? (Impeccable warnt vor doppelten Installationen von Skill und Plugin.)

### 4.2 Kein Argument-Platzhalter in `SKILL.md`

`$ARGUMENTS` funktioniert nur in Claude Code (Cursor: laut Zweitquelle keine Ersetzung). Deshalb gilt für `SKILL.md`:

- **Keine** Platzhalter verwenden. Der Befehl wird aus dem **Text der Nutzeranfrage** abgeleitet („Wenn die Anfrage mit einem der Befehlsnamen beginnt oder ihn klar nennt, …“).
- Claude Code hängt ohnehin `ARGUMENTS: …` an, wenn kein Platzhalter vorkommt. Damit funktioniert dieselbe Datei in beiden Agenten.
- *Annahme (ungeprüft):* Bei `/editorial-ux-skill critique <Ziel>` in Cursor gelangt der Text hinter dem Skill-Namen in die Nachricht an den Agenten. Zu prüfen (siehe 6).
- Konsequenz für die Matrix (Plan 5): Befehle müssen auch bei **natürlichsprachlicher** Anfrage („bewerte das Formular“) funktionieren. Das stärkt zugleich die Aktivierung über die `description`.

### 4.3 Frontmatter: nur Spec-Felder (bestätigt D-005)

- Claude Code ignoriert Unbekanntes stumm, claude.ai-Upload **bricht ab**, Cursor unterstützt eine Teilmenge. Die Schnittmenge ist die Spec: `name`, `description`, `license`, `compatibility`, `metadata`.
- Nicht verwenden: `argument-hint`, `user-invocable`, `allowed-tools` (Cursor: nein; experimentell in der Spec).
- `disable-model-invocation` kennen Claude Code und Cursor, die Spec nicht. Wir brauchen es nicht, da wir Selbstaktivierung wollen.

### 4.4 `name` und Ordnername (schärft D-002)

Die Spec verlangt Gleichheit, Claude Code nicht, Cursor angeblich ja. Wir halten uns an die **strengste** Regel: Ordnername = `name` = `editorial-ux-skill`. Das gilt für den Ordner `skills/editorial-ux-skill/` und für jede Installation. Der Repository-Name spielt dann keine Rolle (D-003). Die Umbenennung des Repositorys bleibt trotzdem sinnvoll, ist aber **nicht blockierend**.

### 4.5 Keine Sub-Agenten-Abhängigkeit (stützt D-013)

In Cursor sind Sub-Agenten nicht verlässlich aus einem Skill heraus startbar. Ein Design, das die isolierte Bewertung zur Pflicht machte (wie bei Impeccable), wäre dort nicht tragfähig. Alpha bleibt im Einzelkontext. Die Eingeschränkt-Regel (D-009) deckt den Fall ab.

### 4.6 Kontextbudget der Kompaktierung

Claude Code behält pro Skill nur die ersten 5 000 Token nach einer Kompaktierung. Daraus folgt: **Die wichtigsten Regeln (Evidenzstufen, Eingeschränkt-Hinweis, Freigabe vor Codeänderungen) stehen am Anfang von `SKILL.md`.** Das stützt D-008 (< 5 000 Token).

### 4.7 Beschreibung

- Spec-Limit 1 024 Zeichen einhalten. Der wichtigste Anwendungsfall steht **zuerst** (Claude Code kürzt bei 1 536 und bei knappem Budget).
- Keine Schlüsselwörter erst am Ende.

### 4.8 Verteilung

| Weg | Aufwand | Anmerkung |
|---|---|---|
| Ordner kopieren oder verlinken nach `.claude/skills/editorial-ux-skill/` | keiner | Erreicht Claude Code, vermutlich auch Cursor (4.1) |
| Cursor-Plugin über Marketplace | mittel | Manifest, Veröffentlichung nur mit Freigabe; Zweitquelle sagt, es gibt dafür noch kein stabiles Muster. **Erst für Beta**, nicht für 1.0-Pflicht |
| Claude-Code-Plugin | mittel | `<plugin>/skills/<name>/SKILL.md`, Namespace `/plugin:skill`; separat prüfen |
| `npx`-Installer | hoch | Widerspricht „keine Build-Abhängigkeiten“; nicht geplant |

## 5. Vorschlag für den Plan

1. **Cursor wird Zielumgebung mit eigenem Testlauf** (Plan Phase 6: „mehrere Agenten“). Zuerst Verhaltenstest in Cursor, dann Aufnahme in die Definition of Done („Kernfunktionen mit mindestens drei Agenten“).
2. Installationsanleitung nennt `.claude/skills/` **und** `.agents/skills/` als gemeinsamen Ort, `.cursor/skills/` optional.
3. `compatibility`-Feld erwägen: „Designed for Claude Code and Cursor; works with other Agent Skills clients.“ (Spec: nur nötig bei besonderen Anforderungen; vorerst weglassen.)
4. `evals/` führt je Agent eine Spalte (Claude Code, Cursor), damit Unterschiede sichtbar werden.

## 6. Noch zu prüfen

1. Offizielle Cursor-Seiten lesen: `cursor.com/docs/context/skills`, `cursor.com/docs/plugins`, `cursor.com/docs/reference/plugins`. **Blockiert**; braucht eine Entscheidung des Projektverantwortlichen (siehe Bericht).
2. Praxistest in Cursor: Wird der Skill unter `.claude/skills/` gefunden? Landet der Text hinter `/editorial-ux-skill` beim Agenten? Wird die `description` ausgewertet?
3. Ob Cursor bei `name` ≠ Ordnername den Skill verwirft oder nur warnt.
4. Nutzerweite und organisationsweite Installationspfade in Cursor.
5. Claude-Code-Seiten zu Plugins und Marketplace (nicht gelesen).
