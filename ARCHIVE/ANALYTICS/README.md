# ANALYTICS Entity Documentation

**Entity Type:** ANALYTICS  
**Domain:** Operational Analytics  
**Purpose:** Track and analyze project execution, task performance, milestone completion, and step-level analytics  
**Created:** November 17, 2025  
**Last Updated:** November 17, 2025

---

## đź“‹ Overview

The ANALYTICS entity domain provides infrastructure for tracking and analyzing operational data including projects, milestones, tasks, and steps. This entity was created by moving analytics-related folders from TASK_MANAGERS to provide dedicated infrastructure for performance tracking, completion metrics, and operational insights.

---

## đź—‚ď¸Ź Sub-Entities

### 1. Projects
**Purpose:** Project instances and execution tracking

**Location:** ANALYTICS/Projects/

**Key Attributes:**
- Project instances with execution data
- Project logs and completion reports
- References to milestones (stored centrally in Milestones/)

**Migration Note:** Moved from TASK_MANAGERS/Projects/ on 2025-11-17

**Note:** Milestone files are stored centrally in `ANALYTICS/Milestones/`, not nested within project folders.

---

### 2. Milestone_Templates
**Purpose:** Template definitions for project milestones

**Location:** ANALYTICS/Milestone_Templates/

**Key Attributes:**
- Milestone structure templates
- Milestone definition standards

**Migration Note:** Moved from TASK_MANAGERS/Milestone_Templates/ on 2025-11-17

---

### 3. Tasks
**Purpose:** Task instances and execution tracking

**Location:** ANALYTICS/Tasks/

**Key Attributes:**
- Task execution instances
- Task completion data

**Migration Note:** Moved from TASK_MANAGERS/Tasks/ on 2025-11-17

---

### 4. Task_Templates
**Purpose:** Template definitions for tasks

**Location:** ANALYTICS/Task_Templates/

**Key Attributes:**
- Task structure templates
- Task definition standards
- Department-specific task templates

**Migration Note:** Moved from TASK_MANAGERS/Task_Templates/ on 2025-11-17

---

### 5. Steps
**Purpose:** Step instances and execution tracking

**Location:** ANALYTICS/Steps/

**Key Attributes:**
- Step execution instances
- Step completion data

**Migration Note:** Moved from TASK_MANAGERS/Steps/ on 2025-11-17

---

### 6. Step_Templates
**Purpose:** Template definitions for steps

**Location:** ANALYTICS/Step_Templates/

**Key Attributes:**
- Step structure templates
- Step definition standards
- Department-specific step templates

**Migration Note:** Moved from TASK_MANAGERS/Step_Templates/ on 2025-11-17

---

## đź“Š Analytics Capabilities

The ANALYTICS entity enables:

- **Project Analytics:** Track project completion rates, timeline adherence, milestone achievement
- **Task Analytics:** Monitor task execution, completion times, department performance
- **Step Analytics:** Analyze step-level execution patterns and efficiency
- **Performance Metrics:** Generate reports on team velocity, productivity, and capacity utilization
- **Trend Analysis:** Identify patterns in project execution and task completion

---

## đź”— Related Entities

- **TASK_MANAGERS:** Contains workflow definitions, guides, and prompts (templates remain in TASK_MANAGERS)
- **LIBRARIES:** Provides taxonomy and standards referenced by analytics data
- **DEPARTMENTS:** Department-specific analytics and reports

---

## đź“ť Migration History

**2025-11-17:** Created ANALYTICS entity by moving analytics infrastructure from TASK_MANAGERS:
- Projects folder
- Milestone_Templates folder
- Tasks folder
- Task_Templates folder
- Steps folder
- Step_Templates folder

---

## đźŽŻ Usage

Analytics data is automatically populated when:
- Projects are created and executed
- Tasks are assigned and completed
- Steps are executed within tasks
- Milestones are achieved

All analytics data maintains references to original templates and definitions in TASK_MANAGERS for consistency.

---

## 📈 Attendance Report Extractor

**Purpose:** Generate a daily attendance snapshot for Remote Helpers employees and store it in the `ANALYTICS` entity for further reporting and analysis.

**Data Source:** The extractor pulls yesterday's attendance data from the CRM-S API endpoint  
`https://crm-s.com/api/v1/employees-attendance-yesterday?global_company_name=Remote%20Helpers`  
(see the Remote Helpers integration documentation for details).

**Output Format:**  
- Primary output is a CSV file stored in `C:\Users\Dell\Dropbox\ENTITIES\ANALYTICS`.  
- File naming pattern: `ANALYTICS_Employees_Attendance_Remote_Helpers_YYYY_MM_DD.csv`.  
- Columns include: `employee_id`, `discord_user_id`, `attendance_records`, `attendance_status`, `first_check_in`, `last_check_out`.  
- When no attendance data is present for an employee, `attendance_status` is set to `"no_records"` and time fields are left blank.

**Execution Mode:**  
- Designed for **manual daily runs** via Python (one-off or ad-hoc analytics).  
- Can also be wired into Windows Task Scheduler via a small helper script in `ENTITIES/Scripts/` to run automatically once per day.

**Script Location:**  
- Core extractor: `ENTITIES/ANALYTICS/EMPLOYEES_Attendance_Remote_Helpers_Extractor.py`  
- Automation hook (scheduler-friendly wrapper): `ENTITIES/Scripts/Run_Attendance_Report.ps1` (see that script for configuration details).
