# ai-fw

An AI gym that runs inside [Claude Code](https://claude.com/claude-code). Claude is your tutor and your interviewer. Work through 50 topics toward an **Applied AI Engineer** job, an **AI consulting agency**, or both, with goals you set yourself.

Every session works the same way:

1. **Teach.** Claude explains the topic from first principles.
2. **Grill.** Interview-style questions, each scored 1–5. Weak answers come back for spaced review.
3. **Build.** A small exercise that grows into a portfolio project.

## Start
1. Click **Use this template** at the top of this page, then clone your copy.
2. Open the folder in Claude Code.
3. Run `/setup`.

`/setup` interviews you about your background and goals, including your agency income target, market, and hours. It then writes your profile, works out the funnel math for your target, and reorders the curriculum around your gaps.

## Commands
```
/setup              # first run: your profile and goals
/session 1          # or /session "RAG fundamentals"
/wrap               # save the session and update your trackers
/mock "Series B startup"
/audit random       # practice an AI-consulting bottleneck audit
```

## Your data stays local
Everything about you goes in `my/`, which is gitignored: your profile, scores, session notes, builds, income targets, and clients. Only the framework is tracked, so you can pull updates or send improvements without exposing any of it.

For a backup, `my/` is its own git repo. Add a **private** remote to it:
```
git -C my remote add origin <your-private-repo-url>
git -C my push -u origin HEAD
```

## Map
| Path | What it is |
|---|---|
| `CLAUDE.md` | Claude's tutor instructions |
| `.claude/skills/` | The commands |
| `templates/` | Blank copies of everything in `my/` |
| `agency/playbook.md` | The consulting method: find the bottleneck, goal-factor it, automate it |
| `raw/research.md` | The research behind the design |
| `tools/export_session.py` | Turns a Claude Code transcript into a session's chat section |
| `my/` | Your private data, created by `/setup` |

## Optional: Notion study sheets
`/setup` can create a Notion database and `/wrap` adds a one-page study sheet to it after each session. Each sheet opens with a topic map: a diagram of the topic and its neighbours, with short definitions in toggles. It uses the Notion MCP:
```
claude mcp add --transport http notion https://mcp.notion.com/mcp
```

## Credits
The agency method is distilled from Nick Saraev's public [AI consulting video](https://www.youtube.com/watch?v=25KVZUg56_s). This project isn't affiliated with him or with LeftClick. Sources are in `raw/research.md`.

## License
[MIT](LICENSE)
