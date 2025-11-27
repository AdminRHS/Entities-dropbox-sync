"""
Aggregate structured and markdown listings (Phase 0)
- Reads normalized CSV/JSON sources from DEV/05_NEXT_DEVELOPMENT/_normalized and DATA.
- Normalizes status fields.
- Writes:
    ARCHITECTURE_PLAN/data_listing_structured.json
    ARCHITECTURE_PLAN/data_listing_markdown.json
"""
from __future__ import annotations

import csv
import json
import datetime as dt
from pathlib import Path
from typing import Dict, List, Callable


PROJECT_ROOT = Path(__file__).resolve().parents[3]  # .../apps/data
DEV_ROOT = PROJECT_ROOT / "DEV" / "05_NEXT_DEVELOPMENT"
NORM_ROOT = DEV_ROOT / "_normalized"
ARCH_PLAN = DEV_ROOT / "ARCHITECTURE_PLAN"


def read_csv(path: Path) -> List[Dict]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def normalize_status(value: str, mapping: Dict[str, str]) -> str:
    raw = (value or "").strip().lower()
    return mapping.get(raw, raw)


def load_researches() -> List[Dict]:
    path = NORM_ROOT / "RESEARCHES_Master_List_normalized.csv"
    if not path.exists():
        return []
    rows = read_csv(path)
    map_status = {
        "active": "active",
        "planning": "planning",
        "review": "review",
        "completed": "completed",
        "archived": "archived",
    }
    for r in rows:
        r["status"] = normalize_status(r.get("status"), map_status)
    return rows


def load_video_queue() -> List[Dict]:
    path = NORM_ROOT / "01_VIDEO_QUEUE" / "Video_Queue_Master_normalized.csv"
    if not path.exists():
        return []
    rows = read_csv(path)
    map_status = {
        "queued": "queued",
        "pending": "queued",
        "transcribing": "transcribing",
        "analyzing": "analyzing",
        "parsed": "completed",
        "completed": "completed",
        "failed": "failed",
        "selected": "analyzing",
    }
    for r in rows:
        r["status"] = normalize_status(r.get("status"), map_status)
    return rows


def load_search_queue() -> List[Dict]:
    path = NORM_ROOT / "00_SEARCH_QUEUE" / "Search_Queue_Master_normalized.csv"
    if not path.exists():
        return []
    rows = read_csv(path)
    map_status = {
        "pending": "pending",
        "active": "active",
        "completed": "completed",
        "cancelled": "cancelled",
    }
    for r in rows:
        r["status"] = normalize_status(r.get("status"), map_status)
    return rows


def load_json(path: Path) -> List[Dict]:
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    return data if isinstance(data, list) else []


def load_influencers() -> List[Dict]:
    # Use original JSON (нет отдельной нормализации)
    return load_json(PROJECT_ROOT / "DATA" / "ARCHIVE" / "04_INFLUENCER_DATA" / "Influencer_Database.json")


def load_channels() -> List[Dict]:
    return load_json(PROJECT_ROOT / "DATA" / "ARCHIVE" / "04_INFLUENCER_DATA" / "YouTube_Channels.json")


def load_tool_mapping() -> List[Dict]:
    return load_json(
        NORM_ROOT
        / "DATA"
        / "ARCHIVE"
        / "Pre_Taxonomy_Cleanup"
        / "Research_Reports"
        / "Extractions"
        / "tool_mapping_normalized.json"
    )


def load_discovered_tools() -> List[Dict]:
    return load_json(
        NORM_ROOT
        / "DATA"
        / "ARCHIVE"
        / "Pre_Taxonomy_Cleanup"
        / "Research_Reports"
        / "Extractions"
        / "discovered_tools_structured.json"
    )


def load_markdown_listing() -> List[Dict]:
    path = DEV_ROOT / "md_listing.json"
    return load_json(path)


def write_json(path: Path, data: Dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    now_utc = dt.datetime.now(dt.timezone.utc).isoformat()
    structured = {
        "generated_at": now_utc,
        "researches": load_researches(),
        "video_queue": load_video_queue(),
        "search_queue": load_search_queue(),
        "influencers": load_influencers(),
        "youtube_channels": load_channels(),
        "tool_mapping": load_tool_mapping(),
        "discovered_tools": load_discovered_tools(),
    }
    markdown = {"generated_at": now_utc, "markdown_listing": load_markdown_listing()}

    write_json(ARCH_PLAN / "data_listing_structured.json", structured)
    write_json(ARCH_PLAN / "data_listing_markdown.json", markdown)


if __name__ == "__main__":
    main()
