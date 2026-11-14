# WordPress notes (meta boxes, block editor)

**Status: Assumptions.** Everything here comes from general model knowledge, not from the current official documentation. WordPress APIs, package names and editor behavior change between versions. When you recommend or write code that depends on these notes, say so, and check the current official WordPress developer documentation if you have access. Otherwise label the statement "Assumption: not verified against current documentation".

## Scope of this adapter

Editor-facing interfaces that a developer builds inside WordPress: meta boxes, fields shown in the block-editor sidebar, custom blocks and their settings, option pages. It does not cover the whole admin area and never proposes changing WordPress core.

## First things to find out

- WordPress version, classic editor or block editor for the post type, theme or plugin that holds the code.
- Which post types and fields exist, which are required, who edits them (roles and capabilities).
- Where field data is registered and shown: look for code that adds meta boxes, registers post meta, registers blocks or settings.
- Whether admin styles are extended or overridden.

## Where editor-facing UI usually lives (Assumption)

- **Meta boxes:** classic boxes added with `add_meta_box`, rendered by a PHP callback. In the block editor they are still available, but appear in a separate area and are saved separately from the content.
- **Post meta with a sidebar panel:** values registered as post meta and edited in a panel of the editor sidebar, built with the editor's own components.
- **Custom blocks:** a block definition (`block.json`) with an edit component; block settings appear in the block toolbar or the settings sidebar.
- **Option pages:** settings screens in the admin menu.

## Host design system (Assumption)

- Use the admin's own markup and classes for forms and buttons, and the editor's component library in React-based UI. Do not build a differently looking interface inside the admin.
- Do not hard-code colors: users can choose an admin color scheme. Do not override core classes or selectors; add your own namespaced classes.
- Keep extra CSS minimal and scoped to your own elements so that WordPress updates do not break it.

## Field design for editors (applies the methodology)

- Group fields by the editor's task, in work order. Use a heading or fieldset with legend per group. Put rarely used fields behind a disclosure.
- Labels in editor language, bound to the field. Help text close to the field, in plain words, describing what the value affects. Placeholder text is not a label.
- Use the right control: date picker for dates, select or radio for fixed choices, toggle for on/off, media picker for images. Avoid free text where a structured value is needed.
- Show validation next to the field, say what is wrong and how to fix it. Do not rely on color alone. Warn before risky actions such as publishing.
- Make required fields visible before saving. Explain what happens when a required value is missing.
- Repeating groups and conditional fields: keep the number small, show the trigger rule, and test with long content and many rows.
- Show where a value will appear on the public site (a short note or preview) so editors understand the effect.

## Accessibility and safety when you build later (Assumption)

- Every control has a label bound to it, groups of radio buttons or checkboxes have a group label, help text is linked to its field, focus is visible, targets are large enough.
- Any code you write must check capabilities, verify nonces on save, sanitize input and escape output. Never trust submitted values.
- Do not store editor-facing configuration in a way that breaks when the plugin or theme is switched, and tell the user where data lives.

## What to verify in the real system

Rendering of meta boxes in the block editor, behavior of the sidebar panel, available components and their package names, how required fields and validation are enforced, how the interface looks with different admin color schemes, keyboard operation, and behavior with long content.
