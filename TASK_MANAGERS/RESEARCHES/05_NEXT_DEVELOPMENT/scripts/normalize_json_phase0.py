"""
Phase 0 JSON normalizer.
- Normalizes tool_mapping.json keys to lowercase and captures conflicts.
- Structures discovered_tools.json into objects with a fixed schema.
- Writes normalized outputs to DEV/05_NEXT_DEVELOPMENT/_normalized/...
- Appends a short report to DEV/05_NEXT_DEVELOPMENT/ARCHITECTURE_PLAN/json_normalization_report.md.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple


PROJECT_ROOT = Path(__file__).resolve().parents[3]  # .../apps/data
DATA_ROOT = PROJECT_ROOT / "DATA"
ENTITIES_ROOT = PROJECT_ROOT / "ENTITIES"
DEV_ROOT = PROJECT_ROOT / "DEV" / "05_NEXT_DEVELOPMENT"
OUTPUT_ROOT = DEV_ROOT / "_normalized"
REPORT_PATH = DEV_ROOT / "reports" / "json_normalization_report.md"


def _pick_source(candidates: List[Path]) -> Path:
    for path in candidates:
        if path.exists():
            return path
    raise FileNotFoundError(f"No source found in: {', '.join(str(p) for p in candidates)}")


def _out_path(src: Path, suffix: str) -> Path:
    rel = src.relative_to(PROJECT_ROOT)
    out_dir = OUTPUT_ROOT / rel.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / f"{src.stem}_{suffix}"


def normalize_tool_mapping() -> str:
    src_candidates = [
        DATA_ROOT / "ARCHIVE" / "Pre_Taxonomy_Cleanup" / "Research_Reports" / "Extractions" / "tool_mapping.json",
        ENTITIES_ROOT
        / "TASK_MANAGERS"
        / "RESEARCHES"
        / "ARCHIVE"
        / "Pre_Taxonomy_Cleanup"
        / "Research_Reports"
        / "Extractions"
        / "tool_mapping.json",
    ]
    src = _pick_source(src_candidates)
    data = json.loads(src.read_text(encoding="utf-8"))
    buckets: Dict[str, List[Dict]] = defaultdict(list)
    for raw_key, payload in data.items():
        key = raw_key.strip().lower()
        buckets[key].append(payload)

    normalized = []
    for key, items in buckets.items():
        first = items[0]
        normalized.append(
            {
                "name": key,
                "tool_id": first.get("tool_id"),
                "category": first.get("category"),
                "file_path": first.get("file_path"),
            }
        )

    conflicts = {k: v for k, v in buckets.items() if len(v) > 1}
    out_main = _out_path(src, "normalized.json")
    out_conflicts = _out_path(src, "conflicts.json")
    out_main.write_text(json.dumps(normalized, ensure_ascii=False, indent=2), encoding="utf-8")
    out_conflicts.write_text(json.dumps(conflicts, ensure_ascii=False, indent=2), encoding="utf-8")

    return (
        f"tool_mapping: src={src.relative_to(PROJECT_ROOT)}, "
        f"normalized={out_main.relative_to(PROJECT_ROOT)}, "
        f"conflicts={len(conflicts)}"
    )


def structure_discovered_tools() -> str:
    src_candidates = [
        DATA_ROOT / "ARCHIVE" / "Pre_Taxonomy_Cleanup" / "Research_Reports" / "Extractions" / "discovered_tools.json",
        ENTITIES_ROOT
        / "TASK_MANAGERS"
        / "RESEARCHES"
        / "ARCHIVE"
        / "Pre_Taxonomy_Cleanup"
        / "Research_Reports"
        / "Extractions"
        / "discovered_tools.json",
    ]
    src = _pick_source(src_candidates)
    raw = json.loads(src.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise ValueError("discovered_tools.json expected to be an array")

    structured = []
    for item in raw:
        name = item if isinstance(item, str) else str(item)
        structured.append(
            {
                "tool_id": None,
                "name": name,
                "category": None,
                "source": "discovered_tools.json",
                "status": "pending",
            }
        )

    out_main = _out_path(src, "structured.json")
    out_main.write_text(json.dumps(structured, ensure_ascii=False, indent=2), encoding="utf-8")
    return f"discovered_tools: src={src.relative_to(PROJECT_ROOT)}, structured={out_main.relative_to(PROJECT_ROOT)}, rows={len(structured)}"


def append_report(lines: List[str]) -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    block = ["\n\n### JSON normalization run", "```text", *lines, "```"]
    with REPORT_PATH.open("a", encoding="utf-8") as f:
        f.write("\n".join(block))


def main() -> None:
    results: List[str] = []
    for func in (normalize_tool_mapping, structure_discovered_tools):
        try:
            results.append(func())
        except FileNotFoundError as exc:
            results.append(f"{func.__name__}: missing file ({exc})")
        except Exception as exc:  # pragma: no cover - defensive logging
            results.append(f"{func.__name__}: error ({exc})")
    append_report(results)


if __name__ == "__main__":
    main()
