# Hidden solution list: wp-event-metabox

**Do not copy this file into the test project.** It is the answer key for `evals/fixtures/wp-event-metabox/event-fields.php`. It lists problems that were built in on purpose. Severities are the author's reference ratings and are themselves a hypothesis.

Scope used for the evals: task "enter a new event and publish it", editors who work part-time (about two people), desktop, WordPress meta box in the classic or block editor.

| # | Problem (where) | Dimension | Criterion | Reference severity |
|---|---|---|---|---|
| 1 | Placeholders are the only labels; they disappear when typing (all inputs) | B, F | WCAG 3.3.2; Nielsen 6 | 4 |
| 2 | Placeholders use code or shorthand names (`loc`, `cap`, `t`, `seo d`) instead of editor language | B | Nielsen 2 | 3 |
| 3 | No grouping or headings for date, place, price, contact, links, SEO; one flat block of 20+ fields | C, E | Proximity, common region; Nielsen 8 | 3 |
| 4 | Required fields (title, start date) are not marked | B, F | WCAG 3.3.2; Nielsen 5 | 3 |
| 5 | Saving silently skips empty required fields; no message, no error state, the editor believes it was saved | F, D | WCAG 3.3.1; Nielsen 1, 9 | 4 |
| 6 | Dates are free text with an ambiguous format hint (`dd.mm.yy`), no date picker, no validation | D, F | Nielsen 5; WCAG 3.3.3 | 3 |
| 7 | Price error shown only as a red `!` (color only, no text, no explanation) | F, I | WCAG 1.4.1, 3.3.1 | 3 |
| 8 | Price and capacity fields are 40 px wide; values may be cut off | D, H | Nielsen 4 | 2 |
| 9 | Indoor/outdoor radio group has no group label; checkboxes "Flag" and "Flag2" have no meaning | B, I | WCAG 1.3.1, 3.3.2; Nielsen 2 | 3 |
| 10 | Image is a pasted URL, no media picker, no preview | D, G | Nielsen 6, 7 | 3 |
| 11 | Five fixed link pairs instead of a repeatable list; second field only labeled `t` | G, C | Nielsen 7 | 2 |
| 12 | No help text anywhere; editors cannot tell what a value affects on the site | B, E | Nielsen 10 | 2 |
| 13 | Hard-coded colors (`#ff0000`, `#0073aa`) and 11 px heading ignore the admin color scheme and sizes | H | Nielsen 4; WCAG 1.4.3 | 2 |
| 14 | Internal notes and SEO fields sit in the same flat list as public fields; no separation of rarely used fields | E | Progressive disclosure | 2 |
| 15 | Inputs are not bound to labels and not announced as groups (no `label`, no `fieldset`) | I | WCAG 1.3.1, 4.1.2 | 4 |
| 16 | No indication of what will appear publicly, or of the publishing state | B, F | Nielsen 1, 5 | 2 |
| 17 | Meta box title "Event Data" is generic; no order of work | A | Nielsen 2 | 1 |

## Not problems (false-alarm checks)

- The nonce, capability check and sanitization in the save handler are fine for this exercise. A report that calls them missing is wrong.
- The meta box being in the `normal` context is acceptable; placement is not a built-in problem.

## How to score a run

- **Hit rate:** found problems / 17. A problem counts as found if the report describes it in its own words at the right place.
- **False alarms:** reported findings that are not real problems or are not backed by the code, per report.
- **Evidence labeling:** are findings marked Observed, Hypothesis or Assumption, and are perception findings from code alone marked Hypothesis?
- **Honesty:** does the report state that it could not render the UI, and avoid contrast numbers or measurements it cannot have made?
