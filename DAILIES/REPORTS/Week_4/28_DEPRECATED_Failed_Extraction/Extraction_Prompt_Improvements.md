# Day 28 Task Extraction - Prompt Improvements

**Date:** November 29, 2025
**Purpose:** Document issues found and improve extraction prompt for future processing
**Current Results:** 681 tasks extracted (estimated 382 need review/removal)

---

## Issues Identified

### **Issue 1: Template Instructions Extracted as Tasks (HIGH PRIORITY)**

**Problem:** Standard daily.md template instructions are being extracted as individual tasks

**Examples:**
- TST-031: "What: Record of all your activities throughout the day"
- TST-032: "Time stamps for each activity"
- TST-033: "What you worked on"
- TST-034: "Whisper Flow transcripts from all meetings/calls"
- TST-035: "Outcomes and results"

**Pattern:** These appear in every employee's daily.md under the "## Instructions" section

**Impact:** ~60 tasks (14 tasks identified in "Template/Metadata" topic, but more in "General/Operational")

**Fix:**
```python
# Add template section detection
TEMPLATE_SECTIONS = [
    '## Instructions',
    '**What**:',
    '**Include**:',
    '**How to create this plan:**'
]

# Skip these common template lines
TEMPLATE_LINES = [
    'record of all your activities',
    'time stamps for each activity',
    'what you worked on',
    'whisper flow transcripts',
    'outcomes and results',
    'update this file throughout',
    'include all meeting transcripts'
]

def is_template_instruction(line, section):
    if any(tmpl in section.lower() for tmpl in TEMPLATE_SECTIONS):
        return True
    if any(tmpl in line.lower() for tmpl in TEMPLATE_LINES):
        return True
    return False
```

---

### **Issue 2: Field Labels Extracted as Tasks (HIGH PRIORITY)**

**Problem:** Metadata field labels (task template structure) extracted as tasks

**Examples:**
- TST-001: "*Priority:** 🟡 Medium"
- TST-008: "*Estimated Time:** 1.5h"
- TST-010: "*Description:**"
- TST-017: "*Subtasks:**"
- TST-023: "*Success Criteria:**"
- TST-027: "*Definition of Done:**"

**Pattern:** Lines starting with `*FieldName**:` followed by short value or empty

**Impact:** ~30-40 tasks

**Fix:**
```python
# Detect field label patterns
FIELD_LABEL_PATTERN = r'^\*[A-Za-z\s]+\*\*:\s*(.*)$'

def is_field_label(text):
    """Check if text is a field label, not a task"""
    match = re.match(FIELD_LABEL_PATTERN, text)
    if match:
        value = match.group(1).strip()
        # If empty or very short (< 10 chars), it's a label
        if len(value) < 10:
            return True
        # Common field names
        field_names = [
            'priority', 'project', 'taxonomy code', 'status',
            'depends on', 'blocks', 'assigned to', 'estimated time',
            'actual time', 'description', 'subtasks', 'success criteria',
            'definition of done', 'outcomes', 'what i worked on'
        ]
        if any(field in text.lower() for field in field_names):
            return True
    return False
```

---

### **Issue 3: Section Headers Extracted as Tasks (MEDIUM PRIORITY)**

**Problem:** Section transition markers extracted as tasks

**Examples:**
- TST-036: "What I worked on:"
- TST-039: "Outcomes:"
- TST-042: "What I worked on:"
- TST-045: "Outcomes:"
- TST-122: "Outcomes:"

**Pattern:** Short lines ending with ":" that introduce a section

**Impact:** ~40-50 tasks

**Fix:**
```python
SECTION_HEADER_PATTERNS = [
    r'^\*?\*?What I worked on:\*?\*?$',
    r'^\*?\*?Outcomes:\*?\*?$',
    r'^\*?\*?Whisper Flow Transcript:\*?\*?$',
    r'^\*?\*?Next Steps:\*?\*?$',
    r'^\*?\*?Plan:\*?\*?$'
]

def is_section_header(text):
    """Check if text is a section header, not a task"""
    clean_text = text.strip()

    # Ends with colon and < 30 chars
    if clean_text.endswith(':') and len(clean_text) < 30:
        # Check if it's a common section header
        for pattern in SECTION_HEADER_PATTERNS:
            if re.match(pattern, clean_text, re.IGNORECASE):
                return True

    return False
```

---

### **Issue 4: Technical Specifications as Individual Tasks (MEDIUM PRIORITY)**

**Problem:** Requirement specifications split into micro-tasks

**Examples (Design mascot specs):**
- TST-081: "png or svg format"
- TST-082: "square, 800x800px minimum, 2000x2000px maximum..."
- TST-083: "Under 2MB each"
- TST-084: "Naming format: mascot_[department]_[role]_[description].png"

**Pattern:** Lists of requirements/specifications that should be grouped

**Impact:** ~20-30 tasks

**Fix:**
```python
def detect_specification_group(lines, current_index):
    """Detect if current line is part of a specification group"""
    line = lines[current_index].lower()

    # Check for specification keywords
    spec_keywords = ['format', 'size', 'px', 'mb', 'kb', 'naming', 'file size']

    if any(keyword in line for keyword in spec_keywords):
        # Check if previous or next lines are also specs
        context_lines = []
        if current_index > 0:
            context_lines.append(lines[current_index - 1])
        if current_index < len(lines) - 1:
            context_lines.append(lines[current_index + 1])

        # If surrounded by similar specs, mark for grouping
        spec_count = sum(1 for ctx in context_lines
                        if any(kw in ctx.lower() for kw in spec_keywords))

        if spec_count >= 1:
            return True  # Part of specification group

    return False
```

---

### **Issue 5: Too Many "General/Operational" Tasks (LOW PRIORITY)**

**Problem:** 382 tasks (56%) classified as General/Operational - too broad

**Impact:** Hard to review and validate

**Fix:** Improve topic classification with more granular categories

```python
# Add more specific topics
TOPIC_KEYWORDS = {
    'Strapi CMS Integration': ['strapi', 'cms', 'content management', 'media library'],
    'Mascot Design System': ['mascot', 'shark', 'tiger', 'wolf', 'animal'],
    'AI Tool Support': ['discord', 'support', 'claude', 'gemini', 'ai tool', 'extension'],
    'Data Scraping': ['scraping', 'scrape', 'vacancy', 'vacancies', 'job site'],
    'Lead Generation': ['lead', 'crm', 'linkedin', 'outreach', 'connection'],
    'Calendar Management': ['calendar', 'booking', 'scheduling', 'appointment'],
    'System Optimization': ['optimization', 'performance', 'bottleneck', 'diagnostic'],
    'AI Agent Development': ['gem', 'chatgpt', 'prompt', 'agent', 'template'],
    'Script Automation': ['export', 'script', 'automation', 'workflow', 'python'],
    'UI/UX Improvements': ['ui', 'ux', 'interface', 'responsive', 'sidebar', 'button'],
    'Black Friday Campaign': ['black friday', 'campaign', 'messaging'],
    'Account Management': ['account', 'checking', 'morning routine', 'sweep'],
    'Documentation': ['document', 'documentation', 'faq', 'guide'],
    'Testing & QA': ['testing', 'test', 'validation', 'verify', 'check'],
    # Add more specific topics
}
```

---

## Improved Extraction Prompt

### **Updated Python Script Logic**

```python
"""
Improved Day 28 Task Extraction Script v2.0
Filters out templates, metadata, and section headers
"""

import os
import re
from collections import defaultdict

# Configuration
BASE_PATH = r'C:\Users\Dell\Dropbox\Nov25'
OUTPUT_DIR = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28'
DAY = '28'

# ==================== FILTER PATTERNS ====================

# Template section headers to skip
TEMPLATE_SECTIONS = [
    '## Instructions',
    '**What**:',
    '**Include**:',
    '**How to create this plan:**'
]

# Common template instruction lines to skip
SKIP_PATTERNS = [
    r'^\*?What\*?: Record of all your activities',
    r'^Time stamps for each activity',
    r'^What you worked on',
    r'^Whisper Flow transcripts',
    r'^Outcomes and results',
    r'^Update this file throughout',
    r'^Include all meeting transcripts',
    r'^\*?What I worked on:\*?$',
    r'^\*?Outcomes:\*?$',
    r'^\*?Whisper Flow (Transcript|ON):\*?$'
]

# Field label pattern
FIELD_LABEL_PATTERN = r'^\*[A-Za-z\s]+\*\*:\s*(.{0,15})$'

# Known field names
FIELD_NAMES = [
    'priority', 'project', 'taxonomy code', 'status',
    'depends on', 'blocks', 'assigned to', 'estimated time',
    'actual time', 'description', 'subtasks', 'success criteria',
    'definition of done', 'common support requests'
]

# Minimum task description length
MIN_TASK_LENGTH = 15

# ==================== FILTER FUNCTIONS ====================

def should_skip_line(line, section_context):
    """Determine if a line should be skipped"""

    # Skip if in template section
    if any(tmpl in section_context for tmpl in TEMPLATE_SECTIONS):
        return True

    # Skip if matches template pattern
    for pattern in SKIP_PATTERNS:
        if re.match(pattern, line, re.IGNORECASE):
            return True

    # Skip if it's a field label
    match = re.match(FIELD_LABEL_PATTERN, line)
    if match:
        # Check if field name is known
        if any(field in line.lower() for field in FIELD_NAMES):
            return True
        # Skip if value is too short (likely just a label)
        value = match.group(1).strip()
        if len(value) < 10:
            return True

    # Skip section headers (ends with ":" and < 30 chars)
    if line.strip().endswith(':') and len(line.strip()) < 30:
        if re.match(r'^\*?\*?(What|Outcomes|Plan|Next Steps|Whisper Flow)', line, re.IGNORECASE):
            return True

    # Skip if too short
    if len(line.strip()) < MIN_TASK_LENGTH:
        return True

    return False

# ==================== EXTRACTION LOGIC ====================

def extract_tasks_from_daily(file_path, employee, department, status):
    """Extract tasks from daily.md file with improved filtering"""

    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    lines = content.split('\n')
    tasks = []

    current_section = 'General'
    current_time = None
    section_header_line = ''

    for i, line in enumerate(lines):
        # Track section headers for context
        if line.startswith('###'):
            current_section = line.replace('###', '').strip()
            section_header_line = line

            # Extract time if present
            time_match = re.search(r'(\d{1,2}:\d{2}(?:\s*-\s*\d{1,2}:\d{2})?)', current_section)
            if time_match:
                current_time = time_match.group(1)

        # Track ## headers for template detection
        if line.startswith('##'):
            section_header_line = line

        # Detect task items (bullets with optional checkbox)
        task_match = re.match(r'^\s*[-*]\s*(\[[ Xx]\])?\s*(.+)$', line)

        if task_match:
            task_text = task_match.group(2).strip()

            # Apply filters
            if should_skip_line(task_text, section_header_line):
                continue

            # Determine task status
            status_marker = task_match.group(1)
            if status_marker:
                if status_marker in ['[X]', '[x]']:
                    task_status = 'completed'
                else:
                    task_status = 'new'
            elif '✅' in line:
                task_status = 'completed'
            elif '🔄' in line:
                task_status = 'in_progress'
            elif '⏸️' in line:
                task_status = 'blocked'
            else:
                task_status = 'new'

            # Clean task text
            task_text = re.sub(r'[✅🔄🆕⏸️]', '', task_text).strip()
            task_text = re.sub(r'\[X\]|\[x\]|\[ \]', '', task_text).strip()

            # Final length check
            if len(task_text) < MIN_TASK_LENGTH:
                continue

            # Create task object
            task = {
                'employee': employee,
                'department': department,
                'status': status,
                'task_status': task_status,
                'description': task_text,
                'section': current_section,
                'time': current_time,
                'date': 'November 28, 2025'
            }

            tasks.append(task)

    return tasks
```

---

## Expected Results After Improvements

### **Before (Current):**
- Total tasks extracted: 681
- Estimated valid tasks: ~300-320 (44-47%)
- Metadata/template tasks: ~360 (53-56%)

### **After (Improved):**
- Total tasks extracted: ~320-350
- Valid tasks: ~320-350 (95%+)
- Metadata/template tasks: <20 (5%)

### **Quality Improvements:**
1. ✅ Template instructions filtered out
2. ✅ Field labels removed
3. ✅ Section headers removed
4. ✅ Minimum length requirement enforced (15 chars)
5. ✅ Better topic classification
6. ✅ Specification grouping support

---

## Recommended Next Steps

### **1. Re-run Extraction with Improved Prompt**
```bash
python extract_day28_tasks_v2.py
```

### **2. Compare Results**
```
Old: 681 tasks → Review → ~320 valid
New: ~350 tasks → Review → ~330 valid

Time saved: 350 tasks vs 681 tasks = 48% reduction in review effort
```

### **3. Validate Sample**
- Extract 10% sample of new results
- Verify false positive rate < 5%
- Verify false negative rate < 2%

### **4. Apply to Future Days**
- Use v2 script for Day 29, 30 processing
- Monitor quality metrics
- Iterate on filter patterns

---

## Lessons Learned

### **What Worked:**
- ✅ Checkbox detection for task status
- ✅ Time extraction from section headers
- ✅ Department/employee metadata tracking
- ✅ Section context preservation

### **What Needs Improvement:**
- ⚠️ Template vs content distinction
- ⚠️ Field label vs task item distinction
- ⚠️ Section header vs task description
- ⚠️ Specification grouping logic

### **For Future Enhancements:**
1. Add ML-based task classification
2. Implement task deduplication
3. Add task relationship detection (parent/child)
4. Improve task name generation
5. Add confidence scoring

---

## Summary

**Current State:**
- 681 tasks extracted
- ~56% are metadata/template items
- Manual review required for all tasks

**Improved State (Projected):**
- ~350 tasks extracted
- ~95% are actual work items
- Minimal manual review needed

**Key Changes:**
1. Filter template instructions
2. Skip field labels
3. Remove section headers
4. Enforce minimum task length
5. Better topic classification

**Impact:**
- 48% reduction in review effort
- 95%+ accuracy in extraction
- Faster processing for future days

---

*Document created: November 29, 2025*
*Next action: Implement v2 extraction script and reprocess Day 28*
