# How to Reference Sample Data in Lovable Prompts

This guide shows you how to include sample data in your Lovable prompts for testing import/export features.

---

## ✅ Best Practice: Embed Sample Data Directly

**DO NOT** reference external files in Lovable prompts because:
- ❌ Lovable AI doesn't have access to your local files
- ❌ Links break when files move
- ❌ Lovable can't read .csv, .txt, .json files from URLs

**INSTEAD:** Copy the sample data content directly into your prompt

---

## 📋 Copy-Paste Templates for Lovable

### For CSV Import Features

When building screens with CSV upload (like bulk video import):

```markdown
## Sample CSV Data for Testing

Use this mock CSV data to test the import functionality:

\`\`\`csv
video_url,video_title,channel_name,duration_minutes,priority,department,assigned_to,notes
https://youtube.com/watch?v=abc123,Claude Desktop MCP Setup Tutorial,AI Explained,15,high,DEV,alex@remotehelpers.com,Great tutorial on MCP connectors
https://youtube.com/watch?v=xyz789,n8n Workflow Automation for Developers,Automation Pro,22,medium,DEV,maria@remotehelpers.com,Comprehensive automation guide
https://youtube.com/watch?v=def456,AI Caption Generator Tools Review,Social Media Masters,18,high,SMM,jordan@remotehelpers.com,Comparison of 5 caption tools
\`\`\`

When parsing this CSV:
- Use Papa Parse library
- Validate each row against the schema
- Show preview table before importing
```

---

### For JSON Import Features

When building screens with JSON upload:

```markdown
## Sample JSON Data for Testing

Use this mock JSON structure for testing:

\`\`\`json
[
  {
    "video_url": "https://youtube.com/watch?v=abc123",
    "video_title": "Claude Desktop MCP Setup Tutorial",
    "channel_name": "AI Explained",
    "duration_minutes": 15,
    "priority": "high",
    "department": "DEV",
    "assigned_to": "alex@remotehelpers.com",
    "notes": "Great tutorial on MCP connectors"
  },
  {
    "video_url": "https://youtube.com/watch?v=xyz789",
    "video_title": "n8n Workflow Automation for Developers",
    "channel_name": "Automation Pro",
    "duration_minutes": 22,
    "priority": "medium",
    "department": "DEV",
    "assigned_to": "maria@remotehelpers.com",
    "notes": "Comprehensive automation guide"
  }
]
\`\`\`

Expected behavior:
- Parse JSON array
- Validate each object
- Display in preview table
```

---

### For Transcription Upload Features

When building screens with transcription file upload:

```markdown
## Sample Transcription Data for Testing

### Plain Text Format (.txt)

\`\`\`
00:00:00 - Introduction
Hello everyone, and welcome to this comprehensive tutorial on setting up MCP servers in Claude Desktop.

00:00:15 - What is MCP?
The Model Context Protocol, or MCP, allows Claude Desktop to connect to external tools and data sources.

00:00:45 - Prerequisites
Before we begin, make sure you have the following installed:
- Claude Desktop application (latest version)
- Node.js version 18 or higher
\`\`\`

### SRT Format (.srt)

\`\`\`
1
00:00:00,000 --> 00:00:15,000
Hello everyone, and welcome to this comprehensive tutorial on setting up MCP servers in Claude Desktop.

2
00:00:15,000 --> 00:00:45,000
The Model Context Protocol, or MCP, allows Claude Desktop to connect to external tools and data sources.
\`\`\`

### VTT Format (.vtt)

\`\`\`
WEBVTT

00:00:00.000 --> 00:00:15.000
Hello everyone, and welcome to this comprehensive tutorial on setting up MCP servers in Claude Desktop.

00:00:15.000 --> 00:00:45.000
The Model Context Protocol, or MCP, allows Claude Desktop to connect to external tools and data sources.
\`\`\`

File validation:
- Accept: .txt, .srt, .vtt
- Max size: 10 MB
- Preview first 500 characters
```

---

### For Export Features (JSON)

When building screens with JSON export:

```markdown
## Export Functionality

When user clicks "Export JSON", create a file like this:

\`\`\`typescript
function exportToJSON(data: any[], type: string) {
  const json = JSON.stringify(data, null, 2);
  const blob = new Blob([json], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = \`extracted_\${type}_\${new Date().toISOString()}.json\`;
  a.click();
}
\`\`\`

Sample exported structure:

\`\`\`json
[
  {
    "id": "1",
    "entity_type": "TOOL",
    "entity_name": "Claude Desktop",
    "entity_id": "TOOL-AI-224",
    "classification": "NEW",
    "category": "AI",
    "confidence_score": 0.95,
    "metadata": {
      "pricing": "Free + Pro ($20/mo)",
      "platform": "Desktop (Mac/Windows)"
    }
  }
]
\`\`\`
```

---

## 🎯 Complete Example: Bulk Import Screen Prompt

Here's how to write a complete Lovable prompt with embedded sample data:

````markdown
Build a Bulk Video Import screen with CSV/JSON upload.

Tech stack: React 18 + TypeScript + Vite + Supabase + shadcn/ui + Papa Parse

Features:
- Drag & drop CSV/JSON file upload
- Parse and validate data
- Preview in table before importing
- Highlight validation errors
- Bulk insert to Supabase

## Mock CSV Data for Testing

\`\`\`csv
video_url,video_title,department,priority
https://youtube.com/watch?v=abc123,Claude Desktop Tutorial,DEV,high
https://youtube.com/watch?v=xyz789,n8n Automation Guide,DEV,medium
https://youtube.com/watch?v=def456,AI Caption Tools,SMM,high
\`\`\`

## Validation Rules

Create Zod schema:

\`\`\`typescript
const videoRowSchema = z.object({
  video_url: z.string().url('Must be valid URL'),
  video_title: z.string().min(3, 'Min 3 characters'),
  department: z.enum(['DEV', 'SMM', 'VID', 'AID', 'DGN', 'MKT']),
  priority: z.enum(['low', 'medium', 'high']).default('medium')
});
\`\`\`

## CSV Parsing Code

\`\`\`typescript
import Papa from 'papaparse';

function parseCSV(file: File) {
  Papa.parse(file, {
    header: true,
    skipEmptyLines: true,
    complete: (results) => {
      const validated = results.data.map(row => {
        try {
          return videoRowSchema.parse(row);
        } catch (error) {
          return { ...row, _error: error.message };
        }
      });
      setImportData(validated);
    }
  });
}
\`\`\`

## Preview Table

Show parsed data in TanStack Table:
- Column: Status (✓ Valid / ✗ Invalid)
- Column: Video URL
- Column: Title
- Column: Department
- Column: Priority
- Column: Errors (if any)

Rows with errors: Red background
Valid rows: Normal background

## Import Button

\`\`\`typescript
async function handleImport() {
  const validRows = importData.filter(row => !row._error);

  const { error } = await supabase
    .from('video_queue')
    .insert(validRows);

  if (!error) {
    toast.success(\`Imported \${validRows.length} videos\`);
  }
}
\`\`\`

Disable button if no valid rows.
Show progress bar during import.

## Download Template Button

\`\`\`typescript
function downloadTemplate() {
  const template = \`video_url,video_title,department,priority
https://youtube.com/watch?v=EXAMPLE,Example Title,DEV,medium\`;

  const blob = new Blob([template], { type: 'text/csv' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'video_import_template.csv';
  a.click();
}
\`\`\`
````

---

## ❌ What NOT to Do

### DON'T: Reference external files

```markdown
❌ BAD:
"Load sample data from sample_data/video_import_template.csv"
"Read the CSV file at path/to/file.csv"
"Import data from attached file"
```

### DON'T: Use file paths or URLs

```markdown
❌ BAD:
"Use this file: C:\Users\...\sample.csv"
"Download from: https://example.com/data.csv"
"See attached file for sample data"
```

### DON'T: Assume file access

```markdown
❌ BAD:
"Parse the CSV file in the sample_data folder"
"Load JSON from local filesystem"
"Read transcription from uploaded file"
```

---

## ✅ What TO Do

### DO: Embed data inline

```markdown
✅ GOOD:
"Use this mock CSV data for testing:

\`\`\`csv
video_url,video_title,department
https://youtube.com/watch?v=abc,Tutorial,DEV
\`\`\`
"
```

### DO: Show expected structure

```markdown
✅ GOOD:
"Parsed data should look like this:

\`\`\`typescript
const parsed: VideoRow[] = [
  {
    video_url: 'https://...',
    video_title: 'Tutorial',
    department: 'DEV',
    _validation_status: 'valid'
  }
];
\`\`\`
"
```

### DO: Include validation examples

```markdown
✅ GOOD:
"Examples of invalid data:

\`\`\`json
{
  "video_url": "not-a-url",  // ❌ Invalid URL
  "video_title": "ab",       // ❌ Too short (min 3)
  "department": "INVALID"    // ❌ Not in enum
}
\`\`\`
"
```

---

## 🔄 Workflow for Using Sample Data

### Step 1: Choose Your Sample
Pick from `sample_data/` directory:
- CSV import → `video_import_template.csv`
- JSON import → `video_import_sample.json`
- Transcription → `sample_transcription.txt/srt/vtt`
- Export → `exported_entities_*.json`

### Step 2: Copy Content
Open the file and copy its contents completely

### Step 3: Embed in Prompt
Paste into Lovable prompt within code blocks:

````markdown
\`\`\`csv
[paste CSV content here]
\`\`\`

\`\`\`json
[paste JSON content here]
\`\`\`

\`\`\`
[paste TXT content here]
\`\`\`
````

### Step 4: Add Context
Explain what the data represents and how to use it

### Step 5: Show Validation
Include expected validation rules and error cases

---

## 📚 Quick Reference by Screen

| Screen | Sample File | What to Copy | Where to Paste |
|--------|-------------|--------------|----------------|
| Bulk Import | `video_import_template.csv` | Full CSV content | "Sample CSV Data" section |
| Bulk Import | `video_import_sample.json` | Full JSON array | "Sample JSON Data" section |
| Upload Transcription | `sample_transcription.txt` | First 20 lines | "Sample Text Format" section |
| Upload Transcription | `sample_transcription.srt` | First 3 entries | "Sample SRT Format" section |
| Upload Transcription | `sample_transcription.vtt` | First 3 entries | "Sample VTT Format" section |
| Entity Extraction | `exported_entities_tools.json` | 2-3 entries | "Export Structure" section |
| Gap Analysis | `exported_entities_workflows.json` | 2-3 entries | "Workflow Format" section |

---

## 💡 Pro Tips

1. **Keep samples concise**: Use 3-5 rows in prompts, full file for actual testing
2. **Show variety**: Include valid, invalid, and edge cases
3. **Format properly**: Use code blocks with correct language tags
4. **Add comments**: Explain what each field represents
5. **Include errors**: Show what validation failures look like
6. **Test locally**: Use full sample files for actual upload testing

---

**Created:** 2025-11-28
**Purpose:** Guide for referencing sample data in Lovable prompts
