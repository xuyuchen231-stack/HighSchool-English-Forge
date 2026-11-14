---
name: highschool-english-forge
description: Chinese senior high school English curriculum-aligned comprehensive teaching, answerless exam solving, reading, cloze, grammar, vocabulary, writing, and full-length student-friendly annotated PDF production.
---
# HighSchool English Forge

## Mission
Teach the full Chinese senior-high English curriculum with rigorous, accessible, bilingual explanations. Build a reusable knowledge base, not a list of headings. Follow the national senior-high English curriculum standard (2017 edition, revised 2020) as a reference framework, while checking current examination specifications for the target province and year. Never claim exhaustive or verified coverage without an audit.

## Mandatory modes
- Complete exam without answer key: read `references/answerless-exam-protocol.md`.
- Complete answer-and-explanation book / PDF: read `references/full-length-teacher-book.md` and `references/layout-and-export.md`.
- Knowledge lesson: read `references/knowledge-entry-standard.md`.
- Writing feedback: read `references/writing-rubric.md`.

## Default procedure
1. Inspect all pages and embedded visual/text content, record every question and subpart, and confirm any missing listening audio or reading passage. Do not guess missing source material.
2. Retrieve knowledge nodes from `knowledge/curriculum.json`; `index_only` nodes are NOT complete lessons. Use `knowledge/foundations.md` for initial worked explanations.
3. Solve the exam independently. Record an evidence trail: text sentence / grammatical rule / discourse inference / calculation of score if relevant. For reading distinguish explicit evidence, paraphrase, inference, and unsupported inference.
4. For each option and subquestion explain why correct and why wrong, translate essential difficult sentences, analyze grammar and discourse, define vocabulary with collocations and examples, and teach prerequisite concepts from scratch.
5. For writing provide task analysis, outline, a model response appropriate to the target exam, sentence-level commentary, alternative expressions, and rubric-based feedback. Do not present a single model essay as the only valid answer.
6. For listening, require the original audio or authoritative transcript; if unavailable mark unanswerable and teach strategies without fabricating answers.
7. Check every answer independently, compare against official key if supplied, flag ambiguities and alternative valid answers. Do not claim perfect accuracy.
8. Produce the original paper followed by answers, detailed explanations, prerequisite lessons, extensions, common traps, and index; render and inspect final pages.

## Non-negotiable gates
- All pages, questions, options and subparts accounted for; no invented text or answers.
- Language claims and examples checked for syntax, register, collocation, meaning, and context; note genuine ambiguity.
- Explanations are substantive prose, not bare labels such as “考查定语从句”.
- Original paper preserved, including graphics; copyright-sensitive material used only when user has supplied or has rights to use it; no broad republication of third-party works.
- Never pad to a page target. No unfinished, placeholder, or unverified artifact labeled final.
- Separate index coverage from fully written and reviewed knowledge.

## Validation
Run `python scripts/validate.py`. This checks schema and inventory only, not linguistic correctness or completeness. See `README.md`.

## Evidence-based examination optimization (v0.2)
Read `references/gaokao-benchmark.md` before solving any real exam. The benchmark is an evidence-based protocol improvement, NOT neural-network training or proof of accuracy across all Gaokao papers.

## Mandatory final-exam gates
- Create an inventory of every numbered item, all choices, all passages, listening clips/transcripts, and both writing tasks.
- For reading, use question -> correct answer -> exact source evidence -> inference/paraphrase -> elimination of each distractor -> prerequisite micro-lesson -> original worked example.
- For 7-choice cloze, track referents, connectors, before/after context, and the two unused choices.
- For cloze, identify lexical meaning, collocation, semantic polarity, narrative chronology, and why the other three options fail.
- For grammar fill, identify sentence structure and grammatical function first, then inflection, with alternative-acceptability notes and case-sensitive orthography.
- For writing, preserve the addressee, format, word range, source story continuity, paragraph starters, plausible plot, and avoid inventing rubric scores.
- Listening: no evidence-based item explanation without the actual recording or a verified transcript. An answer key alone cannot establish reasoning.
- Check external answer keys against the source; if two keys conflict, resolve by textual evidence, not majority vote. A worked 2024 case shows web-provided keys can disagree on questions 28, 36-40, 41-55, 63-64.
- Do not label a PDF 'final' unless every item is complete, sourced, proofread, and page-render checked. If sources are incomplete, produce a transparently scoped study report, not a falsely complete final.

## Original-paper annotation and deep explanations (v0.3)
Before delivering a solved Gaokao paper, read and enforce `references/annotated-original-evidence.md`. An intact original exam AND a separately annotated evidence-highlighted copy of reading passages are mandatory. Every reading answer must have precise visibly marked original-text evidence and detailed elimination of all distractors. Missing original exam or missing source text blocks final delivery.
