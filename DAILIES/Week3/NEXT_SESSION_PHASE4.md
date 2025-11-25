# Next Session: Phase 4 Implementation

**Date Created:** 2025-11-20
**Session:** Phase 4 - Task Hierarchy Formation
**Status:** Ready to Begin

---

## Quick Status

### ✅ Completed (Phase 3)
- PMT-070-P3 prompt created
- script_12_phase3_data_structurer.py working
- script_13_tm_populator.py working
- utils_session_logger.py working
- config.json v1.1 updated
- Documentation complete
- Tested: 74% token reduction achieved

### ⏳ Ready to Build (Phase 4)
All planning complete, user decisions confirmed, ready to code.

---

## Phase 4 To-Do List

### Priority Order

1. **Create PMT-070-P4 Prompt** (~2 hours)
   - File: `PROMPTS/UTILITIES/Daily_Updates/PMT-070_Phase_4_Task_Hierarchy.md`
   - Three-tier classification rules (checklist/step/task)
   - Bottom-up grouping criteria (min 2 steps)
   - Top-down decomposition patterns
   - Pattern-based tool mapping
   - JSON schema

2. **Build Script 14: Granularity Classifier** (~3 hours)
   - File: `scripts/script_14_granularity_classifier.py` (~400 lines)
   - Classify responsibilities into 3 tiers
   - Atomic verb detection: click, open, save, upload, download
   - Granularity scoring (0.0 = atomic, 1.0 = complex)
   - Integration with session logger

3. **Build Script 15: Bottom-Up Promoter** (~3 hours)
   - File: `scripts/script_15_bottom_up_promoter.py` (~350 lines)
   - **Min 2 steps** for promotion (confirmed)
   - Similarity calculation
   - Grouping algorithm
   - Task template generation

4. **Build Script 16: Top-Down Decomposer** (~3 hours)
   - File: `scripts/script_16_top_down_decomposer.py` (~400 lines)
   - **Vagueness threshold: 0.6** (confirmed)
   - Decomposition patterns: create/manage/integrate/deploy
   - **Pattern-based tool inference** (no ML)
   - Step sequence generation

5. **Build Script 17: Checklist Generator** (~2 hours)
   - File: `scripts/script_17_checklist_generator.py` (~250 lines)
   - Convert atomic actions to checklist items
   - Duration estimation (30s - 2min)
   - Parent step linking

6. **Build Script 18: Phase 4 Integrator** (~2 hours)
   - File: `scripts/script_18_phase4_integrator.py` (~300 lines)
   - Merge all outputs
   - Validate hierarchy
   - **Generate manual review reports** (confirmed)
   - Flag items requiring review

7. **Update config.json** (~30 min)
   - Version 1.1 → 1.2
   - Add phase_4_output path
   - Add granularity settings
   - Add tool patterns

8. **Create Documentation** (~2 hours)
   - File: `Processed/PHASE_4_IMPLEMENTATION.md`
   - Manual review workflow guide
   - Examples for each tier
   - Testing procedures

9. **Test & Validate** (~2 hours)
   - Run on Phase 3 output
   - Validate classifications
   - Check manual review workflow
   - Measure token impact

---

## User Decisions (Confirmed)

1. ✅ **Duration estimates:** Approved
   - Checklist: < 2 min
   - Step: 3-10 min
   - Task: 30min - 4 hours

2. ✅ **Promotion:** Min **2 steps** (not 3)

3. ✅ **Vagueness threshold:** **0.6** (60%)

4. ✅ **Tool inference:** **Pattern matching** (not ML)

5. ✅ **TASK_MANAGERS:** **Manual review first** (not auto-populate)

6. ✅ **Chat logs:** Save to `C:\Users\Dell\Dropbox\ENTITIES\LOG`

---

## Key Technical Details

### Granularity Classification

**Tier 1: Checklist Items (Atomic)**
- Verbs: click, open, save, upload, download, delete, close, select, copy, paste, login, logout
- Duration: < 2 minutes
- No decision-making

**Tier 2: Step Templates (Execution Units)**
- Verbs: configure, setup, create, analyze, review, process, execute
- Duration: 3-10 minutes
- Requires specific tool
- Contains 2-5 checklist items

**Tier 3: Task Templates (Work Packages)**
- Duration: 30min - 4 hours
- Contains 2-8 step templates (min 2 for promotion)
- Multiple tools
- Complete deliverable

### Bottom-Up Promotion

**Grouping Criteria:**
- Same department/domain
- Sequential action flow
- Shared tools (at least 1 overlap)
- Common deliverable/goal

**Promotion Criteria:**
- Min 2 steps in group
- Coherent sequence OR shared deliverable
- Tool variety preferred but not required

### Top-Down Decomposition

**Vagueness Detection (≥0.6):**
```python
vague_verbs = ['manage', 'handle', 'coordinate', 'oversee', 'improve', 'optimize']
abstract_objects = ['workflow', 'process', 'system', 'framework']

score = (
    has_vague_verb * 0.3 +
    has_abstract_object * 0.2 +
    no_tools_specified * 0.2 +
    high_skill_level * 0.3
)
```

**Decomposition Patterns:**
- **create:** research → design → implement → test → document
- **manage:** assess → plan → execute → monitor → adjust
- **integrate:** review → configure → test → validate → troubleshoot
- **deploy:** review → configure → execute → validate → document

**Tool Patterns:**
```python
{
    'research': 'Documentation',
    'design': 'Figma',
    'implement': 'VS Code',
    'test': 'Testing Framework',
    'document': 'Markdown Editor',
    'configure': 'Settings Panel',
    'execute': 'CLI/Terminal',
    'validate': 'Review Tools',
    'monitor': 'Dashboard'
}
```

---

## Output Structure

### Phase 4 Main Output
```
Processed/Phase_4_Output/
├── phase_4_task_hierarchy_daily_{id}.json  (structured data, ~400 tokens)
└── phase_4_review_daily_{id}.md            (manual review report)
```

### Manual Review Workflow
1. Script generates outputs
2. Human reviews `phase_4_review_daily_{id}.md`
3. Validates classifications and decompositions
4. Approves templates for TASK_MANAGERS
5. Manual sync (not automatic)

---

## Session Logs

All work logged to: `C:\Users\Dell\Dropbox\ENTITIES\LOG`

Previous session log:
- `LOG/session_2025-11-20_*_phase3_complete_Phase 3 Implementation Session.md`

---

## Quick Commands

### Test Phase 3 (verify working)
```bash
cd C:\Users\Dell\Dropbox\ENTITIES\DAILIES
python scripts/script_12_phase3_data_structurer.py --config scripts/config.json --file phase_2_test_verb_forms.md
```

### Run Phase 4 (after implementation)
```bash
# Classifier
python scripts/script_14_granularity_classifier.py --config scripts/config.json

# Integrator (runs all Phase 4 steps)
python scripts/script_18_phase4_integrator.py --config scripts/config.json
```

---

## Files to Reference

### Existing Code Patterns
- `script_12_phase3_data_structurer.py` - Data processing patterns
- `script_10_form_classifier.py` - Classification logic
- `script_11_learning_extractor.py` - Extraction patterns
- `utils_session_logger.py` - Logging integration

### Documentation
- `PHASE_3_IMPLEMENTATION.md` - Reference for Phase 4 doc structure
- `PMT-070_Phase_3_Data_Structuring.md` - Prompt structure example

### Configuration
- `scripts/config.json` - Current v1.1, update to v1.2

---

## Estimated Timeline

**Total:** ~19.5 hours

**Can be broken into:**
- Session 1: Prompt + Script 14 + Script 15 (~8 hours)
- Session 2: Script 16 + Script 17 + Script 18 (~8 hours)
- Session 3: Config + Docs + Testing (~3.5 hours)

---

**Ready to begin Phase 4 implementation!** 🚀

Start with: Creating PMT-070-P4 prompt
