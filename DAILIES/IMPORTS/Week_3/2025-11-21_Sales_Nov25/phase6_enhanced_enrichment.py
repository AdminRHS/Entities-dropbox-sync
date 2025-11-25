import json
from pathlib import Path
from datetime import datetime
import re
import sys

# Fix encoding for Windows console
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Configuration
ENTITIES_FILE = Path(r"C:\Users\Dell\Dropbox\ENTITIES\IMPORTS\2025-11-21_Sales_Nov25\entities_enriched.json")
SOURCE_FILE = Path(r"C:\Users\Dell\Dropbox\Nov25\Sales Nov25\client_list.md")
BUSINESSES_DIR = Path(r"C:\Users\Dell\Dropbox\ENTITIES\BUSINESSES")
OUTPUT_DIR = Path(r"C:\Users\Dell\Dropbox\ENTITIES\IMPORTS\2025-11-21_Sales_Nov25")

def parse_client_list_detailed(file_path):
    """Parse the markdown table with full details"""
    clients = []

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    header_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith('| Client Company |'):
            header_idx = i
            break

    if header_idx is None:
        return clients

    headers = [h.strip() for h in lines[header_idx].strip().split('|')[1:-1]]

    for line in lines[header_idx + 2:]:
        line = line.strip()
        if not line or not line.startswith('|'):
            continue

        cells = [cell.strip() for cell in line.split('|')[1:-1]]

        if len(cells) < 3 or not cells[0]:
            continue

        client = {}
        for i, header in enumerate(headers):
            if i < len(cells):
                client[header] = cells[i]
            else:
                client[header] = ""

        clients.append(client)

    return clients

def extract_services_from_comments(comments):
    """Extract service interests from comments"""
    services = []

    if not comments:
        return services

    comments_lower = comments.lower()

    # Service keywords mapping
    service_patterns = {
        "Lead Generation": ["lg", "lead gen", "lead generation", "leadgen", "lg managers"],
        "Design": ["design", "designer", "graphic design", "ui/ux", "branding"],
        "Development": ["developer", "development", "coding", "programming", "web dev", "website"],
        "Social Media": ["smm", "social media", "instagram", "linkedin", "facebook"],
        "AI/Automation": ["ai", "automation", "chatbot", "ai/automation"],
        "Content Writing": ["content", "copywriting", "writer", "writing"],
        "Video Production": ["video", "editing", "production"],
        "Virtual Assistant": ["va", "virtual assistant", "admin support"],
        "Customer Support": ["customer support", "support", "call center"],
        "Data Entry": ["data entry", "data processing"],
        "Project Management": ["project management", "pm", "coordinator"]
    }

    for service, keywords in service_patterns.items():
        if any(keyword in comments_lower for keyword in keywords):
            services.append(service)

    return list(set(services))

def extract_services_from_email(email_content):
    """Extract service interests from email content"""
    services = []

    if not email_content:
        return services

    email_lower = email_content.lower()

    # Service keywords in email
    service_patterns = {
        "Lead Generation": ["lead generation", "prospecting", "outreach", "linkedin", "database building"],
        "Design": ["design", "visuals", "branding", "logo", "ui/ux"],
        "Development": ["development", "developer", "website", "platform", "technical"],
        "Social Media": ["social media", "smm", "posts", "instagram", "facebook"],
        "AI/Automation": ["ai", "automation", "chatbot", "automated"],
        "Content Writing": ["content", "copywriting", "blog", "articles"],
    }

    for service, keywords in service_patterns.items():
        if any(keyword in email_lower for keyword in keywords):
            services.append(service)

    return list(set(services))

def analyze_urgency(comments, todo, email):
    """Determine urgency level"""
    urgency_keywords = {
        "urgent": ["urgent", "asap", "immediately", "as soon as possible"],
        "high": ["important", "priority", "needs attention", "follow up soon"],
        "medium": ["follow up", "schedule", "set a call"],
        "low": ["when convenient", "no rush"]
    }

    combined_text = f"{comments} {todo} {email}".lower()

    for level, keywords in urgency_keywords.items():
        if any(keyword in combined_text for keyword in keywords):
            return level

    return "normal"

def extract_company_size_hints(comments, email):
    """Try to extract company size hints"""
    combined = f"{comments} {email}".lower()

    # Look for employee count mentions
    patterns = [
        r'(\d+)\s*(?:employees?|staff|people|team)',
        r'team of (\d+)',
        r'(\d+)[\s-]person'
    ]

    for pattern in patterns:
        match = re.search(pattern, combined)
        if match:
            count = int(match.group(1))
            if count < 10:
                return "1-10 employees"
            elif count < 50:
                return "11-50 employees"
            elif count < 200:
                return "51-200 employees"
            elif count < 500:
                return "201-500 employees"
            else:
                return "500+ employees"

    return "Unknown"

def extract_budget_info(comments, email):
    """Extract budget/pricing mentions"""
    combined = f"{comments} {email}"

    # Look for dollar amounts or pricing mentions
    dollar_pattern = r'\$\s*(\d{1,3}(?:,?\d{3})*(?:\.\d{2})?)'
    matches = re.findall(dollar_pattern, combined)

    if matches:
        amounts = [float(m.replace(',', '')) for m in matches]
        if amounts:
            return {
                "budget_mentioned": True,
                "estimated_value": max(amounts),
                "currency": "USD"
            }

    # Look for pricing discussions
    if any(keyword in combined.lower() for keyword in ['pricing', 'rate', 'cost', 'budget', 'quote']):
        return {
            "budget_mentioned": True,
            "estimated_value": None,
            "currency": None
        }

    return {
        "budget_mentioned": False,
        "estimated_value": None,
        "currency": None
    }

def parse_next_actions(todo, comments):
    """Parse and structure next actions"""
    actions = []

    if todo:
        actions.append({
            "action": todo,
            "source": "to_do_field",
            "priority": "high"
        })

    # Extract actions from comments
    if comments:
        action_patterns = [
            r'(?:need to|should|will|plan to)\s+([^.;]+)',
            r'(?:schedule|set up|arrange)\s+([^.;]+)',
        ]

        for pattern in action_patterns:
            matches = re.findall(pattern, comments, re.IGNORECASE)
            for match in matches:
                if len(match) < 100:  # Reasonable action length
                    actions.append({
                        "action": match.strip(),
                        "source": "comments",
                        "priority": "medium"
                    })

    return actions[:5]  # Limit to top 5 actions

def enhance_entity(entity, source_client):
    """Add detailed enrichment to entity"""

    comments = source_client.get("Comments", "")
    email_content = source_client.get("Email Content", "")
    todo = source_client.get("To Do", "")

    # Extract services of interest
    services_from_comments = extract_services_from_comments(comments)
    services_from_email = extract_services_from_email(email_content)
    all_services = list(set(services_from_comments + services_from_email))

    # Update entity with detailed information
    entity["services_of_interest"] = all_services

    # Add service tags
    for service in all_services:
        service_tag = service.lower().replace(" ", "_").replace("/", "_")
        if service_tag not in entity["tags"]:
            entity["tags"].append(service_tag)

    # Add urgency level
    entity["urgency_level"] = analyze_urgency(comments, todo, email_content)

    # Try to determine company size
    company_size_hint = extract_company_size_hints(comments, email_content)
    if company_size_hint != "Unknown":
        entity["company_size"] = company_size_hint

    # Extract budget information
    budget_info = extract_budget_info(comments, email_content)
    entity["budget_info"] = budget_info

    if budget_info["budget_mentioned"] and "budget_discussed" not in entity["tags"]:
        entity["tags"].append("budget_discussed")

    # Parse next actions
    next_actions = parse_next_actions(todo, comments)
    entity["next_actions"] = next_actions

    # Add detailed last contact info
    if entity.get("last_contact"):
        try:
            last_contact_date = datetime.strptime(entity["last_contact"], "%Y-%m-%d")
            days_ago = (datetime.now() - last_contact_date).days

            entity["last_contact_details"] = {
                "date": entity["last_contact"],
                "days_ago": days_ago,
                "recency": "recent" if days_ago < 7 else "this_month" if days_ago < 30 else "over_month" if days_ago < 60 else "stale"
            }

            # Add recency tag
            if days_ago > 30 and "needs_immediate_followup" not in entity["tags"]:
                entity["tags"].append("needs_immediate_followup")

        except:
            pass

    # Extract key phrases from comments for quick reference
    if comments and len(comments) > 20:
        entity["key_notes"] = comments[:200] + ("..." if len(comments) > 200 else "")

    return entity

def update_json_file(entity):
    """Update the JSON file for an entity"""
    # Determine subdirectory
    if entity['sub_entity'] == 'Client':
        subdir = 'Clients'
    elif entity['sub_entity'] == 'Prospect':
        subdir = 'Prospects'
    elif entity['sub_entity'] == 'Ex_Client':
        subdir = 'Ex_Clients'
    else:
        return None

    # Find the file
    company_id = entity['company_id']

    for json_file in (BUSINESSES_DIR / subdir).glob(f"*{company_id}.json"):
        # Update the file
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(entity, f, indent=2, ensure_ascii=False)
        return json_file

    return None

def main():
    print("="*80)
    print("PHASE 6: ENHANCED ENRICHMENT - Detailed Information Extraction")
    print("="*80)
    print()

    # Load entities
    print(f"Loading entities from: {ENTITIES_FILE}")
    with open(ENTITIES_FILE, 'r', encoding='utf-8') as f:
        entities = json.load(f)
    print(f"[OK] Loaded {len(entities)} entities")
    print()

    # Load source client list
    print(f"Loading source data from: {SOURCE_FILE}")
    source_clients = parse_client_list_detailed(SOURCE_FILE)
    print(f"[OK] Loaded {len(source_clients)} source records")
    print()

    # Create lookup by company name
    source_lookup = {client["Client Company"]: client for client in source_clients}

    # Enhance entities
    print("Enhancing entities with detailed information...")
    print()

    enhanced_count = 0
    services_added = 0
    budget_info_added = 0

    for entity in entities:
        company_name = entity["company_name"]

        # Find matching source record
        source_client = source_lookup.get(company_name)

        if source_client:
            services_before = len(entity.get("services_of_interest", []))

            # Enhance entity
            entity = enhance_entity(entity, source_client)

            services_after = len(entity.get("services_of_interest", []))

            if services_after > services_before:
                services_added += (services_after - services_before)

            if entity.get("budget_info", {}).get("budget_mentioned"):
                budget_info_added += 1

            # Update JSON file
            updated_file = update_json_file(entity)
            if updated_file:
                enhanced_count += 1

                # Print summary for this entity
                print(f"[OK] {entity['company_id']}: {company_name}")
                if entity.get("services_of_interest"):
                    print(f"  Services: {', '.join(entity['services_of_interest'])}")
                if entity.get("last_contact_details"):
                    lcd = entity["last_contact_details"]
                    print(f"  Last Contact: {lcd['date']} ({lcd['days_ago']} days ago - {lcd['recency']})")
                if entity.get("urgency_level") and entity["urgency_level"] != "normal":
                    print(f"  Urgency: {entity['urgency_level']}")
                if entity.get("budget_info", {}).get("budget_mentioned"):
                    if entity["budget_info"].get("estimated_value"):
                        print(f"  Budget: ${entity['budget_info']['estimated_value']:,.2f}")
                    else:
                        print(f"  Budget: Discussed (amount not specified)")
                print()

    print(f"[OK] Enhanced {enhanced_count} entities")
    print(f"[OK] Added {services_added} service interests")
    print(f"[OK] Found budget info in {budget_info_added} entities")
    print()

    # Generate enhanced enrichment report
    report_file = OUTPUT_DIR / "phase6_enhanced_enrichment_report.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# Phase 6: Enhanced Enrichment Report\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("---\n\n")

        f.write("## Summary\n\n")
        f.write(f"- **Entities Enhanced:** {enhanced_count} / {len(entities)}\n")
        f.write(f"- **Service Interests Added:** {services_added}\n")
        f.write(f"- **Budget Information Found:** {budget_info_added}\n\n")

        f.write("## New Fields Added\n\n")
        f.write("Each entity now includes:\n\n")
        f.write("1. **services_of_interest** - Array of services the client is interested in\n")
        f.write("2. **urgency_level** - Priority level (urgent, high, medium, low, normal)\n")
        f.write("3. **budget_info** - Budget mentions and estimated values\n")
        f.write("4. **next_actions** - Structured list of follow-up actions\n")
        f.write("5. **last_contact_details** - Detailed last contact information with days_ago and recency\n")
        f.write("6. **key_notes** - Quick reference summary from comments\n")
        f.write("7. **company_size** - Estimated company size (when detectable)\n\n")

        f.write("## Service Interest Analysis\n\n")

        # Aggregate service interests
        from collections import Counter
        all_services = []
        for entity in entities:
            all_services.extend(entity.get("services_of_interest", []))

        service_counts = Counter(all_services)

        if service_counts:
            f.write("| Service | Interested Companies |\n")
            f.write("|---------|----------------------|\n")
            for service, count in service_counts.most_common():
                f.write(f"| {service} | {count} |\n")
            f.write("\n")

        f.write("## Urgency Distribution\n\n")

        urgency_counts = Counter([e.get("urgency_level", "normal") for e in entities])
        f.write("| Urgency Level | Count |\n")
        f.write("|---------------|-------|\n")
        for level, count in urgency_counts.most_common():
            f.write(f"| {level} | {count} |\n")
        f.write("\n")

        f.write("## Last Contact Recency\n\n")

        recency_counts = Counter([
            e.get("last_contact_details", {}).get("recency", "unknown")
            for e in entities
        ])
        f.write("| Recency | Count |\n")
        f.write("|---------|-------|\n")
        for recency, count in recency_counts.most_common():
            f.write(f"| {recency} | {count} |\n")
        f.write("\n")

        f.write("## High-Value Opportunities\n\n")
        f.write("Companies with budget discussions:\n\n")

        budget_entities = [e for e in entities if e.get("budget_info", {}).get("budget_mentioned")]
        if budget_entities:
            f.write("| Company | Budget Value | Services Interested |\n")
            f.write("|---------|--------------|---------------------|\n")
            for entity in budget_entities:
                budget_val = entity["budget_info"].get("estimated_value")
                budget_str = f"${budget_val:,.0f}" if budget_val else "Discussed"
                services_str = ", ".join(entity.get("services_of_interest", ["Not specified"]))
                f.write(f"| {entity['company_name']} | {budget_str} | {services_str} |\n")
            f.write("\n")
        else:
            f.write("No explicit budget discussions found in source data.\n\n")

        f.write("## Recommendations\n\n")
        f.write("1. **Immediate Follow-Up:** Contact entities with 'urgent' or 'high' urgency\n")
        f.write("2. **Service Matching:** Match service interests to your offerings\n")
        f.write("3. **Budget Prioritization:** Focus on entities with budget discussions\n")
        f.write("4. **Recency Action:** Re-engage 'stale' contacts (60+ days)\n\n")

    print(f"[OK] Enhanced enrichment report saved: {report_file}")
    print()

    print("="*80)
    print("PHASE 6 ENHANCED ENRICHMENT COMPLETE")
    print("="*80)
    print()
    print("Enhanced Information Now Available:")
    print("- Service interests for targeted outreach")
    print("- Last contact recency for prioritization")
    print("- Urgency levels for action planning")
    print("- Budget information for opportunity sizing")
    print("- Structured next actions for follow-up")

if __name__ == "__main__":
    main()
