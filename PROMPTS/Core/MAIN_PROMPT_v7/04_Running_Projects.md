# 4. RUNNING PROJECTS

**Version:** 7.0 | **Date:** 2025-11-26 | **Status:** Production
**Part of:** MAIN_PROMPT_v7 System

---

## ACTIVE PROJECTS (PRT-001 to PRT-009)

**ALWAYS check these before creating new projects:**

### PRT-001: [Project Name TBD]
**Status:** Check Project_Templates_Master_List.csv
**Milestones:** MLT-###
**Current Progress:** TBD

### PRT-002: [Project Name TBD]
**Status:** Check Project_Templates_Master_List.csv
**Milestones:** MLT-###
**Current Progress:** TBD

### PRT-003: Complete HR Automation Implementation
**Status:** Active
**Milestones:**
- MLT-006: HR System Integration (in progress)
- MLT-###: Additional milestones

**Current Tasks (Example):**
- TST-042: Create n8n automation ✅
- TST-055: Set up n8n weekly reports 🔄

**Tools:** TOL-007 (n8n), TOL-150 (Google Sheets), TOL-012 (Dropbox)

### PRT-004 to PRT-009: [Check Master CSV]
**Location:** `ENTITIES/TASK_MANAGERS/TSM-001_Project_Templates/Project_Templates_Master_List.csv`

---

## PROJECT TYPES DISTINCTION

### Internal PRT-### Projects (Remote Helpers Initiatives)

**Characteristics:**
- **Full control**: Remote Helpers defines scope, milestones, timelines
- **Strategic initiatives**: Company-wide improvements, automations, internal tools
- **Multi-week duration**: Planned milestones and deliverables
- **Progress tracking**: % completion, milestone completion, blockers

**Examples:**
- PRT-003: Complete HR Automation Implementation
- PRT-007: Lead Generation Pipeline Optimization
- PRT-### : Company Website Redesign

**How to track:**
- Create PRT-### with clear milestones (MLT-###)
- Track progress with completion percentages
- Link tasks (TST-###) and steps (STT-###)
- Monitor blockers and dependencies

---

### Client Projects (External Client Work)

**Characteristics:**
- **Limited employee control**: Client defines scope, deadlines, requirements
- **Service delivery**: Employee executes client-defined work
- **Variable duration**: Client-managed timeline
- **Task-based tracking**: Focus on deliverables, not milestone management

**Examples:**
- Website design for Acme Corp (Designer assigned, client manages project)
- Social media campaign for XYZ Company (SMM specialist executes, client directs)
- Development work for external platform (Developer implements client specs)

**How to track:**
- **Do NOT create PRT-###** for client projects
- Extract TST-### (individual tasks) from daily reports
- Note client name in task description
- Link employee (Employee ID) and tools (TOL-###)
- Track deliverables and completion status

**Client Project Task Example:**
```
TST-###: Design homepage mockup for Acme Corp
- Employee: 228 (Kucherenko Iuliia)
- Client: Acme Corp
- Tools: TOL-### (Figma), TOL-### (Adobe Illustrator)
- Status: 🔄 In Progress
- Deliverable: High-fidelity homepage mockup
- NOT linked to internal PRT-### (client manages overall project)
```

**When processing daily reports:**
- Identify if work is for client or internal initiative
- Client work → Extract TST-###, note client name
- Internal work → Map to existing PRT-001 to PRT-009 or propose new PRT-###

---

## CREATING NEW PROJECTS

**When to create PRT-010+:**

1. Work doesn't fit existing PRT-001 to PRT-009
2. Multi-week initiative with multiple milestones
3. Requires dedicated tracking and resources
4. Cross-department or department-specific strategic work

**Process:**
1. Check existing: Review PRT-001 to PRT-009
2. Identify gap: What's not covered?
3. Define scope: Multi-week? Multiple milestones?
4. Create structure:
   ```
   PRT-010: [Project Name]
     ├─ MLT-###: [Milestone 1]
     ├─ MLT-###: [Milestone 2]
     └─ MLT-###: [Milestone 3]
   ```
5. Add to master CSV
6. Link initial tasks (TST-###)

---

## PROJECT TRACKING

**Progress Indicators:**
- ✅ **Completed** - Task finished
- 🔄 **In Progress** - Actively working
- 🆕 **New** - Just identified, not started
- ⏸️ **Blocked** - Waiting on dependency
- 🔁 **Recurring** - Repeats regularly

**Track at Project Level:**
- **% Complete:** How many MLT completed / total MLT
- **Blockers:** What's preventing progress
- **Next Milestone:** What's up next
- **Active Tasks:** Current TST-### in progress

---

## EXAMPLE: Project Progress View

**PRT-003: Complete HR Automation Implementation**

**Progress:** 2 of 5 milestones complete (40%)

```
PRT-003: Complete HR Automation Implementation
  ├─ MLT-005: CV Parser Setup ✅
  ├─ MLT-006: HR System Integration 🔄
  │   ├─ TST-042: Create n8n automation ✅
  │   ├─ TST-055: Weekly reports automation 🔄
  │   └─ TST-056: Employee onboarding flow 🆕
  ├─ MLT-007: CRM Integration 🆕
  ├─ MLT-008: Interview Automation ⏸️ (blocked: waiting on API access)
  └─ MLT-009: Analytics Dashboard 🆕
```

**Next Actions:**
1. Complete TST-055 (weekly reports)
2. Start TST-056 (onboarding flow)
3. Unblock MLT-008 (request API access)

**Tools in Use:** TOL-007 (n8n), TOL-150 (Google Sheets), TOL-012 (Dropbox)

---

## DAILY TASK MAPPING

**When extracting from daily reports:**

1. **Extract task:** "Created employee onboarding automation"
2. **Classify:** TST-056: Employee onboarding flow setup
3. **Check projects:** Fits PRT-003 (HR Automation)
4. **Assign milestone:** MLT-006 (HR System Integration)
5. **Update progress:** Mark TST-056 as 🔄 In Progress
6. **Link resources:** TOL-### (tools used)

**Use [GDS-011](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-011) for classification decisions.**
