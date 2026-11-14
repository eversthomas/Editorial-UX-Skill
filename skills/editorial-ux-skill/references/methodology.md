# Methodology

Status: alpha. Scales and rules in section 5 are a draft and have not been calibrated.

## 1. Principles

- This is an **inspection method**: you judge an interface against established criteria. You do not test with users, so findings are hypotheses about problems.
- A single evaluator misses problems and rates severity unreliably. Say so in the report ("single assessment"). For important decisions, recommend repeated independent runs or a test with real users.
- A heuristic violation is only a problem in a context. Name the task, user group and device for every finding.
- Keep the scope narrow: one task, one screen or section, one user group, one device. Do two passes: first get oriented in the task without judging, then look for problems.

## 2. Dimensions

Rate each dimension separately. Guiding questions, not a complete checklist.

| | Dimension | Guiding questions | Roots |
|---|---|---|---|
| A | Orientation | Does the user see where they are? Is navigation understandable? Are relations visible? | Nielsen 1, 4; WCAG 2.4.2, 2.4.5, 2.4.6, 3.2.3 |
| B | Task clarity | Is it clear what to do? Are actions named unambiguously? Is the result of an action predictable? Is help available in context? | Nielsen 2, 10; WCAG 3.3.2, 2.5.3 |
| C | Information architecture | Does the structure match how users think about their work? Are related things grouped? Is density appropriate? | Nielsen 2, 4, 8; WCAG 1.3.1 |
| D | Interaction quality | Are inputs intuitive? Are states clear? Is there immediate, proportionate feedback? | Nielsen 1, 4, 7; WCAG 4.1.3, 3.2.1, 3.2.2 |
| E | Cognitive load | How many decisions and things to remember does a step demand? Is information shown when needed? Is there clutter? | Nielsen 6, 8; progressive disclosure; WCAG 3.3.7 |
| F | Error tolerance | Can errors be prevented? Can changes be undone? Are error messages helpful? | Nielsen 3, 5, 9; WCAG 3.3.1, 3.3.3, 3.3.4 |
| G | Workflow | How many steps do typical tasks need? Are there needless interruptions? Are repeated tasks supported? Are there shortcuts for experts? | Nielsen 7 |
| H | Visual quality | Is it calm and consistent? Is the hierarchy clear? Is density balanced? | Nielsen 4, 8; WCAG 1.4.3, 1.4.11 |
| I | Accessibility | Keyboard operable? Contrast and focus sufficient? Semantics and assistive technology considered? | WCAG 2.2 level AA |

Observable aspects of working comfortably belong into these dimensions, not into a separate score: feedback quality in D, calm and low noise in E, sense of control (undo, visible state) in F, friction and expert speed in G.

## 3. Findings and evidence

Work in two phases. **Phase 1: find and document.** For each problem write what, where (file and line, or screen and element), which dimension and heuristic or criterion, and the context. **Phase 2: rate.** Only after the list exists, assign severity.

Every finding carries exactly one evidence level: **Observed**, **Hypothesis** or **Assumption** (see the core rules). Findings about perception (grouping, hierarchy) from code alone are Hypotheses, because they depend on how the result is rendered.

## 4. Severity

Rate each finding 0 to 4 from three factors: **frequency** (how often it affects the task), **impact** (can users overcome it, can data or content be lost or published wrongly), **persistence** (one-time or repeated annoyance).

| Value | Meaning |
|---|---|
| 0 | Not a problem |
| 1 | Cosmetic: fix only if time allows |
| 2 | Minor: low priority |
| 3 | Major: important, high priority |
| 4 | Catastrophe: must be fixed before the interface is used in production |

For internal tools there is no market impact. The damage of a wrong action (for example publishing unfinished content) counts instead. Mark severities from one assessment as "single assessment".

## 5. Scoring per dimension (draft, uncalibrated)

Derive the score from observed findings. Take the lowest applicable value.

| Score | Condition |
|---|---|
| 0 | A typical task of the dimension cannot be completed at all because of an observed finding |
| 1 | At least one observed severity-4 finding (the task can be completed, but with severe risk or damage) |
| 2 | At least one observed severity-3 finding |
| 3 | Several severity-2 findings or recurring patterns |
| 4 | At most isolated severity-1 or severity-2 findings |
| 5 | No relevant findings and sufficient coverage of the dimension |

Rules:
- Without sufficient coverage a 5 is not possible (maximum 4). Without a basis, write "not assessable".
- When the scope is one component inside a larger screen, orientation (A) and visual quality (H) are often not assessable without rendering or the surrounding screen. Say so instead of guessing.
- A dimension scored 0 or 1 is a **blocker**: list it first and mark it.
- Never combine the scores into one number that hides a blocker. If you give an overall impression, show the per-dimension table next to it.
- Do not rate a dimension higher because the interface looks attractive.

## 6. Accessibility (dimension I)

Reference: WCAG 2.2, target level AA. WCAG applies to web content; for other interfaces say that it applies by analogy only. Classify each check by what it needs:

1. **From code or markup** (for example missing labels, roles, heading structure): can be Observed.
2. **Needs a rendered UI or a tool** (for example contrast ratio, target size, focus not hidden, reflow): without it, a Hypothesis plus the `⚠️ Limited` line.
3. **Needs assistive technology or people**: Hypothesis only, and recommend a real test.

Criteria that often matter for editor interfaces: keyboard operation (2.1.1), visible focus (2.4.7), focus not obscured (2.4.11), alternatives to dragging (2.5.7), target size of at least 24 by 24 CSS pixels (2.5.8), consistent help (3.2.6), no redundant entry (3.3.7), error identification and suggestion (3.3.1, 3.3.3), error prevention for data changes (3.3.4), name, role, value (4.1.2), status messages (4.1.3), contrast (1.4.3, 1.4.11).

## 7. Perception lens (dimensions A, C, E, H)

Use grouping principles to explain why users overlook or mis-assign things:

- **Proximity:** near elements read as related, far elements are overlooked. Unrelated elements in one group hide each other.
- **Similarity:** shared color, shape or size reads as related and equally important. Traps: a decorative element that looks clickable; many equal buttons without a clear main action; identical icons for different things.
- **Common region:** a border or background groups its contents, stronger than proximity or similarity. Too many containers create noise.
- **Visual hierarchy:** contrast, size and grouping guide the eye. If everything is loud, nothing stands out. If you can render the page, blur it slightly to see what actually dominates.

When cues conflict (proximity says group A, color says group B) that is a finding. These principles describe directions, not severity: severity still comes from section 4.

## 8. Cognitive load

Cognitive load is the mental effort needed to operate the interface. Intrinsic load comes from the task and cannot be removed; extraneous load is wasted effort and should be reduced. Ways to reduce it: remove visual clutter, build on mental models users already have, take work off users (sensible defaults, showing earlier input again), show rare options only on request (progressive disclosure). Count decisions and things to remember per step and report them. Do not apply fixed numeric limits.

## 9. Sources

Paraphrased; credit and addresses as requested by the authors. Retrieved November 2026.
- Jakob Nielsen, 10 Usability Heuristics for User Interface Design: nngroup.com/articles/ten-usability-heuristics
- Moran and Gordon, How to Conduct a Heuristic Evaluation: nngroup.com/articles/how-to-conduct-a-heuristic-evaluation
- Jakob Nielsen, Severity Ratings for Usability Problems: nngroup.com/articles/how-to-rate-the-severity-of-usability-problems
- Whitenton, Minimize Cognitive Load to Maximize Usability: nngroup.com/articles/minimize-cognitive-load
- Jakob Nielsen, Progressive Disclosure: nngroup.com/articles/progressive-disclosure
- Harley, Proximity, Similarity and Common Region principles: nngroup.com/articles/gestalt-proximity, gestalt-similarity, common-region
- Gordon, Visual Hierarchy in UX: nngroup.com/articles/visual-hierarchy-ux-definition
- Moran, The Aesthetic-Usability Effect: nngroup.com/articles/aesthetic-usability-effect
- W3C, Web Content Accessibility Guidelines 2.2: w3.org/TR/WCAG22
