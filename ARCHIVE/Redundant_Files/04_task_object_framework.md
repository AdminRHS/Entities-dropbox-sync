# Task + Object Framework

## Overview
This document provides comprehensive guidance on the Action + Object + Context task framework used throughout Remote Helpers for consistent task definition and management.

---

## Task Template Structure

### Basic Format
```
ACTION + OBJECT + CONTEXT
```

**Example**: "Create daily report for HR department"
- **Action**: Create
- **Object**: daily report
- **Context**: for HR department

---

## Complete Task Template (JSON)

```json
{
  "task_id": "",
  "task_name": "",
  "description": "",
  "format": "ACTION + OBJECT + CONTEXT",
  "action": "",
  "object": "",
  "context": "",
  "owner": {
    "name": "",
    "department": "",
    "profession": ""
  },
  "priority": "critical|high|medium|low",
  "timeline": {
    "estimated_duration": "",
    "due_date": "",
    "start_date": ""
  },
  "dependencies": [],
  "status": "not_started|in_progress|blocked|completed",
  "related_project": "",
  "tools_required": [],
  "success_criteria": [],
  "complexity": "beginner|intermediate|advanced|expert",
  "steps": [
    {
      "step_number": 1,
      "name": "",
      "tool": "",
      "responsibility": "",
      "placement": "",
      "duration": "",
      "dependencies": [],
      "success_criteria": "",
      "troubleshooting": ""
    }
  ],
  "checklist": [
    {
      "item": "",
      "guide": "",
      "tools": [],
      "format": "",
      "placement": ""
    }
  ],
  "raci": {
    "responsible": "",
    "accountable": "",
    "consulted": [],
    "informed": []
  },
  "metadata": {
    "created_date": "",
    "last_modified": "",
    "version": "1.0",
    "tags": []
  }
}
```

---

## Standard Actions Library

### Action Forms
Each action has three forms:
1. **Action Form** - Base verb (used in task definition)
2. **Process Form** - Present continuous (used for status updates)
3. **Result Form** - Past participle (used for completion)

### Common Actions

| Action | Process Form | Result Form | Departments |
|--------|--------------|-------------|-------------|
| access | accessing | accessed | All |
| analyze | analyzing | analyzed | All |
| archive | archiving | archived | HR, Admin |
| audit | auditing | audited | Dev, Finance |
| adjust | adjusting | adjusted | All |
| back up | backing up | backed up | Dev, Admin |
| build | building | built | Dev, Design |
| check | checking | checked | All |
| create | creating | created | All |
| debug | debugging | debugged | Dev |
| deploy | deploying | deployed | Dev |
| design | designing | designed | Design |
| develop | developing | developed | Dev |
| document | documenting | documented | All |
| edit | editing | edited | All |
| implement | implementing | implemented | Dev, All |
| integrate | integrating | integrated | Dev |
| maintain | maintaining | maintained | Dev, Admin |
| monitor | monitoring | monitored | All |
| optimize | optimizing | optimized | Dev, Marketing |
| review | reviewing | reviewed | All |
| test | testing | tested | Dev, QA |
| update | updating | updated | All |
| verify | verifying | verified | All, QA |

---

## Standard Objects Library

### By Department/Profession

#### HR/Management Objects
- **candidates** - Types: needed, applied, found, follow-up
- **communications** - Types: first connection, update, follow-up, feedback, faq, onboarding
- **contracts** - Types: employees, presale, content creator, clients agreements
- **databases** - Types: candidates, employees, presale
- **interviews** - Types: video, project
- **negotiations** - Types: salary, contract term, benefit
- **reports** - Types: daily, monthly, employee, department, task
- **salaries** - Types: expected, proposed, start
- **vacancies** - Types: open, closed, suspended, planned
- **channels** - Types: job site, social network, messenger
- **instructions** - Types: onboarding, job posting, crm, communication, video adding
- **scripts** - Types: interview, outreach, offer, onboarding, message
- **employees** - Types: employee, presale, project
- **events** - Types: holidays, birthdays, competitions, team buildings
- **faqs** - Types: candidates, employees, before project, after project
- **feedbacks** - Types: management, candidates, employees, project
- **meetings** - Types: department, team, project, one-on-one
- **onboarding** - Types: company, department, project
- **performance** - Types: personal performance
- **videos** - Types: video interview, re-record, greetings

#### Development Objects
- **databases** - Types: sql, nosql, graph, time-series
- **servers** - Types: dedicated, virtual, cloud, file
- **apis** - Types: internal, external, public, private, partner
- **containers** - Types: docker, kubernetes, virtual machine, cluster
- **microservices** - Types: authentication, logging, billing, notification
- **logs** - Types: system, security, application, audit
- **transactions** - Types: financial, service, batch, real-time
- **sessions** - Types: user, system, persistent, temporary
- **cache** - Types: memory, disk, web, database
- **threads** - Types: worker, ui, background, main
- **requests** - Types: synchronous, asynchronous, idempotent, non-idempotent
- **responses** - Types: synchronous, asynchronous, cached, dynamic
- **configurations** - Types: system, user, network, security
- **dependencies** - Types: direct, transitive, development, production
- **backups** - Types: full, incremental, differential, mirror
- **modules** - Types: utility, feature, core
- **queries** - Types: select, update, insert
- **endpoints** - Types: REST, SOAP, GraphQL
- **forms** - Types: login, registration, data entry
- **routes** - Types: API, resource, redirect
- **schemas** - Types: database, validation, XML
- **templates** - Types: HTML, email, report
- **stylesheets** - Types: CSS, SCSS, LESS
- **widgets** - Types: UI, dashboard, embeddable
- **hooks** - Types: lifecycle, event, utility
- **middleware** - Types: authentication, logging, caching
- **payloads** - Types: JSON, XML, binary

#### Marketing/SMM Objects
- **ads** - Types: search, video, google, paid search, banner, social media, native, contextual
- **collaborations** - Types: cross-industry, brand-artist, competitive, charity, influencer
- **communications** - Types: client correspondence, influencer engagements, support queries
- **metrics** - Types: awareness, engagement, perception, experience, acquisition, conversion
- **posts** - Types: video, image, text, carousel
- **profiles** - Types: business, creator
- **stories** - Types: photo, video
- **strategies** - Types: posting, promotional, conversion, engagement
- **visuals** - Types: images, video, infographic, gif, animation
- **content plan** - Types: posting, promotional, conversion, engagement
- **media** - Types: images, video, infographic, gif, animation

#### Design Objects
- **banners** - Types: web, social media, email
- **headers** - Types: social media, website
- **icons** - Types: outline, filled, flat, dimensional, emoji, hand-drawn
- **illustrations** - Types: flat, isometric, vector, character
- **infographics** - Types: statistical, informational, process
- **logos** - Types: wordmark, lettermark, pictorial, abstract, combination, emblem
- **presentations** - Types: informative, persuasive, demonstrative
- **brandbooks** - Types: corporate, product, visual identity guideline
- **fonts** - Types: web, display, custom
- **business cards** - Types: personal contact, social media, QR code
- **thumbnails** - Types: promo, interview, tutorial
- **mockups** - Types: website, app, advertising
- **email templates** - Types: promotional, newsletter, feedback
- **characters** - Types: mascot, user avatar, instructional, storytelling, iconic
- **portraits** - Types: digital portrait

#### Lead Generation Objects
- **accounts** - Types: new, in work, sold, banned, problematic, free
- **industries** - Types: sector, industry, market
- **customer persona** - Types: business, individual
- **search queries** - Types: google, linkedin
- **profiles** - Types: company, lead
- **contacts** - Types: valid, active, inactive, empty
- **companies** - Types: lead, interested, client, updated, not relevant
- **leads** - Types: cold, new, active, client, updated, not relevant
- **connections** - Types: personalized, relevant, old, received
- **messages** - Types: connection, cold, follow up, presentation, sms
- **emails** - Types: cold, follow up, presentation
- **promotions** - Types: informational, trial-based, discounts, interactive
- **needs** - Types: immediate, long-term, position, skill, replacement, project
- **communications** - Types: first connection, basic correspondence, event, follow up, presentation
- **events** - Types: scheduled, held, transferred, follow up, ignored
- **feedbacks** - Types: direct, in-app, live chat, product/service, price
- **reports** - Types: daily, monthly, by countries, by industries, by manager, by event
- **databases** - Types: operational, analytical

#### Video Objects
- **audios** - Types: audio mixing, sound effect, voiceover
- **background** - Types: virtual set, green screen, thematic
- **color** - Types: color grading, color correction, color enhancement
- **description** - Types: metadata, SEO, narrative
- **effects** - Types: visual, transition, sound
- **footage** - Types: raw, stock, edited
- **frame** - Types: composition, static, dynamic
- **graphics** - Types: motion, static, animated
- **intro** - Types: teaser, thematic, narrative
- **music** - Types: background, theme, incidental
- **noise** - Types: background, noise reduction, ambient
- **outro** - Types: closing, credit, call-to-action
- **script** - Types: shooting, dialogue, storyboard
- **storyboard** - Types: pre-production, animatic, presentation
- **subtitles** - Types: translated, closed caption, descriptive
- **template** - Types: video, title, transition
- **titles** - Types: opening, lower-thirds, credit
- **transitions** - Types: cut, fade, wipe
- **video breakdown** - Types: scene, shot, sequence
- **video hook** - Types: opening, narrative, promotional
- **video take** - Types: master, alternative, b-roll
- **videos** - Types: promotional, documentary, tutorial
- **voiceover** - Types: instructional, narrative, promotional
- **characters** - Types: main, secondary, background
- **backgrounds** - Types: digital, hand-drawn, interactive
- **textures** - Types: natural, synthetic, environmental
- **layers** - Types: foreground, middle ground, background
- **props** - Types: animated, static, interactive
- **animations** - Types: 2d, 3d, stop motion
- **frames** - Types: key, in-between, extreme
- **keyframes** - Types: start, end, breakdown
- **storyboards** - Types: initial, final, presentation
- **timelines** - Types: scene, character, effects
- **palettes** - Types: character, background, detail
- **motions** - Types: linear, complex, guided

#### Project Management Objects
- **dashboards** - Types: overview, employees, milestones, tasks, Gantt chart
- **deadlines** - Types: project, milestone, task
- **edits** - Types: scope, schedule, resource, budget, quality, risk management
- **feedbacks** - Types: client, team, stakeholder
- **goals** - Types: quality, cost, time, scope, customer satisfaction
- **meetings** - Types: kick-off, status update, planning, review, stakeholder, retrospective
- **milestones** - Types: initiation, planning, development, implementation, closure
- **projects** - Types: software development, website development, system integration, data migration
- **strategies** - Types: agile, scrum, waterfall, devops, kanban
- **tasks** - Types: initiation, planning, development, implementation, closure
- **teams** - Types: functional, project, operational, management
- **timelines** - Types: milestone, project, workflow
- **workflows** - Types: sequential, parallel

---

## Step Template Structure

Steps provide detailed procedures for completing tasks.

### Step Format
```json
{
  "step_number": 1,
  "name": "Step name describing what to do",
  "tool": "Tool or platform to use",
  "responsibility": "Who performs this step",
  "placement": "Where this happens (system/location)",
  "duration": "Estimated time",
  "dependencies": ["Previous step numbers"],
  "success_criteria": "How to know it's complete",
  "troubleshooting": "Common issues and solutions"
}
```

### Example Step
```json
{
  "step_number": 1,
  "name": "Read Prompt Log file for today's date",
  "tool": "File Explorer or Finder",
  "responsibility": "Report Compiler",
  "placement": "Local file system",
  "duration": "2 minutes",
  "dependencies": [],
  "success_criteria": "Prompt Log file is open and readable",
  "troubleshooting": "If file not found, check date format and folder path"
}
```

---

## Checklist Template Structure

Checklists provide verification items for task completion.

### Checklist Format
```json
{
  "item": "What to check or verify",
  "guide": "How to check it",
  "tools": ["Tools needed for verification"],
  "format": "Expected format or standard",
  "placement": "Where to find/verify this"
}
```

### Example Checklist
```json
{
  "item": "All participants identified",
  "guide": "Match all mentioned names against Employee Directory",
  "tools": ["Employee Directory", "Transcript"],
  "format": "Full Name (ID: xxxxx) - Role | Department | Confidence: Level",
  "placement": "Meeting Metadata section"
}
```

---

## RACI Matrix

### RACI Definitions
- **R - Responsible**: The person(s) who do the work to complete the task
- **A - Accountable**: The person ultimately answerable for completion (only ONE person)
- **C - Consulted**: People whose opinions are sought (two-way communication)
- **I - Informed**: People kept up-to-date on progress (one-way communication)

### RACI Format
```json
{
  "responsible": "Person doing the work",
  "accountable": "Person ultimately answerable",
  "consulted": ["Person 1", "Person 2"],
  "informed": ["Person 1", "Person 2", "Person 3"]
}
```

### Example RACI
```json
{
  "responsible": "Artemchuk Nikolay (AI Department)",
  "accountable": "Nealova Evgeniya (HR Manager)",
  "consulted": ["Rekonvald Viktoriia (HR)", "Department Leads"],
  "informed": ["All Department Members", "Management Team"]
}
```

---

## Status Values

- **not_started**: Task has been defined but work hasn't begun
- **in_progress**: Work is actively happening
- **blocked**: Work cannot continue due to dependency or issue
- **completed**: Task is finished and verified

---

## Priority Values

- **critical**: Must be done immediately, blocks other work
- **high**: Important and time-sensitive
- **medium**: Standard priority
- **low**: Nice to have, can be deferred

---

## Complexity Values

- **beginner**: Can be completed by someone with basic training
- **intermediate**: Requires some experience and familiarity
- **advanced**: Requires significant expertise
- **expert**: Requires specialized knowledge or mastery

---

## Integration into Daily Report Prompts

### Task Extraction
When extracting tasks from transcripts:

1. **Identify the action** - What verb describes the work?
2. **Identify the object** - What is being worked on?
3. **Add context** - For whom, why, where?
4. **Assign owner** - Match to Employee Directory
5. **Determine priority** - Based on urgency and impact
6. **Set status** - Current state of the task
7. **Assess complexity** - Level of difficulty
8. **Define success criteria** - How to know it's done
9. **List tools required** - What's needed to complete it
10. **Assign RACI** - Who's responsible, accountable, consulted, informed

### Example Task Extraction

**From transcript**: "Olya needs to create the employee onboarding documentation by next week, and she should work with Zhenya on the requirements."

**Extracted task**:
```json
{
  "task_name": "Create employee onboarding documentation",
  "format": "ACTION + OBJECT + CONTEXT",
  "action": "Create",
  "object": "employee onboarding documentation",
  "context": "for new employee registration system",
  "owner": {
    "name": "Shelep Olha",
    "department": "Design",
    "profession": "UI/UX designer"
  },
  "priority": "high",
  "timeline": {
    "due_date": "Next week",
    "estimated_duration": "3-5 days"
  },
  "status": "not_started",
  "related_project": "LibDev / Talents Microservice",
  "complexity": "intermediate",
  "raci": {
    "responsible": "Shelep Olha (Design)",
    "accountable": "Nealova Evgeniya (HR Manager)",
    "consulted": ["Zhenya"],
    "informed": ["Development Team"]
  }
}
```

---

## Quality Standards

### Task Definition Quality Checks
- All tasks use Action + Object + Context format
- Owner is matched to Employee Directory with full details
- Priority level is assigned based on urgency and impact
- Status is current and accurate
- Complexity level matches required skill level
- Success criteria are clear and measurable
- RACI is complete with all roles assigned
- Related project is matched to Project Directory

### Step Definition Quality Checks
- Steps are numbered sequentially
- Each step has clear name, tool, and responsibility
- Dependencies are identified
- Success criteria are defined
- Duration estimates are provided

### Checklist Quality Checks
- Items are specific and actionable
- Verification methods are clear
- Required tools are listed
- Expected formats are defined

---

*Last Updated: November 7, 2025*
