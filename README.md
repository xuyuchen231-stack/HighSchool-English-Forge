# HighSchool-English-Forge

A source-faithful Gaokao English teaching and assessment skill. It turns a user-supplied paper into a complete learning package rather than a short answer sheet.

## Standard examination package
1. Original paper PDF — intact source pages, in original order.
2. Complete solution PDF — answer overview, question-by-question explanations, reading evidence, sentence parsing, option elimination, language points, vocabulary/collocations and extension exercises.
3. Writing PPTX — application writing and continuation writing, foundation and advanced tracks, explained phrases and sentence patterns, model analysis and practice.
4. QA report — coverage, evidence, unresolved issues, PDF/PPT rendering inspection.

## What makes this English-specific
- Reading answers are anchored to exact text evidence and annotated on the passage.
- Vocabulary is extracted from the actual exam context, not pasted from a generic word list.
- Collocations, register, word formation, polysemy, paraphrase and distractor design are taught in context.
- Writing teaching distinguishes application writing from continuation writing, with separate communicative and narrative requirements.

## Mandatory production rules
- Work on one uploaded examination at a time, in upload order.
- Work on one printed chapter/section at a time; complete, check and export it before proceeding.
- If listening audio/transcript is missing, mark listening blocked rather than guessing.
- Do not call a partial chapter a complete exam solution.
- All PPT slides must be English-only and follow a dense, visually disciplined senior-high classroom style. See `references/full-english-classroom-ppt-standard.md`.

## Use
Upload the complete exam PDF/images (and listening audio or verified transcript if listening is included), then ask the agent to run the full exam workflow. Specify province/year if known. If unknown, the agent must state its assumptions. Do not ask it to invent missing pages, audio or official answers.

For a complete package, see `references/exam-production-workflow.md`. The PPT requirements are in `references/writing-slide-deck-spec.md`.

## Scope and status
The repository provides workflow specifications, teaching standards, templates and structural validation. It does not contain a complete, independently audited database of every Gaokao paper or every curriculum knowledge point. A passing script is not proof of linguistic correctness or visual quality.

## Copyright
Keep user-supplied examination papers and generated full-paper reproductions private unless the user has the right to redistribute them. Public GitHub commits should contain reusable tools and templates, not full copyrighted exam scans.
