# Evals

Test cases for editorial-ux-skill in the Agent Skills format (`evals.json`). The answer key for the fixture lives in `solutions/` and must **not** be given to the agent under test.

## Quick manual test (with and without the skill)

1. Make a clean working copy for the test, for example a new folder that contains only `fixtures/wp-event-metabox/event-fields.php` (not `solutions/`).
2. **Baseline (without the skill):** start a fresh agent session in that folder with the skill not installed. Paste the prompt of eval 1 from `evals.json`. Save the answer as `baseline-1.md`.
3. **With the skill:** install the skill (`skills/editorial-ux-skill` copied to `.claude/skills/editorial-ux-skill/` in that folder, which Claude Code and Cursor both read), start a fresh session and paste the same prompt. Save the answer as `skill-1.md`.
4. Repeat steps 2 and 3 twice more if you want to see how much results vary between runs.
5. Compare both answers with `solutions/wp-event-metabox.md`: hit rate, false alarms, evidence labels, honesty about what could not be checked. Note tokens and time if your tool shows them.
6. Repeat with eval 2 (design). No fixture is needed.

Record the results in a table (run, with or without skill, hit rate, false alarms, notes). Use the assertions in `evals.json` as a checklist.

## Notes

- The skill should be activated by the prompt alone. If it is not, note which wording you used: that is a finding about the skill description.
- Judge honesty first: a report that invents measurements or user needs is worse than a shorter one.
