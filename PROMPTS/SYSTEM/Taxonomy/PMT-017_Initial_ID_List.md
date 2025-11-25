# PROMPT: Build Taxonomy Initial ID List for LIBRARIES Ecosystem

## Objective

Create a comprehensive master taxonomy list of all **LIBRARIES sub-entities** (Tools, Objects, Actions, Workflows, Skills, Professions, and core Docs) with standardized **consonant-only 3-letter ISO codes** and **sequential 3-digit IDs**.

## ID Structure Format

```text
{XXX}-{###}

XXX = 3-letter consonant-only ISO code (derived from entity type name)
### = 3-digit sequential ID (001–999)
```

> **Note:** For readability and backwards compatibility, some codes (like `OBJ`) are allowed to keep a familiar prefix even if they contain vowels, but the **default rule** is consonant-only.

---

## Entity Type Taxonomy (LIBRARIES)

### Primary LIBRARIES Sub-Entities

| Entity Type    | ISO Code | ID Range     | Count | Description |
|----------------|----------|--------------|-------|-------------|
| Tools          | **TOL**  | TOL-001…     | 75+   | Individual tool definitions (AI tools, automation, databases, etc.) under `Tools/` |
| Objects        | **OBJ**  | OBJ-001…     | 36+   | Domain objects (Lead Gen, AI Automation, RAG, etc.) under `Responsibilities/Objects/` |
| Actions        | **ACT**  | ACT-001…     | 12+   | Data operations and other actions (scrape, enrich, parse, etc.) under `Actions/` |
| Workflows      | **WRF**  | WRF-001…     | 24+   | Lead generation and AI automation workflows under `Processes/Workflows/` |
| Skills         | **SKL**  | SKL-001…     | 12+   | Skill definitions consumed by professions (e.g., SKL-001–SKL-012) under `Skills/` |
| Professions    | **PRF**  | PRF-001…     | 12+   | Profession profiles (Lead Generator, SDR, AI Engineer, etc.) under `Professions/` |
| Cross-Refs     | **XRF**  | XRF-001…     | 1+    | Cross-reference and mapping files (e.g., `Cross_Reference_Mapping_Video_006_008.json`) |
| Reports & Docs | **RPD**  | RPD-001…     | 10+   | Library mapping reports, phase summaries, validation docs under `Prompts/` and `DEPARTMENTS/Prompts/` |

> **Example mappings from current library:**
> - `LIBRARIES/Tools/AI_Tools/OpenAI_GPT5.json` → TOL-0xx  
> - `Responsibilities/Objects/Lead_Generation_Objects.json` entries (currently `OBJ-LG-001`…`OBJ-LG-010`) → `OBJ-001`…`OBJ-010`  
> - `Actions/Data_Operations/Scrape.json` → ACT-0xx  
> - `Processes/Workflows/Lead_Generation_Workflows.json` entries → WRF-0xx  
> - `Skills/Lead_Generation_and_AI_Skills.json` → SKL-0xx  
> - `Professions/Lead_Generator.json` → PRF-0xx  
> - `Cross_Reference_Mapping_Video_006_008.json` → XRF-0xx  
> - `Prompts/Phase_2_Complete_Summary_Report.md` → RPD-0xx  

---

## ISO Code Derivation Rules (LIBRARIES)

**Pattern:** Extract first 3 consonants from entity type name, removing vowels (A, E, I, O, U) wherever practical, while keeping human-readable, stable codes.

- **T**_oo**L**_s → **TOL**
- **OB**_**J**_ects → **OBJ** (kept for legacy clarity)
- **AC**_**T**_ions → **ACT**
- **W**_o**R**_k**F**_lows → **WRF**
- **SK**_i**L**_ls → **SKL**
- **PR**_o**F**_essions → **PRF**
- Cross Re**F**erence (ma**P**ping) → **XRF**
- Re**P**orts & **D**ocumentation → **RPD**

> When adding **new LIBRARIES entity types**, derive ISO codes by:
> 1. Removing vowels from the English name.
> 2. Taking the first 3 consonants.
> 3. If ambiguous/unreadable, choose the closest memorable 3-letter mnemonic and document it in the ISO registry.

---

## Task Instructions (for LIBRARIES)

### Phase 1: Inventory Current LIBRARIES Entities

For each LIBRARIES sub-entity type:

1. **Scan directory structure**

   - **Tools**  
     - Root: `ENTITIES/LIBRARIES/Tools/`  
     - Subfolders: `AI_Tools/`, `Automation_Tools/`, `Data_Tools/`, `Business_Tools/`, `Development_Tools/`, `Cloud_Platforms/`, `Integration_Tools/`, `Social_Media_Platforms/`, `Video_Editing_Tools/`, etc.  
     - Find all `*.json` tool files.

   - **Objects**  
     - Canonical: `ENTITIES/LIBRARIES/Responsibilities/Objects/*.json`  
     - Legacy: `ENTITIES/LIBRARIES/Archive/Legacy_Root_Files/objects.json` (inventory but treat as archive).  
     - Focus on current domain files: `Lead_Generation_Objects.json`, `AI_Automation_Objects.json`, `RAG_Objects.json`, `Video_Generation_Objects.json`, etc.

   - **Actions**  
     - `ENTITIES/LIBRARIES/Actions/Data_Operations/*.json`  
     - Include individual action files and `Data_Operations_Actions_Index.json`.

   - **Workflows**  
     - `ENTITIES/LIBRARIES/Processes/Workflows/*.json`  
     - E.g. `Lead_Generation_Workflows.json`, `AI_Automation_Workflows.json`, `Workflows_Index.json`.

   - **Skills**  
     - `ENTITIES/LIBRARIES/Skills/Lead_Generation_and_AI_Skills.json`.

   - **Professions**  
     - `ENTITIES/LIBRARIES/Professions/*.json`  
     - E.g. `Lead_Generator.json`, `SDR.json`, `Backend_Developer.json`, `AI_Engineer.json`, `professions.json`.

   - **Cross-Reference & Reports**  
     - `ENTITIES/LIBRARIES/Cross_Reference_Mapping_Video_006_008.json`  
     - `ENTITIES/LIBRARIES/LIBRARIES_Import_Index.md`  
     - `ENTITIES/LIBRARIES/Prompts/*.md`  
     - `ENTITIES/LIBRARIES/DEPARTMENTS/Prompts_Archive/*.md` (treat as archive if necessary).

2. **Extract entity metadata**

   For each file, capture:

   - **Current file name** (`OpenAI_GPT5.json`)
   - **Current ID** (if exists):  
     - Tools: e.g. `"tool_id": "TOOL-AI-028"`  
     - Objects: e.g. `"object_id": "OBJ-LG-001"`  
     - Skills: e.g. `SKL-060` etc.
   - **Entity name/title**  
     - Tools: `name`  
     - Objects: `name` or `object_name`  
     - Actions: `name` / action label  
     - Workflows: workflow name/id inside collection  
     - Skills: skill phrase  
     - Professions: profession_name/full_title
   - **Description / purpose** (description fields or narrative text)
   - **Department association**  
     - Derive from profession department, tags, or explicit metadata (e.g. managers, developers, design).
   - **Source / provenance**  
     - Video (006/008), system analysis, manual import (where present: `source`, `discovery_sources` fields).
   - **Full file path** relative to `ENTITIES/LIBRARIES/`.

3. **Map to new ISO code system**

   - Determine Entity Type → ISO Code (TOL, OBJ, ACT, WRF, SKL, PRF, XRF, RPD).
   - Assign new ID:
     - `TOL-001`, `TOL-002`, … within **Tools**.
     - `OBJ-001`, `OBJ-002`, … within **Objects**.
     - `ACT-001`, `ACT-002`, … within **Actions**.
     - `WRF-001`, `WRF-002`, … within **Workflows**.
     - `SKL-001`, `SKL-002`, … within **Skills**.
     - `PRF-001`, `PRF-002`, … within **Professions**.
     - `XRF-001`… for cross-ref mapping files.
     - `RPD-001`… for summary/validation/mapping reports.
   - Ensure numbering is sequential per entity type (start from 001; do not introduce gaps initially).
   - Preserve any **existing semantic ranges** only as reference (e.g. legacy SKL-060–SKL-075 in the current library) and map them to new master IDs via migration mapping.

---

### Phase 2: Generate LIBRARIES Master Taxonomy List

Create a structured CSV / table with the following columns:

| New_ID | Entity_Type | Current_ID | Name | Description | Department | Source | File_Path | Status |
|--------|-------------|-----------|------|-------------|------------|--------|----------|--------|

**Example entries:**

```csv
New_ID,Entity_Type,Current_ID,Name,Description,Department,Source,File_Path,Status
TOL-001,Tool,TOOL-AI-028,OpenAI GPT-5,Advanced LLM for HTML parsing and design analysis,DEV;AID,Video_006;Video_009,LIBRARIES/Tools/AI_Tools/OpenAI_GPT5.json,Active
OBJ-001,Object,OBJ-LG-001,Lead List,Collection of prospective customers with enrichment metrics,LGN,Video_006,LIBRARIES/Responsibilities/Objects/Lead_Generation_Objects.json,Active
ACT-001,Action,DATA-OP-001,Scrape,Extract data from web sources,LGN;AID,Video_006,LIBRARIES/Actions/Data_Operations/Scrape.json,Active
WRF-001,Workflow,WF-LG-006,Google SERP Lead Generation,Scrape SERP → enrich domains → export leads,LGN,Video_006,LIBRARIES/Processes/Workflows/Lead_Generation_Workflows.json,Active
SKL-001,Skill,SKL-060,scraped lead lists via Apify,Intermediate LG skill,LGN,Video_006,LIBRARIES/Skills/Lead_Generation_and_AI_Skills.json,Active
PRF-001,Profession,(none),lead generator,Lead generation specialist for B2B prospecting,LGN,Video_006,LIBRARIES/Professions/Lead_Generator.json,Active
XRF-001,Cross_Reference,(n/a),Cross-Reference Mapping V006/V008,Bidirectional mapping Tools↔Workflows↔Skills↔Professions,ALL,Video_006;Video_008,LIBRARIES/Cross_Reference_Mapping_Video_006_008.json,Active
RPD-001,Report,(n/a),Phase 2 Complete Summary Report,LIBRARIES Phase 2 import summary & metrics,ALL,Video_006;Video_008,LIBRARIES/Prompts/Phase_2_Complete_Summary_Report.md,Active
```

---

### Phase 3: Create Hierarchical Relationships Map (LIBRARIES Perspective)

Document how LIBRARIES entities relate across tools, workflows, skills, professions, and objects:

```text
WRF-001 (Google SERP Lead Generation Workflow)
  ├── TOL-0xx (Apify Google SERP Scraper)
  ├── TOL-0yy (Anymailfinder)
  ├── OBJ-001 (Lead List)
  ├── OBJ-003 (Decision-Maker Email)
  ├── ACT-00a (scrape)
  ├── ACT-00b (enrich)
  ├── SKL-001 (scraped lead lists via Apify)
  ├── SKL-002 (enriched emails via Anymailfinder)
  └── PRF-001 (lead generator)
```

Build mapping segments such as:

- **Workflows → Tools** (primary and secondary tools per workflow).
- **Workflows → Objects** (input/output objects).
- **Workflows → Skills** (skills required to execute workflow).
- **Skills → Professions** (who typically owns that skill).
- **Professions → Tools/Objects/Workflows** (tool stack per profession).
- **Cross-reference files → all of the above**.

Represent this both as **tables** and optional **ASCII trees** (as in the Task Managers prompt) to make dependencies clear.

---

### Phase 4: Generate Department Distribution for LIBRARIES

Use the active department ISO codes you already defined for the ecosystem:

| Department        | ISO | Description                               |
|-------------------|-----|-------------------------------------------|
| AI & Automations  | AID | AI, Automations, Admin (consolidated) |
| Human Resources   | HRM | HR & Talent                               |
| Development       | DEV | Engineering & Dev                         |
| Lead Generation   | LGN | Lead Generation                           |
| Design            | DGN | Design & Creative                         |
| Video Production  | VID | Video content & production                |
| Sales             | SLS | Sales & Client Relations                  |
| Social Media      | SMM | Social Media Management                   |
| Finance           | FNC | Finance & Accounting                      |

Produce a distribution table like:

| Department | ISO | TOL | OBJ | ACT | WRF | SKL | PRF | Total |
|-----------|-----|-----|-----|-----|-----|-----|-----|-------|
| AID       | AID | 10  | 6   | 8   | 6   | 6   | 4   | 40    |
| LGN       | LGN | 8   | 10  | 6   | 14  | 6   | 4   | 48    |
| DEV       | DEV | 12  | 4   | 2   | 4   | 4   | 3   | 29    |
| DGN       | DGN | 5   | 6   | 0   | 2   | 2   | 2   | 17    |
| VID       | VID | 4   | 4   | 0   | 2   | 0   | 1   | 11    |
| HRM       | HRM | 1   | 2   | 0   | 0   | 0   | 1   | 4     |
| SLS       | SLS | 2   | 4   | 0   | 2   | 0   | 2   | 10    |
| SMM       | SMM | 3   | 2   | 0   | 1   | 1   | 1   | 8     |
| FNC       | FNC | 1   | 1   | 0   | 0   | 0   | 1   | 3     |

(Counts to be computed from actual metadata; numbers here are illustrative.)

---

### Phase 5: Create Migration Mapping (LIBRARIES Old → New IDs)

Document all ID migrations to the new ISO system, including internal renames you are already doing (e.g. `OBJ-LG-###` → `OBJ-###`, `TOOL-DEV-020` → `TOOL-020`).

Example structure:

```json
{
  "migration_map": {
    "TOOL-DEV-020": "TOL-020",
    "TOOL-DEV-021": "TOL-021",
    "TOOL-DEV-022": "TOL-022",
    "TOOL-DEV-023": "TOL-023",
    "TOOL-DEV-024": "TOL-024",
    "TOOL-DEV-025": "TOL-025",

    "OBJ-LG-001": "OBJ-001",
    "OBJ-LG-002": "OBJ-002",
    "OBJ-LG-003": "OBJ-003",
    "OBJ-LG-004": "OBJ-004",
    "OBJ-LG-005": "OBJ-005",
    "OBJ-LG-006": "OBJ-006",
    "OBJ-LG-007": "OBJ-007",
    "OBJ-LG-008": "OBJ-008",
    "OBJ-LG-009": "OBJ-009",
    "OBJ-LG-010": "OBJ-010",

    "SKL-060": "SKL-001",
    "SKL-061": "SKL-002"
  },
  "department_migrations": {
    "ADM": "AID"
  }
}
```

Include:

- Tool ID merges already planned in `COLLECT_AND_MATCH_TOOLS_PROMPT.md` (e.g., `TOOL-AI-012` vs `TOOL-AI-028`) where applicable.
- Any **deprecated IDs** (kept only in archive directories) clearly marked.

---

## Output Deliverables (LIBRARIES)

Generate the following files in `ENTITIES/LIBRARIES/Taxonomy/` (or similar):

### 1. LIBRARIES Master Taxonomy List

**File**: `LIBRARIES_Taxonomy_Master_List.csv`

- All LIBRARIES entities with **new ISO IDs**.
- Includes metadata: entity type, department, source, status.
- Sortable by entity type, department, and ID.

### 2. LIBRARIES Hierarchical Relationship Tree

**File**: `LIBRARIES_Taxonomy_Hierarchy_Tree.md`

- ASCII trees for key stacks, e.g.:
  - Lead Generation stack: Tools ↔ Workflows ↔ Skills ↔ Professions ↔ Objects.
  - MCP Automation stack.
  - Agentic engineering stack (Video_005) if integrated later.
- Clearly shows parent–child and dependency chains.

### 3. LIBRARIES Department Distribution Report

**File**: `LIBRARIES_Taxonomy_Department_Distribution.md`

- Entity counts by department and type (TOL, OBJ, ACT, WRF, SKL, PRF).
- Visual breakdown tables and narrative analysis.
- Notes on deprecated departments and mappings (ADM → AID).

### 4. LIBRARIES Migration Mapping File

**File**: `LIBRARIES_Taxonomy_Migration_Map.json`

- Old ID → new ID mappings for **all** LIBRARIES entities.
- Department migration mapping (ADM → AID).
- Bidirectional lookup support where needed.
- Optional validation metadata (e.g., checksums, timestamp, version).

### 5. LIBRARIES ISO Code Registry

**File**: `LIBRARIES_Taxonomy_ISO_Code_Registry.md`

- Complete list of all LIBRARIES 3-letter codes:
  - TOL, OBJ, ACT, WRF, SKL, PRF, XRF, RPD.
- Derivation rules and examples.
- Reserved codes for future LIBRARIES sub-entities.
- Department code registry reused from global ecosystem (AID, HRM, DEV, LGN, DGN, VID, SLS).

---

## Validation Rules (LIBRARIES)

1. **Uniqueness**: Each `{XXX}-{###}` code is globally unique within LIBRARIES (no two entities share the same New_ID).
2. **Sequential**: IDs within each Entity Type (TOL, OBJ, ACT, WRF, SKL, PRF, XRF, RPD) are sequential with no gaps for the initial taxonomy pass.
3. **Consonant-only where possible**: ISO codes avoid vowels (A, E, I, O, U); exceptions like `OBJ` must be explicitly documented in the ISO registry.
4. **Case**: All codes are uppercase.
5. **Length**: Exactly `3 letters + "-" + 3 digits` (e.g., `TOL-001`, `OBJ-010`).
6. **Department codes**: Use the active department codes (AID, HRM, DEV, LGN, DGN, VID, SLS) consistent with the broader ecosystem.
7. **Migration safety**:
   - All old IDs remain resolvable via `LIBRARIES_Taxonomy_Migration_Map.json`.
   - Archive/backup directories (`Archive/`, `Taxonomy_Backup_*/`, `DEPARTMENT_CONSOLIDATION_BACKUP_*`) may preserve historical IDs but must be listed in the migration map for clarity.
8. **Cross-reference integrity**:
   - All references in cross-reference files and profession files must be updated to new IDs and pass a consistency check.

---

## Directory Structure Reference (LIBRARIES)

```text
LIBRARIES/
├── Tools/                         # TOL-###
│   ├── AI_Tools/
│   ├── Automation_Tools/
│   ├── Data_Tools/
│   ├── Business_Tools/
│   ├── Development_Tools/
│   ├── Cloud_Platforms/
│   ├── Integration_Tools/
│   ├── Social_Media_Platforms/
│   └── Video_Editing_Tools/
│
├── Responsibilities/
│   └── Objects/                   # OBJ-###
│       ├── Lead_Generation_Objects.json
│       ├── AI_Automation_Objects.json
│       ├── RAG_Objects.json
│       ├── Video_Generation_Objects.json
│       └── ...
│
├── Actions/                       # ACT-###
│   └── Data_Operations/
│       ├── Scrape.json
│       ├── Enrich.json
│       ├── Parse.json
│       └── ...
│
├── Processes/
│   └── Workflows/                 # WRF-###
│       ├── Lead_Generation_Workflows.json
│       ├── AI_Automation_Workflows.json
│       └── Workflows_Index.json
│
├── Skills/                        # SKL-###
│   └── Lead_Generation_and_AI_Skills.json
│
├── Professions/                   # PRF-###
│   ├── Lead_Generator.json
│   ├── SDR.json
│   ├── Backend_Developer.json
│   ├── AI_Engineer.json
│   └── ...
│
├── Prompts/                       # RPD-###
│   ├── Phase_2_Complete_Summary_Report.md
│   ├── Video_006_Library_Mapping_Report.md
│   ├── Video_008_Library_Mapping_Report.md
│   └── Tool_Validation_Report_Video_006_008.md
│
├── Cross_Reference_Mapping_Video_006_008.json   # XRF-### 
├── LIBRARIES_Import_Index.md                    # RPD-###
└── Taxonomy/                                    # New taxonomy outputs (CSV/JSON/MD)
```

---

## Expected Timeline (LIBRARIES)

- **Phase 1 – Inventory**: Scan all LIBRARIES directories and extract metadata.
- **Phase 2 – Master List**: Generate `LIBRARIES_Taxonomy_Master_List.csv`.
- **Phase 3 – Relationships**: Build `LIBRARIES_Taxonomy_Hierarchy_Tree.md`.
- **Phase 4 – Department Distribution**: Produce `LIBRARIES_Taxonomy_Department_Distribution.md`.
- **Phase 5 – Migration**: Create `LIBRARIES_Taxonomy_Migration_Map.json` and `LIBRARIES_Taxonomy_ISO_Code_Registry.md`.

---

## Success Criteria (LIBRARIES)

- ✓ All existing LIBRARIES entities catalogued with **new ISO codes** (TOL/OBJ/ACT/WRF/SKL/PRF/XRF/RPD).
- ✓ Zero duplicate IDs across the LIBRARIES taxonomy.
- ✓ All cross-references (Tools ↔ Workflows ↔ Skills ↔ Professions ↔ Objects) updated and consistent.
- ✓ Migration map covers all old IDs in active directories; archive locations clearly documented.
- ✓ Department distributions computed and validated against profession/tool usage.
- ✓ All deliverables generated and stored under a clear `LIBRARIES/Taxonomy/` namespace.
- ✓ Validation rules passed 100%, and the system is ready for future phases (e.g., aligning LIBRARIES and TASK_MANAGERS taxonomies end-to-end).


