import re
import json
import csv
from datetime import datetime
from pathlib import Path
from collections import Counter

# Configuration
SOURCE_FILE = r"C:\Users\Dell\Dropbox\Nov25\Sales Nov25\client_list.md"
OUTPUT_DIR = Path(r"C:\Users\Dell\Dropbox\ENTITIES\IMPORTS\2025-11-21_Sales_Nov25")
BUSINESSES_DIR = Path(r"C:\Users\Dell\Dropbox\ENTITIES\BUSINESSES")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Starting ID for company_id generation
STARTING_ID = 1

def parse_client_list(file_path):
    """Parse the markdown table in client_list.md"""
    clients = []

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find the header and separator
    header_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith('| Client Company |'):
            header_idx = i
            break

    if header_idx is None:
        print("ERROR: Could not find table header")
        return clients

    # Extract headers
    header_line = lines[header_idx].strip()
    headers = [h.strip() for h in header_line.split('|')[1:-1]]

    # Parse data rows (skip header and separator)
    for line in lines[header_idx + 2:]:
        line = line.strip()
        if not line or not line.startswith('|'):
            continue

        # Split by pipe, remove first and last empty elements
        cells = [cell.strip() for cell in line.split('|')[1:-1]]

        # Skip empty rows
        if len(cells) < 3 or not cells[0]:
            continue

        # Create client record
        client = {}
        for i, header in enumerate(headers):
            if i < len(cells):
                client[header] = cells[i]
            else:
                client[header] = ""

        clients.append(client)

    return clients

def convert_date(date_str):
    """Convert date from MM/DD/YYYY to YYYY-MM-DD"""
    if not date_str or date_str.strip() == "":
        return None

    try:
        # Try MM/DD/YYYY format
        dt = datetime.strptime(date_str.strip(), "%m/%d/%Y")
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        try:
            # Try YYYY-MM-DD format
            dt = datetime.strptime(date_str.strip(), "%Y-%m-%d")
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            return None

def categorize_client(client):
    """Categorize client into sub-entity type and status"""
    status = client.get("Status", "").strip().lower()
    comments = client.get("Comments", "").strip().lower()

    # Check for hiring activity
    hiring_keywords = ["hired", "interview happened"]
    has_hiring = any(keyword in comments for keyword in hiring_keywords)

    if has_hiring:
        return "Clients", "Active_Client"
    elif status == "sent":
        return "Prospects", "Active_Outreach"
    elif status == "draft":
        return "Prospects", "Pipeline_Stage_Qualification"
    elif status == "transcript":
        return "Prospects", "Pipeline_Stage_Early"
    elif status == "new year":
        return "Ex_Clients", "Reengagement_Queue"
    else:
        return "Prospects", "Unknown_Status"

def calculate_relationship_health(last_contact_date, status):
    """Calculate relationship health score"""
    if not last_contact_date:
        return "Unknown"

    try:
        last_contact = datetime.strptime(last_contact_date, "%Y-%m-%d")
        today = datetime.now()
        days_ago = (today - last_contact).days

        if days_ago < 30 and status in ["Active_Client", "Active_Outreach"]:
            return "Strong"
        elif days_ago < 60:
            return "Moderate"
        else:
            return "Weak"
    except:
        return "Unknown"

def extract_industry(client):
    """Extract or infer industry from client data"""
    company_name = client.get("Client Company", "").lower()
    comments = client.get("Comments", "").lower()

    # Industry keywords mapping
    industry_map = {
        "AI": ["ai", "artificial intelligence", "automation"],
        "Research/Academic": ["research", "academic", "press", "studies"],
        "Technology": ["tech", "software", "digital", "IT"],
        "Finance": ["bank", "finance", "investment"],
        "Manufacturing": ["manufacturing", "production"],
        "Healthcare": ["health", "medical", "pharma"],
        "Consulting": ["consulting", "advisory"],
        "E-commerce": ["ecommerce", "e-commerce", "online shop"],
        "Marketing": ["marketing", "advertising", "media"],
        "Real Estate": ["real estate", "property", "development"],
    }

    for industry, keywords in industry_map.items():
        for keyword in keywords:
            if keyword in company_name or keyword in comments:
                return industry

    return "Unknown"

def generate_tags(client, sub_entity, status):
    """Generate tags based on client data"""
    tags = []

    # Sub-entity tags
    if sub_entity == "Clients":
        tags.append("active_client")
    elif sub_entity == "Prospects":
        tags.append("active_prospect")
    elif sub_entity == "Ex_Clients":
        tags.append("reengagement")

    # Status tags
    if status == "Active_Outreach":
        tags.append("outreach")
    elif status == "Pipeline_Stage_Qualification":
        tags.append("qualification")
    elif status == "Pipeline_Stage_Early":
        tags.append("early_stage")

    # Account manager tags
    sales_manager = client.get("Sales Manager", "").strip().lower()
    if "anastasia" in sales_manager:
        tags.append("anastasia_portfolio")
    elif "anush" in sales_manager:
        tags.append("anush_portfolio")

    # Comment-based tags
    comments = client.get("Comments", "").strip().lower()
    if "hired" in comments:
        tags.append("hired")
    if "interview" in comments:
        tags.append("interview")
    if "follow up" in comments or "follow-up" in comments:
        tags.append("follow_up_needed")
    if "lg" in comments or "lead gen" in comments:
        tags.append("lead_generation")
    if "design" in comments:
        tags.append("design_services")
    if "smm" in comments or "social media" in comments:
        tags.append("social_media")
    if "ai" in comments or "automation" in comments:
        tags.append("ai_automation")
    if "developer" in comments or "development" in comments:
        tags.append("development")

    # Time-based tags
    last_contact_str = client.get("Last Contact Day", "").strip()
    if last_contact_str:
        converted_date = convert_date(last_contact_str)
        if converted_date:
            try:
                last_contact = datetime.strptime(converted_date, "%Y-%m-%d")
                days_ago = (datetime.now() - last_contact).days
                if days_ago > 30:
                    tags.append("needs_followup")
                if days_ago > 60:
                    tags.append("dormant")
            except:
                pass

    return list(set(tags))  # Remove duplicates

def normalize_sales_manager(sales_manager_str):
    """Normalize sales manager name"""
    if not sales_manager_str or sales_manager_str.strip() == "":
        return "Unknown"

    normalized = sales_manager_str.strip()

    # Map to standard format
    if "anastasia" in normalized.lower():
        return "Kovalska_Anastasiya"
    elif "anush" in normalized.lower():
        return "Anush"  # Add full name if known

    return normalized

def extract_decision_makers(client):
    """Extract decision makers array"""
    decision_makers = []

    client_name = client.get("Client Name", "").strip()
    email = client.get("Email", "").strip()

    if client_name or email:
        decision_makers.append({
            "name": client_name if client_name else "Unknown",
            "title": "Unknown",
            "email": email if email else ""
        })

    return decision_makers

def extract_active_projects(comments):
    """Extract active projects from comments"""
    projects = []

    if not comments:
        return projects

    # Look for hiring patterns
    hired_pattern = r'hired\s+([A-Za-z]+(?:\s+[A-Z])?)\s+(\d+h)'
    matches = re.findall(hired_pattern, comments, re.IGNORECASE)

    for match in matches:
        name = match[0].strip()
        hours = match[1].strip()
        projects.append(f"{name}_{hours}")

    return projects

def generate_company_id(index):
    """Generate unique company ID"""
    return f"BUS-2025-{index:03d}"

def create_entity_record(client, index):
    """Create a complete entity record"""
    # Basic categorization
    sub_entity, status = categorize_client(client)

    # Date conversions
    relationship_start = convert_date(client.get("Date", ""))
    last_contact = convert_date(client.get("Last Contact Day", ""))

    # Use last_contact as relationship_start if relationship_start is missing
    if not relationship_start and last_contact:
        relationship_start = last_contact

    # Calculate relationship health
    relationship_health = calculate_relationship_health(last_contact, status)

    # Extract and normalize fields
    company_name = client.get("Client Company", "").strip()
    sales_manager = normalize_sales_manager(client.get("Sales Manager", ""))
    industry = extract_industry(client)
    decision_makers = extract_decision_makers(client)
    comments = client.get("Comments", "").strip()
    active_projects = extract_active_projects(comments)
    tags = generate_tags(client, sub_entity, status)

    # Build entity record
    entity = {
        "entity_type": "BUSINESSES",
        "sub_entity": sub_entity.rstrip('s'),  # Remove plural (Clients -> Client)
        "company_id": generate_company_id(index),
        "company_name": company_name,
        "status": status,
        "industry": industry,
        "company_size": "Unknown",
        "location": "Unknown",
        "relationship_start": relationship_start if relationship_start else "",
        "lifetime_value": 0,
        "current_monthly_revenue": 0,
        "account_manager": sales_manager,
        "decision_makers": decision_makers,
        "active_projects": active_projects,
        "relationship_health": relationship_health,
        "tags": tags,
        "crm_link": client.get("CRM Link", "").strip(),
        "transcription_link": client.get("Transcription Link", "").strip(),
        "google_doc": client.get("Google Doc", "").strip(),
        "dropbox_path": client.get("Dropbox", "").strip(),
        "last_contact": last_contact if last_contact else "",
        "next_action": client.get("To Do", "").strip(),
        "communication_history": [],
        "notes": comments,
        "email_content": client.get("Email Content", "").strip(),
        "approved": client.get("Approved", "").strip()
    }

    return entity, sub_entity

def main():
    print("="*80)
    print("PHASE 2: ENTITY EXTRACTION & CATEGORIZATION")
    print("="*80)
    print()

    # Parse client list
    print(f"Reading source file: {SOURCE_FILE}")
    clients = parse_client_list(SOURCE_FILE)
    print(f"[OK] Found {len(clients)} client records")
    print()

    # Extract entities
    print("Extracting and categorizing entities...")
    entities = []
    categorization_stats = Counter()

    for i, client in enumerate(clients, STARTING_ID):
        entity, sub_entity = create_entity_record(client, i)
        entities.append(entity)
        categorization_stats[sub_entity] += 1

    print(f"[OK] Extracted {len(entities)} entities")
    print()

    # Statistics
    print("Sub-Entity Distribution:")
    for sub_entity, count in categorization_stats.most_common():
        print(f"  - {sub_entity}: {count}")
    print()

    # Export to CSV
    csv_file = OUTPUT_DIR / "entities_extracted.csv"
    if entities:
        # Flatten decision_makers and active_projects for CSV
        csv_data = []
        for entity in entities:
            flat_entity = entity.copy()
            flat_entity['decision_makers'] = json.dumps(entity['decision_makers'])
            flat_entity['active_projects'] = json.dumps(entity['active_projects'])
            flat_entity['tags'] = json.dumps(entity['tags'])
            flat_entity['communication_history'] = json.dumps(entity['communication_history'])
            csv_data.append(flat_entity)

        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=csv_data[0].keys())
            writer.writeheader()
            writer.writerows(csv_data)

        print(f"[OK] Entities exported to CSV: {csv_file}")

    # Export to JSON
    json_file = OUTPUT_DIR / "entities_extracted.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(entities, f, indent=2, ensure_ascii=False)
    print(f"[OK] Entities exported to JSON: {json_file}")
    print()

    # Generate categorization report
    report_file = OUTPUT_DIR / "categorization_report.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# Phase 2: Categorization Report\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("---\n\n")

        f.write("## Summary\n\n")
        f.write(f"- **Total Entities Extracted:** {len(entities)}\n")
        f.write(f"- **Clients:** {categorization_stats.get('Client', 0)}\n")
        f.write(f"- **Prospects:** {categorization_stats.get('Prospect', 0)}\n")
        f.write(f"- **Ex-Clients:** {categorization_stats.get('Ex_Client', 0)}\n\n")

        f.write("## Categorization Details\n\n")

        # Group entities by sub_entity
        by_sub_entity = {}
        for entity in entities:
            sub_entity = entity['sub_entity']
            if sub_entity not in by_sub_entity:
                by_sub_entity[sub_entity] = []
            by_sub_entity[sub_entity].append(entity)

        for sub_entity, entity_list in sorted(by_sub_entity.items()):
            f.write(f"### {sub_entity}s ({len(entity_list)})\n\n")
            f.write("| Company ID | Company Name | Status | Relationship Health | Tags |\n")
            f.write("|------------|--------------|--------|---------------------|------|\n")

            for entity in entity_list:
                tags_str = ", ".join(entity['tags'][:3])  # Show first 3 tags
                if len(entity['tags']) > 3:
                    tags_str += "..."
                f.write(f"| {entity['company_id']} | {entity['company_name']} | "
                       f"{entity['status']} | {entity['relationship_health']} | {tags_str} |\n")
            f.write("\n")

        f.write("## Status Distribution\n\n")
        status_counts = Counter([e['status'] for e in entities])
        f.write("| Status | Count |\n")
        f.write("|--------|-------|\n")
        for status, count in status_counts.most_common():
            f.write(f"| {status} | {count} |\n")
        f.write("\n")

        f.write("## Relationship Health Distribution\n\n")
        health_counts = Counter([e['relationship_health'] for e in entities])
        f.write("| Health Score | Count |\n")
        f.write("|--------------|-------|\n")
        for health, count in health_counts.most_common():
            f.write(f"| {health} | {count} |\n")
        f.write("\n")

        f.write("## Industry Distribution\n\n")
        industry_counts = Counter([e['industry'] for e in entities])
        f.write("| Industry | Count |\n")
        f.write("|----------|-------|\n")
        for industry, count in industry_counts.most_common():
            f.write(f"| {industry} | {count} |\n")
        f.write("\n")

        f.write("## Account Manager Distribution\n\n")
        manager_counts = Counter([e['account_manager'] for e in entities])
        f.write("| Account Manager | Count |\n")
        f.write("|-----------------|-------|\n")
        for manager, count in manager_counts.most_common():
            f.write(f"| {manager} | {count} |\n")
        f.write("\n")

        f.write("## Tag Analysis\n\n")
        all_tags = []
        for entity in entities:
            all_tags.extend(entity['tags'])
        tag_counts = Counter(all_tags)
        f.write("| Tag | Count |\n")
        f.write("|-----|-------|\n")
        for tag, count in tag_counts.most_common(20):  # Top 20 tags
            f.write(f"| {tag} | {count} |\n")
        f.write("\n")

        f.write("## Data Transformation Summary\n\n")
        f.write("### Transformations Applied\n\n")
        f.write("1. **Date Format:** MM/DD/YYYY -> YYYY-MM-DD (ISO 8601)\n")
        f.write("2. **Status Mapping:** Source status -> Target status codes\n")
        f.write("3. **Contact Restructuring:** Flat fields -> decision_makers array\n")
        f.write("4. **ID Generation:** Sequential BUS-2025-XXX format\n")
        f.write("5. **Relationship Health:** Calculated from last contact + status\n")
        f.write("6. **Tag Generation:** Auto-generated from multiple sources\n")
        f.write("7. **Industry Inference:** Extracted from company name and comments\n")
        f.write("8. **Active Projects:** Parsed from comments using regex\n\n")

    print(f"[OK] Categorization report saved: {report_file}")
    print()

    print("="*80)
    print("PHASE 2 COMPLETE")
    print("="*80)
    print()
    print("Next Steps:")
    print("- Review categorization_report.md")
    print("- Review entities_extracted.json")
    print("- Proceed to Phase 3: Data Enrichment")

if __name__ == "__main__":
    main()
