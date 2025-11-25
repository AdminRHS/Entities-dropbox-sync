# Version Control Automation Script

## Purpose
This automation script handles version control for versioned files (files with version numbers like v2, v3, etc.). When a file is updated to a new version, it automatically creates the new version file and generates a version control changelog.

---

## Automation Workflow

### Step 1: Detect Version Update Request

**Trigger Conditions:**
- User mentions updating a version (e.g., "update v2 to v3", "create v3 from v2")
- File name pattern detected: `* v{number}.{ext}`
- User explicitly requests version control

**Detection Pattern:**
```
File pattern: {BASE_NAME} v{NUMBER}.{EXT}
Examples:
- "MAIN PROMPT v2.md" → BASE_NAME="MAIN PROMPT", NUMBER=2, EXT="md"
- "DEPARTMENT_GUIDE v1.md" → BASE_NAME="DEPARTMENT_GUIDE", NUMBER=1, EXT="md"
```

### Step 2: Read Base Version File

**Actions:**
1. Locate the current version file
2. Read entire file content
3. Extract version information:
   - Current version number
   - Last updated date
   - Version history section

**Example:**
```bash
# Read base file
BASE_FILE="MAIN PROMPT v2.md"
CONTENT=$(read_file "$BASE_FILE")

# Extract version info
CURRENT_VERSION=$(grep "Version:" "$BASE_FILE" | head -1)
LAST_UPDATED=$(grep "Last Updated:" "$BASE_FILE" | head -1)
```

### Step 3: Create New Version File

**Actions:**
1. Determine new version number (increment from current)
2. Create new filename: `{BASE_NAME} v{NEW_NUMBER}.{EXT}`
3. Copy base file to new version
4. Place in same directory as base file

**Example:**
```bash
# Determine new version
OLD_VERSION=2
NEW_VERSION=3

# Create new file
NEW_FILE="MAIN PROMPT v${NEW_VERSION}.md"
cp "$BASE_FILE" "$NEW_FILE"
```

### Step 4: Update Version Information in New File

**Updates Required:**
1. Version History section:
   - Update "Version:" to new version number
   - Update "Last Updated:" to current date
   - Update "Previous Version:" to old version
2. Add changelog entry for new version
3. Preserve previous version history

**Example Updates:**
```markdown
## Version History

**Version:** 3.0
**Last Updated:** November 5, 2025
**Created for:** Remote Helpers - AI-First Organization
**Previous Version:** 2.1 (October 31, 2025)

**Changes in v3.0:**
- [List of changes]

---

**Previous Version Changes (v2.1 - October 31, 2025):**
[Previous changelog]
```

### Step 5: Apply Requested Updates

**Process:**
1. Read user's update requirements
2. Apply changes to new version file
3. Update relevant sections
4. Ensure consistency across document

**Common Updates:**
- Adding new sections
- Updating tool lists
- Modifying vocabulary
- Enhancing instructions
- Updating examples

### Step 6: Create/Update Version Control File

**Location:** `/Users/nikolay/Library/CloudStorage/Dropbox/Version control/`

**File Naming:**
- Extract base name from versioned file
- Format: `VC {BASE_NAME}.md`
- Example: `MAIN PROMPT v2.md` → `VC MAIN PROMPT.md`

**File Structure:**
```markdown
# Version Control: {BASE_NAME}

## File Information
**File Name:** {BASE_NAME}
**Location:** {FILE_PATH}
**Current Version:** v{NEW_VERSION}
**Last Updated:** {CURRENT_DATE}

---

## Version History

### Version {NEW_VERSION} → Current
**Date:** {CURRENT_DATE}
**Previous Version:** {OLD_VERSION} ({OLD_DATE})

#### Changelog {OLD_VERSION} → {NEW_VERSION}

[Detailed changelog with categories and changes]

#### Files Created/Modified
- **Created:** {NEW_FILE_PATH}
- **Modified:** {MODIFIED_FILES}

#### Integration Points
[Related files or systems affected]

---

### Version {OLD_VERSION}
[Previous changelog preserved]

---

## Version Control Automation

**Automation Created:** {AUTOMATION_DATE}
**Process:** [Description of automation workflow]
**Future Updates:** [Guidelines for future use]
```

### Step 7: Generate Changelog Entry

**Changelog Format:**
```markdown
**{EMOJI} {CATEGORY}: {Title}**
- Detailed change description
- Specific sections modified (with line numbers if significant)
- Impact and integration points

**📚 Enhanced Section X** - Description
**🔧 Updated Section Y** - Description
**📝 Added Section Z** - Description
**📋 Removed Section W** - Description
```

**Categories:**
- 🛠️ MAJOR: Significant feature additions
- 📚 Enhanced: Section improvements
- 🔧 Updated: Content modifications
- 📝 Added: New content
- 📋 Removed: Deleted content
- ✨ Updated: Minor improvements

---

## Implementation Example

### Example: MAIN PROMPT v2 → v3

**Input:**
- Base file: `MAIN PROMPT v2.md`
- User request: "Update with comprehensive AI tools directory and create v3"

**Process:**
1. Read `MAIN PROMPT v2.md`
2. Create `MAIN PROMPT v3.md`
3. Update version info in v3
4. Add comprehensive AI tools directory to Section 8
5. Update Core Operating Systems section
6. Update Company-Specific Vocabulary
7. Create/update `Version control/VC MAIN PROMPT.md`
8. Add changelog entry v2.1 → v3.0

**Output Files:**
- `MAIN PROMPT v3.md` (new version)
- `Version control/VC MAIN PROMPT.md` (updated changelog)

---

## Automation Script Template

```bash
#!/bin/bash

# Version Control Automation Script
# Usage: ./version-control.sh <base_file> <update_description>

BASE_FILE="$1"
UPDATE_DESC="$2"

# Extract base name and version
BASE_NAME=$(echo "$BASE_FILE" | sed 's/ v[0-9]*\.[0-9]*//' | sed 's/\.[^.]*$//')
OLD_VERSION=$(echo "$BASE_FILE" | grep -oP 'v\d+\.\d+' | head -1)
NEW_VERSION=$(echo "$OLD_VERSION" | awk -F. '{print $1"."($2+1)}')

# Create new version file
NEW_FILE="${BASE_NAME} v${NEW_VERSION}.md"
cp "$BASE_FILE" "$NEW_FILE"

# Update version info in new file
sed -i "s/Version:.*/Version: ${NEW_VERSION}/" "$NEW_FILE"
sed -i "s/Last Updated:.*/Last Updated: $(date +"%B %d, %Y")/" "$NEW_FILE"

# Create/update VC file
VC_FILE="Version control/VC ${BASE_NAME}.md"
# [Add changelog generation logic]

echo "Created ${NEW_FILE}"
echo "Updated ${VC_FILE}"
```

---

## Usage Instructions for AI Assistant

When user requests version update:

1. **Identify the versioned file**
   - Look for files matching pattern `* v{number}.{ext}`
   - Confirm with user if multiple matches

2. **Read base version file**
   - Read entire file content
   - Extract version information

3. **Create new version file**
   - Copy base file
   - Update version number
   - Place next to base file

4. **Apply requested updates**
   - Make changes as specified by user
   - Update relevant sections
   - Maintain consistency

5. **Update version history**
   - Add changelog entry in new file
   - Preserve previous history

6. **Create/update VC file**
   - Locate or create VC file in Version control folder
   - Add new changelog entry at top
   - Preserve previous entries

7. **Log to department prompt log**
   - Document the version control process
   - Include file paths and changes made

---

## File Structure

```
Dropbox/
├── MAIN PROMPT v2.md          (Base version)
├── MAIN PROMPT v3.md          (New version)
└── Version control/
    └── VC MAIN PROMPT.md      (Version control changelog)
```

---

## Best Practices

1. **Always preserve history** - Never delete previous version entries
2. **Be specific** - Document exact changes, not just "updated"
3. **Include context** - Note why changes were made
4. **Link related files** - Document integration points
5. **Use consistent format** - Follow changelog template
6. **Update both files** - Version file AND VC file must be updated
7. **Chronological order** - Newest changes first in VC file

---

## Troubleshooting

**Issue: Multiple version files found**
- Ask user which file to update
- Check file modification dates
- Use most recent version as base

**Issue: VC file doesn't exist**
- Create new VC file with header structure
- Initialize with current version entry

**Issue: Version number unclear**
- Extract from "Version:" field in file
- If missing, infer from filename
- Confirm with user if ambiguous

---

**Last Updated:** November 5, 2025  
**Maintained By:** Version Control Automation System

