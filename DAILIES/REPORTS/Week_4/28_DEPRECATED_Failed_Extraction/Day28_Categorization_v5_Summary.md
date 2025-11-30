# Day 28 Task Categorization & Matching v5.0 Summary

**Date:** November 28, 2025
**Total Items Processed:** 595

---

## Categorization Results

| Category | Count | % | ID Range | File |
|----------|-------|---|----------|------|
| Tasks (Matched) | 202 | 33.9% | TSK-001 to TSK-202 | Day28_Tasks_Matched.json |
| Tasks (Unmatched) | 212 | 35.6% | TSK-203 to TSK-414 | Day28_Tasks_Unmatched.json |
| Reports (Matched) | 81 | 13.6% | RPT-001 to RPT-081 | Day28_Reports_Matched.json |
| Reports (Unmatched) | 26 | 4.4% | RPT-082 to RPT-107 | Day28_Reports_Unmatched.json |
| Problems | 41 | 6.9% | PRB-001 to PRB-041 | Day28_Problems.json |
| **Filtered Metadata** | **33** | **5.5%** | | Day28_Filtered_Metadata.json |
| **TOTAL VALID** | **562** | **94.5%** | | |

---

## Verb Tense Classification

**Active Verbs (Tasks):** 414 items with process/base verbs
**Completed Verbs (Reports):** 107 items with result verbs

### Top 20 Detected Verbs

| Verb | Count |
|------|-------|
| added | 11 |
| sent | 10 |
| updated | 8 |
| implemented | 8 |
| list | 6 |
| created | 6 |
| file | 5 |
| code | 4 |
| limiting | 4 |
| export | 4 |
| structure | 4 |
| processing | 3 |
| design | 3 |
| format | 3 |
| backup | 3 |
| tracking | 3 |
| post | 3 |
| shared | 3 |
| developed | 3 |
| checked | 3 |

---

## Sample Tasks (Active Verbs)

1. **TSK-001** (None) -> TST-047 (50.0%)
   - Task: *Priority:** 🟡 Medium...
   - Employee: Artemchuk Nikolay (AI)

2. **TSK-004** (None) -> TST-041 (25.0%)
   - Task: *Status:**  New (Daily recurring)...
   - Employee: Artemchuk Nikolay (AI)

3. **TSK-005** (None) -> TST-044 (50.0%)
   - Task: *Depends On:** Employee requests...
   - Employee: Artemchuk Nikolay (AI)

4. **TSK-011** (None) -> TST-045 (44.4%)
   - Task: "Which AI tool should I use for X task?"...
   - Employee: Artemchuk Nikolay (AI)

5. **TSK-015** (respond) -> TST-045 (42.9%)
   - Task: Respond to direct messages about AI tools...
   - Employee: Artemchuk Nikolay (AI)

6. **TSK-016** (guide) -> TST-072 (36.4%)
   - Task: Guide on when to use which tool (Cursor vs Antigravity vs Claude)...
   - Employee: Artemchuk Nikolay (AI)

7. **TSK-017** (None) -> TST-003 (50.0%)
   - Task: *Success Criteria:**...
   - Employee: Artemchuk Nikolay (AI)

8. **TSK-018** (None) -> TST-009 (42.9%)
   - Task: All support requests answered within 2 hours...
   - Employee: Artemchuk Nikolay (AI)

9. **TSK-019** (None) -> TST-048 (66.7%)
   - Task: Employees unblocked on AI tool usage...
   - Employee: Artemchuk Nikolay (AI)

10. **TSK-020** (None) -> TST-019 (33.3%)
   - Task: *Definition of Done:**...
   - Employee: Artemchuk Nikolay (AI)

---

## Sample Reports (Completed Verbs)

1. **RPT-001** (assigned) -> TST-074 (37.5%)
   - Report: *Assigned To:** Designer without daily files in folder...
   - Employee: Artemchuk Nikolay (AI)

2. **RPT-002** (estimated) -> TST-011 (25.0%)
   - Report: *Estimated Time:** 1.5h...
   - Employee: Artemchuk Nikolay (AI)

3. **RPT-003** (handled) -> TST-009 (33.3%)
   - Report: Support requests handled...
   - Employee: Artemchuk Nikolay (AI)

4. **RPT-007** (developed) -> TST-081 (40.0%)
   - Report: Management (needs to be developed)...
   - Employee: Skrypkar Vilhelm (Design)

5. **RPT-012** (implemented) -> TST-045 (28.6%)
   - Report: Implemented `copyToUpdated()` function that recursively copies all JSON files fr...
   - Employee: Makovska Anna (Dev)

6. **RPT-015** (streamlined) -> TST-081 (60.0%)
   - Report: Streamlined workflow for content management...
   - Employee: Makovska Anna (Dev)

7. **RPT-018** (added) -> TST-046 (30.0%)
   - Report: Added batch processing (10 files per batch) for controlled update speed...
   - Employee: Makovska Anna (Dev)

8. **RPT-019** (implemented) -> TST-048 (30.0%)
   - Report: Implemented retry logic with exponential backoff (up to 3 retries)...
   - Employee: Makovska Anna (Dev)

9. **RPT-022** (deleted) -> TST-009 (25.0%)
   - Report: Deleted files → DELETE requests...
   - Employee: Makovska Anna (Dev)

10. **RPT-023** (implemented) -> TST-048 (60.0%)
   - Report: Implemented comprehensive file filtering system:...
   - Employee: Makovska Anna (Dev)

---

## Files Generated

1. **Day28_Tasks_Matched.json** - Tasks matched to templates
2. **Day28_Tasks_Unmatched.json** - New tasks (no template match)
3. **Day28_Reports_Matched.json** - Reports matched to templates
4. **Day28_Reports_Unmatched.json** - New reports (no template match)
5. **Day28_Problems.json** - Problems/issues/bugs
6. **Day28_Filtered_Metadata.json** - Filtered metadata fields
7. **Day28_Categorized_v5.csv** - Master CSV with all categories
8. **Day28_Categorization_v5_Summary.md** - This summary

---

*Generated: 2025-11-29*
*System: Task Categorization v5.0*
