# JOBS Entity Population Prompt

## Objective
Extract and transform recruitment data from `C:\Users\Dell\Dropbox\Nov25\HR Nov25` to populate the JOBS entity structure at `C:\Users\Dell\Dropbox\Nov25\Entities\JOBS` following the specifications in [README.md](README.md).

---

## Data Sources

### Primary Sources
1. **cvs_extracted.tsv** - Candidate applications with position, department, profession, skills
2. **interviews_processed.tsv** - Interview records with positions, departments, and hiring outcomes
3. **CVs/** folder - Individual CV files with detailed skill and experience information
4. **DEPARTMENT_GUIDE.md** - HR capabilities, professions, tools, and responsibilities

### Reference Documents
- **JOBS/README.md** - Entity structure, metadata template, file naming conventions
- **HR Nov25/prompts/cv_prompt.md** - Profession and department mappings

### Company Terminology Libraries (LIBRARIES Entity)
**Location:** `C:\Users\Dell\Dropbox\SummariesOct\LIBRARIES`

Use these libraries to ensure consistency with company-wide terminology:

1. **Actions Library** (`Actions/actions_library.json`)
   - Standard action verbs used across the organization
   - Structure: Actions → Processes → Results
   - Maps actions to Departments and Professions
   - Examples: "access", "analyze", "archive", "check", "adjust"

2. **Objects Library** (`Objects/objects_library.json`)
   - Business objects that actions operate on
   - Structure: Objects → Object Types
   - Recruitment objects: candidates, communications, contracts, databases, interviews, negotiations, reports, salaries
   - Example object types:
     - Candidates: needed candidates, applied candidates, found candidates, follow-up candidates
     - Communications: first connection, update, follow-up, feedback, faq, onboarding
     - Interviews: video interview, project interview

3. **Tools Library** (`Tools/tools_library.json`)
   - Comprehensive list of tools, software, and platforms
   - Maps tools to tasks, professions, and departments
   - Examples: CRM, Notion, Google Docs, Google Calendar, Google Meet, Zoom, LinkedIn

4. **Professions Library** (`Professions/professions_library.json`)
   - Official profession definitions and department mappings
   - Use these exact profession names in all job postings
   - Structure: Professions → Departments

5. **Responsibilities Library** (`Responsibilities/responsibilities_library.json`)
   - Standard responsibility definitions by profession
   - Maps responsibilities to objects, professions, and departments
   - Examples: "Screening candidate resumes", "Conducting candidate interviews", "Managing communications"

**IMPORTANT:** When creating job requirements, templates, and postings:
- Use ACTIONS from the Actions Library for job descriptions
- Reference OBJECTS from the Objects Library for what employees will work with
- List TOOLS from the Tools Library for required software proficiency
- Use exact PROFESSION names from the Professions Library
- Reference RESPONSIBILITIES from the Responsibilities Library for role duties

---

## Task Breakdown

### STEP 1: Analyze Job Positions
**Action:** Identify all unique job positions being recruited for

**Process:**
1. Read `cvs_extracted.tsv` and extract all unique values from the "Profession" column
2. Read `interviews_processed.tsv` and extract all unique values from the "Position" column
3. Merge and deduplicate the positions list
4. Group positions by department (developers, designers, marketers, managers, videographers, linguistics)

**Output:** A comprehensive list of active job positions with their departments

**Example:**
```
Developers:
- Front End Developer
- Back End Developer
- Full Stack Developer
- Mobile Developer

Designers:
- UI/UX Designer
- Graphic Designer
- Web Designer
- 3D Designer

Managers:
- Lead Generator
- Personal Assistant
- Chat Operator
- HR Manager
```

---

### STEP 2: Extract Job Requirements
**Action:** Build skill matrices and experience requirements for each position

**Process:**
1. For each position identified in STEP 1:
   - Search `cvs_extracted.tsv` for candidates with that profession
   - Analyze portfolio links and CV data
   - Extract common skills, tools, and qualifications
2. Reference `DEPARTMENT_GUIDE.md` for standard tools and skills by profession
3. **Reference LIBRARIES for company terminology:**
   - Query `Tools/tools_library.json` for the profession to get standard tools
   - Query `Responsibilities/responsibilities_library.json` for the profession to get standard responsibilities
   - Query `Actions/actions_library.json` for the profession to get relevant actions
   - Query `Objects/objects_library.json` for the profession to get work objects
4. Categorize skills into:
   - **Technical Skills** (React, Python, Photoshop, etc.)
   - **Soft Skills** (Communication, Teamwork, Problem-solving)
   - **Tools** (Use exact names from Tools Library: CRM, Notion, Google Meet, etc.)
   - **Languages** (English level required)
   - **Experience Level** (Junior/Mid/Senior based on interview outcomes)
   - **Actions Performed** (From Actions Library: analyze, create, manage, etc.)
   - **Objects Managed** (From Objects Library: candidates, reports, contracts, etc.)
   - **Core Responsibilities** (From Responsibilities Library)

**Output Format:** JSON files in `Job_Requirements/Skills_Matrices/`

**Example (Frontend Developer):**
```json
{
  "entity_type": "JOBS",
  "sub_entity": "Job_Requirements",
  "position": "Frontend Developer",
  "department": "developers",
  "profession": "front end developer",
  "libraries_references": {
    "professions_library": "C:\\Users\\Dell\\Dropbox\\SummariesOct\\LIBRARIES\\Professions\\professions_library.json",
    "tools_library": "C:\\Users\\Dell\\Dropbox\\SummariesOct\\LIBRARIES\\Tools\\tools_library.json",
    "actions_library": "C:\\Users\\Dell\\Dropbox\\SummariesOct\\LIBRARIES\\Actions\\actions_library.json",
    "objects_library": "C:\\Users\\Dell\\Dropbox\\SummariesOct\\LIBRARIES\\Objects\\objects_library.json",
    "responsibilities_library": "C:\\Users\\Dell\\Dropbox\\SummariesOct\\LIBRARIES\\Responsibilities\\responsibilities_library.json"
  },
  "required_skills": {
    "technical": ["React", "TypeScript", "JavaScript", "HTML", "CSS", "Redux"],
    "soft_skills": ["Problem Solving", "Communication", "Team Collaboration"],
    "tools": ["VS Code", "Git", "GitHub", "Figma", "Chrome DevTools", "npm", "Webpack"],
    "languages": {
      "English": "B1"
    }
  },
  "actions_performed": [
    "develop",
    "build",
    "test",
    "debug",
    "optimize",
    "collaborate",
    "review"
  ],
  "objects_managed": [
    "web applications",
    "user interfaces",
    "components",
    "code repositories"
  ],
  "core_responsibilities": [
    "Building responsive user interfaces",
    "Implementing frontend features",
    "Code review and testing",
    "Performance optimization",
    "Team collaboration"
  ],
  "experience_levels": {
    "Junior": {
      "years": "0-2",
      "proficiency": "Basic React, HTML/CSS, Git basics"
    },
    "Mid": {
      "years": "2-5",
      "proficiency": "Advanced React, TypeScript, State Management, Testing"
    },
    "Senior": {
      "years": "5+",
      "proficiency": "Architecture, Performance optimization, Mentoring, CI/CD"
    }
  },
  "certifications": [],
  "education": "Bachelor's degree in Computer Science or equivalent experience",
  "created_date": "2025-11-11",
  "tags": ["frontend", "react", "typescript", "web-development", "developers"]
}
```

**Example (Recruiter - using LIBRARIES data):**
```json
{
  "entity_type": "JOBS",
  "sub_entity": "Job_Requirements",
  "position": "Recruiter",
  "department": "managers",
  "profession": "recruiter",
  "libraries_references": {
    "professions_library": "C:\\Users\\Dell\\Dropbox\\SummariesOct\\LIBRARIES\\Professions\\professions_library.json",
    "tools_library": "C:\\Users\\Dell\\Dropbox\\SummariesOct\\LIBRARIES\\Tools\\tools_library.json",
    "actions_library": "C:\\Users\\Dell\\Dropbox\\SummariesOct\\LIBRARIES\\Actions\\actions_library.json",
    "objects_library": "C:\\Users\\Dell\\Dropbox\\SummariesOct\\LIBRARIES\\Objects\\objects_library.json",
    "responsibilities_library": "C:\\Users\\Dell\\Dropbox\\SummariesOct\\LIBRARIES\\Responsibilities\\responsibilities_library.json"
  },
  "required_skills": {
    "technical": ["Boolean Search", "CRM Systems", "LinkedIn Recruiting", "ATS Usage", "Talent Sourcing"],
    "soft_skills": ["Communication", "Negotiation", "Relationship Building", "Assessment", "Organization"],
    "tools": ["CRM", "Notion", "Google Docs", "Google Calendar", "Google Meet", "Google Drive", "Zoom", "LinkedIn", "Job Sites"],
    "languages": {
      "English": "B1"
    }
  },
  "actions_performed": [
    "access",
    "analyze",
    "archive",
    "check",
    "adjust",
    "screen",
    "evaluate",
    "communicate",
    "negotiate"
  ],
  "objects_managed": [
    "candidates (needed candidates, applied candidates, found candidates, follow-up candidates)",
    "communications (first connection, update, follow-up, feedback, faq, onboarding)",
    "contracts (employees contracts, presale contract, content creator agreement)",
    "databases (candidates database, employees database, presale database)",
    "interviews (video interview, project interview)",
    "negotiations (salary negotiation, contract term negotiation, benefit negotiation)",
    "reports (daily report, monthly report, employee report, department report, task report)",
    "salaries (expected salary, proposed salary, start salary)"
  ],
  "core_responsibilities": [
    "Screening candidate resumes",
    "Conducting candidate interviews",
    "Assessing candidate qualifications",
    "Distributing job offers",
    "Managing communications",
    "Finalizing employment contracts",
    "Renewing worker contracts",
    "Updating candidate databases"
  ],
  "experience_levels": {
    "Junior": {
      "years": "0-2",
      "proficiency": "Basic recruiting, CV screening, interview coordination"
    },
    "Mid": {
      "years": "2-5",
      "proficiency": "Full-cycle recruiting, sourcing strategies, candidate assessment, CRM management"
    },
    "Senior": {
      "years": "5+",
      "proficiency": "Strategic talent acquisition, team leadership, recruitment analytics, process optimization"
    }
  },
  "certifications": [],
  "education": "Bachelor's degree in HR, Psychology, Business or equivalent experience",
  "created_date": "2025-11-11",
  "tags": ["recruitment", "hr", "talent-acquisition", "sourcing", "managers"]
}
```

**File Naming:** `JOBS_Job_Requirement_{Position}_{Date}.json`

---

### STEP 3: Create Job Posting Templates
**Action:** Generate reusable job templates for each position type

**Process:**
1. For each position, create a template based on:
   - Standard structure from README.md metadata template
   - Department and profession from cv_prompt.md mappings
   - Requirements from STEP 2 Skills Matrices
   - Standard fields (title, description, compensation range, location)
2. Use interview data to determine typical:
   - Availability (Full time/Part time)
   - Remote work options
   - Target countries (based on candidate locations)

**Output Format:** JSON files in `Job_Templates/{Department}_Templates/`

**Example:**
```json
{
  "entity_type": "JOBS",
  "sub_entity": "Job_Template",
  "template_id": "TPL-DEV-001",
  "template_name": "Frontend Developer Template",
  "category": "IT_Templates",
  "department": "Dev",
  "profession": "Frontend Developer",
  "standard_fields": {
    "title": "Frontend Developer",
    "description": "We are seeking a talented Frontend Developer to build responsive, high-performance web applications using modern JavaScript frameworks.",
    "requirements_reference": "Job_Requirements/Skills_Matrices/JOBS_Job_Requirement_Frontend_Developer_2025_11_11.json",
    "compensation": {
      "range": "$2000-3500/month",
      "currency": "USD",
      "type": "Remote contractor"
    },
    "location": "Remote",
    "remote_options": ["Fully Remote", "Hybrid"],
    "availability": "Full time",
    "application_deadline_days": 30,
    "tags": ["frontend", "react", "typescript", "remote"]
  },
  "customization_guidelines": {
    "title": "Adjust seniority level (Junior/Mid/Senior)",
    "compensation": "Adjust based on experience level and market rates",
    "requirements": "Customize skill requirements based on project needs",
    "location": "Specify if on-site required for specific regions"
  },
  "default_hiring_manager": "Klimenko_Yaroslav",
  "created_date": "2025-11-11",
  "last_updated": "2025-11-11",
  "version": "1.0"
}
```

**File Naming:** `JOBS_Job_Template_{Position}_v{Version}.json`

---

### STEP 4: Create Active Job Postings
**Action:** Generate active job postings from current recruitment needs

**Process:**
1. Analyze `cvs_extracted.tsv` to identify positions with recent applications (Last Contact Date in November 2025)
2. For positions with 3+ recent applications, create an active job posting
3. Use the corresponding template from STEP 3
4. Assign unique job IDs: `JOB-2025-{XXX}` (sequential numbering)
5. Set status to "Active"
6. Reference the appropriate skills matrix

**Output Format:** JSON files in `Job_Postings/Active/`

**Example:**
```json
{
  "entity_type": "JOBS",
  "sub_entity": "Job_Posting",
  "job_id": "JOB-2025-001",
  "title": "Frontend Developer (Mid Level)",
  "status": "Active",
  "department": "Dev",
  "profession": "Frontend Developer",
  "created_date": "2025-11-05",
  "posted_date": "2025-11-05",
  "application_deadline": "2025-12-05",
  "hiring_manager": "Klimenko_Yaroslav",
  "recruiter": "Rekonvald_Viktoriia",
  "description": "We are seeking a Mid-level Frontend Developer to join our development team. You will work on building modern web applications using React and TypeScript.",
  "requirements": {
    "skills": ["React", "TypeScript", "CSS", "HTML", "Git"],
    "experience_level": "Mid",
    "years_experience": "2-5",
    "tools": ["VS Code", "Git", "Figma"],
    "languages": {
      "English": "B1"
    },
    "education": "Bachelor's degree preferred or equivalent experience",
    "certifications": []
  },
  "compensation": {
    "range": "$2500-3500/month",
    "currency": "USD",
    "type": "Remote contractor"
  },
  "location": "Remote",
  "remote_work": true,
  "availability": "Full time",
  "target_countries": ["Ukraine", "Azerbaijan", "Poland"],
  "application_count": 5,
  "interview_count": 3,
  "tags": ["frontend", "react", "typescript", "remote", "mid-level"],
  "template_used": "TPL-DEV-001",
  "requirements_reference": "Job_Requirements/Skills_Matrices/JOBS_Job_Requirement_Frontend_Developer_2025_11_11.json"
}
```

**File Naming:** `JOBS_Job_Posting_{Position}_{Date}.json`

**Prioritize these positions** (based on application volume):
- UI/UX Designer
- Graphic Designer
- Frontend Developer
- Lead Generator
- Back End Developer

---

### STEP 5: Build Job Categories Hierarchy
**Action:** Create a structured categorization system

**Process:**
1. Organize positions into primary categories matching department folders
2. Create secondary categories for specializations
3. Add metadata tags for cross-referencing
4. Link to profession definitions

**Output Format:** JSON files in `Job_Categories/{PrimaryCategory}/`

**Example:**
```json
{
  "entity_type": "JOBS",
  "sub_entity": "Job_Categories",
  "primary_category": "IT",
  "secondary_categories": {
    "Frontend_Development": {
      "positions": ["Frontend Developer", "React Developer"],
      "skills_focus": ["JavaScript", "React", "TypeScript", "CSS"],
      "tools": ["VS Code", "Git", "Webpack", "npm"]
    },
    "Backend_Development": {
      "positions": ["Back End Developer", "API Developer"],
      "skills_focus": ["Python", "Node.js", "Databases", "APIs"],
      "tools": ["VS Code", "Git", "Docker", "PostgreSQL"]
    },
    "Full_Stack_Development": {
      "positions": ["Full Stack Developer"],
      "skills_focus": ["React", "Node.js", "Databases", "APIs", "DevOps"],
      "tools": ["VS Code", "Git", "Docker", "AWS"]
    }
  },
  "metadata": {
    "department": "developers",
    "total_positions": 8,
    "common_requirements": {
      "education": "Bachelor's degree or equivalent",
      "language": "English B1+",
      "work_arrangement": "Remote"
    }
  },
  "cross_references": {
    "libraries_professions": "../LIBRARIES/Professions/IT_Professions.json",
    "talents": "../TALENTS/Developer_Talents/",
    "businesses": "../BUSINESSES/Tech_Clients/"
  },
  "tags": ["technology", "software-development", "remote", "engineering"],
  "created_date": "2025-11-11"
}
```

---

### STEP 6: Validate and Organize Files
**Action:** Ensure all files follow naming conventions and proper structure

**Checklist:**
- [ ] All JSON files are valid and properly formatted
- [ ] File names follow pattern: `JOBS_{SubEntity}_{Description}_{Date}.json`
- [ ] Dates are in format: `YYYY_MM_DD` for filenames, `YYYY-MM-DD` in content
- [ ] All files include required metadata fields (entity_type, sub_entity, created_date)
- [ ] Job IDs are unique and sequential (JOB-2025-001, JOB-2025-002, etc.)
- [ ] All references to other files use correct relative paths
- [ ] Tags are consistent and lowercase with hyphens
- [ ] Department names match cv_prompt.md mappings

**Folder Structure to Create:**
```
JOBS/
├── README.md (existing)
├── POPULATE_JOBS_PROMPT.md (this file)
├── Job_Postings/
│   ├── Active/
│   │   ├── JOBS_Job_Posting_Frontend_Developer_2025_11_05.json
│   │   ├── JOBS_Job_Posting_UI_UX_Designer_2025_11_05.json
│   │   ├── JOBS_Job_Posting_Graphic_Designer_2025_11_05.json
│   │   ├── JOBS_Job_Posting_Lead_Generator_2025_11_05.json
│   │   └── JOBS_Job_Posting_Back_End_Developer_2025_11_05.json
│   ├── Archived/
│   └── Templates/ (symlink to ../Job_Templates/)
├── Job_Requirements/
│   ├── Skills_Matrices/
│   │   ├── JOBS_Job_Requirement_Frontend_Developer_2025_11_11.json
│   │   ├── JOBS_Job_Requirement_UI_UX_Designer_2025_11_11.json
│   │   ├── JOBS_Job_Requirement_Graphic_Designer_2025_11_11.json
│   │   └── ... (one per unique position)
│   └── Experience_Levels/
│       └── JOBS_Experience_Level_Definitions_2025_11_11.json
├── Job_Templates/
│   ├── IT_Templates/
│   │   ├── JOBS_Job_Template_Frontend_Developer_v1.json
│   │   ├── JOBS_Job_Template_Back_End_Developer_v1.json
│   │   └── JOBS_Job_Template_Full_Stack_Developer_v1.json
│   ├── Design_Templates/
│   │   ├── JOBS_Job_Template_UI_UX_Designer_v1.json
│   │   ├── JOBS_Job_Template_Graphic_Designer_v1.json
│   │   └── JOBS_Job_Template_Web_Designer_v1.json
│   ├── Marketing_Templates/
│   │   ├── JOBS_Job_Template_Content_Manager_v1.json
│   │   └── JOBS_Job_Template_SMM_Manager_v1.json
│   └── Operations_Templates/
│       ├── JOBS_Job_Template_Lead_Generator_v1.json
│       └── JOBS_Job_Template_Personal_Assistant_v1.json
└── Job_Categories/
    ├── IT/
    │   └── JOBS_Job_Category_IT_2025_11_11.json
    ├── Design/
    │   └── JOBS_Job_Category_Design_2025_11_11.json
    ├── Marketing/
    │   └── JOBS_Job_Category_Marketing_2025_11_11.json
    └── Operations/
        └── JOBS_Job_Category_Operations_2025_11_11.json
```

---

## Execution Instructions

### For AI Assistant:
When executing this prompt, follow these steps in order:

1. **READ** all source files from `C:\Users\Dell\Dropbox\Nov25\HR Nov25`:
   - cvs_extracted.tsv
   - interviews_processed.tsv
   - DEPARTMENT_GUIDE.md
   - prompts/cv_prompt.md

2. **LOAD** company terminology from LIBRARIES:
   - Read `C:\Users\Dell\Dropbox\SummariesOct\LIBRARIES\Professions\professions_library.json`
   - Read `C:\Users\Dell\Dropbox\SummariesOct\LIBRARIES\Tools\tools_library.json`
   - Read `C:\Users\Dell\Dropbox\SummariesOct\LIBRARIES\Actions\actions_library.json`
   - Read `C:\Users\Dell\Dropbox\SummariesOct\LIBRARIES\Objects\objects_library.json`
   - Read `C:\Users\Dell\Dropbox\SummariesOct\LIBRARIES\Responsibilities\responsibilities_library.json`

3. **CREATE** lookup tables for each profession:
   - For each profession in HR data, create a mapping of:
     - Tools used (from Tools Library)
     - Actions performed (from Actions Library)
     - Objects managed (from Objects Library)
     - Responsibilities assigned (from Responsibilities Library)
   - Example: For "recruiter" → extract all entries where `"Professions": "recruiter"`

4. **CREATE** the folder structure listed in STEP 6

5. **EXECUTE** Steps 1-5 in sequence, generating all JSON files:
   - Use LIBRARIES data to populate `actions_performed`, `objects_managed`, `core_responsibilities`, and `tools` fields
   - Ensure all profession names match exactly with Professions Library
   - Reference LIBRARIES file paths in `libraries_references` field

6. **VALIDATE** all files against the checklist in STEP 6

7. **REPORT** summary:
   - Total positions identified
   - Total job postings created (Active)
   - Total templates created
   - Total skills matrices created
   - Confirmation that LIBRARIES terminology was used
   - Any errors or missing data

### Expected Output Summary:
```
JOBS Entity Population Complete:

Positions Identified: 25+ unique positions across 5 departments
Active Job Postings: 15-20 positions with recent applications
Job Templates: 25+ templates (one per position type)
Skills Matrices: 25+ requirement files
Job Categories: 4 primary categories (IT, Design, Marketing, Operations)

Files Created: 80-100 JSON files
Folder Structure: Complete with all sub-entity folders
Data Quality: All files validated and properly formatted
```

---

## Quality Criteria

### Data Completeness
- ✅ Every active position from HR data has a corresponding job posting
- ✅ Every position has a skills matrix
- ✅ Every position has a reusable template
- ✅ All departments are represented in categories
- ✅ All job files include `libraries_references` field linking to LIBRARIES

### Data Accuracy
- ✅ Department-profession mappings match cv_prompt.md specifications
- ✅ Skills and tools match DEPARTMENT_GUIDE.md standards
- ✅ Compensation ranges are realistic for remote work
- ✅ Language requirements match candidate data (English B1)
- ✅ **LIBRARIES terminology is used throughout:**
  - Profession names exactly match Professions Library
  - Tools list matches Tools Library for the profession
  - Actions performed come from Actions Library
  - Objects managed come from Objects Library
  - Core responsibilities match Responsibilities Library

### Data Consistency
- ✅ JSON structure matches README.md metadata template
- ✅ File naming follows exact convention
- ✅ All dates use consistent formats
- ✅ Tags are standardized (lowercase, hyphenated)
- ✅ References between files are valid and relative
- ✅ **Company terminology is consistent:**
  - Action verbs follow Actions Library format (Actions → Processes → Results)
  - Object types use exact names from Objects Library
  - Tool names use exact capitalization from Tools Library

### Business Value
- ✅ Templates enable rapid job posting creation
- ✅ Skills matrices enable AI-powered candidate matching
- ✅ Active postings reflect current hiring needs
- ✅ Structure supports scalability and automation

---

## Maintenance Instructions

### To Add New Positions:
1. Create skills matrix in `Job_Requirements/Skills_Matrices/`
2. Create template in appropriate `Job_Templates/{Category}/`
3. If position is active, create posting in `Job_Postings/Active/`
4. Update category file in `Job_Categories/`

### To Update Requirements:
1. Locate skills matrix file
2. Update required skills, tools, or experience levels
3. Increment version number
4. Update references in dependent job postings

### To Archive Filled Positions:
1. Move job posting from `Job_Postings/Active/` to `Job_Postings/Archived/`
2. Update status field to "Filled" or "Cancelled"
3. Add `filled_date` and `hired_candidate` fields

---

---

## LIBRARIES Integration Guide

### How to Query LIBRARIES for a Profession

**Example: Extracting data for "recruiter" profession**

1. **Get Tools:**
   ```javascript
   // Query Tools Library
   const recruiterTools = toolsLibrary.filter(entry =>
     entry.Professions === "recruiter" &&
     entry.Departments === "managers"
   ).map(entry => entry.Tools);

   // Result: ["CRM", "Notion", "Google Docs", "Google Calendar", "Google Meet", "Google Drive", "Zoom", "Google Slides"]
   ```

2. **Get Actions:**
   ```javascript
   // Query Actions Library
   const recruiterActions = actionsLibrary.filter(entry =>
     entry.Professions === "recruiter" &&
     entry.Departments === "managers"
   ).map(entry => entry.Actions);

   // Result: ["access", "archive", "analyze", "audit", "back up", "check", "adjust", ...]
   ```

3. **Get Objects:**
   ```javascript
   // Query Objects Library
   const recruiterObjects = objectsLibrary.filter(entry =>
     entry.Professions === "recruiter" &&
     entry.Departments === "managers"
   );

   // Result:
   // - candidates (needed, applied, found, follow-up)
   // - communications (first connection, update, follow-up, feedback, faq, onboarding)
   // - contracts (employees contracts, presale contract, content creator agreement)
   // - databases (candidates, employees, presale)
   // - interviews (video, project)
   // - negotiations (salary, contract term, benefit)
   // - reports (daily, monthly, employee, department, task)
   // - salaries (expected, proposed, start)
   ```

4. **Get Responsibilities:**
   ```javascript
   // Query Responsibilities Library
   const recruiterResponsibilities = responsibilitiesLibrary.filter(entry =>
     entry.Professions === "recruiter" &&
     entry.Departments === "managers"
   ).map(entry => entry.Responsibilities);

   // Result:
   // - "Screening candidate resumes"
   // - "Conducting candidate interviews"
   // - "Assessing candidate qualifications"
   // - "Distributing job offers"
   // - "Managing communications"
   // - "Finalizing employment contracts"
   // - "Renewing worker contracts"
   // - "Updating candidate databases"
   ```

### LIBRARIES Field Mapping Table

| JOBS Field | LIBRARIES Source | Query Filter |
|------------|------------------|--------------|
| `profession` | Professions Library | Exact match from `Professions` field |
| `department` | Professions Library | Value from `Departments` field |
| `tools` | Tools Library | Filter by `Professions` + `Departments` → extract `Tools` |
| `actions_performed` | Actions Library | Filter by `Professions` + `Departments` → extract `Actions` |
| `objects_managed` | Objects Library | Filter by `Professions` + `Departments` → extract `Objects` + `Object Types` |
| `core_responsibilities` | Responsibilities Library | Filter by `Professions` + `Departments` → extract `Responsibilities` |

### Standard JSON Structure with LIBRARIES

Every job-related JSON file should include:

```json
{
  "entity_type": "JOBS",
  "sub_entity": "[Job_Posting|Job_Requirements|Job_Template|Job_Categories]",
  "profession": "[exact match from Professions Library]",
  "department": "[exact match from Professions Library]",
  "libraries_references": {
    "professions_library": "C:\\Users\\Dell\\Dropbox\\SummariesOct\\LIBRARIES\\Professions\\professions_library.json",
    "tools_library": "C:\\Users\\Dell\\Dropbox\\SummariesOct\\LIBRARIES\\Tools\\tools_library.json",
    "actions_library": "C:\\Users\\Dell\\Dropbox\\SummariesOct\\LIBRARIES\\Actions\\actions_library.json",
    "objects_library": "C:\\Users\\Dell\\Dropbox\\SummariesOct\\LIBRARIES\\Objects\\objects_library.json",
    "responsibilities_library": "C:\\Users\\Dell\\Dropbox\\SummariesOct\\LIBRARIES\\Responsibilities\\responsibilities_library.json"
  },
  "tools": "[array from Tools Library]",
  "actions_performed": "[array from Actions Library]",
  "objects_managed": "[array from Objects Library with Object Types]",
  "core_responsibilities": "[array from Responsibilities Library]"
}
```

### Benefits of LIBRARIES Integration

1. **Consistency:** All job postings use the same terminology across the organization
2. **Traceability:** Clear references to source libraries for auditing and updates
3. **Automation:** Enables AI-powered matching between jobs and talents
4. **Scalability:** Adding new professions to LIBRARIES automatically propagates to job postings
5. **Knowledge Management:** Single source of truth for company terminology
6. **Cross-Entity Relations:** Jobs link to Talents, Task Managers, and other entities through shared LIBRARIES

---

**Created:** November 11, 2025
**Last Updated:** November 11, 2025
**Purpose:** Populate JOBS entity from HR recruitment data using company LIBRARIES terminology
**Source Data:** C:\Users\Dell\Dropbox\Nov25\HR Nov25
**LIBRARIES Data:** C:\Users\Dell\Dropbox\SummariesOct\LIBRARIES
**Target Location:** C:\Users\Dell\Dropbox\Nov25\Entities\JOBS
