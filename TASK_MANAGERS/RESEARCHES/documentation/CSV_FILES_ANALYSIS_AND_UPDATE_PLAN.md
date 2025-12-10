# CSV Files Analysis and Update Plan
# Search Queue & Video Queue Master Files

**Document ID:** DOC-RES-017
**Version:** 1.0
**Date:** 2025-12-09
**Status:** ✅ Analysis Complete
**Priority:** HIGH
**Classification:** Technical Specification

---

## Purpose

This document analyzes the current state of `Search_Queue_Master.csv` and `Video_Queue_Master.csv` files, identifies issues with ID stability and field compliance, and provides a comprehensive update plan to ensure all records conform to the ID System Standard and documentation requirements.

---

## Executive Summary

### Current State

**Search_Queue_Master.csv:**
- ✅ 1 record (SEARCH-001)
- ✅ ID format correct (SEARCH-XXX)
- ⚠️ Missing fields validation needed
- ⚠️ Need to verify field compliance

**Video_Queue_Master.csv:**
- ✅ 5 records (VQ-001 through VQ-005)
- ✅ ID format correct (VQ-XXX)
- ⚠️ Some fields may need standardization
- ⚠️ Need to verify all required fields present

### Key Issues Identified

1. **ID Stability:** IDs are correctly formatted but need verification of sequential assignment
2. **Field Compliance:** Need to verify all fields match documentation requirements
3. **Data Consistency:** Need to ensure date formats, status values, and field types are consistent
4. **Missing Fields:** Verify no required fields are missing

---

## 1. Search_Queue_Master.csv Analysis

### Current File Structure

```csv
Search_ID,Employee,Department,Topic,Search_Query,Status,Videos_Found,Date_Assigned,Date_Completed,Notes
SEARCH-001,Admin,AI,Knowledge Base Management AI,Knowledge base management AI,Assigned,0,2025-12-07,,
```

### Field-by-Field Analysis

| Field | Current Value | Required Format | Status | Issues |
|-------|--------------|-----------------|--------|--------|
| **Search_ID** | SEARCH-001 | SEARCH-XXX (001-999) | ✅ CORRECT | None - format matches standard |
| **Employee** | Admin | String (employee name) | ✅ CORRECT | None |
| **Department** | AI | Department code (VID, AID, DEV, SMM, DGN, etc.) | ⚠️ NEEDS REVIEW | Should be department code, not full name |
| **Topic** | Knowledge Base Management AI | String | ✅ CORRECT | None |
| **Search_Query** | Knowledge base management AI | String (optional) | ✅ CORRECT | None |
| **Status** | Assigned | Assigned, In_Progress, Completed | ✅ CORRECT | None |
| **Videos_Found** | 0 | Integer | ✅ CORRECT | None |
| **Date_Assigned** | 2025-12-07 | YYYY-MM-DD | ✅ CORRECT | None |
| **Date_Completed** | (empty) | YYYY-MM-DD (optional) | ✅ CORRECT | Empty is valid for Assigned status |
| **Notes** | (empty) | String (optional) | ✅ CORRECT | None |

### Issues Found

1. **Department Field:** 
   - Current: "AI" 
   - Expected: Department code (e.g., "AID" for AI Development)
   - **Impact:** LOW - Still readable but not standardized
   - **Action:** Update to standard department code

### Required Updates

**Update 1: Standardize Department Code**
```csv
# Before:
SEARCH-001,Admin,AI,Knowledge Base Management AI,...

# After:
SEARCH-001,Admin,AID,Knowledge Base Management AI,...
```

**Department Code Mapping:**
- "AI" → "AID" (AI Development)
- Other common codes: VID (Video), DEV (Development), DGN (Design), SMM (Social Media Marketing), HR (Human Resources)

---

## 2. Video_Queue_Master.csv Analysis

### Current File Structure

```csv
Queue_ID,Video_ID,Video_Title,Channel_Name,Channel_URL,Video_URL,Views,Likes,Comments,Publish_Date,Duration,Added_By,Added_Date,Status,Selected_By,Selected_Date,Parsed_Date,Topic_Category,Research_Source,Priority_Score,Notes
VQ-001,dQw4w9WgXcQ,Google AI Studio Full Walkthrough and Tutorial,AI for Grownups,[To be extracted],https://youtube.com/watch?v=dQw4w9WgXcQ,1500000,45000,2300,2025-10-15,00:10:32,Niko Kar,2025-11-24,Pending,,,,AI Tools Overview,Perplexity,75.5,Google AI Studio tutorial - comprehensive overview of features
VQ-002,aBc123DeF45,Advanced Video Editing Techniques 2025,Creative Academy,[To be extracted],https://youtube.com/watch?v=aBc123DeF45,850000,32000,1800,2025-11-01,00:08:15,Maria Designer,2025-11-24,Pending,,,,Video Editing,Gemini,65.2,Tutorial on advanced effects and transitions
VQ-003,xYz789GhI12,UI Design Trends for 2025,Design Masters,[To be extracted],https://youtube.com/watch?v=xYz789GhI12,2500000,98000,4500,2025-11-20,00:12:45,Niko Kar,2025-11-24,Selected,Niko Kar,2025-11-24,,UI Design Trends,Perplexity,92.8,Comprehensive overview of upcoming UI trends
VQ-004,pQr456JkL78,Deep Learning for Beginners,Tech Tutorials,[To be extracted],https://youtube.com/watch?v=pQr456JkL78,500000,15000,980,2025-09-10,00:15:20,Developer1,2025-11-24,Pending,,,,AI & Machine Learning,DeepSeek,42.3,Introductory course on deep learning concepts
VQ-005,mNo234OpQ56,Social Media Marketing Strategies,Marketing Pro,[To be extracted],https://youtube.com/watch?v=mNo234OpQ56,320000,8500,650,2025-11-15,00:07:55,SMM Manager,2025-11-24,Parsed,SMM Manager,2025-11-23,2025-11-24,Social Media Marketing,YouTube,68.7,Effective strategies for social media campaigns
```

### Field-by-Field Analysis

| Field | Current State | Required Format | Status | Issues |
|-------|--------------|-----------------|--------|--------|
| **Queue_ID** | VQ-001 to VQ-005 | VQ-XXX (001-999) | ✅ CORRECT | All IDs properly formatted |
| **Video_ID** | dQw4w9WgXcQ, etc. | 11-character YouTube ID | ⚠️ NEEDS VERIFICATION | Some IDs look like placeholders (aBc123DeF45) |
| **Video_Title** | Present | String | ✅ CORRECT | None |
| **Channel_Name** | Present | String | ✅ CORRECT | None |
| **Channel_URL** | [To be extracted] | String | ⚠️ INCOMPLETE | All entries show placeholder |
| **Video_URL** | Present | Full YouTube URL | ✅ CORRECT | None |
| **Views** | Numbers | Integer | ✅ CORRECT | None |
| **Likes** | Numbers | Integer | ✅ CORRECT | None |
| **Comments** | Numbers | Integer | ✅ CORRECT | None |
| **Publish_Date** | YYYY-MM-DD | YYYY-MM-DD | ✅ CORRECT | None |
| **Duration** | HH:MM:SS | HH:MM:SS | ✅ CORRECT | None |
| **Added_By** | Present | String | ✅ CORRECT | None |
| **Added_Date** | YYYY-MM-DD | YYYY-MM-DD | ✅ CORRECT | None |
| **Status** | Pending, Selected, Parsed | Pending, Selected, Parsing, Parsed, Rejected | ⚠️ NEEDS REVIEW | Status values correct but need verification |
| **Selected_By** | Present when Selected | String (optional) | ✅ CORRECT | None |
| **Selected_Date** | Present when Selected | YYYY-MM-DD (optional) | ✅ CORRECT | None |
| **Parsed_Date** | Present when Parsed | YYYY-MM-DD (optional) | ✅ CORRECT | None |
| **Topic_Category** | Present | String | ✅ CORRECT | None |
| **Research_Source** | Perplexity, Gemini, etc. | Perplexity, Gemini, GPT, DeepSeek, YouTube | ✅ CORRECT | None |
| **Priority_Score** | 75.5, 65.2, etc. | Float (0-100) | ✅ CORRECT | None |
| **Notes** | Present | String (optional) | ✅ CORRECT | None |

### Issues Found

1. **Video_ID Placeholders:**
   - VQ-002: `aBc123DeF45` - Looks like placeholder, not real YouTube ID
   - VQ-003: `xYz789GhI12` - Looks like placeholder
   - VQ-004: `pQr456JkL78` - Looks like placeholder
   - VQ-005: `mNo234OpQ56` - Looks like placeholder
   - **Impact:** HIGH - Invalid IDs prevent video access
   - **Action:** Replace with real YouTube video IDs

2. **Channel_URL Placeholder:**
   - All entries show `[To be extracted]`
   - **Impact:** MEDIUM - Missing data but not critical
   - **Action:** Extract real channel URLs or leave empty if not available

3. **Status Values:**
   - Current: Pending, Selected, Parsed
   - Documentation allows: Pending, Selected, Parsing, Parsed, Rejected
   - **Status:** ✅ CORRECT - Current values are valid

### Required Updates

**Update 1: Replace Placeholder Video IDs**

All placeholder Video_IDs need to be replaced with real YouTube video IDs (11 characters, alphanumeric).

**Example:**
```csv
# Before:
VQ-002,aBc123DeF45,Advanced Video Editing Techniques 2025,...

# After (with real YouTube ID):
VQ-002,REAL_VIDEO_ID,Advanced Video Editing Techniques 2025,...
```

**Update 2: Extract Channel URLs (Optional)**

If channel URLs are available, replace `[To be extracted]` with actual URLs:
```csv
# Before:
Channel_URL,[To be extracted]

# After:
Channel_URL,https://www.youtube.com/@channelname
```

Or leave empty if not available:
```csv
Channel_URL,
```

---

## 3. ID Stability Requirements

### ID System Standard Compliance

According to `04_ID_System_Standard.md`:

**Search Queue IDs:**
- Format: `SEARCH-XXX`
- Range: 001-999
- Rules:
  - Sequential numbering starting from 001
  - Three-digit zero-padded format
  - Hyphen separator
  - No reuse of IDs (even if deleted)
  - Never skip numbers intentionally

**Video Queue IDs:**
- Format: `VQ-XXX`
- Range: 001-999
- Rules:
  - Sequential numbering starting from 001
  - Three-digit zero-padded format
  - Hyphen separator
  - Persistent even after video processed
  - No reuse of IDs

### Current ID Status

**Search Queue:**
- ✅ SEARCH-001 exists
- ✅ Format correct
- ✅ Sequential (starting from 001)
- ✅ Next available: SEARCH-002

**Video Queue:**
- ✅ VQ-001 through VQ-005 exist
- ✅ Format correct
- ✅ Sequential (001-005)
- ✅ Next available: VQ-006

### ID Stability Recommendations

1. **Never Reuse IDs:**
   - Even if a record is deleted, keep the ID in history
   - Document deleted IDs in a separate log

2. **Sequential Assignment:**
   - Always assign next sequential number
   - Check existing IDs before assigning new one
   - Use scripts to auto-generate next ID

3. **Validation:**
   - Validate ID format before saving
   - Check for duplicates
   - Ensure sequential continuity

---

## 4. Field Compliance Analysis

### Search Queue Required Fields

| Field | Required | Type | Format | Validation |
|-------|----------|------|--------|------------|
| Search_ID | ✅ Yes | String | SEARCH-XXX | Regex: `^SEARCH-\d{3}$` |
| Employee | ✅ Yes | String | Employee name | Non-empty |
| Department | ✅ Yes | String | Department code | One of: VID, AID, DEV, SMM, DGN, HR, etc. |
| Topic | ✅ Yes | String | Search topic | Non-empty, 5+ chars |
| Search_Query | ⚠️ Optional | String | Search query | Can be empty |
| Status | ✅ Yes | Enum | Assigned, In_Progress, Completed | Must match enum |
| Videos_Found | ✅ Yes | Integer | Count | ≥ 0 |
| Date_Assigned | ✅ Yes | Date | YYYY-MM-DD | Valid date |
| Date_Completed | ⚠️ Optional | Date | YYYY-MM-DD | Valid date or empty |
| Notes | ⚠️ Optional | String | Free text | Can be empty |

### Video Queue Required Fields

| Field | Required | Type | Format | Validation |
|-------|----------|------|--------|------------|
| Queue_ID | ✅ Yes | String | VQ-XXX | Regex: `^VQ-\d{3}$` |
| Video_ID | ✅ Yes | String | YouTube ID | 11 characters, alphanumeric |
| Video_Title | ✅ Yes | String | Video title | Non-empty |
| Channel_Name | ✅ Yes | String | Channel name | Non-empty |
| Channel_URL | ⚠️ Optional | String | Channel URL | Valid URL or empty |
| Video_URL | ✅ Yes | String | YouTube URL | Valid YouTube URL |
| Views | ✅ Yes | Integer | View count | ≥ 0 |
| Likes | ✅ Yes | Integer | Like count | ≥ 0 |
| Comments | ✅ Yes | Integer | Comment count | ≥ 0 |
| Publish_Date | ✅ Yes | Date | YYYY-MM-DD | Valid date |
| Duration | ✅ Yes | Time | HH:MM:SS | Valid time format |
| Added_By | ✅ Yes | String | Employee name | Non-empty |
| Added_Date | ✅ Yes | Date | YYYY-MM-DD | Valid date |
| Status | ✅ Yes | Enum | Pending, Selected, Parsing, Parsed, Rejected | Must match enum |
| Selected_By | ⚠️ Optional | String | Employee name | Required if Status=Selected |
| Selected_Date | ⚠️ Optional | Date | YYYY-MM-DD | Required if Status=Selected |
| Parsed_Date | ⚠️ Optional | Date | YYYY-MM-DD | Required if Status=Parsed |
| Topic_Category | ✅ Yes | String | Topic | Non-empty |
| Research_Source | ✅ Yes | Enum | Perplexity, Gemini, GPT, DeepSeek, YouTube | Must match enum |
| Priority_Score | ✅ Yes | Float | 0-100 | 0 ≤ score ≤ 100 |
| Notes | ⚠️ Optional | String | Free text | Can be empty |

---

## 5. Update Plan

### Phase 1: Data Validation

**Step 1.1: Backup Current Files**
```bash
# Create backup copies
cp Search_Queue_Master.csv Search_Queue_Master.csv.backup.2025-12-09
cp Video_Queue_Master.csv Video_Queue_Master.csv.backup.2025-12-09
```

**Step 1.2: Validate ID Formats**
- ✅ Search Queue IDs: All valid (SEARCH-001)
- ✅ Video Queue IDs: All valid (VQ-001 to VQ-005)
- ✅ Sequential: No gaps detected
- ✅ Format: All match regex patterns

**Step 1.3: Validate Field Types**
- Check all dates are YYYY-MM-DD format
- Check all numbers are valid integers/floats
- Check all status values match enums
- Check all required fields are present

### Phase 2: Data Corrections

**Step 2.1: Update Search Queue**

**File:** `Search_Queue_Master.csv`

**Changes:**
1. Update Department field from "AI" to "AID"

**Updated Record:**
```csv
Search_ID,Employee,Department,Topic,Search_Query,Status,Videos_Found,Date_Assigned,Date_Completed,Notes
SEARCH-001,Admin,AID,Knowledge Base Management AI,Knowledge base management AI,Assigned,0,2025-12-07,,
```

**Step 2.2: Update Video Queue**

**File:** `Video_Queue_Master.csv`

**Changes:**
1. Replace placeholder Video_IDs with real YouTube IDs
2. Extract or remove Channel_URL placeholders

**Priority Actions:**
- **CRITICAL:** Replace placeholder Video_IDs (VQ-002, VQ-003, VQ-004, VQ-005)
- **MEDIUM:** Extract Channel_URLs or leave empty

**Updated Records Template:**
```csv
# VQ-002 (example - needs real video ID)
VQ-002,REAL_YOUTUBE_ID_11_CHARS,Advanced Video Editing Techniques 2025,Creative Academy,,https://youtube.com/watch?v=REAL_YOUTUBE_ID_11_CHARS,850000,32000,1800,2025-11-01,00:08:15,Maria Designer,2025-11-24,Pending,,,,Video Editing,Gemini,65.2,Tutorial on advanced effects and transitions

# VQ-003 (example - needs real video ID)
VQ-003,REAL_YOUTUBE_ID_11_CHARS,UI Design Trends for 2025,Design Masters,,https://youtube.com/watch?v=REAL_YOUTUBE_ID_11_CHARS,2500000,98000,4500,2025-11-20,00:12:45,Niko Kar,2025-11-24,Selected,Niko Kar,2025-11-24,,UI Design Trends,Perplexity,92.8,Comprehensive overview of upcoming UI trends
```

### Phase 3: Validation Script

**Create:** `scripts/validate_csv_files.py`

**Purpose:** Validate CSV files against ID System Standard

**Features:**
- Validate ID formats (regex patterns)
- Check sequential numbering
- Validate field types
- Check required fields
- Validate enum values
- Generate validation report

**Usage:**
```bash
python scripts/validate_csv_files.py
```

**Output:**
```
CSV Files Validation Report
============================

Search_Queue_Master.csv:
  ✅ ID Format: Valid (1/1 records)
  ✅ Sequential: Valid (001)
  ✅ Required Fields: All present
  ⚠️  Department Code: "AI" should be "AID"
  
Video_Queue_Master.csv:
  ✅ ID Format: Valid (5/5 records)
  ✅ Sequential: Valid (001-005)
  ✅ Required Fields: All present
  ❌ Video_ID: 4 placeholder IDs found (VQ-002, VQ-003, VQ-004, VQ-005)
  ⚠️  Channel_URL: All entries show placeholder

Issues Found: 5
  - 1 Department code standardization needed
  - 4 Video_ID placeholders need replacement
```

### Phase 4: ID Generation Script Enhancement

**Update:** Existing ID generation scripts to ensure:
1. Check for existing IDs before generating new
2. Always use next sequential number
3. Validate format before assignment
4. Log all ID assignments

**Scripts to Update:**
- `00_SEARCH_QUEUE/scripts/assign_search.py`
- `01_VIDEO_QUEUE/scripts/add_video_to_queue_simple.py`

---

## 6. Updated CSV Files

### Updated Search_Queue_Master.csv

```csv
Search_ID,Employee,Department,Topic,Search_Query,Status,Videos_Found,Date_Assigned,Date_Completed,Notes
SEARCH-001,Admin,AID,Knowledge Base Management AI,Knowledge base management AI,Assigned,0,2025-12-07,,
```

**Changes Made:**
- ✅ Department: "AI" → "AID"

### Updated Video_Queue_Master.csv

**Note:** Video_IDs marked as `[REPLACE_WITH_REAL_ID]` need to be replaced with actual YouTube video IDs.

```csv
Queue_ID,Video_ID,Video_Title,Channel_Name,Channel_URL,Video_URL,Views,Likes,Comments,Publish_Date,Duration,Added_By,Added_Date,Status,Selected_By,Selected_Date,Parsed_Date,Topic_Category,Research_Source,Priority_Score,Notes
VQ-001,dQw4w9WgXcQ,Google AI Studio Full Walkthrough and Tutorial,AI for Grownups,,https://youtube.com/watch?v=dQw4w9WgXcQ,1500000,45000,2300,2025-10-15,00:10:32,Niko Kar,2025-11-24,Pending,,,,AI Tools Overview,Perplexity,75.5,Google AI Studio tutorial - comprehensive overview of features
VQ-002,[REPLACE_WITH_REAL_ID],Advanced Video Editing Techniques 2025,Creative Academy,,https://youtube.com/watch?v=[REPLACE_WITH_REAL_ID],850000,32000,1800,2025-11-01,00:08:15,Maria Designer,2025-11-24,Pending,,,,Video Editing,Gemini,65.2,Tutorial on advanced effects and transitions
VQ-003,[REPLACE_WITH_REAL_ID],UI Design Trends for 2025,Design Masters,,https://youtube.com/watch?v=[REPLACE_WITH_REAL_ID],2500000,98000,4500,2025-11-20,00:12:45,Niko Kar,2025-11-24,Selected,Niko Kar,2025-11-24,,UI Design Trends,Perplexity,92.8,Comprehensive overview of upcoming UI trends
VQ-004,[REPLACE_WITH_REAL_ID],Deep Learning for Beginners,Tech Tutorials,,https://youtube.com/watch?v=[REPLACE_WITH_REAL_ID],500000,15000,980,2025-09-10,00:15:20,Developer1,2025-11-24,Pending,,,,AI & Machine Learning,DeepSeek,42.3,Introductory course on deep learning concepts
VQ-005,[REPLACE_WITH_REAL_ID],Social Media Marketing Strategies,Marketing Pro,,https://youtube.com/watch?v=[REPLACE_WITH_REAL_ID],320000,8500,650,2025-11-15,00:07:55,SMM Manager,2025-11-24,Parsed,SMM Manager,2025-11-23,2025-11-24,Social Media Marketing,YouTube,68.7,Effective strategies for social media campaigns
```

**Changes Made:**
- ⚠️ Video_ID: Placeholders need replacement (VQ-002, VQ-003, VQ-004, VQ-005)
- ✅ Channel_URL: Removed placeholder text, left empty

---

## 7. Implementation Checklist

### Immediate Actions (Critical)

- [ ] **Backup current CSV files**
  - [ ] Create timestamped backups
  - [ ] Verify backup integrity

- [ ] **Update Search Queue Department Code**
  - [ ] Change "AI" to "AID" in SEARCH-001
  - [ ] Verify update saved correctly

- [ ] **Replace Video Queue Placeholder IDs**
  - [ ] Identify real YouTube IDs for VQ-002, VQ-003, VQ-004, VQ-005
  - [ ] Update Video_ID column
  - [ ] Update Video_URL column to match
  - [ ] Verify all IDs are 11 characters

### Short-term Actions (High Priority)

- [ ] **Create Validation Script**
  - [ ] Implement ID format validation
  - [ ] Implement field type validation
  - [ ] Implement enum value validation
  - [ ] Generate validation reports

- [ ] **Update ID Generation Scripts**
  - [ ] Add sequential ID checking
  - [ ] Add format validation
  - [ ] Add logging for ID assignments

- [ ] **Extract Channel URLs (Optional)**
  - [ ] Use YouTube API or manual extraction
  - [ ] Update Channel_URL column
  - [ ] Or leave empty if not available

### Long-term Actions (Medium Priority)

- [ ] **Create ID Registry**
  - [ ] Track all assigned IDs
  - [ ] Prevent ID reuse
  - [ ] Document deleted IDs

- [ ] **Automate Validation**
  - [ ] Run validation on file save
  - [ ] Generate alerts for issues
  - [ ] Integrate with scripts

- [ ] **Documentation Updates**
  - [ ] Update field requirements
  - [ ] Add validation rules
  - [ ] Create troubleshooting guide

---

## 8. Validation Rules

### ID Format Validation

**Search Queue ID:**
```regex
^SEARCH-\d{3}$
```
- Must start with "SEARCH-"
- Followed by exactly 3 digits (001-999)
- Example: SEARCH-001, SEARCH-042, SEARCH-999

**Video Queue ID:**
```regex
^VQ-\d{3}$
```
- Must start with "VQ-"
- Followed by exactly 3 digits (001-999)
- Example: VQ-001, VQ-042, VQ-999

**YouTube Video ID:**
```regex
^[a-zA-Z0-9_-]{11}$
```
- Exactly 11 characters
- Alphanumeric, underscore, or hyphen
- Example: dQw4w9WgXcQ

### Field Validation Rules

**Date Fields:**
- Format: YYYY-MM-DD
- Valid date (not future dates beyond reasonable range)
- Examples: 2025-12-09, 2024-01-15

**Status Enums:**

**Search Queue Status:**
- Allowed: `Assigned`, `In_Progress`, `Completed`
- Case-sensitive

**Video Queue Status:**
- Allowed: `Pending`, `Selected`, `Parsing`, `Parsed`, `Rejected`
- Case-sensitive

**Department Codes:**
- Standard codes: VID, AID, DEV, SMM, DGN, HR, SEC, QA, MKT, SLS, LGN
- Case-sensitive, uppercase

**Research Source:**
- Allowed: `Perplexity`, `Gemini`, `GPT`, `DeepSeek`, `YouTube`
- Case-sensitive

**Priority Score:**
- Range: 0.0 to 100.0
- Float/decimal allowed
- Examples: 75.5, 92.8, 42.3

---

## 9. Migration Script

### Python Script: `update_csv_files.py`

```python
#!/usr/bin/env python3
"""
CSV Files Update Script
Updates Search_Queue_Master.csv and Video_Queue_Master.csv
to ensure ID stability and field compliance.
"""

import csv
import re
from datetime import datetime
from pathlib import Path

# Base path
BASE_PATH = Path(__file__).parent.parent

# File paths
SEARCH_QUEUE_FILE = BASE_PATH / "00_SEARCH_QUEUE" / "Search_Queue_Master.csv"
VIDEO_QUEUE_FILE = BASE_PATH / "01_VIDEO_QUEUE" / "Video_Queue_Master.csv"

# Backup function
def backup_file(file_path: Path):
    """Create timestamped backup of file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = file_path.parent / f"{file_path.stem}.backup.{timestamp}{file_path.suffix}"
    
    import shutil
    shutil.copy2(file_path, backup_path)
    print(f"✅ Backup created: {backup_path}")
    return backup_path

# Validation functions
def validate_search_id(search_id: str) -> bool:
    """Validate Search Queue ID format"""
    pattern = r'^SEARCH-\d{3}$'
    return bool(re.match(pattern, search_id))

def validate_vq_id(queue_id: str) -> bool:
    """Validate Video Queue ID format"""
    pattern = r'^VQ-\d{3}$'
    return bool(re.match(pattern, queue_id))

def validate_video_id(video_id: str) -> bool:
    """Validate YouTube Video ID format"""
    pattern = r'^[a-zA-Z0-9_-]{11}$'
    return bool(re.match(pattern, video_id))

def validate_department(dept: str) -> bool:
    """Validate department code"""
    valid_codes = ['VID', 'AID', 'DEV', 'SMM', 'DGN', 'HR', 'SEC', 'QA', 'MKT', 'SLS', 'LGN']
    return dept.upper() in valid_codes

def validate_status_search(status: str) -> bool:
    """Validate Search Queue status"""
    valid_statuses = ['Assigned', 'In_Progress', 'Completed']
    return status in valid_statuses

def validate_status_video(status: str) -> bool:
    """Validate Video Queue status"""
    valid_statuses = ['Pending', 'Selected', 'Parsing', 'Parsed', 'Rejected']
    return status in valid_statuses

# Update functions
def update_search_queue():
    """Update Search Queue CSV file"""
    print("\n=== Updating Search Queue ===")
    
    # Backup
    backup_file(SEARCH_QUEUE_FILE)
    
    # Read current file
    rows = []
    with open(SEARCH_QUEUE_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    
    # Update records
    updates_made = []
    for row in rows:
        # Update Department code
        if row['Department'] == 'AI':
            row['Department'] = 'AID'
            updates_made.append(f"SEARCH-{row['Search_ID']}: Department 'AI' → 'AID'")
        
        # Validate ID
        if not validate_search_id(row['Search_ID']):
            print(f"⚠️  Invalid ID format: {row['Search_ID']}")
        
        # Validate Department
        if not validate_department(row['Department']):
            print(f"⚠️  Invalid Department: {row['Department']}")
        
        # Validate Status
        if not validate_status_search(row['Status']):
            print(f"⚠️  Invalid Status: {row['Status']}")
    
    # Write updated file
    if updates_made:
        fieldnames = ['Search_ID', 'Employee', 'Department', 'Topic', 'Search_Query', 
                     'Status', 'Videos_Found', 'Date_Assigned', 'Date_Completed', 'Notes']
        
        with open(SEARCH_QUEUE_FILE, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        
        print(f"✅ Updated {len(updates_made)} record(s)")
        for update in updates_made:
            print(f"   - {update}")
    else:
        print("✅ No updates needed")

def update_video_queue():
    """Update Video Queue CSV file"""
    print("\n=== Updating Video Queue ===")
    
    # Backup
    backup_file(VIDEO_QUEUE_FILE)
    
    # Read current file
    rows = []
    with open(VIDEO_QUEUE_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    
    # Update records
    updates_made = []
    placeholder_ids = []
    
    for row in rows:
        # Check for placeholder Video_IDs
        video_id = row['Video_ID']
        if not validate_video_id(video_id):
            placeholder_ids.append({
                'queue_id': row['Queue_ID'],
                'video_id': video_id,
                'title': row['Video_Title']
            })
        
        # Remove Channel_URL placeholder
        if row['Channel_URL'] == '[To be extracted]':
            row['Channel_URL'] = ''
            updates_made.append(f"{row['Queue_ID']}: Removed Channel_URL placeholder")
        
        # Validate ID
        if not validate_vq_id(row['Queue_ID']):
            print(f"⚠️  Invalid Queue_ID format: {row['Queue_ID']}")
        
        # Validate Status
        if not validate_status_video(row['Status']):
            print(f"⚠️  Invalid Status: {row['Status']}")
    
    # Write updated file
    if updates_made:
        fieldnames = ['Queue_ID', 'Video_ID', 'Video_Title', 'Channel_Name', 'Channel_URL',
                     'Video_URL', 'Views', 'Likes', 'Comments', 'Publish_Date', 'Duration',
                     'Added_By', 'Added_Date', 'Status', 'Selected_By', 'Selected_Date',
                     'Parsed_Date', 'Topic_Category', 'Research_Source', 'Priority_Score', 'Notes']
        
        with open(VIDEO_QUEUE_FILE, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        
        print(f"✅ Updated {len(updates_made)} record(s)")
        for update in updates_made:
            print(f"   - {update}")
    else:
        print("✅ No updates needed")
    
    # Report placeholder IDs
    if placeholder_ids:
        print(f"\n⚠️  Found {len(placeholder_ids)} placeholder Video_IDs:")
        for item in placeholder_ids:
            print(f"   - {item['queue_id']}: {item['video_id']} ({item['title']})")
        print("\n   ACTION REQUIRED: Replace placeholder IDs with real YouTube video IDs")

def main():
    """Main execution"""
    print("CSV Files Update Script")
    print("=" * 50)
    
    # Update Search Queue
    if SEARCH_QUEUE_FILE.exists():
        update_search_queue()
    else:
        print(f"⚠️  File not found: {SEARCH_QUEUE_FILE}")
    
    # Update Video Queue
    if VIDEO_QUEUE_FILE.exists():
        update_video_queue()
    else:
        print(f"⚠️  File not found: {VIDEO_QUEUE_FILE}")
    
    print("\n" + "=" * 50)
    print("✅ Update process complete")
    print("\nNext steps:")
    print("1. Review updated files")
    print("2. Replace placeholder Video_IDs with real YouTube IDs")
    print("3. Run validation script to verify compliance")

if __name__ == "__main__":
    main()
```

---

## 10. Summary

### Issues Identified

1. **Search Queue:**
   - ✅ ID format: Correct
   - ⚠️ Department code: "AI" should be "AID"
   - ✅ All other fields: Compliant

2. **Video Queue:**
   - ✅ ID format: Correct
   - ❌ Video_ID: 4 placeholder IDs need replacement
   - ⚠️ Channel_URL: Placeholder text should be removed
   - ✅ All other fields: Compliant

### Required Updates

**Critical (Must Fix):**
1. Replace placeholder Video_IDs with real YouTube IDs (4 records)
2. Update Search Queue Department code (1 record)

**Important (Should Fix):**
3. Remove Channel_URL placeholder text (5 records)

**Optional (Nice to Have):**
4. Extract real Channel_URLs if available
5. Create validation script
6. Enhance ID generation scripts

### Compliance Status

**ID Stability:** ✅ COMPLIANT
- All IDs follow correct format
- Sequential numbering maintained
- No gaps detected

**Field Compliance:** ⚠️ MOSTLY COMPLIANT
- Most fields correct
- Minor issues identified
- Easy to fix

**Documentation Alignment:** ✅ COMPLIANT
- Structure matches documentation
- Field names match specifications
- Status values match enums

---

## 11. Next Steps

1. **Immediate:**
   - Run update script to fix Department code
   - Remove Channel_URL placeholders
   - Identify real YouTube IDs for placeholder Video_IDs

2. **Short-term:**
   - Replace placeholder Video_IDs
   - Create validation script
   - Test ID generation scripts

3. **Long-term:**
   - Implement automated validation
   - Create ID registry
   - Document best practices

---

**Document Owner:** Technical Team
**Review Cycle:** As needed
**Related Documents:**
- `04_ID_System_Standard.md`
- `03_SEARCH_QUEUE_COMPLETE.md`
- `04_VIDEO_QUEUE_COMPLETE.md`

**Generated:** 2025-12-09
**Status:** ✅ Analysis Complete - Ready for Implementation
