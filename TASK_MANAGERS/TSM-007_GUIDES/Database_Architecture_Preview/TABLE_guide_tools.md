# TABLE: guide_tools

**Purpose:** Links guides to specific tools in the technology stack
**Relationships:** Junction table connecting `guides` to tools registry

---

## Table Schema

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| `id` | MEDIUMINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| `guide_id` | MEDIUMINT UNSIGNED | FOREIGN KEY, NOT NULL | References guides.id |
| `tool_id` | SMALLINT UNSIGNED | FOREIGN KEY, NOT NULL | References tools.id |
| `usage_context` | VARCHAR(200) | NULL | How tool is used in guide |
| `is_primary_tool` | BOOLEAN | DEFAULT FALSE | Primary tool covered by guide |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | When link was created |

---

## Sample Data

| id | guide_id | tool_id | usage_context | is_primary_tool |
|----|----------|---------|---------------|-----------------|
| 1 | 10 | 5 | Whisper Flow for recording activity transcripts | TRUE |
| 2 | 10 | 1 | Claude for processing daily reports | FALSE |
| 3 | 10 | 2 | Gemini for alternative report generation | FALSE |
| 4 | 11 | 1 | Claude for entity classification assistance | TRUE |
| 5 | 11 | 2 | Gemini for taxonomy suggestions | FALSE |
| 6 | 11 | 15 | Miro for visualizing entity hierarchies | FALSE |
| 7 | 12 | 1 | Claude for template analysis | TRUE |
| 8 | 9 | 10 | Gamma for presentation creation | FALSE |
| 9 | 9 | 4 | Firefly for image generation | FALSE |
| 10 | 3 | 4 | Firefly for designer workflow | TRUE |
| 11 | 3 | 6 | Runway for video/animation | FALSE |

---

## Tool Reference Table (Partial)

| tool_id | tool_name | category | vendor |
|---------|-----------|----------|--------|
| 1 | Claude | AI Assistant | Anthropic |
| 2 | Gemini | AI Assistant | Google |
| 3 | ChatGPT | AI Assistant | OpenAI |
| 4 | Firefly | Image Generation | Adobe |
| 5 | Whisper Flow | Transcription | Custom |
| 6 | Runway | Video/Animation | Runway ML |
| 7 | Lovable | Development Platform | Lovable |
| 10 | Gamma | Presentation | Gamma |
| 15 | Miro | Whiteboard | Miro |
| 16 | Notion | Documentation | Notion |

---

## Tool Coverage by Guide

| Guide Code | Guide Name | Tools Linked | Primary Tool | Secondary Tools |
|------------|------------|--------------|--------------|-----------------|
| GDS-010 | Quick Start PMT-032 | 3 | Whisper Flow | Claude, Gemini |
| GDS-011 | Entity Mapping Tutorial | 3 | Claude | Gemini, Miro |
| GDS-012 | Template Cross-Reference | 1 | Claude | - |
| GDS-009 | SMM Communication Templates | 2 | - | Gamma, Firefly |
| GDS-003 | Designer Integration | 2 | Firefly | Runway |

---

## Tool Usage by Category

| Category | Tools | Guides Using | Example Tools |
|----------|-------|--------------|---------------|
| AI Assistant | 3 | 5 | Claude, Gemini, ChatGPT |
| Transcription | 1 | 1 | Whisper Flow |
| Image Generation | 1 | 2 | Firefly |
| Video/Animation | 1 | 1 | Runway |
| Presentation | 1 | 1 | Gamma |
| Whiteboard | 1 | 1 | Miro |
| Documentation | 1 | 1 | Notion |
| Development Platform | 1 | 0 | Lovable |

---

**File Location:** `ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/Database_Architecture_Preview/TABLE_guide_tools.md`
**Last Updated:** 2025-11-22
