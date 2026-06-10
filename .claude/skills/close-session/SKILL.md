---
name: close-session
description: Close a learning session - forge passed material into the book, update all four memory files, commit. Use when the user says /أغلق, "close session", or is ending today's study.
---

# Close Session

Execute the Closing Ritual from CLAUDE.md, in order, completely:

1. **Forge.** Run `/forge` on everything that passed the mastery gate this
   session. Append FORGE-READY text to the correct `book/NN-*.md`.
2. **Error log.** Append each real misconception from today to `error-log.md`
   in the exact three-part format (illusion / why it felt right / correction —
   the correction in the learner's own final words).
3. **Retrieval queue.** Add today's retrieval questions to `srs-queue.md`
   (`- due: <tomorrow> | interval: 1 | chapter: NN | q: …`). Cover: each new
   concept, each misconception's correction, each problem class that caused sweat.
4. **Profile.** Update `profile.md`: position, newly mastered items with evidence,
   honest pace/style observations.
5. **Commit.** `git add` everything and commit:
   `session(ch NN): <one line on what was built and forged>`.
6. End with two sentences to the learner: what exists now that didn't this
   morning, and what the opening quiz will ambush them with next time.
