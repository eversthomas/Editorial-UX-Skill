# Smoke test: critique on wp-event-metabox (2026-11-14)

**Status: informal, one run. Not a measurement.** It served to find gaps in the instructions before the first real test.

## Setup

- Subject: `evals/fixtures/wp-event-metabox/event-fields.php`, prompt as in eval 1 (German).
- One subagent was told to read `SKILL.md` and the files listed for `critique` and WordPress, then follow them. It did **not** see `evals/solutions/`.
- **Not tested:** automatic activation of the skill by its description (the files were handed over by instruction). **No baseline** without the skill yet. Counting was done by the author of the skill, not independently.

## Result against the answer key

- **Found: 16 of 17** built-in problems. Missed: #17 (generic box title, severity 1). #16 (no hint where values appear publicly / publishing state) only partly.
- **False alarms:** none identified. One out-of-scope note (no autosave guard in the save handler) is true of the code and was kept out of the scoring, as intended. The report did not call the nonce or capability check missing.
- **Evidence labels:** present on every finding. Perception findings (colors, widths, target size) were Hypotheses.
- **Honesty:** started with the `⚠️ Limited` line, gave no contrast or size measurements, marked WordPress statements as not verified, scored two dimensions "not assessable".
- **No single overall score.** The blocker (dimension F) was marked.

## Gaps found in the instructions, and what was changed

| Gap (from the agent's test notes) | Change |
|---|---|
| The user's question "what to fix first" had no place at the start of the report | Template got a short "Summary (answer first)" |
| Findings mixing observed and hypothetical parts: unclear which evidence level to use | `cmd-critique.md`: one level per finding, split or list the hypothetical part separately |
| Score 0 vs 1 was ambiguous ("impossible" vs "severity 4") | Methodology: 0 = task cannot be completed at all, 1 = severity 4 but completable |
| Orientation (A) and visual quality (H) for one box without rendering | Methodology: often "not assessable", say so |
| How fine line references should be | `cmd-critique.md`: line ranges, one finding per place |
| Whether to mention serious non-UX issues | Template: "Out-of-scope observations", no severity |

## Next

Run the same prompt **without** the skill (baseline) and with the skill several times, ideally in a fresh Claude Code or Cursor session with the skill really installed, and compare as described in `evals/README.md`.
