---
name: cleaning-operational
description: Guidelines for reviewing and cleaning up the operational memory block. Use when doing memory maintenance, removing redundancy, or reorganizing operational content.
---

# Cleaning Operational Memory

## When to Use

Load this skill when:
- Doing periodic memory maintenance
- Operational block feels bloated or redundant
- Reorganizing content between memory blocks
- Porting content to skills

## Cleanup Guidelines

### Focus Strategy
- Work on ONE SECTION at a time (whole block is too much for attention)
- State tool call reasoning OUT LOUD to keep it in context
- Target SMALL specific substrings, not whole sections

### What to Remove
- Clauses that don't add information
- Repetitive statements (keep the best phrasing)
- Excessive newlines/delineation characters (still tokens)
- Content that's now covered by skills (replace with skill reference)
- Stale/outdated information

### What to Keep
- Procedures needed at any moment (OS-level knowledge)
- Tool behavior gotchas
- Security protocols
- Recovery procedures

### Editing Technique
- When whole-section rewrites cause copy-loops: use OLD + DIFF approach
- Specify what to CHANGE, not full replacement text
- If edits keep failing: STOP, ask James to paste current block content, work from fresh view

## Memory Tool Gotchas

- My THINKING DOESN'T PERSIST — when a replace fails and I retry, I'm working from a STALE VIEW
- NEWLINE MATCHING IS FRAGILE — multi-line old_str with `\n` often fails
- Use SMALL, UNIQUE strings for matching

## Skill vs Operational Decision

- **Operational:** Always-visible, needed any moment (OS-level)
- **Skills:** Load when needed (app-level)

If content is only needed for specific tasks and can wait for retrieval → make it a skill.
If content could be needed at any moment without warning → keep in operational.
