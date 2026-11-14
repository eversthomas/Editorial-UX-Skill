# Command: design (concept stage)

Plan the editor-facing interface for given tasks. Output is a brief and a wireframe. No code, no file changes.

## Inputs

- The tasks editors must do (create, edit, replace an image, prepare publishing, correct a mistake, find an item, bulk edit).
- The user groups and roles, how often they work with it, their experience.
- The content model: what fields or blocks exist or are planned, which are required, which depend on others.
- The host system and its constraints (for example WordPress admin and block editor).

If an input is missing, ask up to three short questions, otherwise mark it Assumption. Never invent users.

## Procedure

1. **Tasks first.** List the real tasks in the editors' words, with frequency. Rank them. Design for the frequent and the risky tasks.
2. **Field inventory.** List every field or control with its purpose, who fills it, when, whether it is required, and where the value appears later (so editors know what it affects).
3. **Group and order by task, not by database.** Group fields that belong together in the editor's mind (proximity, shared region). Order by the sequence of work. Put frequent fields first and rarely used ones behind progressive disclosure.
4. **Name in editor language.** Write a label and, where needed, a short help text for each field. Avoid code names, abbreviations and internal jargon. A placeholder is not a label.
5. **Conditional display and defaults.** Show a field only when it is relevant; say what triggers it. Offer sensible defaults and re-use earlier input instead of asking twice.
6. **States and errors.** For each important field and action define: empty, filled, invalid (message that says what is wrong and how to fix it), saved, unsaved changes, loading. Prevent mistakes with constraints, formats and confirmations for risky actions (publishing, deleting). Make changes reversible where possible.
7. **Host constraints.** Use the host's own components and styles. Note where the host limits you. For WordPress follow the additional notes (all Assumptions until verified).
8. **Accessibility by design.** Labels bound to fields, logical order, keyboard operation, visible focus, errors not shown by color alone, adequate target size.
9. **Deliver** with the design-brief template: tasks, groups and order, wireframe, component mapping, states and messages, open questions, what to verify in the real system, what to test with real users.

## Wireframe

Provide a text wireframe (monospaced block) showing regions, grouping, hierarchy and the main action. On request, produce an HTML and CSS mockup that uses the host's own styles. Do not present the wireframe as the finished interface.

## Do not

- Do not add features nobody asked for. Plan how the existing work is supported.
- Do not decide silently on trade-offs (for example hiding fields). Name the options and recommend one.
- Do not touch the project's files. Implementation is a later command.
