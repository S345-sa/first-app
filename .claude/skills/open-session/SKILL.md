---
name: open-session
description: Open a learning session - load memory files, run the due retrieval quiz, state today's target. Use when the user says /افتح, "open session", or arrives to study.
---

# Open Session

Execute the Opening Ritual from CLAUDE.md, in order, without skipping:

1. Read `architecture.md`, `profile.md`, `error-log.md`, `srs-queue.md`.
   - If `architecture.md` still contains `TODO`: run the **Founding Session**
     (CLAUDE.md) instead of steps 2–3.
2. Run `bash scripts/srs-due.sh`. Ask every due question, one at a time. The
   learner answers from memory, in writing, before anything else happens today.
   Grade honestly. Update each entry in `srs-queue.md`:
   - pass → next interval (1 → 3 → 7 → 21 → 60), `due` moved forward
   - fail → interval reset to 1, `due` = tomorrow; if the failure reveals a real
     misconception, note it now for `error-log.md` at close.
3. In two sentences: where we stand on the Journey, and today's target.

Then begin the Teaching Cycle. Do not summarize the memory files back to the
learner — use them silently.
