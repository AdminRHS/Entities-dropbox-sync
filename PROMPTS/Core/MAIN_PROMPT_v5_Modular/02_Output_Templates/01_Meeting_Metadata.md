# Template 01: Meeting Metadata

**Purpose:** Capture basic meeting information and metadata
**Library Integration:** None (structural data only)
**Priority:** Always include (every meeting)

---

## Template

```markdown
# Meeting Documentation

## Meeting Metadata

**Meeting ID:** [Auto-generated or manual ID]
**Date:** YYYY-MM-DD
**Time:** HH:MM - HH:MM (Timezone)
**Duration:** XX minutes
**Meeting Type:** [Planning | Review | Standup | All-Hands | Client Call | Technical Discussion | Creative Review | Other]
**Recording Available:** [Yes/No]
**Recording Location:** [URL or file path if available]

### Participants

**Total Attendees:** [Number]

**Internal Team:**
1. [Name] (ID: [Employee ID]) - [Position] - [Department]
2. [Name] (ID: [Employee ID]) - [Position] - [Department]
...

**External Participants:** (if applicable)
1. [Name] - [Company] - [Role]
...

**Absent:** (if notable)
- [Name] - [Reason if mentioned]

### Meeting Context

**Primary Department(s):** [Design | Dev | AI | Video | Sales | LG | HR]
**Related Projects:**
- [Project ID] - [Project Name]
- [Project ID] - [Project Name]

**Meeting Goals/Agenda:**
- [Goal 1]
- [Goal 2]
...

**Previous Meeting:** [Date of last related meeting, if applicable]
**Next Meeting:** [Scheduled follow-up, if mentioned]
```

---

## Recognition Rules

### How to Extract Metadata

**Date & Time:**
- Look for explicit mentions: "Today is November 15th"
- Use current date if not mentioned in transcript
- Extract time if mentioned: "Let's start this 3 PM meeting"

**Duration:**
- Calculate from start/end timestamps if available
- Estimate based on transcript length if not explicit

**Meeting Type:**
- **Planning:** "Let's plan the sprint," "Planning next quarter"
- **Review:** "Review the designs," "Code review meeting"
- **Standup:** "Daily standup," "Quick sync," "What did you do yesterday"
- **All-Hands:** "Team meeting," "Company update," "All hands"
- **Client Call:** Client name mentioned, "Client wants..."
- **Technical Discussion:** Deep technical topics, architecture
- **Creative Review:** Design feedback, creative work review

**Participants:**
- Match names to Employee Directory (00_Core/03_Employee_Directory.md)
- Include Employee ID when identified
- Note confidence level if unsure
- List external participants separately

**Projects:**
- Match to Project Directory (00_Core/04_Project_Directory.md)
- Use project abbreviations (RH, MDL, DGN, l-gn, etc.)
- Multiple projects possible in one meeting

---

## Example 1: Design Team Meeting

```markdown
# Meeting Documentation

## Meeting Metadata

**Meeting ID:** MEET-2025-11-15-DESIGN-001
**Date:** 2025-11-15
**Time:** 14:00 - 15:30 (EET)
**Duration:** 90 minutes
**Meeting Type:** Creative Review
**Recording Available:** Yes
**Recording Location:** /recordings/design-team-2025-11-15.mp3

### Participants

**Total Attendees:** 4

**Internal Team:**
1. Shelep Olha (ID: 86641) - UI/UX Designer - Design
2. Maslo Anastasiia (ID: 86981) - UI/UX Designer - Design
3. Kucherenko Iuliia (ID: 86983) - UI/UX Designer, Graphic Designer - Design
4. Chobotar Yuliia (ID: 72617) - Graphic Designer - Design

**External Participants:** None

**Absent:** None

### Meeting Context

**Primary Department(s):** Design
**Related Projects:**
- PROJ-DGN-001 - Design Services (General)
- PROJ-DGN-DRB-001 - Dribbble Portfolio Management

**Meeting Goals/Agenda:**
- Review client landing page mockups
- Discuss design system updates
- Plan upcoming Dribbble posts

**Previous Meeting:** 2025-11-08 (Weekly design sync)
**Next Meeting:** 2025-11-22 (Scheduled weekly sync)
```

---

## Example 2: Cross-Functional Technical Meeting

```markdown
# Meeting Documentation

## Meeting Metadata

**Meeting ID:** MEET-2025-11-15-TECH-001
**Date:** 2025-11-15
**Time:** 10:00 - 11:15 (EET)
**Duration:** 75 minutes
**Meeting Type:** Technical Discussion
**Recording Available:** Yes
**Recording Location:** /recordings/tech-planning-2025-11-15.mp3

### Participants

**Total Attendees:** 5

**Internal Team:**
1. Klimenko Yaroslav (ID: 86478) - Frontend Developer - Dev
2. Kizilova Olha (ID: 178) - Backend Developer - Dev
3. Zasiadko Matvii (ID: 86981) - Prompt Engineer - AI
4. Shelep Olha (ID: 86641) - UI/UX Designer - Design
5. Artemchuk Nikolay (ID: 37226) - Project Manager - AI

**External Participants:** None

**Absent:**
- Danylenko Liliia - Sick leave

### Meeting Context

**Primary Department(s):** Dev, AI, Design (Cross-functional)
**Related Projects:**
- PROJ-DEV-001 - Development Services
- PROJ-AI-NMP-001 - MAIN_PROMPT v5 Project

**Meeting Goals/Agenda:**
- Plan API integration for new feature
- Discuss UI/UX requirements
- Review timeline and dependencies
- Assign development tasks

**Previous Meeting:** 2025-11-10 (Initial feature discussion)
**Next Meeting:** 2025-11-20 (Development progress check-in)
```

---

## Example 3: LG Campaign Planning

```markdown
# Meeting Documentation

## Meeting Metadata

**Meeting ID:** MEET-2025-11-15-LG-001
**Date:** 2025-11-15
**Time:** 11:00 - 12:00 (EET)
**Duration:** 60 minutes
**Meeting Type:** Planning
**Recording Available:** Yes
**Recording Location:** /recordings/lg-campaign-2025-11-15.mp3

### Participants

**Total Attendees:** 6

**Internal Team:**
1. Hanan Zaheur (ID: 87984) - Lead Generator, Personal Assistant - LG
2. Rybak Nataliia (ID: 88054) - Lead Generator, Content Manager - LG
3. Shkinder Kseniia (ID: 87157) - Lead Generator, Translator - LG
4. Peneva Plamena (ID: 86297) - Lead Generator - LG
5. Burda Anna (ID: 84138) - Lead Generator, Translator - LG
6. Kovalska Anastasiya (ID: 45405) - Sales Manager - Sales

**External Participants:** None

**Absent:** None

### Meeting Context

**Primary Department(s):** LG, Sales
**Related Projects:**
- PROJ-LG-001 - Lead Generation Services

**Meeting Goals/Agenda:**
- Plan LinkedIn campaign for Q4
- Review email outreach results from October
- Discuss data quality standards
- Set campaign targets and KPIs

**Previous Meeting:** 2025-11-08 (Weekly LG sync)
**Next Meeting:** 2025-11-22 (Campaign progress review)
```

---

## Validation Checklist

Before finalizing Meeting Metadata section:

- [ ] **Date** is accurate (YYYY-MM-DD format)
- [ ] **Duration** is reasonable (estimate if not explicit)
- [ ] **Meeting Type** accurately describes the meeting
- [ ] **All participants identified** or flagged as unknown
- [ ] **Employee IDs** match Employee Directory
- [ ] **Departments** are correct
- [ ] **Related projects** match Project Directory (use project IDs)
- [ ] **Meeting goals** captured (if discussed)
- [ ] **Recording location** noted (if available)
- [ ] **Cross-references** are accurate

---

## Notes

- **Always include this section** - Every meeting documentation starts with metadata
- **Accuracy is critical** - Metadata helps with searching and filtering later
- **Flag unknowns** - If participant identity unclear, note "Unknown participant (voice A)" and flag for manual review
- **Multiple departments common** - Cross-functional meetings should list all involved departments
- **Meeting ID format** - Use MEET-YYYY-MM-DD-[DEPT]-[NUMBER] for consistency

---

## Related Templates

**Next:** [02_Executive_Summary.md](02_Executive_Summary.md) - High-level meeting overview
**Related:** [16_Employee_Team_Context.md](16_Employee_Team_Context.md) - Detailed team context

---

**Status:** ✅ Template ready for use
