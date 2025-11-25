"""
Phase 2: Lookup Table Population
Purpose: Extract unique values from source data and populate all lookup table folders

IMPORTANT: Read-only operation on source files
         Creates lookup table JSON files in BUSINESSES/ folders only
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
BUSINESSES_DIR = os.path.join(BASE_DIR, "BUSINESSES")
IMPORTS_DIR = os.path.join(BASE_DIR, "IMPORTS", "2025-11-22_Sales_Import")
CRM_CLUSTERS_DIR = r"C:\Users\Dell\Dropbox\Nov25\Niko Nov25\ExportCRMS\Client_JSON_Clusters"
CHECKPOINT_DIR = os.path.join(IMPORTS_DIR, "checkpoints", "phase_2")

# Timestamp
TIMESTAMP = datetime.now().isoformat()

# Lookup table definitions
LOOKUP_TABLES = {
    "root": [
        "Industries",
        "SubIndustries",
        "Positions",
        "CompanySizes",
        "LeadStatuses",
        "LeadSources",
        "Countries",
        "ContactTypes",
        "Templates"
    ],
    "nested": [
        "JobRequests/Professions",
        "JobRequests/Rates",
        "JobRequests/Shifts",
        "JobRequests/Tools",
        "JobRequests/Languages",
        "JobRequests/LanguageLevels"
    ]
}

def load_crm_clusters():
    """Load all CRM cluster JSON files"""
    print("\nLoading CRM cluster files...")

    all_records = []
    cluster_files = list(Path(CRM_CLUSTERS_DIR).glob("Client_cluster_*.json"))

    for cluster_file in cluster_files:
        try:
            with open(cluster_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Each cluster file contains an array of records
                if isinstance(data, list):
                    all_records.extend(data)
                    print(f"✓ Loaded: {cluster_file.name} ({len(data)} records)")
                else:
                    all_records.append(data)
                    print(f"✓ Loaded: {cluster_file.name} (1 record)")
        except Exception as e:
            print(f"⚠ Error loading {cluster_file.name}: {str(e)}")

    print(f"\n✓ Loaded {len(cluster_files)} cluster files with {len(all_records)} total records")
    return all_records

def extract_industries(records):
    """Extract unique industries from CRM data"""
    industries = {}

    for record in records:
        if 'lead_company_industry' in record and record['lead_company_industry']:
            industry = record['lead_company_industry']
            if isinstance(industry, dict) and 'id' in industry and 'title' in industry:
                industries[industry['id']] = industry['title']

    return industries

def extract_sub_industries(records):
    """Extract unique sub-industries from CRM data"""
    sub_industries = {}

    for record in records:
        if 'sub_industries' in record and record['sub_industries']:
            for sub_ind in record['sub_industries']:
                if isinstance(sub_ind, dict) and 'id' in sub_ind:
                    # Use 'name' or 'title' field
                    name = sub_ind.get('name') or sub_ind.get('title', str(sub_ind['id']))
                    sub_industries[sub_ind['id']] = {
                        'name': name,
                        'industry_id': sub_ind.get('industry_id')
                    }

    return sub_industries

def extract_company_sizes(records):
    """Extract unique company sizes from CRM data"""
    sizes = {}

    for record in records:
        if 'lead_company_size' in record and record['lead_company_size']:
            size = record['lead_company_size']
            if isinstance(size, dict) and 'id' in size and 'title' in size:
                sizes[size['id']] = size['title']

    return sizes

def extract_lead_statuses(records):
    """Extract unique lead statuses from CRM data"""
    statuses = {}

    for record in records:
        if 'lead_status' in record and record['lead_status']:
            status = record['lead_status']
            if isinstance(status, dict) and 'id' in status:
                statuses[status['id']] = {
                    'name': status.get('title', status.get('type', 'Unknown')),
                    'type': status.get('type'),
                    'priority': status.get('priority'),
                    'label_color': status.get('label_color')
                }

    return statuses

def extract_countries(records):
    """Extract unique countries from CRM data"""
    countries = {}

    for record in records:
        # From lead_company_city
        if 'lead_company_city' in record and record['lead_company_city']:
            city = record['lead_company_city']
            if isinstance(city, dict) and 'country' in city:
                country = city['country']
                if isinstance(country, dict) and 'id' in country:
                    name = country.get('name') or country.get('title', str(country['id']))
                    countries[country['id']] = name

        # Also check lead_account.country
        if 'lead_account' in record and record['lead_account']:
            account = record['lead_account']
            if isinstance(account, dict) and 'country' in account:
                country = account['country']
                if isinstance(country, dict) and 'id' in country:
                    name = country.get('name') or country.get('title', str(country['id']))
                    countries[country['id']] = name

    return countries

def extract_positions(records):
    """Extract unique positions from POC data"""
    positions = {}

    for record in records:
        if 'pocs' in record and record['pocs']:
            for poc in record['pocs']:
                if isinstance(poc, dict) and 'position' in poc and poc['position']:
                    pos = poc['position']
                    if isinstance(pos, dict) and 'id' in pos:
                        name = pos.get('title') or pos.get('name', str(pos['id']))
                        positions[pos['id']] = name

    return positions

def create_default_lookups():
    """Create default lookup values for tables not in CRM"""

    contact_types = {
        1: {"name": "LinkedIn Company", "icon": "linkedin"},
        2: {"name": "Email", "icon": "email"},
        3: {"name": "Phone", "icon": "phone"},
        4: {"name": "Website", "icon": "globe"},
        5: {"name": "WhatsApp", "icon": "whatsapp"}
    }

    lead_sources = {
        1: {"name": "LinkedIn Outreach", "channel": "linkedin"},
        2: {"name": "Referral", "channel": "referral"},
        3: {"name": "Website", "channel": "website"},
        4: {"name": "Cold Email", "channel": "email"},
        5: {"name": "Event", "channel": "event"}
    }

    job_professions = {
        1: {"name": "Python Developer", "category": "Development"},
        2: {"name": "JavaScript Developer", "category": "Development"},
        3: {"name": "QA Engineer", "category": "Quality Assurance"},
        4: {"name": "DevOps Engineer", "category": "Operations"},
        5: {"name": "Data Analyst", "category": "Analytics"}
    }

    job_rates = {
        1: {"name": "Junior", "order": 1},
        2: {"name": "Mid", "order": 2},
        3: {"name": "Senior", "order": 3},
        4: {"name": "Lead", "order": 4},
        5: {"name": "Principal", "order": 5}
    }

    job_shifts = {
        1: {"name": "Full-time", "hours_per_week": 40},
        2: {"name": "Part-time", "hours_per_week": 20},
        3: {"name": "Contract", "hours_per_week": None},
        4: {"name": "Freelance", "hours_per_week": None}
    }

    job_tools = {
        1: {"name": "Python", "category": "Language"},
        2: {"name": "JavaScript", "category": "Language"},
        3: {"name": "React", "category": "Framework"},
        4: {"name": "Django", "category": "Framework"},
        5: {"name": "PostgreSQL", "category": "Database"}
    }

    job_languages = {
        1: {"name": "English", "code": "en"},
        2: {"name": "Spanish", "code": "es"},
        3: {"name": "German", "code": "de"},
        4: {"name": "French", "code": "fr"},
        5: {"name": "Ukrainian", "code": "uk"}
    }

    job_language_levels = {
        1: {"name": "Basic", "order": 1, "description": "A1-A2"},
        2: {"name": "Intermediate", "order": 2, "description": "B1-B2"},
        3: {"name": "Advanced", "order": 3, "description": "C1"},
        4: {"name": "Fluent", "order": 4, "description": "C2"},
        5: {"name": "Native", "order": 5, "description": "Native speaker"}
    }

    return {
        "ContactTypes": contact_types,
        "LeadSources": lead_sources,
        "JobRequests/Professions": job_professions,
        "JobRequests/Rates": job_rates,
        "JobRequests/Shifts": job_shifts,
        "JobRequests/Tools": job_tools,
        "JobRequests/Languages": job_languages,
        "JobRequests/LanguageLevels": job_language_levels
    }

def create_lookup_files(table_name, data, folder_path):
    """Create individual JSON files for each lookup value and an INDEX file"""
    print(f"\nCreating {table_name} lookup files...")

    os.makedirs(folder_path, exist_ok=True)

    index = []
    files_created = 0

    for id_val, value in data.items():
        # Prepare record
        if isinstance(value, dict):
            record = {
                "id": id_val,
                "created_at": TIMESTAMP,
                "is_active": True,
                **value
            }
            name = value.get('name', str(id_val))
        else:
            record = {
                "id": id_val,
                "name": value,
                "created_at": TIMESTAMP,
                "is_active": True
            }
            name = value

        # Clean name for filename
        clean_name = "".join(c for c in name if c.isalnum() or c in (' ', '_', '-')).strip()
        clean_name = clean_name.replace(' ', '_')

        # Create filename
        filename = f"{table_name.split('/')[-1]}_{clean_name}_{id_val}.json"
        filepath = os.path.join(folder_path, filename)

        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(record, f, indent=2, ensure_ascii=False)

        files_created += 1
        index.append({
            "id": id_val,
            "name": name,
            "file": filename
        })

    # Create INDEX file
    index_file = os.path.join(folder_path, f"{table_name.split('/')[-1]}_INDEX.json")
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump({
            "table": table_name,
            "count": len(index),
            "created_at": TIMESTAMP,
            "entries": sorted(index, key=lambda x: x['id'])
        }, f, indent=2, ensure_ascii=False)

    print(f"✓ Created {files_created} files + INDEX for {table_name}")
    return files_created

def generate_report(stats):
    """Generate Phase 2 population report"""
    print("\nGenerating report...")

    report = {
        "phase": "Phase 2 - Lookup Table Population",
        "executed_at": TIMESTAMP,
        "status": "completed",
        "summary": {
            "tables_populated": stats['tables_populated'],
            "total_files_created": stats['total_files_created'],
            "extraction_source": "Client_JSON_Clusters + Defaults"
        },
        "tables": stats['tables']
    }

    # Save JSON report
    report_json_path = os.path.join(IMPORTS_DIR, "phase2_lookup_population_report.json")
    with open(report_json_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    # Save Markdown report
    report_md_path = os.path.join(IMPORTS_DIR, "phase2_lookup_population_report.md")
    with open(report_md_path, 'w', encoding='utf-8') as f:
        f.write(f"# Phase 2: Lookup Table Population Report\n\n")
        f.write(f"**Executed:** {TIMESTAMP}\n")
        f.write(f"**Status:** Completed\n\n")

        f.write(f"## Summary\n\n")
        f.write(f"- **Tables Populated:** {stats['tables_populated']}\n")
        f.write(f"- **Total Files Created:** {stats['total_files_created']}\n")
        f.write(f"- **Extraction Source:** Client_JSON_Clusters + Default values\n\n")

        f.write(f"## Lookup Tables Created\n\n")
        f.write("| Table | Files Created | Source |\n")
        f.write("|-------|---------------|--------|\n")
        for table in stats['tables']:
            f.write(f"| {table['name']} | {table['files_created']} | {table['source']} |\n")

        f.write(f"\n## Next Step\n\n")
        f.write(f"Proceed to **Phase 3: Field Classification & Mapping**\n")

    print(f"✓ JSON report: {report_json_path}")
    print(f"✓ Markdown report: {report_md_path}")

    return report

def create_checkpoint(stats):
    """Create checkpoint for rollback capability"""
    print("\nCreating checkpoint...")

    os.makedirs(CHECKPOINT_DIR, exist_ok=True)

    checkpoint = {
        "phase": "phase_2",
        "timestamp": TIMESTAMP,
        "status": "completed",
        "can_rollback": True,
        "rollback_instructions": "Delete lookup table files and re-run phase2_lookup_population.py",
        "stats": stats
    }

    checkpoint_path = os.path.join(CHECKPOINT_DIR, "checkpoint.json")
    with open(checkpoint_path, 'w', encoding='utf-8') as f:
        json.dump(checkpoint, f, indent=2, ensure_ascii=False)

    print(f"✓ Checkpoint saved: {checkpoint_path}")

def main():
    """Main execution"""
    print("="*60)
    print("PHASE 2: LOOKUP TABLE POPULATION")
    print("="*60)
    print(f"Timestamp: {TIMESTAMP}\n")

    try:
        stats = {
            'tables_populated': 0,
            'total_files_created': 0,
            'tables': []
        }

        # Step 1: Load CRM data
        records = load_crm_clusters()

        # Step 2: Extract from CRM
        print("\n" + "-"*60)
        print("Extracting values from CRM clusters...")
        print("-"*60)

        extracted = {
            "Industries": extract_industries(records),
            "SubIndustries": extract_sub_industries(records),
            "CompanySizes": extract_company_sizes(records),
            "LeadStatuses": extract_lead_statuses(records),
            "Countries": extract_countries(records),
            "Positions": extract_positions(records)
        }

        for table, data in extracted.items():
            print(f"✓ Extracted {len(data)} unique {table}")

        # Step 3: Add default lookups
        print("\n" + "-"*60)
        print("Adding default lookup values...")
        print("-"*60)

        defaults = create_default_lookups()

        for table, data in defaults.items():
            print(f"✓ Created {len(data)} default {table}")

        # Step 4: Create lookup files
        print("\n" + "-"*60)
        print("Creating lookup table files...")
        print("-"*60)

        # Process CRM-extracted tables
        for table_name, data in extracted.items():
            if data:  # Only create if we have data
                folder_path = os.path.join(BUSINESSES_DIR, table_name)
                files_created = create_lookup_files(table_name, data, folder_path)

                stats['tables_populated'] += 1
                stats['total_files_created'] += files_created + 1  # +1 for INDEX
                stats['tables'].append({
                    'name': table_name,
                    'files_created': files_created + 1,
                    'source': 'CRM Extract'
                })

        # Process default tables
        for table_name, data in defaults.items():
            folder_path = os.path.join(BUSINESSES_DIR, table_name)
            files_created = create_lookup_files(table_name, data, folder_path)

            stats['tables_populated'] += 1
            stats['total_files_created'] += files_created + 1  # +1 for INDEX
            stats['tables'].append({
                'name': table_name,
                'files_created': files_created + 1,
                'source': 'Default'
            })

        # Step 5: Generate report
        report = generate_report(stats)

        # Step 6: Create checkpoint
        create_checkpoint(stats)

        print("\n" + "="*60)
        print("PHASE 2 COMPLETED SUCCESSFULLY")
        print("="*60)
        print(f"\n✓ Populated {stats['tables_populated']} lookup tables")
        print(f"✓ Created {stats['total_files_created']} files")
        print(f"✓ Reports saved to: {IMPORTS_DIR}")
        print(f"\nNext: Review phase2_lookup_population_report.md and proceed to Phase 3")

    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        raise

if __name__ == "__main__":
    main()
