# JOBS Entity Documentation

**Entity Type:** JOBS  
**Domain:** Talent Marketplace  
**Purpose:** Manages job openings, requirements, and talent matching  
**Created:** November 1, 2025  
**Last Updated:** November 1, 2025

---

## 📋 Overview

The JOBS entity domain manages the complete lifecycle of job postings, from creation through fulfillment. It standardizes job posting creation, enables AI-powered candidate matching, tracks hiring pipeline efficiency, and supports multi-platform job distribution.

---

## 🗂️ Sub-Entities

### 1. Job_Postings
**Purpose:** Active job listings and requirements

**Key Attributes:**
- Position title and description
- Required skills and experience levels
- Compensation ranges
- Location and remote work options
- Application deadlines
- Hiring manager assignments
- Status (Active, Filled, Cancelled, Archived)

**File Structure:**
```
Job_Postings/
├── Active/          # Currently open positions
├── Archived/        # Filled or cancelled positions
└── Templates/       # Reusable job posting templates
```

---

### 2. Job_Requirements
**Purpose:** Structured skill and experience requirements

**Key Attributes:**
- Skills matrix (technical and soft skills)
- Experience levels (Junior/Mid/Senior/Expert)
- Tool proficiency requirements
- Language requirements
- Certification requirements
- Education requirements

**File Structure:**
```
Job_Requirements/
├── Skills_Matrices/       # Skills requirements by role
└── Experience_Levels/     # Experience level definitions
```

---

### 3. Job_Templates
**Purpose:** Reusable job configurations

**Key Attributes:**
- Template name and category
- Standard fields and structure
- Default values
- Department/profession mapping
- Customization guidelines

**File Structure:**
```
Job_Templates/
├── IT_Templates/
├── Marketing_Templates/
├── Design_Templates/
└── Operations_Templates/
```

---

### 4. Job_Categories
**Purpose:** Classification and organization system

**Key Attributes:**
- Category hierarchy (Primary → Secondary → Tertiary)
- Associated job types
- Metadata tags
- Cross-references to professions

**File Structure:**
```
Job_Categories/
├── IT/
├── Marketing/
├── Design/
└── Operations/
```

---

## 🔗 Relationships

### Primary Relationships

1. **JOBS ↔ TALENTS**
   - Jobs require specific talent skills
   - Talents apply to jobs
   - Matching algorithm uses skills matrix

2. **JOBS ↔ BUSINESSES**
   - Businesses (clients) post jobs
   - Jobs filled with talents presented to businesses

3. **JOBS ↔ LIBRARIES**
   - Jobs reference professions from Professions library
   - Jobs use actions and objects from Libraries
   - Jobs require tools from Tools library

---

## 📊 Example Queries

### Find Jobs Requiring Specific Skills
```sql
-- Find all Frontend Developer jobs requiring React
SELECT j.title, j.description, j.skills_required
FROM Job_Postings j
JOIN Job_Requirements r ON j.id = r.job_id
WHERE r.skill_name = 'React'
  AND j.status = 'Active'
```

### Match Talents to Job Requirements
```sql
-- Find talents matching job requirements
SELECT t.name, t.skills
FROM Talents t
JOIN Job_Requirements r ON t.skills @> r.required_skills
WHERE r.job_id = [JOB_ID]
  AND t.availability = 'Available'
```

---

## 📝 File Naming Convention

**Pattern:** `JOBS_Job_Posting_[Position]_[Date].json`

**Examples:**
- `JOBS_Job_Posting_Frontend_Developer_2025_01_15.json`
- `JOBS_Job_Requirement_React_Skills_2025_01_15.json`
- `JOBS_Job_Template_IT_Position_v1.json`

---

## 🔄 Workflow Integration

### Job Posting Creation Workflow

1. **Create** + **Job Posting** + **for [Position]**
   - Use template from Job_Templates
   - Define requirements from Job_Requirements
   - Assign to category from Job_Categories
   - Set status to Active

2. **Match** + **Talent** + **to Job Posting**
   - Query TALENTS entity for matching skills
   - Score candidates based on requirements
   - Present top matches to hiring manager

3. **Update** + **Job Posting** + **with Status**
   - Track application progress
   - Update status (Active → Filled/Archived)
   - Archive to Job_Postings/Archived/

---

## 📋 Metadata Template

Every job posting file should include:

```json
{
  "entity_type": "JOBS",
  "sub_entity": "Job_Posting",
  "job_id": "JOB-2025-001",
  "title": "Frontend Developer",
  "status": "Active",
  "department": "Dev",
  "profession": "Frontend Developer",
  "created_date": "2025-01-15",
  "application_deadline": "2025-02-15",
  "hiring_manager": "Klimenko_Yaroslav",
  "requirements": {
    "skills": ["React", "TypeScript", "CSS"],
    "experience_level": "Mid",
    "tools": ["VS Code", "Git"]
  },
  "compensation": {
    "range": "$2000-3000/month",
    "currency": "USD"
  },
  "location": "Remote",
  "tags": ["frontend", "react", "typescript", "remote"]
}
```

---

## 🎯 Business Value

- **Standardization:** Consistent job posting format across all platforms
- **AI Matching:** Enables automated candidate-job matching
- **Efficiency:** Reduces time to create and post jobs
- **Tracking:** Provides visibility into hiring pipeline
- **Scalability:** Template system supports rapid expansion

---

## 📚 Related Documents

- `../LIBRARIES/Professions/` - Profession definitions
- `../TALENTS/` - Candidate and employee data
- `../BUSINESSES/` - Client job postings
- `../TASK_MANAGERS/Task_Templates/` - Job posting task templates

---

**Last Updated:** November 1, 2025

