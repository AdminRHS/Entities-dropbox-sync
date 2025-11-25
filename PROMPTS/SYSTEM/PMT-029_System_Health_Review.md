# System Health Review Prompt

**Purpose:** Monthly ecosystem maintenance protocol to ensure taxonomy integrity, prevent duplicates, and maintain structural consistency.

**Frequency:** Monthly (first Monday of each month)
**Duration:** 30-45 minutes
**Last Review:** [Insert Date]
**Next Review:** [Insert Date]

---

## Overview

This prompt guides a comprehensive monthly health check of the entire taxonomy ecosystem. Use this to proactively identify and resolve issues before they compound, maintaining the integrity of the ID system, file structure, and cross-references.

---

## Monthly Health Check Protocol

### Step 1: ID Integrity Scan (10 minutes)

**Objective:** Detect duplicate Tool IDs, Object IDs, Workflow IDs, and ID sequence gaps.

**Instructions for Claude:**

```
Please perform a comprehensive ID integrity scan across the entire taxonomy:

1. **Scan all Tool files** in C:\Users\Dell\Dropbox\Entities\LIBRARIES\Tools\
   - Extract all tool_id values from JSON files
   - Group by ID to identify duplicates
   - Report any duplicate Tool IDs with file paths
   - Identify gaps in ID sequences (e.g., TOOL-AI-001, 002, 005 = gap at 003-004)

2. **Scan all Object files** in C:\Users\Dell\Dropbox\Entities\LIBRARIES\Objects\
   - Extract all object_id values
   - Report duplicate Object IDs
   - Identify sequence gaps

3. **Scan all Workflow files** in C:\Users\Dell\Dropbox\Entities\LIBRARIES\Processes\Workflows\
   - Extract all workflow_id values
   - Report duplicate Workflow IDs
   - Identify sequence gaps

4. **Scan all Skill files** in C:\Users\Dell\Dropbox\Entities\LIBRARIES\Skills\
   - Extract all skill_id values
   - Report duplicate Skill IDs
   - Verify departmental prefixes (e.g., SKL-AI-001, SKL-DEV-001)

5. **Scan all Action files** in C:\Users\Dell\Dropbox\Entities\LIBRARIES\Actions\
   - Extract all action_id values
   - Report duplicate Action IDs
   - Identify sequence gaps

**Report Format:**
- Total IDs scanned per entity type
- Duplicate IDs found (if any) with file paths
- Intentional gaps (e.g., departmental skills) vs unintentional gaps
- Status: Green (0 duplicates) | Yellow (1-3 duplicates) | Red (4+ duplicates)
```

**Automation Command:**
```bash
# Future automation: Create scan_ids.py script
# For now: Manual Claude analysis
```

---

### Step 2: File Structure Audit (5 minutes)

**Objective:** Identify misplaced files and verify category organization.

**Instructions for Claude:**

```
Please audit the file structure for misplaced files:

1. **Check Tools directory:**
   - Verify all tool files are in appropriate subdirectories:
     - AI_Tools/ (TOOL-AI-xxx)
     - Development_Tools/ (TOOL-DEV-xxx)
     - Databases/ (TOOL-DB-xxx)
     - Cloud_Platforms/ (TOOL-CLOUD-xxx)
     - Authentication_Services/ (TOOL-AUTH-xxx)
     - Payment_Processing/ (TOOL-PAY-xxx)
     - Infrastructure/ (TOOL-INFRA-xxx)
     - Portfolio_Platforms/ (TOOL-PORT-xxx)
     - Publishing/ (TOOL-PUB-xxx)
     - Social_Media/ (TOOL-SMM-xxx)
     - Video_Platforms/ (TOOL-VID-xxx)
     - Web_Services/ (TOOL-WEB-xxx)
   - Report any files in Tools/ root directory
   - Verify Tool ID prefix matches subdirectory

2. **Check Objects directory:**
   - Verify files in appropriate subdirectories:
     - AI_Agents/, APIs/, Architectures/, Authentication/, Content/, Databases/,
       Deployment/, Infrastructure/, Integration/, Processes/, RAG/, Testing/, Workflows/
   - Report any files in Objects/ root directory

3. **Check Workflows directory:**
   - Verify departmental organization (if applicable)
   - Report any orphaned workflow files

4. **Check for duplicate files:**
   - Scan for same tool documented in multiple locations
   - Verify no redundant copies

**Report Format:**
- Misplaced files count with paths
- Duplicate files count with paths
- Status: Green (0 misplaced) | Yellow (1-5 misplaced) | Red (6+ misplaced)
```

---

### Step 3: Index Completeness Check (5 minutes)

**Objective:** Verify all required index files exist and are up-to-date.

**Instructions for Claude:**

```
Please verify the completeness of all index files:

**Required Indexes:**

1. **C:\Users\Dell\Dropbox\Entities\LIBRARIES\Tools\INDEX.md**
   - Must list all tool categories
   - Must show total tool count per category
   - Must include quick navigation links

2. **C:\Users\Dell\Dropbox\Entities\LIBRARIES\Objects\INDEX.md**
   - Must list all object categories
   - Must show total object count per category

3. **C:\Users\Dell\Dropbox\Entities\LIBRARIES\Processes\Workflows\INDEX.md**
   - Must list all workflow categories
   - Must show total workflow count

4. **C:\Users\Dell\Dropbox\Entities\LIBRARIES\Skills\Skills_Index.md**
   - Must list all skills by department
   - Must show total skill count (should match actual files)

5. **C:\Users\Dell\Dropbox\Entities\LIBRARIES\Actions\INDEX.md**
   - Must list all action categories
   - Must show total action count

6. **C:\Users\Dell\Dropbox\Entities\LIBRARIES\Researches\Videos\VIDEOS_INDEX.md**
   - Must list all processed videos
   - Must show completion status
   - Must reference Video Discovery Pipeline

7. **C:\Users\Dell\Dropbox\Entities\LIBRARIES\LIBRARIES_Import_Index.md**
   - Must track all import phases
   - Must show total entities created
   - Must be current (updated within last 7 days)

8. **C:\Users\Dell\Dropbox\Entities\SERVICES\INDEX.md**
   - Must list all service categories

9. **C:\Users\Dell\Dropbox\Entities\STEPS\INDEX.md**
   - Must list all step categories

10. **C:\Users\Dell\Dropbox\Entities\TASKS\INDEX.md**
    - Must list all task categories

11. **C:\Users\Dell\Dropbox\Entities\PROFESSIONS\INDEX.md**
    - Must list all profession categories

**Verification Steps:**
- Check if file exists
- If exists, verify last updated date (flag if >30 days old)
- If exists, verify counts match actual file counts
- If missing, note for creation

**Report Format:**
- Total indexes required: 11
- Indexes present: X
- Indexes missing: X (list paths)
- Indexes outdated (>30 days): X (list paths)
- Status: Green (11/11, all current) | Yellow (9-10/11 or some outdated) | Red (<9/11)
```

---

### Step 4: Cross-Reference Integrity (5 minutes)

**Objective:** Verify that referenced IDs actually exist (workflows referencing tools, tasks referencing skills, etc.).

**Instructions for Claude:**

```
Please verify cross-reference integrity across the taxonomy:

1. **Workflow → Tool References:**
   - Scan all workflow JSON files for "tools_used" arrays
   - Extract all referenced Tool IDs
   - Verify each referenced Tool ID exists in Tools directory
   - Report any broken references (workflow references non-existent tool)

2. **Workflow → Object References:**
   - Scan workflow files for "objects_used" or related object references
   - Verify each referenced Object ID exists in Objects directory
   - Report broken references

3. **Task → Skill References:**
   - Scan task files for "required_skills" arrays
   - Verify each referenced Skill ID exists in Skills directory
   - Report broken references

4. **Tool → Workflow References:**
   - Scan tool files for "workflows" arrays
   - Verify each referenced Workflow ID exists
   - Report broken references

5. **Video → Entity References:**
   - Scan video markdown files for referenced tool_ids, workflow_ids
   - Verify entities were actually created
   - Report missing entities

**Report Format:**
- Total cross-references scanned: X
- Broken references found: X (list with details)
- Status: Green (0 broken) | Yellow (1-3 broken) | Red (4+ broken)
```

---

### Step 5: Duplicate Detection (5 minutes)

**Objective:** Identify tools, workflows, or objects documented multiple times with different IDs.

**Instructions for Claude:**

```
Please scan for semantic duplicates (same entity, different IDs):

1. **Tool Name Duplicates:**
   - Extract all "name" fields from tool JSON files
   - Identify exact matches with different Tool IDs
   - Identify near-matches (e.g., "GitHub" vs "Github" vs "GitHub Platform")
   - Report duplicates with IDs and file paths

2. **Workflow Name Duplicates:**
   - Extract all "name" fields from workflow JSON files
   - Identify exact matches with different Workflow IDs
   - Report duplicates

3. **Object Name Duplicates:**
   - Extract all "name" fields from object JSON files
   - Identify exact matches with different Object IDs
   - Report duplicates

4. **Vendor/Category Inconsistencies:**
   - Scan for same vendor spelled differently (e.g., "Google" vs "Google LLC")
   - Scan for same category named differently
   - Report inconsistencies

**Report Format:**
- Duplicate tools found: X (list names and IDs)
- Duplicate workflows found: X
- Duplicate objects found: X
- Naming inconsistencies: X
- Status: Green (0 duplicates) | Yellow (1-2 duplicates) | Red (3+ duplicates)
```

---

### Step 6: Consistency Audit (5-10 minutes)

**Objective:** Verify naming conventions, formatting standards, and structural consistency.

**Instructions for Claude:**

```
Please audit consistency across the taxonomy:

1. **JSON Structure Consistency:**
   - Verify all tool files contain required fields: entity_type, sub_entity, tool_id, name, category, vendor, purpose
   - Verify all workflow files contain: workflow_id, name, description, steps
   - Verify all object files contain: object_id, name, type, description
   - Report files missing required fields

2. **Naming Convention Consistency:**
   - Tool files: Should be [Name].json (e.g., ChatGPT.json, not chatgpt.json or Chat_GPT.json)
   - Verify consistent capitalization
   - Report naming violations

3. **Category Naming Consistency:**
   - Verify Claude family uses consistent naming:
     - "Claude Sonnet 3.5" vs "Claude 3.5 Sonnet" vs "Claude Sonnet 4.5"
   - Verify category field consistency (e.g., "AI/LLM" vs "AI / LLM" vs "AI-LLM")
   - Report inconsistencies

4. **ID Format Consistency:**
   - Verify all Tool IDs follow TOOL-XXX-### pattern
   - Verify all Workflow IDs follow WF-XXX-### pattern
   - Verify all Object IDs follow OBJ-XXX-### pattern
   - Verify all Skill IDs follow SKL-XXX-### or SKL-### pattern
   - Report format violations

5. **Date Format Consistency:**
   - Verify "last_updated" or "created_date" fields use consistent format
   - Recommended: YYYY-MM-DD
   - Report inconsistencies

**Report Format:**
- Structure violations: X files
- Naming violations: X files
- Category inconsistencies: X files
- ID format violations: X
- Date format inconsistencies: X
- Status: Green (0-2 violations) | Yellow (3-10 violations) | Red (11+ violations)
```

---

## Health Score Calculation

**Overall Health Status:**

| Status | Criteria | Action Required |
|--------|----------|-----------------|
| 🟢 **GREEN** | All 6 steps Green OR 5 Green + 1 Yellow | Routine maintenance only |
| 🟡 **YELLOW** | 2-3 Yellow statuses OR 1 Red + rest Green | Schedule cleanup within 2 weeks |
| 🔴 **RED** | 2+ Red statuses OR 4+ Yellow statuses | Immediate remediation required |

**Score Breakdown:**
- Each Green = 10 points
- Each Yellow = 5 points
- Each Red = 0 points
- **Total Possible:** 60 points

**Health Grades:**
- 55-60 points: Excellent (🟢)
- 45-54 points: Good (🟡)
- 35-44 points: Fair (🟡)
- Below 35 points: Poor (🔴)

---

## Monthly Report Template

```markdown
# Taxonomy Health Report - [Month Year]

**Review Date:** [Date]
**Reviewed By:** [Name/Claude]
**Overall Health Status:** [Green/Yellow/Red]
**Overall Health Score:** [X/60 points]

---

## Executive Summary

[2-3 sentence summary of ecosystem health and any critical issues]

---

## Detailed Results

### 1. ID Integrity Scan
- **Status:** [Green/Yellow/Red]
- **Total IDs Scanned:** [Number]
- **Duplicate IDs Found:** [Number]
- **Sequence Gaps:** [Number - specify intentional vs unintentional]
- **Issues:**
  - [List any duplicate IDs with file paths]
  - [List any critical gaps]

### 2. File Structure Audit
- **Status:** [Green/Yellow/Red]
- **Misplaced Files:** [Number]
- **Duplicate Files:** [Number]
- **Issues:**
  - [List misplaced files with current and correct paths]
  - [List duplicate files]

### 3. Index Completeness Check
- **Status:** [Green/Yellow/Red]
- **Indexes Present:** [X/11]
- **Indexes Missing:** [Number]
- **Indexes Outdated:** [Number]
- **Issues:**
  - [List missing indexes]
  - [List outdated indexes with last update date]

### 4. Cross-Reference Integrity
- **Status:** [Green/Yellow/Red]
- **Total References Scanned:** [Number]
- **Broken References:** [Number]
- **Issues:**
  - [List broken references with details]

### 5. Duplicate Detection
- **Status:** [Green/Yellow/Red]
- **Duplicate Tools:** [Number]
- **Duplicate Workflows:** [Number]
- **Duplicate Objects:** [Number]
- **Naming Inconsistencies:** [Number]
- **Issues:**
  - [List duplicates with IDs and names]
  - [List naming inconsistencies]

### 6. Consistency Audit
- **Status:** [Green/Yellow/Red]
- **Structure Violations:** [Number]
- **Naming Violations:** [Number]
- **Category Inconsistencies:** [Number]
- **ID Format Violations:** [Number]
- **Date Format Inconsistencies:** [Number]
- **Issues:**
  - [List consistency violations]

---

## Trends (Compare to Last Month)

| Metric | Last Month | This Month | Change |
|--------|------------|------------|--------|
| Duplicate IDs | X | X | +/- X |
| Misplaced Files | X | X | +/- X |
| Broken References | X | X | +/- X |
| Overall Score | X/60 | X/60 | +/- X |

---

## Action Items

### High Priority (Complete within 1 week)
- [ ] [Action item 1]
- [ ] [Action item 2]

### Medium Priority (Complete within 2 weeks)
- [ ] [Action item 1]
- [ ] [Action item 2]

### Low Priority (Complete within 1 month)
- [ ] [Action item 1]
- [ ] [Action item 2]

---

## Recommendations

[List 3-5 recommendations for improving ecosystem health]

---

## Next Review

**Scheduled Date:** [First Monday of next month]
**Focus Areas:** [Any specific areas to monitor based on this month's results]

---

**Report Generated:** [Date and time]
```

---

## Automation Opportunities

### Level 1: Bash Script Automation (Implement Now)

**scan_duplicate_ids.sh:**
```bash
#!/bin/bash
# Scan for duplicate Tool IDs

echo "Scanning for duplicate Tool IDs..."
find "C:/Users/Dell/Dropbox/Entities/LIBRARIES/Tools" -name "*.json" -exec grep -h '"tool_id"' {} \; | sort | uniq -d

echo "Scanning for duplicate Workflow IDs..."
find "C:/Users/Dell/Dropbox/Entities/LIBRARIES/Processes/Workflows" -name "*.json" -exec grep -h '"workflow_id"' {} \; | sort | uniq -d

echo "Scanning for duplicate Object IDs..."
find "C:/Users/Dell/Dropbox/Entities/LIBRARIES/Objects" -name "*.json" -exec grep -h '"object_id"' {} \; | sort | uniq -d
```

**check_misplaced_files.sh:**
```bash
#!/bin/bash
# Check for files in root directories that should be in subdirectories

echo "Checking for misplaced tool files..."
ls "C:/Users/Dell/Dropbox/Entities/LIBRARIES/Tools/"*.json 2>/dev/null

echo "Checking for misplaced object files..."
ls "C:/Users/Dell/Dropbox/Entities/LIBRARIES/Objects/"*.json 2>/dev/null

echo "Checking for misplaced workflow files..."
ls "C:/Users/Dell/Dropbox/Entities/LIBRARIES/Processes/Workflows/"*.json 2>/dev/null
```

### Level 2: Python Script Automation (Plan for Future)

**health_check.py:**
- Automated ID integrity scan with detailed reporting
- Cross-reference validation
- Duplicate detection with fuzzy matching
- JSON structure validation
- Generate monthly report automatically

### Level 3: CI/CD Integration (Future Vision)

**Pre-commit Hook:**
- Validate JSON structure before commit
- Check for duplicate IDs
- Verify file placement
- Enforce naming conventions

**Monthly GitHub Action:**
- Run full health check on first of month
- Generate report as GitHub Issue
- Flag critical issues for immediate attention

---

## Expected Outcomes

**After First Health Check:**
- Baseline metrics established
- All current issues documented
- Prioritized remediation plan created

**After 3 Months:**
- Trends identified (improving/stable/declining)
- Automated scripts reducing manual work by 50%
- Proactive issue detection before they compound

**After 6 Months:**
- Consistent Green status (55-60 points)
- Zero critical duplicate ID issues
- All indexes current and complete
- Ecosystem growth without degradation

**After 12 Months:**
- Fully automated health monitoring
- CI/CD integration preventing issues at creation
- Monthly reviews reduced to 15-20 minutes
- Self-sustaining ecosystem integrity

---

## Notes

**Version History:**
- v1.0 (2025-11-14): Initial creation following ecosystem analysis that identified 87 issues
- Future versions will refine based on actual monthly use

**Related Documentation:**
- [Video Discovery Pipeline](../Researches/Videos/Video_Discovery_Pipeline.md)
- [Video Queue Tracker](../Researches/Videos/Video_Queue_Tracker.md)
- [LIBRARIES Import Index](../LIBRARIES_Import_Index.md)
- [4-Phase Ecosystem Cleanup Plan](#) (if created as separate document)

**Feedback Loop:**
After each monthly review, note any improvements needed to this prompt:
- Steps that took longer than estimated
- Missing checks that should be added
- False positives to filter out
- Additional automation opportunities

---

**Maintained By:** Taxonomy Team
**Last Updated:** November 14, 2025
**Next Scheduled Update:** After first monthly health check (December 2, 2025)
