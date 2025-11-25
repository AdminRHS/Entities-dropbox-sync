# Discord Voice Activity Report - November 18, 2025

**Generated:** 2025-11-19 21:59:13

**Data Source:** `attendance_report_2025-11-18.json`


---

## Executive Summary

- **Total Employees with Voice Activity:** 15
- **Successfully Matched:** 15
- **Unknown Discord IDs:** 0

## ⚠️ Data Limitations

**IMPORTANT:** The Discord log file contains only **aggregated totals** (total minutes/hours per user), not individual JOIN/LEAVE events with timestamps.

- Individual session start/end times are **not available** in the source data
- Only total voice time per employee for the entire day is available
- Session reconstruction (JOIN/LEAVE pairing) **cannot be performed** with current data

---

## Summary: Total Voice Hours per Employee

| Employee Name | Discord ID | Discord Username | Total Voice Hours (2025-11-18) |
|---------------|------------|------------------|-------------------------------|
| Davlatmamadova Firuza | 1336629524627980351 | firuza_d | 6.17 |
| Azar I | 349178900267663361 | azer_imm | 5.17 |
| Hanan Zaheur | 1420822057779859488 | hany_404 | 4.38 |
| D Stan | 541338927387377664 | .deliri | 3.25 |
| Daria Y | 934019087946899476 | eliseeva | 1.58 |
| Anastasia B | 923207596670849024 | anastasiia_berdychevska | 1.25 |
| Bridget A | 1401498823171506291 | bridgetttte | 1.2 |
| Evgeniya N | 1340934988656541736 | nealovayevheniia_13403 | 1.07 |
| Hlushko Mariia | 660069181328457728 | mariahlushko | 1.05 |
| Klimenko Yaroslav | 1401622142172532756 | 333pmcentral | 1.02 |
| Perederii Vladislav | 1381247747650486312 | vladislav_0530 | 1.0 |
| Yuliia S | 859719934287151104 | yulia_shtepa | 0.95 |
| Azanova Darʼya | 1285110685092675608 | _daria_27 | 0.57 |
| Sergii T | 787808546288435231 | sergiitodoriuk | 0.5 |
| Podolskyi Sviatoslav | 918515751177060363 | svyatpodolsky | 0.05 |

---

## Data Sources Used

1. **Discord Voice Log:** `C:\Users\victo\Dropbox\ENTITIES\TALENTS\Employees\Voice Log Discord\attendance_report_2025-11-18.json`
2. **Employee Audit File:** `C:\Users\victo\Dropbox\ENTITIES\TALENTS\Employees\merged final report\final_audit_2025-11-18.json`
3. **Employee Profiles:** `C:\Users\victo\Dropbox\ENTITIES\TALENTS\Employees\profiles`

## Matching Methodology

1. Discord IDs from voice logs were matched against:
   - Discord IDs in `final_audit_2025-11-18.json` (Discord ID → Employee Name)
   - Discord IDs in employee profile files (`profiles/*.md`)
2. If a Discord ID matched, the employee name was assigned
3. If no match was found, the ID was marked as UNKNOWN

## Assumptions

- All voice activity times are for November 18, 2025 (as indicated by the file date)
- Total hours are calculated from total minutes: `hours = minutes / 60`
- Hours are rounded to 2 decimal places
- If a Discord ID appears in logs but not in profiles/audit, it's marked as UNKNOWN

---

## Final Summary

### ✅ Successfully Completed

1. **Discord ID Matching:** 15/15 employees successfully matched (100% match rate)
   - All Discord IDs from voice logs were matched to employee names
   - Matching sources: `final_audit_2025-11-18.json` and employee profile files

2. **Total Voice Time Calculation:** All employees have calculated total voice hours
   - Hours calculated from total minutes with 2 decimal precision
   - Data sorted by total hours (descending)

3. **Data Sources Identified:**
   - Primary Discord log: `attendance_report_2025-11-18.json`
   - Employee mapping: `final_audit_2025-11-18.json` + profile files
   - All data sources verified and accessible

### ❌ Limitations & Missing Data

1. **Individual JOIN/LEAVE Events:** NOT AVAILABLE
   - The Discord log file contains only aggregated totals (total minutes per user)
   - Individual session start/end timestamps are not stored
   - Cannot reconstruct detailed session timeline (JOIN → LEAVE pairs)
   - Cannot create detailed session table with individual join/leave times

2. **Raw Discord Event Logs:** NOT FOUND
   - Searched entire Dropbox for raw Discord event files
   - No files containing individual JOIN/LEAVE events with timestamps found
   - The n8n workflow code shows how events could be extracted, but raw logs aren't saved

### 📊 Data Quality

- **Match Rate:** 100% (15/15 employees matched)
- **Data Completeness:** Complete for aggregated totals
- **Data Accuracy:** High (verified against audit file)
- **Confidence Level:** HIGH for total hours, N/A for individual sessions (data not available)

### 🔍 Files Searched

1. `ENTITIES\TALENTS\Employees\Voice Log Discord\attendance_report_2025-11-18.json` ✓ Found
2. `ENTITIES\TALENTS\Employees\merged final report\final_audit_2025-11-18.json` ✓ Found
3. `ENTITIES\TALENTS\Employees\profiles\` ✓ Found (58 profile files scanned)
4. Raw Discord event logs ✗ Not found (searched entire Dropbox)
5. `Finance\November\public\` ✗ Directory does not exist

### 📝 Notes

- "D Stan" (Discord ID: 541338927387377664) was matched from `final_audit_2025-11-18.json` but has no CRM records (marked as "CHECK CRM" in audit)
- All other employees have both Discord voice activity and CRM attendance records
- The analysis is complete and accurate based on available data sources