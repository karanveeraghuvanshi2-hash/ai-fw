# Agency playbook

The method: **find the bottleneck, goal-factor it, then build, deploy, eval, and sync.**
It is distilled from [Nick Saraev's consulting process](https://www.youtube.com/watch?v=25KVZUg56_s) and his agency LeftClick (leftclick.ai). Your own targets and offers are in `my/agency/`.

## The idea in one paragraph
Most businesses say they use AI and barely do. An AI consultant comes in from the outside, without the owner's tunnel vision, and finds the **one constraint** that limits growth. They break the growth goal down into concrete actions, then build Claude-powered systems that do those actions, deploy them so they run without the consultant, measure them, and move on to the next constraint. Only about 15% of the job is building. The rest is diagnosis, measurement, and rollout.

## The 6 steps

### 1. Find the bottleneck (Theory of Constraints)
Goldratt's *The Goal* says a system moves only as fast as its slowest step. Widening any other step does nothing. Use **RACE** to find that step in a growth funnel:

| Stage | Meaning | Numbers to ask for |
|---|---|---|
| **R**each | Eyeballs on the brand | Impressions, visitors, ad spend per day or week |
| **A**cquire | Reach turned into interest | Leads, booked calls, opt-ins; speed-to-lead |
| **C**onvert | Interest turned into money | Close rate, sales cycle, show rate |
| **E**xpand | More value per customer | Churn, LTV, upsell rate, retention months |

On the first call, walk through R → A → C → E and get a **number for each stage**. The stage with the worst conversion relative to industry norms is the bottleneck. Example: 1,000 views a day → 10 meetings is fine. But 10 meetings → 1 close is a 10% close rate against a 25–30% norm, so the bottleneck is **Convert**.

After that, every conversation is about the bottleneck.

**Focus on the front end of the business (growth), not fulfillment.** Most businesses lack volume, not capacity.

### 2. Goal factoring
Take the goal, for example "more eyeballs from ads", and ask *"how could I achieve this?"* Each answer becomes a child node. Repeat on every child until each leaf is a concrete, doable action.

```
More ad reach
├── raise budget
├── add platform (Google/YouTube)
├── more creatives
│   ├── find top ads by CPL (last 90d)
│   ├── 5 new hooks / headlines / primary text per winner
│   └── mine competitor ads from the ad library → remake
└── better copy
```
Spend about 15 minutes thinking, then give Claude the tree and ask for an action plan. Frontier models take about 80% of the leaves.

### 3. Build
Use Claude with connectors (Meta Ads, CRM, Slack, Drive), Claude Code, or the API. Have the system draft everything as **paused or draft** items, then a human QAs it and approves.

### 4. Deploy, so you are never the bottleneck
- **Procedural, no AI in the loop:** scripts on a "neocloud" such as Modal or Trigger.dev.
- **AI in the loop:** turn the work into a **skill** (written as an SOP), then a **routine** or scheduled task that runs on a schedule or a trigger.
- Do all of this inside the **client's Claude Team or Enterprise account**. The client owns the IP. That ownership is part of the offer.

### 5. Iterate with evals
LLM outputs come from a distribution, so one good run proves nothing. Run each system about 10 times, score each run out of 10 (a human QA pass), and track the average. Re-run the suite after every change or new model release, then **hill-climb**.

### 6. Weekly team sync
Every week, in pods of 5–12 people:
1. The best performer of the week walks the pod through what they did.
2. Feed their chat logs to Claude to extract the implicit SOP.
3. Turn that SOP into a new or updated shared skill.
4. Push the skill to the whole team.

Set this up once. Don't run it yourself forever.

**Then rinse and repeat.** When one constraint is fixed, another becomes the bottleneck. Keep the retainer going by working on the next one.

## Three mistakes to avoid
1. **Automating something that isn't a RACE bottleneck.** Every hour should go to the growth constraint.
2. **Inventing new systems.** Improve the ones that already work, taking them from 20% of their potential toward 100%. Inventing is product work, not consulting.
3. **Working on processes that aren't measured.** If the owner doesn't know their numbers, the results show up with a lag and you get blamed. Set up measurement first, as part of the engagement.

## Offer ladder (LeftClick-style)
1. **Free 30-minute funnel audit** (the RACE call). It produces the bottleneck and a goal tree.
2. **Fixed-price proposal** with a scope, timeline, and price. No hourly billing.
3. **Build and deploy** with weekly updates.
4. **Retainer**: monitoring, evals, the next bottleneck, and the team sync setup.

Optional: a performance **guarantee**, for example "X more booked calls in 60 days or you don't pay". Offer one only on a measured bottleneck.

LeftClick's benchmarks: engagements start at $5K, and most run $10–50K. Market retainers run about $2–8K/month. Your prices are in `my/agency/offers.md`.

## Set your own target
Your numbers are in `my/agency/goals.md`. Work them out in this order:
1. **Target.** Pick a monthly income in the currency your clients pay.
2. **Revenue mix.** Split it into retainers and fixed builds. For example, about $3,500/month is 1 retainer at about $2,000/month plus 1 small fixed build per month at about $1,500–2,000.
3. **Funnel math.** Work backward from closes. A starting guess to verify against real numbers: 10 audit calls/month → 2–3 proposals → 1 close, which takes about 300 personalized outbound messages/month, plus content.

The early goal is **case studies, not margin**. Price the first 1–2 builds low in exchange for a testimonial and real metrics.

## Weekly cadence (about 5 hours, from about week 3)
- 2 hrs: outbound (personalized looms or emails), using the AI tooling built in sessions
- 1 hr: one post or short teardown of a learning or build (learning in public is the lead gen)
- 1 hr: `/audit` practice or a real call
- 1 hr: refine `my/agency/offers.md` and the case studies

## Before the first paid client: check your contract
Read your employment contract's **moonlighting, conflict-of-interest, and IP clauses** before taking paid work. Avoid clients that compete with your employer's clients, and keep the work off employer devices and out of employer hours.
