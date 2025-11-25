# Plan: Process November 20 Daily Reports with v2.1 Department Prompts

**Date Created**: 2025-11-21
**Target Date**: 2025-11-20 (November 20)
**Status**: Complete ✅
**Version**: 1.0

---

## Overview

Process daily activity files from 30 employees across 8 departments (AI, Design, Dev, Finance, HR, LG, Sales, Video) for November 20, 2025, using the newly created v2.1 department report prompts with TASK_MANAGERS entity integration.

---

## Data Sources

**Base Location**: `C:\Users\Dell\Dropbox\Nov25\`

**Folder Patterns**:
- Direct: `[Department] Nov25\[Employee]\20\`
- Week-based: `[Department] Nov25\[Employee]\Week_3\20\`

**Total Employees**: 30 with "20" folders

**Standard File Types**:
- `daily.md` - Primary activity log with Whisper Flow transcripts
- `task.md` - Detailed task breakdowns with action steps
- `plans.md` - Planning and priorities
- `TODO.md` - Next-day priorities and reminders

**Special Cases**:
- Finance: Uses `report.md` instead of `task.md`
- Sales: Only has `TODO.md` (minimal documentation)
- Video: Includes `daily_processed.md` (pre-processed version)

---

## Department Breakdown

### AI Department (2 employees)
**Folder**: `AI Nov25`
- Artemchuk Nikolay (`Week_3/20`)
- Perederii Vladislav (`20` and `Week_3/20`)

**Prompt**: PMT-033_AI_Daily_Report_v2.1.md
**Files**: daily.md, plans.md, task.md
**Focus**: Prompt engineering, AI integration, automation workflows

---

### Design Department (8 employees)
**Folder**: `Design Nov25`
- Bogun Polina (`Week_3/20`)
- Bykova Anastasiia (`Week_3/20`)
- Hlushko Mariia (`Week_3/20`)
- Kucherenko Iuliia (`Week_3/20`)
- Litvinova Natalia (`Week_3/20`)
- Safonova Eleonora (`Week_3/20`)
- Shymkevych Iryna (`20`)
- Skrypkar Vilhelm (`Week_3/20`)

**Prompt**: PMT-035_Design_Daily_Report_v2.1.md
**Files**: daily.md, plans.md, task.md, TODO.md
**Focus**: UI/UX design, graphic design, client deliverables

---

### Development Department (5 employees)
**Folder**: `Dev Nov25`
- Artem Skichko (`20`)
- Azar Imranov (`Week_3/20`)
- Danylenko Liliia (`Week_3/20`)
- Kizilova Olha (`Week_3/20`)
- Klimenko Yaroslav (`Week_3/20`)

**Prompt**: PMT-036_Dev_Daily_Report_v2.1.md
**Files**: daily.md, plans.md, task.md, TODO.md
**Focus**: Frontend/backend development, bug fixes, technical implementation

---

### Finance Department (2 employees) - SPECIAL HANDLING
**Folder**: `Fin Nov25`
- Ponomarova Kateryna (`20`)
- Yelisieieva Daria (`20`)

**Prompt**: PMT-037_Finance_Daily_Report_v2.1.md
**Files**: daily.md, **report.md** (not task.md)
**Focus**: Financial tracking, employee monitoring, hours tracking
**Note**: May include Ukrainian language content

---

### HR Department (3 employees)
**Folder**: `HR Nov25`
- Nealova Evgeniya (`Week_3/20`)
- Pasichna Anastasiia (`Week_3/20`)
- Rekonvald Viktoriya (`Week_3/20`)

**Prompt**: PMT-038_HR_Daily_Report_v2.1.md
**Files**: daily.md, plans.md, task.md, TODO.md
**Focus**: Recruitment, candidate sourcing, interviews, onboarding

---

### Lead Generation Department (6 employees)
**Folder**: `LG Nov25`
- Alakbarova Ulviyya Javid (`20`)
- Bindiak Dana (`20` and `Week_3/20`)
- Burda Anna (`20` and `Week_3/20`)
- Cynthia Aninwezi (`20`)
- Peneva Plamena (`20`)
- Shkinder Kseniia (`20` and `Week_3/20`)

**Prompt**: PMT-039_LG_Daily_Report_v2.1.md
**Files**: daily.md, plans.md, task.md
**Focus**: Lead sourcing, CRM updates, cold outreach, follow-ups

---

### Sales Department (2 employees) - MINIMAL DOCUMENTATION
**Folder**: `Sales Nov25`
- Bessarab Valeriia (`20`)
- Kovalska Anastasiya (`20`)

**Prompt**: PMT-041_Sales_Daily_Report_v2.1.md
**Files**: **TODO.md only**
**Focus**: Next-day action items
**Note**: Very limited data, abbreviated reports expected

---

### Video Department (2 employees) - ENHANCED DOCUMENTATION
**Folder**: `Video Nov25`
- Azanova Darʼya (`Week_3/20`)
- Podolskyi Sviatoslav (`Week_3/20`)

**Prompt**: PMT-043_Video_Daily_Report_v2.1.md
**Files**: daily.md, **daily_processed.md**, plans.md, task.md, TODO.md
**Focus**: Video editing, production work, content creation
**Note**: Has pre-processed daily logs

---

## Processing Workflow

### Phase 1: Individual Department Processing

**For each department**:

1. **Collect Employee Data**
   - Navigate to department folder
   - Find all employee subfolders with "20" directory
   - Handle both direct `/20/` and `/Week_3/20/` paths
   - List all available files

2. **Read Activity Files**
   - Priority 1: `daily.md` (activities + Whisper Flow transcripts)
   - Priority 2: `task.md` or `report.md` (structured tasks)
   - Priority 3: `plans.md` (planning context)
   - Priority 4: `TODO.md` (next-day actions)
   - Priority 5: `daily_processed.md` (Video only)

3. **Apply Department v2.1 Prompt**
   - Load appropriate PMT-0XX_v2.1.md prompt
   - Process employee activities
   - Extract entities using token-efficient format
   - Map to TASK_MANAGERS (PRT, MLT, TST, STT)
   - Assign confidence scores

4. **Generate Department Report**
   - Use 10-section schema:
     1. Executive Summary
     2. Project Contributions
     3. Milestone Progress
     4. Task Sequences
     5. Cross-Department Coordination
     6. Department-Specific Activities
     7. Next Day Plans
     8. Research Needed
     9. Improvements Needed
     10. Metrics Summary
   - Include all employees from department
   - Aggregate entity mappings

---

### Phase 2: Master Report Aggregation

1. **Collect Department Reports**
   - Load all 8 department reports
   - Verify completeness

2. **Apply PMT-032 (Daily Report Collection v2.1)**
   - Aggregate cross-department insights
   - Identify interdependencies
   - Highlight blockers and coordination needs
   - Summarize company-wide progress

3. **Generate Master Report**
   - Executive overview
   - Department summaries
   - Cross-functional initiatives
   - Entity mapping statistics
   - Action items and priorities

---

## Output Structure

### Individual Department Reports
**Location**: `C:\Users\Dell\Dropbox\ENTITIES\REPORTS\2025-11-20\Departments\`

```
AI_Department_Report_2025-11-20.md
Design_Department_Report_2025-11-20.md
Dev_Department_Report_2025-11-20.md
Finance_Department_Report_2025-11-20.md
HR_Department_Report_2025-11-20.md
LG_Department_Report_2025-11-20.md
Sales_Department_Report_2025-11-20.md
Video_Department_Report_2025-11-20.md
```

### Master Report
**Location**: `C:\Users\Dell\Dropbox\ENTITIES\REPORTS\2025-11-20\`

```
MASTER_REPORT_2025-11-20.md
```

### Supporting Files
```
Entity_Mapping_Summary_2025-11-20.json
Processing_Log_2025-11-20.md
```

---

## Key Features & Standards

### Token-Efficient Entity Format
**Old (v1.0)**: `TST-001, Task_Template, Task-Template-001, AI_Powered_HTML_Parsing`
**New (v2.1)**: `TST-001_AI_Powered_HTML_Parsing`

**60% token reduction** for processing large batches

### Entity Hierarchy
```
Activity → TST (Task) → MLT (Milestone) → PRT (Project)
```

### Confidence Scoring
- **High (>90%)**: Direct match with task manager entries
- **Medium (70-89%)**: Contextual inference, partial match
- **Low (<70%)**: Operational/maintenance work, flag for review

### Operational Classification
For routine work that doesn't map to projects:
- Infrastructure maintenance
- Administrative tasks
- General support activities

---

## Quality Checks

### Pre-Processing Validation
- [ ] All 30 employee "20" folders located
- [ ] File structure verified (daily.md, task.md, etc.)
- [ ] Special cases identified (Finance, Sales, Video)
- [ ] v2.1 prompts loaded and ready

### During Processing
- [ ] Entity mapping applied to all activities
- [ ] Whisper Flow transcripts parsed correctly
- [ ] Time-stamped activities extracted
- [ ] Confidence scores assigned
- [ ] Department-specific patterns recognized

### Post-Processing Validation
- [ ] All 8 department reports generated
- [ ] Master report aggregated successfully
- [ ] Entity mapping statistics calculated
- [ ] No missing employees
- [ ] Cross-references validated

---

## Special Handling Notes

### Finance Department
- Use `report.md` instead of `task.md`
- Expect different content structure
- May contain Ukrainian language
- Focus on tracking metrics vs detailed activities

### Sales Department
- Only `TODO.md` available
- Generate abbreviated reports
- Focus on next-day priorities
- Less granular entity mapping

### Video Department
- Leverage `daily_processed.md` if available
- Use as quality reference for other departments
- Understand preprocessing workflow

### Employees with Dual Folders
Some employees have both direct `/20/` and `/Week_3/20/`:
- Perederii Vladislav (AI)
- Bindiak Dana (LG)
- Burda Anna (LG)
- Shkinder Kseniia (LG)

**Strategy**: Use `Week_3/20` as primary source (more structured)

---

## Execution Steps

1. **Setup**
   - Create output directories
   - Load all v2.1 prompts
   - Initialize processing log

2. **Process AI Department** (2 employees)
   - Apply PMT-033
   - Generate report

3. **Process Design Department** (8 employees)
   - Apply PMT-035
   - Generate report

4. **Process Dev Department** (5 employees)
   - Apply PMT-036
   - Generate report

5. **Process Finance Department** (2 employees)
   - Apply PMT-037 with special handling
   - Generate report

6. **Process HR Department** (3 employees)
   - Apply PMT-038
   - Generate report

7. **Process LG Department** (6 employees)
   - Apply PMT-039
   - Generate report

8. **Process Sales Department** (2 employees)
   - Apply PMT-041 with minimal data
   - Generate report

9. **Process Video Department** (2 employees)
   - Apply PMT-043 with enhanced data
   - Generate report

10. **Aggregate Master Report**
    - Apply PMT-032
    - Generate master report
    - Create entity mapping summary

11. **Final Validation**
    - Run quality checks
    - Verify all outputs
    - Log completion

---

## Expected Outcomes

### Quantitative
- **8 department reports** with full 10-section schema
- **1 master report** aggregating all departments
- **30 employees processed** with activity mapping
- **Entity mappings** for all project-related work
- **Token-efficient format** reducing processing overhead by 60%

### Qualitative
- Clear visibility into November 20 activities
- Project progress tracking via entity mapping
- Cross-department coordination identification
- Next-day planning captured
- Research and improvement needs documented

---

## Risk Mitigation

### Identified Risks
1. **Missing files** - Some employees may not have complete documentation
2. **Inconsistent formatting** - Daily logs may vary in structure
3. **Entity mapping ambiguity** - Some activities may be hard to classify
4. **Language barriers** - Finance may include Ukrainian content

### Mitigation Strategies
1. Flag missing files, process available data
2. Use flexible parsing with pattern matching
3. Use confidence scoring, flag low-confidence mappings
4. Use language detection, translate if needed

---

## Future Improvements

### For Next Processing Cycle
1. **Standardize Sales documentation** - Request full daily logs
2. **Adopt Video's preprocessing** - Implement for all departments
3. **Automate entity mapping** - Build ML model for classification
4. **Create department templates** - Standardize file structure
5. **Integrate with TASK_MANAGERS** - Bidirectional sync

---

## Success Criteria

**This plan is successful if**:
- ✅ All 30 employees processed without errors
- ✅ 8 department reports generated with complete 10-section schema
- ✅ 1 master report providing executive summary
- ✅ Entity mappings applied with >70% confidence on average
- ✅ Processing completed within reasonable timeframe
- ✅ Outputs saved to ENTITIES/REPORTS/2025-11-20/

---

**Status**: Complete ✅
**Completion Date**: November 21, 2025 04:30
**All Reports Generated**: 9 reports (8 department + 1 master)
**All Employees Processed**: 30/30 ✅
