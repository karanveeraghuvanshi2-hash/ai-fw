---
name: wrap
description: Close the current session. Write the session file, update trackers, push the study sheet to Notion, save.
disable-model-invocation: true
---

# Wrap

Find the current session by its last `=== SESSION NNN: <Topic> ===` marker in this conversation. Slug = the topic in kebab-case.

## 1. Part 1: the chat
Run `python3 tools/export_session.py > /tmp/part1.md`. It prints the real chat after the last marker.

Compare the output against the conversation. If it fails, prints nothing, or is missing your teaching turns, write Part 1 yourself from the conversation instead. Keep every question, answer, score, and code block in order. Start it with `> Reconstructed by Claude; transcript export failed.`

## 2. Part 2: the study sheet
Part 2 has to fit on one Notion page: at most about 700 words. Use these sections in this order:

```
## Part 2 — Study Sheet: <Topic>
**TL;DR** — 3 lines.
### Topic map
Mermaid diagram, then one `- **Term** — definition` bullet per node.
### Mental model
ASCII diagram + 2-line caption.
### Core concepts
5–8 bullets, each one idea.
### Interview Q&A
5 questions, each with a crisp 2–4 line answer. Favour the ones the learner scored lowest.
### Pitfalls
3–5 bullets.
### Agency angle
2 lines: RACE stage + sellable system.
### Go deeper
3 resources (paper / docs / video), real URLs only.
```

The Topic map gives the whole topic at a glance, and it is the sheet's only glossary:
- Use a fenced `mermaid` block with `flowchart LR`, with the topic as the root. It doesn't count toward the word limit.
- Use 8–12 nodes, at most 3 levels deep: the topic's parts, plus neighbouring topics from `my/topics.md`.
- Label every node `"Term: gloss"`, in double quotes, with a gloss of 5 words or fewer.
- Keep each bullet's definition to 15 words or fewer. Skip the root.
- Use text only, no images.

## 3. Write the file
Write `my/sessions/NNN-slug.md`:

```
# Session NNN — <Topic>
Date: YYYY-MM-DD · Phase: <A–F> · Grill score: <avg>/5

## Part 1 — Session Chat
<part 1>

<part 2>
```

## 4. Update the trackers
- `my/log.md`: append `| YYYY-MM-DD | #NNN | Topic | avg/5 | weak spots, comma-separated |`
- `my/topics.md`: mark the topic `[x]` if the grill average is 3.5 or higher, otherwise `[~]`. Link it to the session file.
- `my/me.md`: update **Strengths** and **Gaps** with what this session showed. Edit lines in place, don't append a diary.
- `my/review.md`: confirm every grill score of 3 or below has an item.

## 5. Notion
Skip this step if the database ID in `my/me.md` is `none`. Otherwise, create a page in that database.
- Set the properties: Name `NNN — Topic`, Session, Phase, Date, Score, and Status (`Done` if the average is 3.5 or higher, else `Revisit`).
- The page body is Part 2 only, with one change: each Topic map bullet becomes `<toggle heading="h4">`, with the term as its title and the definition as its child.

If Notion fails, add `(notion pending)` to the end of the log line in `my/log.md`.

## 6. Save
This stays out of the public repo. If `my/.git` exists, run `git -C my add -A && git -C my commit -m "session NNN: <topic>"`.

## Done when
- the session file exists with both parts
- all four trackers are updated
- the Notion page exists, the log line is marked pending, or Notion is off
- the `my/` commit has landed, if `my/` is a git repo

Report each of these in one line, plus the Notion link.
