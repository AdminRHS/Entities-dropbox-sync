import json
from pathlib import Path
from datetime import datetime
import re

# Configuration
BUSINESSES_DIR = Path(r"C:\Users\Dell\Dropbox\ENTITIES\BUSINESSES")
SALES_OCT25_DIR = Path(r"C:\Users\Dell\Dropbox\Nov25\Sales Nov25\Sales_Oct25\Clients")
OUTPUT_DIR = Path(r"C:\Users\Dell\Dropbox\ENTITIES\IMPORTS\2025-11-21_Sales_Nov25")

# Starting ID (after the 37 already imported)
STARTING_ID = 38

def sanitize_filename(name):
    """Sanitize company name for filenames"""
    sanitized = re.sub(r'[<>:"/\\|?*]', '', name)
    sanitized = re.sub(r'\s+', '_', sanitized)
    return sanitized.strip('._')[:50]

def extract_info_from_files(client_folder):
    """Extract information from files in client folder"""
    info = {
        "has_transcript": False,
        "has_email": False,
        "transcripts": [],
        "emails": [],
        "last_date": None
    }

    if not client_folder.exists():
        return info

    for file in client_folder.glob("*.md"):
        content = file.read_text(encoding='utf-8', errors='ignore')

        # Check if transcript
        if any(keyword in file.name.lower() for keyword in ['transcript', 'notes by gemini', 'call', 'meeting']):
            info["has_transcript"] = True
            info["transcripts"].append(str(file))

            # Try to extract date from filename
            date_match = re.search(r'(\d{4})[_\-](\d{2})[_\-](\d{2})', file.name)
            if date_match:
                file_date = f"{date_match.group(1)}-{date_match.group(2)}-{date_match.group(3)}"
                if not info["last_date"] or file_date > info["last_date"]:
                    info["last_date"] = file_date

        # Check if email
        if 'email' in file.name.lower():
            info["has_email"] = True
            info["emails"].append(str(file))

    return info

def create_entity(company_name, company_id, folder_info):
    """Create entity record for new client"""

    # Basic entity structure
    entity = {
        "entity_type": "BUSINESSES",
        "sub_entity": "Prospect",  # Default to prospect since not in main list
        "company_id": company_id,
        "company_name": company_name,
        "status": "Active_Outreach",
        "industry": "Unknown",
        "company_size": "Unknown",
        "location": "Unknown",
        "relationship_start": folder_info["last_date"] if folder_info["last_date"] else "",
        "lifetime_value": 0,
        "current_monthly_revenue": 0,
        "account_manager": "Unknown",  # To be determined
        "decision_makers": [],
        "active_projects": [],
        "relationship_health": "Moderate" if folder_info["last_date"] else "Unknown",
        "tags": ["active_prospect", "oct25_archive", "needs_review"],
        "crm_link": "",
        "transcription_link": "",
        "google_doc": "",
        "dropbox_path": f"/Sales_Oct25/Clients/{company_name}",
        "last_contact": folder_info["last_date"] if folder_info["last_date"] else "",
        "next_action": "Review Oct25 archive documents and classify",
        "communication_history": [],
        "notes": f"Added from Sales_Oct25 archive. Has {len(folder_info['transcripts'])} transcripts and {len(folder_info['emails'])} emails.",
        "email_content": "",
        "approved": "FALSE",
        "metadata": {
            "created_date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "import_source": "Sales_Oct25_Supplementary",
            "import_date": datetime.now().strftime('%Y-%m-%d'),
            "file_name": "",
            "last_updated": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    }

    # Add communication history from transcripts
    for transcript_path in folder_info["transcripts"]:
        transcript_name = Path(transcript_path).name
        date_match = re.search(r'(\d{4})[_\-](\d{2})[_\-](\d{2})', transcript_name)
        comm_date = f"{date_match.group(1)}-{date_match.group(2)}-{date_match.group(3)}" if date_match else "Unknown"

        entity["communication_history"].append({
            "date": comm_date,
            "type": "call_transcript",
            "summary": f"Call transcript: {transcript_name}",
            "file_path": transcript_path
        })

    # Add tags based on what we found
    if folder_info["has_transcript"]:
        entity["tags"].append("has_transcript")
    if folder_info["has_email"]:
        entity["tags"].append("has_email")

    return entity

def create_json_file(entity):
    """Create individual JSON file"""
    subdir = "Prospects"  # All supplementary entities go to Prospects for now

    company_name = sanitize_filename(entity['company_name'])
    filename = f"BUSINESSES_{entity['sub_entity']}_{company_name}_{entity['company_id']}.json"
    entity['metadata']['file_name'] = filename

    file_path = BUSINESSES_DIR / subdir / filename

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(entity, f, indent=2, ensure_ascii=False)

    return file_path

def update_index_file(new_entities):
    """Update Prospects index file"""
    index_path = BUSINESSES_DIR / "Prospects" / "Prospects_INDEX.json"

    # Load existing index
    with open(index_path, 'r', encoding='utf-8') as f:
        index = json.load(f)

    # Add new entities
    for entity in new_entities:
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
            'file_path': f"Prospects/{filename}"
        })

    # Update counts
    index['total_count'] = len(index['entities'])
    index['last_updated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Save updated index
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    return index_path

def update_master_catalog(new_entities):
    """Update master catalog"""
    catalog_path = BUSINESSES_DIR / "BUSINESSES_Master.json"

    # Load existing catalog
    with open(catalog_path, 'r', encoding='utf-8') as f:
        catalog = json.load(f)

    # Update counts
    catalog['total_entities'] += len(new_entities)
    catalog['statistics']['prospects'] += len(new_entities)
    catalog['last_updated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Add to entities_by_id
    for entity in new_entities:
        company_name = sanitize_filename(entity['company_name'])
        filename = f"BUSINESSES_{entity['sub_entity']}_{company_name}_{entity['company_id']}.json"

        catalog['entities_by_id'][entity['company_id']] = {
            'company_name': entity['company_name'],
            'sub_entity': entity['sub_entity'],
            'status': entity['status'],
            'file_path': f"Prospects/{filename}"
        }

    # Update statistics
    catalog['statistics']['by_status']['Active_Outreach'] = catalog['statistics']['by_status'].get('Active_Outreach', 0) + len(new_entities)
    catalog['statistics']['by_industry']['Unknown'] = catalog['statistics']['by_industry'].get('Unknown', 0) + len(new_entities)

    # Save updated catalog
    with open(catalog_path, 'w', encoding='utf-8') as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)

    return catalog_path

def main():
    print("="*80)
    print("PHASE 5: SUPPLEMENTARY IMPORT FROM SALES_OCT25")
    print("="*80)
    print()

    # Define the 3 new clients to add
    new_clients = [
        "GCO Medienagentur",
        "Greenland Commodities",
        "Marketing BIJ"
    ]

    print(f"Adding {len(new_clients)} new clients from Sales_Oct25 archive...")
    print()

    new_entities = []

    for i, client_name in enumerate(new_clients, STARTING_ID):
        company_id = f"BUS-2025-{i:03d}"

        # Get folder info
        client_folder = SALES_OCT25_DIR / client_name
        folder_info = extract_info_from_files(client_folder)

        print(f"Processing: {client_name} ({company_id})")
        print(f"  - Transcripts found: {len(folder_info['transcripts'])}")
        print(f"  - Emails found: {len(folder_info['emails'])}")
        print(f"  - Last contact: {folder_info['last_date'] or 'Unknown'}")

        # Create entity
        entity = create_entity(client_name, company_id, folder_info)
        new_entities.append(entity)

        # Create JSON file
        file_path = create_json_file(entity)
        print(f"  [OK] Created: {file_path.name}")
        print()

    print(f"[OK] Created {len(new_entities)} new entity files")
    print()

    # Update index
    print("Updating Prospects index...")
    index_path = update_index_file(new_entities)
    print(f"[OK] Updated: {index_path}")
    print()

    # Update master catalog
    print("Updating master catalog...")
    catalog_path = update_master_catalog(new_entities)
    print(f"[OK] Updated: {catalog_path}")
    print()

    # Generate report
    report_path = OUTPUT_DIR / "phase5_supplementary_report.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# Phase 5: Supplementary Import Report\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("---\n\n")
        f.write("## Summary\n\n")
        f.write(f"- **New Entities Added:** {len(new_entities)}\n")
        f.write(f"- **Source:** Sales_Oct25 archive\n")
        f.write(f"- **New ID Range:** BUS-2025-038 to BUS-2025-040\n")
        f.write(f"- **Total BUSINESSES Entities:** 40 (37 + 3)\n\n")

        f.write("## New Entities\n\n")
        f.write("| Company ID | Company Name | Transcripts | Emails | Last Contact |\n")
        f.write("|------------|--------------|-------------|--------|---------------|\n")
        for entity in new_entities:
            transcript_count = len([h for h in entity['communication_history'] if h['type'] == 'call_transcript'])
            email_count = 1 if 'has_email' in entity['tags'] else 0
            f.write(f"| {entity['company_id']} | {entity['company_name']} | {transcript_count} | {email_count} | {entity['last_contact'] or 'Unknown'} |\n")
        f.write("\n")

        f.write("## Files Created\n\n")
        for entity in new_entities:
            company_name = sanitize_filename(entity['company_name'])
            filename = f"BUSINESSES_{entity['sub_entity']}_{company_name}_{entity['company_id']}.json"
            f.write(f"- `Prospects/{filename}`\n")
        f.write("\n")

        f.write("## Next Steps\n\n")
        f.write("1. Review each new entity and complete missing fields:\n")
        f.write("   - Add contact information (decision_makers)\n")
        f.write("   - Classify industry\n")
        f.write("   - Assign account manager\n")
        f.write("   - Update status if needed\n")
        f.write("2. Read and enrich from Oct25 transcripts\n")
        f.write("3. Cross-reference with CRM system\n")
        f.write("4. Update FINAL_IMPORT_SUMMARY.md with new totals\n\n")

    print(f"[OK] Supplementary report saved: {report_path}")
    print()

    print("="*80)
    print("PHASE 5 SUPPLEMENTARY IMPORT COMPLETE")
    print("="*80)
    print()
    print(f"New Entities Added: {len(new_entities)}")
    print(f"Total BUSINESSES Entities: 40")
    print()
    print("Next Steps:")
    print("- Review new entities and complete missing fields")
    print("- Run enhanced enrichment from Sales_Oct25 documents")
    print("- Update final documentation")

if __name__ == "__main__":
    main()
