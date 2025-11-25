# Phase 4 Context: Deep Research Task Manager + Employee Dashboards

**Phase**: 4 of 6
**Agents**: 4 simultaneous
**Priority**: P0-CRITICAL ⚠️
**Status**: ✅ Ready to Execute (can run in parallel with Phase 3)
**Dependencies**: Phase 3B (video queue system) for integration
**Estimated Complexity**: High

---

## 🎯 Phase Objectives

1. **Create Deep Research Task Template** - Systematic research task execution
2. **Build Employee Dashboards** - HTML dashboards showing personal task queues
3. **Online Academy Gap Analysis** - Identify missing Deep Research courses
4. **Portfolio Diversity Tracker** - Solve "goat problem" (duplicate portfolio items)

---

## ⚡ WHY THIS IS P0-CRITICAL

Per Russian transcript:
- **"первая твоя цель на данный момент... тебе нужно только один task который будет называться deep research"**
- **Portfolio problem**: Designers showing same projects ("goat" example)
- **Need diverse case studies** to increase client conversion
- **Employee engagement**: Manual approval keeps employees in decision-making loop
- **Multi-queue system**: Employees choose work direction (videos, reading, tasks)

---

## 🤖 Agent Assignments

### Agent 4A: Deep Research Task Template Creator
**Focus**: Create comprehensive Deep Research task template
**Working Directory**: `TASK_MANAGERS/TSM-003_Task_Templates/`
**Output**: Task template JSON + integration docs

### Agent 4B: Employee Dashboard Generator
**Focus**: Build HTML dashboards for individual employees
**Working Directory**: `TALENTS/Employees/[Employee_Name]/`
**Output**: Dashboard template + generation script

### Agent 4C: Online Academy Gap Analysis Agent
**Focus**: Analyze ASSETS/OA-Y/ for Deep Research course gaps
**Working Directory**: `ASSETS/`
**Output**: Gap analysis report + needed courses list

### Agent 4D: Portfolio Diversity Tracker Agent
**Focus**: Track designer portfolio diversity, flag duplicates
**Working Directory**: `TALENTS/`
**Output**: Portfolio tracker CSV + diversity scoring

---

## 📋 Agent 4A: Deep Research Task Template

### Task Instructions

#### Create Task Template JSON

**File**: `TASK_MANAGERS/TSM-003_Task_Templates/Task-Template-DeepResearch-001.json`

```json
{
  "entity_type": "Task_Template",
  "entity_id": "TASK-DeepResearch-001",
  "template_name": "CONDUCT_DeepResearch_Topic",
  "template_version": "1.0",
  "created_date": "2025-11-22",
  "category": "Research",
  "department": "All",
  "description": "Execute deep research on a specific topic using AI tools (Perplexity, Gemini, GPT, DeepSeek) or YouTube",
  "estimated_duration_minutes": 60,
  "difficulty": "Medium",
  "steps": [
    {
      "step_id": "DR-001",
      "step_name": "Select Research Topic",
      "description": "Choose topic from backlog or create new topic",
      "prompt_reference": "PROMPTS/DEPARTMENTS/Research/Deep_Research_Topic_Selection.md",
      "deliverable": "Topic ID (RT-XXX) and topic description",
      "manual_approval_required": false
    },
    {
      "step_id": "DR-002",
      "step_name": "Choose Research Tool",
      "description": "Select best tool for research: Perplexity (web search + AI), Gemini (technical depth), GPT (broad analysis), DeepSeek (specialized), or YouTube (video tutorials)",
      "prompt_reference": "PROMPTS/DEPARTMENTS/Research/Tool_Selection_Guide.md",
      "deliverable": "Tool name and rationale",
      "manual_approval_required": true,
      "approval_note": "Employee decides which tool fits their learning style"
    },
    {
      "step_id": "DR-003",
      "step_name": "Execute Research",
      "description": "Run research using chosen tool. For YouTube: find 20 videos. For AI tools: extract key findings.",
      "prompt_reference": "PROMPTS/DEPARTMENTS/Research/Research_Execution_Guidelines.md",
      "deliverable": "Research results (Markdown or JSON)",
      "manual_approval_required": false
    },
    {
      "step_id": "DR-004",
      "step_name": "Add Videos to Queue (if YouTube)",
      "description": "If YouTube research: add all found videos to queue using add_video_to_queue.py script",
      "integration_reference": "TASK_MANAGERS/RESEARCHES/Video_Queue/",
      "script_command": "python TASK_MANAGERS/RESEARCHES/Video_Queue/scripts/add_video_to_queue.py [video_url] [employee_name] [topic] [YouTube] [notes]",
      "deliverable": "Videos added to queue (Queue IDs: VQ-XXX)",
      "manual_approval_required": false,
      "conditional": "Only if research tool is YouTube"
    },
    {
      "step_id": "DR-005",
      "step_name": "Format Research Results",
      "description": "Format findings using standard template",
      "prompt_reference": "PROMPTS/DEPARTMENTS/Research/Research_Results_Formatting.md",
      "deliverable": "Formatted report (TASK_MANAGERS/RESEARCHES/ACTIVE/[DATE]/[TOPIC]_Deep_Research.md)",
      "manual_approval_required": false
    },
    {
      "step_id": "DR-006",
      "step_name": "Generate Analysis Report",
      "description": "Create analysis report with key takeaways and action items",
      "prompt_reference": "PROMPTS/DEPARTMENTS/Research/Analysis_Report_Generation.md",
      "deliverable": "Analysis report (TASK_MANAGERS/RESEARCHES/REPORTS/Deep_Research/[TOPIC]_Analysis_[DATE].md)",
      "manual_approval_required": false
    },
    {
      "step_id": "DR-007",
      "step_name": "Manual Review and Approval",
      "description": "Employee reviews research quality, decides next steps",
      "deliverable": "Approval status and next actions (archive, iterate, or escalate)",
      "manual_approval_required": true,
      "approval_note": "Keeps employee engaged in decision-making (мануально)"
    }
  ],
  "integrations": [
    {
      "entity": "RESEARCHES/Video_Queue",
      "purpose": "Add YouTube research videos to queue",
      "trigger_step": "DR-004"
    },
    {
      "entity": "RESEARCHES",
      "purpose": "Store research results and reports",
      "trigger_step": "DR-005, DR-006"
    },
    {
      "entity": "PROMPTS",
      "purpose": "Reference research prompts throughout workflow",
      "trigger_step": "All steps"
    }
  ],
  "success_criteria": [
    "Research topic clearly defined",
    "Tool selection justified",
    "Results formatted per template",
    "Analysis report generated",
    "Manual approval completed",
    "Files saved to correct locations"
  ],
  "related_templates": [
    "TASK-VideoResearch-001",
    "TASK-GapAnalysis-001",
    "TASK-CompetitorAnalysis-001"
  ]
}
```

**Output Files**:
- `Task-Template-DeepResearch-001.json`
- `Deep_Research_Task_Integration_Guide.md` (how to use template)
- Update `TASK_MANAGERS/Task_Templates_Master_List.csv` with new entry

---

## 📋 Agent 4B: Employee Dashboard Generator

### Task Instructions

#### Create Dashboard Template HTML

**File**: `TALENTS/Employees/Employee_Dashboard_Template.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{EMPLOYEE_NAME}} - Personal Dashboard</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 20px; background: #f5f5f5; }
        .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; border-radius: 10px; margin-bottom: 20px; }
        .header h1 { margin: 0; font-size: 32px; }
        .header p { margin: 5px 0 0 0; opacity: 0.9; }
        .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-bottom: 20px; }
        .stat-card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .stat-card h3 { margin: 0 0 10px 0; color: #666; font-size: 14px; text-transform: uppercase; }
        .stat-card .number { font-size: 36px; font-weight: bold; color: #667eea; }
        .section { background: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .section h2 { margin: 0 0 15px 0; color: #333; border-bottom: 2px solid #667eea; padding-bottom: 10px; }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #eee; }
        th { background: #f8f9fa; font-weight: 600; color: #666; }
        .status-pending { background: #fff3cd; padding: 4px 8px; border-radius: 4px; font-size: 12px; }
        .status-in-progress { background: #d1ecf1; padding: 4px 8px; border-radius: 4px; font-size: 12px; }
        .status-completed { background: #d4edda; padding: 4px 8px; border-radius: 4px; font-size: 12px; }
        .priority-high { color: #d9534f; font-weight: bold; }
        .priority-medium { color: #f0ad4e; }
        .priority-low { color: #5bc0de; }
        .queue-section { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; }
        .queue-card { border: 1px solid #e0e0e0; padding: 15px; border-radius: 6px; cursor: pointer; transition: all 0.3s; }
        .queue-card:hover { box-shadow: 0 4px 8px rgba(0,0,0,0.15); transform: translateY(-2px); }
        .queue-card h4 { margin: 0 0 10px 0; color: #333; }
        .queue-card p { margin: 5px 0; font-size: 14px; color: #666; }
        .action-btn { background: #667eea; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; margin-right: 10px; }
        .action-btn:hover { background: #5568d3; }
    </style>
</head>
<body>
    <div class="header">
        <h1>{{EMPLOYEE_NAME}}</h1>
        <p>{{DEPARTMENT}} Department | Employee ID: {{EMPLOYEE_ID}} | Today: {{DATE}}</p>
    </div>

    <div class="stats">
        <div class="stat-card">
            <h3>Tasks Today</h3>
            <div class="number">{{TASKS_TODAY}}</div>
        </div>
        <div class="stat-card">
            <h3>Videos in Queue</h3>
            <div class="number">{{VIDEOS_IN_QUEUE}}</div>
        </div>
        <div class="stat-card">
            <h3>Completed This Week</h3>
            <div class="number">{{COMPLETED_WEEK}}</div>
        </div>
        <div class="stat-card">
            <h3>Portfolio Diversity</h3>
            <div class="number">{{PORTFOLIO_DIVERSITY}}%</div>
        </div>
    </div>

    <div class="section">
        <h2>📋 My Task Queue</h2>
        <table>
            <thead>
                <tr>
                    <th>Task ID</th>
                    <th>Task Name</th>
                    <th>Type</th>
                    <th>Priority</th>
                    <th>Status</th>
                    <th>Due Date</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody id="task-queue">
                <!-- Populated from DAILIES/[DATE]/task_[EMPLOYEE].md -->
            </tbody>
        </table>
    </div>

    <div class="section">
        <h2>🎥 My Video Research Queue</h2>
        <p>Choose your research direction: <button class="action-btn" onclick="filterVideos('all')">All Topics</button> <button class="action-btn" onclick="filterVideos('design')">Design</button> <button class="action-btn" onclick="filterVideos('development')">Development</button></p>
        <div class="queue-section" id="video-queue">
            <!-- Populated from TASK_MANAGERS/RESEARCHES/Video_Queue/Video_Queue_Master.csv filtered by employee -->
        </div>
    </div>

    <div class="section">
        <h2>📚 Available Research Topics</h2>
        <p>Select a topic for Deep Research:</p>
        <div class="queue-section" id="research-topics">
            <!-- Populated from RESEARCHES/TAXONOMY/Research_Topics_Master.csv -->
        </div>
    </div>

    <div class="section">
        <h2>📊 My Progress This Week</h2>
        <canvas id="progress-chart" width="400" height="200"></canvas>
        <!-- Chart.js visualization of weekly activity -->
    </div>

    <script>
        // JavaScript to populate dashboard from CSV/MD sources
        // Load task data from DAILIES/[DATE]/task_{{EMPLOYEE}}.md
        // Load video queue from RESEARCHES/Video_Queue/Video_Queue_Master.csv (filtered by employee)
        // Load research topics from RESEARCHES/TAXONOMY/
        // Generate progress chart from REPORTS/2025-11-XX/
        // TODO: Implement data loading logic
    </script>
</body>
</html>
```

#### Create Dashboard Generation Script

**File**: `TALENTS/Employees/generate_employee_dashboard.py`

```python
#!/usr/bin/env python3
"""
Generate employee dashboard HTML from ENTITIES data

Usage:
    python generate_employee_dashboard.py [employee_name] [date]

Example:
    python generate_employee_dashboard.py "Niko Kar" "2025-11-22"
"""

import sys
import os
from datetime import datetime
import pandas as pd
from pathlib import Path

def generate_dashboard(employee_name, date):
    # Paths
    base_path = Path("C:/Users/Dell/Dropbox/ENTITIES")
    employee_folder = base_path / "TALENTS" / "Employees" / employee_name.replace(" ", "_")
    template_path = employee_folder.parent / "Employee_Dashboard_Template.html"
    output_path = employee_folder / f"Dashboard_{date}.html"

    # Load template
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    # Get employee data
    employee_data = get_employee_data(employee_name, base_path)

    # Get tasks for today
    tasks_today = get_tasks_today(employee_name, date, base_path)

    # Get video queue for employee
    videos_in_queue = get_video_queue(employee_name, base_path)

    # Get completed tasks this week
    completed_week = get_completed_week(employee_name, date, base_path)

    # Get portfolio diversity score
    portfolio_diversity = get_portfolio_diversity(employee_name, base_path)

    # Replace template variables
    html = template.replace("{{EMPLOYEE_NAME}}", employee_name)
    html = html.replace("{{DEPARTMENT}}", employee_data.get('department', 'Unknown'))
    html = html.replace("{{EMPLOYEE_ID}}", employee_data.get('employee_id', 'N/A'))
    html = html.replace("{{DATE}}", date)
    html = html.replace("{{TASKS_TODAY}}", str(len(tasks_today)))
    html = html.replace("{{VIDEOS_IN_QUEUE}}", str(len(videos_in_queue)))
    html = html.replace("{{COMPLETED_WEEK}}", str(completed_week))
    html = html.replace("{{PORTFOLIO_DIVERSITY}}", str(portfolio_diversity))

    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ Dashboard generated: {output_path}")
    return output_path

def get_employee_data(employee_name, base_path):
    """Load employee data from TALENTS/Employees/[Name]/[Name].json"""
    # TODO: Implement
    return {
        'employee_id': 'EMP-001',
        'department': 'AI'
    }

def get_tasks_today(employee_name, date, base_path):
    """Load tasks from DAILIES/[DATE]/task_[employee].md"""
    # TODO: Implement
    return []

def get_video_queue(employee_name, base_path):
    """Load videos from RESEARCHES/Video_Queue/Video_Queue_Master.csv filtered by employee"""
    # TODO: Implement
    return []

def get_completed_week(employee_name, date, base_path):
    """Count completed tasks from past 7 days of dailies"""
    # TODO: Implement
    return 0

def get_portfolio_diversity(employee_name, base_path):
    """Get portfolio diversity score from Portfolio_Tracker.csv"""
    # TODO: Implement
    return 0

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python generate_employee_dashboard.py [employee_name] [date]")
        print("Example: python generate_employee_dashboard.py 'Niko Kar' '2025-11-22'")
        sys.exit(1)

    employee_name = sys.argv[1]
    date = sys.argv[2] if len(sys.argv) > 2 else datetime.now().strftime('%Y-%m-%d')

    generate_dashboard(employee_name, date)
```

#### Test Dashboard Generation

Generate sample dashboard for Niko Kar:
```bash
python TALENTS/Employees/generate_employee_dashboard.py "Niko Kar" "2025-11-22"
```

Open `TALENTS/Employees/Niko_Kar/Dashboard_2025-11-22.html` in browser to verify.

**Output Files**:
- `TALENTS/Employees/Employee_Dashboard_Template.html`
- `TALENTS/Employees/generate_employee_dashboard.py`
- `TALENTS/Employees/Niko_Kar/Dashboard_2025-11-22.html` (sample)
- `Dashboard_Generation_Guide.md`

---

## 📋 Agent 4C: Online Academy Gap Analysis

### Task Instructions

#### Scan ASSETS/OA-Y/ for Deep Research Courses

**Step 1**: Inventory existing courses
- Scan `ASSETS/OA-Y/` for all courses
- Identify courses tagged "Deep Research" or "Research Methods"
- Extract course metadata: title, topics covered, creation date, file count

**Output**: `Existing_DeepResearch_Courses_Inventory.csv`

#### Step 2: Identify Gaps

Compare existing courses against needed topics:
- Deep Research methodology
- Tool-specific guides (Perplexity, Gemini, GPT, DeepSeek)
- YouTube research best practices
- Video selection criteria
- Analysis report writing
- Research project management

**Output**: `DeepResearch_Course_Gaps_Analysis.md`

#### Step 3: Create Needed Courses List

**File**: `ASSETS/New_Academy/Needed_Courses_DeepResearch.md`

```markdown
# Deep Research Courses Needed for Online Academy

## Critical Gaps (P0 - Create by Monday)

### 1. Deep Research Fundamentals
**Topic**: Introduction to Deep Research methodology
**Duration**: 30 minutes
**Content**:
- What is Deep Research
- When to use Deep Research vs quick search
- Tool selection framework (Perplexity vs Gemini vs GPT vs DeepSeek)
- Research workflow overview

### 2. YouTube Video Research Mastery
**Topic**: How to find and evaluate YouTube videos for research
**Duration**: 45 minutes
**Content**:
- Search query optimization
- Video selection criteria (views, likes, recency, engagement)
- Metadata interpretation
- Building video queues
- Batch processing strategy

### 3. Research Results Formatting
**Topic**: How to format and document research findings
**Duration**: 30 minutes
**Content**:
- Markdown templates
- JSON structure for research data
- Analysis report writing
- Key findings extraction
- Action items generation

## Medium Priority Gaps (P1 - Create this month)

### 4. Tool-Specific Guides
- Perplexity Deep Dive (20 min)
- Gemini for Technical Research (20 min)
- GPT Research Workflows (20 min)
- DeepSeek Specialized Research (20 min)

### 5. Research Project Management
**Duration**: 60 minutes
**Content**:
- Research topic selection
- Time management for research tasks
- Queue management
- Archive and knowledge retention

## Nice to Have (P2)

### 6. Advanced Research Techniques
- Competitor analysis
- Market research
- Trend analysis
- Gap analysis methodology
```

**Output Files**:
- `Existing_DeepResearch_Courses_Inventory.csv`
- `DeepResearch_Course_Gaps_Analysis.md`
- `ASSETS/New_Academy/Needed_Courses_DeepResearch.md`

---

## 📋 Agent 4D: Portfolio Diversity Tracker

### Task Instructions

#### Create Portfolio Tracker CSV

**File**: `TALENTS/Portfolio_Tracker.csv`

```csv
Employee_ID,Employee_Name,Department,Total_Projects,Unique_Projects,Duplicate_Projects,Diversity_Score,Flagged_Duplicates,Last_Updated,Notes
EMP-001,Designer A,Design,15,12,3,80,"Project_Goat (shared with EMP-002, EMP-003)",2025-11-22,Needs more variety in motion graphics
EMP-002,Designer B,Design,12,10,2,83,"Project_Goat (shared with EMP-001, EMP-003)",2025-11-22,Good diversity
EMP-003,Designer C,Design,18,14,4,78,"Project_Goat (shared with EMP-001, EMP-002), Logo_Series",2025-11-22,Too many logo projects
```

**Fields**:
- `Employee_ID`: EMP-XXX
- `Employee_Name`: Full name
- `Department`: Design, Video, Development, etc.
- `Total_Projects`: Count of all portfolio items
- `Unique_Projects`: Count of unique portfolio items (not shared with others)
- `Duplicate_Projects`: Count of projects shown by multiple employees
- `Diversity_Score`: 0-100 (higher = more diverse portfolio)
- `Flagged_Duplicates`: List of duplicate project names + who else shows them
- `Last_Updated`: Date of last scan
- `Notes`: Manual notes about portfolio quality

#### Calculate Diversity Score

```python
def calculate_diversity_score(employee_portfolio):
    """
    Calculate portfolio diversity 0-100 based on:
    - Uniqueness (50% weight): Unique projects / Total projects
    - Variety (30% weight): Count of different project types (logo, web, video, etc.)
    - Recency (20% weight): How many projects from last 3 months
    """
    uniqueness_score = (employee_portfolio['unique_projects'] / max(1, employee_portfolio['total_projects'])) * 50
    variety_score = min(30, len(employee_portfolio['project_types']) * 5)  # 6+ types = max
    recency_score = min(20, employee_portfolio['recent_projects_count'] * 4)  # 5+ recent = max

    total_score = uniqueness_score + variety_score + recency_score
    return round(total_score, 2)
```

#### Scan for Duplicate Projects

Cross-reference all designer portfolios:
- Extract project names from `TALENTS/Employees/[Designer_Name]/Portfolio/`
- Find projects with identical or similar names across employees
- Flag as duplicates (especially the "goat problem")

**Output**: `Portfolio_Duplicates_Report.csv`

#### Generate Recommendations

For each designer with low diversity score (<70):
- Recommend project types to add
- Suggest unique research topics
- Flag duplicate projects to replace

**Output**: `Portfolio_Diversity_Recommendations.md`

**Output Files**:
- `TALENTS/Portfolio_Tracker.csv`
- `TALENTS/Portfolio_Duplicates_Report.csv`
- `TALENTS/Portfolio_Diversity_Recommendations.md`
- `Portfolio_Tracking_Guide.md`

---

## 🔗 Cross-Agent Dependencies

### Agent 4A ← → Agent 4B
**Integration**: Dashboard displays Deep Research tasks
- Agent 4B dashboard references Agent 4A task template
- **Execution**: Can run in parallel

### Agent 4A ← → Agent 4C
**Integration**: Courses teach how to use Deep Research tasks
- Agent 4C identifies needed courses to teach Agent 4A workflow
- **Execution**: Can run in parallel

### Agent 4B ← → Agent 4D
**Integration**: Dashboard shows portfolio diversity score
- Agent 4B displays Agent 4D's diversity scores
- **Execution**: Can run in parallel

**Result**: All 4 agents can execute simultaneously.

---

## 🚦 Phase 4 Exit Criteria

**MUST COMPLETE:**
- [ ] Deep Research task template created and tested
- [ ] Sample employee dashboard generated (Niko Kar)
- [ ] Online Academy gap analysis complete
- [ ] Portfolio diversity tracker implemented
- [ ] All 4 validation checklists reviewed

**METRICS UPDATED:**
- [ ] Task templates: 50+ → 51+ (Deep Research added)
- [ ] Employee dashboards: 0 → 1+ (template + sample)
- [ ] Online Academy courses identified: X → X+6 (gap list)
- [ ] Portfolio duplicates: Unknown → Tracked

**READY FOR NEXT PHASE:**
- [ ] Deep Research tasks can be assigned to employees
- [ ] Dashboards ready for all 32 employees
- [ ] Course creation list ready for Monday
- [ ] Portfolio diversity being monitored

---

**END OF PHASE 4 CONTEXT**

**Priority**: ⚡ P0-CRITICAL - Execute in parallel with Phase 3

**Next**: Proceed to Phase 5 (Master Lists Sync)
