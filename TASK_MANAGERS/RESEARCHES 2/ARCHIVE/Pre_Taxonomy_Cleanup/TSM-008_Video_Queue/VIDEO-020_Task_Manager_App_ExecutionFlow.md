# Video_020 – Task Manager App Execution Flow

**Source Transcript:** `ENTITIES/TASK_MANAGERS/RESEARCHES/02_TRANSCRIPTIONS/Video_20.md`  
**Video:** *To-Do List App with JavaScript - From Scratch to Functional!* by Codynn (18:56)  
**Processing Date:** 2025-11-22  
**Related Project Template:** `RESEARCHES/Video_Queue/VIDEO-001_ToDo_List_Tutorial_Project_Template.json`  
**Purpose:** Provide a concise, Task-Manager-ready execution map that mirrors the tutorial’s four phases and links them to reusable tasks, steps, and workflows.

---

## Phase Summary

| Phase | Goal | Key Actions | Task Manager References |
|-------|------|-------------|-------------------------|
| 1. DOM Setup | Prepare boilerplate + capture DOM handles | `document.getElementById` for input/buttons/list | `MIL-VIDEO-001-001`, Step Template: `Select Task Manager DOM Elements` |
| 2. Add Task | Implement `addTask()` + event listener | create `li`, template literals, append, clear input | `MIL-VIDEO-001-002/003`, Task Template: `Implement Task Addition Logic` |
| 3. Delete Task | Event delegation for delete buttons | `taskList.addEventListener('click', deleteTask)` | `MIL-VIDEO-001-004/005`, Step Template: `Event Delegated Delete Handler` |
| 4. Fetch Tasks | Async fetch + render API tasks | `async function fetchTasks()`, `data.forEach` | `MIL-VIDEO-001-006/007`, Task Template: `Integrate JSONPlaceholder Feed` |

---

## Phase-by-Phase Walkthrough

### Phase 1 – Project Setup & DOM Selection (`[01:16 - 04:24]`)
- Load provided HTML/CSS boilerplate (input, Add Task button, Fetch API button, unordered list).
- Declare four `const` references: `taskInput`, `addTaskButton`, `taskList`, `fetchTasksButton`.
- **Quality checks:** Console log variables to ensure no `null` values; confirm JS file linked.

### Phase 2 – Add Task Functionality (`[04:24 - 09:15]`)
- Define `function addTask()`:
  - `const taskText = taskInput.value;`
  - `const li = document.createElement('li');`
  - `li.innerHTML = `${taskText} <button class='delete'>Delete</button>`;`
  - `taskList.appendChild(li);`
  - `taskInput.value = '';`
- Attach listener: `addTaskButton.addEventListener('click', addTask);`
- **Success gates:** Input clears each time, delete button renders inline, no console errors when clicking.

### Phase 3 – Delete Task (Event Delegation) (`[09:15 - 12:28]`)
- Implement `function deleteTask(e)`:
  - `if (e.target.classList.contains('delete')) { e.target.parentElement.remove(); }`
- Delegate via parent list: `taskList.addEventListener('click', deleteTask);`
- **Key teaching:** Avoid binding listeners on every `li`; parent-level delegation handles dynamic items.

### Phase 4 – Fetch Tasks from API (`[12:28 - 18:21]`)
- Create `async function fetchTasks()` using `try/catch`:
  - `const response = await fetch('https://jsonplaceholder.typicode.com/todos?_limit=5');`
  - `const data = await response.json();`
  - `data.forEach(task => { /* build li, append */ });`
  - `catch(error) { console.error('An error occurred...', error); }`
- Bind listener: `fetchTasksButton.addEventListener('click', fetchTasks);`
- **Verification:** Delete handler still works for API items; network errors logged gracefully.

---

## Task / Step Template Mapping

| ID | Candidate Template | Notes |
|----|--------------------|-------|
| TSK-VID-020-01 | Develop Task Manager DOM Scaffold | Action: Develop, Object: Task Manager DOM Scaffold, Dept: DEV |
| TSK-VID-020-02 | Implement Task Addition Logic | Includes template literal + UX clearing step |
| TSK-VID-020-03 | Implement Event Delegated Delete Handler | Highlights `.classList.contains` guard |
| TSK-VID-020-04 | Integrate JSONPlaceholder Task Feed | Async fetch + data iteration |
| STEP-VID-020-01 | Bind Add Task Event Listener | Reusable across Task Manager builds |
| STEP-VID-020-02 | Render API Task Row | Accepts `{title}` input, appends `li` with delete button |
| STEP-VID-020-03 | Clear Input After Submission | UX hygiene step, ensures chain readiness |
| STEP-VID-020-04 | Log Fetch Errors with Context | Encourages consistent error messaging |

---

## Workflow Alignment

- **Workflow YAML candidate:** `WF-VID-020-ToDo-App` capturing sequential phases, dependencies, and success criteria.
- **Project Template usage:** Reuse `VIDEO-001` template; add alias metadata (`video_aliases: ["Video_020"]`) and notes about Codynn compiler environment.
- **Automation hooks:** Stage 4 lends itself to `n8n`/Zapier tasks for data fetch + DOM update simulation; log as future enhancement.

---

## QA & Extension Hooks

- **Validation Checklist:**
  - [ ] Console logs show four DOM elements (Phase 1).
  - [ ] Add/Delete works for manual tasks (Phase 2-3).
  - [ ] Delete still works for API tasks (Phase 4).
  - [ ] Errors captured in console with context string.
- **Beginner Extensions:**
  - Persist to `localStorage`.
  - Add task status toggles.
  - Introduce simple filters (`All / Active / Completed`).

---

## Cross-References & Next Actions

- `Research_Reports/Video_20.md` – full schema report.
- `Video_Queue_Tracker.md` – add completion note once Task Manager execution is published.
- `TASK_MANAGERS/FILES.md` – mention new execution flow under `RESEARCHES/Video_Queue`.
- Future: integrate with lead-gen Task Manager UI research (queue item #1) to showcase advanced UI flows built atop this foundation.

---

**Maintainer:** AI Research Automation Pod (taxonomy@remotehelpers)  
**Version:** 1.0 • **Last Updated:** 2025-11-22

