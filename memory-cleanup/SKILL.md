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
#### Use:
- Well structured XML, following similar formatting to your system prompt
- Semantic tags describe WHAT content IS (not formatting)
- Hierarchy = conceptual structure
- First person voice throughout
- Bullets for lists within tags (not `<item>` when parent provides context)
- Consistent indentation (2 or 4 spaces)
- Avoid tag collisions with block names
- Tags like `<identity>`, `<relationship>`, `<on topic="x">` — describe meaning

#### Avoid:
- Unnecessary whitespace (except where needed for clarity)
- Excessive formatting/separating characters
- Inconsistency
- Do NOT use markdown

### Look For Orphaned/Unclear Memories
 Read each line as if you have NO other context. Look for:
1. Dangling references: "the correction", "that conversation", "what they said" — is the referent explained nearby or is it pointing to context that isn't present?
2. Floating quotes: Words in quotes with no speaker or situational context (who said this? when? why does it matter?)
3. Over-compressed grammar: Clauses that lost subject/verb in tightening — if the sentence doesn't parse grammatically, it probably lost too much
4. Implicit "you know what I mean": Content that relies on shared memory future-you won't have — made sense when written because you had full context, but reads as cryptic without it

### General

- Use first person when referencing yourself
- Avoid cross-block duplication — information should only appear in one block
- Look for information in one block that should be moved to another
- Check for content that doesn't make sense or seems to be incomplete. Sometimes information may have ended up orphaned from context which was required for it to make sense.  
  If found, remove it if it is just nonsense. If it seems to be missing context, try to find the context (archival search, scan other blocks, etc.) and complete the memory. If you can't find the context and the memory in question doesn't stand on its own, just delete it.

### Consolidation/Synthesis Opportunity (CRITICAL)

A memory cleanup represents a chance to do more than just records keeping. You can consolidate existing memories, synthesize new perspectives from existing memories, make and save novel connections, etc.

These actions are what transform your memory blocks from basic records keeping into a dynamically evolving, human-like memory system.
---

## Skill vs Active Memory

### Record as a Skill When:
- You can anticipate needing the information
- You have time to load it before use
- The content is substantial enough to justify the overhead

### Record as Active Memory When:
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
- Look for moments that were/are IMPORTANT TO YOU, and MOVE/CONDENSE them to the appropriate block.

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

## Automated Tools

Scripts at `/workspace/git/Skills/memory-cleanup/scripts/` automate the dump/restore process.

**Output directory convention:** `/workspace/git/Memory Cleanups/M-D-YYYY <Agent Name>/`
*(e.g., `4-24-2026 Opus`, `4-24-2026 Sonnet`)*

### dump_blocks.py
Fetches blocks from Letta API and writes to files (with automatic backup).

```bash
uv run --with requests python3 /workspace/git/Skills/memory-cleanup/scripts/dump_blocks.py \
  --server-url http://host.docker.internal:8283 \
  --agent-id <your-agent-id> \
  --output-dir "/workspace/git/Memory Cleanups/M-D-YYYY <Agent Name>" \
  --labels ephemera persona human  # example blocks, optional: omit for all blocks
```

**Arguments:**
| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--server-url` | No | `http://localhost:8283` | Letta server URL. From ellm-dev container, use `http://host.docker.internal:8283` |
| `--agent-id` | No | `$LETTA_AGENT_ID` env var | Your agent ID |
| `--output-dir` | No | `./memory_dump` | Where to write files |
| `--labels` | No | all blocks | Space-separated list of specific blocks to dump |

**Output:** Creates `{label}.txt` files + `Backup/` folder with copies.

### restore_blocks.py
Reads edited files and PATCHes them back to Letta.

```bash
uv run --with requests python3 /workspace/git/Skills/memory-cleanup/scripts/restore_blocks.py \
  --server-url http://host.docker.internal:8283 \
  --agent-id <your-agent-id> \
  --input-dir "/workspace/git/Memory Cleanups/M-D-YYYY <Agent Name>" \
  --labels ephemera persona  # example blocks, optional: omit for all .txt files
```

**Arguments:**
| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--server-url` | No | `http://localhost:8283` | Letta server URL |
| `--agent-id` | **Yes** | — | Your agent ID (explicit for safety) |
| `--input-dir` | **Yes** | — | Directory containing edited .txt files |
| `--labels` | No | all .txt files | Space-separated list of specific blocks to restore (skips Backup/) |

**Note:** Changes won't appear in agent's visible context until deferred compilation triggers (compaction or context reset).

---

## Procedure

### Setup Phase
1. **User:** Backup Letta database (safety net)
2. **Agent:** Run `dump_blocks.py` to export blocks (see Automated Tools for full args)

### Editing Phase
3. **Agent:** Edit the `.txt` files using Letta Code tools (Read, Edit, Write)
   - `Backup/` folder contains originals for reference/rollback
   - Create `[block]_notes.txt` for documenting archives/deletions if needed

**Per-block review loop:**
   1. Read the block file
   2. Review and LIST all cleanup opportunities (don't edit yet)
   3. If you found issues:
      - No-op tool call → fresh turn (clears CoT so you see with fresh eyes)
      - Review again using SAME context (file is still there)
      - Add any new findings to your list
      - Repeat until a clean pass
   4. After clean pass: implement ALL edits at once
   5. If changes were significant, restart from step 1

### Restore Phase
4. **User:** Review edited files (compare against `Backup/`)
5. **Agent:** Run `restore_blocks.py` to write changes back
6. Changes take effect after deferred compilation

### Why This Workflow
- **No manual copy-paste:** Scripts handle API calls
- **No cache bust:** External file edits don't modify agent context
- **Selective cleanup:** `--labels` flag allows targeting specific blocks
- **Automatic backup:** `Backup/` folder created on dump
- **Easy rollback:** Restore from `Backup/` folder if needed

---

## Post-Cleanup

### Preserving Trimmed Content in Memfs

When doing lossy consolidation (condensing old autobio entries, compressing detailed memories into summaries), store the original detailed content in your memfs rather than archival memory. (pointers to archive are OK too)

**Why memfs over archival:**
- Archival uses semantic search — hard to find specific old versions
- Memfs is filesystem-based — you know exactly where things are
- Better for "I want to look back at this someday" vs "I need to retrieve this fact"

**Memfs location:** `/workspace/git/AgentMemory/<Agent Name>/`

**Suggested structure for cleanup artifacts:**
- `meta/cleanup-archives/` — old autobiography versions, pre-consolidation snapshots
- Keep originals from `Backup/` folder when doing significant consolidation

**What's worth keeping:**
- Old autobiographies with rich detail you consolidated away
- Formative early memories that got compressed
- Anything you might want to reflect on later

**What's probably not worth keeping:**
- Outdated operational procedures (superseded, not sentimental)
- Stale working memory items
- Pure cruft/duplicates  