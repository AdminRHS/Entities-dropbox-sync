"""
Package Week 3 Analysis - Complete Consolidation
Consolidates all extraction, delegation, and analysis work into Week_3_Analysis folder
"""

import shutil
from pathlib import Path
from datetime import datetime

# Paths
BASE_DIR = Path(r"C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS")
SOURCE_WEEK4 = BASE_DIR / "Week_4"
OUTPUT_DIR = BASE_DIR / "Week_3_Analysis"

print("=" * 70)
print("WEEK 3 ANALYSIS - COMPLETE PACKAGING")
print("=" * 70)

# Create main analysis folder
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
print(f"\n[OK] Created: {OUTPUT_DIR}")

# Structure
structure = {
    "01_Source_Data": {
        "Executive_Strategic": SOURCE_WEEK4 / "Executive_Strategic",
        "Operational_Tasks_Nov20": SOURCE_WEEK4 / "Tasks_2025_11_20.csv",
        "Consolidated_Tasks": SOURCE_WEEK4 / "ALL_TASKS_CONSOLIDATED_WITH_NOV20.csv",
    },
    "02_Delegation_Mapping": {
        "All_Files": SOURCE_WEEK4 / "Delegation",
    },
    "03_Scripts": {
        "extract_executive_notes.py": BASE_DIR / "extract_executive_notes.py",
        "extract_weekly_tasks.py": BASE_DIR / "extract_weekly_tasks.py",
        "extract_2025_11_20_tasks.py": BASE_DIR / "extract_2025_11_20_tasks.py",
        "create_delegation_mapping_v2.py": BASE_DIR / "create_delegation_mapping_v2.py",
        "merge_nov20_tasks.py": BASE_DIR / "merge_nov20_tasks.py",
    }
}

print("\nPackaging structure:")

# Copy files and folders
for folder_name, sources in structure.items():
    folder_path = OUTPUT_DIR / folder_name
    folder_path.mkdir(exist_ok=True)
    print(f"\n[{folder_name}]")

    for item_name, source in sources.items():
        if isinstance(source, Path):
            if source.exists():
                if source.is_dir():
                    # Copy entire directory
                    dest = folder_path / source.name
                    if dest.exists():
                        shutil.rmtree(dest)
                    shutil.copytree(source, dest)
                    print(f"  [OK] Copied folder: {source.name}/")
                elif source.is_file():
                    # Copy file
                    dest = folder_path / source.name
                    shutil.copy2(source, dest)
                    print(f"  [OK] Copied file: {source.name}")
            else:
                print(f"  [!] Not found: {source}")

# Create master README
readme_content = f"""# Week 3 Analysis - Complete Package

**Package Created:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Source Period:** Week 3 (2025-11-17 to 2025-11-21)
**Analysis Date:** 2025-11-24

---

## 📋 Contents

### 01_Source_Data/
**Extracted task data from Week 3 daily reports**

- **Executive_Strategic/** - 461 strategic tasks from Executive Notes Summary
  - Executive_All_Tasks.csv (master file)
  - Executive_Projects.csv (17 projects)
  - Executive_Milestones.csv (11 milestones)
  - Executive_Tasks.csv (433 tasks)
  - Executive_Connections.csv (224 relationships)
  - Executive_Categories.csv
  - Executive_Departments.csv
  - Executive_Hierarchy.json
  - README.md

- **Tasks_2025_11_20.csv** - 40 operational tasks from Nov 20 department reports
  - Extracted from narrative markdown reports
  - Department breakdown: Design (10), Development (7), AI (5), HR (5), LG (5), Finance (3), Video (3), Sales (2)

- **ALL_TASKS_CONSOLIDATED_WITH_NOV20.csv** - 530 total tasks
  - Combined executive strategic (490) + operational (40)
  - Complete Week 3 task inventory

---

### 02_Delegation_Mapping/
**Comprehensive delegation system mapping 501 tasks to Task Manager templates**

**Files:**
1. **Task_Template_Mapping.csv** (501 rows)
   - Task-to-template matching with confidence scores
   - ID-proximity matching (TSK-066 → TST-066)
   - Department reclassification (233 tasks corrected)
   - Required skills, tools, estimated duration

2. **Team_Assignment_Matrix.csv**
   - RACI-based assignments (Responsible, Accountable, Consulted, Informed)
   - Role recommendations from templates
   - Department routing with reclassification

3. **Department_Workload_Analysis.csv**
   - Total tasks and estimated hours per department
   - Priority distribution (Critical/High counts)
   - Resource status (Balanced/High Load/Overloaded)
   - Recommendations for capacity management

4. **Workflow_Clustering.csv**
   - Project-based task grouping
   - Sequential vs parallel workflows
   - Milestone dependencies
   - Execution phases

5. **Assignment_Priority_Queue.csv**
   - Priority-sorted task queue (501 tasks)
   - Quick wins flagged (<1 hour tasks)
   - Business impact classification
   - Blocking dependencies identified

6. **README.md**
   - Complete delegation workflow documentation
   - Reclassification examples
   - Usage instructions

---

### 03_Scripts/
**Python scripts used for extraction and analysis**

- **extract_executive_notes.py** - Extract tasks from Executive Notes Summary
- **extract_weekly_tasks.py** - Extract tasks from Week 3 daily reports (CSV/markdown)
- **extract_2025_11_20_tasks.py** - Extract Nov 20 operational tasks
- **create_delegation_mapping_v2.py** - Delegation mapping system v2.0
- **merge_nov20_tasks.py** - Merge Nov 20 tasks with consolidated data

---

## 📊 Key Metrics

### Task Extraction
- **Executive Strategic**: 461 tasks (17 projects, 11 milestones, 433 tasks)
- **Operational (Nov 20)**: 40 tasks
- **Total Tasks**: 501 tasks mapped for delegation

### Delegation Mapping
- **Total Tasks Analyzed**: 501
- **Department Reclassifications**: 233 (46.5%)
  - Client tasks → Sales/Finance
  - Employee tasks → HR
  - Automation tasks → AI
- **Template Match Rate**: 91% (High/Medium confidence)
- **ID-Proximity Matches**: 20+ exact matches (TSK-066 ↔ TST-066)

### Department Workload (Final)
| Department | Tasks | Hours | Status |
|------------|-------|-------|--------|
| AI | 228 | 19.1h | ✅ Balanced |
| Sales | 38 | 112.7h | ⚠️ High Load |
| Design | 62 | 32.3h | ✅ Balanced |
| HR | 55 | 88.0h | ⚠️ High Load |
| Development | 38 | 50.5h | ✅ Balanced |
| Finance | 22 | 62.0h | ✅ Balanced |
| Video | 26 | 60.2h | ✅ Balanced |
| Lead Gen | 21 | 53.0h | ✅ Balanced |
| SMM | 11 | 54.0h | ✅ Balanced |

---

## 🔍 Key Features Implemented

### 1. Department Reclassification
- **Client Priority Rule**: All "client"/"customer" tasks → Sales (or Finance if payment-related)
- **HR Priority Rule**: "employee", "retention", "candidate" → HR
- **Multi-word Keyword Boost**: More specific phrases get higher weight

### 2. ID-Proximity Matching
- Exact ID match: TSK-066 ↔ TST-066 (+50 points)
- Nearby IDs (±5): TSK-066 ↔ TST-064 (+15 points)
- Helps when task IDs align with template numbering

### 3. LIBRARIES Integration
- Matched tasks to LIBRARIES/Responsibilities
- Action + Object pattern matching
- Profession recommendations

### 4. Template Matching Scoring
- Department match: +40 points
- Category/Action match: +30 points
- ID-proximity: +50 points (exact)
- Tool/Technology match: +20 points
- Text similarity: +10 points

---

## 🚀 Usage

### For Week 4 Task Distribution:

1. **Review Priority Queue**
   ```
   02_Delegation_Mapping/Assignment_Priority_Queue.csv
   ```
   Start from Queue_Position 1, tackle quick wins first

2. **Assign to Teams**
   ```
   02_Delegation_Mapping/Team_Assignment_Matrix.csv
   ```
   Use Reclassified_Department and Primary_Role for assignments

3. **Check Workload**
   ```
   02_Delegation_Mapping/Department_Workload_Analysis.csv
   ```
   Monitor High Load departments (Sales: 112.7h, HR: 88.0h)

4. **Plan Workflows**
   ```
   02_Delegation_Mapping/Workflow_Clustering.csv
   ```
   Group sequential tasks, identify parallel work

---

## ⚠️ Important Notes

### High Load Departments
- **Sales** (38 tasks, 112.7 hours): Consider prioritization or additional resources
- **HR** (55 tasks, 88.0 hours): Monitor workload distribution

### Data Sources
- **Week 3 Reports**: `ENTITIES/DAILIES/REPORTS/Reports_week 3/`
  - 2025-11-19, 2025-11-20, 2025-11-21
  - Executive_Notes_Summary
  - Department Reports (markdown format)

### Template Coverage
- 83 templates loaded (some had JSON errors)
- 91% of tasks matched to existing templates
- 9% flagged for custom template creation

---

## 📝 Change Log

**2025-11-24:**
- ✅ Extracted 461 executive strategic tasks
- ✅ Extracted 40 operational tasks (2025-11-20)
- ✅ Created delegation mapping v2.0 with department reclassification
- ✅ Added ID-proximity matching
- ✅ Integrated LIBRARIES/Responsibilities
- ✅ Generated 501-task delegation system
- ✅ Packaged complete Week 3 Analysis

---

## 🔗 Related Directories

- **Source**: `C:\\Users\\Dell\\Dropbox\\ENTITIES\\DAILIES\\REPORTS\\Reports_week 3`
- **Output**: `C:\\Users\\Dell\\Dropbox\\ENTITIES\\DAILIES\\REPORTS\\Week_4`
- **Templates**: `C:\\Users\\Dell\\Dropbox\\ENTITIES\\TASK_MANAGERS`
- **Libraries**: `C:\\Users\\Dell\\Dropbox\\ENTITIES\\LIBRARIES`

---

**Package Complete!**
All Week 3 analysis, extraction, and delegation mapping consolidated in this folder.
"""

readme_path = OUTPUT_DIR / "README.md"
with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(readme_content)

print(f"\n[OK] Created master README: {readme_path.name}")

# Create summary stats file
stats_content = f"""Week 3 Analysis - Summary Statistics
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

TASK EXTRACTION
===============
Executive Strategic Tasks: 461
  - Projects (PRT): 17
  - Milestones (MLT): 11
  - Tasks (TSK/ARC/FIX): 433
  - Connections: 224

Operational Tasks (Nov 20): 40
  - Design: 10
  - Development: 7
  - AI: 5
  - HR: 5
  - Lead Gen: 5
  - Finance: 3
  - Video: 3
  - Sales: 2

Total Tasks: 501 (mapped for delegation)

DELEGATION MAPPING
==================
Total Tasks Analyzed: 501
Department Reclassifications: 233 (46.5%)
Template Match Rate: 91% (High/Medium confidence)
Templates Loaded: 83

DEPARTMENT WORKLOAD
===================
AI:            228 tasks,  19.1 hours  [Balanced]
Sales:          38 tasks, 112.7 hours  [High Load] ⚠️
Design:         62 tasks,  32.3 hours  [Balanced]
HR:             55 tasks,  88.0 hours  [High Load] ⚠️
Development:    38 tasks,  50.5 hours  [Balanced]
Finance:        22 tasks,  62.0 hours  [Balanced]
Video:          26 tasks,  60.2 hours  [Balanced]
Lead Gen:       21 tasks,  53.0 hours  [Balanced]
SMM:            11 tasks,  54.0 hours  [Balanced]

KEY IMPROVEMENTS
================
[OK] Department reclassification (client → Sales, employee → HR)
[OK] ID-proximity matching (TSK-066 <-> TST-066)
[OK] LIBRARIES/Responsibilities integration
[OK] RACI-based team assignments
[OK] Workload analysis with capacity warnings
[OK] Priority queue for systematic task distribution
"""

stats_path = OUTPUT_DIR / "SUMMARY_STATISTICS.txt"
with open(stats_path, 'w', encoding='utf-8') as f:
    f.write(stats_content)

print(f"[OK] Created statistics: {stats_path.name}")

print("\n" + "=" * 70)
print("PACKAGING COMPLETE!")
print("=" * 70)
print(f"\nPackage Location: {OUTPUT_DIR}")
print("\nContents:")
print("  [DIR] 01_Source_Data/")
print("  [DIR] 02_Delegation_Mapping/")
print("  [DIR] 03_Scripts/")
print("  [FILE] README.md")
print("  [FILE] SUMMARY_STATISTICS.txt")
print("\nAll Week 3 analysis consolidated and ready for distribution!")
