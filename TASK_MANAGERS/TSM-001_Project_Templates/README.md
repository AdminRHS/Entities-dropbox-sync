# Project Templates Entity Documentation

**Entity Type:** TASK_MANAGERS  
**Sub-Entity:** Project_Templates  
**Domain:** Task Management System  
**Purpose:** Reusable project blueprints that define phases, milestones, and task sequences  
**Created:** November 25, 2025  
**Last Updated:** November 25, 2025

---

## 📋 Overview

Project Templates are high-level blueprints that define complete project structures with phases, milestones, dependencies, and task sequences. They serve as reusable frameworks for similar projects across the organization, ensuring consistency and efficiency in project execution.

**Key Characteristics:**
- **Reusable:** One template can be used to create multiple project instances
- **Hierarchical:** Contain Milestone Templates → Task Templates → Step Templates
- **Structured:** Define phases, dependencies, and execution order
- **Context-Aware:** Include ownership, departments, and business context

---

## 🔍 Definition

**Project Template:** A collection of related Task Templates organized by phases and dependencies, providing a complete project blueprint from initiation to completion.

According to the framework:
- Project Templates represent **complete project workflows**
- They organize **Milestone Templates** into logical phases
- Each phase contains **Task Templates** with dependencies
- Task Templates contain **Step Templates** with specific actions
- Templates can be **instantiated** to create actual Projects with timelines

**Example:** A "Full Cycle Recruitment" Project Template might include:
- Phase 1: Job Creation (1 week)
- Phase 2: Sourcing (1-2 weeks)
- Phase 3: Screening (1 week)
- Phase 4: Interviews (1-2 weeks)
- Phase 5: Offer (1 week)
- Phase 6: Onboarding (1 week)

---

## 📐 Structure

### Project Template Hierarchy

```
Project Template
├── Phase 1: [Phase Name]
│   ├── Milestone Template 1
│   │   ├── Task Template 1
│   │   │   ├── Step Template 1
│   │   │   ├── Step Template 2
│   │   │   └── Step Template 3
│   │   └── Task Template 2
│   └── Milestone Template 2
├── Phase 2: [Phase Name]
│   └── ...
└── Phase N: [Phase Name]
```

### Project Template JSON Structure

```json
{
  "entity_type": "TASK_MANAGERS",
  "sub_entity": "Project_Template",
  "template_id": "Proj_Temp-{DEPT}-{NUMBER}",
  "project_template_name": "Full Cycle Recruitment",
  "metadata": {
    "status": "Active | Draft | Deprecated",
    "project_type": "Client | Internal | Standard",
    "version": "1.0",
    "last_updated": "YYYY-MM-DD"
  },
  "ownership": {
    "department": "HR",
    "primary_owner": "HR Manager",
    "team_members": ["Recruiter", "HR Coordinator"],
    "stakeholders": ["Department Lead", "Finance"],
    "client": "Internal | External Client Name"
  },
  "taxonomy": {
    "action": "Recruit",
    "object": "Qualified Candidate",
    "object_type": "Full-Time Employee",
    "tool": "CRM + Job Boards",
    "context": "Department-Hiring-Need"
  },
  "structure": {
    "estimated_duration": "4-6 weeks",
    "success_metric": "Qualified candidate hired",
    "phases": [
      {
        "phase_number": 1,
        "phase_name": "Job Creation",
        "duration": "1 week",
        "milestones": ["MIL-PROJ-HR-001-001"],
        "dependencies": [],
        "output": "Approved job posting ready to publish"
      },
      {
        "phase_number": 2,
        "phase_name": "Sourcing",
        "duration": "1-2 weeks",
        "milestones": ["MIL-PROJ-HR-001-002"],
        "dependencies": ["Phase 1 complete"],
        "output": "10+ qualified applications received"
      }
    ]
  },
  "project_metrics": {
    "time_to_complete": "4-6 weeks",
    "expected_applications": "50+",
    "screening_calls": "15",
    "interviews": "6",
    "offers_extended": "1-2",
    "acceptance_rate": "80%",
    "cost_per_hire": "$500"
  },
  "deliverables": [
    {
      "deliverable_name": "Job Posting",
      "format": "Published Job Advertisement",
      "quality_criteria": ["Approved by department lead", "Posted on 3+ platforms"]
    }
  ],
  "source_tracking": {
    "source_file": "RestructuredData/Projects_Deliverables_Nov05_2025.md",
    "extraction_date": "2025-11-10",
    "evidence_lines": "Lines 18-60"
  }
}
```

---

## 📂 File Organization

### Naming Convention

**File Format:** `Proj_Temp-{DEPT}-{NUMBER}.json` or `Proj_Temp-{DEPT}-{NUMBER}.md`

**Examples:**
- `Proj_Temp-HR-001.json` - First HR Project Template
- `Proj_Temp-SALES-001.json` - First Sales Project Template
- `Proj_Temp-DESIGN-002.json` - Second Design Project Template

### Directory Structure

```
Project_Templates/
├── README.md                           # This file
├── Proj_Temp-HR-001.json          # Full Cycle Recruitment
├── Proj_Temp-SALES-001.json       # Client Onboarding Project
├── Proj_Temp-DESIGN-001.json      # Brand Identity Development
├── Proj_Temp-AI-001.json          # Department Setup Video Production
└── [Department]/                       # Optional: Organize by department
    ├── Proj_Temp-HR-001.json
    └── Project-Template-003.json
```

---

## 🔗 Relationships

### Project Templates ↔ Projects

- **One-to-Many:** One Project Template can create multiple Project instances
- **Instantiation:** Projects are created from templates with specific timelines
- **Tracking:** Projects track actual dates, Project Templates define structure

```
Project Template (Blueprint)
    ↓ (instantiate)
Project Instance 1 (Jan 2025)
Project Instance 2 (Mar 2025)
Project Instance 3 (Jun 2025)
```

### Project Templates ↔ Milestone Templates

- **Contains:** Project Templates reference Milestone Templates
- **Ordering:** Phases define milestone execution order
- **Dependencies:** Phases specify milestone dependencies

### Project Templates ↔ Task Templates

- **Indirect:** Project Templates → Milestone Templates → Task Templates
- **Reusability:** Task Templates can be used across multiple Project Templates

### Project Templates ↔ Departments

- **Ownership:** Each Project Template belongs to a primary department
- **Collaboration:** Templates can involve multiple departments
- **Context:** Templates are department-specific or cross-functional

### Project Templates ↔ Tools

- **Tool Requirements:** Templates specify tools needed for each phase
- **Tool Assignment:** Tools are assigned at Task Template level
- **Tool Integration:** Templates document tool workflows

---

## 💡 Examples

### Example 1: Full Cycle Recruitment Project Template

**Source:** CRM_ENTITIES_LLM_TAXONOMY_GUIDE.md (SummariesOct)

```yaml
Project_Template_Name: "Full_Cycle_Recruitment"
Project_Owner: "HR Department"
Estimated_Duration: "4-6 weeks"
Success_Metric: "Qualified candidate hired"

Phase_1_Job_Creation:
  Duration: "1 week"
  Tasks:
    - Task_1: "Create: Job Description"
    - Task_2: "Define: Required Skills"
    - Task_3: "Set: Salary Range"
    - Task_4: "Approve: Job Posting (with department lead)"
  Dependencies: None
  Output: "Approved job posting ready to publish"

Phase_2_Sourcing:
  Duration: "1-2 weeks"
  Tasks:
    - Task_5: "Post: Job Advertisement (LinkedIn, DOU, Djinni)"
    - Task_6: "Search: Active Candidates (portfolio sites)"
    - Task_7: "Scrape: Contact Information (if needed)"
    - Task_8: "Send: Outreach Messages (to passive candidates)"
  Dependencies: ["Phase_1 complete"]
  Output: "10+ qualified applications received"

Phase_3_Screening:
  Duration: "1 week"
  Tasks:
    - Task_9: "Screen: Resumes (filter by requirements)"
    - Task_10: "Review: Portfolios (assess quality)"
    - Task_11: "Conduct: Screening Calls (15 min each)"
    - Task_12: "Select: Top 3-5 Candidates (for interviews)"
  Dependencies: ["Phase_2 complete"]
  Output: "3-5 candidates ready for interviews"

Phase_4_Interviews:
  Duration: "1-2 weeks"
  Tasks:
    - Task_13: "Schedule: Video Interviews"
    - Task_14: "Conduct: Behavioral Interviews (HR)"
    - Task_15: "Conduct: Technical Interviews (dept lead)"
    - Task_16: "Assign: Test Project (if applicable)"
    - Task_17: "Review: Test Submissions"
  Dependencies: ["Phase_3 complete"]
  Output: "1-2 finalists selected"

Phase_5_Offer:
  Duration: "1 week"
  Tasks:
    - Task_18: "Discuss: Salary Expectations"
    - Task_19: "Prepare: Offer Letter"
    - Task_20: "Send: Job Offer (via email)"
    - Task_21: "Negotiate: Terms (if needed)"
    - Task_22: "Receive: Signed Contract"
  Dependencies: ["Phase_4 complete"]
  Output: "Accepted offer, start date confirmed"

Phase_6_Onboarding:
  Duration: "1 week"
  Tasks:
    - Task_23: "Create: Employee Account (systems)"
    - Task_24: "Grant: Tool Access (software licenses)"
    - Task_25: "Send: Welcome Email (with checklist)"
    - Task_26: "Schedule: First Day Orientation"
    - Task_27: "Assign: Mentor (team member)"
    - Task_28: "Set: 30-60-90 Day Goals"
  Dependencies: ["Phase_5 complete"]
  Output: "New hire successfully onboarded"

Project_Metrics:
  - "Time to hire: 4-6 weeks"
  - "Applications received: 50+"
  - "Screening calls conducted: 15"
  - "Interviews conducted: 6"
  - "Offers extended: 1-2"
  - "Acceptance rate: 80%"
  - "Cost per hire: $500"
```

### Example 2: Department Setup Video Production Package

**Source:** Extracted_Project_Templates.md

```yaml
template_id: PROJ-AI-008
project_template_name: "Department Setup Video Production Package"
metadata:
  status: "Active"
  project_type: "Client"
ownership:
  department: "AI"
  primary_owner: "AI Engineer"
  team_members: ["Video Editor", "Content Writer", "Designer"]
  client: "LG Department (Internal)"
taxonomy:
  action: "Produce"
  object: "Training Video Package"
  object_type: "Comprehensive Setup Video (45-60 minutes)"
  tool: "NotebookLM + Video Production Tools"
  context: "Department-Onboarding-Video-Training"
structure:
  milestones:
    - name: "Milestone 1: Script Development"
      tasks:
        - "Design scene structure using Video Planning Tools (60+ scenes across 8 parts)"
        - "Write character-driven content using Storytelling Framework"
        - "Create narration notes using AI Generation Guidelines"
        - "Document screen recording instructions using Technical Documentation"
    - name: "Milestone 2: Production Asset Creation"
      tasks:
        - "Create character designs using Design Tools"
        - "Design visual indicators using Animation Tools"
        - "Prepare text overlays using Typography System"
        - "Document sound cues using Audio Production Guide"
    - name: "Milestone 3: Video Production"
      tasks:
        - "Generate video via NotebookLM using AI Video Generation"
        - "Edit scenes using Video Editing Software (45-60 minute final duration)"
        - "Add character animations using Animation Tools"
        - "Integrate audio using Audio Editing Software"
deliverables:
  - deliverable_name: "LG Setup Video Guide Complete Script"
    format: "Markdown (2,490+ lines)"
    quality_criteria: ["60+ scenes documented", "Character development arc complete", "Production-ready for AI generation"]
  - deliverable_name: "Final Training Video"
    format: "Video file (MP4/WebM)"
    quality_criteria: ["45-60 minutes duration", "Professional narration", "Clear visual instructions", "Character-driven engagement"]
```

### Example 3: Multi-Platform Design System Development

**Source:** Extracted_Project_Templates.md

```yaml
template_id: PROJ-DESIGN-002
project_template_name: "Multi-Platform Design System Development"
metadata:
  status: "Active"
  project_type: "Internal"
ownership:
  department: "DESIGN"
  primary_owner: "Senior Designer"
  team_members: ["Design Team", "Dev Team"]
  client: "Company-wide (Internal Standards)"
taxonomy:
  action: "Design"
  object: "Design System"
  object_type: "Comprehensive Design Guidelines (1,054 lines)"
  tool: "Figma + Design Principles"
  context: "Multi-Platform-Brand-Consistency"
structure:
  milestones:
    - name: "Milestone 1: Brand Identity & Visual Style"
      tasks:
        - "Define brand identity using Brand Strategy (personality, values, voice)"
        - "Create visual style specifications using Design System (logo, colors, typography, spacing)"
```

---

## 🎯 Usage in Framework

### Creating a Project from Template

1. **Select Template:** Choose appropriate Project Template
2. **Instantiate Project:** Create new Project instance with:
   - Start date
   - End date (estimated)
   - Assigned team members
   - Client/Entity context
3. **Generate Milestones:** Create Milestones from Milestone Templates
4. **Generate Tasks:** Create Tasks from Task Templates
5. **Assign Steps:** Create Steps from Step Templates
6. **Track Progress:** Monitor completion through phases

### Template Lifecycle

```
Draft Template
    ↓ (review & refine)
Active Template
    ↓ (use for projects)
Project Instances
    ↓ (gather feedback)
Updated Template (version 2.0)
    ↓ (deprecate old version)
Deprecated Template
```

### Template Versioning

- **Version Control:** Track template versions
- **Backward Compatibility:** Maintain old versions for existing projects
- **Migration:** Provide migration paths for template updates

---

## 📊 Project Template Categories

### By Project Type

1. **Client Projects**
   - External client deliverables
   - Example: "Brand Identity Development for Client X"

2. **Internal Projects**
   - Internal process improvements
   - Example: "Department Setup Video Production"

3. **Standard Projects**
   - Recurring project types
   - Example: "Full Cycle Recruitment"

### By Department

- **HR Projects:** Recruitment, onboarding, training
- **Sales Projects:** Client onboarding, re-engagement campaigns
- **Design Projects:** Brand development, design systems, creative campaigns
- **Development Projects:** Feature development, system integration
- **AI Projects:** Automation, content generation, tool development
- **Video Projects:** Production packages, training videos
- **Lead Generation Projects:** Outreach campaigns, lead enrichment

### By Complexity

1. **Simple Projects:** Single-phase, few tasks
2. **Moderate Projects:** 2-3 phases, multiple milestones
3. **Complex Projects:** 4+ phases, many dependencies, cross-functional

---

## 🔄 Integration with Other Entities

### Project Templates → Milestone Templates

Project Templates define which Milestone Templates are used and in what order:

```json
{
  "phases": [
    {
      "phase_number": 1,
      "milestones": ["MIL-PROJ-HR-001-001", "MIL-PROJ-HR-001-002"]
    }
  ]
}
```

### Project Templates → Task Templates

Through Milestone Templates, Project Templates reference Task Templates:

```
Project Template
  → Phase 1
    → Milestone 1
      → Task Template 1
      → Task Template 2
```

### Project Templates → Step Templates

Through Task Templates, Project Templates ultimately reference Step Templates:

```
Project Template
  → Phase 1
    → Milestone 1
      → Task Template 1
        → Step Template 1
        → Step Template 2
```

### Project Templates → Tools

Tools are specified at multiple levels:
- **Project Level:** Overall tool requirements
- **Phase Level:** Tools needed for phase completion
- **Task Level:** Specific tools for task execution (via Task Templates)

---

## 📚 Related Documentation

### Internal References

- **Task Templates:** `../Task_Templates/README.md`
- **Milestone Templates:** `../Milestone_Templates/README.md`
- **Step Templates:** `../Step_Templates/README.md`
- **Projects:** `../Projects/README.md`
- **Workflows:** `../Workflows/README.md`

### External References

- **CRM Taxonomy Guide:** `SummariesOct/Taxonomy/Guides/CRM_ENTITIES_LLM_TAXONOMY_GUIDE.md`
- **Task Manager Database Structure:** `SummariesOct/INFRASTRUCTURE/ENTITIES/TASK_MANAGERS/TASK_MANAGER_DATABASE_STRUCTURE.md`
- **Data-Driven Project Workflows:** `SummariesOct/Oct_25/INFRASTRUCTURE/LIBRARY/DS/DS.004_Design_Workflows/Data_Driven_Project_Workflows.md`
- **Storytelling Framework:** `SummariesOct/Oct_25/INFRASTRUCTURE/LIBRARY/PS/PS.002_Storytelling_Frameworks/InnerClient_Storytelling_Framework.md`

### Extraction Sources

- **Extracted Project Templates:** `../Extracted_Project_Templates.md`
- **Project Templates Checklist-Item-003:** `../Project_Templates_Checklist-Item-003.md`
- **TASK_MANAGERS Index:** `../INDEX.md`

---

## 🎯 Best Practices

### Template Design

1. **Start with Outcomes:** Define success metrics and deliverables first
2. **Define Phases:** Break project into logical phases with clear outputs
3. **Specify Dependencies:** Document phase and milestone dependencies
4. **Estimate Duration:** Provide realistic time estimates per phase
5. **Include Quality Criteria:** Define what "done" means for each phase

### Template Maintenance

1. **Version Control:** Track template versions and changes
2. **Regular Updates:** Update templates based on project learnings
3. **Documentation:** Keep templates well-documented with examples
4. **Review Process:** Establish review process for template changes
5. **Deprecation:** Deprecate outdated templates rather than deleting

### Template Usage

1. **Template Selection:** Choose templates based on project type and context
2. **Customization:** Allow customization while maintaining core structure
3. **Tracking:** Track which templates are used most frequently
4. **Feedback Loop:** Collect feedback from project teams
5. **Continuous Improvement:** Use feedback to improve templates

---

## 🔍 Template Discovery

### Finding Project Templates

1. **By Department:** Check department-specific templates
2. **By Project Type:** Search by client/internal/standard type
3. **By Action/Object:** Use taxonomy fields to find relevant templates
4. **By Complexity:** Filter by simple/moderate/complex

### Template Matching

When creating a new project:
1. **Search Existing Templates:** Check if similar template exists
2. **Adapt Template:** Modify existing template for new context
3. **Create New Template:** Only if no suitable template exists
4. **Document Decision:** Record why template was chosen or created

---

## 📈 Metrics and Tracking

### Template Metrics

- **Usage Frequency:** How often template is used
- **Success Rate:** Percentage of successful projects using template
- **Average Duration:** Actual vs. estimated duration
- **Team Satisfaction:** Feedback scores from project teams

### Project Metrics (from Template)

- **Time to Complete:** Actual project duration
- **Phase Completion:** Time per phase
- **Deliverable Quality:** Quality metrics for deliverables
- **Resource Utilization:** Team member allocation and efficiency

---

## 🚀 Future Enhancements

### Planned Features

1. **Template Library:** Searchable database of all templates
2. **Template Analytics:** Usage and performance analytics
3. **Template Recommendations:** AI-powered template suggestions
4. **Template Marketplace:** Share templates across organizations
5. **Template Versioning:** Advanced version control and migration

### Integration Opportunities

1. **AI Integration:** AI-assisted template creation and customization
2. **Automation:** Automated project creation from templates
3. **Learning System:** Templates as learning resources
4. **Portfolio Integration:** Link templates to portfolio projects
5. **Client Portal:** Client-facing template selection interface

---

## 📝 Notes

- Project Templates are **blueprints**, not actual projects
- Templates define **structure**, projects track **execution**
- One template can create **multiple project instances**
- Templates should be **versioned** and **maintained**
- Templates should include **realistic estimates** and **dependencies**

---

## 🔗 Related Entities

- **Projects** (`../Projects/`) - Actual project instances created from templates
- **Milestone Templates** (`../Milestone_Templates/`) - Milestone blueprints
- **Task Templates** (`../Task_Templates/`) - Task blueprints
- **Step Templates** (`../Step_Templates/`) - Step blueprints
- **Workflows** (`../Workflows/`) - Automated workflow definitions
- **Libraries** (`../../LIBRARIES/`) - Actions, Objects, Tools, Skills used in templates

---

**Last Updated:** November 25, 2025  
**Document Version:** 1.0

