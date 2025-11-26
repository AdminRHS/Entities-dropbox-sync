# RESEARCHES / VIDEO_RESEARCHES Entity Integration Prompt

## Objective
Design and integrate a new `RESEARCHES` entity into the ENTITIES ecosystem, with a focused sub-entity `VIDEO_RESEARCHES` that consolidates prompts, research inputs, and analysis outputs related to video-focused research.

The prompt guides the system (and human collaborators) through:
- Defining the scope and structure of `RESEARCHES` and `VIDEO_RESEARCHES`.
- Designing the file system under `C:\Users\Dell\Dropbox\ENTITIES\RESEARCHES`.
- Integrating existing assets from:
  - `C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\Video_Processing`
  - `C:\Users\Dell\Dropbox\ENTITIES\REPORTS\Influencer_Tracking`
  - `C:\Users\Dell\Dropbox\ENTITIES\REPORTS\Videos`
- Aligning taxonomy and IDs with existing RESEARCHES distribution (e.g. `RESEARCHES_Department_Distribution.md`).

---

## Step 1: Scope & Structure Definition

**Prompt:**
```markdown
You are an expert system architect and taxonomy designer.
We are integrating a new ENTITY into the ecosystem.

**Root Entity Name:** RESEARCHES
**Sub-Entity Name:** VIDEO_RESEARCHES

### 1.1 RESEARCHES Entity Scope

#Action:Define
Please define the scope and purpose of the `RESEARCHES` entity.
1. What is the primary function of `RESEARCHES` in the ENTITIES ecosystem?
2. Which departments does it serve (e.g., AI, LGN, Video, DEV)?
3. What types of research artifacts should live here (e.g., raw notes, structured reports, gap analyses, distribution summaries)?
4. How should `RESEARCHES` relate to existing entities like `REPORTS`, `TASK_MANAGERS`, and `LIBRARIES`?

### 1.2 VIDEO_RESEARCHES Sub-Entity Scope

#Action:Define
Please define the specific scope of `VIDEO_RESEARCHES` as a sub-entity of `RESEARCHES`.
1. What kinds of video-related research should be grouped here (tools, workflows, SMM/Influencer research, performance studies, etc.)?
2. How should `VIDEO_RESEARCHES` use or aggregate content from:
   - `PROMPTS/Video_Processing` (prompt workflows)
   - `REPORTS/Influencer_Tracking` (influencer & SMM data)
   - `REPORTS/Videos` (video research reports, analysis outputs)
3. What are the key deliverables of `VIDEO_RESEARCHES` (e.g., standardized research templates, dashboards, integration reports)?
4. Which other entities must it link to (e.g., `TASK_MANAGERS` tasks, `LIBRARIES` Tools, `ACCOUNTS`)?
```

---

## Step 2: File System Setup for RESEARCHES / VIDEO_RESEARCHES

**Target Root:** `C:\Users\Dell\Dropbox\ENTITIES\RESEARCHES`

**Prompt:**
```markdown
Based on the defined scope, we need to set up the file system for the `RESEARCHES` entity and its `VIDEO_RESEARCHES` sub-entity.

#Action:Setup

1. Under `C:\Users\Dell\Dropbox\ENTITIES\`, create the root entity folder:
   - `RESEARCHES`  # main entity

2. Inside `RESEARCHES`, create at minimum:
   - `TAXONOMY\`                # taxonomy docs for RESEARCHES
   - `INDEXES\`                 # indices, catalogs, and distributions
   - `RESEARCHES\`        # sub-entity root

3. Inside `TASK_MANAGERS/RESEARCHES/VIDEO_RESEARCHES`, create:
   - `PROMPTS\`                 # specialized prompts for video research
   - `REPORTS\`                 # research outputs, analyses, gap reports
   - `DATA\`                    # structured data, JSON/CSV, extracted signals
   - `MAPPINGS\`                # mapping files linking to other entities

4. Prepare at least 3 example placeholder files to validate the structure, for example:
   - `TASK_MANAGERS/RESEARCHES/TAXONOMY/RESEARCHES_Taxonomy_DRAFT.md`
   - `PROMPTS/VIDEO_RESEARCHES_Prompt_Examples.md`
   - `TASK_MANAGERS/RESEARCHES/REPORTS/VIDEO_RESEARCHES_Example_Report.md`

5. **Task:**
Generate the necessary PowerShell commands to create these directories and placeholder files without overwriting any existing content.
```

---

## Step 3: Taxonomy & ID System Integration

Use existing taxonomy work such as:
- `C:\Users\Dell\Dropbox\ENTITIES\REPORTS\Taxonomy\RESEARCHES_Department_Distribution.md`

**Prompt:**
```markdown
We now need to define the taxonomy and ID system for `RESEARCHES` and `VIDEO_RESEARCHES`.

#Action:Integrate

### 3.1 ID Prefixes
1. Propose an ID prefix for the `RESEARCHES` entity (e.g., `RSH` or `RSH-ALL`).
2. Propose a more specific prefix or pattern for `VIDEO_RESEARCHES` (e.g., `RSH-VID-###` or `VID-RSH-###`).
3. Ensure the prefixes do not conflict with existing entities (PROMPTS PMT-###, TASK_MANAGERS IDs, etc.).

### 3.2 File Naming Conventions
Define naming patterns for:
1. **Research prompts** in `PROMPTS/`.
   - Example pattern: `RSH-VID-###_Video_Research_Title.md`
2. **Research reports / outputs** in `TASK_MANAGERS/RESEARCHES/REPORTS/`.
   - Example pattern: `RSH-VID-###_Report_Type_Description.md`
3. **Data files** in `TASK_MANAGERS/RESEARCHES/DATA/`.
   - Example pattern: `RSH-VID-###_Data_Type_YYYY-MM-DD.ext`

### 3.3 TAXONOMY.md for RESEARCHES

**Task:**
Draft the content of `C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES\TAXONOMY\TAXONOMY.md` including:
1. Description of the `RESEARCHES` entity and its relationship to departments (AI, LGN, VID, DEV, etc.).
2. Definition of `VIDEO_RESEARCHES` as a sub-entity, including scope and typical use cases.
3. ID and naming rules defined above.
4. How research entities should reference:
   - Existing prompts in `PROMPTS/Video_Processing`.
   - Reports in `REPORTS/Influencer_Tracking` and `REPORTS/Videos`.
   - Any relevant TASK_MANAGERS tasks or LIBRARIES entries (Tools, Actions, Objects).
```

---

## Step 4: Integration of Existing Assets

We want to **link and/or migrate** related content into the new entity, without breaking history.

Relevant existing locations:
- `C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\Video_Processing`
- `C:\Users\Dell\Dropbox\ENTITIES\REPORTS\Influencer_Tracking`
- `C:\Users\Dell\Dropbox\ENTITIES\REPORTS\Videos`

**Prompt:**
```markdown
#Action:Map

1. Scan the following locations and produce a structured mapping of candidate items to the new entity:
   - `PROMPTS/Video_Processing/` (Analysis, Transcription, Workflows, Taxonomy_Integration)
   - `REPORTS/Influencer_Tracking/`
   - `REPORTS/Videos/`

2. For each candidate file, capture:
   - Source path
   - Department / domain (AI, LGN, Video, etc.)
   - Type (Prompt, Research Report, Gap Analysis, Tracking, etc.)
   - Recommended target within `TASK_MANAGERS/RESEARCHES/` (PROMPTS, REPORTS, DATA, MAPPINGS)
   - Whether it should be **moved**, **copied**, or just **referenced** via link.

3. Generate a `MAPPINGS` file draft:
   - `TASK_MANAGERS/RESEARCHES/MAPPINGS/VIDEO_RESEARCHES_Source_Mapping.md`
   - Include a table of all mapped items with recommended actions.

4. **Optional:** Propose a migration plan (phased) that:
   - Avoids breaking existing PMT references.
   - Keeps REPORTS and PROMPTS indexes consistent.
```

---

## Step 5: Documentation & Central Taxonomy Update

**Prompt:**
```markdown
#Action:Update

1. Update central taxonomy documentation to register the new `RESEARCHES` entity and its `VIDEO_RESEARCHES` sub-entity.
   - Target: `C:\Users\Dell\Dropbox\ENTITIES\TAXONOMY\TAX-004_Entity_Integration\Entity_Integration_Taxonomy.md` (or current master list).

2. Provide the markdown block to append, including:
   - Entity name: RESEARCHES
   - Sub-entity: VIDEO_RESEARCHES
   - ID prefixes and naming patterns
   - Root path: `ENTITIES/TASK_MANAGERS/RESEARCHES/`
   - Key integration points (PROMPTS/Video_Processing, REPORTS/Influencer_Tracking, REPORTS/Videos).

3. Ensure consistency with `RESEARCHES_Department_Distribution.md` in REPORTS taxonomy.
```

---

## Step 6: Verification Checklist

**Prompt:**
```markdown
#Action:Verify

### 6.1 File System
- [ ] `ENTITIES/TASK_MANAGERS/RESEARCHES/` exists.
- [ ] `ENTITIES/TASK_MANAGERS/RESEARCHES/TAXONOMY/` exists with `TAXONOMY.md`.
- [ ] `ENTITIES/TASK_MANAGERS/RESEARCHES/` exists.
- [ ] `PROMPTS`, `REPORTS`, `DATA`, and `MAPPINGS` subfolders exist under `VIDEO_RESEARCHES`.

### 6.2 Taxonomy & IDs
- [ ] ID prefixes for RESEARCHES and VIDEO_RESEARCHES are defined and documented.
- [ ] Naming conventions for prompts, reports, and data files are documented.
- [ ] Central `Entity_Integration_Taxonomy` (or equivalent) is updated.

### 6.3 Integration & Mapping
- [ ] Mapping file created at `TASK_MANAGERS/RESEARCHES/MAPPINGS/VIDEO_RESEARCHES_Source_Mapping.md`.
- [ ] All key video-related research prompts and reports from:
      - `PROMPTS/Video_Processing`
      - `REPORTS/Influencer_Tracking`
      - `REPORTS/Videos`
      are either linked, copied, or scheduled for migration.

### 6.4 Quality & Consistency
- [ ] Sample files validated for naming and taxonomy compliance.
- [ ] No broken references in PROMPTS or REPORTS indexes.
- [ ] RESEARCHES structure aligns with department distribution (AI, LGN, VID, DEV, etc.).

**Task:**
Summarize the verification results and list any remaining gaps or follow-up tasks.
```
