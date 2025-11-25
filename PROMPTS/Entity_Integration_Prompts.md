# Entity Integration Prompts

This guide provides a multi-step prompt sequence for integrating a new ENTITY into the ecosystem, following the "File System Improvement" project structure.

## Step 1: Scope & Objective Definition

**Prompt:**
```markdown
You are an expert system architect. We are integrating a new ENTITY into our ecosystem.
**Entity Name:** [Insert Entity Name, e.g., REPORTS]
**Objective:** Create a structured environment for this entity to support [Insert Goal, e.g., daily reporting, tracking].

#Action:Define
Please define the scope and specific objectives for this integration.
1. What is the primary function of this entity?
2. How does it interact with existing entities (e.g., DEPARTMENTS, TASK_MANAGERS)?
3. What are the key deliverables for this integration?
```

## Step 2: File System Setup

**Prompt:**
```markdown
Based on the defined scope, we need to set up the file system.
#Action:Setup
1. Create a new directory in `C:\Users\Dell\Dropbox\ENTITIES\` named `[Entity Name]`.
2. Inside this directory, create the standard subdirectories if applicable (e.g., `DATA`, `DOCS`).
3. Import at least 3 example files to populate the directory for testing.

**Task:**
Generate the necessary shell commands (PowerShell) to create these directories and dummy example files.
```

## Step 3: Taxonomy & IDS Integration

**Prompt:**
```markdown
Now we need to establish the taxonomy and integrate with the IDS system.
#Action:Integrate
**Requirements:**
1. **Taxonomy:** Define the classification structure for files within this entity. How should they be named? (e.g., `[Entity_Prefix]-[ID]_[Description]`).
2. **IDS System:** Assign a unique ID prefix for this entity (e.g., `RPT` for Reports).
3. **Classification:** Create a classification scheme (e.g., Type A, Type B).

**Task:**
Draft a `TAXONOMY.md` file for this new entity that documents these rules.
```

## Step 4: Documentation Update

**Prompt:**
```markdown
We must ensure the central ecosystem documentation reflects this new addition.
#Action:Update
**Target File:** `C:\Users\Dell\Dropbox\ENTITIES\TAXONOMY\TAX-004_Entity_Integration\Entity_Integration_Taxonomy.md` (or central master list).

**Task:**
Provide the markdown content to append to the central taxonomy documentation, registering the new entity, its ID prefix, and its location.
```

## Step 5: Verification

**Prompt:**
```markdown
Finally, verify the integration.
#Action:Verify
**Checklist:**
- [ ] Folder `ENTITIES\[Entity Name]` exists.
- [ ] Example files are present.
- [ ] `TAXONOMY.md` is created in the entity folder.
- [ ] Central taxonomy documentation is updated.

**Task:**
Run a verification script or manually check these items and report the status.
```

---

## Example: TASK_MANAGERS Full Cycle

This example demonstrates how to apply the above steps to the `TASK_MANAGERS` entity, creating a full hierarchy of Project -> Milestone -> Task.

### 1. Scope
**Entity:** TASK_MANAGERS
**Objective:** Manage Projects (PRT), Milestones (MLT), and Tasks (TST).

### 2. File System
```powershell
New-Item -Path "C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS" -ItemType Directory
New-Item -Path "C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\DATA" -ItemType Directory
New-Item -Path "C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\PROMPTS" -ItemType Directory
```

### 3. Taxonomy & IDS
**Prefixes:**
- `PRT`: Projects
- `MLT`: Milestones
- `TST`: Tasks

**Hierarchy:**
`PRT-001` (Project) -> `MLT-001` (Milestone) -> `TST-001` (Task)

### 4. Example Files
- `PRT-001_Website_Redesign.md`
- `MLT-001_Design_Phase.md` (#Action:Link)
- `TST-001_Create_Mockups.md` (#Action:Link)

### 5. Verification
- Check that `TST-001` correctly references `MLT-001`.
- Check that `MLT-001` correctly references `PRT-001`.
