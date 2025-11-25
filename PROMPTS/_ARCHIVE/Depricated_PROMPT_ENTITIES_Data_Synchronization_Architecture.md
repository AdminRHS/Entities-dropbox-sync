# PROMPT: ENTITIES Data Synchronization Architecture

## Objective

Define comprehensive data synchronization patterns, cross-entity relationships, ID mapping strategies, and consistency rules to ensure data integrity and real-time synchronization across all ENTITIES (LIBRARIES, TASK_MANAGERS, TALENTS, BUSINESSES, JOBS, ACCOUNTS, ANALYTICS).

---

## 1. Entity Ecosystem Overview

### 1.1 Core Entities

| Entity | Domain | Purpose | ID Format | Key Sub-Entities |
|--------|--------|---------|-----------|-------------------|
| **LIBRARIES** | Knowledge Base | Centralized repository of reusable components | `{XXX}-{###}` (TOL-001, PRF-001) | Actions, Objects, Tools, Skills, Professions, Parameters |
| **TASK_MANAGERS** | Operational Engine | Orchestrates work execution | `TASK-{###}` | Projects, Milestones, Tasks, Step Templates |
| **TALENTS** | Human Capital | Manages talent lifecycle | `EMP-{###}` | Employees, Candidates, Skills, Job Applications |
| **BUSINESSES** | Client Lifecycle | Tracks business relationships | `BUS-{###}` | Clients, Prospects, Companies, Ex_Clients |
| **JOBS** | Talent Marketplace | Manages job openings | `JOB-{###}` | Job Postings, Requirements, Templates |
| **ACCOUNTS** | Access Management | Account verification and access | `ACC-{###}`, `VER-{###}` | Accounts, Verifications, Job Accounts |
| **ANALYTICS** | Performance Data | Tracks metrics and analytics | `PROJ-{###}` | Projects, Tasks, Steps, Milestones, Reports |

### 1.2 Entity Relationships Matrix

```
LIBRARIES
├── → TASK_MANAGERS (Tasks use Actions + Objects + Tools)
├── → TALENTS (Employees have Professions + Skills + Tool proficiency)
├── → JOBS (Jobs reference Professions + Skills + Tools)
└── → BUSINESSES (Products/Services reference Tools + Objects)

TASK_MANAGERS
├── → TALENTS (Tasks assigned to Employees)
├── → BUSINESSES (Client-related tasks)
└── → LIBRARIES (Tasks composed of Actions + Objects)

TALENTS
├── → JOBS (Employees apply to Jobs)
├── → BUSINESSES (Talents assigned to Client projects)
├── → TASK_MANAGERS (Employees assigned to Tasks)
└── → LIBRARIES (Employees have Professions + Skills)

BUSINESSES
├── → JOBS (Clients post Jobs)
├── → TALENTS (Clients matched with Talents)
└── → TASK_MANAGERS (Client onboarding tasks)

JOBS
├── → TALENTS (Jobs require specific Talents)
├── → BUSINESSES (Jobs posted by Clients)
└── → LIBRARIES (Jobs reference Professions + Skills)
```

---

## 2. ID System Architecture

### 2.1 LIBRARIES Taxonomy IDs

**Format:** `{XXX}-{###}` where `XXX` = 3-letter ISO code, `###` = 3-digit sequential ID

| Entity Type | ISO Code | Example | Range |
|-------------|----------|---------|-------|
| Tools | TOL | TOL-001 | TOL-001 to TOL-999 |
| Objects | OBJ | OBJ-001 | OBJ-001 to OBJ-999 |
| Actions | ACT | ACT-001 | ACT-001 to ACT-999 |
| Workflows | WRF | WRF-001 | WRF-001 to WRF-999 |
| Skills | SKL | SKL-001 | SKL-001 to SKL-999 |
| Professions | PRF | PRF-001 | PRF-001 to PRF-999 |
| Departments | DPT | DPT-001 | DPT-001 to DPT-999 |
| Statuses | STS | STS-001 | STS-001 to STS-999 |
| Parameters | PRM | PRM-001 | PRM-001 to PRM-999 |
| Countries | CNT | CNT-001 | CNT-001 to CNT-999 |
| Currencies | CRC | CRC-001 | CRC-001 to CRC-999 |

### 2.2 Cross-Entity ID Mapping

**Mapping Rules:**

1. **LIBRARIES → TALENTS**: Professions (PRF-###) referenced in Employee profiles
2. **LIBRARIES → TASK_MANAGERS**: Actions (ACT-###), Objects (OBJ-###), Tools (TOL-###) referenced in Tasks
3. **LIBRARIES → JOBS**: Professions (PRF-###), Skills (SKL-###) referenced in Job requirements
4. **TALENTS → TASK_MANAGERS**: Employee IDs (EMP-###) referenced in Task assignments
5. **BUSINESSES → JOBS**: Business IDs (BUS-###) referenced in Job postings
6. **JOBS → TALENTS**: Job IDs (JOB-###) referenced in Job Applications

### 2.3 ID Synchronization Rules

**Rule 1: Single Source of Truth**

- LIBRARIES IDs are authoritative for Tools, Actions, Objects, Professions, Skills
- Other entities reference LIBRARIES IDs, never duplicate them

**Rule 2: Referential Integrity**

- When a LIBRARIES entity is deleted/deprecated, all references must be updated
- Use migration mapping (`LIBRARIES_Taxonomy_Migration_Map.json`) to track ID changes

**Rule 3: ID Generation**

- New LIBRARIES entities: Assign next sequential ID within entity type
- Cross-entity references: Always use full ID format (`PRF-001`, not `001`)

**Rule 4: ID Validation**

- All IDs must match pattern: `{XXX}-{###}` where XXX is valid ISO code
- IDs must be unique within entity type
- Cross-references must resolve to existing entities

---

## 3. Data Synchronization Patterns

### 3.1 Unidirectional Synchronization (LIBRARIES → Other Entities)

**Pattern:** LIBRARIES is the source of truth; other entities consume LIBRARIES data

**Examples:**

- **LIBRARIES → TASK_MANAGERS**: When a new Tool (TOL-050) is added, Task Templates can reference it
- **LIBRARIES → TALENTS**: When a Profession (PRF-010) is updated, Employee profiles referencing it should reflect changes
- **LIBRARIES → JOBS**: When Skills (SKL-025) are added, Job requirements can reference them

**Synchronization Trigger:**

- On LIBRARIES entity creation/update
- Propagate changes to dependent entities via:

  1. Cross-reference index updates
  2. Validation scripts
  3. Manual review prompts

### 3.2 Bidirectional Synchronization (Cross-Entity References)

**Pattern:** Entities reference each other; changes require coordination

**Examples:**

- **TALENTS ↔ TASK_MANAGERS**: Employee (EMP-001) assigned to Task (TASK-100) creates bidirectional link
- **BUSINESSES ↔ JOBS**: Client (BUS-005) posts Job (JOB-020) creates bidirectional link
- **JOBS ↔ TALENTS**: Job (JOB-020) receives Application from Candidate (EMP-050)

**Synchronization Rules:**

1. **Create Link**: When relationship is created, update both entities
2. **Update Link**: When relationship changes, update both entities
3. **Delete Link**: When relationship ends, remove references from both entities

### 3.3 Cascading Updates

**Pattern:** Changes in one entity trigger updates in related entities

**Update Cascades:**

```
LIBRARIES Profession (PRF-010) Updated
├── → TALENTS: Update all Employee profiles with PRF-010
├── → JOBS: Update all Job postings requiring PRF-010
└── → TASK_MANAGERS: Update Task Templates requiring PRF-010 profession

LIBRARIES Tool (TOL-025) Deprecated
├── → TASK_MANAGERS: Flag Tasks using TOL-025 as "Needs Review"
├── → TALENTS: Update Employee tool proficiency lists
└── → JOBS: Update Job requirements referencing TOL-025

TALENTS Employee (EMP-001) Status Changed to "LEFT"
├── → TASK_MANAGERS: Reassign Tasks from EMP-001
├── → BUSINESSES: Notify clients if EMP-001 was on their projects
└── → ANALYTICS: Update performance metrics
```

### 3.4 Data Consistency Validation

**Validation Rules:**

1. **Cross-Reference Integrity**

   - All referenced IDs must exist in source entity
   - No orphaned references (ID points to non-existent entity)
   - No circular dependencies

2. **Schema Compliance**

   - All entities must conform to their JSON schemas
   - Required fields must be present
   - Data types must match schema definitions

3. **Naming Consistency**

   - Entity names must follow naming conventions
   - Department codes must match LIBRARIES/Departments
   - Status values must match LIBRARIES/Statuses

4. **ID Format Validation**

   - All IDs must match entity-specific format
   - ISO codes must be valid (from ISO registry)
   - Sequential IDs must not have gaps (for initial taxonomy)

---

## 4. Synchronization Mechanisms

### 4.1 Cross-Reference Index Files

**Purpose:** Maintain bidirectional lookup tables for entity relationships

**Location:** `ENTITIES/SYNC/Cross_Reference_Indexes/`

**Index Files:**

- `profession_to_employees.json` - Maps PRF-### → [EMP-###, ...]
- `tool_to_tasks.json` - Maps TOL-### → [TASK-###, ...]
- `employee_to_tasks.json` - Maps EMP-### → [TASK-###, ...]
- `client_to_projects.json` - Maps BUS-### → [PROJ-###, ...]
- `job_to_applications.json` - Maps JOB-### → [EMP-###, ...]

**Update Frequency:** On-demand when relationships change

### 4.2 Migration Mapping Files

**Purpose:** Track ID changes and maintain backward compatibility

**Location:** `ENTITIES/LIBRARIES/Taxonomy/LIBRARIES_Taxonomy_Migration_Map.json`

**Structure:**

```json
{
  "migration_map": {
    "old_id": "new_id",
    "TOOL-AI-028": "TOL-028",
    "OBJ-LG-001": "OBJ-001"
  },
  "department_migrations": {
    "ADM": "AID"
  },
  "deprecated_ids": ["TOL-999"],
  "last_updated": "2025-11-17"
}
```

**Usage:** When resolving old IDs in cross-references

### 4.3 Validation Scripts

**Purpose:** Automated consistency checking

**Scripts:**

- `validate_cross_references.py` - Checks all cross-entity references
- `validate_id_formats.py` - Validates ID formats match schemas
- `validate_schema_compliance.py` - Validates JSON schema compliance
- `detect_orphaned_references.py` - Finds broken cross-references

**Execution:** Weekly automated runs + on-demand before major updates

### 4.4 Synchronization Prompts

**Purpose:** AI-assisted synchronization workflows

**Prompts:**

- `PROMPT_Sync_LIBRARIES_to_TALENTS.md` - Update Employee profiles when LIBRARIES changes
- `PROMPT_Sync_TASK_MANAGERS_References.md` - Update Task references when LIBRARIES changes
- `PROMPT_Validate_Cross_Entity_Integrity.md` - Comprehensive validation workflow

---

## 5. Data Flow Patterns

### 5.1 LIBRARIES Population Flow

```
[Source Material: Video/Document/Manual]
    ↓
[Prompt Extraction]
    ↓
[Structured JSON Output]
    ↓
[Schema Validation]
    ↓
[LIBRARIES Population]
    ├── → Generate IDs (TOL-###, PRF-###, etc.)
    ├── → Create entity files
    ├── → Update master indexes
    └── → Create cross-references
    ↓
[Cross-Entity Notification]
    ├── → TASK_MANAGERS: New Tools available
    ├── → TALENTS: New Professions available
    └── → JOBS: New Skills available
```

### 5.2 Task Creation Flow

```
[Task Request]
    ↓
[Task Template Selection]
    ├── → References: ACT-### (Action), OBJ-### (Object)
    └── → References: TOL-### (Required Tools)
    ↓
[Employee Assignment]
    ├── → References: EMP-### (Employee)
    ├── → Validates: EMP-### has required Skills (SKL-###)
    └── → Validates: EMP-### has Tool proficiency (TOL-###)
    ↓
[Task Created: TASK-###]
    ├── → Links to: LIBRARIES (Actions, Objects, Tools)
    ├── → Links to: TALENTS (Employee)
    └── → Links to: BUSINESSES (if client-related)
```

### 5.3 Employee Profile Update Flow

```
[Employee Profile Update]
    ├── → Update: EMP-### profile
    ├── → References: PRF-### (Profession from LIBRARIES)
    ├── → References: [SKL-###, ...] (Skills from LIBRARIES)
    └── → References: [TOL-###, ...] (Tool proficiency from LIBRARIES)
    ↓
[Cross-Entity Updates]
    ├── → TASK_MANAGERS: Update Task assignment eligibility
    ├── → JOBS: Update Job matching scores
    └── → ANALYTICS: Update performance metrics
```

---

## 6. Conflict Resolution

### 6.1 ID Conflicts

**Scenario:** Two entities attempt to use same ID

**Resolution:**

1. Check if ID already exists in target entity
2. If exists: Assign next available sequential ID
3. Log conflict in `SYNC/conflict_log.json`
4. Update migration map if ID was changed

### 6.2 Reference Conflicts

**Scenario:** Entity references non-existent ID

**Resolution:**

1. Check migration map for old → new ID mapping
2. If mapped: Update reference to new ID
3. If not mapped: Flag as orphaned reference
4. Create issue in `SYNC/orphaned_references.json`
5. Prompt user to resolve or deprecate reference

### 6.3 Data Inconsistency

**Scenario:** Same entity has different data in different locations

**Resolution:**

1. Identify source of truth (usually LIBRARIES)
2. Compare versions (use timestamps)
3. Merge data (prefer more detailed/complete version)
4. Update all references to merged version
5. Document merge in `SYNC/merge_log.json`

---

## 7. Synchronization Workflows

### 7.1 Daily Synchronization Checklist

**Automated Tasks:**

- [ ] Validate all cross-references
- [ ] Check for orphaned references
- [ ] Verify ID format compliance
- [ ] Update cross-reference indexes
- [ ] Run schema validation

**Manual Review Tasks:**

- [ ] Review conflict log
- [ ] Resolve orphaned references
- [ ] Approve merge operations

### 7.2 Weekly Synchronization Tasks

**Comprehensive Validation:**

- [ ] Full cross-entity integrity check
- [ ] Migration map review
- [ ] Schema compliance audit
- [ ] Performance metrics update
- [ ] Documentation updates

### 7.3 On-Demand Synchronization

**Triggers:**

- LIBRARIES entity added/updated/deleted
- Employee status changed
- Task assignment changed
- Job posting created/updated
- Client relationship changed

**Process:**

1. Identify affected entities
2. Update cross-references
3. Validate integrity
4. Notify dependent systems
5. Log changes

---

## 8. Implementation Guidelines

### 8.1 Creating New Cross-Entity References

**Steps:**

1. Verify source entity exists (e.g., PRF-010 in LIBRARIES)
2. Create reference in target entity (e.g., EMP-001 references PRF-010)
3. Update cross-reference index (profession_to_employees.json)
4. Validate reference resolves correctly
5. Document relationship

### 8.2 Updating Existing References

**Steps:**

1. Identify all entities referencing changed entity
2. Update references in all dependent entities
3. Update cross-reference indexes
4. Validate all references resolve
5. Log changes

### 8.3 Deprecating Entities

**Steps:**

1. Mark entity as deprecated (add `"status": "deprecated"`)
2. Identify all references to deprecated entity
3. Create migration mapping (old_id → new_id or null)
4. Update all references (or mark as "needs review")
5. Archive deprecated entity
6. Update documentation

---

## 9. Monitoring and Reporting

### 9.1 Synchronization Health Metrics

**Metrics to Track:**

- Cross-reference integrity percentage
- Orphaned reference count
- Schema compliance percentage
- ID format compliance percentage
- Average time to resolve conflicts

### 9.2 Reporting

**Reports:**

- `SYNC/health_report.json` - Overall system health
- `SYNC/integrity_report.json` - Cross-reference integrity
- `SYNC/conflict_report.json` - Recent conflicts and resolutions
- `SYNC/orphaned_references_report.json` - Orphaned references needing attention

**Frequency:** Weekly automated reports + on-demand

---

## 10. Success Criteria

### 10.1 Data Integrity Targets

- ✅ 100% cross-reference integrity (all references resolve)
- ✅ 0 orphaned references
- ✅ 100% schema compliance
- ✅ 100% ID format compliance
- ✅ <24 hour conflict resolution time

### 10.2 Synchronization Performance

- ✅ Real-time cross-reference index updates
- ✅ Automated validation runs daily
- ✅ Conflict detection within 1 hour
- ✅ Migration mapping always current

---

## 11. File Structure

```
ENTITIES/
├── SYNC/                                    # Synchronization infrastructure
│   ├── Cross_Reference_Indexes/
│   │   ├── profession_to_employees.json
│   │   ├── tool_to_tasks.json
│   │   ├── employee_to_tasks.json
│   │   └── ...
│   ├── Migration_Maps/
│   │   └── entity_migration_map.json
│   ├── Validation_Reports/
│   │   ├── health_report.json
│   │   ├── integrity_report.json
│   │   └── ...
│   ├── Conflict_Logs/
│   │   ├── conflict_log.json
│   │   └── orphaned_references.json
│   └── Scripts/
│       ├── validate_cross_references.py
│       ├── validate_id_formats.py
│       └── ...
│
├── LIBRARIES/
│   └── Taxonomy/
│       └── LIBRARIES_Taxonomy_Migration_Map.json
│
└── [Other Entities...]
```

---

## 12. Related Documents

- `PROMPT_Build_LIBRARIES_Taxonomy.md` - LIBRARIES ID system
- `PROMPT_Data_Consistency_and_Knowledge_Integration.md` - Data consistency rules
- `Employee_Profile_Schema.md` - TALENTS schema
- `ARCHITECTURE_UPDATE_PLAN.md` - Architecture overview
- `FINAL_MIGRATION_SUMMARY_2025-11-17.md` - Migration history

---

**Created:** 2025-11-17

**Purpose:** Establish comprehensive data synchronization architecture for ENTITIES ecosystem

**Status:** Ready for Implementation

**Version:** 1.0

