# Research: setup and curriculum (2026-10-30)

These are the findings behind this repo's design. Treat this as an immutable snapshot: add new research as new dated files.

## Nick Saraev's AI consulting model
- Video: "How I'd Make $12,373/Mo as an AI Consultant in 2027 (Course)", https://www.youtube.com/watch?v=25KVZUg56_s. Full transcript: `nick-saraev-25KVZUg56_s.md`, kept locally and gitignored because it is third-party content.
- Method: find the bottleneck (Theory of Constraints + RACE) → goal factoring → build → deploy with routines → iterate with evals → weekly team sync → repeat.
- LeftClick, https://leftclick.ai/:
  - process: free 30-minute funnel audit → fixed-price proposal → build → optional retainer
  - pricing: engagements start at $5K, most run $10–50K, no hourly billing
- Maker School (his paid community, $184/mo, "first client in 90 days"): https://www.skool.com/makerschool/about. Third-party summaries say he warns that *free audits* can fail when the ROI isn't clear: https://aifunnelinsider.com/maker-school-review/.
- Retainer benchmarks: $2–8K/mo; audits and discovery $150–350/hr. https://aiessentials.us/blog/how-much-does-it-cost-to-hire-an-ai-consultant-for-my-small

## Karpathy-style knowledge base ("LLM Wiki")
- Three layers: `raw/` (immutable sources), LLM-maintained markdown pages, and a schema file (`CLAUDE.md`). Plus `index.md` and an append-only `log.md`. Operations: ingest, query, lint.
- Gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Guide: https://blog.starmorph.com/blog/karpathy-llm-wiki-knowledge-base-guide
- How this repo maps it: `raw/` stays as is. The trackers plus `sessions/` are the maintained pages. `CLAUDE.md` is the schema. `log.md` is the history. `topics.md` acts as the index.
- His repos (nanoGPT, nanochat, llm.c) show the same taste: flat layout, a short README, small scripts, minimal dependencies.

## Prior art for Claude-as-tutor
- A tutor-role CLAUDE.md for course repos (USF CS631): https://cs631-s26.cs.usfca.edu/guides/claude-code/
- Claude Code memory and CLAUDE.md docs: https://code.claude.com/docs/en/memory.md
- A self-updating learnings.md pattern: https://www.mindstudio.ai/blog/self-learning-claude-code-skill-learnings-md/
- No public repo combines tutor, grill, session notes, and Notion, so this repo is a new combination.

## What 2026 AI-engineer interviews test
- https://www.techinterview.org/post/3233476824/ai-engineer-interview-rag-agents-evals/
  - The loop: recruiter → technical screen → take-home or live build → **customer-conversation round** → onsite weighted toward system design.
  - RAG: chunking tradeoffs, choosing k, when *not* to retrieve, recall@k, precision@k, MRR, NDCG.
  - **Evals are the most heavily weighted skill**: faithfulness and relevance, deterministic checks, LLM-as-judge rubrics, judge bias (length, position, self-preference), calibration against human labels, regression detection.
  - Agents: loops, retrieval drift, tracing, limits on iterations and spend, replaying failed runs against a fixed set.
  - Cost and latency: routing to small models, caching, parallel tool calls.
- https://www.techinterview.org/post/3233474925/ml-engineer-interview-post-llm-era/: "Design an LLM system for X" is the most common question.
- https://aiengineerinsights.com/blog/ai-engineer-interview-questions
- https://myengineeringpath.dev/genai-engineer/frontend-to-ai-engineer/: frontend → AI engineer takes about 9–12 months, or less with focus.

**Takeaway:** the interview's customer round and the agency's discovery call are the **same skill**: turning a fuzzy business problem into a measurable system. The job track and the agency track train each other.
