"""
Run full inventory pipeline (Phase 0):
1. Normalize CSV sources
2. Normalize JSON sources
3. Inventory Markdown sources
4. Aggregate data listings
5. Produce summary metrics and append to README
"""
from __future__ import annotations

import datetime as dt
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple


PROJECT_ROOT = Path(__file__).resolve().parents[3]  # .../apps/data
DEV_ROOT = PROJECT_ROOT / "DEV" / "05_NEXT_DEVELOPMENT"
ARCH_PLAN = DEV_ROOT / "ARCHITECTURE_PLAN"
REPORTS = ARCH_PLAN / "reports"
README = ARCH_PLAN / "README.MD"


def run(cmd: List[str]) -> Tuple[int, str, str]:
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr


def header_check() -> List[str]:
    expected = {
        "researches": [
            "research_id",
            "name",
            "description",
            "department",
            "category",
            "file_path",
            "status",
            "created_date",
            "updated_date",
            "researcher_id",
            "metadata",
            "output_path",
        ],
        "videos": [
            "queue_id",
            "video_id",
            "video_title",
            "channel_name",
            "channel_url",
            "video_url",
            "views",
            "likes",
            "comments",
            "publish_date",
            "duration",
            "added_by",
            "added_date",
            "status",
            "selected_by",
            "selected_date",
            "parsed_date",
            "topic_category",
            "research_source",
            "priority_score",
            "notes",
            "created_date",
            "completed_date",
            "channel_id",
            "transcript_path",
            "phase",
        ],
        "search_queue": [
            "search_id",
            "employee",
            "department",
            "topic",
            "query",
            "status",
            "videos_found",
            "date_assigned",
            "date_completed",
            "results_path",
            "priority",
            "assigned_to",
            "notes",
        ],
    }
    paths = {
        "researches": DEV_ROOT / "_normalized" / "RESEARCHES_Master_List_normalized.csv",
        "videos": DEV_ROOT / "_normalized" / "01_VIDEO_QUEUE" / "Video_Queue_Master_normalized.csv",
        "search_queue": DEV_ROOT / "_normalized" / "00_SEARCH_QUEUE" / "Search_Queue_Master_normalized.csv",
    }
    issues = []
    for key, path in paths.items():
        if not path.exists():
            issues.append(f"{key}: missing file {path}")
            continue
        with path.open(encoding="utf-8") as f:
            header = f.readline().strip().split(",")
        missing = [col for col in expected[key] if col not in header]
        extra = [col for col in header if col not in expected[key]]
        if missing:
            issues.append(f"{key}: missing {missing}")
        if extra:
            issues.append(f"{key}: extra {extra}")
    return issues


def load_json(path: Path):
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def metrics() -> List[str]:
    structured = load_json(ARCH_PLAN / "data_listing_structured.json") or {}
    markdown = load_json(ARCH_PLAN / "data_listing_markdown.json") or {}

    counts = {
        "researches": len(structured.get("researches", [])),
        "video_queue": len(structured.get("video_queue", [])),
        "search_queue": len(structured.get("search_queue", [])),
        "influencers": len(structured.get("influencers", [])),
        "youtube_channels": len(structured.get("youtube_channels", [])),
        "tool_mapping": len(structured.get("tool_mapping", [])),
        "discovered_tools": len(structured.get("discovered_tools", [])),
        "markdown_files": len(markdown.get("markdown_listing", [])),
    }
    # status breakdowns
    video_status = {}
    for r in structured.get("video_queue", []):
        s = (r.get("status") or "").lower()
        video_status[s] = video_status.get(s, 0) + 1
    research_status = {}
    for r in structured.get("researches", []):
        s = (r.get("status") or "").lower()
        research_status[s] = research_status.get(s, 0) + 1

    lines = [
        f"counts: {counts}",
        f"video_status: {video_status}",
        f"research_status: {research_status}",
    ]
    return lines


def append_readme(summary: List[str]) -> None:
    ts = dt.datetime.now(dt.timezone.utc).isoformat()
    block = [f"\n\n### Last inventory run {ts}", "```text", *summary, "```"]
    with README.open("a", encoding="utf-8") as f:
        f.write("\n".join(block))


def write_report(fname: str, content: List[str]) -> None:
    REPORTS.mkdir(parents=True, exist_ok=True)
    path = REPORTS / fname
    block = ["```text", *content, "```"]
    path.write_text("\n".join(block), encoding="utf-8")


def main() -> None:
    steps = [
        ["py", str(DEV_ROOT / "scripts" / "normalize_csv_phase0.py")],
        ["py", str(DEV_ROOT / "scripts" / "normalize_json_phase0.py")],
        ["py", str(DEV_ROOT / "scripts" / "md_inventory.py")],
        ["py", str(DEV_ROOT / "scripts" / "aggregate_data_listings.py")],
    ]
    results = []
    for cmd in steps:
        code, out, err = run(cmd)
        results.append(f"{' '.join(cmd)} -> code={code}")
        if out.strip():
            results.append(f"stdout: {out.strip()}")
        if err.strip():
            results.append(f"stderr: {err.strip()}")

    issues = header_check()
    summary = ["inventory pipeline finished", *results]
    if issues:
        summary.append(f"header_check issues: {issues}")
    summary.extend(metrics())

    write_report("inventory_run.md", summary)
    append_readme(summary)


if __name__ == "__main__":
    main()
