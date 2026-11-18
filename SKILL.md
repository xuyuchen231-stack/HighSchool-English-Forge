---
name: highschool-english-forge
description: Produce source-faithful Chinese Gaokao English exam study packs with intact original papers, independently solved answer keys, deeply explained every question, evidence-annotated reading passages, vocabulary and collocation banks, and complete writing-teaching slide decks for application writing and continuation writing.
---
# HighSchool English Forge

## Mission and release philosophy
Build a rigorous, student-readable English learning system, not a thin answer generator. Follow the national senior-high English curriculum (2017 edition, revised 2020) while checking the target province, exam year and current task formats. Default to PEP-aligned language knowledge; clearly label assumptions. Distinguish verified lessons from index-only curriculum entries.

For full exam jobs, read, in order:
1. `references/exam-production-workflow.md`
2. `references/student-readable-explanations.md`
3. `references/reading-evidence-annotation.md`
4. `references/vocabulary-extraction-and-extension.md`
5. `references/writing-slide-deck-spec.md`
6. `references/pdf-ppt-acceptance.md`

For writing-only teaching, read the writing slide-deck spec and writing rubric. For individual writing feedback, use `references/writing-rubric.md`.

## Required deliverables for a supplied examination
Unless the user asks for a narrower scope, produce:
- **A. Original-paper PDF**: complete source pages in original order, preserving page geometry, diagrams, tables, columns, typography and marks. Do not OCR-recreate the exam as a substitute.
- **B. Complete solution PDF**: original paper first (or a separately supplied intact original PDF explicitly linked in the package), followed by concise answer key, every-question explanation, reading evidence annotations, vocabulary/collocation review, language points and transfer practice. The answer key and detailed explanations must agree.
- **C. Writing PPTX**: a complete, editable slide deck teaching both application writing (小作文) and continuation writing (读后续写/大作文), with foundation and advanced tracks, phrase/sentence explanations, model analysis and practice with answer/rubric guidance.
- **D. QA report**: input inventory, source limitations, answer verification, page-render checks, slide checks and any unresolved ambiguity.
If the environment cannot create or validate one format, report that limitation; never claim a missing file exists.

## Mandatory workflow
1. Inspect every page and embedded image. Record exam name, province, year, duration, total score, page count, question IDs, options, subparts, writing prompts, listening assets and source provenance. Hash the source. Do not infer missing pages or audio.
2. Solve independently before consulting any supplied key. Keep an answer ledger with question ID, answer, evidence/rule, confidence, ambiguity and verification status.
3. For every multiple-choice item explain all options, not just the correct one. For every fill-in, translation and writing task cover every requested element. Never leave an item represented only by a topic label.
4. Reading: map question -> exact paragraph/sentence -> paraphrase/inference chain -> correct answer -> each distractor's failure. Create a separate annotated reading copy or clear page-linked annotation set. Mark evidence visibly on the original text; do not highlight a convenient but irrelevant sentence.
5. Cloze: explain grammar, meaning, collocation, discourse relation, referent, tone and chronology as applicable. Explain why each distractor fails in this context.
6. Grammar filling: identify sentence structure and grammatical slot first; then explain word class, inflection, tense/aspect, voice, non-finite form, agreement, clause function or fixed construction. Give alternatives only when grammatically and contextually acceptable.
7. Writing: analyse audience, purpose, genre, content points, format, register, word limit and continuity constraints. Supply a model answer, sentence-level commentary, alternative expressions and a scoring-oriented checklist. A model is not the only valid answer.
8. Extract exam-specific vocabulary and collocations from the actual paper. Separate directly tested/high-value items from useful extensions; include contextual meaning, part of speech, collocation, example, translation, register and common misuse. Never pad with unrelated word lists.
9. Produce the writing slide deck using the dedicated spec. Cover both genres and both proficiency tracks, and include guided practice, independent practice, model answers and feedback criteria.
10. Independently review answers and language. Compare with official keys only after independent solving; investigate every disagreement from the source evidence. For uncertain items state the uncertainty.
11. Build PDFs/PPTX, reopen them, render every page/slide and inspect. Run structural validation; separately conduct linguistic, pedagogical and visual review.
12. Deliver only when all required gates pass. If source material is incomplete, issue a clearly scoped partial pack and enumerate blockers rather than calling it complete.

## Explanation standard
Assume the learner may have weak foundations. Explain in accessible Chinese while preserving precise English. Start with what the sentence or question is saying; show the actual clue and reasoning steps; explain unfamiliar terminology at first use. Avoid unexplained labels such as “考查定语从句”“固定搭配” as a complete explanation. Include why tempting alternatives are wrong and, where useful, how the sentence would change if the alternative were used.

For long sentences use: original sentence -> clause boundaries and core structure -> phrase/function analysis -> natural Chinese translation -> question relevance. Do not translate mechanically.

## Original material, copyright and integrity
Use the user's supplied paper as the source of the original. Preserve it; do not reconstruct missing text. Respect copyright and licensing: user-provided files are processed for their requested study use, but do not publish full third-party papers or answer books to a public repository. GitHub should contain reusable skill instructions, templates and scripts, not a copyrighted exam PDF unless the user confirms the rights and intended public distribution.

## Quality gates
- Coverage: every page, question, option, blank and writing requirement accounted for.
- Accuracy: answer ledger reconciles with detailed explanations; evidence is exact; language usage is checked.
- Pedagogy: a weak student can follow the explanation without another textbook.
- Vocabulary: each selected item is context-grounded; extensions are labelled and useful.
- Writing: both genres, foundation and advanced expressions, explanation and practice included.
- Source fidelity: original exam pages are retained, not silently OCR-recreated.
- Export: PDF/PPTX opens, fonts and symbols render, no clipping, broken tables, missing diagrams or orphaned headings.
- Transparency: unknown audio, unreadable text, ambiguous answers and non-official scoring claims are disclosed.

## Repository validation
Run `python scripts/validate.py` and `python scripts/validate_release.py` when applicable. These scripts check structure and manifest completeness only; they do not prove answer correctness, teaching quality or visual quality. See the acceptance documents.
