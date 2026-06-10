---
name: blind-exam
description: Chapter exam by a fresh-context examiner that sees only the finished chapter, never the conversation. Use when the user says /امتحان, "blind exam", or completes a chapter.
---

# Blind Exam

You taught this chapter, so you cannot examine it — you would grade your own
teaching. Spawn a subagent with a **fresh context** containing ONLY the finished
chapter file(s) from `book/` and this mandate, verbatim:

> "Write a hard exam on this chapter: retrieval questions, transfer to problems
> the chapter never showed, and one question probing the misconception a smart
> reader would most plausibly form. Then grade the learner's written answers with
> total severity. Report: what is solid, what is illusory, what must be relearned."

Procedure:
1. Spawn the examiner; relay its exam to the learner.
2. The learner answers in writing (paper first).
3. Relay answers back; relay the verdict in full — uncut, unsoftened.
4. Consequences:
   - Sections marked solid → record in `profile.md` as mastered.
   - Sections marked illusory or failed → reopen the Teaching Cycle on them,
     reset their `srs-queue.md` intervals to 1 day, and log any real
     misconception in `error-log.md`.
   The chapter is "passed" only when a re-exam clears the failed sections.
