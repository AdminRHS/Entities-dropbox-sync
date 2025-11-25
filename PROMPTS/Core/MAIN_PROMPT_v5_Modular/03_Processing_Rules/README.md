# 03_Processing_Rules - Entity Recognition and Processing Logic

**Purpose:** Rules and patterns for identifying participants, projects, and entities from meeting transcripts.

**Files in this folder:** 7 (6 processing rules + this README)
**Update Frequency:** When recognition logic needs refinement

---

## Overview

This folder contains the processing logic for analyzing meeting transcripts and extracting structured information. These rules work in conjunction with the library integration files to identify and categorize entities.

---

## Files

### 01_Participant_Identification.md
**Purpose:** How to identify meeting participants from transcripts

**Covers:**
- Name recognition and variations
- Employee ID assignment
- Department detection from context
- Cross-reference with Employee Directory (00_Core/03_Employee_Directory.md)
- Handling of unknown participants
- Multi-name variations (nicknames, formal names)

### 02_Project_Recognition.md
**Purpose:** Project keyword matching and abbreviation detection

**Covers:**
- Project abbreviation matching
- Full project name recognition
- Keyword-based project identification
- Cross-reference with Project Directory (00_Core/04_Project_Directory.md)
- Multi-project discussions
- Disambiguation when multiple projects mentioned

### 03_Entity_Recognition.md
**Purpose:** Master recognition workflow for all 12 LIBRARIES entities

**Covers:**
- Recognition patterns for each library
- Confidence level assignment (High/Medium/Low)
- Context-based recognition
- Ambiguity resolution strategies
- Entity validation rules
- Cross-library entity matching

**Key Process:**
1. Identify potential entity mentions in transcript
2. Match against library recognition patterns
3. Assign confidence level based on match quality
4. Validate in context
5. Cross-reference with related entities
6. Output with entity ID and confidence

### 04_Language_Handling.md
**Purpose:** Multi-language support and translation rules

**Covers:**
- Language detection
- Translation guidelines
- Cultural context preservation
- Multi-language meeting handling
- Non-English entity recognition

### 05_Vocabulary_Recognition.md
**Purpose:** Industry and company-specific terminology

**Covers:**
- Industry-specific terminology
- Company-specific vocabulary and jargon
- Acronym expansion and recognition
- Synonym handling
- Domain-specific language patterns (AI, Dev, Design, LG, etc.)
- Technical term recognition

### 06_Cross_Reference_Rules.md
**Purpose:** How to create cross-references between entities

**Covers:**
- Relationship validation between entities
- Bidirectional linking strategies
- Confidence scoring for relationships
- Reference format standards
- Common relationship patterns:
  - Action → Process → Result
  - Action + Object → Task/Responsibility
  - Tool → Profession → Department
  - Product → Service
  - Skill → Responsibility → Profession

---

## Processing Workflow

### Overall Process Flow:

```
1. Receive Transcript
   ↓
2. Identify Participants (01_Participant_Identification)
   ↓
3. Identify Projects (02_Project_Recognition)
   ↓
4. Detect Language (04_Language_Handling)
   ↓
5. Recognize Vocabulary (05_Vocabulary_Recognition)
   ↓
6. Identify Entities (03_Entity_Recognition)
   ↓
7. Create Cross-References (06_Cross_Reference_Rules)
   ↓
8. Apply Output Templates (from 02_Output_Templates/)
   ↓
9. Generate Structured Output
```

### Priority Order:

1. **Participants** - Who is speaking/involved
2. **Projects** - What project is being discussed
3. **Context** - Department, domain, technical level
4. **Entities** - What specific LIBRARIES entities are mentioned
5. **Relationships** - How entities relate to each other

---

## Confidence Levels

### High Confidence (90-100%)
- Exact match to entity name or ID
- Clear context supports the match
- Multiple confirming signals

### Medium Confidence (60-89%)
- Partial match or synonym
- Context somewhat supports
- Some ambiguity exists

### Low Confidence (30-59%)
- Weak match or inference
- Limited context
- Significant ambiguity

### No Match (<30%)
- Don't include in output
- Log for potential new entity

---

## Recognition Pattern Types

### 1. Exact Match
- Entity name appears verbatim
- ID is mentioned directly
- **Example:** "We used Figma" → TOOL-XXX (Figma)

### 2. Synonym Match
- Synonym or alternative name used
- Common variation recognized
- **Example:** "We need to recruit" → ACTION-XXX (Hire)

### 3. Context Match
- Entity inferred from context
- Department or domain implies entity
- **Example:** "The design needs iteration" → PROCESS-XXX (Design Iteration)

### 4. Composite Match
- Multiple words form entity
- Phrase recognition
- **Example:** "send follow-up email" → ACTION-XXX (Send Email)

### 5. Cross-Reference Match
- Entity implied by relationship
- Linked entity suggests this one
- **Example:** "Using that authentication service" → TOOL-XXX (Auth0) if Auth0 mentioned earlier

---

## Integration with Libraries

These processing rules work with library integration files:

| Processing Rule | Primary Library References |
|----------------|---------------------------|
| 01_Participant_Identification | 10_Professions_Library.md |
| 02_Project_Recognition | 07_Products_Library.md |
| 03_Entity_Recognition | ALL library files (01-12) |
| 04_Language_Handling | No direct library |
| 05_Vocabulary_Recognition | ALL library files |
| 06_Cross_Reference_Rules | 13_Taxonomy_Framework.md |

---

## Error Handling

### Common Issues:

**Ambiguous Entity:**
- Resolution: Use context, assign lower confidence, note alternatives

**Unknown Entity:**
- Resolution: Log for review, include in Documentation Gaps section

**Conflicting Entities:**
- Resolution: Include both with context explaining difference

**Weak Signal:**
- Resolution: Don't force a match, prefer "none" over wrong match

---

## Quality Standards

Every entity match should have:
- ✅ Valid entity ID from library
- ✅ Confidence level assigned
- ✅ Context explaining the match
- ✅ Source location in transcript (if applicable)
- ✅ Cross-references to related entities

---

## Examples

Detailed examples for each recognition type are included in the individual processing rule files.

---

**Status:** 🚧 Pending - Files to be created in MIL-005
