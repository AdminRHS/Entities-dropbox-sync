"""
Automated Entity Creation Script
Processes all 1000 CRM records into BUSINESSES entities
"""

import os
import sys
import json
import re
from datetime import datetime
from pathlib import Path

# Set UTF-8 encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Configuration
BASE_DIR = r"C:\Users\Dell\Dropbox\ENTITIES"
BUSINESSES_DIR = os.path.join(BASE_DIR, "BUSINESSES")
IMPORTS_DIR = os.path.join(BASE_DIR, "IMPORTS", "2025-11-22_Sales_Import")

# Counters
business_id_counter = 1
poc_id_counter = 1

def clean_company_name(name):
    """Clean company name for folder creation"""
    if not name:
        return "Unknown_Company"
    # Remove special characters, keep alphanumeric, spaces, hyphens
    cleaned = re.sub(r'[^\w\s-]', '', name)
    cleaned = re.sub(r'\s+', '_', cleaned.strip())
    return cleaned[:100]  # Limit length

def classify_entity_type(record):
    """Classify as Client, Prospect, or Ex_Client"""
    # Check status.name field
    status = record.get("status", {})
    if isinstance(status, dict):
        status_name = status.get("name", "").lower()
        if "client" in status_name:
            return "Client"
        if "ex" in status_name or "former" in status_name:
            return "Ex_Client"

    # Default to Prospect
    return "Prospect"

def generate_tags(record, entity_type):
    """Generate tags from record data"""
    tags = [entity_type.lower()]

    # Industry tags
    industry = record.get("lead_company_industry", {})
    if industry and industry.get("title"):
        tags.append(f"industry_{industry['title'].lower().replace(' ', '_')}")

    # Country tags
    country = record.get("country", {})
    if country and country.get("name"):
        tags.append(country["name"].lower().replace(" ", "_"))

    # Company size tags
    size = record.get("lead_company_size", {})
    if size and size.get("title"):
        size_title = size["title"]
        if "..." in size_title:
            try:
                max_size = int(size_title.split("...")[1])
                if max_size <= 10:
                    tags.append("small_company")
                elif max_size <= 50:
                    tags.append("medium_company")
                else:
                    tags.append("large_company")
            except:
                pass

    # Source tags
    lead_source = record.get("lead_source", {})
    if lead_source and lead_source.get("name"):
        tags.append(f"source_{lead_source['name'].lower().replace(' ', '_')}")

    # Status tags
    lead_status = record.get("lead_status", {})
    if lead_status and lead_status.get("type"):
        tags.append(f"status_{lead_status['type'].lower().replace(' ', '_')}")

    return sorted(list(set(tags)))

def calculate_quality_score(entity):
    """Calculate data completeness score"""
    score = 0
    total = 100

    # Company fields (40 points)
    if entity["company"]["name"]: score += 10
    if entity["company"]["website"]: score += 5
    if entity["company"]["size_id"]: score += 5
    if entity["company"]["industries"]: score += 10
    if entity["company"]["locations"]: score += 10

    # POCs (20 points)
    if entity["pocs"]:
        score += 10
        if entity["pocs"][0].get("email"):
            score += 10

    # Business relationship (15 points)
    if entity["business_relationship"]["status_id"]: score += 5
    if entity["business_relationship"]["source_id"]: score += 5
    if entity["business_relationship"]["relationship_start_date"]: score += 5

    # Assigned users (15 points)
    if entity["assigned_users"]["sales_manager_id"]: score += 5
    if entity["assigned_users"]["lead_agent_id"]: score += 5
    if entity["assigned_users"]["created_by_id"]: score += 5

    # References (10 points)
    if entity["references"]["crm_id"]: score += 10

    return min(score, 100)

def process_record(record, sequence_id):
    """Process a single CRM record into entity format"""
    global business_id_counter, poc_id_counter

    # Generate IDs
    business_id = f"BUS-2025-{business_id_counter:03d}"
    business_id_counter += 1

    # Company section
    company_name = record.get("company_name", "Unknown Company")
    company = {
        "id": business_id,
        "name": company_name,
        "logo": None,
        "website": record.get("website"),
        "size_id": record.get("lead_company_size", {}).get("id"),
        "size_label": record.get("lead_company_size", {}).get("title"),
        "year_established": None,
        "note": None,
        "locations": [],
        "industries": []
    }

    # Locations
    country = record.get("country", {})
    if country:
        company["locations"].append({
            "city_id": None,
            "city_name": None,
            "country_id": country.get("id"),
            "country_name": country.get("name"),
            "is_primary": True
        })

    # Industries
    industry = record.get("lead_company_industry", {})
    sub_industries = record.get("sub_industries", [])

    if industry:
        for sub_ind in sub_industries if sub_industries else [{}]:
            company["industries"].append({
                "industry_id": industry.get("id"),
                "industry_name": industry.get("title"),
                "sub_industry_id": sub_ind.get("id") if sub_ind else None,
                "sub_industry_name": sub_ind.get("name") if sub_ind else None
            })

        # If no sub-industries, still add main industry
        if not sub_industries:
            company["industries"].append({
                "industry_id": industry.get("id"),
                "industry_name": industry.get("title"),
                "sub_industry_id": None,
                "sub_industry_name": None
            })

    # POCs
    pocs = []
    contact_name = record.get("name")
    contact_email = record.get("user", {}).get("email")

    if contact_name:
        poc_id = f"POC-{poc_id_counter:03d}"
        poc_id_counter += 1

        pocs.append({
            "id": poc_id,
            "name": contact_name,
            "position_id": None,
            "position_title": None,
            "email": contact_email,
            "phone": None,
            "linkedin_url": None,
            "is_primary": True,
            "notes": None
        })

    # Business Relationship
    entity_type = classify_entity_type(record)
    lead_status = record.get("lead_status", {})
    lead_source = record.get("lead_source", {})
    created_at = record.get("lead_account", {}).get("created_at")

    business_relationship = {
        "entity_type": entity_type,
        "status_id": lead_status.get("id"),
        "status_type": lead_status.get("type"),
        "source_id": lead_source.get("id"),
        "source_name": lead_source.get("name"),
        "priority": lead_status.get("priority"),
        "relationship_start_date": created_at
    }

    # Communication History
    communication_history = {
        "total_interactions": 0,
        "last_contact_date": None,
        "interactions": []
    }

    # Assigned Users
    created_by = record.get("created_by", {})
    sales_manager_asst = record.get("sales_manager_assistant", {})
    lead_agent = record.get("lead_agent", {})

    assigned_users = {
        "sales_manager_id": record.get("sales_manager"),
        "sales_manager_name": sales_manager_asst.get("name"),
        "lead_agent_id": lead_agent.get("id"),
        "lead_agent_name": lead_agent.get("user", {}).get("name"),
        "created_by_id": created_by.get("id"),
        "created_by_name": created_by.get("name")
    }

    # References
    crm_id = record.get("client_id")
    linkedin = record.get("website")

    references = {
        "crm_link": f"https://crm-s.com/clients/{crm_id}" if crm_id else None,
        "crm_id": crm_id,
        "linkedin_company": linkedin if linkedin and "linkedin" in linkedin else None,
        "dropbox_path": f"ENTITIES/BUSINESSES/{entity_type}s/{clean_company_name(company_name)}/"
    }

    # Build entity
    entity = {
        "company": company,
        "pocs": pocs,
        "business_relationship": business_relationship,
        "communication_history": communication_history,
        "assigned_users": assigned_users,
        "references": references,
        "metadata": {
            "schema_version": "1.0.0",
            "tags": generate_tags(record, entity_type),
            "created_at": datetime.now().isoformat() + "Z",
            "updated_at": datetime.now().isoformat() + "Z",
            "source_file": record.get("_source_file"),
            "import_batch": "2025-11-22_Sales_Import",
            "data_quality_score": 0,  # Will calculate after
            "approved": False,
            "lifecycle_status": "active"
        }
    }

    # Calculate quality score
    entity["metadata"]["data_quality_score"] = calculate_quality_score(entity)

    return entity, entity_type, company_name

def save_entity(entity, entity_type, company_name):
    """Save entity to appropriate folder"""
    folder_name = clean_company_name(company_name)
    entity_folder = os.path.join(BUSINESSES_DIR, f"{entity_type}s", folder_name)

    os.makedirs(entity_folder, exist_ok=True)

    filepath = os.path.join(entity_folder, f"{folder_name}_MASTER.json")

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(entity, f, indent=2, ensure_ascii=False)

    return filepath

def main():
    print("="*60)
    print("AUTOMATED ENTITY CREATION")
    print("="*60)
    print()

    # Load raw data
    print("Loading raw data...")
    raw_data_path = os.path.join(IMPORTS_DIR, "raw_extracted_data.json")

    with open(raw_data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    records = data.get("records", [])
    print(f"✓ Loaded {len(records)} records\n")

    # Process all records
    stats = {
        "total": len(records),
        "processed": 0,
        "clients": 0,
        "prospects": 0,
        "ex_clients": 0,
        "errors": []
    }

    print("Processing records...")
    for idx, record in enumerate(records, 1):
        try:
            entity, entity_type, company_name = process_record(record, idx)
            filepath = save_entity(entity, entity_type, company_name)

            stats["processed"] += 1
            if entity_type == "Client":
                stats["clients"] += 1
            elif entity_type == "Ex_Client":
                stats["ex_clients"] += 1
            else:
                stats["prospects"] += 1

            if idx % 50 == 0:
                print(f"  ✓ Processed {idx}/{len(records)} records...")

        except Exception as e:
            stats["errors"].append({
                "record": idx,
                "company": record.get("company_name"),
                "error": str(e)
            })
            print(f"  ✗ Error processing record {idx}: {str(e)}")

    # Save final report
    print("\n" + "="*60)
    print("PROCESSING COMPLETE")
    print("="*60)
    print(f"\n✓ Total Processed: {stats['processed']}/{stats['total']}")
    print(f"✓ Clients: {stats['clients']}")
    print(f"✓ Prospects: {stats['prospects']}")
    print(f"✓ Ex_Clients: {stats['ex_clients']}")
    print(f"✓ Errors: {len(stats['errors'])}")

    # Save stats
    stats_path = os.path.join(IMPORTS_DIR, "processing_complete_stats.json")
    with open(stats_path, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2)

    print(f"\n✓ Stats saved: {stats_path}")

    if stats["errors"]:
        print("\nErrors encountered:")
        for error in stats["errors"][:10]:
            print(f"  - Record {error['record']}: {error['company']} - {error['error']}")

if __name__ == "__main__":
    main()
