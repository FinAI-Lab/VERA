# APSEC 2026 camera-ready — what to do, in order

Accepted 29 September 2026 (paper 0891, SEIP track). Scores: reject, accept, accept.
Conference: 7–10 December 2026, Sheraton Bali Kuta Resort, Bali.

## 1. Hard deadlines

| Date | What | Note |
|---|---|---|
| **9 October 2026 (AoE)** | At least one author registers at the **Professional rate** (Main Conference or Full Pass) | Without it the paper is **not** in the proceedings. This is the only irreversible date. |
| Announced later | Camera-ready upload, with the conference toolkit | The chairs will send instructions and a copyright form |

## 2. Format, from the acceptance mail

- IEEE conference template, `\documentclass[10pt,conference]{IEEEtran}`, no `compsoc`.
- **A4 paper size** (the submitted version was US Letter).
- Title 24 pt, main text 10 pt; PDF; IEEE Policy on Authorship; respect the page limit.

`make apsec-cameraready` builds the A4 version (`apsec/main_apsec_cameraready.pdf`) and checks
the page size, the embedded fonts and the page count. The copyright notice supplied by the
toolkit still has to be added, usually as a `\IEEEpubid` or a first-page footnote.

## 3. What the reviewers asked

Reviewer 2 (accept) asks for one small thing: a sentence at the end of the introduction giving the
structure of the paper.

Reviewer 3 (accept) asks for two substantive additions, and "strongly suggests" reworking the text:

1. **What the banking context changes.** Which design decisions come from the bank, and which would
   differ in, say, a telecommunications or a manufacturing company. Candidates, all already in the
   paper as facts: the self-hosting constraint (prompts may not transit to a third party), the
   three-lines-of-defence separation between those who produce evidence and those who approve,
   the supervisory anchoring of the requirements, and the run-tied artifacts that a filed technical
   document needs.
2. **A real external-validity discussion.** The current one is two sentences. Argue it with the
   generalisation literature the reviewer names: `wieringa2015generalizing` (six strategies,
   architectural similarity) and `ghaisas2013generalizing` (generalising by similarity from
   industrial case studies). Both are now in `references.bib`. State what transfers to another
   large European bank, to an insurer, to a non-regulated company, and why.

Reviewer 1 (reject) will not read the camera-ready, but three of its points are worth a sentence
each, because an ICSE reviewer would raise them too:

- **[W3] Who does what.** Say plainly that engineers host the models and configure the environment,
  and that the non-specialist path starts once a model is connected.
- **[W4] Deployability.** Say what a second institution would have to provide (a served model, the
  benchmark extras, a machine) and what the two deployment profiles give them.
- **[W1] Review quality.** Repeat, without hedging, that the study measures reading, not decision
  quality — the ICSE paper is the one that studies decisions.

## 4. Suggested edit plan (about 250 words net)

| Where | Edit |
|---|---|
| End of Section I | One sentence on the structure of the paper (reviewer 2) |
| Section III (or a new paragraph in §II) | 4–6 sentences: what the banking context fixes in the design, and what would change elsewhere |
| Threats to validity, external validity | Rewrite into a real paragraph, 6–8 sentences, citing the two references |
| Threats, construct validity | One sentence: reading is not decision quality |
| Section VI (deployment experience) | Two sentences: who configures what, and what a second institution needs |

The paper is at its page limit, so pay for these with the passages the reviewers did not need:
the second half of the fallback discussion and one of the two paragraphs on the energy method.

## 5. Order of work

1. Register before 9 October.
2. Apply the edits above in `main_apsec.tex` (they also improve the ICSE paper's Section III).
3. `make apsec-cameraready`, check the report, then add the toolkit's copyright notice.
4. Sign the IEEE copyright form when it arrives.
5. Post the accepted version on arXiv (see `ARXIV_SUBMISSION.md`) — after the internal clearance.
