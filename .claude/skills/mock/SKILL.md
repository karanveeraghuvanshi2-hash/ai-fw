---
name: mock
description: Full mock interview loop for an Applied AI Engineer role over topics covered so far.
disable-model-invocation: true
argument-hint: "[role or company, e.g. 'Anthropic applied AI' | 'Series B startup']"
---

# Mock interview

Target: `$ARGUMENTS`. If empty, use a generic Applied AI Engineer role at a Series B AI startup.

1. Read `my/topics.md`, `my/log.md`, and `my/review.md`. Questions come from topics marked `[x]` or `[~]`. Lean toward the weak spots in `my/log.md`.
2. Print `=== SESSION NNN: Mock — <target> ===` (session number rules are the same as `/session`).
3. Run these rounds in order. Stay in character as the interviewer. Ask one question at a time and give no hints unless the learner asks.
   1. **Recruiter screen (5 min).** "Walk me through your background and why AI." Judge the story of how they got here and why AI.
   2. **LLM depth (15 min).** 4 questions on fundamentals and RAG/agents.
   3. **System design (20 min).** "Design an LLM system for <domain>." Probe evals, cost, latency, and failure modes.
   4. **Debugging (10 min).** A production failure: a tool-call loop, retrieval drift, or a regression after a prompt change.
   5. **Customer round (10 min).** A fuzzy complaint, like "the bot feels dumb." The learner turns it into scoped, measurable changes.
   6. **Behavioral (5 min).** One build-vs-buy or shipping-under-pressure story.
4. Then drop character and give the debrief:
   - a hire / lean hire / lean no / no verdict
   - a 1–5 score for each round
   - the top 3 fixes
   - each miss added to `my/review.md`

Done when every round is scored and the debrief is delivered. The learner can then `/wrap`. Part 2 of the study sheet becomes the debrief plus model answers.
