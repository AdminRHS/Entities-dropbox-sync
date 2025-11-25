# 04_Usage - Documentation, Guides, and Maintenance

**Purpose:** Usage instructions, examples, best practices, and maintenance guides for MAIN_PROMPT v5.

**Files in this folder:** 7
**Update Frequency:** As needed when workflow or features change

---

## Files

### 01_Usage_Instructions.md
**Purpose:** Step-by-step workflow for using MAIN_PROMPT v5

**Covers:**
- Complete processing workflow
- How to analyze a meeting transcript
- How to apply templates
- How to use library integrations
- How to generate output
- Quality checks and validation
- Troubleshooting common issues

**Target Audience:** All users (new and experienced)

### 02_Examples.md
**Purpose:** Full examples showing transcript → output transformation

**Includes:**
- **AI Department Meeting Example** - Technical discussion with tool mentions
- **Sales Meeting Example** - Product and service discussions
- **Design Review Example** - Creative work and deliverables
- **All-Hands Meeting Example** - Multi-department, various topics
- **Annotated examples** showing entity recognition process

**Each example shows:**
- Original transcript excerpt
- Identified participants and projects
- Recognized entities with IDs
- Applied templates
- Final structured output
- Confidence levels for matches

### 03_Tips_Best_Practices.md
**Purpose:** Tips for accuracy and optimization

**Covers:**
- How to improve recognition accuracy
- Best practices for different meeting types
- Department-specific tips (AI, Dev, Design, LG, Sales, etc.)
- Common mistakes to avoid
- Optimization strategies
- Shortcuts and efficiency tips

**Organized by:**
- Meeting type (technical, creative, planning, etc.)
- Department
- Complexity level

### 04_Advanced_Features.md
**Purpose:** Advanced capabilities and customization

**Covers:**
- **Multi-language processing** - Handling non-English transcripts
- **Batch processing** - Processing multiple meetings efficiently
- **Custom library integration** - Adding new entities or libraries
- **Advanced cross-referencing** - Complex entity relationships
- **Department-specific configurations** - Tailoring for specific teams
- **Template customization** - Modifying output templates
- **Assembly script customization** - Creating custom variations

### 05_Maintenance_Guide.md
**Purpose:** How to keep MAIN_PROMPT v5 up-to-date

**Covers:**
- **Monthly tasks:**
  - Update employee directory (00_Core/03_Employee_Directory.md)
  - Verify employee count (should be 32, or current count)

- **Weekly tasks:**
  - Update project directory (00_Core/04_Project_Directory.md)
  - Add new projects as they start

- **As-needed tasks:**
  - Sync library statistics when LIBRARIES updated
  - Update individual library integration files
  - Re-generate monolithic version after updates

- **Quarterly tasks:**
  - Review and update examples in templates
  - Verify all library statistics
  - Update recognition patterns if needed
  - Review and refine processing rules

**Testing procedures:**
- How to validate changes
- How to test assembly scripts
- How to verify library integrations

### 06_CHANGELOG.md
**Purpose:** Complete version history

**Includes:**
- **Version 5.0 (2025)** - Modular architecture changes
- **Version 4.0 (2025-01-27)** - Previous version details
- **Version 3.0** - Historical changes
- **Version 2.0** - Historical changes
- **Version 1.0** - Initial release

**For each version:**
- Major changes
- New features
- Improvements
- Bug fixes
- Migration notes

### 07_Migration_Guide.md
**Purpose:** Guide for migrating from MAIN_PROMPT v4 to v5

**Covers:**
- **Key differences** between v4 and v5
- **Feature mapping** - Where v4 features are in v5
- **Structural changes** - Monolithic vs modular
- **New capabilities** in v5
- **Backward compatibility** notes
- **Migration checklist**
- **Common migration issues** and solutions

**For v4 users:**
- How to transition to modular structure
- When to use monolithic vs modular
- How to generate v4-style output from v5
- What's been enhanced

---

## Quick Start Guide

### New Users (Never used any version):
1. Read **01_Usage_Instructions.md** completely
2. Review **02_Examples.md** - at least 2 examples
3. Start with simple meeting (1-2 participants, 1 project)
4. Reference **03_Tips_Best_Practices.md** as needed
5. Consult other core folders (00_Core, 01_Library_Integration, etc.)

### v4 Users (Upgrading to v5):
1. Read **07_Migration_Guide.md** first
2. Understand key differences
3. Review **01_Usage_Instructions.md** for v5-specific workflow
4. Try processing with both monolithic and modular approaches
5. Refer to **03_Tips_Best_Practices.md** for v5 optimizations

### Experienced v5 Users (Reference):
- Use **01_Usage_Instructions.md** as workflow reference
- Check **03_Tips_Best_Practices.md** for specific scenarios
- Consult **04_Advanced_Features.md** for complex cases
- Use **05_Maintenance_Guide.md** for updates

---

## Common Use Cases

### "Process a standard meeting"
→ **01_Usage_Instructions.md** - Follow standard workflow

### "Handle a multi-language transcript"
→ **04_Advanced_Features.md** - Multi-language processing

### "Improve accuracy for design meetings"
→ **03_Tips_Best_Practices.md** - Department-specific tips (Design)

### "Update employee list"
→ **05_Maintenance_Guide.md** - Monthly tasks section

### "Understand what changed from v4"
→ **07_Migration_Guide.md** - Complete comparison

### "See real examples"
→ **02_Examples.md** - Multiple annotated examples

### "Process many meetings at once"
→ **04_Advanced_Features.md** - Batch processing

### "Fix a common problem"
→ **01_Usage_Instructions.md** - Troubleshooting section

---

## Documentation Standards

All documentation in this folder follows:
- **Clear structure** with headers and sections
- **Practical examples** showing real usage
- **Step-by-step instructions** where applicable
- **Cross-references** to related files
- **Troubleshooting** sections
- **Validation** guidance

---

## Feedback and Updates

If you encounter:
- **Missing information** → Log in project Issues Log
- **Outdated examples** → Note in Maintenance Guide
- **Workflow improvements** → Document in Tips/Best Practices
- **Bugs or errors** → Report in project tracking

---

## Related Resources

### Core Documentation:
- **Root README:** `../README.md` - System overview
- **Source Files:** `../MAIN_PROMPT_v4.md` and `CREATE_MAIN_PROMPT_v5.md`

### Processing References:
- **Library Integration:** `../01_Library_Integration/` - Entity recognition
- **Output Templates:** `../02_Output_Templates/` - Output formatting
- **Processing Rules:** `../03_Processing_Rules/` - Recognition logic

### Assembly:
- **Scripts:** `../scripts/` - Generate monolithic versions

---

**Status:** 🚧 Pending - Files to be created in MIL-006
