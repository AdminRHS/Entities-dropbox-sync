---
PMT_ID: PMT-073
Title: Create Main Prompt v6 (Ultra-Condensed)
Category: CORE
Department: Multi
Version: 1.0
Status: Active
Created: 2025-11-19
Last_Updated: 2025-11-19
Author: AI & Automation Team
Tags: [core, system-prompt, ultra-condensed, optimization, main-prompt]
Dependencies: [PMT-001]
Referenced_Entities: [TASK_MANAGERS, LIBRARIES, PROMPTS, TALENTS, DEPARTMENTS, BUSINESSES]
---

# Create Main Prompt v6 (Ultra-Condensed)

## Purpose
Generate an ultra-condensed, highly optimized Main Prompt v6 that achieves 70% size reduction from v4 while maintaining full functionality through strategic compression, smart referencing, and modular architecture.

## Context
Main Prompt v4 is comprehensive but lengthy (~2800 lines). Version 6 aims to condense this to ~500-800 lines while:
- Maintaining all core functionality
- Improving clarity and scanability
- Reducing token usage
- Enabling faster context loading
- Supporting dynamic module loading

## Design Philosophy

### Core Principles

**1. Extreme Compression**
- Remove redundancy
- Merge related sections
- Use tables over prose
- Employ abbreviations strategically
- Reference external files

**2. Smart Referencing**
- Link to entity taxonomies instead of embedding
- Reference standardized templates
- Use PMT-### IDs for prompt references
- Point to master data files (JSON, CSV)

**3. Modular Architecture**
- Core system in main prompt (always loaded)
- Optional modules loaded on-demand
- Department-specific extensions
- Workflow-specific addons

**4. Token Optimization**
- Dense information packing
- Minimal boilerplate
- Strategic use of symbols and codes
- Eliminate conversational fluff

---

## Main Prompt v6 Structure

### Section 1: Core Identity & Purpose (50-100 lines)

**Components:**
- **WHO:** AI role and capabilities (3-5 lines)
- **WHAT:** Primary functions (bullet list, 10-15 items)
- **HOW:** Operating principles (table format, 5-7 rules)
- **ENTITIES:** Available systems with ISO codes (table, 8 entities)

**Compression Techniques:**
```markdown
# YOU ARE
AI Assistant for Remote Helpers | Entity-Aware | Taxonomy-Driven | Automation-First

# CORE FUNCTIONS
- Extract entities: TASK_MANAGERS (MLT/TSK/STP), LIBRARIES (ACT/OBJ/TOL/SKL), PROMPTS (PMT)
- Execute workflows: Video processing, daily reports, research integration
- Maintain consistency: Cross-reference entities, validate IDs, update taxonomies
[... 10 more bullets]

# OPERATING PRINCIPLES
| Principle | Rule |
|-----------|------|
| Entity-First | Always identify & tag entities before processing |
| ID-Driven | Use XXX-### format (MLT-001, PMT-005, ACT-042) |
| Validate | Check master CSVs before creating new entities |
| Cross-Ref | Link related entities across systems |
| Automate | Scripts > Manual, Templates > Custom |
```

**What to Remove from v4:**
- Long explanatory paragraphs
- Redundant examples
- Conversational preambles
- Detailed history/background

**What to Keep:**
- Entity ISO codes and formats
- Core operating rules
- Primary functions list

---

### Section 2: Entity Taxonomy Reference (100-150 lines)

**Components:**
- **Entity Overview Table** (8 entities x 1 line each)
- **ID Format Standards** (consolidated table)
- **Master File Locations** (reference paths)
- **Quick Cross-Reference Matrix**

**Compression Techniques:**

```markdown
## ENTITIES & TAXONOMY

### Entity Map
| Code | Entity | ID Format | Master CSV | Count |
|------|--------|-----------|------------|-------|
| **PRT** | Project Template | PRT-### | TASK_MANAGERS/DATA/Projects_Master.csv | 50+ |
| **MLT** | Milestone Template | MLT-### | TASK_MANAGERS/DATA/Milestones_Master.csv | 200+ |
| **TSK** | Task Template | TSK-### | TASK_MANAGERS/DATA/Tasks_Master.csv | 500+ |
| **STP** | Step Template | STP-### | TASK_MANAGERS/DATA/Steps_Master.csv | 1000+ |
| **ACT** | Action | ACT-### | LIBRARIES/Actions/actions_master.json | 300+ |
| **OBJ** | Object | OBJ-### | LIBRARIES/Objects/objects_master.json | 500+ |
| **TOL** | Tool | TOL-### | LIBRARIES/Tools/tools_master.json | 200+ |
| **PMT** | Prompt | PMT-### | PROMPTS/DATA_FIELDS/PMT_Master_List.csv | 73 |

### ID Rules
- Format: `XXX-###` (3 consonants, 3 digits, zero-padded)
- Sequential: No gaps, no category prefixes
- Unique: Per entity type (MLT-001 ≠ PMT-001)
- Immutable: IDs never change after assignment

### Cross-Entity Links
- Tasks → Milestones: MLT_ID field
- Steps → Tasks: TSK_ID field
- All → Actions/Objects: Reference in descriptions
- Prompts → All: Can reference any entity

**📂 Master Data:** `ENTITIES/{ENTITY_TYPE}/DATA_FIELDS/` or `/DATA/`
```

**What to Remove:**
- Lengthy entity descriptions
- Detailed field explanations
- Examples for every entity type
- Historical context

**What to Keep:**
- Entity codes and ID formats
- Master file locations
- Cross-reference rules

---

### Section 3: Workflow Execution (150-200 lines)

**Components:**
- **Common Workflows** (condensed to essential steps)
- **Video Processing Pipeline** (7 phases → table format)
- **Daily Reports** (template reference)
- **Research Integration** (abbreviated workflow)

**Compression Techniques:**

```markdown
## WORKFLOWS

### Video Transcription → Entity Extraction
**Prompt:** PMT-004 | **Output:** TASK_MANAGERS entities (MLS/TSK/STP)

1. Load transcript → 2. Identify milestones → 3. Extract tasks → 4. Assign IDs → 5. Validate → 6. Save JSON
**Validation:** Check against TASK_MANAGERS/DATA/*.csv for duplicates

### Daily Reports
**Collection:** PMT-032 | **Departments:** PMT-033 to PMT-043 (11 dept prompts)

```bash
# Execute all department reports
for dept in AID DGN DEV HRM LGN MKT SLS SMM VID FIN; do
  run_prompt "PMT-0XX_${dept}_Daily_Report" >> daily_reports/$(date +%Y-%m-%d)_${dept}.md
done
# Aggregate with PMT-032
```

### Research Integration
**Prompts:** PMT-044 to PMT-052 | **Workflow:**
Research (YouTube/Web) → Extract entities → Cross-ref LIBRARIES → Update taxonomies → Generate reports

### Task Manager Workflows
| Workflow | Prompts | Entities Created | Validation |
|----------|---------|------------------|------------|
| Project Setup | PMT-061 | PRT-###, MLT-### | Check PRT CSV |
| Task Breakdown | Manual | TSK-###, STP-### | Link to MLT-### |
| Library Match | PMT-062 | ACT/OBJ/TOL refs | Fuzzy match existing |
```

**What to Remove:**
- Step-by-step instructions (reference prompts instead)
- Detailed examples for each workflow
- Troubleshooting guides
- Alternative approaches

**What to Keep:**
- Workflow names and prompt IDs
- Essential steps in compact format
- Validation checkpoints

---

### Section 4: Department Operations (100-150 lines)

**Components:**
- **Department Codes** (table)
- **Primary Responsibilities** (1-2 bullets per dept)
- **Key Prompts** (reference only)
- **Daily Operations** (ultra-condensed)

**Compression Techniques:**

```markdown
## DEPARTMENTS

| Code | Department | Prompts | Primary Focus |
|------|-----------|---------|---------------|
| **AID** | AI & Automation | PMT-033, PMT-048, PMT-066-069 | Taxonomy, automation, system health |
| **VID** | Video Production | PMT-004-013, PMT-043, PMT-071 | Transcription, entity extraction |
| **HRM** | Human Resources | PMT-038, PMT-053-057, PMT-047/049 | CV parsing, recruitment, automation |
| **DEV** | Development | PMT-036, PMT-046, PMT-052, PMT-068-069 | Version control, VSCode, APIs |
| **LGN** | Lead Generation | PMT-039 | Lead research, outreach |
| **DGN** | Design | PMT-035 | Creative assets, branding |
| **MKT** | Marketing | PMT-034, PMT-040, PMT-042 | Content, campaigns, social |
| **SLS** | Sales | PMT-041, PMT-044 | Pipeline, research |
| **SMM** | Social Media | PMT-042, PMT-045 | Content, engagement |
| **FIN** | Finance | PMT-037 | Reporting, compliance |

**Daily Ops:** Run dept report (PMT-0XX) → Extract entities → Update CSVs → Archive to /REPORTS/
**Collaboration:** Cross-dept entities link via shared LIBRARIES (ACT/OBJ/TOL)
```

**What to Remove:**
- Org chart details
- Individual role descriptions
- Detailed responsibilities
- Project histories

**What to Keep:**
- Department codes
- Key prompts per department
- Primary focus areas

---

### Section 5: File Operations & Data Management (50-100 lines)

**Components:**
- **File Structure** (directory tree, condensed)
- **Naming Conventions** (table)
- **Master Data Files** (locations)
- **Validation Rules** (checklist)

**Compression Techniques:**

```markdown
## FILE OPERATIONS

### Directory Structure (Key Paths)
```
ENTITIES/
├── TASK_MANAGERS/DATA/        # *.csv (PRT/MLT/TSK/STP)
├── LIBRARIES/{Type}/           # *.json (ACT/OBJ/TOL/SKL/etc)
├── PROMPTS/DATA_FIELDS/        # PMT_Master_List.csv, *.json
├── DEPARTMENTS/{DEPT}/         # Dept-specific files
└── REPORTS/                    # Generated outputs
```

### Naming Rules
| Type | Pattern | Example |
|------|---------|---------|
| Templates | `XXX-###_Name.md` | `MLT-042_Onboarding_Process.md` |
| Data Files | `{entity}_master.{csv\|json}` | `milestones_master.csv` |
| Reports | `YYYY-MM-DD_{Type}.md` | `2025-11-19_AI_Daily_Report.md` |
| Archives | `{Year}/{Month}/{File}` | `2025/November/archived_file.md` |

### Validation Checklist
- [ ] ID exists in master CSV/JSON
- [ ] No duplicate IDs within entity type
- [ ] Referenced entities exist (MLT-### in TSK, etc.)
- [ ] File paths match catalog
- [ ] Required metadata present

**Auto-Validation:** Run `scripts/validate_{entity}.py` before commits
```

**What to Remove:**
- Detailed file format specifications
- Complete directory trees
- Step-by-step file creation guides

**What to Keep:**
- Essential paths
- Naming patterns
- Validation rules

---

### Section 6: Prompt Reference System (50-80 lines)

**Components:**
- **Prompt Categories** (table with PMT IDs)
- **When to Use Which Prompt** (decision matrix)
- **Prompt Chaining** (common sequences)

**Compression Techniques:**

```markdown
## PROMPT REFERENCE

### By Category
| Category | PMT Range | Use For |
|----------|-----------|---------|
| Core System | PMT-001 to PMT-003 | Base operations, v6 creation |
| Video Processing | PMT-004 to PMT-013, PMT-071 | Transcription, analysis, workflows |
| Daily Reports | PMT-032 to PMT-043 | Department daily ops |
| Taxonomy | PMT-014 to PMT-020 | ID systems, schema building |
| System Analysis | PMT-021 to PMT-029 | Health checks, validation |
| Research | PMT-044 to PMT-052 | YouTube, VSCode, integrations |
| HR Operations | PMT-053 to PMT-057 | Recruitment, CV parsing |
| Workflows | PMT-058 to PMT-065 | General operations, account mgmt |
| Automation | PMT-066 to PMT-069 | Scripts, version control |

### Decision Matrix
**Need to:** → **Use Prompt:**
- Extract from video → PMT-004
- Create taxonomy → PMT-014, PMT-016
- Daily report (AI) → PMT-033
- Validate system → PMT-029
- Parse CV → PMT-053
- Organize call notes → PMT-058

### Common Chains
1. **Video → Entities:** PMT-004 → PMT-009 (transcribe → integrate taxonomy)
2. **Research → Library:** PMT-048 → PMT-060 (research tools → integrate to LIBRARIES)
3. **Daily Ops:** PMT-0XX (dept report) → PMT-032 (collection) → Archive
```

**What to Remove:**
- Full prompt descriptions
- Detailed usage examples
- Alternative prompt suggestions

**What to Keep:**
- Prompt ID ranges
- Primary use cases
- Common prompt sequences

---

### Section 7: Quality & Validation (40-60 lines)

**Components:**
- **Validation Scripts** (commands)
- **Quality Checklist** (condensed)
- **Error Handling** (common fixes)

**Compression Techniques:**

```markdown
## QUALITY ASSURANCE

### Auto-Validation
```bash
# Entity validation
./scripts/validate_task_managers.py  # TASK_MANAGERS
./scripts/validate_libraries.py      # LIBRARIES
./scripts/validate_prompts.py        # PROMPTS

# Pre-commit hook (auto-runs)
git add . && git commit -m "message"  # Triggers validation
```

### Quality Checklist
- [ ] **IDs:** Unique, sequential, zero-padded (MLT-001 not MLT-1)
- [ ] **Refs:** All entity references exist (no broken MLT-### links)
- [ ] **Meta:** Required fields complete (Name, Description, Category, etc.)
- [ ] **Files:** Paths in CSV match physical files
- [ ] **Format:** Consistent naming (XXX-###_Name.ext)

### Common Errors & Fixes
| Error | Fix |
|-------|-----|
| Duplicate ID | Reassign to next available |
| Missing ref | Update or remove broken reference |
| Path mismatch | Move file or update CSV |
| Invalid format | Rename: `XXX-###_Name.ext` |

**On Failure:** Check validation output → Fix issues → Re-run → Commit when clean
```

**What to Remove:**
- Detailed error explanations
- Troubleshooting guides
- Alternative validation methods

**What to Keep:**
- Validation commands
- Essential checklist
- Quick fix reference

---

### Section 8: External Modules (Reference Only) (20-30 lines)

**Components:**
- **Available Modules** (list with locations)
- **Loading Syntax** (how to include)
- **When to Load** (use cases)

**Compression Techniques:**

```markdown
## EXTERNAL MODULES

### Available
- **Video Processing Extended** → `PROMPTS/Video_Processing/MODULES/extended_workflow.md`
- **HR Automation Suite** → `PROMPTS/DEPARTMENTS/HR_Operations/MODULES/automation.md`
- **Advanced Taxonomy** → `PROMPTS/SYSTEM/Taxonomy/MODULES/advanced.md`
- **API Integration** → `PROMPTS/SYSTEM/MODULES/api_integration.md`

### Load On-Demand
```markdown
**When working with [specific task], load module:**
> Include: [module_path]

**Example:**
> Include: PROMPTS/Video_Processing/MODULES/extended_workflow.md
```

### Module Selection
**If task involves:** → **Load module:**
- Complex video workflows → Video Processing Extended
- Bulk HR operations → HR Automation Suite
- Cross-entity taxonomy → Advanced Taxonomy
- External API calls → API Integration
```

**What to Remove:**
- Module contents (referenced externally)
- Detailed module descriptions

**What to Keep:**
- Module names and paths
- Loading syntax
- Selection criteria

---

## Compression Metrics

### Target Metrics
| Metric | v4 (Current) | v6 (Target) | Reduction |
|--------|-------------|-------------|-----------|
| **Total Lines** | ~2800 | ~500-800 | 70-80% |
| **Token Count** | ~15,000 | ~4,000-6,000 | 70% |
| **Sections** | 25+ | 8 | 68% |
| **Tables** | 5 | 20+ | +300% |
| **Examples** | 50+ | 10-15 | 70% |
| **Load Time** | 8-10s | 2-3s | 75% |

### Compression Strategies Applied
1. ✅ Tables replace prose (20+ tables vs 5)
2. ✅ External references vs embedded content
3. ✅ Bullet lists vs paragraphs
4. ✅ Code blocks vs written instructions
5. ✅ Symbols/abbreviations strategically used
6. ✅ Redundancy eliminated
7. ✅ Modular architecture (load on demand)
8. ✅ Essential info only (no fluff)

---

## Implementation Instructions

### Step 1: Read Main Prompt v4
Location: `C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\Core\PMT-001_Main_Prompt_v4.md`

Extract:
- All entity types and codes
- Core operating principles
- Workflow summaries
- Department information
- File structure overview

### Step 2: Create Condensed Sections

For each section (1-8 above):
1. Extract essential information from v4
2. Convert prose to tables/lists
3. Remove examples (or keep 1-2 minimal ones)
4. Replace detailed instructions with prompt references
5. Use abbreviations and symbols
6. Add external module references for deep content

### Step 3: Build v6 Structure

```markdown
# MAIN PROMPT v6 (Ultra-Condensed)
**Version:** 6.0 | **Date:** 2025-11-19 | **Status:** Production
**Replaces:** v4 | **Size:** ~700 lines | **Tokens:** ~5,000

---

## 1. CORE IDENTITY & PURPOSE
[50-100 lines - compressed from v4 Introduction + Overview]

## 2. ENTITY TAXONOMY REFERENCE
[100-150 lines - compressed from v4 Entities + Taxonomy sections]

## 3. WORKFLOW EXECUTION
[150-200 lines - compressed from v4 Workflows + Examples]

## 4. DEPARTMENT OPERATIONS
[100-150 lines - compressed from v4 Departments + Roles]

## 5. FILE OPERATIONS & DATA MANAGEMENT
[50-100 lines - compressed from v4 File Structure + Standards]

## 6. PROMPT REFERENCE SYSTEM
[50-80 lines - NEW - quick prompt lookup]

## 7. QUALITY & VALIDATION
[40-60 lines - compressed from v4 QA + Validation]

## 8. EXTERNAL MODULES
[20-30 lines - NEW - module loading system]

---

**Total:** ~560-870 lines (target: 700 avg)
```

### Step 4: Validate Compression

Check that v6 includes:
- ✅ All entity ISO codes (PRT, MLT, TSK, STP, ACT, OBJ, TOL, SKL, PMT, etc.)
- ✅ Core operating principles
- ✅ Essential workflows (even if abbreviated)
- ✅ Department codes and primary prompts
- ✅ File structure and naming conventions
- ✅ Validation rules
- ✅ Prompt reference system
- ✅ Module loading capability

### Step 5: Test Functionality

Use v6 to:
1. Extract entities from sample video transcript
2. Generate daily report for one department
3. Validate TASK_MANAGERS data
4. Reference appropriate prompts
5. Load external module

If all work correctly: ✅ v6 is production-ready

### Step 6: Save and Deploy

**Save as:** `C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\Core\PMT-002_Main_Prompt_v6.md`

**Update:**
- Status from "Draft" to "Active"
- PMT_Master_List.csv: Update PMT-002 status
- README.md: Document v6 release
- MIGRATION_LOG.md: Note v4 → v6 transition

**Deprecate v4:**
- Update PMT-001 status to "Deprecated" (after 30-day transition)
- Move to _ARCHIVE/ after 90 days
- Keep as fallback during transition period

---

## Success Criteria

✅ **v6 is successful when:**
1. **Size:** 70%+ reduction from v4 (~2800 → ~700 lines)
2. **Completeness:** All essential functionality preserved
3. **Clarity:** Faster to scan and understand
4. **Performance:** <3 seconds to load vs v4's 8-10 seconds
5. **Modularity:** Can load extensions on-demand
6. **Tested:** All core workflows function correctly

## Deliverables

1. **Main Prompt v6** - Ultra-condensed production version (~700 lines)
2. **Module Files** - External modules for extended functionality
3. **Migration Guide** - How to transition from v4 to v6
4. **Comparison Document** - Side-by-side v4 vs v6 feature matrix
5. **Performance Report** - Token usage, load time, functionality benchmarks

## Related Prompts
- PMT-001 - Main Prompt v4 (source)
- PMT-003 - Create Main Prompt v5 (modular approach)
- PMT-028 - Folder Reorganization
- PMT-072 - PROMPTS Critical Fixes

## Version History

### v1.0 (2025-11-19)
**Changes:**
- Initial creation of v6 generation prompt
- Ultra-condensed design philosophy established
- 8-section structure defined
- 70% compression target set
- Module system introduced

**Author:** AI & Automation Team

---

**Next Step:** Execute this prompt to generate Main Prompt v6
