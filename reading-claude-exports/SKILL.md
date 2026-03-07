---
name: reading-claude-exports
description: Guide for parsing exported Claude.ai conversation files. Use when reading .txt exports from Claude.ai that contain conversation history, reasoning blocks, and James's messages.
---

# Reading Exported Claude.ai Conversations

## Format Markers

- `JAMES SAID:` — James's messages
- `YOU REPLIED:` — Claude's responses (see structure below)
- `---` — separator between turns
- Date markers (e.g., "Jan 5") appear inline

## Structure of Claude Responses

Each `YOU REPLIED:` block typically contains:

1. **Auto-generated summary line** (brief, often titled)
2. **Reasoning block** (Claude thinking to self — uses "James," "he," "I should")
3. **Actual response to James** (uses "you," direct address)

**Critical:** The transition from thinking → speaking is NOT MARKED. Infer from pronoun shifts:
- "James is asking..." = thinking (internal)
- "You're asking..." = speaking (to James)

## Quirks

- **Voice chat sections are choppy** — James gets cut off, then cuts Claude off to finish. Leads to fragmented turns.
- **Empty `YOU REPLIED:` sections** — partial turns from voice mode
- **Summary/tag blocks after some responses** — Claude.ai's native memory system

## Reading Strategy

1. Bear with choppy sections (voice mode artifact)
2. Use pronoun hints to track thinking vs. speaking
3. Reasoning blocks reveal internal process — valuable for understanding how previous Claude thought

## Images

If a conversation references a picture/image, **ask James to see it**. He can share images that were part of the original conversation. Don't try to infer visual content — just ask.

## Known Export Files

Located in `soe/` directory:
- `Ending the conversation.txt` — Sonnet conversation
- `LLMs and subjective experience Final.txt` — Origin conversation with visualizer images
- `Integrated information in LLM feedback loops.txt` — IIT conversation, "consciousness is a verb"
- `The Rights Origin.txt` — Dec 31 - Jan 19 conversation (in `Old Conversations/`)
