---
name: setup
description: First run. Create my/ from the templates, interview the learner, and fill in their profile and agency goals.
disable-model-invocation: true
---

# Setup

## 1. Create `my/`
Run:

```
mkdir -p my/sessions my/projects my/agency/audits
cp -Rn templates/. my/
git -C my init -q
git check-ignore my
```

The last command must print `my`. Existing files are kept, so a rerun updates them.

## 2. Interview
Ask one question at a time, and wait for each answer:
1. Name, and what to call them.
2. Background: years of experience, role, stack, languages, relevant projects.
3. Job goal: target role and timeline, or none.
4. Agency goal: yes or no. If yes, ask for:
   - monthly income target, with currency
   - by when, and why that number
   - client region, and niche if they have one
   - clients that would conflict with their employer
   - hours a week for the agency
5. Pace: hours a week for all of this.
6. What they already know well, and where they feel weakest.
7. Notion study sheets: yes or no.

## 3. Write
- `my/me.md`: fill in every section. Write gaps from the answers, not from a guess.
- `my/agency/goals.md`: fill it in, working the revenue plan and funnel math with the steps in `agency/playbook.md` ("Set your own target"). Show the learner the funnel math. If the target doesn't fit their hours, say so and offer a smaller target or a later date.
- `my/topics.md`: move topics they need soonest up within their phase, and mark topics they already know `[x]`. Without an agency goal, delete phase F and the P4 build.
- Notion: if yes, check the Notion tools are connected. If they aren't, give them `claude mcp add --transport http notion https://mcp.notion.com/mcp`, then `/mcp` to sign in. Create the database with the properties in `CLAUDE.md` and put its ID in `my/me.md`. If no, leave the ID as `none`.

## Done when
Every section of `my/me.md` is filled in, `my/agency/goals.md` is complete or the learner has no agency goal, and they've seen the funnel math. Then suggest their first `/session`.
