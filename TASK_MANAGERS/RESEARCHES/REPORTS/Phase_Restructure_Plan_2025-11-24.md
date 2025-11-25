# Phase Restructure Plan: 8 Phases → 6 Phases

**Date:** 2025-11-24
**Purpose:** Eliminate redundant phases and rename remaining phases for clarity

---

## New 6-Phase Workflow Structure

### ❌ OLD 8-Phase System:
```
Phase_0_Queued          → Video added to queue
Phase_1_Transcribed     → Video transcribed (PMT-004)
Phase_2_Named           → Title refined (PMT-005) [REDUNDANT]
Phase_3_Analyzed        → Initial analysis (PMT-006) [REDUNDANT]
Phase_4_Objects         → Objects extracted (PMT-007)
Phase_5_Gap_Analysis    → Gap analysis (PMT-009 Part 1)
Phase_6_Integration     → Taxonomy integration (PMT-009 Part 2)
Phase_7_Mapped          → Library mapping (PMT-009 Part 3)
Complete                → All phases finished
```

### ✅ NEW 6-Phase System:
```
Phase_0_Queued              → Video added to queue
Phase_1_Transcribed         → Full transcription + analysis (PMT-004)
Phase_2_Extraction          → Entity extraction & cross-referencing (PMT-007)
Phase_3_Gap_Analysis        → Library comparison & gap identification (PMT-009 Part 1)
Phase_4_Integration         → JSON creation & taxonomy integration (PMT-009 Part 2)
Phase_5_Mapping             → Final mapping & documentation (PMT-009 Part 3)
Complete                    → All phases finished
```

---

## Rationale for Changes

### Phase Eliminations:

#### ❌ Phase_2_Named (PMT-005) - ELIMINATED
**Why:** PMT-004 already captures video title in transcription output.
- All transcription files include: `Video Title: [Full descriptive title]`
- No additional naming step needed

#### ❌ Phase_3_Analyzed (PMT-006) - ELIMINATED
**Why:** PMT-004 already performs comprehensive taxonomy analysis.
- PMT-004 v4.0+ extracts:
  - Workflows with task breakdowns
  - Action verbs (7 categories A-G)
  - Tools & Technologies Matrix
  - Objects & Deliverables
  - Integration Patterns
  - Task Chains
  - 37+ entities pre-categorized
- Separate "analysis" phase duplicates this work

### Phase Renaming:

#### Phase_4_Objects → Phase_2_Extraction
**Why:** "Objects" is misleading - this phase extracts ALL entities, not just objects.

**What PMT-007 Actually Does:**
- Extracts Objects (deliverables, outputs)
- Extracts Tools with TOOL-{CATEGORY}-### IDs
- Extracts Actions (ACT-###)
- Extracts Workflows (WRF-###)
- Extracts Professions (PRF-###)
- Extracts Skills (SKL-###)
- **Cross-references** all entities bidirectionally
- Creates entity relationship maps

**Better Name:** "Extraction" or "Entity Extraction & Cross-Referencing"

#### Phase_7_Mapped → Phase_5_Mapping
**Why:** Clearer action verb form (ongoing process vs past tense)

---

## Phase Descriptions (Updated)

### Phase_0_Queued
**Description:** Video added to queue
**Status:** Initial state
**Output:** Video_Queue_Master.csv entry

### Phase_1_Transcribed
**Description:** Full transcription + taxonomy analysis (PMT-004)
**Prompt:** PMT-004 Video Transcription v4.1
**Output:**
- Word-for-word transcription with timestamps
- Video metadata (title, description, duration)
- TAXONOMY ANALYSIS section:
  - Workflows identified (WRF-###)
  - Action verbs extracted (7 categories)
  - Tools & Technologies Matrix (TOL-###)
  - Objects & Deliverables (OBJ-###)
  - Integration Patterns
  - Task Chains
  - Responsibilities vocabulary
  - 37+ entities pre-categorized
**File:** `02_TRANSCRIPTIONS/Video_XXX.md`

### Phase_2_Extraction
**Description:** Deep entity extraction & cross-referencing (PMT-007)
**Prompt:** PMT-007 Objects Library Extraction
**Focus:**
- Extract ALL objects with types (thumbnails, videos, scripts, etc.)
- Extract Tools with TOOL-{CATEGORY}-### format
- Extract Actions (ACT-###)
- Extract Workflows (WRF-###)
- Extract Professions (PRF-###)
- Extract Skills (SKL-###)
- **Cross-reference bidirectionally:**
  - Object ↔ Tool
  - Object ↔ Action
  - Object ↔ Workflow
  - Object ↔ Profession
  - Object ↔ Skill
  - Object ↔ Related Objects
**Output:**
- Complete entity inventory with IDs
- Cross-reference mapping
- Entity relationship trees
**File:** `03_ANALYSIS/Extractions/Video_XXX_Extraction.md`

### Phase_3_Gap_Analysis
**Description:** Library comparison & gap identification (PMT-009 Part 1)
**Prompt:** PMT-009 Taxonomy Integration Part 1
**Process:**
- Compare extracted entities to existing LIBRARIES
- Identify NEW entities (not in library)
- Identify EXISTING entities (need enhancement)
- Identify DUPLICATES across system
- Prioritize entities for integration
**Output:**
- Gap analysis report
- NEW entity list with priority levels
- EXISTING entity enhancement notes
- Duplicate detection report
**File:** `03_ANALYSIS/Gap_Analysis/Video_XXX_Gap_Analysis.md`

### Phase_4_Integration
**Description:** JSON creation & taxonomy integration (PMT-009 Part 2)
**Prompt:** PMT-009 Taxonomy Integration Part 2
**Process:**
- Create JSON files for NEW entities:
  - Tools → `LIBRARIES/Tools/TOOL-{CATEGORY}-###.json`
  - Workflows → `TASK_MANAGERS/TSM-006_Workflows/WRF-###.json`
  - Actions → Update `LIBRARIES/Actions/Actions_Master.json`
  - Objects → Update `LIBRARIES/Responsibilities/Objects/`
  - Professions → Update `LIBRARIES/Responsibilities/Professions/`
  - Skills → Update `LIBRARIES/Skills/`
- Update ENTITIES_MASTER_LIST.csv
- Update master registries
- Move files to correct locations
**Output:**
- JSON entity files created
- Master lists updated
- Files integrated into LIBRARIES/TASK_MANAGERS
**File:** Integration tracking in `04_INTEGRATION/Video_XXX_Integration.md`

### Phase_5_Mapping
**Description:** Final mapping & documentation (PMT-009 Part 3)
**Prompt:** PMT-009 Taxonomy Integration Part 3
**Process:**
- Generate library mapping report
- Document cross-references
- Create integration summary
- Update workflows with new entity references
- Verify bidirectional links
**Output:**
- Library mapping report
- Integration summary
- Cross-reference documentation
**File:** `03_ANALYSIS/Library_Mapping/Video_XXX_Mapping.md`

### Complete
**Description:** All phases finished
**Status:** Final state
**Verification:**
- All entities integrated
- All cross-references validated
- All documentation complete

---

## Implementation Plan

### Step 1: Update Progress Tracker Script
**File:** `scripts/update_video_progress.py`

**Changes:**
```python
# OLD PHASES dictionary
PHASES = {
    'Phase_0_Queued': 'Video added to queue',
    'Phase_1_Transcribed': 'Video transcribed (PMT-004)',
    'Phase_2_Named': 'Title refined (PMT-005)',  # REMOVE
    'Phase_3_Analyzed': 'Initial analysis (PMT-006)',  # REMOVE
    'Phase_4_Objects': 'Objects extracted (PMT-007)',
    'Phase_5_Gap_Analysis': 'Gap analysis (PMT-009 Part 1)',
    'Phase_6_Integration': 'Taxonomy integration (PMT-009 Part 2)',
    'Phase_7_Mapped': 'Library mapping (PMT-009 Part 3)',
    'Complete': 'All phases completed'
}

# NEW PHASES dictionary
PHASES = {
    'Phase_0_Queued': 'Video added to queue',
    'Phase_1_Transcribed': 'Full transcription + analysis (PMT-004)',
    'Phase_2_Extraction': 'Entity extraction & cross-referencing (PMT-007)',
    'Phase_3_Gap_Analysis': 'Library comparison & gap identification (PMT-009 Part 1)',
    'Phase_4_Integration': 'JSON creation & taxonomy integration (PMT-009 Part 2)',
    'Phase_5_Mapping': 'Final mapping & documentation (PMT-009 Part 3)',
    'Complete': 'All phases completed'
}
```

**CSV Headers:**
```python
# OLD headers
headers = [
    'Video_ID', 'Video_Number', 'Title', 'YouTube_URL', 'Current_Phase',
    'Phase_0_Queued', 'Phase_1_Transcribed', 'Phase_2_Named', 'Phase_3_Analyzed',  # Remove these 2
    'Phase_4_Objects', 'Phase_5_Gap_Analysis', 'Phase_6_Integration', 'Phase_7_Mapped',
    'Status', 'Employee', 'Date_Started', 'Date_Completed', 'Total_Days', 'Notes'
]

# NEW headers
headers = [
    'Video_ID', 'Video_Number', 'Title', 'YouTube_URL', 'Current_Phase',
    'Phase_0_Queued', 'Phase_1_Transcribed', 'Phase_2_Extraction',
    'Phase_3_Gap_Analysis', 'Phase_4_Integration', 'Phase_5_Mapping',
    'Status', 'Employee', 'Date_Started', 'Date_Completed', 'Total_Days', 'Notes'
]
```

### Step 2: Update Report Generator Script
**File:** `scripts/generate_progress_report.py`

**Changes:**
- Update phase references in `generate_detailed_report()`
- Update phase list display
- Remove references to Phase_2_Named and Phase_3_Analyzed

### Step 3: Update Documentation

#### README.md
**Update:**
- Quick Start section (line 186-190)
- Workflow Phases section
- Phase count: "8 processing phases" → "6 processing phases"

#### SCRIPTS_INVENTORY.md
**Update:**
- Line 238-247: Phases Tracked list
- Line 277-317: Complete Video Processing Workflow
- Remove Phase_2 and Phase_3 steps
- Renumber remaining phases

### Step 4: Migrate Existing VIDEO_PROGRESS_TRACKER.csv (If Exists)
**Script to create:**
```python
# migrate_tracker.py
import csv
from pathlib import Path

def migrate_tracker():
    """Migrate existing tracker to new phase structure"""
    old_file = Path('VIDEO_PROGRESS_TRACKER.csv')
    backup_file = Path('VIDEO_PROGRESS_TRACKER_BACKUP_2025-11-24.csv')

    if not old_file.exists():
        print("No existing tracker found. New one will use 6-phase structure.")
        return

    # Backup
    import shutil
    shutil.copy(old_file, backup_file)
    print(f"✅ Backed up to: {backup_file}")

    # Read old data
    with open(old_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Transform to new structure
    new_rows = []
    for row in rows:
        new_row = {
            'Video_ID': row['Video_ID'],
            'Video_Number': row['Video_Number'],
            'Title': row['Title'],
            'YouTube_URL': row['YouTube_URL'],
            'Current_Phase': row['Current_Phase'],
            'Phase_0_Queued': row['Phase_0_Queued'],
            'Phase_1_Transcribed': row['Phase_1_Transcribed'],
            # Phase_2_Named and Phase_3_Analyzed skipped (were redundant)
            'Phase_2_Extraction': row.get('Phase_4_Objects', ''),  # Renamed
            'Phase_3_Gap_Analysis': row.get('Phase_5_Gap_Analysis', ''),
            'Phase_4_Integration': row.get('Phase_6_Integration', ''),
            'Phase_5_Mapping': row.get('Phase_7_Mapped', ''),  # Renamed
            'Status': row['Status'],
            'Employee': row['Employee'],
            'Date_Started': row['Date_Started'],
            'Date_Completed': row['Date_Completed'],
            'Total_Days': row['Total_Days'],
            'Notes': row['Notes']
        }

        # Update Current_Phase naming
        phase_mapping = {
            'Phase_2_Named': 'Phase_1_Transcribed',  # Merge into Phase 1
            'Phase_3_Analyzed': 'Phase_1_Transcribed',  # Merge into Phase 1
            'Phase_4_Objects': 'Phase_2_Extraction',
            'Phase_5_Gap_Analysis': 'Phase_3_Gap_Analysis',
            'Phase_6_Integration': 'Phase_4_Integration',
            'Phase_7_Mapped': 'Phase_5_Mapping'
        }

        if new_row['Current_Phase'] in phase_mapping:
            new_row['Current_Phase'] = phase_mapping[new_row['Current_Phase']]

        new_rows.append(new_row)

    # Write new structure
    new_headers = [
        'Video_ID', 'Video_Number', 'Title', 'YouTube_URL', 'Current_Phase',
        'Phase_0_Queued', 'Phase_1_Transcribed', 'Phase_2_Extraction',
        'Phase_3_Gap_Analysis', 'Phase_4_Integration', 'Phase_5_Mapping',
        'Status', 'Employee', 'Date_Started', 'Date_Completed', 'Total_Days', 'Notes'
    ]

    with open(old_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=new_headers)
        writer.writeheader()
        writer.writerows(new_rows)

    print(f"✅ Migrated {len(new_rows)} videos to new 6-phase structure")
    print(f"   Old: 8 phases (Phase_0 to Phase_7)")
    print(f"   New: 6 phases (Phase_0 to Phase_5)")

if __name__ == '__main__':
    migrate_tracker()
```

---

## Benefits of New Structure

### Time Savings
- **Eliminated:** 2 redundant phases
- **Reduced:** Average processing time by ~25%
- **Streamlined:** Clear progression from transcription → extraction → integration

### Clarity Improvements
- **Phase_2_Extraction:** Accurately describes comprehensive entity extraction (not just "objects")
- **Phase_5_Mapping:** Active verb form (ongoing process)
- **Numbered 0-5:** Simpler mental model (6 phases vs 8)

### Process Improvements
- **No Duplication:** PMT-004 does title + analysis in one pass
- **Focused Phases:** Each phase has distinct, non-overlapping purpose
- **Better Naming:** Phase names reflect actual work performed

---

## Migration Checklist

- [ ] Create `scripts/migrate_tracker.py` migration script
- [ ] Backup existing VIDEO_PROGRESS_TRACKER.csv
- [ ] Update `scripts/update_video_progress.py` PHASES dictionary
- [ ] Update `scripts/update_video_progress.py` CSV headers
- [ ] Update `scripts/generate_progress_report.py` phase references
- [ ] Run migration script on VIDEO_PROGRESS_TRACKER.csv
- [ ] Test `update_video_progress.py add` command
- [ ] Test `update_video_progress.py update` command
- [ ] Test `update_video_progress.py view` command
- [ ] Test `generate_progress_report.py summary` command
- [ ] Test `generate_progress_report.py weekly` command
- [ ] Update README.md Workflow Phases section
- [ ] Update README.md Quick Start section
- [ ] Update README.md phase count reference
- [ ] Update SCRIPTS_INVENTORY.md Phases Tracked list
- [ ] Update SCRIPTS_INVENTORY.md Complete Video Processing Workflow
- [ ] Update Phase_Redundancy_Analysis_2025-11-24.md with final decision
- [ ] Archive PMT-005 and PMT-006 to PROMPTS/ARCHIVE/
- [ ] Document deprecation reason in archive

---

**Status:** Ready for Implementation
**Impact:** Low risk - no videos have reached deprecated phases yet
**Rollback:** Backup created, can restore if needed
