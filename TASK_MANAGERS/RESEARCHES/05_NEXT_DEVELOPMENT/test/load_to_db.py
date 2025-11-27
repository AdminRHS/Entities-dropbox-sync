"""
Helper script to load Phase 0 test data into PostgreSQL.

Inputs:
- DEV/05_NEXT_DEVELOPMENT/test/data_listing_structured.json
- DEV/05_NEXT_DEVELOPMENT/test/data_listing_markdown.json

Env vars:
- PGHOST, PGPORT, PGUSER, PGPASSWORD, PGDATABASE

Usage:
  py DEV/05_NEXT_DEVELOPMENT/test/load_to_db.py
"""
from __future__ import annotations

import csv
import io
import json
import os
from pathlib import Path
from typing import Iterable, List, Dict

import psycopg2

ROOT = Path(__file__).resolve().parents[2]  # .../DEV/05_NEXT_DEVELOPMENT
TEST_ROOT = ROOT / "test"
STRUCTURED = TEST_ROOT / "data_listing_structured.json"
MARKDOWN = TEST_ROOT / "data_listing_markdown.json"


def connect():
    conn = psycopg2.connect(
        host=os.environ.get("PGHOST", "localhost"),
        port=os.environ.get("PGPORT", "5432"),
        user=os.environ.get("PGUSER", "postgres"),
        password=os.environ.get("PGPASSWORD", ""),
        dbname=os.environ.get("PGDATABASE", "postgres"),
    )
    conn.autocommit = True
    return conn


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def copy_rows(cur, table: str, rows: Iterable[Dict], columns: List[str]) -> None:
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=columns)
    for row in rows:
        writer.writerow({c: row.get(c, "") for c in columns})
    buf.seek(0)
    cur.copy_expert(
        f"COPY {table} ({', '.join(columns)}) FROM STDIN WITH CSV",
        buf,
    )


def main():
    structured = load_json(STRUCTURED)
    markdown = load_json(MARKDOWN)
    conn = connect()
    cur = conn.cursor()

    copy_rows(
        cur,
        "researches",
        structured.get("researches", []),
        [
            "research_id",
            "name",
            "description",
            "department",
            "status",
            "created_date",
            "updated_date",
            "researcher_id",
            "metadata",
            "output_path",
        ],
    )

    copy_rows(
        cur,
        "videos",
        structured.get("video_queue", []),
        [
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
    )

    copy_rows(
        cur,
        "search_queue",
        structured.get("search_queue", []),
        [
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
    )

    copy_rows(
        cur,
        "tool_mapping",
        structured.get("tool_mapping", []),
        [
            "name",
            "tool_id",
            "category",
            "file_path",
        ],
    )

    copy_rows(
        cur,
        "discovered_tools",
        structured.get("discovered_tools", []),
        [
            "name",
            "status",
            "category",
            "source",
            "tool_id",
        ],
    )

    copy_rows(
        cur,
        "markdown_files",
        markdown.get("markdown_listing", []),
        [
            "path",
            "entity_id",
            "entity_type",
            "department",
            "status",
            "phase",
            "last_modified",
        ],
    )

    cur.close()
    conn.close()
    print("Load completed.")


if __name__ == "__main__":
    main()
