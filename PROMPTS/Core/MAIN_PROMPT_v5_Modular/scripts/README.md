# scripts - Assembly Scripts for Generating Combined Versions

**Purpose:** Python scripts to assemble modular files into monolithic and specialized versions of MAIN_PROMPT v5.

**Files in this folder:** 4 (3 scripts + this README)
**Update Frequency:** When assembly logic needs modification

---

## Scripts

### assemble_full_prompt.py
**Purpose:** Generate complete monolithic MAIN_PROMPT_v5.md from all modular files

**Usage:**
```bash
python assemble_full_prompt.py
```

**Output:**
- **File:** `../MAIN_PROMPT_v5.md` (in Core folder)
- **Size:** ~119KB (similar to v4)
- **Lines:** ~2,500-3,000 lines
- **Includes:** ALL content from all folders

**Features:**
- Combines all ~50 modular files in correct order
- Adds table of contents with navigation links
- Includes metadata (file count, total size, last updated date)
- Preserves all formatting and structure
- Validates markdown syntax
- Creates backup of previous version

**Algorithm:**
1. Read files from 00_Core/ (in order)
2. Read files from 01_Library_Integration/ (in order)
3. Read files from 02_Output_Templates/ (in order)
4. Read files from 03_Processing_Rules/ (in order)
5. Read files from 04_Usage/ (in order)
6. Generate table of contents
7. Add navigation links between sections
8. Insert metadata block at top
9. Validate markdown
10. Write to MAIN_PROMPT_v5.md

### assemble_department.py
**Purpose:** Create department-specific versions with filtered content

**Usage:**
```bash
python assemble_department.py --dept AI
python assemble_department.py --dept Design
python assemble_department.py --dept Dev
```

**Options:**
- `--dept` (required): AI, Video, Sales, Design, Dev, HR, LG, AI

**Output:**
- **File:** `../MAIN_PROMPT_v5_[DEPT].md`
- **Example:** `MAIN_PROMPT_v5_AI.md`, `MAIN_PROMPT_v5_Design.md`

**Features:**
- Includes core files (00_Core/)
- Includes relevant library integrations only
- Filters output templates to department-specific ones
- Includes processing rules
- Includes usage docs
- Smaller file size (focused content)

**Filtering Logic:**
- **Core:** Always included (all departments need context)
- **Libraries:** Include only libraries relevant to department
- **Templates:** Include templates 01-15 (general) + department-specific (16-21)
- **Processing Rules:** Always included
- **Usage:** Always included

**Department-Specific Libraries:**

| Department | Primary Libraries |
|------------|------------------|
| AI | All (comprehensive) |
| Design | Objects, Products, Tools, Parameters |
| Dev | Tools, Processes, Objects, Results |
| Sales/LG | Services, Products, Actions, Processes |
| HR | Professions, Skills, Responsibilities |
| Video | Objects, Tools, Processes |
| AI | Processes, Results, Parameters |

### assemble_lightweight.py
**Purpose:** Create minimal version without extensive examples

**Usage:**
```bash
python assemble_lightweight.py
```

**Output:**
- **File:** `../MAIN_PROMPT_v5_Lightweight.md`
- **Size:** ~50-60KB (about half of full version)

**Features:**
- Includes all core files (00_Core/)
- Includes library integration structure without extensive examples
- Includes output templates without detailed examples
- Includes processing rules (condensed)
- Includes basic usage instructions only
- Excludes:
  - Detailed examples in library files
  - Multiple examples per template
  - Advanced features documentation
  - Full changelog history

**Use Cases:**
- Quick reference
- Reduced file size for faster loading
- Mobile/web viewing
- When examples aren't needed

---

## Requirements

### Python Version
- **Minimum:** Python 3.7+
- **Recommended:** Python 3.10+

### Required Libraries (Built-in)
- `pathlib` - File path handling
- `os` - Operating system operations
- `sys` - System parameters
- `argparse` - Command-line argument parsing
- `re` - Regular expressions for validation

### Optional Libraries
- `markdown` - For markdown validation (install with `pip install markdown`)

---

## Installation

### Check Python Version
```bash
python --version
```

If Python is not installed or version is < 3.7, install from [python.org](https://www.python.org/downloads/).

### Install Optional Dependencies (Recommended)
```bash
pip install markdown
```

---

## Usage Examples

### Generate Full Monolithic Version
```bash
cd scripts
python assemble_full_prompt.py
```

Output: `../MAIN_PROMPT_v5.md`

### Generate AI Department Version
```bash
cd scripts
python assemble_department.py --dept AI
```

Output: `../MAIN_PROMPT_v5_AI.md`

### Generate Lightweight Version
```bash
cd scripts
python assemble_lightweight.py
```

Output: `../MAIN_PROMPT_v5_Lightweight.md`

### Generate Multiple Versions at Once
```bash
cd scripts
python assemble_full_prompt.py
python assemble_department.py --dept AI
python assemble_department.py --dept Design
python assemble_lightweight.py
```

---

## Script Features

### All Scripts Include:

**Error Handling:**
- Validates all source files exist
- Checks for read permissions
- Handles encoding issues
- Reports missing files clearly

**Logging:**
- Progress updates during assembly
- File count and size statistics
- Error messages with context
- Success confirmation

**Validation:**
- Markdown syntax checking
- File format verification
- Cross-reference validation (optional)

**Performance:**
- Efficient file reading
- Minimal memory usage
- Fast assembly (< 1 second for full version)

### Output Format:

All generated files include:

**Metadata Block:**
```markdown
---
Generated: 2025-11-15 17:30:00
Source: MAIN_PROMPT_v5_Modular/
Files Combined: 58
Total Size: 119 KB
Generator: assemble_full_prompt.py
Version: 5.0
---
```

**Table of Contents:**
- Automatic TOC generation
- Links to all major sections
- Nested structure for subsections

**Navigation:**
- "Back to top" links
- Section-to-section links
- Related content references

---

## Configuration

### Customizing Assembly:

Edit the relevant Python script to:
- Change file order
- Modify filtering logic
- Adjust output format
- Add/remove sections
- Customize metadata

### Common Customizations:

**Change Output Location:**
```python
OUTPUT_PATH = Path("../custom_location/MAIN_PROMPT_v5.md")
```

**Add Custom Header:**
```python
CUSTOM_HEADER = "# Custom Organization Name\n\n"
```

**Exclude Specific Files:**
```python
EXCLUDE_FILES = ["file_to_skip.md"]
```

---

## Troubleshooting

### "Python not found"
- Install Python 3.7+ from python.org
- Ensure Python is in system PATH

### "No such file or directory"
- Run from scripts/ folder: `cd scripts`
- Check that modular files exist

### "Permission denied"
- Check write permissions in output directory
- Close file if open in another application

### "Encoding error"
- All files should be UTF-8 encoded
- Check for special characters in source files

### "Script runs but no output"
- Check for error messages in console
- Verify source files are not empty
- Check output path is writable

---

## Testing

### Test Script Functionality:

```bash
# Test full assembly
python assemble_full_prompt.py

# Verify output exists and is valid
ls -lh ../MAIN_PROMPT_v5.md

# Test department assembly
python assemble_department.py --dept AI
ls -lh ../MAIN_PROMPT_v5_AI.md

# Compare file sizes
du -h ../*.md
```

### Validation:

```bash
# If markdown library installed
python -c "import markdown; markdown.markdown(open('../MAIN_PROMPT_v5.md').read())"
```

---

## Performance

**Typical Assembly Times:**
- Full version: ~0.5-1.0 seconds
- Department version: ~0.3-0.5 seconds
- Lightweight version: ~0.3-0.5 seconds

**File Sizes:**
- Full version: ~119 KB
- Department version: ~40-60 KB (varies by dept)
- Lightweight version: ~50-60 KB

---

## Maintenance

### When to Update Scripts:

- New folders added to modular structure
- File naming conventions change
- New department added
- Output format requirements change
- New assembly variation needed

### Best Practices:

- Test scripts after any changes
- Keep backup of previous versions
- Document customizations
- Version control script changes

---

## Future Enhancements

Potential additions to consider:
- Web-based assembly interface
- Automated scheduling (daily assembly)
- Git integration for version control
- Diff generation between versions
- Custom template support
- Multi-format output (PDF, HTML, etc.)

---

**Status:** 🚧 Pending - Scripts to be created in MIL-007
