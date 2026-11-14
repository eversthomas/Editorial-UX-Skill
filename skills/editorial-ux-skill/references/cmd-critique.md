# Command: critique

Evaluate an existing interface and report per dimension. Read-only.

## Procedure

1. **Fix the scope.** Use the scope questions from the main file for anything the user did not say. Write the scope at the top of the report: task, screen or section, user group, device. If you must assume something, mark it Assumption.
2. **Gather evidence and list what you inspected.** Read the relevant code, templates, screenshots or description. Name every file, screen or element you actually looked at. If you could not see a rendered UI, say so with the `⚠️ Limited` line and treat perception, contrast, target size and focus findings as Hypotheses.
3. **Orient (pass 1).** Walk through the task as a user would, without judging. Note the steps, decisions and things to remember.
4. **Find problems (pass 2), no severity yet.** Go dimension by dimension (A to I) using the guiding questions. For each problem record: what, where, dimension, criterion, context, evidence level. Use the perception lens for grouping and hierarchy findings. Check labels against editor language, not code names.
5. **Rate.** Only now assign severity 0 to 4 per finding, with a short reason (frequency, impact, persistence). Mark them "single assessment".
6. **Score per dimension** with the draft rule in the methodology, from observed findings only. Use "not assessable" where there is no basis. Mark blockers (score 0 or 1).
7. **Report** with the ux-critique template. Start with the short summary (blockers, top three findings, biggest limit), because the user asks what to fix first. Then scope and limits, the dimension table with blockers marked, findings by severity, hypotheses and assumptions separately, out-of-scope observations, recommended changes by priority, what to test with real users.
8. **Offer next steps:** `design` for the weak areas; a test with real users where hypotheses decide the matter.

## Do and do not

- Do cite the place of every observed finding (file and line range, screen and element). One finding per place where possible.
- Do keep one evidence level per finding. If a problem has an observed core and a hypothetical effect, write two findings, or label the finding by its observed core and list the hypothetical effect separately under Hypotheses.
- Do mention serious things you notice outside usability (for example a security gap) in one line under out-of-scope observations, without a severity. Do not call something missing without checking.
- Do keep recommendations specific and small: what to change, where, why.
- Do not report a style preference as a problem unless a criterion and a context make it one.
- Do not assess dimensions you have no basis for. Say "not assessable".
- Do not change files.

## If the user gives only a description

Everything is then a Hypothesis or an Assumption. Say so, give a short, qualitative critique without scores, and list what you would need to inspect (code, screenshots, a task list) for a full critique.
