# Daily Log - November 28, 2025

## Instructions
**What**: Record of all activities for the day  
**Include**:
- Time blocks with brief descriptions
- Results / next steps
- Any agreements with the team

---

## Activities

### Morning — Strapi Collections Export Script Enhancement (9:00-10:30)
**What I worked on:**
- Enhanced `script-collections-export.js` to automatically copy exported data to `updated/collections/` folder
- Implemented `copyToUpdated()` function that recursively copies all JSON files from `exported/collections/` to `updated/collections/`
- Added automatic synchronization after export process completes
- Ensured directory structure is preserved during copy operation

**Technical Details:**
- Function skips list files (`-list.json`) and hidden files (`.snapshot.json`)
- Maintains exact folder structure from exported to updated
- Provides statistics on copied files
- Runs automatically after snapshot creation

**Outcomes:**
- ✅ Content makers now have data automatically available in `updated/collections/` for editing
- ✅ No manual copying required after export
- ✅ Streamlined workflow for content management

---

### Morning — Collections Update Script Refactoring (10:30-12:00)
**What I worked on:**
- Completely refactored `script-collections-update.js` to work with `updated/collections/` folder
- Implemented comprehensive rate limiting (800ms delay between requests) to prevent server overload
- Added batch processing (10 files per batch) for controlled update speed
- Implemented retry logic with exponential backoff (up to 3 retries)
- Added intelligent change detection:
  - New files → POST requests
  - Modified files → PUT/PATCH requests
  - Deleted files → DELETE requests
- Fixed API endpoint mapping (singular vs plural):
  - `categories` → `category`
  - `keyword-tags` → `keyword-tag`
  - `skills` → `skill`
  - `form-users` → `form-user`

**Technical Details:**
- Rate limiting: 800ms between requests
- Batch size: 10 files
- Max retries: 3 attempts with exponential backoff
- Automatic fallback from PUT to PATCH if PUT fails
- Comprehensive error handling with detailed messages

**Outcomes:**
- ✅ Script safely handles server requests without overloading
- ✅ Automatic retry on transient errors (429, 500)
- ✅ Correct API endpoints for all collections
- ✅ Smart change detection and appropriate HTTP methods

---

### Afternoon — File Filtering and Template Handling (12:00-13:30)
**What I worked on:**
- Implemented comprehensive file filtering system:
  - Template directories (`template/`, `templates/`) are completely ignored
  - Files without ID prefix (e.g., `vacancy-template.json`) are skipped
  - Hidden files (starting with `.`) are ignored
  - List files are handled separately (for synchronization, not as collection items)
- Created `shouldIgnoreFile()` and `shouldIgnoreDirectory()` helper functions
- Added path-based filtering to catch files in template folders even if they have IDs

**Technical Details:**
- Files must start with number_ID_ pattern (e.g., `1432_polish-translator.json`)
- Template folders are skipped at directory scan level
- Path checking ensures files in `template/` subdirectories are ignored
- List files are excluded from snapshot but included in synchronization

**Outcomes:**
- ✅ Template files never sent to backend
- ✅ Only valid collection items are processed
- ✅ Clean project structure maintained

---

### Afternoon — List.json Synchronization System (13:30-15:00)
**What I worked on:**
- Implemented `syncListFiles()` function that runs before sending updates
- Created automatic synchronization of `{collection}-list.json` files:
  - Scans all files in collection folder
  - Creates/updates full list with all items (id, title, filename, slug, dates)
  - Maintains same structure as export script
- Created separate `{collection}-changed-list.json` files:
  - Contains only changed items (created/updated/deleted)
  - Includes relative paths for reference
  - Timestamped with sync date

**Technical Details:**
- Groups changes by collection and locale
- Reads file metadata to extract title, slug, dates
- Sorts items by ID for consistency
- Creates both full list and changed list files
- Ensures directories exist before writing

**Outcomes:**
- ✅ Full list.json files always synchronized before updates
- ✅ Separate tracking of changed items for reference
- ✅ Content makers can see what will be updated

---

### Afternoon — Documentation Updates (15:00-16:00)
**What I worked on:**
- Updated `README.md` for collections-update script with simple, child-friendly language
- Added comprehensive sections:
  - Quick start guide (3 steps)
  - What the script does (POST/PUT/DELETE explanation)
  - Server protection details (rate limiting, batching, retries)
  - File filtering information
  - Dry-run mode explanation
  - Troubleshooting section
- Created visual indicators and emojis for better readability
- Added checklist for safe updates

**Technical Details:**
- Simplified technical language
- Step-by-step instructions with commands
- Clear examples and visual structure
- Comprehensive error handling guide

**Outcomes:**
- ✅ Non-technical users can understand and use the script
- ✅ Clear safety guidelines (dry-run first)
- ✅ Comprehensive troubleshooting section

---

## Notes

### Key Learnings
- Rate limiting is essential for Strapi API to prevent server overload
- Batch processing provides better control over update speed
- Retry logic with exponential backoff handles transient errors gracefully
- File filtering must be comprehensive to avoid sending unwanted files
- List.json synchronization ensures data consistency

### Technical Decisions
- 800ms delay between requests balances speed and server safety
- Batch size of 10 files provides good balance
- 3 retries with exponential backoff handles most transient errors
- Template folders completely ignored at directory level
- List files synchronized but not sent as collection items

---

## Daily Report Structure

### 1️⃣ Completed Tasks
- ✅ Enhanced export script with automatic copy to updated/collections
- ✅ Refactored update script with rate limiting and retry logic
- ✅ Fixed API endpoint mapping (singular vs plural)
- ✅ Implemented comprehensive file filtering (template files, files without ID)
- ✅ Created list.json synchronization system
- ✅ Updated documentation with simple, clear instructions
- ✅ Added dry-run mode for safe testing

### 2️⃣ Challenges & Solutions
- **Challenge:** Server overload risk when sending many updates  
  **Solution:** ✅ Implemented rate limiting (800ms), batch processing (10 files), and retry logic
- **Challenge:** Incorrect API endpoints causing 405 errors  
  **Solution:** ✅ Fixed endpoint mapping to use singular forms (category, not categories)
- **Challenge:** Template files being sent to backend  
  **Solution:** ✅ Implemented comprehensive filtering (template folders, files without ID, path checking)
- **Challenge:** List.json files need synchronization before updates  
  **Solution:** ✅ Created syncListFiles() function that runs before sending updates

### 3️⃣ Tools & Software Used
- Node.js (axios for HTTP requests)
- Strapi API (https://strapi.rem-s.com)
- File system operations (fs.promises)
- Path manipulation (path module)
- JSON parsing and serialization

### 4️⃣ Plans for Tomorrow
- Test the update script with real data changes
- Verify list.json synchronization works correctly
- Gather feedback from content makers on workflow
- Consider additional safety features if needed

---

## Reminder
- Update file throughout the day after each work block
- Add results of calls/agreements immediately
- Keep script structure consistent and well-documented
- Test with dry-run mode before applying real changes
