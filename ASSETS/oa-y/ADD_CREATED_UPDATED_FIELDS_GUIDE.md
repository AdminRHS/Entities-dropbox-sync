# Guide: Adding Created and Updated Fields

**Purpose:** This document explains the pattern for adding "Created" and "Updated" date fields to all files in the oa-y_content directory.

**Created:** 2025-11-25  
**Updated:** 2025-11-25

---

## Pattern Established

### 1. Course Files

**Location:** `Courses/*.md`

**Pattern:**
Add after the URL line:
```markdown
**Created:** YYYY-MM-DD  
**Updated:** YYYY-MM-DD
```

**Example:**
```markdown
# Course Title

**Course ID:** [id]  
**Slug:** [slug]  
**URL:** [url]  
**Created:** 2025-10-27  
**Updated:** 2025-10-29
```

**Files Updated (Sample):**
- ✅ `6895eca862db728ad919c84e_Cursor-Fundamentals.md`
- ✅ `689c457e62db728ad9f2ede1_VS-Code-Fundamentals.md`
- ✅ `68ff8dc53ee727c09098a64a_Advanced-Prompting.md`
- ✅ `689c3b9c62db728ad9f1f2a1_DropBox-Fundamentals.md`

**Remaining Files:** 27 course files need to be updated

---

### 2. Listing Files

**Location:** Root directory listing files

**Pattern:**
Add after existing date fields:
```markdown
**Created:** YYYY-MM-DD  
**Updated:** YYYY-MM-DD
```

**Files Updated:**
- ✅ `Courses_Listing.md` - Added Created/Updated header, table columns added
- ✅ `Lessons/Lessons_Listing.md` - Added Created/Updated header
- ✅ `Modules/Modules_Listing.md` - Added Created/Updated header
- ✅ `Tests/Tests_Listing.md` - Added Created/Updated header
- ✅ `FILE_MAP.md` - Added Created/Updated fields

---

### 3. Lessons Listing

**Pattern:**
For each lesson entry, add Created field:
```markdown
- Created: [timestamp]
- Updated: [timestamp]
```

**Status:** Header updated, individual entries need Created field added (currently only have Updated)

---

### 4. Courses Listing Table

**Pattern:**
Table header updated to include Created and Updated columns:
```markdown
| # | Course ID | Title | Slug | Created | Updated |
```

**Status:** Header updated, table rows need Updated dates populated (currently only have Created dates from "Last Updated" column)

---

## Date Sources

### For Course Files:
- Check `Courses_Listing.md` table for "Last Updated" dates
- Use FILE_MAP.md for creation dates if available
- Default to export date (2025-11-09) if no specific date found

### For Listing Files:
- Use export date: 2025-11-09
- Or use actual file modification dates

---

## Next Steps

1. **Update remaining 27 course files** with Created/Updated fields
2. **Update Courses_Listing.md table** - Add Updated column data to all rows
3. **Update Lessons_Listing.md** - Add Created field to all lesson entries
4. **Verify consistency** across all files

---

## Script Pattern (for automation)

```bash
# Pattern to add to course files:
# Find: **URL:** [url]
# Replace: **URL:** [url]  
#         **Created:** [date]  
#         **Updated:** [date]
```

---

**Note:** Dates should be in YYYY-MM-DD format for consistency.

