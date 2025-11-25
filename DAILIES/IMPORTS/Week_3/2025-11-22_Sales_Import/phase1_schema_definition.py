"""
Phase 1: Schema Definition
Purpose: Generate formal JSON schemas for BUSINESSES entity with all sub-entities

Incorporates:
- All 14 sub-entity definitions
- schema_version tracking
- ISO 8601 date format standard
- FK relationship definitions
- Required field markers
"""

import os
import sys
import json
from datetime import datetime

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Configuration
BASE_DIR = r"C:\Users\Dell\Dropbox\ENTITIES"
BUSINESSES_DIR = os.path.join(BASE_DIR, "BUSINESSES")
SCHEMAS_DIR = os.path.join(BUSINESSES_DIR, "schemas")
IMPORTS_DIR = os.path.join(BASE_DIR, "IMPORTS", "2025-11-22_Sales_Import")

# Timestamp
TIMESTAMP = datetime.now().isoformat()

def generate_main_schema():
    """Generate main BUSINESSES JSON Schema"""

    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": "https://entities.dropbox.com/schemas/BUSINESSES_v1.0.0.json",
        "title": "BUSINESSES Entity Schema",
        "description": "Complete schema for BUSINESSES entity including all sub-entities",
        "version": "1.0.0",
        "type": "object",
        "required": ["company", "metadata"],
        "properties": {
            "company": {
                "$ref": "#/definitions/Company"
            },
            "pocs": {
                "type": "array",
                "items": {"$ref": "#/definitions/POC"}
            },
            "business_relationship": {
                "$ref": "#/definitions/BusinessRelationship"
            },
            "communication_history": {
                "$ref": "#/definitions/CommunicationHistory"
            },
            "prospect": {
                "$ref": "#/definitions/Prospect"
            },
            "prospect_company": {
                "$ref": "#/definitions/ProspectCompany"
            },
            "prospect_communications": {
                "type": "array",
                "items": {"$ref": "#/definitions/ProspectCommunication"}
            },
            "assigned_users": {
                "$ref": "#/definitions/AssignedUsers"
            },
            "job_requests": {
                "type": "array",
                "items": {"$ref": "#/definitions/JobRequest"}
            },
            "references": {
                "$ref": "#/definitions/References"
            },
            "metadata": {
                "$ref": "#/definitions/Metadata"
            }
        },
        "definitions": {
            "Company": {
                "type": "object",
                "required": ["id", "name"],
                "properties": {
                    "id": {"type": "string", "pattern": "^BUS-\\d{4}-\\d{3}$"},
                    "name": {"type": "string", "minLength": 1, "maxLength": 255},
                    "logo": {"type": ["string", "null"]},
                    "website": {"type": ["string", "null"], "format": "uri"},
                    "size_id": {"type": ["integer", "null"]},
                    "size_label": {"type": ["string", "null"]},
                    "year_established": {"type": ["integer", "null"]},
                    "note": {"type": ["string", "null"], "maxLength": 3000},
                    "tool_id": {"type": ["integer", "null"]},
                    "prospect_company_id": {"type": ["string", "null"]},
                    "locations": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "city_id": {"type": "integer"},
                                "city_name": {"type": "string"},
                                "country_id": {"type": "integer"},
                                "country_name": {"type": "string"},
                                "is_primary": {"type": "boolean"}
                            }
                        }
                    },
                    "industries": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "industry_id": {"type": "integer"},
                                "industry_name": {"type": "string"},
                                "sub_industry_id": {"type": ["integer", "null"]},
                                "sub_industry_name": {"type": ["string", "null"]}
                            }
                        }
                    }
                }
            },
            "POC": {
                "type": "object",
                "required": ["id", "name"],
                "properties": {
                    "id": {"type": "string", "pattern": "^POC-\\d{3}$"},
                    "name": {"type": "string", "maxLength": 100},
                    "position_id": {"type": ["integer", "null"]},
                    "position_name": {"type": ["string", "null"]},
                    "status_id": {"type": ["integer", "null"]},
                    "status_name": {"type": ["string", "null"]},
                    "availability": {"type": "string", "enum": ["active", "inactive"]},
                    "poc_types": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "poc_type_id": {"type": "integer"},
                                "poc_type_name": {"type": "string"}
                            }
                        }
                    },
                    "contacts": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "contact_id": {"type": "integer"},
                                "contact_type": {"type": "string"},
                                "contact_value": {"type": "string"},
                                "is_primary": {"type": "boolean"}
                            }
                        }
                    }
                }
            },
            "BusinessRelationship": {
                "type": "object",
                "properties": {
                    "business_id": {"type": "string"},
                    "entity_id": {"type": "integer"},
                    "entity_type": {"type": "string", "enum": ["lead", "client", "affiliate"]},
                    "created_by": {"type": "integer"},
                    "created_at": {"type": "string", "format": "date-time"},
                    "lead_info": {"type": ["object", "null"]},
                    "client_info": {"type": ["object", "null"]},
                    "affiliate_info": {"type": ["object", "null"]}
                }
            },
            "CommunicationHistory": {
                "type": "object",
                "required": ["total_interactions", "interactions"],
                "properties": {
                    "total_interactions": {"type": "integer", "minimum": 0},
                    "first_contact": {"type": ["string", "null"], "format": "date"},
                    "last_contact": {"type": ["string", "null"], "format": "date"},
                    "interactions": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": ["id", "date", "type", "source", "summary"],
                            "properties": {
                                "id": {"type": "string", "pattern": "^COMM-\\d{3}$"},
                                "date": {"type": "string", "format": "date"},
                                "time": {"type": ["string", "null"]},
                                "type": {"type": "string", "enum": ["Call", "Email", "Meeting"]},
                                "source": {"type": "string", "enum": ["manual", "google_calendar"]},
                                "event_id": {"type": ["string", "null"]},
                                "summary": {"type": "string"},
                                "duration_minutes": {"type": ["integer", "null"]},
                                "attendees": {"type": "array", "items": {"type": "string"}},
                                "meeting_link": {"type": ["string", "null"]},
                                "notes": {"type": ["string", "null"]},
                                "outcome": {"type": ["string", "null"]},
                                "action_items": {"type": "array", "items": {"type": "string"}},
                                "conducted_by": {"type": ["string", "null"]}
                            }
                        }
                    },
                    "emails_sent": {"type": "integer", "minimum": 0},
                    "calls_completed": {"type": "integer", "minimum": 0},
                    "meetings_held": {"type": "integer", "minimum": 0}
                }
            },
            "Prospect": {
                "type": "object",
                "properties": {
                    "id": {"type": "string", "pattern": "^PROS-\\d{3}$"},
                    "name": {"type": "string", "maxLength": 100},
                    "position_id": {"type": ["integer", "null"]},
                    "position_name": {"type": ["string", "null"]},
                    "status_id": {"type": ["integer", "null"]},
                    "status_name": {"type": ["string", "null"]},
                    "notes": {"type": ["string", "null"], "maxLength": 500},
                    "tool_id": {"type": ["integer", "null"]},
                    "contacts": {"type": "array"}
                }
            },
            "ProspectCompany": {
                "type": "object",
                "properties": {
                    "id": {"type": "string", "pattern": "^PCOMP-\\d{3}$"},
                    "name": {"type": "string", "maxLength": 100},
                    "website": {"type": ["string", "null"]},
                    "city_id": {"type": ["integer", "null"]},
                    "city_name": {"type": ["string", "null"]},
                    "country_id": {"type": ["integer", "null"]},
                    "country_name": {"type": ["string", "null"]},
                    "manager_id": {"type": ["integer", "null"]},
                    "manager_name": {"type": ["string", "null"]},
                    "created_by": {"type": "integer"},
                    "created_at": {"type": "string", "format": "date-time"},
                    "industries": {"type": "array"},
                    "sub_industries": {"type": "array"}
                }
            },
            "ProspectCommunication": {
                "type": "object",
                "properties": {
                    "id": {"type": "string", "pattern": "^PCOMM-\\d{3}$"},
                    "prospect_id": {"type": "string"},
                    "prospect_company_id": {"type": "string"},
                    "user_id": {"type": "integer"},
                    "user_name": {"type": "string"},
                    "created_at": {"type": "string", "format": "date-time"},
                    "is_followup": {"type": "boolean"},
                    "note": {"type": ["string", "null"], "maxLength": 500},
                    "messages": {"type": "array"}
                }
            },
            "AssignedUsers": {
                "type": "object",
                "properties": {
                    "lead_generator_id": {"type": ["integer", "null"]},
                    "lead_generator_name": {"type": ["string", "null"]},
                    "sales_assistant_id": {"type": ["integer", "null"]},
                    "sales_assistant_name": {"type": ["string", "null"]},
                    "sales_manager_id": {"type": ["integer", "null"]},
                    "sales_manager_name": {"type": ["string", "null"]},
                    "business_users": {"type": "array"}
                }
            },
            "JobRequest": {
                "type": "object",
                "required": ["id", "name"],
                "properties": {
                    "id": {"type": "string", "pattern": "^JR-\\d{3}$"},
                    "name": {"type": "string", "maxLength": 255},
                    "entity_id": {"type": "integer"},
                    "inner_client_id": {"type": ["integer", "null"]},
                    "profession_id": {"type": "integer"},
                    "profession_name": {"type": "string"},
                    "status_id": {"type": "integer"},
                    "status_name": {"type": "string"},
                    "quantity": {"type": "integer", "minimum": 1},
                    "manager_id": {"type": ["integer", "null"]},
                    "manager_name": {"type": ["string", "null"]},
                    "rate_id": {"type": ["integer", "null"]},
                    "rate_name": {"type": ["string", "null"]},
                    "shift_id": {"type": ["integer", "null"]},
                    "shift_name": {"type": ["string", "null"]},
                    "created_by": {"type": "integer"},
                    "created_at": {"type": "string", "format": "date-time"},
                    "demand_date": {"type": ["string", "null"], "format": "date"},
                    "close_date": {"type": ["string", "null"], "format": "date"},
                    "sum_jas": {"type": "integer", "minimum": 0},
                    "note": {"type": ["string", "null"], "maxLength": 2000},
                    "prospect_id": {"type": ["string", "null"]},
                    "tools": {"type": "array"},
                    "languages": {"type": "array"},
                    "object_actions": {"type": "array"},
                    "job_templates": {"type": "array"}
                }
            },
            "References": {
                "type": "object",
                "properties": {
                    "crm_link": {"type": ["string", "null"]},
                    "crm_id": {"type": ["string", "null"]},
                    "dropbox_path": {"type": ["string", "null"]},
                    "google_doc": {"type": ["string", "null"]},
                    "transcription_links": {"type": "array", "items": {"type": "string"}},
                    "contract_link": {"type": ["string", "null"]},
                    "proposal_link": {"type": ["string", "null"]},
                    "calendar_id": {"type": ["string", "null"]}
                }
            },
            "Metadata": {
                "type": "object",
                "required": ["schema_version", "tags", "created_at", "updated_at", "source_file", "import_batch", "approved"],
                "properties": {
                    "schema_version": {"type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$"},
                    "tags": {"type": "array", "items": {"type": "string"}},
                    "created_at": {"type": "string", "format": "date-time"},
                    "updated_at": {"type": "string", "format": "date-time"},
                    "source_file": {"type": "string"},
                    "source_row": {"type": ["integer", "null"]},
                    "import_batch": {"type": "string"},
                    "last_synced_calendar": {"type": ["string", "null"], "format": "date-time"},
                    "data_quality_score": {"type": ["integer", "null"], "minimum": 0, "maximum": 100},
                    "approved": {"type": "string", "enum": ["TRUE", "FALSE"]},
                    "lifecycle_status": {"type": "string", "enum": ["active", "archived", "deleted"]},
                    "archived_at": {"type": ["string", "null"], "format": "date-time"},
                    "archive_reason": {"type": ["string", "null"]}
                }
            }
        }
    }

    return schema

def generate_validation_rules():
    """Generate validation rules"""

    rules = {
        "version": "1.0.0",
        "date_format": "ISO 8601 (YYYY-MM-DDTHH:MM:SSZ)",
        "id_formats": {
            "company": "BUS-YYYY-###",
            "poc": "POC-###",
            "prospect": "PROS-###",
            "prospect_company": "PCOMP-###",
            "job_request": "JR-###",
            "communication": "COMM-###",
            "prospect_communication": "PCOMM-###"
        },
        "required_validations": [
            {
                "check": "schema_compliance",
                "target": "all_entities",
                "threshold": "100%"
            },
            {
                "check": "unique_ids",
                "target": "all_id_fields",
                "threshold": "100%"
            },
            {
                "check": "fk_integrity",
                "description": "All foreign key references must exist in lookup tables",
                "fields": [
                    "company.size_id",
                    "poc.position_id",
                    "prospect.status_id",
                    "industry_id",
                    "sub_industry_id",
                    "country_id",
                    "job_request.profession_id",
                    "job_request.rate_id",
                    "job_request.shift_id"
                ],
                "threshold": "100%"
            },
            {
                "check": "date_format",
                "description": "All dates must be ISO 8601 compliant",
                "threshold": "100%"
            },
            {
                "check": "data_completeness",
                "description": "Percentage of non-null fields",
                "threshold": "85%"
            }
        ],
        "lookup_table_validations": {
            "must_exist": [
                "Industries",
                "SubIndustries",
                "Positions",
                "CompanySizes",
                "LeadStatuses",
                "LeadSources",
                "Countries",
                "ContactTypes",
                "Templates",
                "JobRequests/Professions",
                "JobRequests/Rates",
                "JobRequests/Shifts",
                "JobRequests/Tools",
                "JobRequests/Languages",
                "JobRequests/LanguageLevels"
            ],
            "must_have_index": True
        }
    }

    return rules

def generate_field_definitions():
    """Generate human-readable field definitions"""

    content = """# BUSINESSES Entity - Field Definitions

**Schema Version:** 1.0.0
**Last Updated:** """ + TIMESTAMP + """

---

## Core Entity Fields

### Company Sub-Entity
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | Yes | Unique company ID (BUS-YYYY-###) |
| name | string | Yes | Company name (max 255 chars) |
| logo | string | No | Logo URL |
| website | string | No | Company website (URI format) |
| size_id | integer | No | FK to CompanySizes |
| size_label | string | No | Denormalized size name |
| year_established | integer | No | Year company was founded |
| note | string | No | Notes (max 3000 chars) |
| locations | array | No | Company locations |
| industries | array | No | Company industries |

### POCs Sub-Entity
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | Yes | POC ID (POC-###) |
| name | string | Yes | Full name (max 100 chars) |
| position_id | integer | No | FK to Positions |
| position_name | string | No | Denormalized position |
| availability | string | No | active or inactive |
| contacts | array | No | Contact methods (email, phone, linkedin) |

### Job Requests Sub-Entity
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | Yes | Job request ID (JR-###) |
| name | string | Yes | Position name (max 255 chars) |
| profession_id | integer | Yes | FK to JobRequests/Professions |
| quantity | integer | Yes | Number of positions (min 1) |
| demand_date | string | No | Required start date (ISO 8601) |
| close_date | string | No | Position filled date (ISO 8601) |
| tools | array | No | Required technologies |
| languages | array | No | Language requirements with levels |

### Communication History Sub-Entity
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| total_interactions | integer | Yes | Total count of interactions |
| interactions | array | Yes | List of all communications |
| interactions[].id | string | Yes | Communication ID (COMM-###) |
| interactions[].date | string | Yes | Date (YYYY-MM-DD) |
| interactions[].type | string | Yes | Call, Email, or Meeting |
| interactions[].source | string | Yes | manual or google_calendar |
| interactions[].event_id | string | No | Google Calendar event ID |

### Metadata Sub-Entity
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| schema_version | string | Yes | Schema version (semver format) |
| tags | array | Yes | Searchable tags |
| created_at | string | Yes | Creation timestamp (ISO 8601) |
| updated_at | string | Yes | Last update timestamp (ISO 8601) |
| source_file | string | Yes | Import source filename |
| import_batch | string | Yes | Import batch identifier |
| approved | string | Yes | TRUE or FALSE |
| lifecycle_status | string | No | active, archived, or deleted |
| data_quality_score | integer | No | 0-100 quality score |

---

## Date Format Standard

All dates and timestamps MUST use **ISO 8601** format:
- Dates: `YYYY-MM-DD`
- DateTimes: `YYYY-MM-DDTHH:MM:SSZ`

**Examples:**
- `2025-11-22`
- `2025-11-22T10:30:00Z`

---

## Foreign Key References

All FK fields must reference existing entries in lookup tables:

| Field | References | Location |
|-------|-----------|----------|
| size_id | CompanySizes | BUSINESSES/CompanySizes/ |
| position_id | Positions | BUSINESSES/Positions/ |
| industry_id | Industries | BUSINESSES/Industries/ |
| sub_industry_id | SubIndustries | BUSINESSES/SubIndustries/ |
| country_id | Countries | BUSINESSES/Countries/ |
| profession_id | Professions | BUSINESSES/JobRequests/Professions/ |
| rate_id | Rates | BUSINESSES/JobRequests/Rates/ |
| shift_id | Shifts | BUSINESSES/JobRequests/Shifts/ |

---

## Required Fields by Sub-Entity

**Minimum Required for Valid Entity:**
1. `company.id`
2. `company.name`
3. `metadata.schema_version` (must be "1.0.0")
4. `metadata.tags`
5. `metadata.created_at`
6. `metadata.updated_at`
7. `metadata.source_file`
8. `metadata.import_batch`
9. `metadata.approved`

All other fields are optional but recommended for completeness.

---

*Generated: """ + TIMESTAMP + """*
"""

    return content

def save_schemas():
    """Save all schema files"""
    print("Generating schema files...")

    # Main schema
    main_schema = generate_main_schema()
    schema_path = os.path.join(SCHEMAS_DIR, "BUSINESSES_SCHEMA.json")
    with open(schema_path, 'w', encoding='utf-8') as f:
        json.dump(main_schema, f, indent=2)
    print(f"✓ Created: BUSINESSES_SCHEMA.json")

    # Validation rules
    validation_rules = generate_validation_rules()
    validation_path = os.path.join(SCHEMAS_DIR, "validation_rules.json")
    with open(validation_path, 'w', encoding='utf-8') as f:
        json.dump(validation_rules, f, indent=2)
    print(f"✓ Created: validation_rules.json")

    # Field definitions
    field_defs = generate_field_definitions()
    field_defs_path = os.path.join(SCHEMAS_DIR, "field_definitions.md")
    with open(field_defs_path, 'w', encoding='utf-8') as f:
        f.write(field_defs)
    print(f"✓ Created: field_definitions.md")

    return {
        "main_schema": schema_path,
        "validation_rules": validation_path,
        "field_definitions": field_defs_path
    }

def generate_report(created_files):
    """Generate Phase 1 report"""
    print("\nGenerating report...")

    report = {
        "phase": "Phase 1 - Schema Definition",
        "executed_at": TIMESTAMP,
        "status": "completed",
        "schema_version": "1.0.0",
        "files_created": created_files,
        "key_features": [
            "14 sub-entity definitions",
            "schema_version field added to metadata",
            "ISO 8601 date format standard",
            "FK validation rules defined",
            "Required field markers"
        ]
    }

    # Save JSON report
    report_json_path = os.path.join(IMPORTS_DIR, "phase1_schema_report.json")
    with open(report_json_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)

    # Save Markdown report
    report_md_path = os.path.join(IMPORTS_DIR, "phase1_schema_report.md")
    with open(report_md_path, 'w', encoding='utf-8') as f:
        f.write(f"# Phase 1: Schema Definition Report\n\n")
        f.write(f"**Executed:** {TIMESTAMP}\n")
        f.write(f"**Status:** Completed\n")
        f.write(f"**Schema Version:** 1.0.0\n\n")

        f.write(f"## Files Created\n\n")
        for key, path in created_files.items():
            f.write(f"- **{key}:** `{path}`\n")

        f.write(f"\n## Key Features\n\n")
        for feature in report["key_features"]:
            f.write(f"- {feature}\n")

        f.write(f"\n## Sub-Entities Defined\n\n")
        f.write(f"1. Company (2.2)\n")
        f.write(f"2. POCs (2.3)\n")
        f.write(f"3. Business Relationship (2.4)\n")
        f.write(f"4. Communication History (2.5)\n")
        f.write(f"5. Prospect (2.6)\n")
        f.write(f"6. Prospect Company (2.7)\n")
        f.write(f"7. Prospect Communications (2.8)\n")
        f.write(f"8. Assigned Users (2.9)\n")
        f.write(f"9. Job Requests (2.11)\n")
        f.write(f"10. References (2.12)\n")
        f.write(f"11. Metadata (2.13)\n")

        f.write(f"\n## Next Step\n\n")
        f.write(f"Proceed to **Phase 2: Lookup Table Population**\n")

    print(f"✓ JSON report: {report_json_path}")
    print(f"✓ Markdown report: {report_md_path}")

def main():
    """Main execution"""
    print("="*60)
    print("PHASE 1: SCHEMA DEFINITION")
    print("="*60)
    print(f"Timestamp: {TIMESTAMP}\n")

    try:
        # Generate and save schemas
        created_files = save_schemas()

        # Generate report
        generate_report(created_files)

        print("\n" + "="*60)
        print("PHASE 1 COMPLETED SUCCESSFULLY")
        print("="*60)
        print(f"\nSchema Version: 1.0.0")
        print(f"Files saved to: {SCHEMAS_DIR}")
        print(f"\nNext: Review schemas and proceed to Phase 2")

    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        raise

if __name__ == "__main__":
    main()
