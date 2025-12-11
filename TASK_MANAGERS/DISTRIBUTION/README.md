# Distribution Master System

**Created:** 2025-12-11
**Purpose:** Daily employee distribution and compliance tracking

---

## Folder Structure

```
DISTRIBUTION/
├── DISTRIBUTION_CURRENT.csv          # Current working version (always latest)
├── daily/                             # Daily snapshots organized by month
│   ├── 2025-12/
│   │   ├── DISTRIBUTION_2025-12-10.csv
│   │   ├── DISTRIBUTION_2025-12-11.csv
│   │   └── DISTRIBUTION_2025-12-12.csv
│   └── 2026-01/
│       └── DISTRIBUTION_2026-01-01.csv
├── archive/                           # Historical archives and backups
│   └── DISTRIBUTION_MASTER_archived_2025-12-11.csv
└── templates/                         # Template files for new distributions
    └── DISTRIBUTION_TEMPLATE.csv
```

---

## Daily Workflow

### Every Day (Automated or Manual)

1. **Morning Snapshot Creation**
   ```bash
   # Copy current to daily snapshot
   cp DISTRIBUTION_CURRENT.csv daily/YYYY-MM/DISTRIBUTION_YYYY-MM-DD.csv
   ```

2. **Update Current Version**
   - Edit `DISTRIBUTION_CURRENT.csv` throughout the day
   - Track employee compliance changes
   - Update tool installations
   - Log violations

3. **End of Day**
   - Final snapshot automatically saved
   - Current version ready for next day

---

## File Naming Convention

### Daily Snapshots
**Format:** `DISTRIBUTION_YYYY-MM-DD.csv`

**Examples:**
- `DISTRIBUTION_2025-12-11.csv` (December 11, 2025)
- `DISTRIBUTION_2025-12-31.csv` (December 31, 2025)
- `DISTRIBUTION_2026-01-01.csv` (January 1, 2026)

### Monthly Organization
Daily snapshots are organized in folders by `YYYY-MM` format:
- `daily/2025-12/` contains all December 2025 snapshots
- `daily/2026-01/` contains all January 2026 snapshots

---

## Fields in DISTRIBUTION Files

```csv
EMPLOYEE_NAME,DEPT_CODE,FOLDER_PATH,ACTIVE,ACCOUNT_TRACKING_REQUIRED,MULTI_TOOL_REQUIRED,TOOLS_INSTALLED,COMPLIANCE_STATUS,LAST_LOGIN_LOGGED,VIOLATIONS_COUNT,UPDATED
```

### Field Descriptions

- **EMPLOYEE_NAME:** Employee identifier from registry
- **DEPT_CODE:** Department code (DEP.02, EMP, etc.)
- **FOLDER_PATH:** Relative path to employee folder
- **ACTIVE:** Activity status (active/inactive/unknown)
- **ACCOUNT_TRACKING_REQUIRED:** Whether tracking is required (yes/no)
- **MULTI_TOOL_REQUIRED:** Required tools list (Cursor,VS_Code,AntiGravity)
- **TOOLS_INSTALLED:** Currently installed tools
- **COMPLIANCE_STATUS:** compliant/partial/non_compliant/unknown
- **LAST_LOGIN_LOGGED:** Timestamp of last tracking entry
- **VIOLATIONS_COUNT:** Number of violations
- **UPDATED:** Last update date (YYYY-MM-DD)

---

## Usage Guidelines

### For Daily Updates

1. **Always work with `DISTRIBUTION_CURRENT.csv`**
2. **Never edit daily snapshots** (they are historical records)
3. **Create daily snapshot before major changes** (for rollback capability)

### For Compliance Monitoring

1. **Check `DISTRIBUTION_CURRENT.csv` for real-time status**
2. **Compare daily snapshots to track trends:**
   ```bash
   # Compare yesterday to today
   diff daily/2025-12/DISTRIBUTION_2025-12-10.csv daily/2025-12/DISTRIBUTION_2025-12-11.csv
   ```

### For Historical Analysis

1. **Use daily snapshots in `daily/YYYY-MM/`**
2. **Track compliance improvements over time**
3. **Generate weekly/monthly reports from snapshots**

---

## Automation Scripts

### Create Daily Snapshot (Python)

```python
import os
import shutil
from datetime import datetime

def create_daily_snapshot():
    today = datetime.now().strftime('%Y-%m-%d')
    year_month = datetime.now().strftime('%Y-%m')

    current = 'DISTRIBUTION/DISTRIBUTION_CURRENT.csv'
    daily = f'DISTRIBUTION/daily/{year_month}/DISTRIBUTION_{today}.csv'

    # Create month folder if needed
    os.makedirs(f'DISTRIBUTION/daily/{year_month}', exist_ok=True)

    # Copy current to daily
    shutil.copy2(current, daily)
    print(f'Daily snapshot created: {daily}')

if __name__ == '__main__':
    create_daily_snapshot()
```

### Check Compliance Changes

```python
import csv

def compare_distributions(file1, file2):
    # Read both files
    with open(file1) as f1, open(file2) as f2:
        reader1 = csv.DictReader(f1)
        reader2 = csv.DictReader(f2)

        data1 = {row['EMPLOYEE_NAME']: row for row in reader1}
        data2 = {row['EMPLOYEE_NAME']: row for row in reader2}

    # Find changes
    for emp_name in data1.keys():
        if emp_name in data2:
            if data1[emp_name]['COMPLIANCE_STATUS'] != data2[emp_name]['COMPLIANCE_STATUS']:
                print(f"{emp_name}: {data1[emp_name]['COMPLIANCE_STATUS']} -> {data2[emp_name]['COMPLIANCE_STATUS']}")
```

---

## Integration Points

### With limits_tracking.csv
- LAST_LOGIN_LOGGED updated from limits_tracking.csv entries
- VIOLATIONS_COUNT calculated from missing tracking entries

### With ACCOUNT_TRACKING_RULES.md
- COMPLIANCE_STATUS follows rules defined in enforcement document
- MULTI_TOOL_REQUIRED matches requirements in rules

### With Employee Registry
- EMPLOYEE_NAME, DEPT_CODE, FOLDER_PATH synced with registry
- ACTIVE status updated from registry scans

---

## Retention Policy

### Daily Snapshots
- **Keep:** All snapshots from current month + last 3 months
- **Archive:** Snapshots older than 3 months (monthly summary only)
- **Delete:** Snapshots older than 1 year (unless flagged as important)

### Monthly Summaries
- First day of month snapshot kept permanently
- Last day of month snapshot kept permanently

---

## Backup Strategy

1. **Daily:** Automated snapshot creation (stored in daily/)
2. **Weekly:** Full folder backup to external location
3. **Monthly:** Archive snapshot to long-term storage

---

## Troubleshooting

### If DISTRIBUTION_CURRENT.csv is corrupted
1. Find most recent daily snapshot
2. Copy to DISTRIBUTION_CURRENT.csv
3. Verify data integrity
4. Resume normal operations

### If daily snapshot is missing
1. Use DISTRIBUTION_CURRENT.csv as reference
2. Recreate missing snapshot (mark as reconstructed)
3. Continue daily workflow

---

## Change Log

```csv
DATE,CHANGE,REASON,AUTHOR
2025-12-11,Initial creation,Restructure from single DISTRIBUTION_MASTER.csv,System
2025-12-11,Added daily snapshot system,Better version control and history tracking,System
```

---

## Cross-References

- [ACCOUNT_TRACKING_RULES.md](../../DEC_25/EXC/System/ACCOUNT_TRACKING_RULES.md)
- [Employee Registry](../../DEC_25/EXC/EMP_002_Niko_Kar/DAILIES/Week_02/10/output/employee_registry.csv)
- [limits_tracking.csv](../limits_tracking.csv)

---

**END DISTRIBUTION SYSTEM README**
