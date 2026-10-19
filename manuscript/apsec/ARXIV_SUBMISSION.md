# Posting the accepted version on arXiv

`make apsec-arxiv` builds everything: `apsec/arxiv/vera-apsec2026-arxiv.tar.gz` (the upload),
`apsec/arxiv/main.pdf` (what arXiv will produce) and the sources it contains.

The package inlines the author block, adds a first-page footnote with the acceptance and the IEEE
copyright notice, and ships `main.bbl`, because **arXiv does not run BibTeX**.

## Before uploading

1. **Internal clearance.** Confirm with the co-authors' institutions that the preprint may be
   posted, and obtain any communication or legal sign-off that applies.
2. **Co-authors' agreement.** One line to the six co-authors is enough; nobody should discover the
   preprint after the fact.
3. **An arXiv account with submission rights.** A first submission in `cs.SE` needs an
   *endorsement*. The simplest route: Tushar Sharma or Saurabh Rajput (both publish on arXiv)
   either submits it, or endorses you. Ask early, it can take a few days.

## The form, field by field

| Field | What to put |
|---|---|
| Submission type | Article (new submission) |
| Primary category | `cs.SE` (Software Engineering) |
| Cross-lists | `cs.CY` (Computers and Society), `cs.LG` or `cs.AI` |
| License | Keep the default **arXiv non-exclusive licence**. Do not pick CC BY: it can conflict with the IEEE copyright transfer |
| Title | VERA: A Responsible AI Dashboard for Assessing LLM Deployments in Light of the EU AI Act |
| Authors | Robin Quériaux, Solveig Bachellery, Léa Déléris, Saurabh Rajput, Mariam Barry, Tushar Sharma, Jérôme Lebecq |
| Abstract | The paper's abstract, as plain text, with no LaTeX macros |
| Comments | `Accepted at APSEC 2026 (Software Engineering in Practice track). 11 pages. Tool and study material: https://github.com/FinAI-Lab/VERA` |
| ACM class (optional) | `D.2.9; K.4.1` |
| Files | Upload the `.tar.gz`. Do **not** upload the IEEE-typeset PDF from IEEE Xplore |

## After publication in IEEE Xplore

Update the arXiv entry (new version or just the comments) with the DOI, and keep the copyright
footnote. The IEEE author posting policy allows the submitted and accepted versions on arXiv; the
final IEEE-formatted PDF is the one that may not be posted there.

## Checks done by the build

- 0 LaTeX errors, and the PDF carries the acceptance footnote.
- The tarball holds only sources, class and style files, figures and the `.bbl`.
- Size is about 6 MB, well under the arXiv limit.
