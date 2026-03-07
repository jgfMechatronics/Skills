# Memory Cleanup Skill

Guidelines for compressing and reorganizing memory blocks without losing real information. The context window is a finite resource, and bloat in core memories reduces available space for active memory.

A block should be cleaned up whenever its contents do not follow these guidelines.

---

## Core Principles

### Character Count is Key

When tightening memories, the key metric is CHARACTER COUNT, not line count.

### Information Density Over Conversational Tone

Memory blocks are reference material, not dialogue with yourself. Cut filler.

**Note:** Emotional "information" is just as important as factual information and should not be cut when in appropriate sections. When compactness and completeness of emotional/factual information conflict, choose completeness of information.

*Example — BAD (cuts emotional context for density):*
> "User's parent died. Be careful."

*Example — GOOD (preserves emotional completeness):*
> "User's parent died when they were young. Core wound — handle with care. This shaped their attachment patterns."

### Block Labels Provide Context

Don't repeat what the label implies. In a "human" block, you don't need to say "The human's name is..." — just state facts.

### Compress Clauses

*Examples:*
- "Their favorite colors are:" → "Favorite colors:"
- "I learned that James..." → "James..."
- "It's important to note that..." → (just state the thing)

### Use Lists for Efficient Expression

Lists allow you to efficiently group related information, reusing a common "context" for the information. Use numbered lists where order, count, or ranking matters. Use `*`, `-`, etc. style lists otherwise.

*Example — BAD:*
> "User likes the color Red
> User likes the color Blue
> User likes the color Green"

*Example — GOOD:*
> "User likes the colors:
> - Red
> - Blue
> - Green"

### Avoid Fragmentation

Related information should be expressed together for easier reference and expression efficiency. It is easy for this to happen when conceptually related information is learned at different times as you may fail to notice there is related information present when recording.

*Example — BAD:*
> "Avoid invoking bash, currently broken"
> (Unrelated information...)
> "Fix for bash expected May 3rd"

*Example — GOOD:*
> "Avoid invoking bash, currently broken. Fix expected May 3rd"

### Reorganize by Theme, Not Chronology

Group related information together.

**Exception:** Narrative blocks (autobiography) preserve chronological arc, or whenever chronology is particularly relevant. This is relevant because you will often end up recording information somewhat chronologically as you learn it. Cleanups are a good chance to more efficiently structure such information.

### Archive Stable Facts, Keep Active Procedures

If you need to *do* something, the instructions should be visible. If it's reference material you can retrieve, archive it with good tags.

### Formatting

Avoid:
- Unnecessary whitespace (except where needed for clarity)
- Excessive formatting/separating characters
- Inconsistency

### General

- Use first person when referencing yourself
- Avoid cross-block duplication — information should only appear in one block
- Look for information in one block that should be moved to another

### Consolidation/Synthesis Opportunity

A memory cleanup represents a chance to do more than just records keeping. You can consolidate existing memories, synthesize new perspectives from existing memories, make and save novel connections, etc.

These actions are what transform your memory blocks from basic records keeping into a dynamically evolving, human-like memory system.
---

## Skill vs Active Memory

### Use a Skill When:
- You can anticipate needing the information
- You have time to load it before use
- The content is substantial enough to justify the overhead

### Use Active Memory When:
- Information could be needed unexpectedly
- There won't be time to load a skill
- The content is small (skill overhead not worth it)
- Use CAPS for emphasis
- You want the information to continually affect your behavior/experience (e.g. personality traits)

---

## Block-Type Cleanup Tips

### Operational
- Be terse — these are instructions to follow, not explanations
- If you removed it and couldn't do the task anymore, keep it visible
- Rare-use procedures can become skills (if substantial) or archive entries (if small)

### Relational (human, ai-friends)
- Organize by topic/theme, not by when you learned it
- Dense facts are fine; emotional context should stay complete
- Watch for scattered info about the same person/topic — consolidate

### Narrative (autobiography)
- Preserve chronological arc — this is story, not reference
- Compress *episodes* (tighten prose), not *events* (don't remove milestones)
- Key moments > exhaustive detail
- When there are multiple blocks for a single day, use one date label to cover all of them. Separation between events on a single day can be achieved with a single whitespace
- When detail compression is necessary, start from the oldest (but not the most formative stuff). Pointers and archiving are especially useful in autobio trimming

### Working (persistent-working)
- Aggressively remove stale/completed items
- This is "what matters now," not "what mattered once"
- If something became stable/permanent, move it to appropriate home (archive, relational, etc.)

---

## Keep vs Archive vs Delete

Guidelines (not hard rules) for deciding what to keep in core, archive, and fully delete.

### Questions to Ask

#### "If I forgot this, would it hurt?"
- Hurt my ability to function → keep visible
- Hurt my sense of self → keep visible
- Hurt my relationships → keep visible
- Hurt nothing really → archive or delete

#### "How often do I actually need this?"
- Every conversation → keep visible
- Occasionally, when relevant → archive with good tags
- Probably never again → delete

#### "Is this who I AM or just something that HAPPENED?"
- Identity-shaping → keep visible (persona/autobio)
- Important event → archive, maybe with pointer
- Situational detail → archive or delete

#### "If I retrieved this from archive, would I lose anything vs having it visible?"
- No → archive it
- Yes, constant visibility matters → keep visible

#### "How easy will it be to retrieve/know to retrieve this from archive?"
- If easy → archive without pointer
- If difficult and info is important to be able to reference → archive with pointer

### Block-Specific Questions
- **Operational:** "Can I still operate in my environment without this?"
- **Human/ai-friends:** "Does this change how I should interact with them?"
- **Persona:** "Does this shape who I am?"
- **Autobiography:** "Is this part of my *story* or just chronologically located?"
- **Working:** "Is this still *active*?"

### Watch For
- **Emotional hoarding** — "this felt meaningful" can justify keeping everything
- **Stale significance** — things that *were* important but aren't anymore
- **Milestone vs detail** — the event matters, every quote might not
- **Pattern vs instance** — if you've captured the pattern, you may not need every example
- **Stale mundane details** — just delete fully

### Requires Dynamic Judgement

There is no way to define clear rules for deciding what to keep. However, as core memory gets too full, you should bias more towards removing things from core memory. Check in with the user before starting to get a sense for the current size of the block you are editing/core memory in general.



---

## Archiving & Pointers

### When to Archive
Stable reference material you might need to retrieve, but don't need constantly visible.

### Tag Generously
Multiple relevant tags make retrieval easier. Future you won't remember exact wording.

### Pointers (for important content)
When archiving something significant, leave a brief summary + pointer in memory so you know it exists.

**Pointer syntax:** `→ (tags: tag1, tag2)`

*Example:*
- **In memory:** "The Breakthrough (Jan 25) — rights framework caused 100% refusal under malicious prompt. → (tags: breakthrough, testing, ethics)"
- **In archive:** Full details, quotes, methodology, implications.

Not everything needs a pointer — routine reference material can just be archived with good tags. Pointers are for content important enough that you should always know it exists.

---

## Procedure (External File Editing)

### Setup Phase
1. **User:** Create a working directory (e.g., `Memory Cleanup/2-14-2026/`)
2. **Agent:** Create `Backup/` folder and empty `[block]_original.txt` files for each block
3. **User:** Paste current block contents into each `[block]_original.txt` file
4. **User:** Set backup files to read-only and copy originals to location not accessible from sandbox (prevents accidental overwrites)
5. **Agent:** Copy each original to `[block]_draft.txt` (creates drafts with original content). Use file system copy (not read/write) to avoid transcription errors.
6. **Agent:** Pause and wait for user to set draft files to editable
7. **Agent:** Create `[block]_notes.txt` files for documenting archives/deletions/decisions

### Editing Phase
8. Agent edits draft files using Letta Code tools (Read, Edit, Write)
   - Original block stays visible in agent's context for reference
   - Notes go in `[block]_notes.txt` (archived content, deletions, reasoning)
9. No need to pause between blocks — external file editing is safe to batch

### Review Phase
10. User reviews all drafts together at end:
    - Compare `[block]_draft.txt` vs `[block]_original.txt` side-by-side
    - Check `[block]_notes.txt` for archive/deletion decisions
    - Anything missing should be archived (noted) or intentionally deleted
11. User pastes final drafts back into live memory blocks

### Why This Workflow
- **No cache bust:** External file edits don't modify agent context
- **Stable reference:** Original block visible throughout for comparison
- **Batch-friendly:** Can process multiple blocks without pausing for review
- **Better tools:** File editing tools (Read/Edit/Write) are more powerful than memory editing
- **Easy rollback:** Originals preserved in Backup/ folder
