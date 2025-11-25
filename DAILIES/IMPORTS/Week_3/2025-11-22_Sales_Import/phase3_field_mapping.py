"""
Phase 3: Field Classification & Mapping
Purpose: Map all source fields to target schema and define transformation functions

IMPORTANT: Read-only operation on source files
         Creates mapping documentation in IMPORTS/ folder only
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Configuration
BASE_DIR = r"C:\Users\Dell\Dropbox\ENTITIES"
IMPORTS_DIR = os.path.join(BASE_DIR, "IMPORTS", "2025-11-22_Sales_Import")
CRM_CLUSTERS_DIR = r"C:\Users\Dell\Dropbox\Nov25\Niko Nov25\ExportCRMS\Client_JSON_Clusters"
CLIENT_LIST_PATH = r"C:\Users\Dell\Dropbox\Nov25\Sales Nov25\client_list.md"
CHECKPOINT_DIR = os.path.join(IMPORTS_DIR, "checkpoints", "phase_3")

# Timestamp
TIMESTAMP = datetime.now().isoformat()

def analyze_crm_structure():
    """Analyze CRM cluster structure to identify all fields"""
    print("\nAnalyzing CRM cluster structure...")

    # Load first cluster file as sample
    sample_file = os.path.join(CRM_CLUSTERS_DIR, "Client_cluster_0001.json")

    with open(sample_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if isinstance(data, list) and len(data) > 0:
        sample_record = data[0]
    else:
        sample_record = data

    # Extract field structure
    fields = analyze_record_structure(sample_record, prefix="")

    print(f"✓ Analyzed CRM structure: {len(fields)} fields found")
    return fields, sample_record

def analyze_record_structure(obj, prefix="", fields=None):
    """Recursively analyze record structure"""
    if fields is None:
        fields = {}

    if isinstance(obj, dict):
        for key, value in obj.items():
            field_path = f"{prefix}.{key}" if prefix else key

            if isinstance(value, dict):
                fields[field_path] = "object"
                analyze_record_structure(value, field_path, fields)
            elif isinstance(value, list):
                fields[field_path] = "array"
                if len(value) > 0:
                    analyze_record_structure(value[0], f"{field_path}[]", fields)
            else:
                value_type = type(value).__name__
                fields[field_path] = value_type

    return fields

def create_field_mapping():
    """Create field mapping from CRM to BUSINESSES schema"""
    print("\nCreating field mappings...")

    mapping = {
        "company": {
            "id": {
                "source": "generated",
                "format": "BUS-YYYY-###",
                "transformation": "generate_company_id()"
            },
            "name": {
                "source": "company_name",
                "transformation": "normalize_company_name(company_name)"
            },
            "website": {
                "source": "website",
                "transformation": "clean_url(website)"
            },
            "size_id": {
                "source": "lead_company_size.id",
                "transformation": "direct_map"
            },
            "size_label": {
                "source": "lead_company_size.title",
                "transformation": "direct_map"
            },
            "year_established": {
                "source": "not_available",
                "transformation": "null"
            },
            "note": {
                "source": "multiple",
                "fields": ["notes", "description"],
                "transformation": "combine_notes()"
            },
            "locations": {
                "source": "lead_company_city",
                "transformation": "extract_locations(lead_company_city)"
            },
            "industries": {
                "source": "multiple",
                "fields": ["lead_company_industry", "sub_industries"],
                "transformation": "extract_industries(lead_company_industry, sub_industries)"
            }
        },
        "pocs": {
            "id": {
                "source": "generated",
                "format": "POC-###",
                "transformation": "generate_poc_id()"
            },
            "name": {
                "source": "pocs[].name",
                "transformation": "normalize_name(name)"
            },
            "position_id": {
                "source": "pocs[].position.id",
                "transformation": "direct_map"
            },
            "position_title": {
                "source": "pocs[].position.title",
                "transformation": "direct_map"
            },
            "email": {
                "source": "pocs[].email",
                "transformation": "normalize_email(email)"
            },
            "phone": {
                "source": "pocs[].phone",
                "transformation": "normalize_phone(phone)"
            },
            "linkedin_url": {
                "source": "pocs[].linkedin_url",
                "transformation": "clean_url(linkedin_url)"
            },
            "is_primary": {
                "source": "pocs[].is_primary",
                "transformation": "boolean_conversion(is_primary)"
            },
            "notes": {
                "source": "pocs[].notes",
                "transformation": "direct_map"
            }
        },
        "business_relationship": {
            "entity_type": {
                "source": "derived",
                "transformation": "classify_entity_type(record)"
            },
            "status_id": {
                "source": "lead_status.id",
                "transformation": "direct_map"
            },
            "status_type": {
                "source": "lead_status.type",
                "transformation": "direct_map"
            },
            "source_id": {
                "source": "lead_source.id",
                "transformation": "direct_map"
            },
            "source_name": {
                "source": "lead_source.name",
                "transformation": "direct_map"
            },
            "priority": {
                "source": "lead_status.priority",
                "transformation": "integer_conversion(priority)"
            }
        },
        "communication_history": {
            "total_interactions": {
                "source": "calculated",
                "transformation": "count_interactions()"
            },
            "last_contact_date": {
                "source": "communications[].created_at",
                "transformation": "max_date(communications)"
            },
            "interactions": {
                "source": "communications[]",
                "transformation": "extract_communications(communications)"
            }
        },
        "assigned_users": {
            "sales_manager_id": {
                "source": "sales_manager",
                "transformation": "integer_conversion(sales_manager)"
            },
            "sales_manager_name": {
                "source": "sales_manager_assistant.name",
                "transformation": "direct_map"
            },
            "lead_agent_id": {
                "source": "lead_agent.id",
                "transformation": "direct_map"
            },
            "created_by_id": {
                "source": "created_by.id",
                "transformation": "direct_map"
            },
            "created_by_name": {
                "source": "created_by.name",
                "transformation": "direct_map"
            }
        },
        "references": {
            "crm_link": {
                "source": "calculated",
                "transformation": "generate_crm_link(client_id)"
            },
            "crm_id": {
                "source": "client_id",
                "transformation": "direct_map"
            },
            "dropbox_path": {
                "source": "generated",
                "transformation": "generate_dropbox_path(company_name, entity_type)"
            }
        },
        "metadata": {
            "schema_version": {
                "source": "constant",
                "value": "1.0.0"
            },
            "tags": {
                "source": "derived",
                "transformation": "derive_tags(record)"
            },
            "created_at": {
                "source": "generated",
                "transformation": "current_timestamp()"
            },
            "updated_at": {
                "source": "generated",
                "transformation": "current_timestamp()"
            },
            "source_file": {
                "source": "tracking",
                "transformation": "record_source_file()"
            },
            "import_batch": {
                "source": "constant",
                "value": "2025-11-22_Sales_Import"
            },
            "data_quality_score": {
                "source": "calculated",
                "transformation": "calculate_quality_score(record)"
            }
        }
    }

    print(f"✓ Created field mappings for {len(mapping)} sub-entities")
    return mapping

def create_transformation_functions():
    """Define transformation function specifications"""
    print("\nDefining transformation functions...")

    transformations = {
        "normalize_company_name": {
            "description": "Clean and normalize company name",
            "input": "string",
            "output": "string",
            "logic": [
                "Trim whitespace",
                "Remove special characters (except spaces, hyphens, apostrophes)",
                "Title case each word",
                "Handle common abbreviations (LLC, Inc, Ltd)"
            ],
            "example": "\"ACME Corp. \" → \"Acme Corp\""
        },
        "generate_company_id": {
            "description": "Generate unique company ID",
            "input": "none",
            "output": "string",
            "logic": [
                "Format: BUS-YYYY-###",
                "YYYY = current year (2025)",
                "### = sequential 3-digit number",
                "Check uniqueness in registry"
            ],
            "example": "→ \"BUS-2025-001\""
        },
        "generate_poc_id": {
            "description": "Generate unique POC ID",
            "input": "none",
            "output": "string",
            "logic": [
                "Format: POC-###",
                "### = sequential 3-digit number",
                "Check uniqueness in registry"
            ],
            "example": "→ \"POC-001\""
        },
        "normalize_email": {
            "description": "Validate and normalize email address",
            "input": "string",
            "output": "string",
            "logic": [
                "Convert to lowercase",
                "Trim whitespace",
                "Validate format (basic regex)",
                "Return null if invalid"
            ],
            "example": "\"John.Doe@Example.COM \" → \"john.doe@example.com\""
        },
        "clean_url": {
            "description": "Clean and validate URL",
            "input": "string",
            "output": "string",
            "logic": [
                "Trim whitespace",
                "Add https:// if no protocol",
                "Remove trailing slashes",
                "Validate basic URL format"
            ],
            "example": "\"linkedin.com/company/acme\" → \"https://linkedin.com/company/acme\""
        },
        "classify_entity_type": {
            "description": "Classify as Client/Prospect/Ex_Client",
            "input": "record object",
            "output": "string",
            "logic": [
                "Check for job_requests → Client",
                "Check lead_status.type == 'Client' → Client",
                "Check notes for 'hired' → Client",
                "Check notes for 'stopped' → Ex_Client",
                "Default → Prospect"
            ],
            "example": "record with job_requests → \"Client\""
        },
        "derive_tags": {
            "description": "Extract tags from record data",
            "input": "record object",
            "output": "array of strings",
            "logic": [
                "Scan notes for keywords: 'urgent', 'hired', 'lead gen', 'dev', 'ai'",
                "Add industry as tag",
                "Add entity_type as tag",
                "Add lead_status.type as tag"
            ],
            "example": "notes: 'urgent dev needs' → ['urgent', 'development', 'active_prospect']"
        },
        "calculate_quality_score": {
            "description": "Calculate data completeness score",
            "input": "record object",
            "output": "integer (0-100)",
            "logic": [
                "Count total fields in schema",
                "Count non-null fields in record",
                "Score = (filled / total) * 100"
            ],
            "example": "15/20 fields filled → 75"
        },
        "extract_locations": {
            "description": "Extract company locations from city data",
            "input": "lead_company_city object",
            "output": "array of location objects",
            "logic": [
                "Map city_id, city_name from lead_company_city",
                "Map country_id, country_name from city.country",
                "Set is_primary = true for main location"
            ],
            "example": "city object → [{city_id: 123, city_name: 'NYC', country_id: 1, is_primary: true}]"
        },
        "extract_industries": {
            "description": "Extract industries and sub-industries",
            "input": "lead_company_industry, sub_industries array",
            "output": "array of industry objects",
            "logic": [
                "Map industry_id, industry_name from lead_company_industry",
                "Iterate sub_industries array",
                "Map sub_industry_id, sub_industry_name for each",
                "Return combined array"
            ],
            "example": "industry + 2 sub_industries → [{industry_id: 20, industry_name: 'Finance', sub_industry_id: 114, sub_industry_name: 'Financial Services'}]"
        },
        "parse_iso_date": {
            "description": "Parse date to ISO 8601 format",
            "input": "string (various formats)",
            "output": "string (ISO 8601)",
            "logic": [
                "Try parsing common formats: YYYY-MM-DD, MM/DD/YYYY, DD.MM.YYYY",
                "Add T00:00:00Z for dates without time",
                "Return null if unparseable"
            ],
            "example": "\"2025-11-22\" → \"2025-11-22T00:00:00Z\""
        }
    }

    print(f"✓ Defined {len(transformations)} transformation functions")
    return transformations

def identify_unmapped_fields(crm_fields, mapping):
    """Identify CRM fields not mapped to schema"""
    print("\nIdentifying unmapped fields...")

    # Flatten mapping to get all source fields
    mapped_sources = set()

    for entity, fields in mapping.items():
        for field, config in fields.items():
            if "source" in config:
                source = config["source"]
                if source not in ["generated", "calculated", "constant", "derived", "tracking", "not_available", "multiple"]:
                    mapped_sources.add(source)

                # Also add fields from "fields" array
                if "fields" in config:
                    for f in config["fields"]:
                        mapped_sources.add(f)

    # Find unmapped CRM fields
    unmapped = []
    for field in crm_fields.keys():
        # Simplify field path for comparison
        simple_field = field.split('[')[0].split('.')[0]

        is_mapped = False
        for mapped in mapped_sources:
            if simple_field in mapped or mapped in field:
                is_mapped = True
                break

        if not is_mapped:
            unmapped.append(field)

    print(f"✓ Found {len(unmapped)} unmapped fields")
    return unmapped

def generate_mapping_report(mapping, transformations, unmapped_fields, sample_record):
    """Generate comprehensive mapping report"""
    print("\nGenerating mapping report...")

    # JSON Report
    report = {
        "phase": "Phase 3 - Field Classification & Mapping",
        "executed_at": TIMESTAMP,
        "status": "completed",
        "summary": {
            "sub_entities_mapped": len(mapping),
            "transformation_functions": len(transformations),
            "unmapped_fields": len(unmapped_fields)
        },
        "field_mapping": mapping,
        "transformation_functions": transformations,
        "unmapped_fields": unmapped_fields[:50],  # Limit to first 50
        "sample_crm_record": {
            "id": sample_record.get("id"),
            "company_name": sample_record.get("company_name"),
            "name": sample_record.get("name")
        }
    }

    report_json_path = os.path.join(IMPORTS_DIR, "phase3_field_mapping_report.json")
    with open(report_json_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    # Markdown Report
    report_md_path = os.path.join(IMPORTS_DIR, "phase3_field_mapping_report.md")
    with open(report_md_path, 'w', encoding='utf-8') as f:
        f.write(f"# Phase 3: Field Classification & Mapping Report\n\n")
        f.write(f"**Executed:** {TIMESTAMP}\n")
        f.write(f"**Status:** Completed\n\n")

        f.write(f"## Summary\n\n")
        f.write(f"- **Sub-Entities Mapped:** {len(mapping)}\n")
        f.write(f"- **Transformation Functions:** {len(transformations)}\n")
        f.write(f"- **Unmapped Fields:** {len(unmapped_fields)}\n\n")

        f.write(f"## Field Mapping Overview\n\n")
        f.write("| Sub-Entity | Fields Mapped | Source Types |\n")
        f.write("|------------|---------------|---------------|\n")

        for entity, fields in mapping.items():
            source_types = set()
            for field_config in fields.values():
                if "source" in field_config:
                    source_types.add(field_config["source"])

            f.write(f"| {entity} | {len(fields)} | {', '.join(sorted(source_types))} |\n")

        f.write(f"\n## Transformation Functions\n\n")
        for func_name, func_spec in transformations.items():
            f.write(f"### {func_name}\n\n")
            f.write(f"**Description:** {func_spec['description']}\n\n")
            f.write(f"**Input:** {func_spec['input']}\n\n")
            f.write(f"**Output:** {func_spec['output']}\n\n")
            f.write(f"**Logic:**\n")
            for step in func_spec['logic']:
                f.write(f"- {step}\n")
            f.write(f"\n**Example:** {func_spec['example']}\n\n")

        f.write(f"\n## Unmapped Fields (First 50)\n\n")
        for field in unmapped_fields[:50]:
            f.write(f"- `{field}`\n")

        f.write(f"\n## Next Step\n\n")
        f.write(f"Proceed to **Phase 4: Data Extraction**\n")

    # Create transformation_functions.json for use in later phases
    func_json_path = os.path.join(IMPORTS_DIR, "transformation_functions.json")
    with open(func_json_path, 'w', encoding='utf-8') as f:
        json.dump(transformations, f, indent=2, ensure_ascii=False)

    # Create mapping_rules.json for use in later phases
    mapping_json_path = os.path.join(IMPORTS_DIR, "mapping_rules.json")
    with open(mapping_json_path, 'w', encoding='utf-8') as f:
        json.dump(mapping, f, indent=2, ensure_ascii=False)

    print(f"✓ JSON report: {report_json_path}")
    print(f"✓ Markdown report: {report_md_path}")
    print(f"✓ Transformation functions: {func_json_path}")
    print(f"✓ Mapping rules: {mapping_json_path}")

    return report

def create_checkpoint(mapping, transformations):
    """Create checkpoint for rollback capability"""
    print("\nCreating checkpoint...")

    os.makedirs(CHECKPOINT_DIR, exist_ok=True)

    checkpoint = {
        "phase": "phase_3",
        "timestamp": TIMESTAMP,
        "status": "completed",
        "can_rollback": True,
        "rollback_instructions": "No data files created, mapping can be regenerated",
        "stats": {
            "sub_entities_mapped": len(mapping),
            "transformation_functions": len(transformations)
        }
    }

    checkpoint_path = os.path.join(CHECKPOINT_DIR, "checkpoint.json")
    with open(checkpoint_path, 'w', encoding='utf-8') as f:
        json.dump(checkpoint, f, indent=2, ensure_ascii=False)

    print(f"✓ Checkpoint saved: {checkpoint_path}")

def main():
    """Main execution"""
    print("="*60)
    print("PHASE 3: FIELD CLASSIFICATION & MAPPING")
    print("="*60)
    print(f"Timestamp: {TIMESTAMP}\n")

    try:
        # Step 1: Analyze CRM structure
        crm_fields, sample_record = analyze_crm_structure()

        # Step 2: Create field mapping
        mapping = create_field_mapping()

        # Step 3: Define transformation functions
        transformations = create_transformation_functions()

        # Step 4: Identify unmapped fields
        unmapped_fields = identify_unmapped_fields(crm_fields, mapping)

        # Step 5: Generate reports
        report = generate_mapping_report(mapping, transformations, unmapped_fields, sample_record)

        # Step 6: Create checkpoint
        create_checkpoint(mapping, transformations)

        print("\n" + "="*60)
        print("PHASE 3 COMPLETED SUCCESSFULLY")
        print("="*60)
        print(f"\n✓ Mapped {len(mapping)} sub-entities")
        print(f"✓ Defined {len(transformations)} transformation functions")
        print(f"✓ Identified {len(unmapped_fields)} unmapped fields")
        print(f"✓ Reports saved to: {IMPORTS_DIR}")
        print(f"\nNext: Review phase3_field_mapping_report.md and proceed to Phase 4")

    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        raise

if __name__ == "__main__":
    main()
