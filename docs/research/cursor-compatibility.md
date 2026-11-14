# Cursor- und Claude-Code-Kompatibilität

Recherche zur Frage: Was ist nötig, damit `editorial-ux-skill` neben Claude Code auch in **Cursor** funktioniert? Ergänzt `agent-skills-compatibility.md`.

## 1. Quellen und Prüfstatus

| Quelle | Status |
|---|---|
| Cursor: https://cursor.com/docs/skills (Weiterleitung von `/docs/context/skills`) | **Direkt gelesen** (HTML per `curl` geladen, 2026-11-14, Text extrahiert) |
| Cursor: https://cursor.com/docs/plugins | **Direkt gelesen** |
| Cursor: https://cursor.com/docs/reference/plugins | **Direkt gelesen** (Abschnitte Manifest, Komponenten, Marketplace, Einreichung) |
| Claude Code: https://code.claude.com/docs/en/skills | **Direkt gelesen** (Teile als Modell-Zusammenfassung geliefert) |
| Claude Code: Plugin-Seiten (`plugins`, `plugin-marketplaces`, `discover-plugins`, `plugins/manifest-reference`, `plugins/components`, `plugins/marketplace-reference`, `plugins/publish`) | **Gelesen**, `marketplace-reference` nur teilweise |
| Praxistest in Cursor oder Claude Code | **Nicht durchgeführt** |

Die Cursor-Seiten sind veränderlich. Der gelesene Stand ist das Abrufdatum. Frühere Angaben aus Zweitquellen (Impeccable-Doku, Websuche) wurden durch diese Lektüre ersetzt, wo sie abwichen (siehe 2.3).

## 2. Cursor (Primärquelle)

### 2.1 Skills

| Thema | Angabe (Zitate englisch) |
|---|---|
| Ordnerformat | Ein Ordner mit `SKILL.md`; optional `scripts/`, `references/`, `assets/` |
| Projektpfade | `.agents/skills/` und `.cursor/skills/` |
| Nutzerpfade | `~/.agents/skills/` und `~/.cursor/skills/` |
| Kompatibilitätspfade | „For compatibility, Cursor also loads skills from Claude and Codex directories: `.claude/skills/`, `.codex/skills/`, `~/.claude/skills/`, and `~/.codex/skills/`.“ |
| Rekursion | „Cursor walks the skills root recursively and picks up any SKILL.md it finds.“ Der Kategorieordner ist nur Organisation; die Identität kommt vom Ordner, der `SKILL.md` enthält. |
| Verschachtelte Projekte | Ein `.cursor/skills/` oder `.agents/skills/` irgendwo im Repository wird gefunden und auf Dateien in diesem Verzeichnis begrenzt |
| Entdeckung | Beim Start; „The agent is presented with available skills and decides when they are relevant based on context.“ |
| Slash-Aufruf | „Skills can also be manually invoked by typing / in Agent chat and searching for the skill name. A skill invoked this way attaches to one message.“ Für die ganze Sitzung: Custom Mode |
| Argumente | **Auf den Seiten nicht dokumentiert.** Keine Platzhalter wie `$ARGUMENTS`. |
| Cloud Agents | Persönliche Skills in `~/.cursor/skills/` und `~/.agents/skills/` werden nicht auf Cloud Agents kopiert (außer per „Sync Skills“ für `~/.cursor/skills/`). Projektskills im Repository funktionieren dort. |
| Größe | Keine Zahlen; „Keep your main SKILL.md focused and move detailed reference material to separate files.“ |

### 2.2 Frontmatter in Cursor

| Feld | Pflicht | Regel |
|---|---|---|
| `name` | **ja** | „Lowercase letters, numbers, and hyphens only. **Must match the parent folder name.**“ |
| `description` | **ja** | „Describes what the skill does and when to use it. Used by the agent to determine relevance.“ Ohne Beschreibung wählt der Agent den Skill kaum von selbst, Aufruf per Name geht weiter. |
| `paths` | nein | Glob-Muster, die den Skill auf passende Dateien begrenzen |
| `disable-model-invocation` | nein | `true`: nur per `/skill-name` |
| `icon`, `color` | nein | Nur für den Custom-Mode-Badge |
| `metadata` | nein | Beliebige Schlüssel/Werte |

**Nicht aufgeführt:** `license`, `compatibility`, `allowed-tools`, `user-invocable`, `argument-hint`, `model`, `effort`. Ob Cursor sie ignoriert, warnt oder verwirft, steht nicht auf den Seiten. Warnungen sind nur für nicht lesbare Dateien, ungültiges Frontmatter oder fehlende Beschreibung dokumentiert („In Cloud Agents … shows a warning in the run that names the skill“).

### 2.3 Korrekturen gegenüber den Zweitquellen

| Zweitquelle behauptete | Primärquelle |
|---|---|
| `license` und `compatibility` werden unterstützt | **Nicht aufgeführt** (Behandlung unbekannt) |
| `name` muss dem Ordner entsprechen (Drittanbieter) | **Bestätigt**, offiziell |
| Skills können aus GitHub „importiert“ werden | **Nur über Plugin und Marketplace**, nicht als einzelner Skill-Ordner (2.5) |
| Keine Argumentersetzung | **Passt**: nicht dokumentiert |

### 2.4 Rules und Commands

- Cursor bietet den eingebauten Skill `/migrate-to-skills`, der „dynamic rules“ und Slash-Befehle in Skills umwandelt. Konvertierte Slash-Befehle erhalten `disable-model-invocation: true`.
- Regeln mit `alwaysApply: true` oder `globs` werden nicht migriert. Das heißt: Cursor-Rules (`.mdc`) bleiben ein eigenes Konzept neben Skills. Wir brauchen sie nicht.
- Eingebaute Cursor-Skills (u. a. `/review`, `/loop`, `/canvas`, `/create-skill`) kollidieren nicht mit `editorial-ux-skill`.

### 2.5 Installation und Verteilung in Cursor

| Weg | Beleg |
|---|---|
| **Ordner ablegen** in `.claude/skills/`, `.agents/skills/` oder `.cursor/skills/` (projektweit oder nutzerweit) | Skills-Seite |
| **Aus GitHub-Repository:** „Skills aren't imported on their own.“ Man verpackt sie als **Plugin** und veröffentlicht es über einen **Marketplace**. Import in Customize über „From GitHub Repository“; das Repository braucht `.cursor-plugin/marketplace.json`. Alternativ als Team-Marketplace (Teams/Enterprise). | Skills-Seite, Plugins-Seite |
| **Öffentlicher Cursor-Marketplace:** Einreichung über cursor.com/marketplace/publish. „Every plugin is manually reviewed … All plugins must be open source.“ | Plugins-Seite |
| **Lokal testen:** Plugin nach `~/.cursor/plugins/local/<name>`, danach Neustart oder „Developer: Reload Window“ | Plugins-Seite |

### 2.6 Plugin-Formate in Cursor

Cursor lädt zwei Formate, erkennbar am Manifest:

| Format | Manifest | Enthält |
|---|---|---|
| **Agent Plugins** (offener Standard, agent-plugins.org) | `plugin.json` im Plugin-Wurzelverzeichnis (mit `$schema`) | Skills und MCP-Server |
| **Cursor Plugins** | `.cursor-plugin/plugin.json` | zusätzlich Rules, Agents, Commands, Hooks, Variablen |

- Skills in Plugins: `skills/<name>/SKILL.md`. Ein `SKILL.md` im Plugin-Wurzelverzeichnis zählt als Ein-Skill-Plugin (nur ohne `skills/`-Ordner und ohne `skills`-Feld).
- Pflichtfeld nur `name` (Kleinbuchstaben, kebab-case, Ziffern, Bindestriche, Punkte).
- Marketplace-Manifest `.cursor-plugin/marketplace.json`: Pflicht `name`, `owner`, `plugins[]`; je Eintrag `name`, `source`.
- Einreichungs-Checkliste (Auszug): gültiges Manifest, eindeutiger kebab-case-Name, klare Beschreibung, README, Pfade relativ ohne `..`, lokal getestet.

## 3. Claude Code (Primärquelle)

| Thema | Claude Code |
|---|---|
| Pfade | Projekt `.claude/skills/<name>/SKILL.md`, nutzerweit `~/.claude/skills/`, Plugin `<plugin>/skills/<name>/SKILL.md`, verschachtelt `<subdir>/.claude/skills/` |
| Frontmatter | „All fields are optional. Only `description` is recommended.“ Unbekannte Felder werden **ohne Meldung ignoriert**. Zusätzlich zur Spec u. a. `argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `model`, `effort`, `context`, `when_to_use`, `paths`, `hooks` |
| `name` = Ordnername? | **Nein, nicht erforderlich** (`name` setzt den Befehlsnamen, „The directory name also invokes the skill.“) |
| Argumente | `/skill-name <args>`: `$ARGUMENTS`, `$0…$N`, benannte `$name`. Ohne Platzhalter im Body hängt Claude Code „`ARGUMENTS: <your input>`“ an. |
| Größe | „Keep `SKILL.md` under 500 lines.“ `description` + `when_to_use` werden bei **1 536 Zeichen** gekappt; „Put the key use case first.“ |
| Beschreibungsbudget | Listenbudget ca. 1 % des Kontextfensters; selten genutzte Beschreibungen werden zuerst gekürzt, Namen bleiben (Zusammenfassung) |
| Kompaktierung | Nach Kompaktierung bleiben je Skill die ersten **5 000 Token**; alle Skills teilen ein Budget von 25 000 Token |
| Supporting Files | Nicht vorgeladen; aus `SKILL.md` referenzieren |
| claude.ai-Upload | Nur die sechs Spec-Felder; ein weiteres Feld führt zu einem **harten Fehler** |

### Claude-Code-Plugins

- Manifest optional: `.claude-plugin/plugin.json`; „`name` is the only required key“ (kebab-case, keine Leerzeichen).
- Skills in `skills/<name>/SKILL.md`, Befehl **`/<plugin>:<verzeichnis>`**. Ein `name` im Frontmatter ersetzt nur das letzte Segment.
- Ohne `skills/`-Ordner lädt ein `SKILL.md` im Plugin-Wurzelverzeichnis als einzelner Skill.
- Marketplace: `.claude-plugin/marketplace.json` (Pflicht `name`, `owner.name`, `plugins[]` mit `name` und `source`). Ein Plugin-Repository kann selbst Marketplace sein (`"source": "./"`).
- Installation: `/plugin marketplace add owner/repo`, dann `/plugin install <plugin>@<marketplace>`. Versions-Pin mit `owner/repo#v1.2.0`. Direkt `claude plugin install owner/repo` ohne Marketplace ist **nicht dokumentiert**.
- Scopes: user, project (`.claude/settings.json`), local.
- Veröffentlichung: Eigener Marketplace ohne Einreichung („the plugin is published, with no submission form“). Anthropic-Verzeichnis über das Developer-Portal (bezahlter claude.ai-Plan; Review-Kriterien nicht gelesen).
- Namen, die als Anthropic-Plugin durchgehen (`claude-`, `anthropic-`, `anthropics-` am Anfang), werden von `claude plugin validate` als Fehler gemeldet. **`editorial-ux-skill` ist davon nicht betroffen.**

## 4. Folgen für Editorial UX Skill

### 4.1 Ein gemeinsamer Installationsort funktioniert (belegt)

Cursor liest laut offizieller Doku `.claude/skills/` und `.agents/skills/`. Eine Installation unter `.claude/skills/editorial-ux-skill/` erreicht damit **beide** Agenten, ohne Build (Plan 9.2). Zu vermeiden: zusätzlich eine Kopie unter `.cursor/skills/` (Dopplung; Verhalten bei gleichem Namen in Cursor nicht dokumentiert).

### 4.2 Name = Ordnername: jetzt offiziell begründet (D-002)

Spec **und** Cursor verlangen Gleichheit von `name` und Ordnername. Nur Claude Code ist lockerer. Die Regel für alle Installationen: Ordner `editorial-ux-skill/`, `name: editorial-ux-skill`. Das Umbenennen des Repositorys ist damit **nicht erforderlich** für die Funktion, sofern die Nutzlast im Unterordner `skills/editorial-ux-skill/` liegt (D-003).

### 4.3 Frontmatter (stützt D-005, mit neuer Unsicherheit)

- Gemeinsame Schnittmenge aller drei: `name`, `description`, `metadata`.
- `license` und `compatibility` sind Spec-Felder und werden von Claude Code akzeptiert. Cursor listet sie **nicht**. Ihre Behandlung ist ungeprüft. Praxistest nötig; bis dahin ist `license: MIT` vertretbar (Claude Code ignoriert Unbekanntes), aber nicht belegt für Cursor. Alternativ in `metadata` oder nur in `LICENSE` führen.
- Nicht verwenden: `argument-hint`, `user-invocable`, `allowed-tools`, `paths`, `icon`, `color`, `when_to_use`.
- `name` ist in Cursor **Pflicht**, in Claude Code optional: wir setzen es immer.

### 4.4 Befehle ohne Platzhalter (bestätigt D-017)

Cursor dokumentiert keinen Argumentmechanismus; `$ARGUMENTS` gäbe es nur in Claude Code. `SKILL.md` leitet den Befehl aus dem Text der Anfrage ab. Ungeklärt: Ob Text hinter `/editorial-ux-skill` in Cursor in dieselbe Nachricht gelangt. Die Doku sagt nur, der Skill „attaches to one message“. Der Praxistest bleibt nötig. Als Rückfallweg gilt die natürlichsprachliche Anfrage.

### 4.5 Keine Sub-Agenten als Pflicht (stützt D-013)

Cursor hat Sub-Agenten, aber die Skills-Doku sieht keinen Skill-gesteuerten Start vor (Zweitquelle: „not reliably skill-spawnable“, nicht an der Primärquelle geprüft). Alpha bleibt im Einzelkontext.

### 4.6 Kompaktierung (stützt D-008)

Claude Code behält je Skill die ersten 5 000 Token. Wichtigste Regeln stehen am Anfang von `SKILL.md`.

### 4.7 Beschreibung

Spec-Limit 1 024 Zeichen. Wichtigster Anwendungsfall zuerst. Imperativ formuliert. Ohne `description` setzt Cursor den Skill kaum selbst ein.

### 4.8 Unser Layout ist bereits ein Plugin-Layout (neu)

`skills/editorial-ux-skill/SKILL.md` (D-003) entspricht dem Plugin-Standard `skills/<name>/SKILL.md` bei Claude Code, Cursor und Agent Plugins. Das Repository ließe sich später mit geringem Aufwand als Plugin verteilen. Offen:

- **Claude Code:** Befehl wäre `/<plugin>:<skill>`, bei gleichem Namen also `/editorial-ux-skill:editorial-ux-skill`. Ein Ein-Skill-Plugin mit `SKILL.md` im Plugin-Wurzelverzeichnis wäre eine Alternative; ob der Befehl dann kürzer ist, steht nicht auf den Seiten.
- **Cursor:** `plugin.json` (Agent Plugins) im Wurzelverzeichnis oder `.cursor-plugin/plugin.json`; GitHub-Import verlangt `.cursor-plugin/marketplace.json`. Marketplace-Aufnahme ist ein manueller Review, Open Source ist Pflicht.
- **Gemeinsames Manifest:** Ob ein einziges `plugin.json` beide Agenten bedient, ist ungeprüft.

### 4.9 Verteilungswege (Stand)

| Weg | Claude Code | Cursor | Aufwand | Zeitpunkt |
|---|---|---|---|---|
| Ordner kopieren nach `.claude/skills/editorial-ux-skill/` | ja | ja (liest `.claude/skills/`) | keiner | **ab Alpha** |
| Eigener Marketplace im GitHub-Repository | `.claude-plugin/marketplace.json` | `.cursor-plugin/marketplace.json` | gering | Beta |
| Öffentlicher Cursor-Marketplace | – | manueller Review | mittel | nach 1.0 |
| Anthropic-Verzeichnis | Developer-Portal, bezahlter Plan | – | mittel | optional |
| `npx`-Installer | – | – | hoch, widerspricht „keine Build-Abhängigkeit“ | nicht geplant |

## 5. Vorschlag für den Plan

1. **Cursor ist gleichrangige Zielumgebung** mit eigenem Testlauf (Phase 2: Kurztest, Phase 6: voller Verhaltenstest). Eval-Ergebnisse je Agent getrennt ausweisen.
2. Installationsanleitung: **einziger Ort `.claude/skills/editorial-ux-skill/`** (oder `.agents/skills/`), nicht doppelt.
3. Strukturtest prüft zusätzlich: Ordnername = `name`, nur zulässige Zeichen, `description` vorhanden, keine Platzhalter im Body.
4. Plugin-/Marketplace-Dateien frühestens in Beta, getrennt von der Nutzlast.

## 6. Noch zu prüfen (Praxistest)

1. Cursor: Wird der Skill unter `.claude/skills/editorial-ux-skill/` gefunden und per `/` aufgerufen?
2. Cursor: Gelangt Text hinter `/editorial-ux-skill` in die Nachricht an den Agenten?
3. Cursor: Reaktion auf `license` und `compatibility` im Frontmatter.
4. Cursor: Verhalten bei doppelter Installation (`.claude/` und `.cursor/`).
5. Claude Code: Befehlsname bei Plugin-Installation und Ein-Skill-Plugin.
6. Ob ein `plugin.json` beide Agenten bedienen kann.
7. Claude-Code-Review-Kriterien des Anthropic-Verzeichnisses (nicht gelesen).
