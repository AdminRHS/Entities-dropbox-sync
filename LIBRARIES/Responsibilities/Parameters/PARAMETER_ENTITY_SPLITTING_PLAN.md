# Parameter Entity Splitting Plan

**Date:** 2025-12-11
**Purpose:** Organize 10,596 parameters by related entities for better cross-referencing
**Current Status:** Parameters organized by profession (6 professions, 822 parameters)
**Remaining:** ~3,443 parameters + 245 general parameters

---

## Current Organization Status

### Existing Organization

**By Profession** (`organized_by_profession/`)
- ✅ Sales Manager: 95 parameters
- ✅ Lead Generator: 78 parameters
- ✅ Back End Developer: 124 parameters
- ✅ SEO Manager: 89 parameters
- ✅ Graphic Designer: 48 parameters
- ✅ Recruiter: 87 parameters
- ✅ Project Manager: 56 parameters
- ✅ General: 245 parameters
- **Subtotal:** 822 parameters organized

**By Department** (`organized_by_department/`)
- Managers parameters
- Marketers parameters
- Designers parameters
- Developers parameters

**Total Source:** 10,596 original entries (6,331 duplicates removed = 4,265 unique)

**Organized:** 822 parameters (19.3%)
**Remaining:** 3,443 parameters (80.7%)

---

## Related Entities for Cross-Reference

### Available Entity Types

From `ENTITIES\LIBRARIES\Responsibilities\`:

1. **Actions** (429 total)
   - Task-based parameters
   - Workflow parameters
   - Execution metrics

2. **Objects** (36 total)
   - Document parameters
   - Deliverable parameters
   - Asset parameters

3. **Core** (Responsibilities)
   - Role-based parameters
   - Permission parameters
   - Authority parameters

4. **By_Department**
   - Department-specific parameters
   - Team parameters
   - Collaboration parameters

From other LIBRARIES:

5. **Processes** (428 total)
   - Process quality parameters
   - Efficiency metrics
   - Step-by-step parameters

6. **Results** (432 total)
   - Outcome parameters
   - Success metrics
   - Performance indicators

7. **Tools** (75+ total)
   - Tool configuration parameters
   - Integration parameters
   - Usage metrics

8. **Products** (39 total)
   - Product feature parameters
   - Quality parameters
   - Specification parameters

9. **Services** (7 categories)
   - Service level parameters
   - Quality metrics
   - Delivery parameters

10. **Professions** (12+ total)
    - Already organized
    - Skill parameters
    - Competency metrics

---

## Proposed New Organization Structure

### Folder Structure

```
Parameters/
├── parameters.json (10,596 original - SOURCE)
│
├── organized_by_profession/ (EXISTING - 822 params)
│   ├── sales_manager_parameters.json
│   ├── lead_generator_parameters.json
│   ├── back_end_developer_parameters.json
│   ├── seo_manager_parameters.json
│   ├── graphic_designer_parameters.json
│   ├── recruiter_parameters.json
│   ├── project_manager_parameters.json
│   ├── general_parameters.json
│   └── README.md
│
├── organized_by_department/ (EXISTING)
│   ├── managers_parameters.json
│   ├── marketers_parameters.json
│   ├── designers_parameters.json
│   ├── developers_parameters.json
│   └── README.md
│
├── organized_by_action/ (NEW - ~800 params)
│   ├── communication_action_parameters.json
│   ├── analysis_action_parameters.json
│   ├── creation_action_parameters.json
│   ├── review_action_parameters.json
│   ├── optimization_action_parameters.json
│   ├── management_action_parameters.json
│   ├── integration_action_parameters.json
│   ├── _action_mapping_summary.json
│   └── README.md
│
├── organized_by_object/ (NEW - ~300 params)
│   ├── document_object_parameters.json
│   ├── video_object_parameters.json
│   ├── design_object_parameters.json
│   ├── code_object_parameters.json
│   ├── data_object_parameters.json
│   ├── _object_mapping_summary.json
│   └── README.md
│
├── organized_by_process/ (NEW - ~850 params)
│   ├── recruitment_process_parameters.json
│   ├── sales_process_parameters.json
│   ├── development_process_parameters.json
│   ├── design_process_parameters.json
│   ├── marketing_process_parameters.json
│   ├── onboarding_process_parameters.json
│   ├── _process_mapping_summary.json
│   └── README.md
│
├── organized_by_result/ (NEW - ~600 params)
│   ├── delivery_result_parameters.json
│   ├── quality_result_parameters.json
│   ├── performance_result_parameters.json
│   ├── completion_result_parameters.json
│   ├── success_result_parameters.json
│   ├── _result_mapping_summary.json
│   └── README.md
│
├── organized_by_tool/ (NEW - ~400 params)
│   ├── crm_tool_parameters.json
│   ├── design_tool_parameters.json
│   ├── development_tool_parameters.json
│   ├── communication_tool_parameters.json
│   ├── analytics_tool_parameters.json
│   ├── _tool_mapping_summary.json
│   └── README.md
│
├── organized_by_product/ (NEW - ~250 params)
│   ├── application_product_parameters.json
│   ├── website_product_parameters.json
│   ├── platform_product_parameters.json
│   ├── feature_product_parameters.json
│   ├── _product_mapping_summary.json
│   └── README.md
│
├── organized_by_service/ (NEW - ~200 params)
│   ├── consulting_service_parameters.json
│   ├── development_service_parameters.json
│   ├── design_service_parameters.json
│   ├── marketing_service_parameters.json
│   ├── _service_mapping_summary.json
│   └── README.md
│
├── cross_reference/ (NEW - Mapping files)
│   ├── parameter_to_action_map.json
│   ├── parameter_to_object_map.json
│   ├── parameter_to_process_map.json
│   ├── parameter_to_result_map.json
│   ├── parameter_to_tool_map.json
│   ├── parameter_to_product_map.json
│   ├── parameter_to_service_map.json
│   ├── parameter_to_profession_map.json
│   ├── entity_relationship_graph.json
│   └── README.md
│
├── analysis/ (NEW - Analytics and insights)
│   ├── parameter_coverage_report.json
│   ├── entity_distribution_analysis.json
│   ├── cross_reference_statistics.json
│   ├── unorganized_parameters_report.json
│   └── README.md
│
└── MASTER_ORGANIZATION_INDEX.json (NEW - Complete overview)
```

---

## Mapping Strategy

### Phase 1: Entity Relationship Identification

**1.1 Parameter Analysis**
- Read all 10,596 parameters
- Identify parameter types
- Extract keywords
- Detect entity mentions

**1.2 Cross-Reference with Entity Libraries**
- Match parameters to Actions (429)
- Match parameters to Objects (36)
- Match parameters to Processes (428)
- Match parameters to Results (432)
- Match parameters to Tools (75+)
- Match parameters to Products (39)
- Match parameters to Services (7 categories)

**1.3 Keyword Mapping**
Create mapping dictionaries:
```python
action_keywords = {
    "communication": ["email", "message", "notify", "communicate", "contact"],
    "analysis": ["analyze", "review", "assess", "evaluate", "measure"],
    "creation": ["create", "design", "develop", "build", "generate"],
    # ... more mappings
}
```

---

### Phase 2: Automated Classification

**2.1 Script Development**

Create `split_parameters_by_entity.py`:

```python
"""
Split parameters.json by related entities
"""

import json
import re
from collections import defaultdict

# Load source data
with open('parameters.json') as f:
    params_data = json.load(f)

# Load entity libraries
actions = load_json('../../Actions/actions.json')
objects = load_json('../../Objects/objects.json')
processes = load_json('../../../Processes/processes.json')
results = load_json('../../../Results/results.json')
tools = load_json('../../../Tools/tools.json')
products = load_json('../../../Products/products.json')
services = load_json('../../../Services/services.json')

# Classification logic
def classify_parameter(param_text, param_type):
    classifications = {
        'action': [],
        'object': [],
        'process': [],
        'result': [],
        'tool': [],
        'product': [],
        'service': []
    }

    # Match against each entity type
    # ... matching logic

    return classifications

# Process all parameters
for param in params_data['data']:
    classifications = classify_parameter(
        param['Parameters'],
        param['Types']
    )

    # Assign to appropriate categories
    # ... assignment logic
```

**2.2 Matching Rules**

**Direct Matching:**
- Parameter text contains entity name
- Parameter type matches entity category
- Parameter keywords overlap with entity keywords

**Contextual Matching:**
- Parameter relates to entity workflow
- Parameter measures entity performance
- Parameter configures entity behavior

**Fuzzy Matching:**
- Similarity score > 0.7
- Semantic similarity using embeddings
- Manual review for borderline cases

---

### Phase 3: File Generation

**3.1 Entity-Specific Files**

For each entity type, create JSON file:

```json
{
  "metadata": {
    "entity_type": "action",
    "entity_name": "communication_action",
    "total_parameters": 127,
    "source_file": "../../parameters.json",
    "organization_date": "2025-12-11",
    "related_entities": {
      "actions": ["ACT-001", "ACT-023", ...],
      "professions": ["sales manager", "lead generator"],
      "tools": ["TOL-045 - Email Client", "TOL-078 - CRM"]
    }
  },
  "summary": {
    "parameter_categories": [
      "response_time",
      "message_quality",
      "engagement_metrics",
      "channel_effectiveness"
    ],
    "key_metrics": [
      "average_response_time",
      "open_rate",
      "click_through_rate"
    ]
  },
  "parameters": [
    {
      "parameter": "initial response rate",
      "type": "new",
      "related_actions": ["ACT-001 - Send Email"],
      "related_processes": ["PROC-023 - Lead Outreach"],
      "use_cases": [
        "Measuring cold outreach effectiveness",
        "Tracking communication performance"
      ]
    },
    // ... more parameters
  ]
}
```

**3.2 Cross-Reference Files**

Create bidirectional mapping:

```json
{
  "parameter_to_action": {
    "initial response rate": ["ACT-001", "ACT-023", "ACT-045"],
    "conversion rate": ["ACT-078", "ACT-089"],
    // ... more mappings
  },
  "action_to_parameter": {
    "ACT-001": ["initial response rate", "open rate", "reply rate"],
    "ACT-023": ["engagement level", "response time"],
    // ... more mappings
  }
}
```

---

### Phase 4: Quality Assurance

**4.1 Validation Checks**

- [ ] All 4,265 unique parameters assigned
- [ ] No orphaned parameters
- [ ] Cross-references validated
- [ ] Metadata accurate
- [ ] File formats consistent

**4.2 Coverage Analysis**

Generate report:
- Parameters per entity type
- Entities with most parameters
- Entities with no parameters
- Overlap analysis (parameters assigned to multiple entities)

**4.3 Manual Review**

Review borderline assignments:
- Low confidence scores
- Multiple entity matches
- Ambiguous parameters

---

## Implementation Plan

### Week 1: Setup & Analysis
**Days 1-2:**
- [x] Create project structure
- [x] Write this plan document
- [ ] Set up development environment
- [ ] Create backup of parameters.json

**Days 3-5:**
- [ ] Load all entity libraries
- [ ] Analyze parameter patterns
- [ ] Build keyword dictionaries
- [ ] Create classification rules

### Week 2: Automated Classification
**Days 1-3:**
- [ ] Develop classification script
- [ ] Test on sample (100 parameters)
- [ ] Refine matching rules
- [ ] Validate results

**Days 4-5:**
- [ ] Run full classification (4,265 parameters)
- [ ] Generate entity-specific files
- [ ] Create cross-reference maps

### Week 3: Quality Assurance
**Days 1-2:**
- [ ] Validation checks
- [ ] Coverage analysis
- [ ] Generate reports

**Days 3-4:**
- [ ] Manual review of borderline cases
- [ ] Corrections and adjustments
- [ ] Final validation

**Day 5:**
- [ ] Documentation
- [ ] README files for each folder
- [ ] Usage examples

### Week 4: Integration & Testing
**Days 1-2:**
- [ ] Integrate with MAIN_PROMPT v5
- [ ] Test cross-referencing
- [ ] Performance testing

**Days 3-5:**
- [ ] User acceptance testing
- [ ] Final adjustments
- [ ] Deployment
- [ ] Announce completion

---

## Expected Outcomes

### Quantitative
- **10,596 parameters** classified by 8 entity types
- **8 new organized folders** created
- **~3,400 parameters** newly organized
- **8 cross-reference maps** generated
- **~50 new files** created

### Qualitative
- **Improved discoverability:** Find parameters by entity type
- **Enhanced cross-referencing:** See all parameters for a given action/object/process
- **Better MAIN_PROMPT integration:** Entity-aware parameter suggestions
- **Reduced complexity:** Focused parameter sets per entity
- **Scalable structure:** Easy to add new entity types

---

## Benefits by Entity Type

### For Actions (429 actions)
**Example:** "Send Email" action
- See all email-related parameters
- Response rate, open rate, bounce rate
- Quality metrics, timing parameters
- Quick reference for action implementation

### For Objects (36 objects)
**Example:** "Design_Mockup" object
- See all design-related parameters
- Resolution, format, color space
- File size, layer structure
- Design quality standards

### For Processes (428 processes)
**Example:** "Lead_Qualification" process
- See all qualification parameters
- Scoring criteria, disqualification rules
- Stage progression metrics
- Process efficiency indicators

### For Results (432 results)
**Example:** "Project_Completion" result
- See all completion parameters
- Success criteria, quality benchmarks
- Timeline adherence, budget compliance
- Stakeholder satisfaction metrics

### For Tools (75+ tools)
**Example:** "CRM" tool
- See all CRM-related parameters
- Configuration settings, integration points
- Usage metrics, performance indicators
- Data quality parameters

### For Products (39 products)
**Example:** "Mobile_App" product
- See all mobile app parameters
- Feature specifications, performance benchmarks
- Quality standards, compatibility requirements
- User experience metrics

### For Services (7 categories)
**Example:** "Consulting_Service" service
- See all consulting parameters
- Service level agreements, quality metrics
- Delivery timelines, client satisfaction
- Pricing and scope parameters

---

## Technical Specifications

### Data Format

**Standard JSON Structure:**
```json
{
  "metadata": {
    "entity_type": "string",
    "entity_name": "string",
    "total_parameters": "integer",
    "source_file": "string",
    "organization_date": "ISO 8601 date",
    "related_entities": "object"
  },
  "summary": {
    "parameter_categories": "array",
    "key_metrics": "array",
    "coverage_percentage": "float"
  },
  "parameters": [
    {
      "parameter": "string",
      "type": "string",
      "related_entities": "object",
      "use_cases": "array",
      "confidence_score": "float (0-1)"
    }
  ]
}
```

### Naming Conventions

**Files:**
- `{entity_type}_{entity_name}_parameters.json`
- Example: `action_communication_parameters.json`

**Folders:**
- `organized_by_{entity_type}/`
- Example: `organized_by_action/`

**IDs:**
- Use existing entity IDs from libraries
- Example: `ACT-001`, `OBJ-023`, `PROC-078`

---

## Success Metrics

### Completion Metrics
- [ ] 100% of 4,265 unique parameters classified
- [ ] 8 entity type folders created
- [ ] 8+ cross-reference maps generated
- [ ] All README files written

### Quality Metrics
- [ ] Classification confidence > 0.8 average
- [ ] < 5% parameters in multiple categories
- [ ] < 2% orphaned parameters
- [ ] 100% validation checks passed

### Usage Metrics (Post-Launch)
- Parameter lookup time reduced by 70%
- Cross-reference queries successful > 95%
- User satisfaction > 4.5/5
- MAIN_PROMPT integration working

---

## Dependencies

### Required Data
- [x] parameters.json (10,596 entries)
- [ ] Actions library (429 actions)
- [ ] Objects library (36 objects)
- [ ] Processes library (428 processes)
- [ ] Results library (432 results)
- [ ] Tools library (75+ tools)
- [ ] Products library (39 products)
- [ ] Services library (7 categories)

### Required Scripts
- [ ] split_parameters_by_entity.py (Main script)
- [ ] validate_organization.py (Validation)
- [ ] generate_cross_references.py (Mapping)
- [ ] create_reports.py (Analytics)

### Required Tools
- Python 3.8+
- JSON libraries
- Text processing libraries
- (Optional) NLP libraries for semantic matching

---

## Risk Mitigation

### Risks & Solutions

**Risk 1: Parameter ambiguity**
- Solution: Allow multi-category assignment with confidence scores
- Fallback: Manual review queue for low confidence

**Risk 2: Entity library incompleteness**
- Solution: Create "unmapped" category
- Fallback: Iterative refinement as libraries grow

**Risk 3: Performance issues (10K+ parameters)**
- Solution: Batch processing, progress tracking
- Fallback: Process in chunks, parallel processing

**Risk 4: Data quality issues**
- Solution: Extensive validation checks
- Fallback: Manual correction workflow

---

## Next Steps

### Immediate (This Week)
1. [ ] Review and approve this plan
2. [ ] Load all entity libraries
3. [ ] Create classification script (v1)
4. [ ] Test on 100-parameter sample

### Short-term (This Month)
5. [ ] Refine classification rules
6. [ ] Run full classification
7. [ ] Generate all new files
8. [ ] Complete validation

### Long-term (Next Quarter)
9. [ ] Integrate with MAIN_PROMPT v5
10. [ ] Monitor usage and gather feedback
11. [ ] Iterate and improve
12. [ ] Expand to additional entity types

---

## Questions for Clarification

1. **Priority:** Which entity types should be organized first?
   - Recommend: Actions, Processes (highest cross-reference value)

2. **Overlap:** Should parameters be allowed in multiple categories?
   - Recommend: Yes, with confidence scores

3. **Threshold:** What confidence score threshold for automatic assignment?
   - Recommend: 0.7 (70%)

4. **Manual Review:** Who will handle borderline case reviews?
   - Recommend: AI Department + Data Quality Team

5. **Timeline:** Is 4-week timeline acceptable?
   - Adjustable based on resource availability

---

**Status:** 📋 Plan Complete - Awaiting Approval
**Next:** Load entity libraries and start Phase 1
**Owner:** AI Department
**Estimated Completion:** January 15, 2026
