# Processed Department Reports for TASK_MANAGERS Import

**Purpose:** This directory contains processed variations of department reports that match the TASK_MANAGERS architecture naming conventions for data import.

**Generated:** November 20, 2025

---

## Naming Convention

All processed reports follow the pattern:
```
[DEPT_CODE]_Department_Report_YYYY-MM-DD.md
```

Where `DEPT_CODE` is the 3-letter department code used in TASK_MANAGERS architecture.

---

## Department Code Mapping

| Original Name | Department Code | Full Name |
|--------------|-----------------|-----------|
| AI | AID | AI Department |
| Design | DGN | Design & Creative |
| Dev/Development | DEV | Development & Engineering |
| Finance | FNC | Finance |
| HR | HRM | Human Resource Management |
| LG/Lead Generation | LGN | Lead Generation & Marketing |
| Sales | SLS | Sales & Client Relations |
| Video | VID | Video Production |

---

## Files

- `AID_Department_Report_2025-11-20.md` - AI Department report
- `DGN_Department_Report_2025-11-20.md` - Design Department report
- `DEV_Department_Report_2025-11-20.md` - Development Department report
- `FNC_Department_Report_2025-11-20.md` - Finance Department report
- `HRM_Department_Report_2025-11-20.md` - HR Department report
- `LGN_Department_Report_2025-11-20.md` - Lead Generation Department report
- `SLS_Department_Report_2025-11-20.md` - Sales Department report
- `VID_Department_Report_2025-11-20.md` - Video Department report
- `Department_Report_Mapping.json` - Mapping between original and processed filenames

---

## Processing Script

The reports were processed using `process_reports_for_tm.py` located in the parent directory.

**Key Processing Steps:**
1. Extract department code from original filename
2. **Filename Transformation:** Renamed files to use department codes
3. **Content Validation:** Ensured department codes are consistently used in headers and content
4. **Malformed Pattern Fixes:** Fixed any incorrectly inserted department codes
5. **Duplicate Removal:** Removed duplicate department code references
6. Extract date and calculate day of week (added for pattern analysis)
7. Inject day of week metadata into report content (added for pattern analysis)
8. **Filename Transformation:** Renamed files to use department codes
9. **Content Validation:** Ensured department codes are consistently used in headers and content
10. **Malformed Pattern Fixes:** Fixed any incorrectly inserted department codes
11. **Duplicate Removal:** Removed duplicate department code references

## Day of Week Integration

All processed reports include day of week information for pattern analysis:

- **Day Name:** Full day name (e.g., "Thursday")
- **Day Name Short:** 3-letter abbreviation (e.g., "Thu")
- **Day Number:** 0-6 (Monday=0, Sunday=6)
- **Weekday/Weekend:** Boolean flags for filtering

This data is:
- Injected into the EXECUTIVE SUMMARY section of each report
- Stored in the `Department_Report_Mapping.json` metadata
- Available for pattern analysis using `analyze_report_patterns.py`

## Pattern Analysis

Use `analyze_report_patterns.py` to identify patterns and repetitions:

```bash
# Analyze all reports
python analyze_report_patterns.py

# Filter by date range
python analyze_report_patterns.py --date-range 2025-11-01 2025-11-30

# Filter by department
python analyze_report_patterns.py --department AID

# Custom output file
python analyze_report_patterns.py --output Custom_Pattern_Report.md
```

The analysis generates:
- `Pattern_Analysis_Report.md` - Human-readable pattern report
- `Pattern_Analysis_Data.json` - Machine-readable data for further analysis

---

## Usage

These processed reports are ready for import into TASK_MANAGERS systems that expect department codes in filenames and content.

**Original Reports Location:** `../Departments/`

**Processed Reports Location:** `Departments_Processed_TM/`

---

## Related Documentation

- See `Department_Report_Mapping.json` for detailed mapping information
- See `../MASTER_REPORT_2025-11-20.md` for consolidated report
- See `../../TASK_MANAGERS/README.md` for TASK_MANAGERS architecture details

---

**Last Updated:** November 20, 2025

