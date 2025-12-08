# Similar Entity (SIM)

**Entity ID:** SIM
**Purpose:** Normalization, taxonomy, whisper cleanup, term mapping
**Created:** 2025-12-07
**Owner:** Niko_Kar_002

---

## Overview

The Similar (SIM) entity handles normalization and mapping of similar terms, concepts, and entities across the system. It serves as a taxonomy and cleanup mechanism for:
- Whisper transcription normalization
- Term standardization
- Concept mapping
- Entity relationship tracking

---

## Core Functions

### 1. Whisper Cleanup
**Problem:** Voice transcriptions use varied terminology for same concepts

**Solution:** Mapping table that normalizes variations

**Example:**
```
"folder" = "directory" = "dir" → folder
"file" = "document" = "doc" → file
"cloud" = "cloud platform" = "cloud service" → cloud_platform
```

### 2. Taxonomy Management
**Purpose:** Hierarchical organization of concepts

**Example:**
```
Project Management
├─ Task Manager
│   ├─ PRT (Project level)
│   └─ SPRG (Template level)
└─ Tags
    ├─ work
    ├─ personal
    └─ terminology
```

### 3. Entity Normalization
**Purpose:** Map related entities and their relationships

**Example:**
```
LBS (Libraries)
  ↔ Similar: Books, Reading, Research
  ↔ Related: SCR (Scraping)
  ↔ Integrates: Cloud storage, E-readers
```

---

## Folder Structure

```
ENTITIES/Similar/
├── README.md (this file)
├── whisper_mappings.md (transcription normalization)
├── taxonomy.md (hierarchical organization)
├── entity_relationships.md (how entities relate)
└── normalization_rules.md (standardization rules)
```

---

## Whisper Mappings

### File: whisper_mappings.md

**Purpose:** Map transcription variations to canonical terms

**Format:**
```markdown
### Category: File Operations
create file = make file = new file → create_file
delete file = remove file = erase file → delete_file
move file = transfer file = relocate file → move_file

### Category: Reserved Words
research = investigate = look into → RESEARCH
build = construct = develop → BUILD
```

**Usage:**
- Automation agent reads mappings
- Normalizes detected reserved words
- Standardizes terminology before processing

---

## Taxonomy Structure

### File: taxonomy.md

**Purpose:** Define hierarchical relationships

**Format:**
```markdown
## Task Manager Hierarchy
PRT (Project)
  └─ SPRG (Template/Sprint)
      └─ Tasks
          └─ Subtasks

## Budget Template Hierarchy
Month
  └─ Week
      └─ Day
          └─ Expense Category
```

**Integration:**
- Task manager uses this structure
- Budget tracking follows hierarchy
- All agents reference same taxonomy

---

## Entity Relationships

### File: entity_relationships.md

**Purpose:** Map how entities interact

**Format:**
```markdown
LBS (Libraries)
  ├─ Uses: SCR (Scraping)
  ├─ Outputs to: Cloud storage
  └─ Related: Personal knowledge management

SCR (Scraping)
  ├─ Serves: LBS, HR, Research
  ├─ Uses: Task queue (QQ)
  └─ Requires: Network access

VID (Video)
  ├─ Department: Video production
  ├─ Uses: Google Drive
  └─ Related: Personal brand (Relax Warsaw)
```

---

## Normalization Rules

### File: normalization_rules.md

**Rules for standardizing data:**

1. **Casing:**
   - Reserved words: UPPERCASE
   - Entity IDs: UPPERCASE (LBS, SCR, VID)
   - File names: lowercase with underscores

2. **Dates:**
   - Format: YYYY-MM-DD
   - Month: Mon_YY (Dec_25)
   - Week: Week_XX or WW_XX

3. **IDs:**
   - System: SYS.XX
   - Skills: SKL.XX
   - Queues: QQ.XXX
   - Entities: 3-letter codes

4. **Terms:**
   - Use mappings from whisper_mappings.md
   - Canonical form preferred
   - Variations accepted, normalized on processing

---

## Integration with Automation

### Detection Process
```
Whisper transcription
  → Read SIM mappings
  → Normalize variations
  → Detect reserved words
  → Create standardized tasks
```

### Example Flow
```
User says: "I need to investigate cloud options"
  ↓
Whisper captures: "investigate cloud options"
  ↓
SIM maps: investigate → RESEARCH, cloud → cloud_platform
  ↓
Normalized: "RESEARCH cloud_platform options"
  ↓
Automation detects: RESEARCH reserved word
  ↓
Creates task in Share/
```

---

## Variable System

### "Similar" Variable in Task Manager
**Purpose:** Link related tasks, normalize tags

**Format:**
```
Task A
  Similar: Task B, Task C
  Normalized_Tags: #research #cloud #budget

Task B
  Similar: Task A, Task D
  Normalized_Tags: #research #cloud #platform
```

**Use Cases:**
- Find related tasks
- Group by normalized concepts
- Build knowledge graph

---

## Implementation Priority

### Week 02 (Current)
- [x] Create SIM entity structure
- [ ] Build whisper_mappings.md
- [ ] Define basic normalization rules

### Week 03
- [ ] Integrate with automation-agent
- [ ] Test normalization in processing
- [ ] Build taxonomy structure

### Week 04+
- [ ] Entity relationship mapping
- [ ] Advanced normalization
- [ ] Knowledge graph visualization

---

## Next Steps

1. Populate whisper_mappings.md with common variations
2. Define taxonomy for task manager integration
3. Map entity relationships
4. Integrate normalization into automation-agent
5. Test with real whisper transcriptions

---

**Entity Status:** Structure created - Content population in progress
**Dependencies:** automation-agent, whisper transcriptions
**Priority:** High (normalization improves all processing)
