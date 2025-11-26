# Architecture Merge Planning Prompt: Actions & Objects → Responsibilities

**Document Type:** Architecture Planning Prompt
**Purpose:** Plan merger of Actions and Objects sub-entities into Responsibilities as single endpoint to Task Managers
**Created:** 2025-11-15
**Status:** Planning Phase
**Complexity:** High (Architecture Refactoring)

---

## 🎯 Executive Summary

**Current State Problem:**
- Task Managers currently reference THREE separate LIBRARIES endpoints: Actions, Objects, AND Responsibilities
- This creates redundancy, maintenance overhead, and potential inconsistency
- Example from TASK-AI-031.json shows multiple reference points:
  - `"action": "Design"` (from Actions)
  - `"object": "Evaluation System"` (from Objects)
  - `"objects_used": ["OBJ-AI-027", "OBJ-AI-029"]` (from Objects)
  - `"responsibility": "AI Engineer"` (from Responsibilities - but should be responsibility ID)

**Proposed Solution:**
- Merge Actions and Objects INTO Responsibilities
- Responsibilities become the **SINGLE endpoint** connecting LIBRARIES → TASK_MANAGERS
- All Task Manager entities reference ONLY Responsibilities (via RESP-XXX IDs)

**Business Value:**
- **Simplified Architecture**: 1 endpoint instead of 3
- **Single Source of Truth**: Responsibilities own action+object combinations
- **Easier Maintenance**: Update responsibilities once, propagate everywhere
- **Clearer Semantics**: "What can be done?" → Check responsibilities, not scattered across 3 entities

---

## 📊 Current Architecture Analysis

### Current LIBRARIES Structure

```
LIBRARIES/
├── Actions/
│   ├── Actions_Master.json          # ~100+ actions (verbs)
│   ├── Data_Operations/             # 12 specialized actions
│   └── Video_Generation_Actions.json
│
├── Objects/
│   ├── object_types.json
│   ├── Agentic_Engineering_Objects.json  # OBJ-AI-027, etc.
│   ├── AI_Automation_Objects.json
│   ├── Design_Deliverables.json
│   ├── Documents.json
│   ├── Lead_Generation_Objects.json
│   ├── RAG_Objects.json
│   ├── Recruitment_Objects.json
│   ├── Social_Media_Deliverables.json
│   ├── Video_Deliverables.json
│   └── Video_Generation_Objects.json
│
└── Responsibilities/
    └── responsibilities.json         # 6 responsibilities (RESP-001 through RESP-006)
```

### Current Task Manager References (from TASK-AI-031.json)

```json
{
  "action": "Design",                              // ← References Actions
  "object": "Evaluation System",                    // ← References Objects
  "objects_used": ["OBJ-AI-027", "OBJ-AI-029"],    // ← References Objects with IDs
  "responsibility": "AI Engineer",                  // ← Should be RESP-ID, not profession
  "steps": [
    {
      "action": "define",                          // ← References Actions
      "responsibility": "AI Engineer"               // ← Should be RESP-ID
    }
  ]
}
```

**Problem Identified:**
- Multiple reference points (Actions, Objects, Responsibilities)
- Inconsistent usage ("responsibility" field uses profession name, not RESP-ID)
- No clear single endpoint

---

## 🏗️ Proposed Architecture

### Target LIBRARIES Structure

```
LIBRARIES/
├── Responsibilities/                 # ← SINGLE ENDPOINT
│   ├── responsibilities_master.json  # All responsibilities with embedded actions+objects
│   ├── By_Department/
│   │   ├── AI_Responsibilities.json
│   │   ├── Design_Responsibilities.json
│   │   ├── Dev_Responsibilities.json
│   │   ├── HR_Responsibilities.json
│   │   ├── LG_Responsibilities.json
│   │   ├── Sales_Responsibilities.json
│   │   └── Video_Responsibilities.json
│   │
│   └── Archive/                      # ← Legacy entities archived
│       ├── Legacy_Actions/
│       └── Legacy_Objects/
│
├── Professions/                      # Unchanged
├── Skills/                           # Unchanged
├── Tools/                            # Unchanged
└── Workflows/                        # Unchanged
```

### Target Task Manager References

```json
{
  "responsibility_id": "RESP-AI-031",              // ← SINGLE reference point
  "responsibility_name": "design evaluation systems",
  // Action and Object now embedded in responsibility

  "steps": [
    {
      "step_number": 1,
      "responsibility_id": "RESP-AI-031-SUBSTEP-001",  // ← Each step has responsibility
      "responsibility_name": "define evaluation metrics"
    }
  ]
}
```

---

## 📋 Merger Plan: Phase-by-Phase Breakdown

### **Phase 1: Data Analysis & Mapping (Week 1)**

#### **Task 1.1: Inventory Current Entities**
- **Action**: Count and categorize all Actions
  - Actions_Master.json: ~100+ actions
  - Data_Operations: 12 actions
  - Video_Generation_Actions: X actions
- **Action**: Count and categorize all Objects
  - 13 object files identified
  - Estimate: 200+ objects across all categories
- **Action**: Count existing Responsibilities
  - Current: 6 responsibilities (RESP-001 through RESP-006)

#### **Task 1.2: Create Action-Object Combination Matrix**
- **Objective**: Identify all valid action+object combinations currently used in Task Managers
- **Method**:
  1. Scan all Task Manager JSON files (Task Templates, Step Templates, Projects, Workflows)
  2. Extract all `"action"` + `"object"` pairs
  3. Create matrix showing which combinations are actively used
  4. Example output:
     ```
     | Action   | Object             | Used In Tasks | Frequency |
     |----------|--------------------|---------------|-----------|
     | Design   | Evaluation System  | TASK-AI-031   | 1         |
     | Create   | Job Posting        | TASK-HR-001   | 1         |
     | Generate | Leads              | TASK-LG-002   | 15        |
     ```

#### **Task 1.3: Map Actions+Objects → Departments**
- **Objective**: Determine which department each action+object combination belongs to
- **Method**:
  1. Review existing responsibilities (RESP-001 through RESP-006) for department patterns
  2. Analyze Task Manager files to see department usage
  3. Create department mapping rules
  4. Example:
     ```
     "design evaluation systems" → AI Department
     "screen candidates" → HR Department
     "generate leads" → Lead Generation Department
     ```

**Phase 1 Deliverables:**
- Action-Object Combination Matrix (CSV/JSON)
- Department Mapping Rules (JSON)
- Gap Analysis Report: Which combinations exist but have no responsibility?
- Duplication Report: Any overlapping combinations?

---

### **Phase 2: Responsibility Schema Design (Week 2)**

#### **Task 2.1: Design Enhanced Responsibility Schema**

**Current Responsibility Schema:**
```json
{
  "responsibility_id": "RESP-001",
  "responsibility_name": "screen candidates",
  "components": {
    "action": "screen",
    "object": "candidates",
    "object_type": "applied candidates, needed candidates, found candidates"
  },
  "department": "Managers (HR)",
  "description": "Review and evaluate candidate applications, resumes, and qualifications",
  "related_tasks": ["Screen candidate resumes", "Update candidate status in CRM"],
  "frequency": "daily"
}
```

**Proposed Enhanced Responsibility Schema:**
```json
{
  "responsibility_id": "RESP-AI-031",
  "responsibility_name": "design evaluation systems",
  "components": {
    "action": {
      "action_id": "ACT-001",
      "action_name": "design",
      "action_forms": {
        "base": "design",
        "continuous": "designing",
        "past": "designed"
      }
    },
    "object": {
      "object_id": "OBJ-AI-027",
      "object_name": "Evaluation System",
      "object_category": "Agentic_Engineering / Quality Assurance",
      "object_types": [
        "Code-based objective evaluation",
        "Code-based universal standard",
        "LLM-as-a-judge subjective evaluation",
        "LLM-as-a-judge with ground truth"
      ]
    }
  },
  "department": "AI",
  "profession": "AI Engineer",
  "description": "Design and implement evaluation systems for AI agents using code-based and LLM-as-a-judge methods",
  "business_value": "Enables systematic agent improvement; prevents bad behaviors; massive ROI through measurable quality improvements",
  "related_tasks": ["TASK-AI-031"],
  "related_skills": ["SKL-AI-EVAL-001"],
  "related_workflows": ["WF-AGENTIC-005"],
  "frequency": "weekly",
  "complexity": "High",
  "estimated_duration": "45-60 minutes",
  "tags": ["agentic-ai", "evaluation", "quality-assurance"],
  "source": "Video_013_Andrew_Ng_Agentic_AI_Course",
  "created_date": "2025-11-15",
  "last_updated": "2025-11-15"
}
```

**Key Enhancements:**
1. **Embedded Action Details**: Full action object with ID, forms, metadata
2. **Embedded Object Details**: Full object definition with ID, category, types
3. **Cross-References**: Links to skills, workflows, tasks
4. **Metadata**: Business value, complexity, duration, tags, source
5. **Department + Profession**: Clear ownership mapping

#### **Task 2.2: Create Responsibility Naming Convention**
- **Pattern**: `[verb] [plural noun]` (lowercase)
- **Examples**:
  - "design evaluation systems"
  - "implement reflection patterns"
  - "establish ground truth datasets"
  - "screen candidates"
  - "generate leads"
- **ID Convention**: `RESP-[DEPT]-[XXX]`
  - `RESP-AI-001` through `RESP-AI-999` (AI Department)
  - `RESP-HR-001` through `RESP-HR-999` (HR Department)
  - `RESP-LG-001` through `RESP-LG-999` (Lead Generation)
  - etc.

#### **Task 2.3: Design Sub-Responsibility Schema for Steps**
- **Problem**: Task steps also have action+object combinations
- **Solution**: Create sub-responsibility IDs for granular steps
- **Example**:
  ```json
  {
    "responsibility_id": "RESP-AI-031-SUB-001",
    "parent_responsibility": "RESP-AI-031",
    "responsibility_name": "define evaluation metrics",
    "components": {
      "action": {"action_name": "define", "action_id": "ACT-042"},
      "object": {"object_name": "evaluation metrics", "object_id": "OBJ-AI-028"}
    },
    "level": "step",
    "estimated_duration": "8-10 minutes"
  }
  ```

**Phase 2 Deliverables:**
- Enhanced Responsibility Schema (JSON Schema definition)
- Naming Convention Guide (Markdown)
- Sub-Responsibility Design (JSON Schema)
- Sample Responsibilities (10 examples following new schema)

---

### **Phase 3: Data Migration & Generation (Weeks 3-4)**

#### **Task 3.1: Generate Responsibilities from Action-Object Matrix**
- **Input**: Action-Object Combination Matrix from Phase 1
- **Process**:
  1. For each unique action+object combination:
     - Generate responsibility_id (RESP-[DEPT]-XXX)
     - Create responsibility_name ([action] [object])
     - Embed action details from Actions_Master.json
     - Embed object details from Objects/*.json files
     - Assign department based on mapping rules
     - Assign profession(s) that use this responsibility
     - Add metadata (frequency, complexity, duration)
  2. Cross-reference with existing Task Managers to populate:
     - related_tasks
     - estimated_duration (average from Task Templates)
     - complexity (from Task Templates)

#### **Task 3.2: Create Responsibility Files by Department**
- **Objective**: Organize responsibilities into department-specific files
- **Structure**:
  ```
  Responsibilities/
  ├── responsibilities_master.json        # All responsibilities
  ├── By_Department/
  │   ├── AI_Responsibilities.json        # RESP-AI-001 through RESP-AI-XXX
  │   ├── HR_Responsibilities.json        # RESP-HR-001 through RESP-HR-XXX
  │   ├── LG_Responsibilities.json        # RESP-LG-001 through RESP-LG-XXX
  │   ├── Dev_Responsibilities.json       # RESP-DEV-001 through RESP-DEV-XXX
  │   ├── Design_Responsibilities.json    # RESP-DES-001 through RESP-DES-XXX
  │   ├── Sales_Responsibilities.json     # RESP-SAL-001 through RESP-SAL-XXX
  │   └── Video_Responsibilities.json     # RESP-VID-001 through RESP-VID-XXX
  └── Archive/
      ├── Legacy_Actions/
      └── Legacy_Objects/
  ```

#### **Task 3.3: Generate Sub-Responsibilities for Step Templates**
- **Input**: All Step Template JSON/MD files
- **Process**:
  1. For each step in each Task Template:
     - Extract step's action + object (if not explicitly stated, infer from step name)
     - Generate sub-responsibility ID: RESP-[DEPT]-XXX-SUB-YYY
     - Create sub-responsibility entry
     - Link to parent responsibility
  2. Estimate: 141 PHASE4 steps + 340 existing steps = ~500 sub-responsibilities

**Phase 3 Deliverables:**
- responsibilities_master.json (all responsibilities)
- 7 department-specific responsibility files
- Sub-responsibilities index (JSON)
- Migration statistics report
- Data quality validation report

---

### **Phase 4: Task Manager Refactoring (Weeks 5-6)**

#### **Task 4.1: Update Task Template Schema**

**Current Task Template Schema:**
```json
{
  "action": "Design",
  "object": "Evaluation System",
  "objects_used": ["OBJ-AI-027", "OBJ-AI-029"],
  "responsibility": "AI Engineer"  // ← Wrong (profession, not responsibility)
}
```

**New Task Template Schema:**
```json
{
  "responsibility_id": "RESP-AI-031",
  "responsibility_name": "design evaluation systems",
  // action and object removed (now in responsibility)
  "responsibilities": {
    "responsible": "RESP-AI-031",      // ← Responsibility ID
    "accountable": "AI Engineering Lead",
    "consulted": ["ML Engineer", "Research Scientist"],
    "informed": ["Product Team", "QA Team"]
  }
}
```

#### **Task 4.2: Update Step Template Schema**

**Current Step Schema (from steps array in Task Template):**
```json
{
  "step_number": 1,
  "name": "Define evaluation objectives and metrics",
  "action": "define",
  "responsibility": "AI Engineer"
}
```

**New Step Schema:**
```json
{
  "step_number": 1,
  "responsibility_id": "RESP-AI-031-SUB-001",
  "responsibility_name": "define evaluation metrics"
  // action removed (now in sub-responsibility)
}
```

#### **Task 4.3: Batch Update All Task Manager Files**
- **Files to Update**:
  - Task Templates: ~77 Task Templates (22 PHASE4 + 55 legacy)
  - Step Templates: ~481 Step Templates (141 PHASE4 + 340 legacy)
  - Projects: Unknown count
  - Workflows: Unknown count
  - Communication Templates: Unknown count

- **Update Process**:
  1. Create backup of all Task Manager files
  2. For each file:
     - Extract current `action` + `object` fields
     - Look up corresponding `responsibility_id` from responsibilities_master.json
     - Replace `action` + `object` with `responsibility_id`
     - Update `responsibility` field (if RACI matrix) to use RESP-ID
     - Update `responsibilities.responsible` to use RESP-ID
     - Validate JSON structure
  3. Run automated tests to ensure no broken references

**Phase 4 Deliverables:**
- Updated Task Template schema documentation
- Updated Step Template schema documentation
- All Task Manager files refactored (backed up originals in Archive/)
- Validation test suite results
- Migration report with before/after statistics

---

### **Phase 5: Documentation & Cross-Referencing (Week 7)**

#### **Task 5.1: Update All README Files**
- **Files to Update**:
  - `LIBRARIES/Responsibilities/README.md` - Document new merged structure
  - `LIBRARIES/Responsibilities/Actions/README.md` - Actions documentation
  - `LIBRARIES/Responsibilities/Objects/README.md` - Objects documentation
  - `LIBRARIES/ACTIONS_README.md` - Navigation helper to Actions
  - `LIBRARIES/OBJECTS_README.md` - Navigation helper to Objects
  - `TASK_MANAGERS/README.md` - Update to reflect single endpoint architecture

#### **Task 5.2: Create Migration Guide**
- **Content**:
  - Architecture changes explanation
  - Before/after examples
  - How to use responsibilities as single endpoint
  - How to look up action/object from responsibility
  - Backwards compatibility notes (if any)

#### **Task 5.3: Update Cross-Reference Documents**
- **Files to Update**:
  - `LIBRARIES/Cross_Reference_Map.json` (if exists)
  - `TASK_MANAGERS/Task_Templates_Checklist-Item-003.md`
  - `TASK_MANAGERS/Step_Templates/PHASE4_STEPS_INDEX.md`
  - Any other index/listing files

#### **Task 5.4: Create Responsibility Browser Tool**
- **Purpose**: Make it easy to search and browse responsibilities
- **Features**:
  - Search by action keyword
  - Search by object keyword
  - Filter by department
  - Filter by profession
  - Filter by complexity
  - Show embedded action+object details
  - Show related tasks/skills/workflows

**Phase 5 Deliverables:**
- All README files updated
- Migration Guide (Markdown)
- Updated cross-reference documents
- Responsibility Browser Tool (optional, but recommended)
- Final architecture documentation

---

### **Phase 6: Validation & Testing (Week 8)**

#### **Task 6.1: Data Integrity Validation**
- **Tests**:
  - All Task Manager files have valid responsibility_id references
  - All responsibility_ids in Task Managers exist in responsibilities_master.json
  - No orphaned action/object references
  - All sub-responsibilities have valid parent responsibilities
  - All professions reference valid responsibilities

#### **Task 6.2: Cross-Reference Validation**
- **Tests**:
  - Responsibilities ↔ Professions bidirectional links valid
  - Responsibilities ↔ Skills bidirectional links valid
  - Responsibilities ↔ Workflows bidirectional links valid
  - Responsibilities ↔ Task Templates bidirectional links valid

#### **Task 6.3: Performance Testing**
- **Tests**:
  - Time to look up responsibility by ID
  - Time to search responsibilities by action keyword
  - Time to search responsibilities by object keyword
  - File size impact (combined responsibilities vs separate actions+objects)

#### **Task 6.4: User Acceptance Testing**
- **Tests**:
  - Can team members easily find responsibilities?
  - Is the new schema intuitive?
  - Are the department-specific files helpful?
  - Is the migration guide clear?

**Phase 6 Deliverables:**
- Validation test suite (automated)
- Validation test results report
- Performance benchmarks
- User acceptance feedback
- Bug/issue tracker with resolutions

---

## 🎯 Success Criteria

### Technical Success Criteria
1. ✅ All actions merged into responsibilities with embedded action details
2. ✅ All objects merged into responsibilities with embedded object details
3. ✅ All Task Manager files reference ONLY responsibility_id (no direct action/object refs)
4. ✅ All responsibility_ids are valid and exist in responsibilities_master.json
5. ✅ Zero broken cross-references after migration
6. ✅ All tests pass (data integrity, cross-reference, performance)

### Business Success Criteria
1. ✅ Single endpoint architecture achieved (LIBRARIES → Responsibilities → TASK_MANAGERS)
2. ✅ Maintenance overhead reduced (update 1 file, not 3)
3. ✅ Developer experience improved (clearer, simpler references)
4. ✅ Documentation complete and understandable
5. ✅ Team can operate with new architecture without confusion

### Quality Criteria
1. ✅ No data loss during migration (all actions/objects preserved in responsibilities)
2. ✅ Backwards compatibility documented (how to reference old action/object if needed)
3. ✅ Migration is reversible (backup strategy exists)
4. ✅ Performance is equivalent or better than before

---

## ⚠️ Risk Assessment & Mitigation

### Risk 1: Data Loss During Migration
- **Probability**: Medium
- **Impact**: Critical
- **Mitigation**:
  - Create full backups before any changes
  - Use version control (git) for all changes
  - Implement automated data validation after each phase
  - Manual spot-checks on random sample files

### Risk 2: Broken References After Refactoring
- **Probability**: High
- **Impact**: High
- **Mitigation**:
  - Create automated validation suite
  - Run validation after each file update
  - Implement rollback mechanism
  - Test on sample files first before batch update

### Risk 3: Performance Degradation
- **Probability**: Low
- **Impact**: Medium
- **Mitigation**:
  - Benchmark current performance before migration
  - Test performance after each phase
  - Optimize JSON structure if needed (indexed lookups)
  - Consider caching strategies if file sizes become too large

### Risk 4: Team Confusion/Resistance
- **Probability**: Medium
- **Impact**: Medium
- **Mitigation**:
  - Create clear migration guide with examples
  - Provide training/walkthrough sessions
  - Implement gradual rollout (one department at a time)
  - Maintain backwards compatibility documentation

### Risk 5: Schema Complexity Increases
- **Probability**: Medium
- **Impact**: Low
- **Mitigation**:
  - Keep schema as simple as possible
  - Use JSON Schema validation to enforce structure
  - Provide schema documentation with examples
  - Create helper tools/scripts for working with responsibilities

---

## 📈 Estimated Effort & Timeline

| Phase | Duration | Effort (Hours) | Dependencies |
|-------|----------|----------------|--------------|
| Phase 1: Data Analysis & Mapping | 1 week | 20-30 hours | None |
| Phase 2: Schema Design | 1 week | 15-20 hours | Phase 1 |
| Phase 3: Data Migration | 2 weeks | 40-60 hours | Phase 2 |
| Phase 4: Task Manager Refactoring | 2 weeks | 60-80 hours | Phase 3 |
| Phase 5: Documentation | 1 week | 15-20 hours | Phase 4 |
| Phase 6: Validation & Testing | 1 week | 20-30 hours | Phase 5 |
| **TOTAL** | **8 weeks** | **170-240 hours** | |

**Resource Allocation:**
- **Data Engineer/Architect**: Phase 1-3 (primary)
- **Software Engineer**: Phase 4 (primary), Phase 3 (support)
- **Technical Writer**: Phase 5 (primary)
- **QA Engineer**: Phase 6 (primary)

---

## 🔄 Rollback Plan

If critical issues arise during migration:

1. **Immediate Rollback**: Restore from backups (git revert)
2. **Partial Rollback**: Revert only affected department files
3. **Pause & Fix**: Stop migration, fix issues, resume from checkpoint
4. **Hybrid Mode**: Maintain both old (action+object) and new (responsibility_id) references temporarily

**Rollback Triggers:**
- >10% of files fail validation
- Performance degradation >50%
- Critical production system failures
- Team consensus to abort

---

## 📚 Reference Links

### Current Architecture
- Actions: `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Actions`
- Objects: `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Objects`
- Responsibilities: `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Responsibilities`
- Task Managers: `C:\Users\Dell\Dropbox\Entities\TASK_MANAGERS`

### Documentation
- Actions README: `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Actions\README.md`
- Objects README: `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Objects\README.md`
- Responsibilities README: `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Responsibilities\README.md`

### Sample Files
- Sample Task Template: `C:\Users\Dell\Dropbox\Entities\TASK_MANAGERS\Task_Templates\By_Department\AI_Tasks\TASK-AI-031.json`
- Sample Responsibility: `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Responsibilities\responsibilities.json` (RESP-001 through RESP-006)

---

## 🎯 Next Steps

### Immediate Actions (This Week)
1. **Review this planning document** with team/stakeholders
2. **Get approval** to proceed with Phase 1
3. **Create project tracking** structure (Jira/GitHub issues)
4. **Allocate resources** (assign team members to phases)
5. **Set up version control** for all affected files

### Phase 1 Kickoff (Next Week)
1. Begin Task 1.1: Inventory Current Entities
2. Set up automated scripts for scanning Task Manager files
3. Create Action-Object Combination Matrix template
4. Schedule daily standup for Phase 1 progress

---

**Document Version:** 1.0
**Last Updated:** 2025-11-15
**Author:** AI Assistant (Claude Sonnet 4.5)
**Reviewers:** [To be assigned]
**Approval Status:** Pending Review
