# Reserved Action Vocabulary System

**Version:** 1.0
**Created:** 2025-12-07
**Purpose:** Define reserved action verbs for automated task detection and processing
**Location:** ENTITIES/Actions/

---

## System Overview

Reserved action words are special verbs that trigger automated task processing when detected in employee Daily files. Scripts scan files every 15 minutes to identify these verbs and execute corresponding workflows.

### Core Principle
- Each reserved word = One specific action type
- Consistent usage across all employee files
- Script-detectable as defined variables
- Creates executable tasks automatically

---

## Reserved Action Verbs

### 1. **RESEARCH**
**Definition:** Investigate, gather information, analyze options, compare solutions
**Output:** Documentation with findings, sources, and recommendations
**Trigger Behavior:** Creates research task in Share/ folder
**Example Usage:**
- "RESEARCH cloud solutions with $1000/month budget"
- "RESEARCH Reddit communities for AI + local models"
- "RESEARCH pricing comparison for servers"

**Script Action:**
- Identify research topic
- Create research task file in folder 07
- Track progress in dashboard
- Require deliverable with sources section

---

### 2. **BUILD**
**Definition:** Construct, develop, create functional systems or features
**Output:** Working code, system, or infrastructure
**Trigger Behavior:** Creates development task with specification requirement
**Example Usage:**
- "BUILD YouTube research dashboard"
- "BUILD WhatsApp agent for note-taking"
- "BUILD trigger system for tool automation"

**Script Action:**
- Extract technical requirements
- Create specification document
- Assign to development queue
- Track milestones

---

### 3. **CREATE**
**Definition:** Make new files, folders, documents, or content
**Output:** New file system entities or documentation
**Trigger Behavior:** File/folder creation task
**Example Usage:**
- "CREATE Week_2 folder structure"
- "CREATE learning materials for employee training"
- "CREATE Reminders folder inside Entities"

**Script Action:**
- Parse folder/file specifications
- Execute creation commands
- Update folder structure map
- Log in Execution/ folder

---

### 4. **UPGRADE**
**Definition:** Improve, enhance, update existing systems or content
**Output:** Updated version of existing entity
**Trigger Behavior:** Modification task with version tracking
**Example Usage:**
- "UPGRADE prompt 7.2 with backend information"
- "UPGRADE Week_2 folder structure"

**Script Action:**
- Identify target entity
- Create backup before modification
- Track version changes
- Document upgrade details

---

### 5. **TEACH**
**Definition:** Educate, train, provide learning materials
**Output:** Training content, documentation, instructional materials
**Trigger Behavior:** Creates training task with assessment requirement
**Example Usage:**
- "TEACH employees on Monday about key bindings"
- "TEACH reserved action words"
- "TEACH memory retention techniques"

**Script Action:**
- Create training material outline
- Schedule training session
- Prepare assessment method
- Track employee learning progress

---

### 6. **PROCESS**
**Definition:** Handle, transform, analyze existing data or content
**Output:** Processed/transformed data
**Trigger Behavior:** Data processing pipeline task
**Example Usage:**
- "PROCESS daily list with main prompt 7.2"
- "PROCESS transcriptions every 15 minutes"
- "PROCESS old server data and migrate to cloud"

**Script Action:**
- Identify input data source
- Apply processing workflow
- Save output to Output/ folder
- Track processing completion

---

### 7. **SHARE**
**Definition:** Distribute, send, communicate information to team
**Output:** Shared files, communications, distributed tasks
**Trigger Behavior:** Creates distribution task
**Example Usage:**
- "SHARE API tokens with employees"
- "SHARE instructions via Discord"
- "SHARE custom instructions"

**Script Action:**
- Identify recipients
- Prepare shared content
- Move to Share/ folder
- Send notifications

---

### 8. **EXECUTE**
**Definition:** Run, implement, carry out planned actions
**Output:** Execution results and logs
**Trigger Behavior:** Marks task for immediate execution
**Example Usage:**
- "EXECUTE cloud research plan"
- "EXECUTE daily file processing"

**Script Action:**
- Run specified task
- Log execution details
- Save results to Execution/ folder
- Update dashboard status

---

### 9. **REVIEW**
**Definition:** Examine, analyze, evaluate existing work
**Output:** Review notes, feedback, quality assessment
**Trigger Behavior:** Creates review task
**Example Usage:**
- "REVIEW prompt 7.2 specifications"
- "REVIEW employee progress"

**Script Action:**
- Load target content
- Apply review criteria
- Document findings
- Flag issues for attention

---

### 10. **MARK**
**Definition:** Flag, highlight, designate for attention
**Output:** Marked items in attention queue
**Trigger Behavior:** Adds to executive attention dashboard
**Example Usage:**
- "MARK for executive attention"
- "MARK as urgent reminder"

**Script Action:**
- Add to attention pile
- Set priority level
- Create reminder entry
- Update dashboard

---

## Script Detection Rules

### Syntax Requirements
1. Reserved word must be in UPPERCASE
2. Must appear at start of line or after bullet/number
3. Followed by space and action description
4. Can appear multiple times in one file

### Detection Pattern
```
[RESERVED_WORD] [action description]
```

### Examples
```
- RESEARCH pricing options for cloud servers
1. BUILD attendance tracking microservice
* CREATE folder 07 for documentation
EXECUTE daily processing workflow
```

### Invalid Patterns (will not trigger)
```
research pricing options (lowercase - ignored)
We need to RESEARCH later (mid-sentence - ignored)
```

---

## Automation Workflow

### 15-Minute Loop Process
1. **Scan Phase:**
   - Check all employee Daily files
   - Identify reserved action verbs
   - Extract action descriptions

2. **Parse Phase:**
   - Create task objects
   - Assign priority levels
   - Determine dependencies

3. **Route Phase:**
   - Sort tasks by type
   - Move to appropriate folders
   - Update tracking systems

4. **Execute Phase:**
   - Run executable tasks
   - Create work files
   - Log progress

5. **Report Phase:**
   - Update dashboard
   - Flag executive attention items
   - Send notifications

---

## File Naming Conventions

### Task Files
- Format: `[YYMMDD]_[ACTION]_[brief-description].md`
- Example: `251207_RESEARCH_cloud-pricing.md`

### Output Files
- Format: `[original-name]_AI.md`
- Example: `06_wspr_AI.md`

### Log Files
- Format: `[YYMMDD]_[HHMM]_execution-log.md`
- Example: `251207_1430_execution-log.md`

---

## Employee Training Requirements

### Memorization Priority (Week_2)
1. RESEARCH (highest frequency)
2. CREATE (folder/file operations)
3. BUILD (development tasks)
4. PROCESS (daily workflows)
5. SHARE (team collaboration)

### Training Method
- No rote repetition
- Context linking to ecosystem
- Recall testing within 3 minutes
- Practical usage examples
- Real task execution practice

### Assessment
- Identify reserved words in sample files
- Write tasks using correct syntax
- Explain automation behavior for each verb

---

## Integration with Other Systems

### Links to:
- **Dashboard:** Task progress tracking
- **Share/ folder:** Distribution system
- **Output/ folder:** Processed results
- **Execution/ folder:** Execution logs
- **Reminders/ folder:** Flagged items

### Data Flow
```
Daily File → Reserved Word Detection → Task Creation →
→ Folder Routing → Execution → Output → Dashboard Update
```

---

## Version Control

### Current Version: 1.0
- Initial 10 reserved action verbs
- 15-minute loop automation
- Basic task routing

### Planned Updates (v1.1)
- Add SCHEDULE verb for calendar integration
- Add ARCHIVE verb for cleanup workflows
- Enhanced context awareness
- Multi-step task chaining

---

## References

**Source Document:** Week_01/06/06_wspr.md
**Implementation Date:** Week_2 (December 9-13, 2025)
**Training Session:** Monday, Week_2
**Automation Script:** To be developed Week_2

---

**Backup Location:** ENTITIES/Reserve/RESERVED_VOCABULARY.md
