# TALENTS Entity Documentation

**Entity Type:** TALENTS  
**Domain:** Human Capital  
**Purpose:** Manages talent from application through employment lifecycle  
**Created:** November 1, 2025  
**Last Updated:** November 1, 2025

---

## 📋 Overview

The TALENTS entity domain manages the complete talent lifecycle, from initial job application through employment. It supports video-first talent presentation (competitive differentiator), enables rapid client-talent matching, facilitates skills gap analysis for training, and tracks performance-based development paths.

---

## 🗂️ Sub-Entities

### 1. Skills
**Purpose:** Complete skills catalog for talent management and matching

**Key Attributes:**
- 28 skills across 6 departments (HR, LG, Design, Dev, Sales, Video)
- Skills organized by profession (13 professions)
- Skills categorized by difficulty (beginner/intermediate/advanced)
- Skill components (action, object, tool, result)
- Skill mappings (profession, tool, workflow)
- Skill assessment and development templates

**File Structure:**
```
Skills/
├── Master/                    # Complete catalog & index
├── By_Department/             # Skills by department (6 files)
├── By_Profession/             # Skills by profession (13 files)
├── By_Difficulty/             # Skills by difficulty level
├── By_Tool/                   # Skills by tool used
├── Mappings/                  # Profession & tool mappings
├── Templates/                 # Skill profile templates
└── README.md                  # Skills documentation
```

**Migration Info:**
- Migrated from: `LIBRARIES/LBS_004_Skills`
- Migration date: 2025-11-22
- Reason: Skills are talent-centric and belong in TALENTS ecosystem (integrated during LBS restructuring)

---

### 3. Job_Applications
**Purpose:** Submitted applications and candidate data

**Key Attributes:**
- Applicant personal information
- Contact details
- Application date
- Position applied for
- Initial screening status
- Application source

**File Structure:**
```
Job_Applications/
├── New_Applications/        # Recently submitted
├── Under_Review/           # Being evaluated
└── Archived/               # Processed applications
```

---

### 2. Candidates_JSON_Clusters
**Purpose:** Qualified applicants in the hiring pipeline

**Key Attributes:**
- Skills matrix and proficiency levels
- Experience history
- Technical assessment results
- Interview feedback
- Offer status (Extended/Pending/Accepted/Declined)
- Availability date

**File Structure:**
```
Candidates/
├── Technical_Assessment/    # Test results and evaluations
├── Interview_Stage/         # Interview notes and feedback
└── Offers_Extended/        # Offer letters and negotiations
```

---

### 4. Employees
**Purpose:** Hired team members with full HR profiles (32 current)

**Key Attributes:**
- Employee ID and personal information
- Department assignment (HR, AI, Video, Sales, Design, Dev, LG)
- Profession and role level (Junior/Mid/Senior/Expert)
- Skills matrix and proficiency levels
- Tool proficiency
- Video CV link
- Portfolio links
- Employment history
- Performance metrics
- Availability and project assignments
- Compensation and benefits
- Performance reviews

**Current Team Structure:**
- **HR:** 2 employees (Rekonvald Viktoriia, Nealova Evgeniya)
- **AI:** 3 employees (Zasiadko Matvii, Artemchuk Nikolay, Perederii Vladislav)
- **Video:** 3 employees (Panchenko Diana, Podolskyi Sviatoslav, Azanova Darya)
- **Sales:** 1 employee (Kovalska Anastasiya)
- **Design:** 9 employees (Shelep Olha, Bogun Polina, and 7 others)
- **Dev:** 3 employees (Klimenko Yaroslav, Kizilova Olha, Danylenko Liliia)
- **LG:** 11 employees (Hanan Zaheur, Rybak Nataliia, and 9 others)

**File Structure:**
```
Employees/
├── HR_Department/          # HR team members
├── AI_Department/          # AI team members
├── Video_Department/       # Video team members
├── Sales_Department/        # Sales team members
├── Design_Department/       # Design team members
├── Dev_Department/         # Development team members
└── LG_Department/          # Lead Generation team members
```

---

### 5. Presales
**Purpose:** Available talent for client presentations

**Key Attributes:**
- Video CVs (competitive differentiator)
- Portfolio links
- Client-ready profiles
- Availability status
- Skill highlights
- Past project examples
- Client testimonials

**File Structure:**
```
Presales/
├── Video_CVs/             # Video CV files and links
├── Portfolios/             # Portfolio collections
└── Client_Ready_Profiles/  # Formatted client presentation profiles
```

---

## 🔗 Relationships

### Primary Relationships

1. **TALENTS ↔ JOBS**
   - Talents apply to jobs
   - Jobs require specific talent skills
   - Matching algorithm uses skills matrix

2. **TALENTS ↔ BUSINESSES**
   - Talents assigned to client projects
   - Client feedback affects talent performance metrics
   - Video-first presentation differentiates service

3. **TALENTS ↔ TASK_MANAGERS**
   - Employees assigned to tasks
   - Tasks require specific profession capabilities
   - Performance tracked through task completion

4. **TALENTS ↔ LIBRARIES**
   - Professions define required skills
   - Employees have tool proficiency levels
   - Responsibilities mapped to roles

---

## 📊 Example Queries

### Find Talents Matching Job Requirements
```sql
-- Find all Frontend Developers available for a React project
SELECT t.name, t.skills, t.video_cv_link
FROM Talents t
JOIN Professions p ON t.profession_id = p.id
JOIN Skills s ON p.id = s.profession_id
WHERE p.name = 'Frontend Developer'
  AND s.name = 'React'
  AND t.availability = 'Available'
  AND t.skill_level >= 'Intermediate'
  AND t.status = 'Employee'
```

### Get Employee Performance Metrics
```sql
-- Get performance data for an employee
SELECT 
  t.name,
  COUNT(tm.id) as tasks_completed,
  AVG(tm.completion_time) as avg_completion_time,
  SUM(tm.quality_score) / COUNT(tm.id) as avg_quality_score
FROM Talents t
JOIN Task_Managers tm ON t.id = tm.assigned_to
WHERE t.id = [EMPLOYEE_ID]
  AND tm.status = 'Completed'
GROUP BY t.id
```

---

## 📝 File Naming Convention

**Pattern:** `TALENTS_[Type]_[EmployeeName]_[Item]_[Date].ext`

**Examples:**
- `TALENTS_Employee_Artemchuk_Nikolay_Performance_Review_2025_Q1.md`
- `TALENTS_Candidate_John_Doe_Technical_Assessment_2025_01_15.json`
- `TALENTS_Presales_Shelep_Olha_Video_CV_2025_01_20.mp4`

---

## 🔄 Workflow Integration

### Talent Hiring Workflow

1. **Receive** + **Job Application** + **for [Position]**
   - Process application
   - Initial screening
   - Move to Candidates if qualified

2. **Assess** + **Candidate** + **with Technical Test**
   - Administer skills assessment
   - Evaluate results
   - Determine fit

3. **Interview** + **Candidate** + **with Hiring Manager**
   - Conduct interviews
   - Gather feedback
   - Make hiring decision

4. **Hire** + **Candidate** + **as Employee**
   - Extend offer
   - Onboard new employee
   - Set up employee profile

5. **Track** + **Employee Performance** + **with Metrics**
   - Monitor task completion
   - Track quality scores
   - Conduct performance reviews

---

## 📋 Metadata Template

Every talent file should include:

```json
{
  "entity_type": "TALENTS",
  "sub_entity": "Employee",
  "employee_id": "EMP-2025-001",
  "name": "Artemchuk Nikolay",
  "status": "Employee",
  "department": "AI",
  "profession": "AI Engineer",
  "role_level": "Mid",
  "hire_date": "2024-03-01",
  "skills": {
    "technical": ["Python", "Machine Learning", "n8n"],
    "soft_skills": ["Problem Solving", "Communication"],
    "languages": ["English (C1)", "Russian", "Ukrainian"]
  },
  "tool_proficiency": {
    "Claude": "Advanced",
    "ChatGPT": "Intermediate",
    "n8n": "Expert"
  },
  "video_cv_link": "https://...",
  "portfolio_link": "https://...",
  "availability": "Available",
  "current_projects": ["Project_A"],
  "performance_metrics": {
    "tasks_completed": 45,
    "avg_quality_score": 4.5,
    "avg_completion_time": "2.5 hours"
  },
  "tags": ["ai", "python", "automation", "n8n"]
}
```

---

## 🎯 Business Value

- **Video-First Presentation:** Competitive differentiator in talent marketplace
- **Rapid Matching:** AI-powered client-talent matching reduces time to placement
- **Skills Gap Analysis:** Identifies training needs for employee development
- **Performance Tracking:** Data-driven performance evaluation and development paths
- **Scalability:** Supports growth from 32 to 40+ employees

---

## 📚 Related Documents

- `./Skills/` - Complete skills catalog (migrated from LIBRARIES/Skills)
- `../JOBS/` - Jobs employees apply to and work on
- `../BUSINESSES/` - Clients employees work with
- `../TASK_MANAGERS/` - Tasks assigned to employees
- `../LIBRARIES/Professions/` - Profession definitions and requirements
- `../LIBRARIES/Tools/` - Tools employees use

---

**Last Updated:** 2025-01-16

