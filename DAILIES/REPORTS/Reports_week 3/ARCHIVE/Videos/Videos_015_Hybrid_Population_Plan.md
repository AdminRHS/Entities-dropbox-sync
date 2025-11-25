# Videos_015 Hybrid System Population Plan

**Source:** Videos_015.md - VS Code AI Features
**Date:** 2025-11-17
**Purpose:** Populate LIBRARIES and TASK_MANAGERS with extracted entities from video processing

---

## 📋 OVERVIEW

This document outlines how to integrate the extracted data from Videos_015 into the hybrid LIBRARIES ↔ TASK_MANAGERS system following the entity filling workflow.

**Entities to Populate:**
- ✅ Tools (4 created: TOOL-108, TOOL-109, TOOL-110, TOOL-111)
- ⏳ Actions (3 to add: Install, Configure, Generate)
- ⏳ Objects (5 to add: MCP Server, Command Lists, Project Instructions, Chat Modes, Code Completions)
- ⏳ Workflows (4 to create: WF-DEV-005 through WF-DEV-008)
- ⏳ Cross-References (Tool ↔ Task ↔ Workflow linkages)

---

## 1. ACTIONS TO ADD TO LIBRARIES

### Actions Extraction from Video Workflows

| Action (Verb) | Process (Gerund) | Result (Past) | Source Workflow | Department |
|---------------|------------------|---------------|-----------------|------------|
| **install** | installing | installed | WF-DEV-005 (Install MCP Server) | DEV |
| **configure** | configuring | configured | WF-DEV-006 (Configure Allow Lists) | DEV |
| **generate** | generating | generated | WF-DEV-007 (Generate Instructions) | DEV / AI |

### JSON Entries for actions.json

Add these entries to `C:\Users\victo\Dropbox\ENTITIES\LIBRARIES\actions.json`:

```json
{
  "Actions": "install",
  "Processes": "installing",
  "Results": "installed",
  "Departments": "DEV",
  "Professions": "Developer"
},
{
  "Actions": "configure",
  "Processes": "configuring",
  "Results": "configured",
  "Departments": "DEV",
  "Professions": "Developer"
},
{
  "Actions": "generate",
  "Processes": "generating",
  "Results": "generated",
  "Departments": "DEV, AI",
  "Professions": "Developer, AI Engineer"
}
```

**Note:** Check if these actions already exist before adding.

---

## 2. OBJECTS TO ADD TO LIBRARIES

### Objects Extraction from Video Workflows

| Object | Category | Description | Used In |
|--------|----------|-------------|---------|
| **MCP Server** | Software / Extension | Model Context Protocol server for AI agent integration | Task-Template-059, WF-DEV-005 |
| **Command Allow List** | Configuration | List of auto-approved terminal commands | Task-Template-060, WF-DEV-006 |
| **Command Deny List** | Configuration | List of blocked terminal commands | Task-Template-060, WF-DEV-006 |
| **Project Instructions** | Documentation | Auto-generated context file for AI (.github/copilot-instructions.md) | Task-Template-061, WF-DEV-007 |
| **Chat Mode** | Configuration | Custom AI agent behavior definition | Referenced in TOOL-109 |
| **Code Completions** | Feature | Ghost text code suggestions | TOOL-110 feature |
| **Agent Mode** | Feature | Autonomous multi-step development mode | TOOL-110 feature |

### JSON Entries for objects.json

Add these entries to `C:\Users\victo\Dropbox\ENTITIES\LIBRARIES\objects.json`:

```json
{
  "Objects": "MCP Server",
  "Category": "Software Extension",
  "Description": "Model Context Protocol server that extends AI agent capabilities to external services",
  "Tools": ["TOOL-108", "TOOL-111"],
  "Departments": "DEV, AI",
  "Professions": "Developer, AI Engineer"
},
{
  "Objects": "Command Allow List",
  "Category": "Configuration",
  "Description": "List of terminal commands that AI agent can execute automatically without approval",
  "Tools": ["TOOL-110", "TOOL-111"],
  "Departments": "DEV",
  "Professions": "Developer"
},
{
  "Objects": "Project Instructions",
  "Category": "Documentation",
  "Description": "Auto-generated context file containing project architecture, conventions, and workflows for AI understanding",
  "Tools": ["TOOL-110"],
  "Departments": "All",
  "Professions": "Developer"
},
{
  "Objects": "Chat Mode",
  "Category": "Configuration",
  "Description": "Custom behavioral configuration for AI agent specialized workflows (e.g., Beast Mode, DBA Mode)",
  "Tools": ["TOOL-109", "TOOL-110"],
  "Departments": "AI, DEV",
  "Professions": "AI Engineer, Developer"
}
```

---

## 3. WORKFLOWS TO CREATE

### Workflow Entity Files

Create workflow JSON files in `C:\Users\victo\Dropbox\ENTITIES\TASK_MANAGERS\Workflows\`:

#### WF-DEV-005: Install MCP Server

**File:** `Workflows/WF-DEV-005_Install_MCP_Server.json`

```json
{
  "entity_type": "TASK_MANAGERS",
  "sub_entity": "Workflow",
  "workflow_id": "WF-DEV-005",
  "workflow_name": "Discover and Install an MCP Server",
  "version": "1.0",
  "created_date": "2025-11-17",
  "metadata": {
    "description": "Install Model Context Protocol server to extend GitHub Copilot Agent Mode with external service integration",
    "department": "DEV",
    "complexity": "Low",
    "estimated_duration": "2-3 minutes",
    "objective": "To extend the capabilities of GitHub Copilot's Agent Mode by adding tools for external services like GitHub",
    "discovery_source": "Videos_015.md - Section 4, Workflow 1"
  },
  "taxonomy": {
    "action": "install",
    "object": "MCP Server",
    "tools_used": ["TOOL-111", "TOOL-110", "TOOL-108"],
    "professions": ["Developer", "AI Engineer"],
    "departments": ["DEV", "AI"]
  },
  "steps": [
    {"step_number": 1, "step_id": "STEP-DEV-059-01", "step_template": "Navigate to Extensions Tab"},
    {"step_number": 2, "step_id": "STEP-DEV-059-02", "step_template": "Select MCP Servers Section"},
    {"step_number": 3, "step_id": "STEP-DEV-059-03", "step_template": "Browse MCP Marketplace"},
    {"step_number": 4, "step_id": "STEP-DEV-059-04", "step_template": "Select MCP Server"},
    {"step_number": 5, "step_id": "STEP-DEV-059-05", "step_template": "Click Install in Browser"},
    {"step_number": 6, "step_id": "STEP-DEV-059-06", "step_template": "Open in VS Code"},
    {"step_number": 7, "step_id": "STEP-DEV-059-07", "step_template": "Confirm Installation"},
    {"step_number": 8, "step_id": "STEP-DEV-059-08", "step_template": "Start MCP Server"},
    {"step_number": 9, "step_id": "STEP-DEV-059-09", "step_template": "Authenticate External Service"},
    {"step_number": 10, "step_id": "STEP-DEV-059-10", "step_template": "Verify Tools Available"}
  ],
  "inputs": [
    "VS Code with GitHub Copilot installed",
    "Internet connection",
    "External service account (e.g., GitHub, Notion)"
  ],
  "outputs": [
    "MCP server installed and running",
    "External service authenticated",
    "New tools available in Copilot Agent Mode"
  ],
  "task_templates_using": ["Task-Template-059"],
  "related_workflows": ["WF-DEV-006", "WF-DEV-007"],
  "tags": ["mcp", "installation", "agent-mode", "vs-code", "copilot"]
}
```

#### WF-DEV-006: Configure Terminal Automation

**File:** `Workflows/WF-DEV-006_Configure_Terminal_Automation.json`

```json
{
  "entity_type": "TASK_MANAGERS",
  "sub_entity": "Workflow",
  "workflow_id": "WF-DEV-006",
  "workflow_name": "Automate Terminal Commands in Agent Mode",
  "version": "1.0",
  "created_date": "2025-11-17",
  "metadata": {
    "description": "Configure GitHub Copilot Agent to automatically run trusted terminal commands without approval prompts",
    "department": "DEV",
    "complexity": "Low",
    "estimated_duration": "1-2 minutes",
    "objective": "Allow Copilot Agent to run specific, trusted terminal commands without requiring user confirmation for each execution",
    "discovery_source": "Videos_015.md - Section 4, Workflow 2"
  },
  "taxonomy": {
    "action": "configure",
    "object": "Command Allow List",
    "tools_used": ["TOOL-111", "TOOL-110"],
    "professions": ["Developer"],
    "departments": ["DEV"]
  },
  "steps": [
    {"step_number": 1, "step_id": "STEP-DEV-060-01", "step_template": "Open VS Code Settings"},
    {"step_number": 2, "step_id": "STEP-DEV-060-02", "step_template": "Navigate to Copilot Experimental Settings"},
    {"step_number": 3, "step_id": "STEP-DEV-060-03", "step_template": "Locate Allow List Setting"},
    {"step_number": 4, "step_id": "STEP-DEV-060-04", "step_template": "Add Trusted Commands"},
    {"step_number": 5, "step_id": "STEP-DEV-060-05", "step_template": "Configure Deny List (Optional)"},
    {"step_number": 6, "step_id": "STEP-DEV-060-06", "step_template": "Test Configuration"}
  ],
  "inputs": [
    "VS Code with GitHub Copilot installed",
    "Understanding of safe vs dangerous commands"
  ],
  "outputs": [
    "Allow list configured with trusted commands",
    "Deny list configured with dangerous commands",
    "Agent executes allowed commands automatically"
  ],
  "task_templates_using": ["Task-Template-060"],
  "related_workflows": ["WF-DEV-005", "WF-DEV-007"],
  "tags": ["configuration", "terminal", "automation", "agent-mode", "productivity"]
}
```

#### WF-DEV-007: Generate Project Instructions

**File:** `Workflows/WF-DEV-007_Generate_Project_Instructions.json`

```json
{
  "entity_type": "TASK_MANAGERS",
  "sub_entity": "Workflow",
  "workflow_id": "WF-DEV-007",
  "workflow_name": "Generate Custom Project Instructions for Copilot",
  "version": "1.0",
  "created_date": "2025-11-17",
  "metadata": {
    "description": "Automatically analyze codebase and create detailed project instructions file for AI agent context",
    "department": "All",
    "complexity": "Low",
    "estimated_duration": "1-5 minutes",
    "objective": "To automatically analyze a codebase and create a detailed instruction file (copilot-instructions.md) to give the Copilot agent project-specific context",
    "discovery_source": "Videos_015.md - Section 4, Workflow 3"
  },
  "taxonomy": {
    "action": "generate",
    "object": "Project Instructions",
    "tools_used": ["TOOL-110", "TOOL-111"],
    "professions": ["Developer", "AI Engineer", "Technical Writer"],
    "departments": ["All"]
  },
  "steps": [
    {"step_number": 1, "step_id": "STEP-DEV-061-01", "step_template": "Open Copilot Chat Panel"},
    {"step_number": 2, "step_id": "STEP-DEV-061-02", "step_template": "Access Settings Menu"},
    {"step_number": 3, "step_id": "STEP-DEV-061-03", "step_template": "Select Generate Instructions"},
    {"step_number": 4, "step_id": "STEP-DEV-061-04", "step_template": "Wait for Analysis"},
    {"step_number": 5, "step_id": "STEP-DEV-061-05", "step_template": "Review Generated File"},
    {"step_number": 6, "step_id": "STEP-DEV-061-06", "step_template": "Customize if Needed (Optional)"},
    {"step_number": 7, "step_id": "STEP-DEV-061-07", "step_template": "Test Enhanced Context"}
  ],
  "inputs": [
    "VS Code with GitHub Copilot installed",
    "Project/codebase open in VS Code",
    "Copilot has read access to project files"
  ],
  "outputs": [
    ".github/copilot-instructions.md file created/updated",
    "File contains project overview and architecture",
    "Agent has enhanced context for development tasks"
  ],
  "task_templates_using": ["Task-Template-061"],
  "related_workflows": ["WF-DEV-005", "WF-DEV-006"],
  "time_savings": {
    "manual_documentation": "1-2 hours",
    "automated_generation": "1-5 minutes",
    "savings_percentage": "90-95%"
  },
  "tags": ["generation", "documentation", "ai-context", "automation", "productivity"]
}
```

#### WF-DEV-008: Build Web App with Agent Mode

**File:** `Workflows/WF-DEV-008_Build_Web_App_Agent_Mode.json`

```json
{
  "entity_type": "TASK_MANAGERS",
  "sub_entity": "Workflow",
  "workflow_id": "WF-DEV-008",
  "workflow_name": "Create a To-Do App with VS Code Agent Mode",
  "version": "1.0",
  "created_date": "2025-11-17",
  "metadata": {
    "description": "Build a functional web application from scratch using AI agent with iterative prompts",
    "department": "DEV",
    "complexity": "Medium",
    "estimated_duration": "10-15 minutes",
    "objective": "To build a functional web application from scratch using an AI agent with iterative prompts",
    "discovery_source": "Videos_015.md - Section 4, Workflow 4"
  },
  "taxonomy": {
    "action": "create",
    "object": "Web Application",
    "tools_used": ["TOOL-110", "TOOL-111", "Python", "Django", "Bootstrap"],
    "professions": ["Developer", "Full-Stack Developer"],
    "departments": ["DEV"]
  },
  "steps": [
    {"step_number": 1, "description": "Open empty folder in VS Code"},
    {"step_number": 2, "description": "Activate Agent Mode in Copilot Chat"},
    {"step_number": 3, "description": "Provide initial high-level prompt: create to-do app with Python/Django"},
    {"step_number": 4, "description": "Follow agent instructions for dependencies and setup"},
    {"step_number": 5, "description": "Allow agent to create project structure, models, views, templates"},
    {"step_number": 6, "description": "Run application to verify initial result"},
    {"step_number": 7, "description": "Provide follow-up prompt to improve UI (add Bootstrap)"},
    {"step_number": 8, "description": "Provide another prompt to add functionality (authentication)"},
    {"step_number": 9, "description": "Test final application"}
  ],
  "inputs": [
    "Empty folder",
    "High-level feature description",
    "VS Code with Copilot Agent Mode"
  ],
  "outputs": [
    "Functional web application with database",
    "User authentication system",
    "Styled UI with Bootstrap"
  ],
  "task_templates_using": [],
  "related_workflows": ["WF-DEV-005", "WF-DEV-007"],
  "tags": ["web-development", "agent-mode", "python", "django", "full-stack", "demo"]
}
```

---

## 4. CROSS-REFERENCES TO UPDATE

### Tool → Workflow Linkages

Update tool JSON files with workflow references:

**TOOL-108 (MCP Servers)**:
```json
"used_in_workflows": ["WF-DEV-005"]
```

**TOOL-109 (awesome-copilot)**:
```json
"used_in_workflows": []
```

**TOOL-110 (GitHub Copilot)**:
```json
"used_in_workflows": ["WF-DEV-005", "WF-DEV-006", "WF-DEV-007", "WF-DEV-008"]
```

**TOOL-111 (VS Code)**:
```json
"used_in_workflows": ["WF-DEV-005", "WF-DEV-006", "WF-DEV-007", "WF-DEV-008"]
```

### Task Template → Workflow Linkages

Already complete in task templates:
- Task-Template-059 → WF-DEV-005 ✅
- Task-Template-060 → WF-DEV-006 ✅
- Task-Template-061 → WF-DEV-007 ✅

### Action → Task Linkages

Add to actions.json entries:
- "install" → Used in Task-Template-059
- "configure" → Used in Task-Template-060
- "generate" → Used in Task-Template-061

---

## 5. EXECUTION CHECKLIST

### Phase 1: LIBRARIES Population

- [ ] **Add 3 actions** to `actions.json`
  - [ ] install
  - [ ] configure
  - [ ] generate

- [ ] **Add 4-7 objects** to `objects.json`
  - [ ] MCP Server
  - [ ] Command Allow List
  - [ ] Project Instructions
  - [ ] Chat Mode

- [ ] **Update 4 tool files** with workflow references
  - [ ] TOOL-108: Add WF-DEV-005 to used_in_workflows
  - [ ] TOOL-110: Add WF-DEV-005, 006, 007, 008 to used_in_workflows
  - [ ] TOOL-111: Add WF-DEV-005, 006, 007, 008 to used_in_workflows

### Phase 2: TASK_MANAGERS Population

- [ ] **Create 4 workflow JSON files**
  - [ ] WF-DEV-005_Install_MCP_Server.json
  - [ ] WF-DEV-006_Configure_Terminal_Automation.json
  - [ ] WF-DEV-007_Generate_Project_Instructions.json
  - [ ] WF-DEV-008_Build_Web_App_Agent_Mode.json

- [ ] **Verify task template linkages**
  - [ ] Task-Template-059 references WF-DEV-005 ✅
  - [ ] Task-Template-060 references WF-DEV-006 ✅
  - [ ] Task-Template-061 references WF-DEV-007 ✅

### Phase 3: Cross-Reference Validation

- [ ] **Validate all bidirectional links**
  - [ ] Tools → Workflows ← Tools
  - [ ] Workflows → Tasks ← Workflows
  - [ ] Actions → Tasks
  - [ ] Objects → Tasks

- [ ] **Test link integrity**
  - [ ] All tool IDs resolve to existing files
  - [ ] All workflow IDs match created files
  - [ ] All step IDs match task template steps

---

## 6. VALIDATION QUERIES

After population, run these validation queries:

### Count Entities
```bash
# Count new actions
grep -c '"install"\|"configure"\|"generate"' actions.json

# Count new objects
grep -c '"MCP Server"\|"Command Allow List"\|"Project Instructions"' objects.json

# Count workflows
ls -1 Workflows/WF-DEV-00*.json | wc -l
```

### Verify Cross-References
```bash
# Check tool files reference workflows
grep -r "WF-DEV-00" Tools/AI_Tools/*.json Tools/Development_Tools/*.json

# Check task templates reference workflows
grep -r "WF-DEV-00" Task_Templates/Task-Template-05*.json Task-Template-06*.json
```

---

## 7. EXPECTED OUTCOMES

### Quantitative
- ✅ 4 tools created
- ⏳ 3 actions added
- ⏳ 4+ objects added
- ⏳ 4 workflows created
- ⏳ 3 task templates linked
- ⏳ 40+ cross-references established

### Qualitative
- Complete traceability: Tool → Workflow → Task → Step
- Taxonomy compliance: All entities follow naming conventions
- Machine-readable: All data in JSON/structured format
- Human-readable: Clear descriptions and documentation

### Business Value
- **Reusability:** Templates and workflows can be used across projects
- **Discoverability:** Entities findable via taxonomy queries
- **Consistency:** Standard processes documented and reusable
- **ROI:** 820+ hours/year potential savings for 5-person team

---

## 8. NEXT STEPS AFTER POPULATION

1. **Test Workflows in Practice**
   - Follow Task-Template-059 to install GitHub MCP Server
   - Follow Task-Template-060 to configure allow list
   - Follow Task-Template-061 to generate ENTITIES project instructions

2. **Expand Taxonomy**
   - Create additional step templates as standalone files
   - Add more objects as discovered in practice
   - Document edge cases and variations

3. **Share with Team**
   - Distribute workflow files as process guides
   - Train team on taxonomy system
   - Collect feedback for improvements

---

## 📧 METADATA

**Created:** 2025-11-17
**Source:** Videos_015.md processing
**Template:** Hybrid System Population following Task_Manager_Entity_Filling_Prompt.md
**Status:** Ready for execution
**Estimated Time:** 1-2 hours for complete population
**Priority:** HIGH (enables systematic knowledge management)

---

*End of Hybrid Population Plan*
