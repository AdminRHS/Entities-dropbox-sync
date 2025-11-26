# 2. ENTITY TAXONOMY REFERENCE

**Version:** 6.1 | **Date:** 2025-11-26 | **Status:** Production
**Part of:** MAIN_PROMPT_v6 Modular System

---

## ID STANDARDS

**Format:** `XXX-###`
- **XXX:** 3 consonants (PRT, MLT, TST, STT, TOL, GDS, PMT)
- **###:** 3 digits, zero-padded (001, 042, 153)
- **Sequential:** No gaps, no category prefixes
- **Unique:** Per entity type (MLT-001 ≠ PMT-001 ≠ TOL-001)
- **Immutable:** IDs never change after assignment

**Examples:**
- ✅ CORRECT: MLT-001, TST-042, PMT-005, GDS-010, STT-127
- ❌ WRONG: MLT-1, TSK-VID-042, PMT-COR-005, GDS10, STT-1

## ENTITY RELATIONSHIPS

**Hierarchical Structure (Reusable Templates):**
```
PRT (Project Templates)
  ├─→ MLT (Milestone Templates) [many:many] - reusable across projects
       ├─→ TST (Task Templates) [many:many] - reusable across milestones
            ├─→ STT (Step Templates) [many:many] - reusable across tasks

Templates are INDEPENDENT and REUSABLE:
- Same STT-### can be used in multiple TST
- Same TST-### can be used in multiple MLT
- Same MLT-### can be used in multiple PRT
```

**Cross-Entity References:**
```
All entities → TOL (Tools) [many:many]
All entities → GDS (Guides) [many:many] - for classification help
Prompts (PMT) → Can reference any entity type
```

## CROSS-ENTITY LINKING

**In TASK_MANAGERS (Reusable Template System):**
- **No hard links** - Templates are independent and reusable
- **Composition at runtime** - Projects compose milestones, milestones compose tasks, tasks compose steps
- **Many-to-many relationships:**
  - One step (STT-###) can be part of multiple tasks
  - One task (TST-###) can be part of multiple milestones
  - One milestone (MLT-###) can be part of multiple projects
- **Check existing** - Review PRT-001 through PRT-009 before creating new projects
- **Reference** - All templates reference Tools (TOL-###) and Guides (GDS-###)

**In PROMPTS:**
- Reference entities by ID: "Use PMT-004 for transcription"
- Chain prompts: PMT-004 → PMT-009 → PMT-032

**In LIBRARIES (Tools):**
- Tools (TOL-###) referenced by tasks
- Browser extensions explicitly marked in TOL metadata
- Tools link to workflows and departments

**In GUIDES:**
- [GDS-010](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-010): Daily workflow structure
- [GDS-011](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-011): Entity classification decision tree (PRT/MLT/TST/STT)
- [GDS-012](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-012): Template cross-references and relationships

## VALIDATION RULES

Before creating new entity:
1. Check master CSV/JSON for existing
2. Use next sequential ID (find highest, +1)
3. Fill all required metadata
4. Validate no duplicates
5. Run validation script: `./scripts/validate_{entity}.py`

---

## PRACTICAL EXAMPLES

### Example 1: Daily Report Task Extraction

**Scenario:** Employee reports: "Created n8n automation to sync Google Sheets to Dropbox"

**Task-First Approach:**
1. Extract task: TST-042 "Create n8n automation for employee data sync"
2. Check project: Belongs to PRT-003 (Complete HR Automation Implementation)
3. Check milestone: Part of MLT-006 (HR System Integration)
4. Break into steps:
   - STT-127: Configure Google Sheets node
   - STT-128: Set up Dropbox upload node
   - STT-129: Map employee data fields
5. Link tools: TOL-007 (n8n), TOL-150 (Google Sheets), TOL-012 (Dropbox)
6. Reference guide: GDS-010 (Daily workflow setup)

**Structured Output:**
```
PRT-003: Complete HR Automation Implementation
  └─ MLT-006: HR System Integration
      └─ TST-042: Create n8n automation ✅
          ├─ STT-127: Configure Google Sheets node ✅
          ├─ STT-128: Set up Dropbox upload node ✅
          └─ STT-129: Map employee data fields ✅
```

### Example 2: New Project Identification

**Scenario:** Work doesn't fit existing PRT-001 through PRT-009

**Steps:**
1. Check existing projects: Review PRT-001 to PRT-009
2. Identify gap: "Video tutorial series" not covered
3. Create new: PRT-010 "Video Tutorial Production Pipeline"
4. Define milestones:
   - MLT-028: Research & Planning
   - MLT-029: Video Production
   - MLT-030: Publishing & Distribution
5. Reference guide: GDS-011 (Entity Mapping Tutorial)

### Example 3: Using GUIDES for Classification

**Scenario:** Uncertain whether to create TST or STT

**Decision Tree (from GDS-011):**
- ❓ "Is this a complete work unit that takes hours/days?"
  - ✅ YES → Create TST-### (Task Template)
  - ❌ NO → Check next question
- ❓ "Is this a 5-30 minute action within a larger task?"
  - ✅ YES → Create STT-### (Step Template)
  - ❌ NO → Might be MLT-### (Milestone)

**Example Application:**
- "Set up n8n workflow" = TST-### (takes hours)
- "Configure Google Sheets node" = STT-### (takes 10 minutes, part of workflow setup)

### Example 4: Tool Linking with Browser Extensions

**Scenario:** Task involves Chrome extension

**Proper Linking:**
```
TST-065: Extract LinkedIn contacts
  └─ Tools:
      - TOL-042 (LinkedIn Sales Navigator) - main platform
      - TOL-156 (Browse AI) - Chrome extension for scraping
      - TOL-150 (Google Sheets) - data storage
  └─ Guide: GDS-012 (Template Cross-Reference)
```

**TOL Metadata Notes:**
- TOL-156 explicitly marked as `"browser_extension": true`
- Platform compatibility: `["Chrome", "Edge"]`
- Integration type: `"web_automation"`

### Example 5: Cross-Entity Validation

**Before Creating TST-073:**

**Checklist:**
1. ✅ Check TSM-003_Task_Templates/Task_Templates_Master_List.csv
   - Last ID: TST-072
   - Next ID: TST-073 ✓
2. ✅ Verify parent milestone exists
   - MLT_ID: MLT-009 (Behance Project Publishing) ✓
3. ✅ Check required metadata
   - Name: "Behance Step 05 - Add Project Tags" ✓
   - Department: DGN ✓
   - Description: Complete ✓
4. ✅ Link to tools
   - TOL-??? (Behance platform - check if exists)
5. ✅ Reference guide
   - GDS-012 for workflow cross-reference

### Example 6: Hierarchical ID Assignment

**Scenario:** Building complete project structure

**Bottom-Up Approach:**

**Step 1:** Create Steps (STT-###)
```
STT-450: Write project description
STT-451: Select cover image
STT-452: Upload project images
STT-453: Add tags and categories
```

**Step 2:** Group into Tasks (TST-###)
```
TST-074: Prepare Behance project content
  └─ STT-450, STT-451, STT-452, STT-453
```

**Step 3:** Group into Milestone (MLT-###)
```
MLT-009: Behance Project Publishing
  └─ TST-068: Select and prepare project
  └─ TST-072: Write project description
  └─ TST-074: Upload project images
  └─ TST-076: Publish and share
```

**Step 4:** Link to Project (PRT-###)
```
PRT-009: Designer Portfolio Expansion
  └─ MLT-009: Behance Project Publishing
  └─ MLT-015: Dribbble Shot Posting
  └─ MLT-023: Instagram Portfolio Updates
```
