# Professions Entity Documentation

**Entity Type:** LIBRARIES  
**Sub-Entity:** Professions  
**Domain:** Knowledge Base  
**Purpose:** Primary job roles and profession definitions with department mapping  
**Created:** November 25, 2025  
**Last Updated:** November 25, 2025

---

## 📋 Overview

The Professions sub-entity contains job roles or titles that the system manages. Each profession has its own set of objects, task templates, actions, and tools. Professions are the primary entity in the LLM framework and serve as the foundation for organizing work, assigning tasks, and managing talent.

---

## 🔍 Definition

**Professions** are the primary job roles or titles that the system manages. According to the LLM instruction framework:

- A profession is defined either from a **pre-existing list** or is **introduced by HR or recruiters** when they require a new job role to be added
- Each profession has its own set of:
  - **Objects**: Entities the profession works with
  - **Task Templates**: Tasks the profession performs
  - **Actions**: Actions the profession can perform
  - **Tools**: Instruments the profession uses

**Examples:**
- 3D Designer
- Frontend Developer
- HR Manager
- Lead Generator
- Graphic Designer

---

## 📐 Structure

Each profession in the system includes:

- **Profession Name**: The job title or role name (e.g., "front end developer", "hr manager")
- **Department**: The department the profession belongs to (e.g., "developers", "managers", "designers")
- **Objects**: Objects this profession works with
- **Task Templates**: Task templates this profession performs
- **Actions**: Actions this profession can perform
- **Tools**: Tools this profession uses

---

## 📂 Department Mapping

Professions are organized by departments:

### Managers Department
- hr manager
- lead generator
- project manager
- sales manager
- seo manager
- seo manager tech

### Developers Department
- front end developer
- back end developer
- full stack developer

### Designers Department
- graphic designer
- ui/ux designer
- motion designer
- 3d designer

### Marketers Department
- smm (Social Media Manager)
- content manager
- seo manager

### Videographers Department
- video editor
- animator

### Other Departments
- recruiter
- personal assistant
- ai engineer

---

## 🔗 Relationships

### Professions ↔ Objects
- Each profession defines which objects it works with
- Objects represent entities the profession interacts with
- Example: A 3D Designer works with objects like structures, textures, meshes, renders, environments

### Professions ↔ Task Templates
- Professions perform task templates
- Task templates are assigned to professions
- Example: A Recruiter performs task templates like "Screen Candidates", "Conduct Interviews"

### Professions ↔ Actions
- Professions use specific actions
- Actions define what the profession can do
- Example: A Designer uses actions like "Create", "Design", "Generate"

### Professions ↔ Tools
- Each profession uses specific tools
- Tools are instruments the profession uses to complete tasks
- Example: A Frontend Developer uses tools like VS Code, Git, Figma

### Professions ↔ Departments
- Professions are assigned to departments
- Departments group related professions
- Example: "front end developer" belongs to "developers" department

---

## 📁 File Structure

```
LBS_005_Professions/
└── professions.json    # Complete professions list with department mapping
```

---

## 💡 Examples

### Example 1: Profession with Department
```json
{
  "Professions": "hr manager",
  "Departments": "managers"
}
```

### Example 2: Developer Profession
```json
{
  "Professions": "front end developer",
  "Departments": "developers"
}
```

### Example 3: Designer Profession
```json
{
  "Professions": "graphic designer",
  "Departments": "designers"
}
```

---

## 🎯 Usage in Framework

### LLM Framework Structure
Professions are the primary entity in the LLM framework:

```
Profession
  ├── Objects (what the profession works with)
  ├── Task Templates (tasks the profession performs)
  │     ├── Actions (verbs from task templates)
  │     └── Objects (nouns from task templates)
  └── Tools (instruments the profession uses)
```

### Task Template Assignment
When creating task templates:
1. Assign to a profession
2. Profession defines available objects and actions
3. Profession determines tool requirements
4. Example: "Create Job Posting" task template assigned to "hr manager" profession

### Talent Matching
Professions are used for:
- Matching talents to job requirements
- Assigning tasks to employees
- Defining skill requirements
- Organizing team structure

---

## 📊 Profession Categories

### Technical Professions
- front end developer
- back end developer
- full stack developer
- ai engineer

### Creative Professions
- graphic designer
- ui/ux designer
- motion designer
- 3d designer
- video editor
- animator

### Management Professions
- hr manager
- project manager
- sales manager
- lead generator

### Marketing Professions
- smm
- content manager
- seo manager
- seo manager tech

### Support Professions
- recruiter
- personal assistant

---

## 🔄 Profession Workflow

### Adding a New Profession
1. HR or recruiter identifies need for new profession
2. Profession is added to professions.json
3. Objects are assigned to the profession
4. Task templates are created for the profession
5. Actions and tools are mapped to the profession

### Profession-Object-Task Template Relationship
```
Profession: 3D Designer
  Objects: structures, textures, meshes, renders, environments
  Task Templates:
    - Model structures
    - Texture structures
    - Create renders
  Actions: model, texture, create
  Tools: Blender, Photoshop, ChatGPT
```

---

## 📚 Related Entities

- **Objects** (`../Objects/`) - Objects professions work with
- **Task Templates** (`../../TASK_MANAGERS/Task_Templates/`) - Templates professions perform
- **Actions** (`../Actions/`) - Actions professions use
- **Tools** (`../LBS_003_Tools/`) - Tools professions use
- **Responsibilities** (`../Responsibilities/`) - Responsibilities mapped to professions
- **Skills** (`../../TALENTS/Skills/`) - Skills required by professions
- **TALENTS** (`../../TALENTS/`) - Employees with profession assignments

---

## 🎯 Business Value

- **Role Definition**: Clear definition of job roles and responsibilities
- **Task Organization**: Organizes tasks by profession
- **Talent Matching**: Enables matching employees to job requirements
- **Tool Assignment**: Determines which tools each profession needs
- **Workflow Standardization**: Standardizes work processes by profession

---

**Last Updated:** November 25, 2025

