# Human Resources Entity (HR)

**Entity ID:** HR
**Purpose:** Employee management, hiring, onboarding, task management
**Department:** Human Resources
**Created:** 2025-12-08
**Owner:** Niko_Kar_002

---

## Overview

The HR (Human Resources) entity manages all aspects of employee lifecycle and HR operations including:
- Employee onboarding and offboarding
- Video interviews (AI-assisted)
- Task management for HR team
- Attendance monitoring
- Employee file management
- Compliance tracking
- Dropbox storage monitoring
- Anti-Gravity browser tracking for verification

---

## Folder Structure

```
ENTITIES/HR/
├── README.md (this file)
├── video_interview_workflow.md (AI-assisted interviews)
├── employee_guidelines_monday.md (created from cluster 03)
├── onboarding_checklist.md (new hire process)
├── task_management.md (HR task workflows)
├── dropbox_monitoring.md (storage checks)
├── professions/
│   ├── recruiter.md
│   ├── hr_manager.md
│   ├── training_specialist.md
│   └── compliance_officer.md
└── employees/
    └── (individual employee folders/files)
```

---

## Core Functions

### 1. Video Interviews (AI-Assisted)

**Purpose:** Streamline hiring process with AI support

**Workflow:**
```
Candidate applies
  ↓
HR schedules video interview
  ↓
AI generates interview questions
  ↓
Candidate records responses
  ↓
AI analyzes:
  - Communication skills
  - Technical knowledge
  - Cultural fit indicators
  - Red flags
  ↓
AI provides summary + score
  ↓
HR reviews AI analysis
  ↓
Makes hiring decision
```

**File:** video_interview_workflow.md

**Features:**
- Automated question generation
- Response analysis
- Candidate scoring
- Bias reduction
- Time efficiency

---

### 2. Employee Onboarding

**Purpose:** Consistent new hire experience

**Checklist Phases:**
1. **Pre-Start (1 week before)**
   - Equipment ordered
   - Accounts created
   - Workspace prepared
   - Welcome package sent

2. **Day 1**
   - Welcome meeting
   - Equipment setup
   - System access verification
   - Initial training

3. **Week 1**
   - Team introductions
   - Role overview
   - Training schedule
   - First assignments

4. **Month 1**
   - Progress check-ins
   - Feedback sessions
   - Integration assessment
   - Milestone review

**File:** onboarding_checklist.md

---

### 3. Task Management

**Purpose:** HR team task coordination

**Types of Tasks:**
- Recruitment activities
- Onboarding processes
- Employee requests
- Compliance deadlines
- Training coordination
- Performance reviews

**Integration:**
- Automation agent detects "PROCESS hiring" or "EXECUTE onboarding"
- Creates tasks in Share/
- Routes to HR agent
- Tracks completion

**File:** task_management.md

---

### 4. Employee Verification (Anti-Gravity Browser)

**From Cluster 03:**
- Browser tracking for employee activity
- Google Gravity communication verification
- Monday.com guidelines
- Activity monitoring

**Purpose:**
- Verify employee engagement
- Track communication patterns
- Ensure guideline compliance
- Identify issues early

**File:** employee_guidelines_monday.md (already created)

---

### 5. Dropbox Storage Monitoring

**Purpose:** Prevent storage issues

**Monitoring:**
- Check Dropbox storage weekly
- Alert at 80% capacity
- Plan cleanup before limits
- Track per-employee usage

**Workflow:**
```
Automation agent checks Dropbox size
  ↓
If > 80% full:
  ↓
Create alert in Reminders/
  ↓
HR reviews largest folders
  ↓
Archives old content
  ↓
Notifies employees if needed
```

**File:** dropbox_monitoring.md

---

### 6. Attendance Monitoring

**Purpose:** Track work hours and lateness

**Integration with Automation Agent:**
- Scans DAILIES/ folder for check-in files
- Detects late arrivals (> 15 min after 9:00 AM)
- Alerts HR to absences
- Generates weekly reports

**Settings:**
- Work start: 9:00 AM
- Late threshold: 15 minutes
- Track in: attendance_checker.py module

---

## Integration Points

### With Automation Agent
- Detects HR-related reserved words
- Creates tasks automatically
- Monitors attendance
- Checks Dropbox storage
- Sends alerts to Reminders/

### With DAILIES/ Folder
- Employee daily files
- Check-in tracking
- Activity monitoring
- Performance indicators

### With Monday.com
- Task assignment
- Project tracking
- Employee guidelines
- Communication protocols

### With Anti-Gravity Browser
- Employee verification
- Activity tracking
- Communication monitoring
- Google Gravity integration

---

## Profession Data

### Location
ENTITIES/HR/professions/

### Roles Defined

**1. Recruiter**
- Source candidates
- Conduct interviews (video + in-person)
- Screen applications
- Coordinate hiring process

**2. HR Manager**
- Team leadership
- Policy enforcement
- Employee relations
- Strategic planning

**3. Training Specialist**
- Onboarding coordination
- Training program development
- Skill development
- Performance improvement

**4. Compliance Officer**
- Legal compliance
- Policy documentation
- Risk management
- Audit preparation

---

## AI-Assisted Features

### Video Interview Analysis

**AI Evaluates:**
1. **Communication:**
   - Clarity of expression
   - Professional demeanor
   - Response completeness

2. **Technical Skills:**
   - Knowledge depth
   - Problem-solving approach
   - Experience validation

3. **Cultural Fit:**
   - Values alignment
   - Team compatibility
   - Work style match

4. **Red Flags:**
   - Inconsistencies
   - Concerning responses
   - Missing qualifications

**Output:**
```markdown
# Candidate: [Name]
**Position:** [Role]
**Interview Date:** YYYY-MM-DD

## AI Analysis Summary

**Overall Score:** 7.5/10

**Strengths:**
- Strong technical knowledge
- Excellent communication
- Relevant experience

**Concerns:**
- Limited team leadership experience
- Salary expectations high

**Recommendation:** Proceed to next round

**Detailed Analysis:**
[Section-by-section breakdown]
```

---

## Monday.com Guidelines

**From Cluster 03 (employee_guidelines_monday.md):**

### Core Principles
1. All tasks logged in Monday
2. Daily status updates required
3. Transparent communication
4. Deadline adherence
5. Team collaboration

### Usage Requirements
- Check Monday twice daily minimum
- Update task status immediately upon completion
- Comment on assigned tasks
- Use appropriate labels/tags
- Set realistic deadlines

---

## Implementation Priority

### Day 08 (Current)
- [x] Create HR entity structure
- [ ] Create video_interview_workflow.md
- [ ] Create onboarding_checklist.md
- [ ] Create task_management.md
- [ ] Create dropbox_monitoring.md

### Week 02
- [ ] Populate profession data files
- [ ] Test video interview AI integration
- [ ] Build onboarding automation
- [ ] Test Dropbox monitoring

### Week 03
- [ ] Implement HR Agent
- [ ] Integrate with automation-agent
- [ ] Deploy attendance monitoring
- [ ] Build Monday.com integration

---

## Compliance & Privacy

### Data Handling
- Employee data is confidential
- Video interviews stored securely
- AI analysis anonymized where possible
- GDPR/privacy compliance required

### Access Control
- HR team only
- Encrypted storage
- Audit trail maintained
- Regular access reviews

---

## Metrics & Reporting

### Key HR Metrics
- Time to hire (days)
- Onboarding completion rate
- Employee retention (90-day, 1-year)
- Attendance rate
- Training completion

### Weekly Reports
- New hires this week
- Onboarding in progress
- Open positions
- Attendance issues
- Storage status

### Monthly Reports
- Hiring pipeline status
- Retention analysis
- Training effectiveness
- Compliance status
- Budget vs actual

---

## Next Steps

1. Create video_interview_workflow.md (detailed AI process)
2. Create onboarding_checklist.md (comprehensive)
3. Create task_management.md (HR workflows)
4. Create dropbox_monitoring.md (automation)
5. Populate profession data files
6. Test AI interview analysis
7. Build HR Agent (Week 03)

---

**Entity Status:** Structure created - Content population in progress
**Dependencies:** Automation-agent, Monday.com, Anti-Gravity browser, AI interview platform
**Priority:** High (critical business function)
