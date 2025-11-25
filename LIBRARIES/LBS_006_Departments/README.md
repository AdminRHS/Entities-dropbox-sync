# Departments Library

**Entity Type:** LIBRARIES  
**Sub-Entity:** Departments  
**Domain:** Organizational Structure  
**Purpose:** Department definitions with IDs, codes, and full names  
**Created:** November 25, 2025  
**Last Updated:** November 25, 2025

---

## 📋 Overview

The Departments library contains a comprehensive list of all departments in the ecosystem with their unique identifiers, codes, full names, and descriptions. This library serves as the authoritative reference for department information across all entities.

---

## 🔍 Definition

**Departments** are organizational units that group related professions, responsibilities, and workflows. Each department has:

- **ID**: Unique numeric identifier
- **Code**: Short uppercase code (e.g., "AI", "DEV", "HR")
- **Name**: Short department name
- **Full Name**: Complete department name
- **Description**: Primary function and responsibilities
- **Color**: RGB color code for UI representation
- **Status**: Active/inactive flag

---

## 📐 Structure

### Master File: `departments.json`

```json
{
  "version": "1.0",
  "source": "ENTITIES/LIBRARIES/DEPARTMENTS",
  "created_date": "2025-11-25",
  "total_departments": 10,
  "data": [
    {
      "id": 1,
      "code": "AI",
      "name": "Artificial Intelligence",
      "full_name": "Artificial Intelligence Department",
      "description": "AI operations, prompt engineering, automation, LLM integration",
      "color": "rgb(61, 183, 124)",
      "is_active": true
    }
  ]
}
```

---

## 📊 Departments List

| ID | Code | Name | Full Name |
|----|------|------|-----------|
| 1 | AI | Artificial Intelligence | Artificial Intelligence Department |
| 2 | DESIGN | Designers | Graphic Design Department |
| 3 | DGN | Designers | Graphic Design Department (alternative code) |
| 4 | DEV | Developers | Software Development Department |
| 5 | FIN | Finance | Finance Department |
| 6 | HR | Human Resources | Human Resources Department |
| 7 | LG | Lead Generation | Lead Generation Department |
| 8 | SALES | Sales | Sales Department |
| 9 | VIDEO | Video Editors | Video Production Department |
| 10 | SMM | Social Media Management | Social Media Management Department |

---

## 🔗 Relationships

### Departments ↔ Professions
- Departments group related professions
- Each profession belongs to one primary department
- Example: "Backend Developer" profession belongs to "DEV" department

### Departments ↔ Responsibilities
- Responsibilities are assigned to departments
- Department-specific responsibilities are stored in `Responsibilities/By_Department/`
- Example: `AI_Responsibilities.json` contains AI department responsibilities

### Departments ↔ Task Templates
- Task templates are assigned to departments
- Department-specific tasks are organized by department code
- Example: Tasks with code "TASK-AI-001" belong to AI department

### Departments ↔ Libraries
- Each department has its own library structure
- Libraries contain department-specific actions, objects, tools, and skills
- Example: `LBS_006_Departments/AI/LIBRARIES/` contains AI-specific resources

---

## 📁 File Structure

```
LBS_006_Departments/
├── departments.json          # Master departments list (this file's data)
├── README.md                 # This file
├── README_SHARED_RESOURCES.md # Shared resources documentation
├── Archive/                  # Historical department data
├── REPORTS/                  # Department reports and analysis
└── RESEARCHES/               # Department-specific research
```

---

## 💡 Usage Examples

### Example 1: Get Department by Code
```python
import json

with open('departments.json', 'r') as f:
    data = json.load(f)
    
department = next((d for d in data['data'] if d['code'] == 'AI'), None)
print(f"Department: {department['full_name']}")
# Output: Department: Artificial Intelligence Department
```

### Example 2: List All Active Departments
```python
active_departments = [d for d in data['data'] if d['is_active']]
for dept in active_departments:
    print(f"{dept['code']}: {dept['full_name']}")
```

### Example 3: Get Department Color for UI
```python
dept_colors = {d['code']: d['color'] for d in data['data']}
print(dept_colors['DESIGN'])
# Output: rgb(151, 71, 255)
```

---

## 🎯 Usage in Framework

### Department Identification
- Use department codes for file naming and organization
- Use department IDs for database references
- Use full names for display purposes

### Cross-Entity References
- Task templates reference departments by code
- Responsibilities are organized by department
- Libraries are structured by department folders

### Reporting and Analytics
- Department codes used in analytics and reporting
- Department IDs used for data aggregation
- Department names used in user-facing reports

---

## 📚 Related Entities

- **Professions** (`../LBS_005_Professions/`) - Professions grouped by departments
- **Responsibilities** (`../Responsibilities/`) - Department-specific responsibilities
- **Task Templates** (`../../TASK_MANAGERS/Task_Templates/`) - Tasks organized by department
- **Analytics** (`../../ANALYTICS/`) - Department-specific analytics and reports

---

## 🔄 Maintenance

### Adding a New Department
1. Add entry to `departments.json` with unique ID
2. Create department folder structure
3. Update related documentation
4. Update cross-references in other entities

### Updating Department Information
1. Modify entry in `departments.json`
2. Update `last_updated` date
3. Document changes in version history

### Deprecating a Department
1. Set `is_active: false` in `departments.json`
2. Archive department folder
3. Update cross-references

---

## 📝 Notes

- **Color Codes**: Colors are RGB format for consistency with UI systems
- **ID Assignment**: IDs are sequential and should not be reused when departments are deprecated
- **Alternative Codes**: 
  - **DGN** is an alternative code for DESIGN department, used in some systems/platforms
  - Both DESIGN and DGN refer to the same Graphic Design Department
- **Removed Departments**: ADMIN, CONTENT_OPS, ECM, MARKETING, MKT, and OPS departments have been removed from the active list

---

## 🎯 Business Value

- **Consistency**: Single source of truth for department information
- **Organization**: Enables structured file and folder organization
- **Reporting**: Supports department-based analytics and reporting
- **Integration**: Facilitates integration with CRM and other systems

---

**Last Updated:** November 25, 2025

