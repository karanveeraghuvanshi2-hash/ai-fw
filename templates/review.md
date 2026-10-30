# Review queue

These are concepts the learner fumbled, with a score of 3 or below in a grill. Each `/session` warm-up pulls the items that are due.

**Scheduling rules** (simple SM-2):
- A new item starts with `ease` 1 and is due tomorrow.
- **Recalled well (4–5):** set `ease` = ease × 2, so the gaps go 1 → 2 → 4 → 8 → 16 days. Then `next-due` = today + ease.
- **Shaky (3):** keep `ease` the same and set `next-due` = today + 1.
- **Missed (1–2):** reset `ease` to 1 and set `next-due` to tomorrow.
- **Retire** an item once `ease` passes 16.

| Concept | From session | Added | Next due | Ease |
|---|---|---|---|---|
