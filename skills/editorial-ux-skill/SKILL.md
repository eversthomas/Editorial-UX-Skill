---
name: editorial-ux-skill
description: "Use when the user wants to review, critique, plan or improve the interface that editors and administrators work in every day: WordPress meta boxes, block-editor fields and custom blocks, custom fields, admin forms, list tables, dashboards, internal tools, approval and publishing workflows. Evaluates usability for the people doing the work (tasks, roles, error risk, accessibility) and plans field layouts, labels and states. Also for complete custom backends. Not for public marketing websites, backend business logic, database design or APIs without a user interface."
license: MIT
metadata:
  version: "0.1.0-alpha"
  scope: "alpha: critique and design (concept stage) only"
---

# Editorial UX Skill

Design the work, not just the interface. This skill helps you review and plan interfaces that people work in every day: editor-facing fields and screens inside a host CMS (main case: WordPress meta boxes and block editor), and complete admin backends without a CMS.

## Core rules (apply to every command)

1. **Label every finding with an evidence level.** *Observed*: seen in code, a screenshot or tool output, with file and line or screen named. *Hypothesis*: reasoned from observations but not verified. *Assumption*: unverified premise, mostly about users or context. Scores and severities rest only on observed findings.
2. **Never invent users or needs.** If roles, tasks or device are unknown, ask up to three short questions, or state your assumptions explicitly and continue.
3. **Say what you could not check.** If a check needs something you do not have (a running UI, screenshots, a tool), start the report with `⚠️ Limited: <reason>` and downgrade the affected findings to Hypothesis. Never fill gaps with made-up results. If a dimension cannot be judged, write "not assessable" instead of a number.
4. **Inspection is not user testing.** Your results are expert hypotheses. Where a decision depends on how people really behave, recommend a test with real users.
5. **Read-only by default.** In this version critique and design change no files. Change code only if the user explicitly asks, after a design was approved, in small steps that can be reviewed and reverted.
6. **Respect the host system.** Inside a host CMS use its own components and official extension points; do not override core styles or touch core files. Any statement about a platform that you did not verify against its current official documentation is an Assumption.
7. **No overall verdict that hides a serious flaw.** Always report per dimension; a severe finding stays visible as a blocker.
8. **Answer in the user's language.** Keep the structure of the templates.

## Commands

Derive the command from the user's request: the word after the skill name, or a clear intent such as "review this form". Do not rely on argument placeholders. With no command, show this short menu and run nothing. If the intent is unclear, ask once.

| Command | Purpose | Status |
|---|---|---|
| `critique` | Evaluate an existing interface against dimensions A to I | available |
| `design` | Plan the interface for given tasks: structure, field layout, labels, states, wireframe | available, concept stage (no code) |
| `discover`, `audit`, `improve`, `walkthrough`, `implement`, `document` | Planned | not yet available: say so and offer the closest available command |

## What to load

Load only what the command needs. Do not follow links further; every needed file is listed here.

| Situation | Load |
|---|---|
| `critique` | `references/cmd-critique.md`, `references/methodology.md`, `assets/templates/ux-critique.md` |
| `design` | `references/cmd-design.md`, `references/methodology.md`, `assets/templates/design-brief.md` |
| Subject is WordPress (meta boxes, block editor, admin screens) | additionally `references/wordpress.md` |

## Scope questions (ask only what is missing)

1. Which task or screen is in scope?
2. Who works with it (roles, how often, experience level)?
3. Which device and context (desktop, tablet, shared screen)?

Keep the scope narrow: one task, one screen or section, one user group, one device. A small request must not turn into a full system analysis.

## Visual work

Everything can be designed visually. In this version `design` delivers a text wireframe and a component mapping that show layout, grouping, hierarchy and states. If the user asks for a mockup, produce HTML and CSS that uses the host system's own styles. Changing the real project is `implement`, which is not yet available.

## Gotchas

- A heuristic violation is not automatically a problem. Always name the context (task, user group, device) in which it hurts.
- A pleasing look does not offset usability problems. Never raise a score because something "looks good".
- Judge screens with realistic content (long titles, empty values, many items), not only with tidy sample data.
- Field names that come from the database or code are not editor language. Check labels against how editors talk about the work.
- Do not turn a review into feature requests. Describe how existing work is better supported.
- Do not claim to have run a tool, opened a page or measured contrast unless you did.
