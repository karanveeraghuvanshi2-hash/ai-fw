# Curriculum: 50 topics

Weighted for an **Applied AI Engineer** job plus an **AI consulting agency**. At about 4 sessions a week, this runs about 13–15 weeks. `/setup` reorders it around your goals and gaps.

Status: `[ ]` not started · `[~]` in progress or needs a revisit · `[x]` done (grill score of 3.5 or higher). Link each finished topic to its session file.
New topics come from `suggested.md`.

## A. Foundations: how LLMs actually work
- [ ] 1. How LLMs work end to end (next-token prediction, training vs inference)
- [ ] 2. Tokenization (BPE, why tokens drive cost and odd failures)
- [ ] 3. Neural net basics: loss, gradient descent, backprop (micrograd)
- [ ] 4. Embeddings and vector similarity
- [ ] 5. Transformers and attention
- [ ] 6. Pretraining → SFT → RLHF / DPO / RLVR
- [ ] 7. Sampling and decoding (temperature, top-p, determinism)
- [ ] 8. Context windows, KV cache, long context
- [ ] 9. Reasoning models and test-time compute
- [ ] 10. Model landscape and selection (cost, latency, quality, open vs closed)

## B. Building with LLM APIs
- [ ] 11. Python for AI engineering (uv, async, pydantic, notebooks)
- [ ] 12. LLM API fundamentals and streaming
- [ ] 13. Prompt engineering
- [ ] 14. Context engineering
- [ ] 15. Structured outputs (JSON schema, validation, retries)
- [ ] 16. Tool use / function calling
- [ ] 17. Prompt caching, cost and latency optimization
- [ ] 18. Multimodal: vision, PDFs, audio
- [ ] 19. AI UX: streaming and generative UI (Vercel AI SDK)

> **Build P1: Speed-to-lead agent** (Acquire). An inbound lead gets classified and a personalized reply drafted in under 5 minutes. Next.js, the Claude API, and a streaming UI.

## C. RAG
- [ ] 20. RAG fundamentals, and when not to use RAG
- [ ] 21. Document parsing and chunking
- [ ] 22. Vector DBs and hybrid search (pgvector, BM25)
- [ ] 23. Reranking and query transformation
- [ ] 24. Advanced RAG: contextual retrieval, agentic RAG, GraphRAG

> **Build P2: SOP / sales-enablement RAG** with an eval harness (recall@k, faithfulness).

## D. Agents
- [ ] 25. The agent loop and ReAct
- [ ] 26. Workflow vs agent patterns (routing, orchestrator-workers, evaluator-optimizer)
- [ ] 27. Agent memory
- [ ] 28. Multi-agent systems
- [ ] 29. MCP (Model Context Protocol)
- [ ] 30. Agent frameworks: Claude Agent SDK, OpenAI Agents SDK, LangGraph
- [ ] 31. Computer and browser use
- [ ] 32. Claude Code as a platform (skills, hooks, routines, subagents)
- [ ] 33. Agent reliability: guardrails, budgets, human-in-the-loop

## E. Evals and production
- [ ] 34. Eval fundamentals and datasets
- [ ] 35. LLM-as-judge and calibration
- [ ] 36. Observability and tracing (Langfuse / LangSmith)
- [ ] 37. AI security: prompt injection, PII, jailbreaks
- [ ] 38. Deployment: serverless, queues, Modal / Trigger.dev
- [ ] 39. Open models and local inference (Ollama, vLLM, quantization)
- [ ] 40. Fine-tuning and LoRA: when to, when not to
- [ ] 41. Voice AI agents
- [ ] 42. LLM system design interview framework

> **Build P3: Outbound-research or ad-creative agent** (Reach/Convert). MCP, deployed as a scheduled routine, with evals and tracing.

## F. Agency and career
- [ ] 43. n8n / Make / Zapier vs code
- [ ] 44. Theory of Constraints and the RACE bottleneck audit
- [ ] 45. Goal factoring → automation roadmap
- [ ] 46. AI lead generation and outbound (Clay, enrichment, personalization)
- [ ] 47. AI sales and CRM automation (speed-to-lead, follow-ups, call analysis)
- [ ] 48. Scoping, pricing, ROI, and guarantees
- [ ] 49. Client rollout: team accounts, skills sync, change management
- [ ] 50. Portfolio, personal brand, and the AI job hunt

> **Build P4: Bottleneck Audit web app.** It walks an owner through RACE, computes the funnel, flags the bottleneck, goal-factors the fix, and drafts a proposal. This becomes the agency's lead magnet.

**Tip:** run topics 44–45 early, around week 3, alongside phase B, so agency outreach can start while learning continues.
