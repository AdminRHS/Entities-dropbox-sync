# Objects Entity Documentation

**Entity Type:** LIBRARIES  
**Sub-Entity:** Objects  
**Domain:** Knowledge Base  
**Purpose:** Business objects that professions work with or manage  
**Created:** November 25, 2025  
**Last Updated:** November 25, 2025  
**Last Synced to `Nov25/Libs 25/Objects`:** November 11, 2025

---

## 📋 Overview

The Objects sub-entity contains plural, lowercase nouns (typically one-word, sometimes two-word) that represent tangible or slightly abstract entities that professions interact with or work on. Objects are the noun portion of task templates following the "verb + object" structure.

---

## 🔍 Definition

**Objects** are entities a profession can work with or on. According to the LLM instruction framework:

- Objects are **plural, concrete nouns** (e.g., structures, textures, meshes)
- Objects are typically **tangible**, but can also represent **slightly abstract ideas**
- Objects are usually **one-word**, but can be **two words** in rare cases
- Objects are **lowercase** in the system
- Objects are the **noun portion** of task templates

**Example:** A 3D Designer might interact with objects like:
- structures
- textures
- meshes
- renders
- environments

---

## 📐 Structure

Each object in the system includes:

- **Name**: The object name (plural, lowercase)
- **Category**: Classification (Documents, Communication, Data, Media, Design Deliverables, etc.)
- **Description**: What the object represents
- **Attributes**: Fields or properties of the object
- **Common Actions**: Actions typically performed on this object
- **Storage Location**: Where objects of this type are stored
- **Related Entities**: Other entities this object relates to
- **Object Types**: Different states or modifiers for the object (e.g., "needed", "applied", "found")

---

## 📂 Categories

Objects are organized into the following categories:

### Documents
- Job Posting
- Client Proposal
- Report
- Contract
- Invoice
- NDA

### Communication
- Email
- Message
- Call
- Meeting
- Notification

### Data
- Lead
- Contact
- Company
- Project
- Task
- Candidate

### Media
- Video CV
- Image
- Design
- Presentation
- Audio

### Design Deliverables
- Mockups
- Logos
- Illustrations
- UI Components
- Brand Assets

---

## 🔗 Relationships

### Objects ↔ Professions
- Each profession has specific objects it works with
- Objects define what entities a profession interacts with
- Example: A Recruiter works with objects like "candidates", "communications", "contracts"

### Objects ↔ Task Templates
- Objects are the noun portion of task templates
- Task templates follow the format: **Action + Object**
- Example: "Create" (action) + "Job Posting" (object) = "Create Job Posting"

### Objects ↔ Actions
- Objects are paired with actions to form task templates
- Each object has common actions that can be performed on it
- Example: "Job Posting" object pairs with actions like "Create", "Update", "Publish"

### Objects ↔ Object Types
- Objects can have different types or states
- Object types represent modifiers or states of the object
- Example: "candidates" object has types: "needed", "applied", "found", "interviewed", "offered", "hired"

---

## 📁 File Structure

```
Objects/
├── object_types.json          # Comprehensive object types by profession
├── objects.json               # Master objects library (in parent folder)
├── Documents.json             # Document-type objects
├── Design_Deliverables.json   # Design-related objects
└── [Category]_Objects.json    # Other category-specific files
```

---

## 🎯 Object Types

Objects can have **types** or **modifiers** that represent different states or variations:

### Example: Candidates Object Types
For the "candidates" object (used by HR/Recruiter profession):
- **needed**: Required positions to fill
- **applied**: Submitted applications
- **found**: Sourced/identified prospects
- **follow-up**: In active communication
- **interviewed**: Completed interview stage
- **offered**: Extended job offer
- **hired**: Successfully onboarded

### Example: Communications Object Types
For the "communications" object:
- **first connection**: Initial outreach
- **update**: Status or progress communication
- **follow-up**: Subsequent touchpoint
- **feedback**: Interview or application feedback

### Example: Contracts Object Types
For the "contracts" object:
- **employee contracts**: Employment agreements
- **presale contract**: Pre-sales agreements
- **NDA**: Non-disclosure agreements

---

## 💡 Examples

### Example 1: Document Object
```json
{
  "object_id": "OBJ-DOC-001",
  "name": "Job Posting",
  "category": "Documents",
  "description": "A published announcement for an open position",
  "attributes": [
    "title",
    "description",
    "requirements",
    "skills",
    "experience_level",
    "compensation",
    "location"
  ],
  "common_actions": ["Create", "Update", "Publish", "Archive", "Review"],
  "storage_location": "Entities/JOBS/Job_Postings/",
  "related_entities": ["JOBS", "TALENTS", "LIBRARIES/Professions"]
}
```

### Example 2: Object with Types
```json
{
  "profession": "HR/Recruiter",
  "department": "managers",
  "object_types": [
    {
      "object": "candidates",
      "types": ["needed", "applied", "found", "follow-up", "interviewed", "offered", "hired"],
      "descriptions": {
        "needed": "Required positions to fill",
        "applied": "Submitted applications",
        "found": "Sourced/identified prospects"
      }
    }
  ]
}
```

---

## 🎯 Usage in Framework

### Task Template Creation
When creating a task template:
1. Select an object from Objects library
2. Pair with appropriate action
3. Format as "Action + Object"
4. Example: "Create" + "Job Posting" = "Create Job Posting"

### Object Type Usage
Object types help track states:
- Use object types to filter and organize objects
- Object types enable workflow state management
- Example: Filter "candidates" by type "interviewed" to see all interviewed candidates

### Profession-Object Mapping
Each profession has specific objects:
- Objects define what a profession works with
- Objects are assigned to professions in the system
- Example: 3D Designer works with: structures, textures, meshes, renders, environments

---

## 📊 Object Types by Profession

The `object_types.json` file contains detailed object type classifications organized by profession:

### Professions Covered:
- **HR/Recruiter**: candidates, communications, contracts, interviews
- **Lead Generator**: accounts, companies, leads, messages
- **Developer**: APIs, databases, modules, code
- **Designer**: mockups, logos, illustrations, UI Components
- **Video Editor**: videos, assets
- **Marketer**: ad campaigns, content, keywords, analytics, SEO Objects, social media
- **AI Engineer**: models, prompts, training data

---

## 📚 Related Entities

- **Actions** (`../Actions/`) - Actions performed on objects
- **Task Templates** (`../../TASK_MANAGERS/Task_Templates/`) - Templates using objects
- **Professions** (`../LBS_005_Professions/`) - Professions that work with objects
- **Tools** (`../LBS_003_Tools/`) - Tools used to work with objects
- **Skills** (`../LBS_004_Skills/`) - Skills involving objects

---

## 🔄 Object in Task Template Structure

Objects are central to the task template structure:

```
Task Template = Action + Object

Examples:
- "Create" (action) + "Job Posting" (object)
- "Model" (action) + "Structures" (object)
- "Texture" (action) + "Meshes" (object)
- "Generate" (action) + "Leads" (object)
```

---

**Last Updated:** November 25, 2025
