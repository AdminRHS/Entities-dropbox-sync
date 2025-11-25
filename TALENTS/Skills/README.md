# Skills Sub-Entity Documentation

**Entity Type:** LIBRARIES > Skills
**Domain:** Knowledge Base - Skills Catalog
**Purpose:** Complete skills catalog combining responsibilities (action + object) with tools
**Created:** 2025-01-16
**Last Updated:** 2025-11-25
**ISO Code:** SKL (consonant-only, follows LIBRARIES naming conventions)

---

## 📋 Overview

The Skills sub-entity contains the complete catalog of standardized skills that combine responsibilities (action + object phrases) with tools. Skills serve as reusable definitions in the LIBRARIES ecosystem and are referenced by TALENTS for employee skill profiles, job requirements, and talent matching.

**Skills in LIBRARIES Ecosystem:**
- Skills are **standardized definitions** in LIBRARIES (reusable catalog)
- Skills combine **Responsibilities** (from Actions + Objects) with **Tools**
- Skills use **SKL-XXX** ID format following LIBRARIES conventions
- Skills are **referenced by TALENTS** for employee profiles and job requirements
- Skills enable **cross-entity integration** (TALENTS, JOBS, TASK_MANAGERS)

---

## 🔍 Skills Definition

**Skills** are phrase-matched combinations of responsibilities (action + object) with tools, showing practical application of capabilities.

**Skill Formula:**
```
Skill = Responsibility + Tool
Where Responsibility = Action + Object (phrase-matched)

Examples:
- "screened candidates via CRM" (action: screen, object: candidates, tool: CRM)
- "developed features in React" (action: develop, object: features, tool: React)
- "edited videos in Adobe Premiere" (action: edit, object: videos, tool: Adobe Premiere)
```

---

## 📁 Directory Structure

```
../TALENTS/Skills/
├── Master/
│   ├── all_skills.json              # Complete skills catalog (28 skills)
│   ├── skills_index.json            # Searchable index with keywords
│   └── skills_metadata.json         # Version control & statistics
├── By_Department/
│   ├── HR_skills.json               # 5 HR skills
│   ├── LG_skills.json               # 5 Lead Generation skills
│   ├── Design_skills.json           # 5 Design skills
│   ├── DEV_skills.json              # 5 Developer skills
│   ├── Sales_skills.json            # 5 Sales skills
│   └── Video_skills.json            # 3 Video skills
├── By_Profession/
│   ├── recruiter.json               # Skills for recruiters
│   ├── hr_manager.json              # Skills for HR managers
│   ├── lead_generator.json          # Skills for lead generators
│   ├── ui_ux_designer.json          # Skills for UI/UX designers
│   ├── frontend_developer.json      # Skills for frontend devs
│   ├── backend_developer.json       # Skills for backend devs
│   ├── full_stack_developer.json    # Skills for full stack devs
│   ├── graphic_designer.json        # Skills for graphic designers
│   ├── sales_manager.json           # Skills for sales managers
│   ├── video_editor.json            # Skills for video editors
│   ├── motion_designer.json         # Skills for motion designers
│   ├── animator.json                # Skills for animators
│   └── smm.json                     # Skills for social media managers
├── By_Difficulty/
│   ├── beginner.json                # 12 beginner skills
│   ├── intermediate.json            # 11 intermediate skills
│   └── advanced.json                # 5 advanced skills
├── By_Tool/
│   └── [20 tool-specific files]     # Skills grouped by tool used
├── Mappings/
│   ├── skill_profession_map.json    # Skills to professions mapping
│   └── skill_tool_map.json          # Skills to tools mapping
├── Templates/
│   ├── talent_skill_profile.json    # Template for talent skill profiles
│   ├── skill_assessment.json        # Template for skill assessments
│   └── skill_development_plan.json  # Template for development plans
├── Archive/
│   └── [deprecated skills]          # Archived/deprecated skills
└── README.md                        # This file
```

---

## 📐 Skill Structure

Each skill in the catalog includes:

```json
{
  "skill_id": "SKL-XXX",
  "skill_phrase": "action + object + via/using/in + tool",
  "components": {
    "result": "past participle form",
    "action": "verb",
    "object": "entity being acted upon",
    "object_type": "variations/modifiers",
    "tool": "software/instrument used",
    "tool_category": "category classification"
  },
  "department": "Department Name",
  "professions": ["profession1", "profession2"],
  "difficulty_level": "beginner | intermediate | advanced | expert",
  "frequency": "daily | weekly | monthly",
  "time_estimate_minutes": 0,
  "automation_potential": "low | medium | high | very high",
  "related_skills": ["SKL-XXX"],
  "example_tasks": ["Task description"],
  "training_resources": []
}
```

---

## 🎯 Usage in TALENTS Ecosystem

### 1. **Employee Skill Profiles**
- Employees link to skills from the catalog
- Track proficiency levels (beginner to expert)
- Validate skills through assessments and task completion
- Monitor skill development over time

### 2. **Candidate Skill Matching**
- Match candidates to job requirements based on skills
- Identify skills gaps before hiring
- Validate claimed skills during interviews
- Support resume parsing with standardized skill names

### 3. **Presales Talent Showcasing**
- Highlight employee skills in client presentations
- Generate skill matrices for proposals
- Link skills to video CVs and portfolios
- Support competitive differentiation

### 4. **Training & Development**
- Identify skills gaps for training needs
- Create skill development plans
- Track training progress and completion
- Measure ROI on skill training

### 5. **Performance Management**
- Track skill usage in completed tasks
- Measure skill proficiency improvements
- Link skills to performance reviews
- Support career progression planning

---

## 💡 Example Skills

### HR Skills
- **SKL-001:** screened candidates via CRM
- **SKL-002:** conducted video interviews via Zoom
- **SKL-003:** sent job offers via Gmail
- **SKL-004:** updated candidate status in CRM
- **SKL-005:** analyzed recruitment data in Google Sheets

### Development Skills
- **SKL-030:** developed features in React
- **SKL-031:** created APIs using Node.js
- **SKL-032:** managed code via GitHub
- **SKL-033:** debugged applications using DevTools
- **SKL-034:** deployed applications to production servers

### Design Skills
- **SKL-020:** created UI mockups in Figma
- **SKL-021:** designed social media posts in Canva
- **SKL-022:** exported design files from Figma
- **SKL-023:** generated AI images using Midjourney
- **SKL-024:** shared design previews via Discord

---

## 🔗 Integration with TALENTS Entities

### Employees
Employees have detailed skill profiles that include:
- Skills possessed (from catalog)
- Proficiency levels (self-assessed and manager-assessed)
- Validation status (verified skills)
- Performance metrics (quality scores, task completion)
- Development plans (skills in progress)

**File:** See `Templates/talent_skill_profile.json`

### Candidates
Candidates list claimed skills that are:
- Matched to skills catalog (SKL-XXX IDs)
- Assessed during interviews
- Verified through evidence (portfolios, certifications)
- Compared against job requirements

### Job Requirements
Jobs specify required skills:
- List of required skill IDs from catalog
- Desired proficiency levels
- Optional vs mandatory skills
- Skills gap analysis for matching

---

## 📊 Skills Statistics

**Total Skills:** 28
**Departments Covered:** 6 (HR, Lead Generation, Design, Developers, Sales, Video)
**Professions Covered:** 13
**Tools Referenced:** 20

**By Difficulty:**
- Beginner: 12 skills (43%)
- Intermediate: 11 skills (39%)
- Advanced: 5 skills (18%)
- Expert: 0 skills (0%)

**By Department:**
- HR: 5 skills
- Lead Generation: 5 skills
- Design: 5 skills
- Developers: 5 skills
- Sales: 5 skills
- Video: 3 skills

---

## 🔍 Searching Skills

### 1. By Skill ID
```javascript
// Find specific skill
skill_id: "SKL-030"
```

### 2. By Profession
```javascript
// Find all frontend developer skills
profession: "frontend developer"
// Use: By_Profession/frontend_developer.json
```

### 3. By Department
```javascript
// Find all HR skills
department: "Managers (HR)"
// Use: By_Department/HR_skills.json
```

### 4. By Tool
```javascript
// Find all skills using Figma
tool: "Figma"
// Use: skill_tool_map.json or search skills_index.json
```

### 5. By Keyword
```javascript
// Use skills_index.json for keyword search
keywords: ["video", "edit", "premiere"]
// Returns: SKL-050, SKL-051
```

---

## 📈 Talent Skill Profile Example

```json
{
  "employee_id": "EMP-2025-001",
  "name": "Artemchuk Nikolay",
  "department": "AI",
  "profession": "AI Engineer",
  "skills_profile": {
    "skills": [
      {
        "skill_id": "SKL-030",
        "skill_phrase": "developed features in React",
        "proficiency": {
          "level": "advanced",
          "self_assessed": "advanced",
          "manager_assessed": "expert",
          "last_assessment_date": "2025-01-10"
        },
        "experience": {
          "years": 2.5,
          "frequency": "daily",
          "total_tasks_completed": 45
        },
        "validation": {
          "verified": true,
          "verified_by": "EMP-2025-005",
          "evidence": ["completed_task_TM-2024-089"]
        },
        "performance": {
          "avg_quality_score": 4.5,
          "success_rate": 0.95
        }
      }
    ],
    "summary": {
      "total_skills": 28,
      "by_difficulty": {
        "beginner": 5,
        "intermediate": 12,
        "advanced": 9,
        "expert": 2
      }
    }
  }
}
```

---

## 🎯 Common Use Cases

### 1. Find Employees with Specific Skill
```
Query: employees.skills_profile.skills.skill_id = "SKL-030"
Filter: proficiency.level >= "intermediate"
Result: List of qualified employees
```

### 2. Skills Gap Analysis for Candidate
```
Job Required: ["SKL-030", "SKL-031", "SKL-032"]
Candidate Has: ["SKL-030", "SKL-032"]
Gap: ["SKL-031"]
Match: 67%
```

### 3. Generate Presales Skill Matrix
```
Employee: EMP-2025-001
Filter: verified skills only, proficiency >= advanced
Output: Client-ready skill matrix with proficiency levels
```

### 4. Create Development Plan
```
Current Skills: ["SKL-030"]
Target Role: Full Stack Developer
Required Skills: ["SKL-030", "SKL-031", "SKL-034"]
Skills to Develop: ["SKL-031", "SKL-034"]
```

---

## 🔗 Integration with LIBRARIES Ecosystem

**Skills are part of LIBRARIES:**
- Skills reference **Actions** and **Objects** (from Responsibilities)
- Skills reference **Tools** (from Tools library)
- Skills map to **Professions** (from Professions library)
- Skills are organized by **Departments** (from Departments registry)

**Skills are used by other entities:**
- **TALENTS/Employees** - Reference skills from this catalog
- **TALENTS/Candidates** - Match claimed skills to catalog
- **JOBS** - Specify required skills from catalog
- **TASK_MANAGERS** - Link tasks to skills that produce them

**ID System:**
- Format: `SKL-XXX` (e.g., SKL-001, SKL-030, SKL-050)
- Sequential numbering within entity type
- Zero-padded to 3 digits
- Follows LIBRARIES ISO Code Registry conventions

---

## 📚 Related Entities

**Within LIBRARIES:**
- **LIBRARIES/Responsibilities** - Actions + Objects that form skill responsibilities
- **LIBRARIES/Tools** - Tools referenced in skills
- **LIBRARIES/Professions** - Professions that use these skills
- **LIBRARIES/Departments** - Department mappings for skills

**Cross-Entity References:**
- **TALENTS/Employees** - Employees reference skills from this catalog
- **TALENTS/Candidates** - Candidates match claimed skills to catalog
- **JOBS** - Job requirements specify skills from catalog
- **TASK_MANAGERS/Task_Templates** - Tasks link to skills that produce them

---

## 🎯 Business Value

- **Faster Hiring:** Match candidates to jobs by skills in seconds
- **Better Presales:** Showcase talent skills in client presentations
- **Targeted Training:** Identify and close skills gaps systematically
- **Performance Tracking:** Measure skill development over time
- **Career Development:** Clear skill progression paths for employees
- **Standardization:** Consistent skill naming across organization

---

## 📝 Maintenance

### Adding New Skills
1. Add skill to `Master/all_skills.json`
2. Assign unique SKL-XXX ID
3. Include complete skill structure
4. Run organization scripts to update views
5. Update `skills_metadata.json`

### Updating Skills
1. Edit skill in `Master/all_skills.json`
2. Increment version in metadata
3. Update last_updated date
4. Regenerate view files if needed
5. Document changes

### Deprecating Skills
1. Move skill to `Archive/deprecated_skills.json`
2. Add deprecation date and reason
3. Update metadata
4. Notify stakeholders
5. Update affected talent profiles

---

**Last Updated:** 2025-11-25
**Version:** 1.1
**Maintained By:** LIBRARIES Taxonomy Team
**ISO Code:** SKL (registered in Libraries_ISO_Code_Registry.md)

---

**For Questions or Issues:**
- Check skills_metadata.json for statistics
- Use skills_index.json for keyword search
- Refer to Templates/ for integration examples
- Contact HR team for skill validation processes
