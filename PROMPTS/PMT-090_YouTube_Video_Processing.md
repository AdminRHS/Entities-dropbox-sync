# YouTube Video Processing with Custom Instructions

**Purpose**: Process YouTube videos using AI Studio with Gemini model following custom instruction file for transcription and analysis.

**Version**: 1.0  
**Date**: 2025-11-21  
**Status**: Active  
**Related Prompts**: PMT-004_Video_Transcription_v4.1.md

---

## Overview

This workflow processes YouTube videos through AI Studio using the Gemini model, following a custom instruction file for transcription and content analysis. The custom instructions file provides specific guidelines for video processing.

**Primary Use Case**: Processing YouTube videos with standardized transcription and analysis  
**Target Platform**: AI Studio (Google) with Gemini model  
**Department**: Multi (used across departments for video content)

---

## Prompt Instructions

### Base Processing Prompt

```
*choose gemini model*

please process this video following the instructions file

[Attach YouTube link]
[Attach video instructions file]
```

### Custom Instructions File

**Location**: Dropbox link (or local file)  
**Format**: Markdown file with video processing instructions  
**Example**: `Video_Transcription_Custom_Instructions.md`

**File Reference**: `https://www.dropbox.com/scl/fi/7niv2qtxawlzh2w7og3qy/Video_Transcription_Custom_Instructions.md?rlkey=8ckwk5xrkvw48jw74tlgx0tj5&st=npijokbj&dl=0`

---

## Usage Workflow

### Step 1: Prepare Materials
1. Obtain YouTube video URL
2. Access custom instructions file (download if needed)
3. Open AI Studio
4. Select Gemini model

### Step 2: Execute Processing
1. Attach YouTube video link
2. Attach custom instructions file
3. Run processing prompt
4. Wait for AI processing

### Step 3: Review Output
1. Verify transcription accuracy
2. Check analysis completeness
3. Validate format compliance
4. Export results if needed

---

## Input Requirements

### Required Materials
- ✅ **YouTube Video URL**: Valid, accessible video link
- ✅ **Custom Instructions File**: Markdown file with processing guidelines
- ✅ **AI Studio Access**: Google account with AI Studio access
- ✅ **Gemini Model**: Available in AI Studio

### Custom Instructions File Structure
The instructions file should contain:
- Transcription format requirements
- Analysis sections to extract
- Output structure guidelines
- Quality standards

---

## Expected Output Structure

Based on custom instructions file, output typically includes:
- **Video Transcription**: Full text transcript
- **Content Analysis**: Key topics and themes
- **Structured Sections**: Organized by instruction file format
- **Metadata**: Video information, duration, etc.

---

## Examples

### Example Input
**YouTube Video**: `https://www.youtube.com/watch?v=example123`  
**Instructions File**: `Video_Transcription_Custom_Instructions.md`

### Example Output
- Full transcript in specified format
- Analysis sections as per instructions
- Structured data extraction
- Quality metrics

---

## Best Practices

- ✅ Always use Gemini model in AI Studio
- ✅ Verify custom instructions file is accessible
- ✅ Check YouTube video accessibility
- ✅ Review output against instruction requirements
- ✅ Save custom instructions file locally for reference
- ❌ Don't process without instruction file
- ❌ Don't use wrong model (must be Gemini)

---

## Dependencies

- **Custom Instructions File**: Required for processing
- **AI Studio Access**: Google account needed
- **Gemini Model**: Must be available in AI Studio

---

## Version History

- v1.0 (2025-11-21): Initial integration from personal prompts collection

