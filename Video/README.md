# Video Entity (VID)

**Entity ID:** VID
**Purpose:** Video production, shooting coordination, content management
**Department:** Video Production
**Created:** 2025-12-08
**Owner:** Niko_Kar_002

---

## Overview

The Video (VID) entity manages all aspects of video production including:
- Video shooting coordination
- Clothes and appearance preparation
- Google Drive upload management
- Content calendar and scheduling
- Equipment tracking
- Post-production workflow

---

## Folder Structure

```
ENTITIES/Video/
├── README.md (this file)
├── shooting_instructions.md (step-by-step guides)
├── clothes_catalog.md (appearance preparation)
├── equipment_inventory.md (gear tracking)
├── content_calendar.md (scheduling)
├── upload_workflow.md (Google Drive process)
├── professions/
│   ├── videographer.md
│   ├── editor.md
│   ├── director.md
│   └── content_coordinator.md
└── projects/
    └── (individual video projects)
```

---

## Core Functions

### 1. Shooting Coordination
**Purpose:** Manage pre-production and production phases

**Workflow:**
```
Planning
  → Location scouting
  → Equipment preparation
  → Clothes selection
  → Shooting checklist
  → Execution
  → Asset collection
```

**Files:**
- shooting_instructions.md (detailed guides)
- equipment_inventory.md (what to bring)

### 2. Clothes & Appearance
**Purpose:** Prepare visual identity for shoots

**Catalog System:**
- Images of outfit combinations
- Tagged by style/theme
- Linked to shoot types
- Google Drive organization

**File:** clothes_catalog.md

### 3. Upload Management
**Purpose:** Streamline post-shoot asset handling

**Google Drive Integration:**
- Automated folder creation
- Naming conventions
- Asset organization
- Backup verification

**File:** upload_workflow.md

### 4. Content Calendar
**Purpose:** Schedule shoots and releases

**Tracking:**
- Shooting dates
- Editing deadlines
- Publishing schedule
- Platform distribution

**File:** content_calendar.md

---

## Integration Points

### With Personal Agent
- Calendar sync for shooting schedules
- Personal brand (Relax Warsaw) content
- Work-life balance considerations

### With Google Drive
- Upload automation
- Asset storage
- Sharing workflows
- Backup management

### With Automation Agent
- Detect "PROCESS video" or "CREATE video content"
- Generate tasks in Share/
- Track production pipeline

### With Marketing Agent
- Content calendar coordination
- Social media distribution
- Relax Warsaw Instagram

---

## Profession Data

### Location
ENTITIES/Video/professions/

### Roles Defined
1. **Videographer**
   - Shooting execution
   - Camera operation
   - Lighting setup

2. **Editor**
   - Post-production
   - Color grading
   - Audio mixing

3. **Director**
   - Creative vision
   - Shot planning
   - Team coordination

4. **Content Coordinator**
   - Calendar management
   - Asset organization
   - Distribution

---

## Shooting Instructions Template

### Pre-Production Checklist
- [ ] Location confirmed
- [ ] Equipment packed
- [ ] Clothes selected and prepared
- [ ] Shot list created
- [ ] Weather/conditions checked
- [ ] Travel/parking planned

### Production Checklist
- [ ] Arrive early for setup
- [ ] Test equipment
- [ ] Frame and light shots
- [ ] Execute shot list
- [ ] Review footage
- [ ] Pack equipment securely

### Post-Production Checklist
- [ ] Upload footage to Google Drive
- [ ] Back up to local storage
- [ ] Organize in project folders
- [ ] Log in content_calendar.md
- [ ] Create editing task

---

## Google Drive Structure

```
Video Production/
├── Raw Footage/
│   └── YYYY-MM-DD_project_name/
├── Edited/
│   └── project_name/
│       ├── drafts/
│       └── final/
├── Clothes Catalog/
│   └── outfit_images/
└── Assets/
    ├── music/
    ├── graphics/
    └── b-roll/
```

---

## Clothes Catalog System

### Organization
**Format:** Image + metadata

**Metadata:**
```markdown
### Outfit #001

**Image:** clothes_catalog/outfit_001.jpg
**Style:** Casual professional
**Colors:** Navy, white
**Suitable For:** Interview videos, vlogs
**Season:** All year
**Last Used:** 2025-11-20
**Notes:** Works well on camera, avoid busy patterns
```

**Tags:**
- #casual #professional #business #creative
- #indoor #outdoor
- #warm #cool #neutral

---

## Content Types

### Video Categories
1. **Personal Brand (Relax Warsaw)**
   - Instagram content
   - Lifestyle videos
   - Travel content

2. **Business/Professional**
   - Company updates
   - Training videos
   - Presentations

3. **Educational**
   - Tutorials
   - Explanations
   - Demonstrations

4. **Creative**
   - Short films
   - Experimental
   - Artistic projects

---

## Equipment Inventory

### Camera Equipment
- Camera body
- Lenses (list each)
- Tripod/stabilizer
- Batteries + chargers
- Memory cards

### Lighting
- Key light
- Fill light
- Background light
- Reflectors
- Light stands

### Audio
- Microphones
- Audio recorder
- Windscreen
- Cables

### Accessories
- Cleaning kit
- Gaffer tape
- Extension cords
- Bags/cases

**File:** equipment_inventory.md (detailed tracking)

---

## Workflow Integration

### Automation Detection
```
User says: "PROCESS video shooting for new tutorial"
  ↓
Automation agent detects: PROCESS + video
  ↓
Creates task in Share/
  ↓
Video Agent receives task
  ↓
Generates shooting checklist
  ↓
Updates content_calendar.md
```

### Task Example
```markdown
# Video Shooting Task

**Type:** Tutorial
**Date:** 2025-12-15
**Location:** Home studio

**Pre-Production:**
- [ ] Select outfit (Outfit #003)
- [ ] Prepare equipment
- [ ] Write script
- [ ] Plan shots

**Production:**
- [ ] Execute shooting
- [ ] Review footage

**Post-Production:**
- [ ] Upload to Drive
- [ ] Create editing task
- [ ] Schedule release
```

---

## Implementation Priority

### Day 08 (Current)
- [x] Create VID entity structure
- [ ] Create shooting_instructions.md
- [ ] Create clothes_catalog.md template
- [ ] Create upload_workflow.md

### Week 02
- [ ] Populate equipment_inventory.md
- [ ] Build content_calendar.md
- [ ] Create profession files
- [ ] Test Google Drive integration

### Week 03
- [ ] Implement Video Agent
- [ ] Automate upload workflows
- [ ] Build shooting checklists automation
- [ ] Integrate with calendar

---

## Next Steps

1. Create detailed shooting_instructions.md
2. Set up clothes_catalog.md with existing images
3. Document upload_workflow.md for Google Drive
4. Create equipment_inventory.md
5. Build content_calendar.md
6. Populate profession data files
7. Test automation integration

---

**Entity Status:** Structure created - Content population in progress
**Dependencies:** Google Drive API, Personal Agent calendar, automation-agent
**Priority:** High (active video production needs)
