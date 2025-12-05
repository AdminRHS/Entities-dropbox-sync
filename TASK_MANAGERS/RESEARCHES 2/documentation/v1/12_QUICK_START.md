# RESEARCHES 2 - Quick Start Guide

**Generated:** 2025-12-04
**Purpose:** Get started with the RESEARCHES 2 system quickly
**Audience:** New users, all skill levels

---

## 🚀 Welcome!

This guide will help you get started with the RESEARCHES 2 video research and taxonomy integration system in under 30 minutes.

---

## ⚡ 5-Minute Overview

### What is RESEARCHES 2?

A system that:
1. **Searches** for educational videos
2. **Manages** video queue and priorities
3. **Transcribes** videos with AI assistance
4. **Extracts** entities (tools, workflows, actions, objects)
5. **Analyzes** gaps in your knowledge base
6. **Integrates** entities into taxonomy
7. **Documents** everything with reports

### The 7-Phase Workflow

```
Search → Queue → Transcribe → Extract → Analyze → Integrate → Document
  (0)     (0→1)     (1)        (2)       (3)        (4)        (5)
```

### Time Investment
- **Setup:** 10 minutes
- **First video:** 4-5 hours
- **Subsequent videos:** 3-4 hours
- **With experience:** 2-3 hours

---

## 📋 Prerequisites

### Required
- Access to this folder: `G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES 2`
- Python 3.8+ installed
- AI assistant access (Claude/ChatGPT/Gemini)
- Basic markdown knowledge

### Optional
- YouTube account (for metadata)
- VS Code or text editor
- Git for version control

---

## 🎯 Your First 30 Minutes

### Minute 1-5: Explore the System

**Open these folders:**
```
RESEARCHES 2/
├── 00_SEARCH_QUEUE/     ← Video search tasks
├── 01_VIDEO_QUEUE/      ← Video priority queue
├── 02_TRANSCRIPTIONS/   ← Transcribed videos
├── PROMPTS/             ← Processing prompts
└── scripts/             ← Automation scripts
```

**Quick look:**
- Browse `02_TRANSCRIPTIONS/` → See example Video_001.md
- Open `PROMPTS/` → See PMT-004, PMT-007, PMT-009
- Check `scripts/` → See Python automation files

### Minute 6-10: Understand the Workflow

**Read this:**

**Phase 0: Search**
- Assign video search task
- Employee searches with AI
- Discovers 15-20 videos

**Phase 0→1: Queue**
- Add all videos to queue
- System prioritizes (0-100 score)
- Select top 3-5 for processing

**Phase 1: Transcribe**
- Use PMT-004 prompt
- AI extracts 37+ entities
- Save as Video_XXX.md

**Phase 2-5: Process**
- Extract (PMT-007)
- Analyze gaps (PMT-009 Part 1)
- Create JSON files (PMT-009 Part 2)
- Generate report (PMT-009 Part 3)

### Minute 11-15: Install Scripts (Optional)

**If using Python automation:**

```bash
cd "G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES 2"

# Install dependencies
pip install pandas requests python-dateutil yt-dlp

# Test installation
python scripts/video_id_scanner.py
```

If successful, you'll see ID scan results.

### Minute 16-20: Find a Video

**Practice video search:**

1. Pick a topic (e.g., "AI design tools")
2. Go to Perplexity AI
3. Use this search:
   ```
   Find 5 recent YouTube videos (last 30 days) with step-by-step
   tutorials on AI design tools. Focus on Figma AI plugins and
   Midjourney workflows. Videos should be 10-20 minutes long.
   ```
4. Get 5-10 video URLs

### Minute 21-25: Add Videos to Queue

**Manual method (quick):**

Create a file `video_urls.txt`:
```
https://youtube.com/watch?v=VIDEO1
https://youtube.com/watch?v=VIDEO2
https://youtube.com/watch?v=VIDEO3
```

**Script method (better):**

```bash
python 01_VIDEO_QUEUE/scripts/add_video_to_queue_simple.py "VIDEO_URL"
```

For each video URL.

### Minute 26-30: Review Queue

**Open the dashboard:**
```
01_VIDEO_QUEUE/Video_Queue_Dashboard.html
```

Double-click to open in browser.

**What you'll see:**
- All queued videos
- Priority scores
- Metadata (title, channel, duration)
- Status (Queued, Selected, etc.)

---

## 🎓 Your First Video Processing

Now let's process one video completely (4-5 hours total).

### Step 1: Select Video (5 minutes)

**From queue dashboard:**
1. Sort by priority (high to low)
2. Pick highest priority video
3. Note the Queue ID (e.g., VQ-103)

**Update status:**
```bash
python 01_VIDEO_QUEUE/scripts/update_queue_status.py update VQ-103 Selected "Your Name"
```

**Add to progress tracker:**
```bash
python scripts/update_video_progress.py add \
    24 \
    "Video Title Here" \
    "https://youtube.com/watch?v=VIDEO_ID" \
    "Your Name"
```

### Step 2: Get Transcript (15-30 minutes)

**Method 1: YouTube Auto-Transcript**
1. Open video on YouTube
2. Click "Show transcript"
3. Copy all text with timestamps
4. Save to text file

**Method 2: Use Tool**
- Use YouTube transcript extractor tools
- Download .srt or .txt file
- Ensure timestamps included

### Step 3: Transcribe with PMT-004 (1-2 hours)

**Open AI assistant (Claude/ChatGPT):**

1. Load prompt:
   ```
   Open: PROMPTS/PMT-004_Video_Transcription_v4.1.md
   (If in ENTITIES/PROMPTS, find it there)
   ```

2. Provide video info:
   ```
   Video URL: [URL]
   Video Title: [Title]
   Channel: [Channel Name]
   Duration: [Duration]

   Transcript:
   [Paste full transcript here]
   ```

3. AI will generate:
   - Full structured transcription
   - Video metadata
   - 37+ pre-categorized entities:
     * Workflows (WRF-###)
     * Tools (TOL-###)
     * Objects (OBJ-###)
     * Action verbs (categories A-G)
     * Integration patterns

4. Copy output to file:
   ```
   Save as: 02_TRANSCRIPTIONS/Video_024.md
   ```

5. Update progress:
   ```bash
   python scripts/update_video_progress.py update 24 Phase_1_Transcribed \
       "Used PMT-004 v4.1, extracted 45 entities"
   ```

### Step 4: Extract Entities (30-45 minutes)

**Use PMT-007 prompt:**

1. Open AI assistant
2. Load: `PROMPTS/PMT-007_Objects_Library_Extraction.md`
3. Provide:
   ```
   I have Video_024.md transcription.
   Please perform deep entity extraction following PMT-007.

   [Paste or attach Video_024.md]
   ```

4. AI extracts:
   - All object types
   - Complete cross-references
   - Tool → Object mappings
   - Profession → Object mappings

5. Save outputs:
   ```
   03_ANALYSIS/Extractions/Video_024_Phase3_Analysis.md
   03_ANALYSIS/Extractions/Video_024_Phase4_Objects.md
   ```

6. Update progress:
   ```bash
   python scripts/update_video_progress.py update 24 Phase_2_Extraction \
       "Extracted 68 entities with cross-references"
   ```

### Step 5: Run Gap Analysis (20-30 minutes)

**Automated method (recommended):**

```bash
python scripts/video_gap_analyzer.py Video_024
```

This will:
- Compare extracted entities vs LIBRARIES
- Identify NEW (needs creation) entities
- Identify EXISTING entities
- Identify UPDATE (needs enhancement) entities
- Calculate coverage metrics
- Generate gap analysis report

**Output:**
```
03_ANALYSIS/Gap_Analysis/Video_024_Gap_Analysis.md
```

**Update progress:**
```bash
python scripts/update_video_progress.py update 24 Phase_3_Gap_Analysis \
    "NEW: 28 | EXISTING: 35 | UPDATE: 5 | Coverage: 51% → 96%"
```

### Step 6: Integration (45-60 minutes)

**This is the most involved step - creating JSON files.**

**Option A: Semi-Automated (recommended):**

```bash
python scripts/video_json_updater.py Video_024
```

Script will:
- Read gap analysis
- Generate JSON templates
- Prompt for review
- Save to appropriate locations
- Update registries

**Option B: Manual:**

1. Use PMT-009 Part 2
2. Create JSON files for NEW entities
3. Update JSON files for existing entities
4. See [07_TAXONOMY_BUILDING.md](../v2/07_TAXONOMY_BUILDING.md) for templates

**Update progress:**
```bash
python scripts/update_video_progress.py update 24 Phase_4_Integration \
    "Created 28 JSON files, updated 5 files"
```

### Step 7: Generate Report (30-45 minutes)

**Automated:**

```bash
python scripts/video_integration_reporter.py Video_024 --include-cross-refs
```

Generates comprehensive report with:
- Coverage metrics
- Entity lists
- Cross-reference map
- Business value
- Recommendations

**Output:**
```
03_ANALYSIS/Library_Mapping/Video_024_Library_Mapping_Report.md
```

**Update to complete:**
```bash
python scripts/update_video_progress.py update 24 Complete \
    "All phases finished. Coverage: 51% → 96%"
```

### Step 8: Final Cleanup (5 minutes)

**Update queue status:**
```bash
python 01_VIDEO_QUEUE/scripts/update_queue_status.py update VQ-103 Completed
```

**Generate weekly report:**
```bash
python scripts/generate_progress_report.py weekly
```

---

## 🎉 Congratulations!

You've processed your first video! Here's what you accomplished:

✅ Found and queued videos
✅ Transcribed with 37+ entities
✅ Extracted detailed entities
✅ Analyzed gaps
✅ Integrated into taxonomy
✅ Generated comprehensive report

**Time spent:** 4-5 hours
**Entities added:** 28+ new
**Coverage improvement:** ~45%

---

## 📚 What's Next?

### To Get Faster
1. Process 2-3 more videos
2. Learn keyboard shortcuts
3. Create custom templates
4. Use automation scripts more

**Your speed will improve:**
- Video 2-3: 3-4 hours
- Video 4-5: 2-3 hours
- Video 6+: 2 hours

### To Go Deeper
Read detailed documentation:
- [03_SEARCH_QUEUE_COMPLETE.md](./03_SEARCH_QUEUE_COMPLETE.md)
- [04_VIDEO_QUEUE_COMPLETE.md](./04_VIDEO_QUEUE_COMPLETE.md)
- [05_TRANSCRIPTIONS_COMPLETE.md](./05_TRANSCRIPTIONS_COMPLETE.md)
- [06_ANALYSIS_COMPLETE.md](./06_ANALYSIS_COMPLETE.md)
- [07_INTEGRATION_COMPLETE.md](./07_INTEGRATION_COMPLETE.md)

### To Master the System
Study advanced topics:
- [08_SCRIPTS_DETAILED.md](./08_SCRIPTS_DETAILED.md) - All automation
- [09_PROMPTS_CATALOG.md](./09_PROMPTS_CATALOG.md) - All prompts
- [10_DATA_FILES.md](./10_DATA_FILES.md) - Data management
- [../v2/07_TAXONOMY_BUILDING.md](../v2/07_TAXONOMY_BUILDING.md) - Taxonomy deep dive

---

## 💡 Quick Tips

### Efficiency Tips
1. **Use scripts** - Automate what you can
2. **Batch process** - Do 3-5 videos at once
3. **Templates** - Reuse successful patterns
4. **Shortcuts** - Learn your AI assistant's shortcuts

### Quality Tips
1. **Read examples** - Study Video_001.md through Video_024.md
2. **Follow prompts** - PMT-004, PMT-007, PMT-009 are well-tested
3. **Verify entities** - Check extracted entities make sense
4. **Test cross-refs** - Ensure bidirectional links work

### Productivity Tips
1. **Phase 1 first** - Get good transcripts, everything else is easier
2. **Automate Phase 3** - Use video_gap_analyzer.py
3. **Use templates** - Copy-paste JSON structures
4. **Track progress** - Update progress tracker consistently

---

## 🆘 Common Issues

### "Script won't run"
```bash
# Reinstall dependencies
pip install --force-reinstall pandas requests python-dateutil

# Check Python version
python --version  # Should be 3.8+
```

### "Prompt is too long"
- Break into sections
- Process in 2-3 chunks
- Use Claude (100K+ context) instead of ChatGPT

### "Can't find files"
- Check you're in correct directory
- Use absolute paths
- Verify folder structure matches documentation

### "Entities not extracting well"
- Ensure full transcript provided
- Include video metadata
- Review PMT-004 instructions carefully
- Try different AI assistant (Claude vs ChatGPT)

### More Help
See [13_TROUBLESHOOTING.md](./13_TROUBLESHOOTING.md) for complete troubleshooting guide.

---

## 📞 Support

### Documentation
- **Master Index:** [00_MASTER_INDEX.md](./00_MASTER_INDEX.md)
- **All Files:** [02_ALL_FILES_INVENTORY.md](./02_ALL_FILES_INVENTORY.md)
- **Troubleshooting:** [13_TROUBLESHOOTING.md](./13_TROUBLESHOOTING.md)

### Original Documentation
- System README: `../README.md`
- System Overview: `../SYSTEM_OVERVIEW.md`
- Scripts Inventory: `../SCRIPTS_INVENTORY.md`

---

## ✅ Checklist for Success

### Before You Start
- [ ] Python installed
- [ ] Dependencies installed
- [ ] AI assistant access
- [ ] Folder access verified
- [ ] Example videos reviewed

### Your First Video
- [ ] Video found and queued
- [ ] Transcript obtained
- [ ] PMT-004 applied successfully
- [ ] Entities extracted (37+ minimum)
- [ ] Gap analysis run
- [ ] JSON files created
- [ ] Report generated
- [ ] Progress tracked

### Going Forward
- [ ] Understand all 7 phases
- [ ] Can use all core scripts
- [ ] Know all core prompts
- [ ] Process speed improving
- [ ] Quality staying high

---

## 🏁 Ready to Go!

You now have everything you need to:
- ✅ Find videos
- ✅ Process transcriptions
- ✅ Extract entities
- ✅ Integrate taxonomy
- ✅ Generate reports

**Next Action:** Find your first video and start Phase 0!

---

**Good luck! You've got this! 🚀**

---

*End of Quick Start Guide*
