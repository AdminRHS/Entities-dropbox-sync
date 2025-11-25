"""
Phase 4: Data Extraction (Read-Only)
Purpose: Extract all data from source files without modification

IMPORTANT: Read-only operation on all source files
         Creates extracted data in IMPORTS/ folder only
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
CHECKPOINT_DIR = os.path.join(IMPORTS_DIR, "checkpoints", "phase_4")

# Timestamp
TIMESTAMP = datetime.now().isoformat()

def load_crm_records():
    """Load all CRM cluster records"""
    print("\nLoading CRM cluster files...")

    all_records = []
    cluster_files = sorted(Path(CRM_CLUSTERS_DIR).glob("Client_cluster_*.json"))

    for cluster_file in cluster_files:
        try:
            with open(cluster_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Each cluster file contains an array of records
                if isinstance(data, list):
                    # Add source tracking to each record
                    for record in data:
                        record['_source_file'] = cluster_file.name
                        record['_source_type'] = 'crm_export'
                    all_records.extend(data)
                else:
                    data['_source_file'] = cluster_file.name
                    data['_source_type'] = 'crm_export'
                    all_records.append(data)
        except Exception as e:
            print(f"⚠ Error loading {cluster_file.name}: {str(e)}")

    print(f"✓ Loaded {len(cluster_files)} cluster files with {len(all_records)} total records")
    return all_records

def create_processing_registry(records):
    """Create registry to track processed records"""
    print("\nCreating processing registry...")

    registry = {
        "created_at": TIMESTAMP,
        "total_records": len(records),
        "records": []
    }

    for idx, record in enumerate(records, 1):
        registry_entry = {
            "sequence_id": idx,
            "crm_id": record.get("client_id"),
            "company_name": record.get("company_name"),
            "contact_name": record.get("name"),
            "source_file": record.get("_source_file"),
            "source_type": record.get("_source_type"),
            "processed": False,
            "generated_id": None,
            "entity_type": None,
            "extraction_timestamp": TIMESTAMP
        }
        registry["records"].append(registry_entry)

    print(f"✓ Created registry with {len(registry['records'])} entries")
    return registry

def analyze_data_coverage(records):
    """Analyze data coverage and completeness"""
    print("\nAnalyzing data coverage...")

    coverage = {
        "total_records": len(records),
        "field_coverage": {},
        "key_fields": {
            "has_company_name": 0,
            "has_contact_name": 0,
            "has_email": 0,
            "has_pocs": 0,
            "has_industry": 0,
            "has_location": 0,
            "has_lead_status": 0,
            "has_communications": 0
        },
        "entity_type_estimates": {
            "potential_clients": 0,
            "potential_prospects": 0,
            "has_job_requests": 0
        }
    }

    # Analyze each record
    for record in records:
        # Key field presence
        if record.get("company_name"):
            coverage["key_fields"]["has_company_name"] += 1

        if record.get("name"):
            coverage["key_fields"]["has_contact_name"] += 1

        if record.get("email"):
            coverage["key_fields"]["has_email"] += 1

        if record.get("pocs") and len(record.get("pocs", [])) > 0:
            coverage["key_fields"]["has_pocs"] += 1

        if record.get("lead_company_industry"):
            coverage["key_fields"]["has_industry"] += 1

        if record.get("lead_company_city"):
            coverage["key_fields"]["has_location"] += 1

        if record.get("lead_status"):
            coverage["key_fields"]["has_lead_status"] += 1

        if record.get("communications") and len(record.get("communications", [])) > 0:
            coverage["key_fields"]["has_communications"] += 1

        # Entity type estimation
        if record.get("job_requests") and len(record.get("job_requests", [])) > 0:
            coverage["entity_type_estimates"]["has_job_requests"] += 1
            coverage["entity_type_estimates"]["potential_clients"] += 1
        else:
            coverage["entity_type_estimates"]["potential_prospects"] += 1

    # Calculate percentages
    total = coverage["total_records"]
    for field, count in coverage["key_fields"].items():
        percentage = (count / total * 100) if total > 0 else 0
        coverage["field_coverage"][field] = {
            "count": count,
            "percentage": round(percentage, 2)
        }

    print(f"✓ Analyzed coverage for {total} records")
    return coverage

def extract_unique_values(records):
    """Extract unique values for validation"""
    print("\nExtracting unique values for validation...")

    unique_values = {
        "company_names": set(),
        "contact_emails": set(),
        "crm_ids": set(),
        "industries": set(),
        "countries": set(),
        "lead_statuses": set()
    }

    for record in records:
        # Company names
        if record.get("company_name"):
            unique_values["company_names"].add(record["company_name"])

        # Contact emails
        if record.get("email"):
            unique_values["contact_emails"].add(record["email"])

        # Extract emails from POCs
        if record.get("pocs"):
            for poc in record.get("pocs", []):
                if poc.get("email"):
                    unique_values["contact_emails"].add(poc["email"])

        # CRM IDs
        if record.get("client_id"):
            unique_values["crm_ids"].add(record["client_id"])

        # Industries
        if record.get("lead_company_industry") and record["lead_company_industry"].get("title"):
            unique_values["industries"].add(record["lead_company_industry"]["title"])

        # Countries
        if record.get("lead_company_city") and record["lead_company_city"].get("country"):
            country = record["lead_company_city"]["country"]
            if country.get("name"):
                unique_values["countries"].add(country["name"])

        # Lead statuses
        if record.get("lead_status") and record["lead_status"].get("type"):
            unique_values["lead_statuses"].add(record["lead_status"]["type"])

    # Convert sets to sorted lists for JSON serialization
    unique_counts = {
        "unique_companies": len(unique_values["company_names"]),
        "unique_emails": len(unique_values["contact_emails"]),
        "unique_crm_ids": len(unique_values["crm_ids"]),
        "unique_industries": len(unique_values["industries"]),
        "unique_countries": len(unique_values["countries"]),
        "unique_lead_statuses": len(unique_values["lead_statuses"])
    }

    print(f"✓ Found {unique_counts['unique_companies']} unique companies")
    print(f"✓ Found {unique_counts['unique_emails']} unique emails")
    print(f"✓ Found {unique_counts['unique_crm_ids']} unique CRM IDs")

    return unique_counts

def identify_duplicates(records):
    """Identify potential duplicate records"""
    print("\nIdentifying potential duplicates...")

    # Track by company name
    company_tracker = {}
    email_tracker = {}
    crm_id_tracker = {}

    for idx, record in enumerate(records):
        record_id = f"record_{idx}"

        # Track by company name
        company_name = record.get("company_name", "").strip().lower()
        if company_name:
            if company_name not in company_tracker:
                company_tracker[company_name] = []
            company_tracker[company_name].append(record_id)

        # Track by email
        email = record.get("email", "").strip().lower()
        if email:
            if email not in email_tracker:
                email_tracker[email] = []
            email_tracker[email].append(record_id)

        # Track by CRM ID
        crm_id = record.get("client_id")
        if crm_id:
            if crm_id not in crm_id_tracker:
                crm_id_tracker[crm_id] = []
            crm_id_tracker[crm_id].append(record_id)

    # Find duplicates
    duplicates = {
        "by_company_name": {k: v for k, v in company_tracker.items() if len(v) > 1},
        "by_email": {k: v for k, v in email_tracker.items() if len(v) > 1},
        "by_crm_id": {k: v for k, v in crm_id_tracker.items() if len(v) > 1}
    }

    duplicate_summary = {
        "duplicate_companies": len(duplicates["by_company_name"]),
        "duplicate_emails": len(duplicates["by_email"]),
        "duplicate_crm_ids": len(duplicates["by_crm_id"])
    }

    print(f"✓ Found {duplicate_summary['duplicate_companies']} duplicate company names")
    print(f"✓ Found {duplicate_summary['duplicate_emails']} duplicate emails")
    print(f"✓ Found {duplicate_summary['duplicate_crm_ids']} duplicate CRM IDs")

    return duplicate_summary, duplicates

def save_raw_extracted_data(records):
    """Save raw extracted data"""
    print("\nSaving raw extracted data...")

    # Full dataset
    full_data_path = os.path.join(IMPORTS_DIR, "raw_extracted_data.json")
    with open(full_data_path, 'w', encoding='utf-8') as f:
        json.dump({
            "extracted_at": TIMESTAMP,
            "total_records": len(records),
            "source": "CRM Client_JSON_Clusters",
            "records": records
        }, f, indent=2, ensure_ascii=False)

    print(f"✓ Saved {len(records)} records to raw_extracted_data.json")

    # Sample dataset (first 10 records for quick review)
    sample_data_path = os.path.join(IMPORTS_DIR, "raw_extracted_data_sample.json")
    with open(sample_data_path, 'w', encoding='utf-8') as f:
        json.dump({
            "extracted_at": TIMESTAMP,
            "note": "First 10 records for review",
            "records": records[:10]
        }, f, indent=2, ensure_ascii=False)

    print(f"✓ Saved sample (10 records) to raw_extracted_data_sample.json")

    return full_data_path, sample_data_path

def generate_extraction_report(registry, coverage, unique_counts, duplicate_summary):
    """Generate extraction report"""
    print("\nGenerating extraction report...")

    report = {
        "phase": "Phase 4 - Data Extraction",
        "executed_at": TIMESTAMP,
        "status": "completed",
        "summary": {
            "total_records_extracted": registry["total_records"],
            "source_files": 100,  # CRM clusters
            "data_sources": ["CRM Export (Client_JSON_Clusters)"]
        },
        "coverage_analysis": coverage,
        "unique_values": unique_counts,
        "duplicate_detection": duplicate_summary
    }

    # JSON report
    report_json_path = os.path.join(IMPORTS_DIR, "phase4_extraction_report.json")
    with open(report_json_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    # Markdown report
    report_md_path = os.path.join(IMPORTS_DIR, "phase4_extraction_report.md")
    with open(report_md_path, 'w', encoding='utf-8') as f:
        f.write(f"# Phase 4: Data Extraction Report\n\n")
        f.write(f"**Executed:** {TIMESTAMP}\n")
        f.write(f"**Status:** Completed\n\n")

        f.write(f"## Summary\n\n")
        f.write(f"- **Total Records Extracted:** {registry['total_records']}\n")
        f.write(f"- **Source Files:** 100 CRM cluster files\n")
        f.write(f"- **Data Source:** CRM Export (Client_JSON_Clusters)\n\n")

        f.write(f"## Data Coverage Analysis\n\n")
        f.write("| Field | Records | Coverage |\n")
        f.write("|-------|---------|----------|\n")
        for field, data in coverage["field_coverage"].items():
            f.write(f"| {field} | {data['count']} | {data['percentage']}% |\n")

        f.write(f"\n## Entity Type Estimates\n\n")
        f.write(f"- **Potential Clients:** {coverage['entity_type_estimates']['potential_clients']}\n")
        f.write(f"- **Potential Prospects:** {coverage['entity_type_estimates']['potential_prospects']}\n")
        f.write(f"- **Has Job Requests:** {coverage['entity_type_estimates']['has_job_requests']}\n\n")

        f.write(f"## Unique Values\n\n")
        f.write(f"- **Unique Companies:** {unique_counts['unique_companies']}\n")
        f.write(f"- **Unique Emails:** {unique_counts['unique_emails']}\n")
        f.write(f"- **Unique CRM IDs:** {unique_counts['unique_crm_ids']}\n")
        f.write(f"- **Unique Industries:** {unique_counts['unique_industries']}\n")
        f.write(f"- **Unique Countries:** {unique_counts['unique_countries']}\n")
        f.write(f"- **Unique Lead Statuses:** {unique_counts['unique_lead_statuses']}\n\n")

        f.write(f"## Duplicate Detection\n\n")
        f.write(f"- **Duplicate Company Names:** {duplicate_summary['duplicate_companies']}\n")
        f.write(f"- **Duplicate Emails:** {duplicate_summary['duplicate_emails']}\n")
        f.write(f"- **Duplicate CRM IDs:** {duplicate_summary['duplicate_crm_ids']}\n\n")

        f.write(f"## Files Generated\n\n")
        f.write(f"- `raw_extracted_data.json` - Full dataset ({registry['total_records']} records)\n")
        f.write(f"- `raw_extracted_data_sample.json` - Sample dataset (10 records)\n")
        f.write(f"- `processing_registry.json` - Record tracking registry\n\n")

        f.write(f"## Next Step\n\n")
        f.write(f"Proceed to **Phase 5: Metadata Tagging**\n")

    # Save processing registry
    registry_path = os.path.join(IMPORTS_DIR, "processing_registry.json")
    with open(registry_path, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)

    print(f"✓ JSON report: {report_json_path}")
    print(f"✓ Markdown report: {report_md_path}")
    print(f"✓ Processing registry: {registry_path}")

    return report

def create_checkpoint(registry):
    """Create checkpoint for rollback capability"""
    print("\nCreating checkpoint...")

    os.makedirs(CHECKPOINT_DIR, exist_ok=True)

    checkpoint = {
        "phase": "phase_4",
        "timestamp": TIMESTAMP,
        "status": "completed",
        "can_rollback": True,
        "rollback_instructions": "Delete raw_extracted_data.json and processing_registry.json, re-run phase4_data_extraction.py",
        "stats": {
            "records_extracted": registry["total_records"]
        }
    }

    checkpoint_path = os.path.join(CHECKPOINT_DIR, "checkpoint.json")
    with open(checkpoint_path, 'w', encoding='utf-8') as f:
        json.dump(checkpoint, f, indent=2, ensure_ascii=False)

    print(f"✓ Checkpoint saved: {checkpoint_path}")

def main():
    """Main execution"""
    print("="*60)
    print("PHASE 4: DATA EXTRACTION (READ-ONLY)")
    print("="*60)
    print(f"Timestamp: {TIMESTAMP}\n")

    try:
        # Step 1: Load CRM records
        records = load_crm_records()

        # Step 2: Create processing registry
        registry = create_processing_registry(records)

        # Step 3: Analyze data coverage
        coverage = analyze_data_coverage(records)

        # Step 4: Extract unique values
        unique_counts = extract_unique_values(records)

        # Step 5: Identify duplicates
        duplicate_summary, duplicates = identify_duplicates(records)

        # Step 6: Save raw extracted data
        full_data_path, sample_data_path = save_raw_extracted_data(records)

        # Step 7: Generate report
        report = generate_extraction_report(registry, coverage, unique_counts, duplicate_summary)

        # Step 8: Create checkpoint
        create_checkpoint(registry)

        print("\n" + "="*60)
        print("PHASE 4 COMPLETED SUCCESSFULLY")
        print("="*60)
        print(f"\n✓ Extracted {len(records)} records from CRM")
        print(f"✓ Created processing registry with {len(registry['records'])} entries")
        print(f"✓ Identified {unique_counts['unique_companies']} unique companies")
        print(f"✓ Detected {duplicate_summary['duplicate_companies']} potential duplicates")
        print(f"✓ Data coverage: {coverage['field_coverage']['has_company_name']['percentage']}% have company names")
        print(f"✓ Reports saved to: {IMPORTS_DIR}")
        print(f"\nNext: Review phase4_extraction_report.md and proceed to Phase 5")

    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        raise

if __name__ == "__main__":
    main()
