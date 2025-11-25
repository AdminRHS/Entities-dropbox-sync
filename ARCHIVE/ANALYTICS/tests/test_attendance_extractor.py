"""
Tests for EMPLOYEES_Attendance_Remote_Helpers_Extractor.
"""

from __future__ import annotations

import csv
import io
from pathlib import Path
from typing import Any, Dict

import json

import importlib.util


def _load_module() -> Any:
    """
    Load the attendance extractor module from its file path.

    Returns:
        Any: Loaded module object for the extractor.
    """
    module_path = (
        Path(__file__)
        .resolve()
        .parents[1]
        / "EMPLOYEES_Attendance_Remote_Helpers_Extractor.py"
    )
    spec = importlib.util.spec_from_file_location(
        "attendance_extractor", module_path
    )
    module = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)  # type: ignore[assignment]
    return module


def _fake_response(payload: Dict[str, Any]) -> Any:
    """
    Create a minimal fake HTTP response object.

    Args:
        payload (Dict[str, Any]): JSON payload to be returned by the fake response.

    Returns:
        Any: Object implementing a context manager with a .read() method.
    """

    class _Response:
        def __init__(self, data: bytes) -> None:
            self._data = data

        def read(self) -> bytes:
            return self._data

        def __enter__(self) -> "_Response":
            return self

        def __exit__(self, exc_type, exc, tb) -> None:  # noqa: D401, ANN001
            """No-op context manager exit."""
            return None

    raw = json.dumps(payload).encode("utf-8")
    return _Response(raw)


def test_generate_attendance_report_happy_path(tmp_path: Path) -> None:
    """
    Happy path: employees with and without attendance records produce a CSV.

    Args:
        tmp_path (Path): Temporary directory provided by pytest.
    """
    module = _load_module()

    payload = {
        "message": "Get employees with attendance successfully",
        "data": {
            "date": "2025-11-16",
            "employees": [
                {
                    "employee_id": "EMP001",
                    "discord_user_id": "1234567890",
                    "attendance": [
                        {
                            "check_in": "2025-11-16T09:00:00",
                            "check_out": "2025-11-16T18:00:00",
                        }
                    ],
                },
                {
                    "employee_id": "EMP002",
                    "discord_user_id": "0987654321",
                    "attendance": [],
                },
            ],
        },
    }

    report_path = module.generate_attendance_report(payload, output_dir=tmp_path)

    assert report_path.exists()

    with report_path.open("r", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)

    assert len(rows) == 2

    row_with_attendance = next(r for r in rows if r["employee_id"] == "EMP001")
    assert row_with_attendance["attendance_status"] == "present"
    assert row_with_attendance["attendance_records"] == "1"
    assert row_with_attendance["first_check_in"] == "2025-11-16T09:00:00"
    assert row_with_attendance["last_check_out"] == "2025-11-16T18:00:00"

    row_without_attendance = next(r for r in rows if r["employee_id"] == "EMP002")
    assert row_without_attendance["attendance_status"] == "no_records"
    assert row_without_attendance["attendance_records"] == "0"


def test_generate_attendance_report_empty_employees(tmp_path: Path) -> None:
    """
    Edge case: API returns an empty employees list and still writes a CSV header.

    Args:
        tmp_path (Path): Temporary directory provided by pytest.
    """
    module = _load_module()

    payload = {
        "message": "Get employees with attendance successfully",
        "data": {"date": "2025-11-16", "employees": []},
    }

    report_path = module.generate_attendance_report(payload, output_dir=tmp_path)
    assert report_path.exists()

    with report_path.open("r", encoding="utf-8") as fh:
        content = fh.read()

    # There should be exactly one data section: the header.
    reader = csv.DictReader(io.StringIO(content))
    rows = list(reader)
    assert rows == []


def test_fetch_yesterday_attendance_http_failure(tmp_path: Path) -> None:
    """
    Failure case: HTTP error during fetch raises a RuntimeError from run().

    Args:
        tmp_path (Path): Temporary directory provided by pytest.
    """
    module = _load_module()

    def failing_opener(url: str) -> Any:  # noqa: ARG001
        raise RuntimeError("network down")

    try:
        module.run(output_dir=tmp_path, opener=failing_opener)
        assert False, "Expected RuntimeError to be raised"
    except RuntimeError as exc:
        assert "network down" in str(exc)


