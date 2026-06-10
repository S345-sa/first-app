# Spaced-Retrieval Queue

> One line per question. Read at the start of every session: every entry with
> `due` ≤ today is asked BEFORE any new material (Procedures Constitution, rule 5).
> `bash scripts/srs-due.sh` prints today's due questions.
>
> Interval ladder: 1 → 3 → 7 → 21 → 60 days.
> Pass → promote to the next interval and move `due` forward.
> Fail → reset interval to 1, and consider an `error-log.md` entry.
> Questions only — never store the answer next to the question.

<!-- Entries below. Format (exact, machine-parseable):
- due: YYYY-MM-DD | interval: 1 | chapter: 01 | q: <the question>
-->
