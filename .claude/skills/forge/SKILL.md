---
name: forge
description: Forge session material into final book text via draft, fresh-context critic, and rewrite passes. Use when the user says /اصهر, "forge", or at session close for material that passed the mastery gate.
---

# Forge

The production pipeline (CLAUDE.md). Input: only material that passed the mastery
gate this session. Output: FORGE-READY text appended to the correct `book/` chapter.

1. **Draft.** Write the section under the full Excellence Constitution, weaving in
   this learner's actual questions from the session and the relevant entries of
   `error-log.md` ("you might be thinking X here — you'd be in good company,
   because…"). The weave is this book's unfair advantage; never produce a generic
   textbook section.

2. **Critic.** Spawn a subagent with a **fresh context** containing ONLY:
   - the draft,
   - Articles 1–7 of the Excellence Constitution (copy them in),
   - the contents of `exemplars/`.
   It must not see this conversation. Mandate, verbatim:

   > "Judge this draft article by article. For every violation, cite the article
   > number, quote the offending passage, and state what repair is required. Then
   > place the draft against the exemplar passages and name every way it falls
   > short of them. Be merciless; flattery is a failure mode. End with a verdict:
   > FORGE-READY or RETURNED."

3. **Rewrite.** Repair every cited violation. Return to step 2.

Constraints: minimum **two** critic passes even if the first verdict is
FORGE-READY; append to `book/NN-*.md` only on a FORGE-READY verdict; show the
learner the final verdict and one-line summary of what each pass changed.
