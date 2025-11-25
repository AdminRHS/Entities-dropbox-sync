# PROMPT: Build Employee Profile Schema Workflow - Complete Data Collection System

## Objective
Create a comprehensive Employee Profile Schema by analyzing all data sources in Nov25 employee folders, then collect and organize all Profile*.md files into a centralized TALENTS/Employees/profiles/ structure following taxonomy-based analysis methodology.

## Workflow Overview

This workflow executes a complete employee data collection and schema creation process:
1. **Schema Creation**: Document all data sources and map them to schema fields using taxonomy methodology
2. **Directory Structure**: Create organized folder hierarchy for profile storage
3. **Profile Collection**: Gather all Profile*.md files from Nov25 departments
4. **Organization**: Organize profiles by department and status (including Left folder handling)

---

## Phase 1: Schema Creation

### Step 1.1: Analyze Profile Structure
**Source**: `Nov25/{Department}/{Employee Name}/Profile*.md`

**Core Fields Identified**:
- ID (Number, Required)
- Name (String, Required)
- Age (Number, Optional)
- Country (String, Optional)
- Start Date (Date, Optional, Format: MM/DD/YYYY)
- Contact Information (Personal Email, Work Email, Discord ID, Phone, Telegram)
- Position (Profession, Shift, Rate, Status)
- Skills (Array, Comma-separated)
- Tools (Array, Comma-separated)
- Summary (Text)

### Step 1.2: Identify Extended Data Sources
**Following Taxonomy Methodology** (from PROMPT_Build_LIBRARIES_Taxonomy.md):

**Data Sources to Analyze**:
1. **daily.md** - Daily work logs with activities, transcripts, outcomes
2. **plans.md** - Strategic plans with priorities and goals
3. **task.md** - Task breakdowns with action items and steps
4. **README.md** - Workflow documentation and onboarding info
5. **notes.md** - Additional notes and learning materials
6. **JSON files** - Structured data (task templates, employee exports)
7. **Folder Structure** - Work patterns and organization metrics
8. **Overview Nov25** - Department analysis files with performance data

### Step 1.3: Create Schema Document
**Output File**: `ENTITIES/TALENTS/Employees/Employee_Profile_Schema.md`

**Schema Structure**:
- Core Profile Fields (from Profile*.md)
- Extended Data Sources Taxonomy
- Field Mapping Tables
- Data Extraction Rules
- Validation Rules
- Integration Points (LIBRARIES, TASK_MANAGERS)
- Department-Specific Patterns
- Complete Output Schema Format (JSON structure)

**Key Sections**:
- Data Source Priority Matrix (P0-P4)
- Data Extraction Rules (Skills, Tools, Status, Work History, Performance Metrics)
- Schema Validation Rules (10 validation rules)
- Cross-Entity Relationships (LIBRARIES → TALENTS → TASK_MANAGERS)

---

## Phase 2: Directory Structure Creation

### Step 2.1: Create Base Directory
**Location**: `ENTITIES/TALENTS/Employees/profiles/`

### Step 2.2: Create Department Subdirectories
**Subdirectories**:
- `AI/` - AI Department profiles
- `Design/` - Design Department profiles
- `Dev/` - Development Department profiles
- `LG/` - Lead Generation Department profiles
- `Video/` - Video Department profiles
- `Left/` - Profiles from Left folders (terminated/left employees)

**Command**:
```bash
mkdir -p "ENTITIES/TALENTS/Employees/profiles/{AI,Design,Dev,LG,Video,Left}"
```

---

## Phase 3: Profile Collection

### Step 3.1: Collect AI Department Profiles
**Source**: `Nov25/AI/**/Profile*.md`
**Destination**: `ENTITIES/TALENTS/Employees/profiles/AI/`
**Expected Count**: 3 files

**Command**:
```bash
find "Nov25/AI" -name "Profile*.md" -type f -exec cp {} "ENTITIES/TALENTS/Employees/profiles/AI/" \;
```

**Files Collected**:
- Profile Project manager, Lead generator Artemchuk Nikolay.md
- Profile Prompt engineer Perederii Vladislav.md
- Profile Prompt engineer Zasiadko Matvii.md

### Step 3.2: Collect Design Department Profiles
**Source**: `Nov25/Design/**/Profile*.md`
**Destination**: `ENTITIES/TALENTS/Employees/profiles/Design/`
**Expected Count**: 18-19 files

**Command**:
```bash
find "Nov25/Design" -name "Profile*.md" -type f -exec cp {} "ENTITIES/TALENTS/Employees/profiles/Design/" \;
```

### Step 3.3: Collect Dev Department Profiles
**Source**: `Nov25/Dev/**/Profile*.md`
**Destination**: `ENTITIES/TALENTS/Employees/profiles/Dev/`
**Expected Count**: 6-7 files

**Command**:
```bash
find "Nov25/Dev" -name "Profile*.md" -type f -exec cp {} "ENTITIES/TALENTS/Employees/profiles/Dev/" \;
```

### Step 3.4: Collect LG Department Profiles
**Source**: `Nov25/LG/**/Profile*.md` (excluding Left folder)
**Destination**: `ENTITIES/TALENTS/Employees/profiles/LG/`
**Expected Count**: ~22 files

**Command**:
```bash
find "Nov25/LG" -name "Profile*.md" -type f ! -path "*/Left/*" -exec cp {} "ENTITIES/TALENTS/Employees/profiles/LG/" \;
```

### Step 3.5: Collect Video Department Profiles
**Source**: `Nov25/Video/**/Profile*.md` (excluding Left folder)
**Destination**: `ENTITIES/TALENTS/Employees/profiles/Video/`
**Expected Count**: 2 files

**Command**:
```bash
find "Nov25/Video" -name "Profile*.md" -type f ! -path "*/Left/*" -exec cp {} "ENTITIES/TALENTS/Employees/profiles/Video/" \;
```

### Step 3.6: Collect Left Folder Profiles
**Source**: `Nov25/{LG,Video}/Left/**/Profile*.md`
**Destination**: `ENTITIES/TALENTS/Employees/profiles/Left/`
**Expected Count**: ~5 files

**Commands**:
```bash
# LG Left folder
find "Nov25/LG/Left" -name "Profile*.md" -type f -exec cp {} "ENTITIES/TALENTS/Employees/profiles/Left/" \;

# Video Left folder
find "Nov25/Video/Left" -name "Profile*.md" -type f -exec cp {} "ENTITIES/TALENTS/Employees/profiles/Left/" \;
```

---

## Phase 4: Validation and Verification

### Step 4.1: Verify File Counts
**Command**:
```bash
echo "AI: $(ls -1 'ENTITIES/TALENTS/Employees/profiles/AI/' | wc -l)"
echo "Design: $(ls -1 'ENTITIES/TALENTS/Employees/profiles/Design/' | wc -l)"
echo "Dev: $(ls -1 'ENTITIES/TALENTS/Employees/profiles/Dev/' | wc -l)"
echo "LG: $(ls -1 'ENTITIES/TALENTS/Employees/profiles/LG/' | wc -l)"
echo "Video: $(ls -1 'ENTITIES/TALENTS/Employees/profiles/Video/' | wc -l)"
echo "Left: $(ls -1 'ENTITIES/TALENTS/Employees/profiles/Left/' | wc -l)"
echo "Total: $(find 'ENTITIES/TALENTS/Employees/profiles' -name 'Profile*.md' -type f | wc -l)"
```

**Expected Results**:
- AI: 3
- Design: 19
- Dev: 7
- LG: 22
- Video: 2
- Left: 5
- **Total: 58**

### Step 4.2: Verify Schema Document
**Check**: `ENTITIES/TALENTS/Employees/Employee_Profile_Schema.md` exists and contains:
- ✓ Core Profile Fields section
- ✓ Extended Data Sources Taxonomy (8 data sources)
- ✓ Field Mapping Tables
- ✓ Data Extraction Rules
- ✓ Validation Rules
- ✓ Integration Points
- ✓ Complete Output Schema Format

---

## Data Source Taxonomy Mapping

### Priority Matrix

| Priority | Source | Use Case | Update Frequency |
|----------|--------|----------|------------------|
| **P0** | Profile*.md | Core employee data | On creation/update |
| **P1** | daily.md | Work activities, skills, tools | Daily |
| **P1** | Overview Nov25 | Performance reviews, role | Monthly/Quarterly |
| **P2** | plans.md | Current projects, goals | Weekly |
| **P2** | task.md | Task patterns, skills | Weekly |
| **P3** | README.md | Workflow compliance | On change |
| **P3** | notes.md | Learning, preferences | As needed |
| **P4** | JSON files | Structured data, templates | On creation |
| **P4** | Folder structure | Activity metrics | Monthly |

### Field Extraction Rules

**Rule 1: Skills Extraction**
- Sources: Profile*.md Skills field, daily.md activities, task.md tools, JSON task templates
- Method: Merge all sources, deduplicate, maintain comma-separated format
- Update: Add new skills from daily.md and task.md activities

**Rule 2: Tools Extraction**
- Sources: Profile*.md Tools field, daily.md tools used, task.md tools required, JSON templates
- Method: Merge all sources, deduplicate, categorize by type
- Update: Add new tools from daily work logs

**Rule 3: Status Updates**
- Sources: Profile*.md Status field, Overview Nov25 analysis, folder location (Left/)
- Method: Check folder path for "Left/" or "LEFT/" → set Status to "LEFT"
- Update: Automatic on folder detection, manual on profile update

**Rule 4: Work History**
- Sources: daily.md files aggregated chronologically
- Method: Extract activities, outcomes, projects from all daily.md files
- Update: Append new entries daily

**Rule 5: Performance Metrics**
- Sources: Overview Nov25 analysis files, daily.md consistency, folder structure
- Method: Calculate activity frequency, completion rates, organization scores
- Update: Recalculate monthly

---

## Integration Points

### LIBRARIES Taxonomy Integration
- **Professions**: Map Employee.Profession → PRF-### (Professions taxonomy)
- **Tools**: Map Employee.Tools[] → TLS-### (Tools taxonomy)
- **Skills**: Map Employee.Skills[] → SKL-### (Skills taxonomy)
- **Departments**: Map Employee.Department → DPT-### (Departments taxonomy)
- **Statuses**: Map Employee.Status → STS-### (Statuses taxonomy)

### TASK_MANAGERS Integration
- **Task Templates**: Link Employee.TaskTemplates[] → TSK-### (Task templates)
- **Projects**: Link Employee.Projects[] → PRJ-### (Projects)
- **Actions**: Extract from tasks → ACT-### (Actions taxonomy)

### Cross-Entity Relationships
```
Employee (TALENTS)
  ├─ Profession → PRF-### (LIBRARIES)
  ├─ Department → DPT-### (LIBRARIES)
  ├─ Tools → TLS-### (LIBRARIES)
  ├─ Skills → SKL-### (LIBRARIES)
  ├─ Projects → PRJ-### (TASK_MANAGERS)
  └─ Tasks → TSK-### (TASK_MANAGERS)
```

---

## Department-Specific Patterns

### AI Department
- **Common Files**: daily.md, plans.md, task.md, README.md, JSON task templates
- **Special Patterns**: Overview Nov25 analysis files, automation workflows
- **Tools**: Claude, ChatGPT, Cursor, n8n, Python scripts
- **Skills**: Prompt engineering, automation, project management

### Design Department
- **Common Files**: daily.md, plans.md, task.md, README.md
- **Special Patterns**: Design deliverables, portfolio links
- **Tools**: Figma, Adobe Suite, Canva, design systems
- **Skills**: UI/UX design, graphic design, illustration

### Dev Department
- **Common Files**: daily.md, plans.md, task.md, notes.md, README.md
- **Special Patterns**: Code repositories, technical documentation
- **Tools**: VS Code, Cursor, Git, development frameworks
- **Skills**: Programming languages, frameworks, development methodologies

### LG (Lead Generation) Department
- **Common Files**: daily.md, plans.md, task.md, README.md
- **Special Patterns**: Lead tracking, outreach metrics
- **Tools**: CRM systems, email tools, LinkedIn, research tools
- **Skills**: Lead generation, outreach, research, communication

### Video Department
- **Common Files**: daily.md, plans.md, task.md, README.md
- **Special Patterns**: Video project folders, editing workflows
- **Tools**: Video editing software, transcription tools, content platforms
- **Skills**: Video editing, content creation, post-production

---

## Validation Rules

1. **ID Uniqueness**: Employee ID must be unique across all profiles
2. **Required Fields**: ID, Name, Profession, Status are mandatory
3. **Date Format**: Start Date must be MM/DD/YYYY format
4. **Status Values**: Must be one of: Available, Work, Project, Part Time, On Leave, Fired, LEFT
5. **Skills Format**: Comma-separated list, no duplicates
6. **Tools Format**: Comma-separated list, no duplicates
7. **Email Validation**: Email fields must contain "@" symbol if not "Not specified"
8. **Phone Format**: Phone numbers should be numeric strings
9. **Discord ID**: Must be numeric string if not "Not specified"
10. **Rate**: Must be numeric (typically 0.5, 0.75, or 1.0)

---

## Output Deliverables

### 1. Schema Document
**File**: `ENTITIES/TALENTS/Employees/Employee_Profile_Schema.md`
- Complete field documentation
- Data source taxonomy
- Extraction rules
- Validation rules
- Integration points

### 2. Profile Collection
**Location**: `ENTITIES/TALENTS/Employees/profiles/`
- Organized by department
- Separate Left folder for terminated employees
- All Profile*.md files preserved with original names

### 3. Directory Structure
```
ENTITIES/TALENTS/Employees/profiles/
├── AI/                    (3 profiles)
├── Design/                 (19 profiles)
├── Dev/                    (7 profiles)
├── LG/                     (22 profiles)
├── Video/                  (2 profiles)
└── Left/                   (5 profiles)
```

---

## Execution Checklist

### Pre-Execution
- [ ] Verify Nov25 folder structure exists
- [ ] Verify ENTITIES/TALENTS/Employees/ directory exists
- [ ] Review PROMPT_Build_LIBRARIES_Taxonomy.md for methodology

### Execution Steps
- [ ] Create Employee_Profile_Schema.md with taxonomy structure
- [ ] Create profiles/ directory structure
- [ ] Copy AI department profiles (3 files)
- [ ] Copy Design department profiles (19 files)
- [ ] Copy Dev department profiles (7 files)
- [ ] Copy LG department profiles (22 files)
- [ ] Copy Video department profiles (2 files)
- [ ] Copy Left folder profiles (5 files)

### Post-Execution Verification
- [ ] Verify all 58 profiles collected
- [ ] Verify schema document completeness
- [ ] Verify directory structure correct
- [ ] Verify no duplicate files
- [ ] Verify Left folder profiles separated correctly

---

## Reverse Workflow (Cleanup)

### To Reverse This Workflow:

**Step 1: Remove Profile Collection**
```bash
rm -rf "ENTITIES/TALENTS/Employees/profiles/"
```

**Step 2: Remove Schema Document**
```bash
rm "ENTITIES/TALENTS/Employees/Employee_Profile_Schema.md"
```

**Note**: Original Profile*.md files in Nov25 folders remain untouched.

---

## Success Criteria

✓ **Schema Document Created**: Complete taxonomy-based schema with all data sources documented
✓ **Directory Structure Created**: All 6 department folders created
✓ **All Profiles Collected**: 58 Profile*.md files collected and organized
✓ **Left Folder Handling**: Profiles from Left folders properly separated
✓ **Original Files Preserved**: All original Profile*.md files remain in Nov25 folders
✓ **Validation Passed**: All file counts match expected values
✓ **Integration Documented**: Cross-entity relationships mapped to LIBRARIES taxonomy

---

## Notes

- **Taxonomy Methodology**: Follows PROMPT_Build_LIBRARIES_Taxonomy.md structure
- **Data Priority**: Core profile data (Profile*.md) takes precedence, extended data supplements
- **Automation Ready**: Schema designed for automated data extraction and population
- **Extensible**: New data sources can be added following the same taxonomy pattern
- **Source Tracking**: All fields maintain reference to source file for traceability
- **Status Automation**: Left folder detection automatically updates Status to "LEFT"

---

## Related Prompts

- `PROMPT_Build_LIBRARIES_Taxonomy.md` - Taxonomy methodology reference
- Employee profile status automation rules (workspace rules)
- Version control automation rules (workspace rules)

---

**Created**: 2025-01-18
**Last Updated**: 2025-01-18
**Workflow Version**: 1.0

