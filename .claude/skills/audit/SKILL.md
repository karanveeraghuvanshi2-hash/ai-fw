---
name: audit
description: Practice an AI-consulting bottleneck audit (RACE + goal factoring) on a real or simulated business.
disable-model-invocation: true
argument-hint: "<business description | 'random'>"
---

# Audit drill

Read `agency/playbook.md` first. This drill rehearses its steps 1–2 plus the proposal.

Business: `$ARGUMENTS`. If it is `random` or empty, invent a realistic international B2B business with $30K–$300K/month in revenue, and keep its true funnel numbers hidden.

1. Print `=== SESSION NNN: Audit — <business> ===`.
2. **Discovery call.** You play the business owner: vague, busy, not technical. The learner runs the call. Answer only what the learner actually asks. If the learner asks for numbers you "don't track", say so. That is the untracked-process trap from the playbook.
3. **Bottleneck call.** The learner names the RACE stage with the worst relative conversion and justifies it with the numbers.
4. **Goal factoring.** The learner builds the goal tree down to concrete actions. You push back on any leaf that isn't actionable yet.
5. **Proposal.** The learner pitches 1–3 systems, each with:
   - its RACE stage
   - how it will be measured
   - a fixed price and timeline
   - whether a guarantee is offered
6. **Debrief.** Drop character and score each of these 1–5, each with one line of feedback:
   - discovery questions
   - bottleneck accuracy (reveal the true numbers)
   - quality of the goal tree
   - offer and pricing

Add any misses to `my/review.md`.

If the learner used a real prospect, offer to save the audit in `my/agency/audits/<slug>.md`. It is never committed.

Done when all five phases are complete and the debrief is delivered.
