# Daily Report Collection Automation Prompt

## Purpose
This prompt automates the process of collecting daily activity reports from all department prompt logs and consolidating them into comprehensive department-specific reports.

---

## Instructions for AI Assistant

### Step 1: Read All Department Prompt Logs

Read the following department prompt log files to collect today's activities:

1. `Dropbox/Nov25/AI/AI prompt log.md`
2. `Dropbox/Nov25/Design/Design prompt log.md`
3. `Dropbox/Nov25/Dev/Dev prompt log.md`
4. `Dropbox/Nov25/LG/LG prompt log.md`
5. `Dropbox/Nov25/Video/Video prompt log.md`

### Step 2: Determine Current Date

Use the system date to determine the day number (e.g., 05 for November 5, 2025).

Format: Two-digit day number (01, 02, 03... 30, 31)

### Step 3: Create Folder Structure

For each department, ensure the following folder structure exists:
```
/Nov25/{DEPARTMENT}/Reports/{DAY}/
```

Example for day 05:
- `/Nov25/AI/Reports/05/`
- `/Nov25/Design/Reports/05/`
- `/Nov25/Dev/Reports/05/`
- `/Nov25/LG/Reports/05/`
- `/Nov25/Video/Reports/05/`

### Step 4: Generate Department Reports

For each department, create a comprehensive daily activity report following this structure:

#### Report Template Structure

**File Name:** `Daily_Activity_Report_Nov{DAY}_2025.md`

**Report Sections:**

1. **Executive Summary**
   - Report period (date)
   - Department name
   - Total major activities count
   - Team size
   - Overall status
   - Key achievements (bullet list)

2. **Activity Timeline**
   - Detailed breakdown of each activity from the prompt log
   - For each activity:
     - Title and status
     - Priority level
     - Objective
     - Actions taken (detailed list)
     - Results (with checkmarks for completed items)
     - Impact assessment

3. **Metrics and Statistics**
   - Quantitative summary table
   - Task distribution tables
   - Documentation impact tables
   - Any relevant statistics

4. **Key Deliverables**
   - List all files created
   - List all major outputs
   - Status of each deliverable

5. **Department Impact Analysis**
   - Impact level (Critical/High/Medium/Low)
   - Improvements made
   - Benefits gained
   - Categories affected

6. **Technical Achievements**
   - System configurations
   - Documentation enhancements
   - Process improvements
   - Tool integrations

7. **Challenges and Solutions**
   - Each challenge with:
     - Problem description
     - Solution applied
     - Result achieved
     - Impact on work

8. **Files Created/Modified Summary**
   - New files created (with paths)
   - Modified files (with descriptions)
   - Deleted files (if any)

9. **Recommendations for Follow-up**
   - Immediate actions required
   - Short-term improvements
   - Long-term enhancements

10. **Success Indicators**
    - Completed successfully (checkboxes)
    - Quality metrics (checkboxes)
    - Any pending items

11. **Conclusion**
    - Summary of day's work
    - Key achievements recap
    - Impact assessment
    - Overall status

**Report Footer:**
```
---
**Report Generated:** [Date]
**Department:** [Department Name]
**Team Size:** [Number]
**Report Status:** Complete
---
*End of Report*
```

### Step 5: Extract Department-Specific Information

For each department, extract from the prompt log:

**AI Department:**
- Infrastructure and system tasks
- Tool integrations
- Framework enhancements
- Technical configurations
- Task distributions to AI team members
- Documentation updates

**Design Department:**
- Employee profile updates
- Design guidelines created/updated
- Video scenarios developed
- Daily activities processed
- Creative deliverables
- Task distributions to designers

**Dev Department:**
- Development tool integrations
- Code-related activities
- System configurations
- Task distributions to developers
- Technical implementations

**LG Department:**
- Setup guides created
- Training materials developed
- Onboarding documentation
- Task distributions to LG team
- Process improvements

**Video Department:**
- Video tool integrations
- Production materials
- Video-related documentation
- Task distributions to video team
- Creative assets

### Step 6: Create Department Reports

For each department:

1. Analyze all activities from that department's prompt log for today
2. Generate comprehensive report following the template
3. Include all metrics, statistics, and impact analysis
4. Save report to: `/Nov25/{DEPARTMENT}/Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md`

---

## Report Quality Standards

### Content Requirements
- ✅ All activities from prompt logs included
- ✅ Detailed breakdown of each task
- ✅ Metrics and statistics calculated
- ✅ Impact analysis provided
- ✅ Challenges and solutions documented
- ✅ Files created/modified listed
- ✅ Recommendations for follow-up included

### Formatting Requirements
- ✅ Markdown format with proper headers
- ✅ Tables for statistics and metrics
- ✅ Bullet lists for achievements
- ✅ Checkboxes for completed items
- ✅ Consistent section structure
- ✅ Professional tone and language
- ✅ Clear, concise descriptions

### Technical Requirements
- ✅ File paths accurate and absolute
- ✅ Line counts included where applicable
- ✅ Tool names with URLs
- ✅ Employee names accurate
- ✅ Task counts verified
- ✅ Priority levels specified

---

## Example Usage

### Command to AI Assistant:

```
Process my department prompt logs and create comprehensive daily activity reports for November [DAY], 2025.

1. Read all department prompt logs (AI, Design, Dev, LG, Video, etc.)
2. Create Reports/{DAY} folder in each department
3. Generate detailed activity report for each department

Use the PROMPT_Daily_Report_Collection.md template.
```

### Expected Output:

**Department Reports Created:**
1. `/Nov25/AI/Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md`
2. `/Nov25/Design/Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md`
3. `/Nov25/Dev/Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md`
4. `/Nov25/LG/Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md`
5. `/Nov25/Video/Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md`

---

## Automation Schedule

### Recommended Timing
- **End of Day:** Generate reports at end of work day (6:00 PM)
- **Next Morning:** Review reports before daily standup (9:00 AM)
- **Weekly:** Compile weekly summary on Friday evening

### Trigger Conditions
Run this automation:
- At end of each work day
- When explicitly requested
- Before important meetings
- For weekly/monthly reporting

---

## Maintenance and Updates

### Regular Reviews
- Weekly: Review report quality and completeness
- Monthly: Update template if needed
- Quarterly: Refine metrics and statistics

### Version Control
- Track changes to report template
- Document any structural changes
- Maintain backward compatibility

### Improvements
- Add new sections as needed
- Enhance metrics and statistics
- Improve formatting and readability
- Integrate with other systems

---

## Troubleshooting

### Issue: Missing Department Activities
**Solution:** Verify prompt log files exist and contain today's entries

### Issue: Incomplete Reports
**Solution:** Check that all log entries have "Result:" sections

### Issue: Wrong Date/Day Number
**Solution:** Verify system date and use correct two-digit format

### Issue: Folder Creation Fails
**Solution:** Check permissions and path accuracy

### Issue: Report Quality Issues
**Solution:** Review template requirements and ensure all sections included

---

## Notes

- This prompt should be run at the end of each work day
- Reports are cumulative and based on prompt logs
- Each department maintains its own report copy
- Reports serve as daily activity documentation and progress tracking
- Can be used for weekly/monthly summaries and reviews

---

## Version History

**v1.0** - November 5, 2025
- Initial prompt creation
- Template structure defined
- All departments included

**v1.1** - November 16, 2025
- Removed deprecated AI department references
- Streamlined folder structure

---

*Last Updated: November 5, 2025*
