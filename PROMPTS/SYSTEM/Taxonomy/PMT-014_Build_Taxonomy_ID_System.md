# PROMPT: Build Taxonomy Initial ID List for Ecosystem

## Objective
Create a comprehensive master taxonomy list of all Task Manager sub-entities with standardized consonant-only 3-letter ISO codes and sequential 3-digit IDs.

## ID Structure Format
```
{XXX}-{###}

XXX = 3-letter consonant-only ISO code (derived from entity type name)
### = 3-digit sequential ID (001-999)
```

## Entity Type Taxonomy

### Primary Task Manager Sub-Entities

| Entity Type | ISO Code | ID Range | Count | Description |
|-------------|----------|----------|-------|-------------|
| Project Templates | **PRT** | PRT-001 to PRT-009 | 9 | High-level project definitions with milestones |
| Milestone Templates | **MLT** | MLT-001 to MLT-009 | 9 | Project phase markers with task collections |
| Task Templates | **TST** | TST-001 to TST-071 | 71 | Individual task definitions (Action + Object + Tool) |
| Step Templates | **STT** | STT-001 to STT-379 | 379 | Detailed procedural steps within tasks |
| Checklist Templates | **CHT** | CHT-001 to CHT-098 | 98 | Deliverable items and substeps |
| Workflows | **WRF** | WRF-001 to WRF-002 | 2 | Automated process flows (Linear/Parallel) |
| Guides | **GDS** | GDS-001 onwards | TBD | Taxonomy and framework documentation |
| Prompts | **PRM** | PRM-001 onwards | 100+ | AI prompts organized by department |
| Researches | **RSR** | RSR-001 onwards | 50+ | Research reports and video analyses |

### ISO Code Derivation Rules

**Pattern**: Extract first 3 consonants from entity type name, removing vowels (A, E, I, O, U)

Examples:
- **P**_**R**_oject **T**_emplate → **PRT**
- **M**_i**L**_estone **T**_emplate → **MLT**
- **T**_a**S**_k **T**_emplate → **TST**
- **ST**_ep **T**_emplate → **STT**
- **CH**_ecklist **T**_emplate → **CHT**
- **W**_o**R**_k**F**_low → **WRF**
- **G**_ui**D**_e**S** → **GDS**
- **PR**_o**M**_pt → **PRM**
- **R**_e**S**_ea**R**_ch → **RSR**

**Note**: All Template entities include 'T' as the final character in their ISO code.

## Task Instructions

### Phase 1: Inventory Current Entities

For each entity type in TASK_MANAGERS directory:

1. **Scan directory structure**:
   - Location: `C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\{EntityType}/`
   - Identify all JSON and MD files
   - Extract current naming patterns

2. **Extract entity metadata**:
   - Current file name
   - Current ID (if exists)
   - Entity name/title
   - Description
   - Department association
   - Full file path

3. **Map to new ISO code system**:
   - Assign new ID: `{ISO}-{###}`
   - Maintain sequential numbering
   - Preserve hierarchical relationships

### Phase 2: Generate Master Taxonomy List

Create a structured list with the following columns:

| New_ID | Entity_Type | Current_ID | Name | Description | Department | File_Path | Status |
|--------|-------------|------------|------|-------------|------------|-----------|--------|

**Example entries**:

```csv
New_ID,Entity_Type,Current_ID,Name,Description,Department,File_Path,Status
PRT-001,Project_Template,Project-Template-001,AI Tutorial Research,Research and analyze AI tutorial content,AID,TASK_MANAGERS/Project_Templates/Project-Template-001_AI.json,Active
MLT-001,Milestone_Template,Milestone-Template-001,Content Analysis,Initial content discovery and analysis phase,AID,TASK_MANAGERS/Milestone_Templates/Milestone-Template-001_Content_Analysis.json,Active
TST-001,Task_Template,Task-Template-001,Create Job Posting,Create and publish job posting in Notion,HRM,TASK_MANAGERS/Task_Templates/Task-Template-001.json,Active
STT-001,Step_Template,Step-Template-001,Configure Perplexity Search,Set up Perplexity with specific parameters,AID,TASK_MANAGERS/Step_Templates/AI/Step-Template-001_configure-perplexity.md,Active
CHT-001,Checklist_Template,CHK-001,Job Description Draft,Draft complete job description document,HRM,TASK_MANAGERS/Checklist_Items/Checklist-Item-001.json,Active
WRF-001,Workflow,WF-LIN-001,Old Client Re-Engagement,Linear workflow for client re-engagement,SLS,TASK_MANAGERS/Workflows/WF-LIN-001_Old_Client_ReEngagement.yaml,Active
```

### Phase 3: Create Hierarchical Relationships Map

Document parent-child relationships:

```
PRT-001 (AI Tutorial Research Project)
  ├── MLT-001 (Tutorial Sources Identified)
  │   ├── TST-052 (Discover AI Tutorial Content)
  │   │   └── STT-001 (Configure Perplexity Search)
  │   └── TST-054 (Track AI Tutorial Influencers)
  │
  ├── MLT-002 (Videos Transcribed)
  │   └── TST-051 (Transcribe Videos)
  │       ├── STT-045 (Upload to Transcription Service)
  │       └── STT-046 (Review Transcript Quality)
  │
  └── MLT-003 (Taxonomy Enriched)
      ├── TST-053 (Initial Video Analysis)
      ├── TST-056 (Gap Analysis)
      └── TST-055 (Tool Library Creation)
          └── CHT-015 (Document New Tools)
```

### Phase 4: Generate Department Distribution

Break down entity counts by department:

| Department | ISO | PRJ | MLS | TSK | STP | CHK | Total |
|------------|-----|-----|-----|-----|-----|-----|-------|
| AI Department | AID | 3 | 10 | 28 | 150 | 30 | 226 |
| Human Resources | HRM | 1 | 2 | 6 | 6 | 8 | 23 |
| Development | DEV | 1 | 3 | 4 | 20 | 5 | 33 |
| Lead Generation | LGN | 2 | 6 | 12 | 82 | 18 | 120 |
| Design | DGN | 0 | 1 | 2 | 20 | 2 | 30 |
| Video Production | VID | 1 | 3 | 6 | 35 | 3 | 68 |
| Sales | SLS | 0 | 0 | 1 | 9 | 5 | 16 |

**Note**: Administration (ADM) department has been deprecated. All content from this department has been migrated to AI Department (AID).

### Phase 5: Create Migration Mapping

Document old ID → new ID mappings:

```json
{
  "migration_map": {
    "Project-Template-001": "PRT-001",
    "Milestone-Template-001": "MLT-001",
    "Task-Template-001": "TST-001",
    "Step-Template-001": "STT-001",
    "CHK-001": "CHT-001",
    "WF-LIN-001": "WRF-001"
  },
  "department_migrations": {
    "ADM": "AID",
    "AI": "AID"
  }
}
```

## Active Department Codes

| Department | ISO Code | Full Name |
|------------|----------|-----------|
| AI Department | **AID** | AI, Automations, Administration |
| Human Resources | **HRM** | Human Resource Management |
| Development | **DEV** | Development & Engineering |
| Lead Generation | **LGN** | Lead Generation |
| Design | **DGN** | Design & Creative |
| Video Production | **VID** | Video Production |
| Sales | **SLS** | Sales & Client Relations |

**Deprecated Departments** (content migrated to AID):
- ~~ADM~~ (Administration) → AID

## Output Deliverables

Generate the following files:

### 1. Master Taxonomy List
**File**: `Taxonomy_Master_List.csv`
- All entities with new ISO codes
- Complete metadata
- Sortable by entity type, department, ID

### 2. Hierarchical Relationship Tree
**File**: `Taxonomy_Hierarchy_Tree.md`
- ASCII tree structure showing parent-child relationships
- Cross-references to related entities
- Dependency chains

### 3. Department Distribution Report
**File**: `Taxonomy_Department_Distribution.md`
- Entity counts by department
- Visual breakdown tables
- Coverage analysis
- Migration notes for deprecated departments

### 4. Migration Mapping File
**File**: `Taxonomy_Migration_Map.json`
- Old ID → New ID mappings
- Department migration mappings
- Bidirectional lookup support
- Validation checksums

### 5. ISO Code Registry
**File**: `Taxonomy_ISO_Code_Registry.md`
- Complete list of all 3-letter codes
- Derivation rules and examples
- Reserved codes for future entities
- Department code registry

## Validation Rules

1. **Uniqueness**: Each ISO-### code must be globally unique
2. **Sequential**: IDs within each type must be sequential (no gaps initially)
3. **Consonant-only**: All ISO codes use only consonants (B,C,D,F,G,H,J,K,L,M,N,P,Q,R,S,T,V,W,X,Y,Z)
4. **Case**: Always uppercase for consistency
5. **Length**: Always 3 letters + 3 digits (e.g., TSK-001, not TSK-1)
6. **Department codes**: Use active 7 department codes only (AID, HRM, DEV, LGN, DGN, VID, SLS)
7. **Migration**: All ADM entities must be reassigned to AID

## Directory Structure Reference

```
TASK_MANAGERS/
├── Project_Templates/          # PRT-001 to PRT-009
├── Milestone_Templates/        # MLT-001 to MLT-009
├── Task_Templates/             # TST-001 to TST-071
├── Step_Templates/             # STT-001 to STT-379
│   ├── AI/                     # Now AID (AI Department)
│   ├── DESIGN/                 # DGN
│   ├── DEV/                    # DEV
│   ├── HR/                     # HRM
│   ├── LG/                     # LGN
│   ├── SALES/                  # SLS
│   ├── ADMIN/                  # DEPRECATED → Migrated to AID
│   └── OPS/                    # DEPRECATED → Migrated to AID
├── Checklist_Items/            # CHT-001 to CHT-098
├── Workflows/                  # WRF-001 to WRF-020
├── GUIDES/                     # GDS-001 onwards
├── PROMPTS/                    # PRM-001 onwards
└── RESEARCHES/                 # RSR-001 onwards
```

## Expected Timeline

- **Phase 1** (Inventory): Scan all directories and extract metadata
- **Phase 2** (Master List): Generate comprehensive CSV with all entities
- **Phase 3** (Relationships): Map hierarchical connections
- **Phase 4** (Distribution): Calculate department breakdowns with migration notes
- **Phase 5** (Migration): Create old→new ID mappings and department migrations

## Success Criteria

- ✓ All 544+ entities catalogued with new ISO codes
- ✓ Zero duplicate IDs across entire system
- ✓ Hierarchical relationships preserved
- ✓ Migration path documented for ADM → AID
- ✓ All deliverable files generated
- ✓ Validation rules passed 100%
- ✓ Department consolidation completed

## Notes

- This is the **initial** taxonomy for Task Managers only
- Future phases will extend to other ENTITIES (LIBRARIES, DEPARTMENTS, BUSINESSES, etc.)
- ISO codes are designed to be human-readable and memorable
- System supports up to 999 entities per type before namespace expansion needed
- Maintain backward compatibility during migration period
- **AI Department (AID)** now consolidates AI and Administration functions
- ADM is a deprecated department; all content migrated to AID
