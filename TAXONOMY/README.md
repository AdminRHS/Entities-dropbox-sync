# TAXONOMY Entity Documentation

**Entity Type:** TAXONOMY  
**Domain:** Knowledge Graph / Classification  
**Purpose:** Central hub for IDs, hierarchies, and ISO-style codes across all ENTITIES  
**Created:** 2025-11-19  
**Last Updated:** 2025-11-19

---

## 📋 Overview

The **TAXONOMY** entity provides a **single place to understand IDs and classification systems** used across the ENTITIES workspace.

Instead of replacing the existing taxonomy files in `LIBRARIES`, `TASK_MANAGERS`, or `PROMPTS`, this entity acts as a:

- **Navigation hub** for all taxonomy artifacts
- **Documentation layer** that explains how IDs and ISO codes are structured
- **Integration point** for future automation (agents, scripts, dashboards)

All canonical data remains in the original entities. The `ENTITIES/TAXONOMY` folder contains **mirrored views** and **documentation** that keep everything discoverable and consistent.

---

## 🗂️ Sub-Entities & Artifacts

### 1. LIBRARIES Taxonomy

**Purpose:** IDs and codes for responsibilities, actions, objects, tools, professions, departments, and related library entities.

**Mirrored Location (this entity):**

- `TAXONOMY/TAX-001_Libraries/`
  - `Libraries_Master_List.csv`
  - `Libraries_ISO_Code_Registry.md`
  - `Libraries_Hierarchy_Tree.md`
  - `Libraries_Department_Distribution.md`
  - `Libraries_Migration_Map.json`

**Canonical Source Location:**

- `ENTITIES/LIBRARIES/Taxonomy/`

**What it contains:**

- **Libraries_Master_List.csv** – master catalog of all LIBRARIES entities (RSP, ACT, OBJ, PRM, TOL, PRF, DPT, etc.) with:
  - Entity_ID, Entity_Name, Entity_Type, Department, Category, File_Path, Count, Status
- **Libraries_ISO_Code_Registry.md** – rules + registry for LIBRARIES ISO-style codes (RSP, ACT, OBJ, PRM, TOL, SKL, PRF, DPT, department codes, etc.)
- **Libraries_Hierarchy_Tree.md** – hierarchical view of how library entities relate
- **Libraries_Department_Distribution.md** – statistics by department
- **Libraries_Migration_Map.json** – migration mapping for legacy → new IDs/paths

Use this when you need to **look up or assign IDs for LIBRARIES entities.**

---

### 2. TASK_MANAGERS Taxonomy

**Purpose:** IDs and codes for project templates, milestone templates, task templates, workflows, guides, prompts, and research items in TASK_MANAGERS.

**Mirrored Location (this entity):**

- `TAXONOMY/TAX-002_Task_Managers/`
  - `Taxonomy_Master_List.csv`
  - `Taxonomy_ISO_Code_Registry.md`
  - `Taxonomy_Hierarchy_Tree.md`
  - `Taxonomy_Department_Distribution.md`
  - `Taxonomy_Migration_Map.json`

**Canonical Source Location:**

- `ENTITIES/TASK_MANAGERS/Taxonomy/`

**What it contains:**

- **Taxonomy_Master_List.csv** – catalog spanning:
  - Project Templates (PRJ-*), Milestone Templates (MLS-*), Task Templates (TSK-*), Workflows (WRF-*), Guides (GDS-*), Prompts (PRM-* references), Researches (RSR-*), Prompt categories (PMT-*), etc.
  - Columns: New_ID, Entity_Type, Current_ID, Name, Description, Department, File_Path, Status
- **Taxonomy_ISO_Code_Registry.md** – TASK_MANAGERS ISO-style codes (PRT, MLT, TST, STT, CHT, WRF, GDS, PRM, RSR) and department codes (AID, HRM, DEV, LGN, DGN, VID, SLS), with rules and ranges.
- **Taxonomy_Hierarchy_Tree.md** – hierarchy from project templates down to checklist templates.
- **Taxonomy_Department_Distribution.md** – department distributions.
- **Taxonomy_Migration_Map.json** – migration mapping for IDs and structures.

Use this when you need to **map workflows, templates, or guides to IDs** or align TASK_MANAGERS with other entities.

---

### 3. PROMPTS – Video Processing Taxonomy Integration

**Purpose:** Document how video research and processing pipelines feed into taxonomy updates.

**Mirrored Location (this entity):**

- `TAXONOMY/TAX-003_Video_Processing/`
  - `PMT-009_Taxonomy_Integration.md`

**Canonical Source Locations:**

- `ENTITIES/PROMPTS/PROMPTS/Taxonomy_Integration/PMT-009_Taxonomy_Integration.md`
- Prompt metadata in: `ENTITIES/TASK_MANAGERS/Taxonomy/Taxonomy_Master_List.csv` (rows for video/taxonomy prompts)
- PROMPTS index: `ENTITIES/TASK_MANAGERS/PROMPTS/PROMPTS_Master_List.csv` and `ENTITIES/PROMPTS/PROMPTS_INDEX.json`

Use this when you need to **connect research/transcription workflows to taxonomy changes**, especially for video sources.

---

### 4. Entity Integration Taxonomy

**Purpose:** Standard workflow and taxonomy for integrating new ENTITIES (e.g. REPORTS).

**Mirrored Location (this entity):**

- `TAXONOMY/TAX-004_Entity_Integration/Entity_Integration_Taxonomy.md`

**Canonical Source Location:**

- `ENTITIES/TAXONOMY/Entity_Integration_Taxonomy.md` (Self-contained)

**What it contains:**

- Standard 6-step integration workflow (Create Folder, Add Taxonomy, etc.).
- Definitions for `#Action` tags.
- Example `TASK_MANAGERS` full cycle integration.

Use this when you need to **create a new ENTITY** in the ecosystem.

---

### 5. REPORTS Taxonomy

**Purpose:** IDs and classification for Daily, Weekly, and Ad-hoc reports.

**Mirrored Location (this entity):**

- *None yet (direct link to canonical)*

**Canonical Source Location:**

- `ENTITIES/REPORTS/TAXONOMY.md`

**What it contains:**

- **IDS System:** `RPT-[ID]`
- **Classification:** `RPT-DLY`, `RPT-WKY`, `RPT-ADH`
- **Naming Conventions:** `[Prefix]-[Type]_[Department]_[Date]_[Description].ext`

Use this when you need to **generate or look up reports**.

---

## 🧾 ID Systems (High-Level)

The TAXONOMY entity does **not** introduce new ID formats. Instead, it documents and connects the ID systems already defined in LIBRARIES and TASK_MANAGERS.

### 1. LIBRARIES IDs (content-focused)

Defined and maintained in:

- `TAXONOMY/TAX-001_Libraries/Libraries_Master_List.csv`
- `TAXONOMY/TAX-001_Libraries/Libraries_ISO_Code_Registry.md`

**Examples:**

- Responsibilities: `RSP-001`, `RSP-002`, ...
- Actions: `ACT-001`, ... (with subcodes like ACT-CMD, ACT-PRC, ACT-RST)
- Objects: `OBJ-001`, ...
- Tools: `TOL-001`, ...
- Professions: `PRF-001`, ...
- Departments: `DPT-001`, ...

Use these IDs when you:

- Link TASK_MANAGERS templates to LIBRARIES responsibilities/objects/tools.
- Map TALENTS skills/professions to LIBRARIES definitions.

### 2. TASK_MANAGERS IDs (workflow-focused)

Defined and maintained in:

- `TAXONOMY/TAX-002_Task_Managers/Taxonomy_Master_List.csv`
- `TAXONOMY/TAX-002_Task_Managers/Taxonomy_ISO_Code_Registry.md`

**Examples:**

- Project Templates: `PRJ-001`, ... mapped to PRT codes
- Milestone Templates: `MLS-00X` mapped to MLT
- Task Templates: `TSK-00X` mapped to TST
- Workflows: `WRF-00X`
- Guides: `GDS-00X`
- Prompts: `PRM-00X`
- Research: `RSR-00X`

Use these IDs when you:

- Track workflows and templates across departments.
- Connect prompts/researches to concrete actions, objects, and responsibilities.

### 3. PROMPTS & Taxonomy Prompts

Prompt taxonomy is defined primarily in:

- `ENTITIES/TASK_MANAGERS/Taxonomy/Taxonomy_Master_List.csv` (rows with `Entity_Type = Prompt` or `Prompt_Category`)
- `ENTITIES/TASK_MANAGERS/PROMPTS/PROMPTS_Master_List.csv` (per-prompt rows including `PRM-TX-001` etc.)
- `ENTITIES/PROMPTS/Taxonomy/` (prompt files used to build and maintain taxonomy)

TAXONOMY entity references these as **drivers of change** rather than adding a separate ID layer.

---

## 🔗 Relationships

### Primary Relationships

1. **TAXONOMY ↔ LIBRARIES**
   - LIBRARIES defines core content entities: responsibilities, actions, objects, tools, professions, departments.
   - TAXONOMY documents how these entities are **coded**, **counted**, and **distributed** via master lists and ISO registries.

2. **TAXONOMY ↔ TASK_MANAGERS**
   - TASK_MANAGERS defines workflows, templates, and operational structures.
   - TAXONOMY documents the **ID system for all templates and workflows**, enabling reporting and cross-entity mapping.

3. **TAXONOMY ↔ PROMPTS**
   - PROMPTS drive research, analysis, and updates to taxonomy.
   - TAXONOMY records the **resulting structures and IDs**, especially for video processing and research-driven pipelines.

4. **TAXONOMY ↔ TALENTS / JOBS / ACCOUNTS / BUSINESSES** (indirect)
   - TALENTS uses professions and skills that are defined in LIBRARIES and tracked via IDs.
   - JOBS and ACCOUNTS rely on department/profession/tool taxonomies for consistent structure.
   - TAXONOMY helps keep these references **consistent and auditable**.

---

## 📍 Quick Navigation

Use these links when working with taxonomy:

- **LIBRARIES Taxonomy (content):**
  - `TAXONOMY/TAX-001_Libraries/Libraries_Master_List.csv`
  - `TAXONOMY/TAX-001_Libraries/Libraries_ISO_Code_Registry.md`
  - `TAXONOMY/TAX-001_Libraries/Libraries_Hierarchy_Tree.md`
  - `TAXONOMY/TAX-001_Libraries/Libraries_Department_Distribution.md`

- **TASK_MANAGERS Taxonomy (workflows):**
  - `TAXONOMY/TAX-002_Task_Managers/Taxonomy_Master_List.csv`
  - `TAXONOMY/TAX-002_Task_Managers/Taxonomy_ISO_Code_Registry.md`
  - `TAXONOMY/TAX-002_Task_Managers/Taxonomy_Hierarchy_Tree.md`
  - `TAXONOMY/TAX-002_Task_Managers/Taxonomy_Department_Distribution.md`

- **PROMPTS – Video Processing Taxonomy Integration:**
  - `TAXONOMY/TAX-003_Video_Processing/PMT-009_Taxonomy_Integration.md`

- **Entity Integration Taxonomy:**
  - `TAXONOMY/TAX-004_Entity_Integration/Entity_Integration_Taxonomy.md`

- **REPORTS Taxonomy:**
  - `ENTITIES/REPORTS/TAXONOMY.md`

---

## 🧩 How To Extend the TAXONOMY Entity

When you add new taxonomy structures:

1. **Decide the home entity**
   - Content-focused (responsibilities, actions, objects, tools, professions, departments) → **LIBRARIES**
   - Workflow-focused (projects, milestones, tasks, steps, checklists, workflows, guides, research) → **TASK_MANAGERS**
   - Prompt/automation-focused integration → **PROMPTS** (with references logged in TASK_MANAGERS taxonomy where appropriate)

2. **Assign IDs following existing rules**
   - Use the next available ID in the relevant master list (e.g. `Libraries_Master_List.csv`, `Taxonomy_Master_List.csv`).
   - Ensure ISO-style codes are compliant with:
     - `Libraries_ISO_Code_Registry.md`
     - `Taxonomy_ISO_Code_Registry.md`

3. **Update the relevant master/registry files**
   - Add rows to the appropriate `*_Master_List.csv` file.
   - If a new code family is introduced, update the corresponding ISO registry.

4. **(Optional) Add navigation notes here**
   - If you introduce a new taxonomy area (e.g. ACCOUNTS taxonomy, JOBS taxonomy), add a new subsection under **Sub-Entities & Artifacts** in this README pointing to its master list and registry.

---

## 📊 Example Usage Scenarios

- **From a TASK_MANAGERS template:**
  - Use `Taxonomy_Master_List.csv` to find the template's ID and map it to LIBRARIES entities via RSP/ACT/OBJ/TOL IDs.

- **From a LIBRARIES responsibility:**
  - Use `Libraries_Master_List.csv` + TASK_MANAGERS taxonomy to discover which tasks, workflows, and prompts reference that responsibility.

- **From a PROMPT file:**
  - Use PROMPTS indices + TAXONOMY master lists to see which workflows and content structures the prompt reads/writes.

---

**Status:** Active  
**Owner:** Taxonomy / Architecture Team
