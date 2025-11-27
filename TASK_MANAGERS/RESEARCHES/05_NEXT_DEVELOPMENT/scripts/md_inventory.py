"""
Markdown inventory (Phase 0)
- Scans DATA/** for .md files.
- Extracts metadata: entity_id, entity_type, department, status, phase, last_modified.
- Outputs CSV/JSON to DEV/05_NEXT_DEVELOPMENT/md_listing.{csv,json}.
- Logs summary to DEV/05_NEXT_DEVELOPMENT/reports/md_inventory_report.md.
Note: run with `python` available on PATH.
"""
from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable, List, Optional


PROJECT_ROOT = Path(__file__).resolve().parents[3]  # .../apps/data
DATA_ROOT = PROJECT_ROOT / "DATA"
DEV_ROOT = PROJECT_ROOT / "DEV" / "05_NEXT_DEVELOPMENT"
REPORTS_ROOT = DEV_ROOT / "reports"
OUT_CSV = DEV_ROOT / "md_listing.csv"
OUT_JSON = DEV_ROOT / "md_listing.json"
REPORT_PATH = REPORTS_ROOT / "md_inventory_report.md"


ENTITY_ID_RE = re.compile(r"(RSH-[A-Z]+-\d+|RSR-\d+|Video_\d+|Video_\d{3}|TASK-[A-Z]+-\d+|WRF-\d+)", re.IGNORECASE)
STATUS_RE = re.compile(r"\b(Active|Archived|Draft)\b", re.IGNORECASE)


@dataclass
class MdRecord:
    path: str
    entity_id: str
    entity_type: str
    department: str
    status: str
    phase: str
    last_modified: str


def guess_entity_type(rel_parts: List[str]) -> str:
    if not rel_parts:
        return "other"
    top = rel_parts[0].lower()
    if top.startswith("02_transcriptions") or "transcription" in top:
        return "video"
    if top.startswith("03_analysis") or "analysis" in top:
        return "analysis"
    if top.startswith("prompts"):
        return "prompt"
    if top.startswith("reports"):
        return "report"
    if top.startswith("00_search_queue") or top.startswith("01_video_queue"):
        return "queue"
    if top.startswith("archive"):
        return "archive"
    return "other"


def guess_department(rel_parts: List[str]) -> str:
    # Use the first part after DATA/ if present, else empty.
    return rel_parts[0] if rel_parts else ""


def extract_status(text: str) -> str:
    match = STATUS_RE.search(text)
    return match.group(1).title() if match else ""


def extract_phase(rel_parts: List[str], filename: str) -> str:
    for part in rel_parts:
        m = re.search(r"phase[_\-\s]?(\d+)", part, re.IGNORECASE)
        if m:
            return m.group(1)
    m = re.search(r"phase[_\-\s]?(\d+)", filename, re.IGNORECASE)
    return m.group(1) if m else ""


def extract_entity_id(text: str, filename: str) -> str:
    for candidate in [filename, text]:
        match = ENTITY_ID_RE.search(candidate)
        if match:
            return match.group(1)
    return ""


def scan_markdown_files(root: Path) -> Iterable[Path]:
    yield from root.rglob("*.md")


def main() -> None:
    records: List[MdRecord] = []
    for path in scan_markdown_files(DATA_ROOT):
        rel = path.relative_to(PROJECT_ROOT)
        rel_parts = list(rel.parts[1:])  # skip DATA
        text = path.read_text(encoding="utf-8", errors="ignore")
        entity_id = extract_entity_id(text, path.name)
        entity_type = guess_entity_type(rel_parts)
        department = guess_department(rel_parts)
        status = extract_status(text)
        phase = extract_phase(rel_parts, path.name)
        last_modified = path.stat().st_mtime
        records.append(
            MdRecord(
                path=str(rel).replace("\\", "/"),
                entity_id=entity_id,
                entity_type=entity_type,
                department=department,
                status=status,
                phase=phase,
                last_modified=str(last_modified),
            )
        )

    # Outputs
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(asdict(records[0]).keys()) if records else [])
        if records:
            writer.writeheader()
            writer.writerows(asdict(r) for r in records)

    OUT_JSON.write_text(json.dumps([asdict(r) for r in records], ensure_ascii=False, indent=2), encoding="utf-8")

    # Report
    REPORTS_ROOT.mkdir(parents=True, exist_ok=True)
    summary = [
        f"files={len(records)}",
        f"with_entity_id={sum(1 for r in records if r.entity_id)}",
        f"video={sum(1 for r in records if r.entity_type=='video')}",
        f"analysis={sum(1 for r in records if r.entity_type=='analysis')}",
        f"prompt={sum(1 for r in records if r.entity_type=='prompt')}",
        f"report={sum(1 for r in records if r.entity_type=='report')}",
    ]
    block = ["\n\n### MD inventory run", "```text", *summary, "```"]
    with REPORT_PATH.open("a", encoding="utf-8") as f:
        f.write("\n".join(block))


if __name__ == "__main__":
    main()
