"""
EMPLOYEES Attendance Remote Helpers Extractor.

Fetches yesterday's attendance data for Remote Helpers employees from the CRM-S
API and writes a CSV report into the ANALYTICS entity.
"""

from __future__ import annotations

import csv
import json
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Optional

import urllib.error
import urllib.request


API_URL = (
    "https://crm-s.com/api/v1/employees-attendance-yesterday"
    "?global_company_name=Remote%20Helpers"
)
DEFAULT_OUTPUT_DIR = Path(r"C:\Users\Dell\Dropbox\ENTITIES\ANALYTICS")

AttendanceOpener = Callable[[str], Any]


@dataclass
class AttendanceRow:
    """
    Normalized attendance row for CSV export.

    Args:
        employee_id (str): Employee identifier from the CRM-S system.
        discord_user_id (str): Optional Discord user ID associated with the employee.
        attendance_records (int): Count of attendance entries for the day.
        attendance_status (str): High-level attendance status
            (for example, "present" or "no_records").
        first_check_in (str): First check-in timestamp string, if available.
        last_check_out (str): Last check-out timestamp string, if available.
    """

    employee_id: str
    discord_user_id: str
    attendance_records: int
    attendance_status: str
    first_check_in: str
    last_check_out: str


def fetch_yesterday_attendance(
    api_url: str = API_URL,
    opener: Optional[AttendanceOpener] = None,
) -> Dict[str, Any]:
    """
    Fetch yesterday's attendance payload from the CRM-S API.

    Args:
        api_url (str): Endpoint URL to request attendance data from.
        opener (Optional[AttendanceOpener]): Optional function used to open
            the URL, primarily for testing. Defaults to `urllib.request.urlopen`.

    Returns:
        Dict[str, Any]: Parsed JSON payload with keys like "message" and "data".

    Raises:
        RuntimeError: If the HTTP request fails or the payload cannot be parsed.
    """
    opener = opener or urllib.request.urlopen

    try:
        with opener(api_url) as response:
            # Reason: CRM-S API is expected to return JSON as UTF-8 text.
            raw = response.read()
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Failed to fetch attendance data: {exc}") from exc

    try:
        text = raw.decode("utf-8")
        payload: Dict[str, Any] = json.loads(text)
    except Exception as exc:
        raise RuntimeError(f"Failed to parse attendance response JSON: {exc}") from exc

    if not isinstance(payload, Dict) or "data" not in payload:
        raise RuntimeError("Unexpected attendance response format: missing 'data' key.")

    return payload


def _normalize_attendance_rows(
    employees: Iterable[Dict[str, Any]],
) -> List[AttendanceRow]:
    """
    Normalize raw employee records into flat attendance rows.

    Args:
        employees (Iterable[Dict[str, Any]]): Raw employee entries from the
            CRM-S API payload.

    Returns:
        List[AttendanceRow]: Flattened attendance rows ready for CSV export.
    """
    rows: List[AttendanceRow] = []

    for item in employees:
        employee_id = str(item.get("employee_id", "") or "")
        discord_user_id = str(item.get("discord_user_id", "") or "")
        attendance_list = item.get("attendance") or []

        if not isinstance(attendance_list, list):
            # Reason: Defensive fallback in case attendance is not the expected list.
            attendance_list = []

        if not attendance_list:
            rows.append(
                AttendanceRow(
                    employee_id=employee_id,
                    discord_user_id=discord_user_id,
                    attendance_records=0,
                    attendance_status="no_records",
                    first_check_in="",
                    last_check_out="",
                )
            )
            continue

        # Reason: Schema for attendance entries is not strictly defined;
        # we look for generic check-in / check-out style fields when present.
        first_entry = attendance_list[0]
        last_entry = attendance_list[-1]

        first_check_in = str(
            first_entry.get("check_in")
            or first_entry.get("start_time")
            or first_entry.get("time_in")
            or ""
        )
        last_check_out = str(
            last_entry.get("check_out")
            or last_entry.get("end_time")
            or last_entry.get("time_out")
            or ""
        )

        rows.append(
            AttendanceRow(
                employee_id=employee_id,
                discord_user_id=discord_user_id,
                attendance_records=len(attendance_list),
                attendance_status="present",
                first_check_in=first_check_in,
                last_check_out=last_check_out,
            )
        )

    return rows


def _build_output_path(report_date: date, output_dir: Optional[Path] = None) -> Path:
    """
    Build a standardized output path for the attendance CSV.

    Args:
        report_date (date): Date the report represents (typically yesterday).
        output_dir (Optional[Path]): Directory where the CSV should be written.

    Returns:
        Path: Full path to the output CSV file.
    """
    base_dir = output_dir or DEFAULT_OUTPUT_DIR
    base_dir = Path(base_dir)

    date_str = report_date.strftime("%Y_%m_%d")
    filename = f"ANALYTICS_Employees_Attendance_Remote_Helpers_{date_str}.csv"

    return base_dir / filename


def generate_attendance_report(
    payload: Dict[str, Any],
    output_dir: Optional[Path] = None,
) -> Path:
    """
    Generate the attendance CSV report from an API payload.

    Args:
        payload (Dict[str, Any]): Parsed JSON response from the CRM-S API.
        output_dir (Optional[Path]): Directory where the CSV should be stored.

    Returns:
        Path: Path to the generated CSV report.

    Raises:
        RuntimeError: If required data is missing or malformed.
    """
    data = payload.get("data") or {}
    employees = data.get("employees") or []

    if not isinstance(employees, list):
        raise RuntimeError("Unexpected data format: 'employees' is not a list.")

    report_date_str = data.get("date") or payload.get("date")
    if report_date_str:
        try:
            report_date = date.fromisoformat(str(report_date_str))
        except ValueError:
            # Reason: Fall back to today's date if the API date is not parseable.
            report_date = date.today()
    else:
        report_date = date.today()

    rows = _normalize_attendance_rows(employees)
    output_path = _build_output_path(report_date, output_dir=output_dir)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "employee_id",
        "discord_user_id",
        "attendance_records",
        "attendance_status",
        "first_check_in",
        "last_check_out",
    ]

    with output_path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "employee_id": row.employee_id,
                    "discord_user_id": row.discord_user_id,
                    "attendance_records": row.attendance_records,
                    "attendance_status": row.attendance_status,
                    "first_check_in": row.first_check_in,
                    "last_check_out": row.last_check_out,
                }
            )

    return output_path


def run(
    output_dir: Optional[Path] = None,
    api_url: str = API_URL,
    opener: Optional[AttendanceOpener] = None,
) -> Path:
    """
    Fetch yesterday's attendance and generate the CSV report.

    Args:
        output_dir (Optional[Path]): Directory where the CSV should be stored.
        api_url (str): Endpoint URL for the attendance API.
        opener (Optional[AttendanceOpener]): Optional custom opener for testing.

    Returns:
        Path: Path to the generated CSV report.

    Raises:
        RuntimeError: If fetching or report generation fails.
    """
    payload = fetch_yesterday_attendance(api_url=api_url, opener=opener)
    return generate_attendance_report(payload, output_dir=output_dir)


def main(argv: Optional[List[str]] = None) -> int:
    """
    Command-line entry point for the attendance extractor.

    Supports an optional `--output-dir` argument to override the default
    analytics folder location.

    Args:
        argv (Optional[List[str]]): Optional list of arguments (for testing).

    Returns:
        int: Exit status code (0 on success, non-zero on failure).
    """
    import argparse

    parser = argparse.ArgumentParser(
        description=(
            "Fetch yesterday's Remote Helpers attendance from CRM-S and write a CSV report."
        )
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=None,
        help=(
            "Optional directory where the CSV report should be saved "
            "(default: C:\\Users\\Dell\\Dropbox\\ENTITIES\\ANALYTICS)."
        ),
    )
    args = parser.parse_args(argv)

    try:
        output_dir = Path(args.output_dir) if args.output_dir else None
        path = run(output_dir=output_dir)
        print(f"[OK] Attendance report generated at: {path}")
    except Exception as exc:  # noqa: BLE001
        # Reason: Top-level handler to ensure a clean, non-traceback CLI error.
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


