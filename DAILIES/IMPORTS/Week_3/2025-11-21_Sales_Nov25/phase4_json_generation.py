import json
from pathlib import Path
from datetime import datetime
import re

# Configuration
ENTITIES_FILE = Path(r"C:\Users\Dell\Dropbox\ENTITIES\IMPORTS\2025-11-21_Sales_Nov25\entities_enriched.json")
BUSINESSES_DIR = Path(r"C:\Users\Dell\Dropbox\ENTITIES\BUSINESSES")
OUTPUT_DIR = Path(r"C:\Users\Dell\Dropbox\ENTITIES\IMPORTS\2025-11-21_Sales_Nov25")

def load_entities():
    """Load enriched entities from JSON file"""
    with open(ENTITIES_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def sanitize_filename(name):
    """Sanitize company name for use in filenames"""
    # Remove or replace invalid characters
    sanitized = re.sub(r'[<>:"/\\|?*]', '', name)
    sanitized = re.sub(r'\s+', '_', sanitized)
    sanitized = sanitized.strip('._')
    # Limit length
    if len(sanitized) > 50:
        sanitized = sanitized[:50]
    return sanitized

def create_directory_structure():
    """Create the BUSINESSES directory structure"""
    subdirs = ['Clients', 'Prospects', 'Ex_Clients', 'Companies']

    print("Creating directory structure...")
    for subdir in subdirs:
        dir_path = BUSINESSES_DIR / subdir
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"  [OK] {dir_path}")

    print()

def generate_json_file(entity):
    """Generate individual JSON file for an entity"""
    # Determine subdirectory based on sub_entity
    if entity['sub_entity'] == 'Client':
        subdir = 'Clients'
    elif entity['sub_entity'] == 'Prospect':
        subdir = 'Prospects'
    elif entity['sub_entity'] == 'Ex_Client':
        subdir = 'Ex_Clients'
    else:
        subdir = 'Prospects'  # Default

    # Create filename
    company_id = entity['company_id']
    company_name = sanitize_filename(entity['company_name'])
    filename = f"BUSINESSES_{entity['sub_entity']}_{company_name}_{company_id}.json"

    # Full path
    file_path = BUSINESSES_DIR / subdir / filename

    # Add metadata
    entity_copy = entity.copy()
    entity_copy['metadata'] = {
        'created_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'import_source': 'Sales_Nov25',
        'import_date': datetime.now().strftime('%Y-%m-%d'),
        'file_name': filename,
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    # Write JSON file
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(entity_copy, f, indent=2, ensure_ascii=False)

    return file_path, subdir

def create_index_file(entities, subdir):
    """Create index file for a sub-entity type"""
    # Filter entities for this subdirectory
    if subdir == 'Clients':
        filtered = [e for e in entities if e['sub_entity'] == 'Client']
    elif subdir == 'Prospects':
        filtered = [e for e in entities if e['sub_entity'] == 'Prospect']
    elif subdir == 'Ex_Clients':
        filtered = [e for e in entities if e['sub_entity'] == 'Ex_Client']
    else:
        filtered = []

    # Create index
    index = {
        'sub_entity_type': subdir,
        'total_count': len(filtered),
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'entities': []
    }

    for entity in filtered:
        company_name = sanitize_filename(entity['company_name'])
        filename = f"BUSINESSES_{entity['sub_entity']}_{company_name}_{entity['company_id']}.json"

        index['entities'].append({
            'company_id': entity['company_id'],
            'company_name': entity['company_name'],
            'status': entity['status'],
            'industry': entity['industry'],
            'account_manager': entity['account_manager'],
            'relationship_health': entity['relationship_health'],
            'tags': entity['tags'],
            'file_path': f"{subdir}/{filename}"
        })

    # Write index file
    index_path = BUSINESSES_DIR / subdir / f"{subdir}_INDEX.json"
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    return index_path

def create_master_catalog(entities):
    """Create master catalog file"""
    catalog = {
        'entity_type': 'BUSINESSES',
        'total_entities': len(entities),
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'import_info': {
            'import_date': datetime.now().strftime('%Y-%m-%d'),
            'source': 'Sales Nov25 - client_list.md',
            'import_phase': 'Phase 4 - JSON Generation'
        },
        'statistics': {
            'clients': len([e for e in entities if e['sub_entity'] == 'Client']),
            'prospects': len([e for e in entities if e['sub_entity'] == 'Prospect']),
            'ex_clients': len([e for e in entities if e['sub_entity'] == 'Ex_Client']),
            'by_status': {},
            'by_industry': {},
            'by_account_manager': {},
            'by_relationship_health': {}
        },
        'entities_by_id': {}
    }

    # Collect statistics
    for entity in entities:
        # By status
        status = entity['status']
        catalog['statistics']['by_status'][status] = catalog['statistics']['by_status'].get(status, 0) + 1

        # By industry
        industry = entity['industry']
        catalog['statistics']['by_industry'][industry] = catalog['statistics']['by_industry'].get(industry, 0) + 1

        # By account manager
        manager = entity['account_manager']
        catalog['statistics']['by_account_manager'][manager] = catalog['statistics']['by_account_manager'].get(manager, 0) + 1

        # By relationship health
        health = entity['relationship_health']
        catalog['statistics']['by_relationship_health'][health] = catalog['statistics']['by_relationship_health'].get(health, 0) + 1

        # Add to entities_by_id
        company_name = sanitize_filename(entity['company_name'])
        subdir = 'Clients' if entity['sub_entity'] == 'Client' else ('Ex_Clients' if entity['sub_entity'] == 'Ex_Client' else 'Prospects')
        filename = f"BUSINESSES_{entity['sub_entity']}_{company_name}_{entity['company_id']}.json"

        catalog['entities_by_id'][entity['company_id']] = {
            'company_name': entity['company_name'],
            'sub_entity': entity['sub_entity'],
            'status': entity['status'],
            'file_path': f"{subdir}/{filename}"
        }

    # Write master catalog
    catalog_path = BUSINESSES_DIR / "BUSINESSES_Master.json"
    with open(catalog_path, 'w', encoding='utf-8') as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)

    return catalog_path

def main():
    print("="*80)
    print("PHASE 4: JSON FILE GENERATION")
    print("="*80)
    print()

    # Load entities
    print(f"Loading enriched entities from: {ENTITIES_FILE}")
    entities = load_entities()
    print(f"[OK] Loaded {len(entities)} entities")
    print()

    # Create directory structure
    create_directory_structure()

    # Generate individual JSON files
    print("Generating individual JSON files...")
    file_count = {
        'Clients': 0,
        'Prospects': 0,
        'Ex_Clients': 0
    }

    for i, entity in enumerate(entities, 1):
        file_path, subdir = generate_json_file(entity)
        file_count[subdir] += 1

        if i % 10 == 0:
            print(f"  [Progress] {i}/{len(entities)} files created...")

    print(f"[OK] Created {len(entities)} JSON files")
    print()

    print("File distribution:")
    for subdir, count in file_count.items():
        print(f"  - {subdir}: {count} files")
    print()

    # Create index files
    print("Creating index files...")
    for subdir in ['Clients', 'Prospects', 'Ex_Clients']:
        index_path = create_index_file(entities, subdir)
        print(f"  [OK] {index_path.name}")
    print()

    # Create master catalog
    print("Creating master catalog...")
    catalog_path = create_master_catalog(entities)
    print(f"[OK] {catalog_path}")
    print()

    # Generate phase 4 report
    report_path = OUTPUT_DIR / "phase4_generation_report.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# Phase 4: JSON File Generation Report\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("---\n\n")

        f.write("## Summary\n\n")
        f.write(f"- **Total JSON Files Created:** {len(entities)}\n")
        f.write(f"- **Clients:** {file_count['Clients']}\n")
        f.write(f"- **Prospects:** {file_count['Prospects']}\n")
        f.write(f"- **Ex-Clients:** {file_count['Ex_Clients']}\n")
        f.write(f"- **Index Files Created:** 3\n")
        f.write(f"- **Master Catalog Created:** Yes\n\n")

        f.write("## Directory Structure\n\n")
        f.write("```\n")
        f.write("BUSINESSES/\n")
        f.write(f"├── Clients/ ({file_count['Clients']} files)\n")
        f.write(f"│   ├── Clients_INDEX.json\n")
        f.write(f"│   └── BUSINESSES_Client_*.json\n")
        f.write(f"├── Prospects/ ({file_count['Prospects']} files)\n")
        f.write(f"│   ├── Prospects_INDEX.json\n")
        f.write(f"│   └── BUSINESSES_Prospect_*.json\n")
        f.write(f"├── Ex_Clients/ ({file_count['Ex_Clients']} files)\n")
        f.write(f"│   ├── Ex_Clients_INDEX.json\n")
        f.write(f"│   └── BUSINESSES_Ex_Client_*.json\n")
        f.write(f"└── BUSINESSES_Master.json\n")
        f.write("```\n\n")

        f.write("## File Naming Convention\n\n")
        f.write("All entity files follow this pattern:\n\n")
        f.write("`BUSINESSES_[SubEntity]_[CompanyName]_[CompanyID].json`\n\n")
        f.write("Examples:\n")
        f.write("- `BUSINESSES_Client_TIAL_The_Institutional_Architecture_Lab_BUS-2025-001.json`\n")
        f.write("- `BUSINESSES_Prospect_Academic_Studies_Press_BUS-2025-005.json`\n")
        f.write("- `BUSINESSES_Ex_Client_Global_Wind_Service_BUS-2025-023.json`\n\n")

        f.write("## JSON Schema\n\n")
        f.write("Each JSON file contains:\n\n")
        f.write("- **Core Fields:** entity_type, sub_entity, company_id, company_name, status\n")
        f.write("- **Company Info:** industry, company_size, location\n")
        f.write("- **Relationship:** relationship_start, lifetime_value, account_manager\n")
        f.write("- **Contacts:** decision_makers array\n")
        f.write("- **Projects:** active_projects array\n")
        f.write("- **Health:** relationship_health score\n")
        f.write("- **References:** crm_link, transcription_link, dropbox_path\n")
        f.write("- **Communication:** communication_history array\n")
        f.write("- **Metadata:** tags, notes, metadata (created/updated timestamps)\n\n")

        f.write("## Index Files\n\n")
        f.write("Each subdirectory contains an INDEX.json file with:\n")
        f.write("- Quick reference to all entities in that category\n")
        f.write("- Key fields for filtering and searching\n")
        f.write("- File path references for easy access\n\n")

        f.write("## Master Catalog\n\n")
        f.write("The BUSINESSES_Master.json provides:\n")
        f.write("- Overall statistics and distribution\n")
        f.write("- Company ID lookup table\n")
        f.write("- Import metadata and timestamps\n")
        f.write("- Aggregated analytics by status, industry, manager, health\n\n")

        f.write("## Validation\n\n")
        f.write(f"- [OK] All {len(entities)} entities successfully written to JSON\n")
        f.write("- [OK] All files follow naming convention\n")
        f.write("- [OK] Directory structure created successfully\n")
        f.write("- [OK] Index files generated for all sub-entities\n")
        f.write("- [OK] Master catalog created with full statistics\n\n")

        f.write("## Next Steps\n\n")
        f.write("1. **Validate JSON Schema:** Ensure all files conform to expected schema\n")
        f.write("2. **Link Documents:** Connect transcripts and supporting documents\n")
        f.write("3. **Map Relationships:** Link to Products, Services, and Talents entities\n")
        f.write("4. **Quality Assurance:** Run comprehensive validation checks\n")
        f.write("5. **Documentation:** Create user guide for navigating the BUSINESSES entity\n\n")

    print(f"[OK] Phase 4 report saved: {report_path}")
    print()

    print("="*80)
    print("PHASE 4 COMPLETE")
    print("="*80)
    print()
    print(f"Total JSON Files: {len(entities)}")
    print(f"Location: {BUSINESSES_DIR}")
    print()
    print("Next Steps:")
    print("- Review phase4_generation_report.md")
    print("- Verify JSON files in BUSINESSES directory")
    print("- Proceed to Phase 5: Document Linking")

if __name__ == "__main__":
    main()
