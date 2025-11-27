"""
Phase 0 CSV normalizer.
- Renames headers to snake_case.
- Adds missing columns required by target schemas.
- Writes *_normalized.csv to DEV/05_NEXT_DEVELOPMENT/_normalized.
- Appends a short report to DEV/05_NEXT_DEVELOPMENT/ARCHITECTURE_PLAN/README.MD.
"""
from __future__ import annotations

import csv
import datetime as dt
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


PROJECT_ROOT = Path(__file__).resolve().parents[3]  # .../apps/data
DATA_ROOT = PROJECT_ROOT / "DATA"
DEV_ROOT = PROJECT_ROOT / "DEV" / "05_NEXT_DEVELOPMENT"
OUTPUT_ROOT = DEV_ROOT / "_normalized"
REPORT_PATH = DEV_ROOT / "reports" / "csv_normalization_report.md"


def _read_csv(path: Path) -> Tuple[List[dict], List[str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        headers = reader.fieldnames or []
    return rows, headers


def _write_csv(path: Path, headers: Iterable[str], rows: Iterable[Dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(headers))
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _get_value(row: Dict[str, str], candidates: Iterable[str]) -> str:
    lower_map = {k.lower(): v for k, v in row.items()}
    for cand in candidates:
        key = cand.lower()
        if key in lower_map:
            return lower_map[key]
    return ""


def _out_path(src: Path) -> Path:
    rel = src.relative_to(DATA_ROOT)
    out_dir = OUTPUT_ROOT / rel.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / f"{src.stem}_normalized.csv"


def normalize_researches() -> str:
    src = DATA_ROOT / "RESEARCHES_Master_List.csv"
    target_cols = [
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
    ]
    rename = {
        "research_id": ["RSR_ID", "research_id"],
        "name": ["Name", "Title"],
        "description": ["Description"],
        "department": ["Department"],
        "category": ["Category"],
        "file_path": ["File_Path", "FilePath", "Path"],
        "status": ["Status"],
    }
    rows, headers = _read_csv(src)
    header_lower = {h.lower() for h in headers}
    missing = [col for col, cands in rename.items() if not any(c.lower() in header_lower for c in cands)]
    normalized = []
    for row in rows:
        new_row = {col: _get_value(row, rename.get(col, [col])) for col in target_cols}
        normalized.append(new_row)
    out = _out_path(src)
    _write_csv(out, target_cols, normalized)
    miss_txt = f", missing_sources={missing}" if missing else ""
    return f"researches: rows={len(rows)}, src_headers={headers}{miss_txt}, out={out.relative_to(PROJECT_ROOT)}"


def normalize_videos() -> str:
    src = DATA_ROOT / "01_VIDEO_QUEUE" / "Video_Queue_Master.csv"
    target_cols = [
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
    ]
    rename = {
        "queue_id": ["Queue_ID"],
        "video_id": ["Video_ID"],
        "video_title": ["Video_Title", "Title"],
        "channel_name": ["Channel_Name"],
        "channel_url": ["Channel_URL"],
        "video_url": ["Video_URL"],
        "views": ["Views"],
        "likes": ["Likes"],
        "comments": ["Comments"],
        "publish_date": ["Publish_Date"],
        "duration": ["Duration"],
        "added_by": ["Added_By"],
        "added_date": ["Added_Date"],
        "status": ["Status"],
        "selected_by": ["Selected_By"],
        "selected_date": ["Selected_Date"],
        "parsed_date": ["Parsed_Date"],
        "topic_category": ["Topic_Category"],
        "research_source": ["Research_Source"],
        "priority_score": ["Priority_Score"],
        "notes": ["Notes"],
    }
    status_map = {"pending": "queued", "selected": "analyzing", "parsed": "completed"}
    rows, headers = _read_csv(src)
    header_lower = {h.lower() for h in headers}
    missing = [col for col, cands in rename.items() if not any(c.lower() in header_lower for c in cands)]
    normalized = []
    for row in rows:
        new_row = {col: _get_value(row, rename.get(col, [col])) for col in target_cols}
        status_raw = new_row.get("status", "").strip().lower()
        new_row["status"] = status_map.get(status_raw, status_raw or "")
        new_row["created_date"] = new_row.get("added_date", "")
        new_row["completed_date"] = new_row.get("parsed_date", "")
        new_row.setdefault("channel_id", "")
        new_row.setdefault("transcript_path", "")
        new_row.setdefault("phase", "")
        normalized.append(new_row)
    out = _out_path(src)
    _write_csv(out, target_cols, normalized)
    miss_txt = f", missing_sources={missing}" if missing else ""
    return f"videos: rows={len(rows)}, src_headers={headers}{miss_txt}, out={out.relative_to(PROJECT_ROOT)}"


def normalize_search_queue() -> str:
    src = DATA_ROOT / "00_SEARCH_QUEUE" / "Search_Queue_Master.csv"
    target_cols = [
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
    ]
    rename = {
        "search_id": ["Search_ID"],
        "employee": ["Employee", "Assigned_To"],
        "department": ["Department"],
        "topic": ["Topic"],
        "query": ["Search_Query", "Query"],
        "status": ["Status"],
        "videos_found": ["Videos_Found"],
        "date_assigned": ["Date_Assigned"],
        "date_completed": ["Date_Completed"],
        "notes": ["Notes"],
    }
    rows, headers = _read_csv(src)
    header_lower = {h.lower() for h in headers}
    missing = [col for col, cands in rename.items() if not any(c.lower() in header_lower for c in cands)]
    normalized = []
    for row in rows:
        new_row = {col: _get_value(row, rename.get(col, [col])) for col in target_cols}
        if not new_row.get("query"):
            new_row["query"] = new_row.get("search_query", "")
        normalized.append(new_row)
    out = _out_path(src)
    _write_csv(out, target_cols, normalized)
    miss_txt = f", missing_sources={missing}" if missing else ""
    return f"search_queue: rows={len(rows)}, src_headers={headers}{miss_txt}, out={out.relative_to(PROJECT_ROOT)}"


def append_report(lines: List[str]) -> None:
    ts = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    block = [f"\n\n### CSV normalization run {ts}", "```text", *lines, "```"]
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with REPORT_PATH.open("a", encoding="utf-8") as f:
        f.write("\n".join(block))


def main() -> None:
    results = []
    for func in (normalize_researches, normalize_videos, normalize_search_queue):
        try:
            results.append(func())
        except FileNotFoundError as exc:
            results.append(f"{func.__name__}: missing file ({exc})")
    append_report(results)


if __name__ == "__main__":
    main()
