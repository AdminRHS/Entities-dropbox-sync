#!/usr/bin/env python3
"""Assign AI Tools to specific departments based on their purpose and use case."""

import csv
from pathlib import Path
from collections import defaultdict

TOOLS_ROOT = Path(r"C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\LBS_003_Tools")
MASTER_CSV = TOOLS_ROOT / "Tools_Master_Inventory.csv"
BY_DEPT_CSV = TOOLS_ROOT / "Tools_By_Department.csv"

# Department Assignment Map
DEPARTMENT_ASSIGNMENTS = {
    # AI/LLM Tools - Core AI work
    "TOL-026": "AI, Dev, Design, Marketing, All",  # Claude - Universal AI
    "TOL-025": "AI, Dev, Marketing",  # ChatGPT
    "TOL-058": "AI, Dev, Marketing, LG",  # Gemini
    "TOL-072": "AI, Marketing",  # Grok
    "TOL-112": "AI, Marketing, LG",  # Perplexity

    # Development & Code Tools
    "TOL-037": "Dev",  # Cursor - AI code editor
    "TOL-062": "Dev",  # GitHub Copilot
    "TOL-010": "Dev",  # Archon - AI coding assistant enhancement
    "TOL-014": "Dev",  # Awesome Copilot
    "TOL-027": "Dev, AI",  # Claude Desktop App
    "TOL-030": "Dev",  # CodeRabbit - Code review
    "TOL-093": "Dev, AI",  # MCP Builder
    "TOL-087": "Dev, Design",  # Lovable.dev - AI app builder
    "TOL-039": "Dev, Design",  # DeepSite - AI website generation
    "TOL-022": "Dev, Design",  # Bubble.io - No-code platform
    "TOL-057": "Dev, Design, Marketing",  # Gamma.app - Presentations
    "TOL-060": "Dev, AI",  # Genspark.ai

    # Multi-Agent & Orchestration
    "TOL-035": "Dev, AI",  # CrewAI
    "TOL-082": "Dev, AI",  # LangGraph
    "TOL-081": "Dev, AI",  # Langfuse - Observability
    "TOL-021": "Dev, AI",  # Browserbase
    "TOL-009": "Dev, AI",  # Arcade.ai

    # Knowledge & RAG Tools
    "TOL-044": "Dev, AI",  # Docling - Document extraction
    "TOL-034": "Dev, AI, LG",  # Crawl4AI - Web scraping
    "TOL-059": "Dev, AI",  # Gemini File Search API
    "TOL-071": "Dev, AI",  # Graphiti - Knowledge graphs
    "TOL-028": "Dev, AI, Marketing",  # Claude Projects

    # AI Video Tools - Video Editors
    "TOL-080": "Video",  # Kling
    "TOL-075": "Video",  # Hedra
    "TOL-113": "Video",  # Pedra
    "TOL-070": "Video, Marketing",  # Google Veo 3.1
    "TOL-076": "Video, Marketing",  # HeyGen
    "TOL-078": "Video, Marketing",  # InVideo AI
    "TOL-024": "Video",  # C dans
    "TOL-073": "Video",  # Hailo
    "TOL-104": "Video, Marketing",  # Otter.ai - Transcription
    "TOL-089": "Video, Marketing",  # Maestra.ai - Transcription
    "TOL-124": "Video, Marketing",  # Riverside.fm
    "TOL-134": "Video, Marketing",  # Sora
    "TOL-086": "All",  # Loom - Universal video messaging

    # AI Image Generation - Design
    "TOL-002": "Design",  # Adobe Firefly
    "TOL-031": "Design, Video",  # ComfyUI
    "TOL-054": "Design",  # Flux
    "TOL-055": "Design, Marketing",  # Flux Kontext
    "TOL-083": "Design",  # Leonardo.ai
    "TOL-097": "Design",  # Midjourney
    "TOL-096": "Design",  # Microsoft Designer
    "TOL-105": "Design",  # Pexels AI
    "TOL-116": "Design",  # Recraft V3
    "TOL-128": "Design, Marketing",  # Runway
    "TOL-063": "Design, Video, Marketing",  # GLIF - Workflow automation

    # Voice/Audio AI
    "TOL-049": "Video, Marketing",  # ElevenLabs
    "TOL-101": "Video, Marketing",  # NotebookLM

    # Project Management & Productivity
    "TOL-100": "All",  # Notion AI - Universal
    "TOL-090": "Dev",  # Manus.im
    "TOL-033": "All",  # Cove.ai

    # Marketing & Content Tools
    "TOL-092": "Marketing",  # Mayple - Marketing platform
    "TOL-102": "Marketing, Sales",  # Odius - Marketing automation
    "TOL-149": "Marketing",  # v0.dev - UI generation
    "TOL-160": "Marketing, Sales",  # Zep - Memory for agents

    # AI Research & Analysis
    "TOL-065": "AI, Dev",  # Google AI Studio
    "TOL-079": "AI, Dev",  # Kimi K2 Thinking
    "TOL-099": "AI",  # MiniCPM-o 2.6

    # Lead Generation & Sales
    "TOL-130": "LG, Sales",  # Sales Navigator Agent
    "TOL-150": "LG, Sales, Marketing",  # V7 Go Agent

    # Database & Data Tools (AI-enhanced)
    "TOL-067": "Dev, AI",  # Google Cloud AI Platform
    "TOL-107": "Dev, AI",  # Pinecone
    "TOL-115": "Dev, AI",  # Qdrant

    # Specialized AI Tools
    "TOL-084": "Marketing, Sales, LG, All",  # LinkedIn (not AI but critical)
    "TOL-088": "Dev, Design",  # Lucide Icons
    "TOL-095": "Marketing",  # Mem0
    "TOL-108": "Marketing, HR",  # Poe
    "TOL-120": "Marketing, Design",  # Replit Agent
    "TOL-122": "AI",  # Research Labs
    "TOL-127": "Marketing, Design",  # Rows.ai
    "TOL-135": "Marketing",  # Speedrun
    "TOL-138": "Marketing",  # Synthesia
    "TOL-139": "Marketing, Sales",  # Taplio
    "TOL-151": "Marketing, Sales",  # V7 Llama
    "TOL-154": "Marketing",  # VLM Vision
    "TOL-155": "AI, Dev",  # VoyageAI
    "TOL-158": "Marketing",  # Windsurf
}


def assign_departments():
    """Add Departments column to master CSV."""
    print("=" * 80)
    print("ASSIGNING AI TOOLS TO DEPARTMENTS")
    print("=" * 80)

    tools = []
    updated_count = 0

    # Read CSV
    with open(MASTER_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        headers = list(reader.fieldnames)

        # Add Departments column if not exists
        if "Departments" not in headers:
            cat_idx = headers.index("Category")
            headers.insert(cat_idx + 1, "Departments")

        for row in reader:
            tol_id = row["TOL_ID"]
            category = row["Category"]

            # Assign departments for AI Tools
            if category == "AI Tools":
                if tol_id in DEPARTMENT_ASSIGNMENTS:
                    row["Departments"] = DEPARTMENT_ASSIGNMENTS[tol_id]
                    updated_count += 1
                    tool_name = row["Name"][:30]
                    dept_list = DEPARTMENT_ASSIGNMENTS[tol_id]
                    print(f"  [ASSIGN] {tol_id} {tool_name:<30} -> {dept_list}")
                else:
                    # Default for unassigned AI tools
                    row["Departments"] = "AI"
                    tool_name = row["Name"][:30]
                    print(f"  [DEFAULT] {tol_id} {tool_name:<30} -> AI (unassigned)")
            else:
                # Non-AI tools don't get department assignments
                row["Departments"] = ""

            tools.append(row)

    # Write updated CSV
    with open(MASTER_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(tools)

    print(f"\n[OK] Assigned departments to {updated_count} AI tools")
    print("=" * 80)

    return tools, headers


def create_department_view(tools):
    """Create department-based CSV view."""
    print("\n" + "=" * 80)
    print("CREATING DEPARTMENT-BASED VIEW")
    print("=" * 80)

    # Filter only AI Tools with departments
    ai_tools = [t for t in tools if t["Category"] == "AI Tools" and t.get("Departments")]

    # Create department mapping
    dept_tools = defaultdict(list)

    for tool in ai_tools:
        depts = [d.strip() for d in tool["Departments"].split(",")]
        for dept in depts:
            dept_tools[dept].append({
                "Department": dept,
                "TOL_ID": tool["TOL_ID"],
                "Name": tool["Name"],
                "Description": tool["Description"][:100] + "..." if len(tool["Description"]) > 100 else tool["Description"],
                "Purpose": tool["Purpose"][:80] + "..." if len(tool.get("Purpose", "")) > 80 else tool.get("Purpose", ""),
                "Cost": tool["Cost"][:50] + "..." if len(tool["Cost"]) > 50 else tool["Cost"],
                "Testing_Status": tool.get("Testing_Status", "Unknown"),
                "Mention_Count": tool.get("Mention_Count", "0")
            })

    # Sort by department, then by tool name
    all_dept_tools = []
    for dept in sorted(dept_tools.keys()):
        sorted_tools = sorted(dept_tools[dept], key=lambda x: x["Name"])
        all_dept_tools.extend(sorted_tools)
        print(f"  {dept}: {len(sorted_tools)} tools")

    # Write department view
    headers = ["Department", "TOL_ID", "Name", "Description", "Purpose", "Cost", "Testing_Status", "Mention_Count"]

    with open(BY_DEPT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(all_dept_tools)

    print(f"\n[OK] Created department view: {BY_DEPT_CSV}")
    print("=" * 80)

    return dept_tools


def generate_summary(dept_tools):
    """Generate department assignment summary."""
    print("\n" + "=" * 80)
    print("DEPARTMENT ASSIGNMENT SUMMARY")
    print("=" * 80)

    summary_file = TOOLS_ROOT / "DEPARTMENT_ASSIGNMENT_SUMMARY.md"
    total_assigned = sum(len(tools) for tools in dept_tools.values())

    lines = []
    lines.append("# AI Tools Department Assignment Summary")
    lines.append("")
    lines.append(f"**Date:** November 26, 2025")
    lines.append(f"**Total AI Tools:** 85")
    lines.append(f"**Tools Assigned:** {total_assigned} (with departments)")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Department Breakdown")
    lines.append("")

    # Department statistics
    for dept in sorted(dept_tools.keys()):
        tools = dept_tools[dept]
        tool_count = len(tools)
        lines.append(f"### {dept} ({tool_count} tools)")
        lines.append("")

        # List tools for this department
        for tool in sorted(tools, key=lambda x: x["Name"]):
            tol_id = tool["TOL_ID"]
            tool_name = tool["Name"]
            lines.append(f"- **{tol_id}**: {tool_name}")

        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Department Descriptions")
    lines.append("")
    lines.append("- **AI**: AI & Automation team - Core AI research, development, and implementation")
    lines.append("- **Dev**: Developers - Software development, coding, and technical implementation")
    lines.append("- **Design**: Designers / UI-UX - Visual design, branding, and user experience")
    lines.append("- **Video**: Video Editors - Video production, editing, and content creation")
    lines.append("- **HR**: Human Resources - People management and organizational tools")
    lines.append("- **Sales**: Sales Team - Sales enablement and customer acquisition")
    lines.append("- **LG**: Lead Generation - Prospect research and lead discovery")
    lines.append("- **Marketing**: Marketing Team - Content, campaigns, and brand marketing")
    lines.append("- **Finance**: Finance Team - Financial planning and analysis")
    lines.append("- **All**: All Employees - Universal tools for company-wide use")
    lines.append("")
    lines.append("---")
    lines.append("")

    with open(summary_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"[OK] Generated summary: {summary_file}")
    print("=" * 80)


def main():
    """Main execution."""
    print("\n" + "=" * 80)
    print("AI TOOLS DEPARTMENT ASSIGNMENT")
    print("=" * 80)

    # Step 1: Assign departments
    tools, headers = assign_departments()

    # Step 2: Create department view
    dept_tools = create_department_view(tools)

    # Step 3: Generate summary
    generate_summary(dept_tools)

    print("\n" + "=" * 80)
    print("[SUCCESS] DEPARTMENT ASSIGNMENT COMPLETE!")
    print("=" * 80)
    print("\nDepartment Distribution:")
    for dept in sorted(dept_tools.keys()):
        print(f"  {dept}: {len(dept_tools[dept])} tools")


if __name__ == "__main__":
    main()
