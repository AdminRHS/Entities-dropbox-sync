# Bronze Library - Video Research Collection

This file maps the "Bronze Library" of video research files to importable sample data for the Research Management System.

---

## 📺 What is the Bronze Library?

The **Bronze Library** refers to processed video research files stored in:
- **Primary Location**: `C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_3\Reports_week 3_Source\ARCHIVE\Videos\`
- **Secondary Location**: `C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES\03_ANALYSIS\Library_Mapping\`

### Current Video Files:
- Video_001.md through Video_018.md (Existing)
- Video_022.md and beyond (To be created)

Each Video file contains:
- Video title and description
- Full transcription with timestamps
- Video content breakdown
- YouTube URL and metadata

---

## 🔗 Connection to Sample Data

The **Bronze Library** videos have been converted to CSV format for bulk import:

**File**: `video_bronze_library.csv` (22 videos)

This CSV contains realistic video data based on the pattern found in Video_001.md and similar files. Each row represents a video ready for import into the Research Management System.

---

## 📊 Bronze Library CSV Structure

```csv
video_url,video_title,channel_name,duration_minutes,priority,department,assigned_to,notes,perplexity_search_id
https://youtube.com/watch?v=abc123,How To Use AI Agents to 10x Your Creative AI Game,Startup Ideas Podcast,20,high,AID,alex@remotehelpers.com,GLIF tutorial for AI agents and creative workflows,search_001
```

### Fields:
- **video_url**: YouTube video URL
- **video_title**: Title from Video_###.md files
- **channel_name**: YouTube channel name
- **duration_minutes**: Video length
- **priority**: low/medium/high
- **department**: DEV, SMM, VID, AID, DGN, MKT
- **assigned_to**: Team member email
- **notes**: Brief description
- **perplexity_search_id**: Link to search_queue entry

---

## 🎯 Video Categories in Bronze Library

### Development (DEV) - 7 videos
- MCP Server integration
- n8n automation
- Supabase security
- React Hook Form validation
- TypeScript best practices
- Redis caching
- API integration

### Social Media Marketing (SMM) - 5 videos
- AI caption tools
- TikTok content strategy
- Instagram reels
- YouTube SEO
- Social growth hacks

### Video Production (VID) - 2 videos
- Adobe Premiere AI features
- AI video generation (Runway)

### AI & Automation (AID) - 4 videos
- AI agents and creative AI (Video_001 actual)
- ChatGPT API integration
- Perplexity AI research
- AI workflow automation

### Design (DGN) - 4 videos
- Figma to React
- Brand identity design
- Canva AI tools
- Midjourney prompting

### Marketing (MKT) - 3 videos
- Google Analytics setup
- Email automation
- Notion AI project management

---

## 📁 Creating New Video Files

### Format for Video_022.md and beyond:

```markdown
Video Title: [YouTube Title]
Video Description:
[Full description from YouTube]

Timestamps:
00:00 - Section 1
05:30 - Section 2
10:00 - Section 3

Video Subtitles:
[If available, or "No subtitles exist"]

Video content:
[00:00] Transcribed content here...
[00:26] More content...
```

### Video_022 Example:
```markdown
Video Title: Redis Caching Strategies for APIs
Video Description:
Learn advanced Redis caching strategies for high-performance APIs. This tutorial covers:
- Redis fundamentals and data structures
- Cache invalidation patterns
- Distributed caching with Redis Cluster
- Performance optimization techniques
- Real-world case studies

Timestamps:
00:00 - Introduction to Redis caching
02:15 - Cache vs Database trade-offs
05:30 - Implementing cache-aside pattern
10:00 - Cache invalidation strategies
15:00 - Redis Cluster configuration
20:00 - Performance benchmarking
25:00 - Production deployment tips

Video content:
[00:00] Today we're diving deep into Redis caching strategies...
```

---

## 🔄 How to Use Bronze Library Data

### Step 1: Import Videos from Bronze Library CSV

1. Navigate to bulk import screen (if created)
2. Upload `video_bronze_library.csv`
3. Validate 22 rows
4. Import to `video_queue` table

### Step 2: Link to Actual Video Files

Each imported video can be linked to its corresponding Video_###.md file:

| CSV Row | Maps To | Location |
|---------|---------|----------|
| Row 1 (AI Agents) | Video_001.md | ARCHIVE/Videos/Video_001.md |
| Row 2 (MCP Servers) | Video_022.md | (To be created) |
| Row 3 (n8n Workflow) | Video_023.md | (To be created) |

### Step 3: Extract Video Transcriptions

Once videos are in the queue, upload their transcriptions:

1. Read content from Video_###.md "Video content" section
2. Create .txt file with timestamps
3. Upload to transcription screen
4. Link to video_id in database

---

## 📝 Creating New Bronze Library Entries

### Workflow:

1. **Research Phase** (Phase 0):
   - Use Perplexity to find videos
   - Add to search_queue table
   - Select videos for processing

2. **Video File Creation** (Manual):
   - Create Video_###.md in ARCHIVE/Videos/
   - Include full transcription
   - Add timestamps and metadata

3. **CSV Export** (Automated):
   - Extract metadata from Video_###.md
   - Add row to bronze_library.csv
   - Include all required fields

4. **Import to System**:
   - Bulk import CSV to video_queue
   - Upload transcription files
   - Begin Phase 2 (entity extraction)

---

## 🗂️ Bronze Library File Structure

```
ENTITIES/
├── DAILIES/REPORTS/Week_3/Reports_week 3_Source/ARCHIVE/Videos/
│   ├── Video_001.md ✅ (AI Agents - GLIF tutorial)
│   ├── Video_002.md ✅
│   ├── Video_003.md ✅
│   ├── ...
│   ├── Video_018.md ✅
│   ├── Video_022.md ❌ (To create - Redis Caching)
│   ├── Video_023.md ❌ (To create - n8n Workflow)
│   └── ...
│
├── TASK_MANAGERS/RESEARCHES/
│   ├── PROMPTS/
│   │   ├── PMT-044_Sales_Department_Research.md
│   │   ├── PMT-047_YouTube_AI_HR_Tutorials.md
│   │   └── ...
│   └── 03_ANALYSIS/Library_Mapping/
│       ├── Video_001_Library_Mapping_Report.md
│       ├── Video_002_Library_Mapping_Report.md
│       └── ...
│
└── PROMPTS/research_app/screen_apps/sample_data/
    ├── video_bronze_library.csv ✅ (22 videos for import)
    ├── video_import_template.csv
    └── ...
```

---

## 🎯 Next Steps

### To expand Bronze Library:

1. **Create Video_022.md** with Redis Caching content
2. **Create Video_023.md** with n8n Automation content
3. Continue through Video_043.md (to match 22 CSV rows)

### To use in Research Management System:

1. **Import CSV**: Load all 22 videos at once
2. **Upload Transcriptions**: Link .txt/.srt/.vtt files
3. **Extract Entities**: Phase 2 processing
4. **Gap Analysis**: Phase 3 comparison
5. **Knowledge Mapping**: Phase 5 visualization

---

## 📚 Related Files

- **Main Library**: `video_bronze_library.csv` (This file)
- **Import Template**: `video_import_template.csv` (Smaller sample)
- **Transcriptions**: `sample_transcription.txt/srt/vtt`
- **Exports**: `exported_entities_*.json`

---

## 💡 Bronze Library Philosophy

**Why "Bronze"?**
- **Bronze** = Raw processed data (first level of refinement)
- **Silver** = Extracted entities and structured knowledge
- **Gold** = Validated, integrated knowledge in production

The Bronze Library represents the **foundational layer** of video research data that feeds into the entire Research Management System pipeline.

---

**Created:** 2025-11-28
**Purpose:** Map Bronze Library videos to importable CSV data
**Maintained by:** Research Management System Team

**Current Status:**
- ✅ 18 Video files exist (Video_001 - Video_018)
- ✅ 22 CSV rows created
- ❌ 4 Video files needed (Video_022 - Video_025+)
