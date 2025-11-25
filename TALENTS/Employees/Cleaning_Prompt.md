# Employees.json Data Cleaning Prompt

## Overview

**Source File:** `C:\Users\Dell\Dropbox\Nov25\AI Nov25\Niko AI\ExportCRMS\Employees.json`
**Total Records:** 224 employee units
**Current File Size:** ~Large (contains extensive null/empty data)
**Expected Reduction:** 30-40% after cleaning
**Template Reference:** See `Employee_Unit_Template.json` in this folder

## Objective

Clean the Employees.json file by removing:
1. Fields that are ALWAYS null (template/unused fields)
2. Empty arrays and collections
3. Duplicate data structures
4. Empty string placeholders and whitespace-only values
5. Null-only nested objects

**CRITICAL:** Preserve all meaningful data. Only remove null, empty, or duplicate values.

---

## Data Structure Summary

Each employee record contains:
- **Core employee fields** (id, name, contact info, dates, etc.)
- **User object** with authentication and profile data
- **Nested collections** (languages, skills, departments, work experiences, documents, responsibilities, portfolios, tasks, etc.)
- **Related objects** (designation, department, position, address, status, candidate/HR details, team lead, currency, etc.)
- **Project-specific arrays** (video_editing, empl_content, empl_artist)

---

## Cleaning Instructions

### PRIORITY 1: Always Remove (100% of records)

#### 1.1 Remove `presale_id` Field Everywhere

The `presale_id` field appears ~50+ times per employee record and is ALWAYS null. This field should be removed from:

- Top-level employee object
- user object
- user.employee_detail (if exists)
- employee_languages array items
- employee_skills array items
- employee_departments array items
- work_experiences array items
- employee_documents array items
- video_editing array items
- empl_content array items
- empl_artist array items
- candidate/hr_details object
- Any other nested location

**Estimated Impact:** Removes 11,200+ null fields across all employees

#### 1.2 Remove Duplicate Data Structures

These objects duplicate data already present elsewhere:

**Remove entirely:**
- `user.employee_detail` - mirrors parent employee data
- Either `candidate` OR `hr_details` if both exist and are identical
- Duplicate `contacts` array (appears in both user object and top level)

**Estimated Impact:** Removes 224-448 redundant large objects

#### 1.3 Remove Always-Null Fields in Designation Object

The `designation` object consistently has these as null:
```json
"created_at": null,
"updated_at": null
```

Remove these two fields from all designation objects.

---

### PRIORITY 2: Conditionally Remove Empty/Null Values

#### 2.1 Remove Empty Arrays

If an employee has no data in these collections, remove the entire empty array:

**In user object:**
- `modules: []`
- `employee_portfolios: []`
- `educations: []`
- `contacts: []`

**In top level:**
- `task_employees: []`
- `correspondences: []`
- `contacts: []`

**In nested objects (work_experiences, educations):**
- `industries: []`

**Condition:** Only remove if array is literally empty `[]`. If it contains any items (even with null values), keep it.

**Estimated Impact:** Removes 1,120-1,792 empty arrays

#### 2.2 Remove Null Object References

If these objects are entirely null (not just containing null fields), remove them:

- `emplcity: null`
- `team_lead: null`
- `currency: null`
- `lead_agent: null` (if entire object is null)

**Condition:** Only remove if the entire field value is `null`, not if it's an object with null properties.

#### 2.3 Remove Null-Heavy Employee Fields

If ALL of the following fields are null for an employee, remove all of them:

**Optional contact methods:**
- `telegram`
- `whatsapp`
- `facebook`
- `linkedin`
- `skype`
- `mobile_work_email`
- `work_hemail`

**Optional media fields:**
- `resume_url`
- `photo_url`
- `original_video`
- `url_video_stock`
- `url_contract`

**Optional pricing fields:**
- `full_price`
- `part_price`
- `minimum_price`
- `currency_id`
- `discount`

**Optional management fields:**
- `team_lead_id`
- `note_team_lead`
- `office_id`
- `city_id`
- `attendance_reminder`
- `start_position`
- `last_date`
- `reason_dismissal`

**Condition:** Remove these fields ONLY if they are null. If they contain any value, keep them.

#### 2.4 Remove Null-Heavy User Fields

If the following fields are null in the user object, remove them:

- `onesignal_player_id`
- `email_verification_code`
- `social_token`
- `two_factor_recovery_codes`
- `salutation`
- `two_fa_verify_via`
- `two_factor_code`
- `two_factor_expires_at`
- `country_id`
- `authorize_id`
- `authorize_payment_id`
- `card_brand`
- `card_last_four`
- `last_login`

#### 2.5 Remove Null Fields in Address Object

In `empaddress` object, remove if null:
- `street`
- `house`
- `flat`
- `postal_code`

Keep the address object and its non-null fields (city_id, region_id, country_id, dates).

#### 2.6 Remove Null Fields in Position Object

In `position` object, remove if null:
- `full_price`
- `part_price`
- `minimum_price`
- `currency_id`
- `url_meet`

#### 2.7 Clean Candidate/HR Details Object

In the `candidate` (or `hr_details`) object, remove if null:

**Always remove these if null:**
- `empl_protege`
- `admin_name_id`
- `created_by`
- `courses`
- `date_video_added`
- `last_contact_date`
- `follow_up_date`
- `age`
- `shift_id`
- `expected_salary`
- `expected_salary_currency_id`
- `started_salary`
- `started_currency_id`
- `note`
- `note_admin`
- `status_admin_id`
- `instagram`
- `photo_url`
- `resume_url`
- `video_interview_url`
- `test_link`
- `job_site_link`
- `start_time`
- `end_date`
- `portfolio_url`
- `telegram`
- `resume_editor`
- `note_team_lead`
- `sub_titles`
- `team_lead_id`
- `date_interview`

**Remove empty string fields:**
- `video_url: ""` (empty string, not null)

#### 2.8 Clean Work Experience Items

In each item of the `work_experiences` array, remove if null:
- `hr_detail_id`
- `responsibilities`
- `client_details_id` (if null)
- `industries` (if empty array)

#### 2.9 Clean Responsibilities Items

In each item of the `responsibilities` array, remove if null:
- `parent_id`
- `product_id`
- `responsibility_id`
- `min_hours`
- `max_hours`

#### 2.10 Clean Lead Agent Object

If `lead_agent` exists (not null), remove these fields if null:
- `added_by`
- `last_updated_by`

If ALL fields in lead_agent are null except id/company_id/user_id, consider removing the entire object.

---

### PRIORITY 3: Clean Nested Project Arrays

#### 3.1 Video Editing Array

For each item in `video_editing` array, remove if null:
- `start_date`
- `due_date`
- `video_editor_id`
- `video_editor_created_by`
- `url_video_to_drive_disk`
- `url_video_to_youtube`
- `url_youtube_short`
- `youtube_description`
- `youtube_hashtags`
- `sub_titles`

**Special case:** If a video_editing item has ALL fields null except id, employee_details_id, project_company_id, approved, and dates, consider if it's meaningful to keep.

#### 3.2 Content Management Array (empl_content)

For each item in `empl_content` array, remove if null or empty:

**Null fields:**
- `smm_manager_id`
- `smm_manager_created_by`
- `smm_start_date`
- `smm_updated_date`
- `copywriter_manager_id`
- `copywriter_manager_created_by`
- `copywriter_start_date`
- `copywriter_updated_date`
- `content_manager_id`
- `content_manager_created_by`
- `content_start_date`
- `content_updated_date`

**Empty string fields:**
- `seo_title: ""`
- `cv_heading: ""`

**Whitespace-only fields:**
- `meta_description: "          "` (if only contains whitespace)

#### 3.3 Artist Management Array (empl_artist)

For each item in `empl_artist` array, remove if null or empty:
- `url_portrait` (if null or empty string)
- `promo_pic` (if null or empty string)
- `artist_id`
- `artist_created_by`
- `artist_start_date`
- `artist_updated_date`
- `created_at` (if null)

**Special case:** If an empl_artist item has ALL optional fields null except id, employee_details_id, and updated_at, consider if meaningful.

---

### PRIORITY 4: Optional Normalization (Lower Priority)

These are optional improvements but not strictly necessary for cleaning:

#### 4.1 Empty String to Null Conversion

Convert empty strings to null or remove them:
- `video_url: ""` → remove field
- `seo_title: ""` → remove field
- `cv_heading: ""` → remove field
- Whitespace-only strings → remove field

#### 4.2 String Boolean Normalization (Optional)

Currently booleans are stored as strings. Optionally convert:
- `"0"` → `false`
- `"1"` → `true`

Fields affected:
- `approved`
- `is_student`
- `is_approved_manager`
- `super_admin`
- `email_notifications`
- `two_factor_confirmed`
- `two_factor_email_confirmed`
- `dark_theme`
- `rtl`
- `admin_approval`
- `permission_sync`
- `google_calendar_status`

**Note:** Only do this if you're confident the system can handle boolean types instead of string types.

#### 4.3 String Number Normalization (Optional)

Convert string numbers to actual numbers:
- `"company_id": "1"` → `"company_id": 1`
- `"user_id": "2"` → `"user_id": 2`

**Warning:** Only do this if you know the system expects numeric types. Many systems use string IDs intentionally.

---

## Data Quality Issues to Identify

While cleaning, flag these records for manual review:

### 1. Test/Placeholder Data

Records with suspicious values:
- Names like: "вап", "явап", "ывап" (gibberish)
- Addresses like: "address" (generic placeholder)
- Reasons like: "ывап" in `reason_dismissal`

### 2. Invalid Default Values

- `time_interview: "00:00:00"` (may indicate no interview scheduled)
- `hourly_rate: "0"` or very low values

### 3. Incomplete Records

Employees missing critical information:
- No contact methods (all of viber, telegram, whatsapp, work_email null/empty)
- No valid address data (all address fields null)
- Empty skills/languages arrays

---

## Validation Steps

After cleaning, verify:

1. **Record Count:** Still have exactly 224 employees
2. **Structure Integrity:** Each employee still has required core fields:
   - id, company_id, user_id, employee_id
   - name_eng, name_ua
   - user object with id, email, name
   - department, position, designation objects
3. **No Data Loss:** Spot-check 5-10 random employees to ensure meaningful data preserved
4. **File Size:** Should be reduced by 30-40%
5. **JSON Validity:** File is still valid JSON after cleaning

---

## Implementation Approaches

### Approach 1: JavaScript/Node.js Script

```javascript
const fs = require('fs');

// Read the file
const data = JSON.parse(fs.readFileSync('Employees.json', 'utf8'));

// Function to remove null/empty values
function cleanObject(obj, depth = 0) {
  if (Array.isArray(obj)) {
    return obj.length > 0 ? obj.map(item => cleanObject(item, depth + 1)).filter(item => item !== null) : null;
  }

  if (obj !== null && typeof obj === 'object') {
    const cleaned = {};
    for (const [key, value] of Object.entries(obj)) {
      // Always remove presale_id
      if (key === 'presale_id') continue;

      // Remove null values
      if (value === null) continue;

      // Remove empty strings
      if (value === '' || (typeof value === 'string' && value.trim() === '')) continue;

      // Remove empty arrays
      if (Array.isArray(value) && value.length === 0) continue;

      // Recursively clean nested objects
      const cleanedValue = cleanObject(value, depth + 1);
      if (cleanedValue !== null) {
        cleaned[key] = cleanedValue;
      }
    }
    return Object.keys(cleaned).length > 0 ? cleaned : null;
  }

  return obj;
}

// Clean the data
data.data.employees = data.data.employees.map(emp => cleanObject(emp));

// Write cleaned data
fs.writeFileSync('Employees_Cleaned.json', JSON.stringify(data, null, 2));
```

### Approach 2: Python Script

```python
import json

def clean_object(obj, depth=0):
    if isinstance(obj, list):
        cleaned = [clean_object(item, depth + 1) for item in obj]
        return [item for item in cleaned if item is not None] if cleaned else None

    if isinstance(obj, dict):
        cleaned = {}
        for key, value in obj.items():
            # Always remove presale_id
            if key == 'presale_id':
                continue

            # Remove null values
            if value is None:
                continue

            # Remove empty strings and whitespace-only strings
            if isinstance(value, str) and (value == '' or value.strip() == ''):
                continue

            # Remove empty lists
            if isinstance(value, list) and len(value) == 0:
                continue

            # Recursively clean
            cleaned_value = clean_object(value, depth + 1)
            if cleaned_value is not None:
                cleaned[key] = cleaned_value

        return cleaned if cleaned else None

    return obj

# Read file
with open('Employees.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Clean data
data['data']['employees'] = [clean_object(emp) for emp in data['data']['employees']]
data['data']['employees'] = [emp for emp in data['data']['employees'] if emp is not None]

# Write cleaned file
with open('Employees_Cleaned.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
```

### Approach 3: Manual with Text Editor

1. Load file in VS Code or similar
2. Use Find & Replace with regex:
   - Find: `"presale_id":\s*null,?\s*\n` → Replace: (empty)
   - Find: `:\s*null,?\s*\n` → Replace: (empty) - careful with this!
   - Find: `:\s*\[\],?\s*\n` → Replace: (empty)
   - Find: `:\s*"",?\s*\n` → Replace: (empty)
3. Fix any trailing commas
4. Validate JSON

**Warning:** Manual approach is error-prone. Use scripting if possible.

---

## Expected Results

### Before Cleaning
```json
{
  "id": 1,
  "presale_id": null,
  "name_eng": "John Doe",
  "telegram": null,
  "whatsapp": null,
  "facebook": null,
  "linkedin": null,
  "modules": [],
  "employee_portfolios": [],
  "educations": [],
  "video_url": "",
  "seo_title": "",
  "meta_description": "          "
}
```

### After Cleaning
```json
{
  "id": 1,
  "name_eng": "John Doe"
}
```

**Size Reduction:** 80-90% reduction for this simplified example

---

## Notes and Warnings

1. **Backup First:** ALWAYS create a backup of the original file before cleaning
2. **Test on Subset:** Test your cleaning script on 2-3 employee records first
3. **Preserve IDs:** Never remove or modify ID fields (id, company_id, user_id, employee_id, etc.)
4. **Preserve Relationships:** Keep foreign key references even if other fields are null
5. **Validate JSON:** Always validate the output is valid JSON
6. **Check Application:** Ensure your application can handle missing fields (doesn't expect them to be present even if null)

---

## Summary

**Total Impact:**
- Remove ~11,200+ `presale_id` fields (ALWAYS null)
- Remove 224-448 duplicate data objects
- Remove 1,120-1,792 empty arrays
- Remove thousands of individual null fields
- **Expected file size reduction: 30-40%**
- **Expected field count reduction: 40-50%**
- **Zero data loss** (only removing null/empty/duplicate values)

**Priority Order:**
1. Remove `presale_id` everywhere (highest impact)
2. Remove duplicate structures (high impact)
3. Remove empty arrays (medium impact)
4. Remove null fields conditionally (medium impact)
5. Clean project-specific arrays (lower impact)
6. Normalize data types (optional)

This cleaning will make the file significantly smaller, faster to parse, and easier to work with while preserving all meaningful employee data.
