# VIDEO_RESEARCHES Source Mapping

**Created:** 2025-11-20
**Purpose:** Map existing video-related assets for integration into VIDEO_RESEARCHES

---

## 1. PROMPTS/Video_Processing

| Source File | Domain | Type | Target Location | Action |
|-------------|--------|------|-----------------|--------|
| `Analysis/PMT-006_Video_Analysis.md` | VID | Prompt | RESEARCHES/PROMPTS | Reference |
| `Analysis/PMT-007_Objects_Library_Extraction.md` | VID | Prompt | RESEARCHES/PROMPTS | Reference |
| `Analysis/PMT-008_Video_Analysis_Improvements.md` | VID | Prompt | RESEARCHES/PROMPTS | Reference |
| `Analysis/PMT-071_Actions_Library_Extraction.md` | VID | Prompt | RESEARCHES/PROMPTS | Reference |
| `Taxonomy_Integration/PMT-009_Taxonomy_Integration.md` | VID | Prompt | RESEARCHES/PROMPTS | Reference |
| `Transcription/PMT-004_Video_Transcription_v4.1.md` | VID | Prompt | RESEARCHES/PROMPTS | Reference |
| `Transcription/PMT-005_Video_Naming_Alternatives.md` | VID | Prompt | RESEARCHES/PROMPTS | Reference |
| `Workflows/PMT-010_Complete_Workflow_Full.md` | VID | Workflow | RESEARCHES/PROMPTS | Reference |
| `Workflows/PMT-011_Complete_Workflow_Short.md` | VID | Workflow | RESEARCHES/PROMPTS | Reference |
| `Workflows/PMT-012_Transcript_Processing_Workflow.md` | VID | Workflow | RESEARCHES/PROMPTS | Reference |

**Recommendation:** Keep prompts in PROMPTS/Video_Processing. Create links/references in RESEARCHES/PROMPTS for research context.

---

## 2. REPORTS/Influencer_Tracking

| Source File | Domain | Type | Target Location | Action |
|-------------|--------|------|-----------------|--------|
| `Influencer_Database.json` | VID/SMM | Data | RESEARCHES/DATA | Reference |
| `YouTube_Channels.json` | VID/SMM | Data | RESEARCHES/DATA | Reference |
| `README.md` | VID/SMM | Documentation | N/A | Reference |

**Recommendation:** Reference data files for research analysis. Keep source in REPORTS for tracking purposes.

---

## 3. REPORTS/Videos

| Source File | Domain | Type | Target Location | Action |
|-------------|--------|------|-----------------|--------|
| `Reports/Video_001_Library_Mapping_Report.md` | VID | Analysis | RESEARCHES/REPORTS | Reference |
| `Reports/Video_002_Extraction_Inventory.md` | VID | Analysis | RESEARCHES/REPORTS | Reference |
| `Reports/Video_002_Gap_Analysis.md` | VID | Gap Analysis | RESEARCHES/REPORTS | Link |
| `Reports/Video_002_Library_Mapping_Report.md` | VID | Analysis | RESEARCHES/REPORTS | Reference |
| `Reports/Video_005_Library_Mapping_Report.md` | VID | Analysis | RESEARCHES/REPORTS | Reference |
| `Reports/Video_009_Gap_Analysis.md` | VID | Gap Analysis | RESEARCHES/REPORTS | Link |
| `Reports/Video_009_Library_Mapping_Report.md` | VID | Analysis | RESEARCHES/REPORTS | Reference |
| `Videos_015.md` - `Video_016.md` | VID | Processing | N/A | Reference only |
| `VIDEOS_INDEX.md` | VID | Index | RESEARCHES/DATA | Reference |
| `Video_Discovery_Pipeline.md` | VID | Pipeline | RESEARCHES/REPORTS | Link |

**Recommendation:** Gap analyses and research-oriented reports should be linked to RESEARCHES/REPORTS. Video processing summaries stay in REPORTS/Videos.

---

## 4. Migration Plan

### Phase 1: Reference Links (Immediate)
- Create reference documents in VIDEO_RESEARCHES pointing to existing assets
- No file movement required
- Preserves PMT and RPT references

### Phase 2: Research Aggregation (Short-term)
- Create consolidated research views in RESEARCHES/REPORTS
- Link gap analyses and methodology documents
- Build research indexes

### Phase 3: Active Research (Ongoing)
- New video research created directly in VIDEO_RESEARCHES
- Existing PROMPTS/Video_Processing prompts remain as operational prompts
- REPORTS/Videos continues for video processing outputs

---

## 5. Integration Notes

### Maintaining Consistency
- PMT-### IDs remain in PROMPTS entity
- RPT-### IDs remain in REPORTS entity
- New research uses RSH-VID-### IDs

### Cross-References
All VIDEO_RESEARCHES documents should include:
- Source file paths
- Original PMT/RPT IDs where applicable
- TASK_MANAGERS task references

---

*Mapping completed: 2025-11-20*
