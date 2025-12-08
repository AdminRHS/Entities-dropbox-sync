# Scraping Task Queue (QQ)

**Last Updated:** 2025-12-07
**Total Tasks:** 0
**Pending:** 0
**In Progress:** 0
**Completed:** 0
**Failed:** 0

---

## Queue Rules

1. Tasks numbered sequentially: QQ.001, QQ.002, etc.
2. Priority: High → Medium → Low
3. Status updated by scraping-agent
4. Failed tasks moved to failed/ folder with error log
5. Completed tasks archived to completed/ folder

---

## Pending Tasks

*No tasks currently in queue*

---

## In Progress

*No tasks currently being processed*

---

## Task Template

```markdown
### Task QQ.XXX
**URL:** [target URL]
**Type:** [book|article|data|general]
**Priority:** [High|Medium|Low]
**Status:** [Pending|In Progress|Complete|Failed|Retry]
**Assigned:** scraping-agent
**Added:** YYYY-MM-DD HH:MM
**Started:** (when processing begins)
**Completed:** (when finished)
**Output:** [path to extracted data]
**Notes:** [any special instructions or issues]
```

---

**How to Add Task:**

1. Manual: Copy template, fill details, increment QQ number
2. Automated: Use "PROCESS scraping for [URL]" in daily notes
3. Integration: Task manager creates via API (future)

---

**Next QQ Number:** QQ.001
