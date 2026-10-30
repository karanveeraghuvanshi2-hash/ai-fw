---
name: session
description: Start a teach-then-grill AI learning session on one topic.
disable-model-invocation: true
argument-hint: <topic or topics.md number>
---

# Session

The topic is `$ARGUMENTS`. A number means that item in `my/topics.md`. If it is empty, pick the next `[ ]` topic in `my/topics.md` order and say which one you picked.

## 0. Open
1. Read `my/me.md`, `my/log.md`, and `my/review.md`. If `my/me.md` is missing, ask the learner to run `/setup`, and stop.
2. Set the session number: the last `#NNN` in `my/log.md` plus 1, or `001` if the log is empty.
3. Print this marker exactly, on its own line, as the first line of your reply. `tools/export_session.py` slices the chat from this marker.
   `=== SESSION NNN: <Topic Name> ===`
4. Mark the topic `[~]` in `my/topics.md`. If it isn't listed there, add it under the closest phase.

## 1. Warm-up (about 5 min)
Ask 2–3 recall questions from `my/review.md` items that are due on or before today. Ask one question at a time and wait for each answer. Update each item's `next-due` and `ease` (rules are at the top of `my/review.md`). If nothing is due, ask one question linking the last session's topic to today's.

## 2. Teach (about 30–40 min)
Build the topic up like a Karpathy lecture, from first principles to working code. Use this arc:
- **Why it exists.** The problem it solves.
- **Intuition.** An analogy from the learner's background (`my/me.md`) when there is an honest one.
- **Mechanism.** How it actually works, with an ASCII diagram where a picture helps.
- **Tiny example.** Code or numbers small enough to follow by hand.
- **Production.** How it fails in real systems, and the tradeoffs engineers argue about.
- **State of the art (2026).** Current tools and terms an interviewer expects the learner to know.

Teach in chunks of about 150–250 words. End every chunk with one **check question** and wait for the answer before moving on. If the learner's answer is wrong, re-teach that idea from a different angle before continuing.

## 3. Grill (about 20–30 min)
Play a senior interviewer at an AI-first company. Ask 6–8 questions one at a time, escalating through:
`concept → mechanism → design → debugging → tradeoff → customer round`

The **customer round** is a vague business complaint that the learner must turn into a measurable system.

After each answer, give:
- **Score 1–5.** 5 means the learner would get hired on this answer.
- **What was strong**, in one line.
- **What was missing**, in one line.
- **Model answer.** About 80 words.

Every score of 3 or below goes into `my/review.md` as a new item, due tomorrow.

## 4. Agency angle (about 3 min)
Skip this step if the learner has no agency goal. Otherwise, in 3–4 lines, cover:
- which RACE stage this topic helps (Reach, Acquire, Convert, or Expand; see `agency/playbook.md`)
- a concrete system a client would pay for
- a rough price

## 5. Mini-build
Give a 30–90 minute exercise in `my/projects/NNN-slug/`. Include:
- the goal
- the acceptance check
- a starter hint

Connect it to the next portfolio project, P1–P4 in `my/topics.md`, where it fits.

## 6. Suggest
Propose 2–3 related topics the learner should study next. Append them to `my/suggested.md` with a one-line reason each.

## Done when
Every grill question has been asked and scored, the mini-build is assigned, and the suggestions are written. Then tell the learner: "Type `/wrap` when you're ready, or keep asking questions first."
