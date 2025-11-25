import re
import json
import csv
from datetime import datetime
from pathlib import Path
from collections import Counter

# Configuration
SOURCE_FILE = r"C:\Users\Dell\Dropbox\Nov25\Sales Nov25\client_list.md"
OUTPUT_DIR = Path(r"C:\Users\Dell\Dropbox\ENTITIES\IMPORTS\2025-11-21_Sales_Nov25")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

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

def validate_date(date_str):
    """Validate and convert date format"""
    if not date_str or date_str.strip() == "":
        return None, "Missing"

    try:
        # Try MM/DD/YYYY format
        dt = datetime.strptime(date_str.strip(), "%m/%d/%Y")
        return dt.strftime("%Y-%m-%d"), "Valid"
    except ValueError:
        try:
            # Try other common formats
            dt = datetime.strptime(date_str.strip(), "%Y-%m-%d")
            return dt.strftime("%Y-%m-%d"), "Valid"
        except ValueError:
            return date_str, "Invalid format"

def validate_email(email):
    """Validate email format"""
    if not email or email.strip() == "":
        return "Missing"

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email.strip()):
        return "Valid"
    return "Invalid format"

def validate_url(url):
    """Validate URL format"""
    if not url or url.strip() == "":
        return "Missing"

    if url.strip().startswith("http://") or url.strip().startswith("https://"):
        return "Valid"
    return "Invalid format"

def check_dropbox_path(path):
    """Check if Dropbox path exists"""
    if not path or path.strip() == "":
        return "Missing", None

    # Normalize the path
    path = path.strip()

    # Try different variations
    variations = [
        path,
        path.replace("/Dropbox/", r"C:\Users\Dell\Dropbox\\"),
        path.replace("Dropbox/", r"C:\Users\Dell\Dropbox\\"),
        r"C:\Users\Dell\Dropbox" + path.replace("/", "\\"),
    ]

    for var in variations:
        p = Path(var)
        if p.exists():
            return "Exists", str(p)

    return "Not Found", None

def categorize_client(client):
    """Categorize client into sub-entity type"""
    status = client.get("Status", "").strip().lower()
    comments = client.get("Comments", "").strip().lower()

    # Check for hiring activity
    hiring_keywords = ["hired", "interview happened"]
    has_hiring = any(keyword in comments for keyword in hiring_keywords)

    if has_hiring:
        return "Client", "Active_Client"
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

        if days_ago < 30 and status in ["sent", "Sent"]:
            return "Strong"
        elif days_ago < 60:
            return "Moderate"
        else:
            return "Weak"
    except:
        return "Unknown"

def generate_tags(client, sub_entity):
    """Generate tags based on client data"""
    tags = []

    # Status-based tags
    status = client.get("Status", "").strip().lower()
    if status == "sent":
        tags.append("active_outreach")
    elif status == "draft":
        tags.append("draft_stage")
    elif status == "transcript":
        tags.append("early_contact")

    # Sub-entity tags
    if sub_entity == "Client":
        tags.append("active_client")
    elif sub_entity == "Prospects":
        tags.append("active_prospect")

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
    if "follow up" in comments:
        tags.append("follow_up_needed")
    if "lg" in comments or "lead gen" in comments:
        tags.append("lead_generation")
    if "design" in comments:
        tags.append("design_services")

    # Time-based tags
    last_contact_str = client.get("Last Contact Day", "").strip()
    if last_contact_str:
        converted_date, valid = validate_date(last_contact_str)
        if valid == "Valid":
            try:
                last_contact = datetime.strptime(converted_date, "%Y-%m-%d")
                days_ago = (datetime.now() - last_contact).days
                if days_ago > 30:
                    tags.append("needs_followup")
            except:
                pass

    return list(set(tags))  # Remove duplicates

def main():
    print("="*80)
    print("PHASE 1: VALIDATION & PREPARATION")
    print("="*80)
    print()

    # Parse client list
    print(f"Reading source file: {SOURCE_FILE}")
    clients = parse_client_list(SOURCE_FILE)
    print(f"[OK] Found {len(clients)} client records")
    print()

    # Validation statistics
    stats = {
        "total_records": len(clients),
        "missing_company_name": 0,
        "missing_email": 0,
        "invalid_email": 0,
        "missing_crm_link": 0,
        "invalid_crm_link": 0,
        "missing_last_contact": 0,
        "invalid_last_contact": 0,
        "missing_date": 0,
        "invalid_date": 0,
        "missing_dropbox_path": 0,
        "invalid_dropbox_path": 0,
        "missing_sales_manager": 0,
        "status_distribution": Counter(),
        "sales_manager_distribution": Counter(),
        "sub_entity_distribution": Counter(),
    }

    # Detailed validation results
    validation_results = []

    for i, client in enumerate(clients, 1):
        result = {
            "row": i,
            "company_name": client.get("Client Company", ""),
            "issues": []
        }

        # Validate company name
        if not client.get("Client Company", "").strip():
            stats["missing_company_name"] += 1
            result["issues"].append("Missing company name")

        # Validate email
        email_status = validate_email(client.get("Email", ""))
        if email_status == "Missing":
            stats["missing_email"] += 1
            result["issues"].append("Missing email")
        elif email_status == "Invalid format":
            stats["invalid_email"] += 1
            result["issues"].append("Invalid email format")

        # Validate CRM Link
        crm_status = validate_url(client.get("CRM Link", ""))
        if crm_status == "Missing":
            stats["missing_crm_link"] += 1
            result["issues"].append("Missing CRM link")
        elif crm_status == "Invalid format":
            stats["invalid_crm_link"] += 1
            result["issues"].append("Invalid CRM link format")

        # Validate Last Contact Day
        last_contact_str = client.get("Last Contact Day", "")
        converted_last_contact, last_contact_status = validate_date(last_contact_str)
        if last_contact_status == "Missing":
            stats["missing_last_contact"] += 1
            result["issues"].append("Missing last contact date")
        elif last_contact_status == "Invalid format":
            stats["invalid_last_contact"] += 1
            result["issues"].append(f"Invalid last contact date: {last_contact_str}")

        # Validate Date
        date_str = client.get("Date", "")
        converted_date, date_status = validate_date(date_str)
        if date_status == "Missing":
            stats["missing_date"] += 1
            result["issues"].append("Missing relationship start date")
        elif date_status == "Invalid format":
            stats["invalid_date"] += 1
            result["issues"].append(f"Invalid relationship start date: {date_str}")

        # Validate Dropbox Path
        dropbox_path = client.get("Dropbox", "")
        path_status, resolved_path = check_dropbox_path(dropbox_path)
        if path_status == "Missing":
            stats["missing_dropbox_path"] += 1
            result["issues"].append("Missing Dropbox path")
        elif path_status == "Not Found":
            stats["invalid_dropbox_path"] += 1
            result["issues"].append(f"Dropbox path not found: {dropbox_path}")

        # Validate Sales Manager
        if not client.get("Sales Manager", "").strip():
            stats["missing_sales_manager"] += 1
            result["issues"].append("Missing sales manager")

        # Status distribution
        status = client.get("Status", "").strip()
        stats["status_distribution"][status] += 1

        # Sales manager distribution
        sales_manager = client.get("Sales Manager", "").strip()
        stats["sales_manager_distribution"][sales_manager] += 1

        # Sub-entity categorization
        sub_entity, _ = categorize_client(client)
        stats["sub_entity_distribution"][sub_entity] += 1

        validation_results.append(result)

    # Generate validation report
    report_file = OUTPUT_DIR / "validation_report.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# Phase 1: Validation Report\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**Source File:** `{SOURCE_FILE}`\n\n")
        f.write("---\n\n")

        f.write("## Summary Statistics\n\n")
        f.write(f"- **Total Records:** {stats['total_records']}\n")
        f.write(f"- **Missing Company Names:** {stats['missing_company_name']}\n")
        f.write(f"- **Missing Emails:** {stats['missing_email']}\n")
        f.write(f"- **Invalid Emails:** {stats['invalid_email']}\n")
        f.write(f"- **Missing CRM Links:** {stats['missing_crm_link']}\n")
        f.write(f"- **Invalid CRM Links:** {stats['invalid_crm_link']}\n")
        f.write(f"- **Missing Last Contact Dates:** {stats['missing_last_contact']}\n")
        f.write(f"- **Invalid Last Contact Dates:** {stats['invalid_last_contact']}\n")
        f.write(f"- **Missing Relationship Start Dates:** {stats['missing_date']}\n")
        f.write(f"- **Invalid Relationship Start Dates:** {stats['invalid_date']}\n")
        f.write(f"- **Missing Dropbox Paths:** {stats['missing_dropbox_path']}\n")
        f.write(f"- **Invalid Dropbox Paths:** {stats['invalid_dropbox_path']}\n")
        f.write(f"- **Missing Sales Manager:** {stats['missing_sales_manager']}\n\n")

        f.write("## Status Distribution\n\n")
        f.write("| Status | Count |\n")
        f.write("|--------|-------|\n")
        for status, count in stats['status_distribution'].most_common():
            f.write(f"| {status or '(empty)'} | {count} |\n")
        f.write("\n")

        f.write("## Sales Manager Distribution\n\n")
        f.write("| Sales Manager | Count |\n")
        f.write("|---------------|-------|\n")
        for manager, count in stats['sales_manager_distribution'].most_common():
            f.write(f"| {manager or '(empty)'} | {count} |\n")
        f.write("\n")

        f.write("## Sub-Entity Categorization (Preliminary)\n\n")
        f.write("| Sub-Entity Type | Count |\n")
        f.write("|-----------------|-------|\n")
        for sub_entity, count in stats['sub_entity_distribution'].most_common():
            f.write(f"| {sub_entity} | {count} |\n")
        f.write("\n")

        f.write("## Data Quality Score\n\n")
        total_fields = stats['total_records'] * 7  # 7 critical fields
        total_issues = (stats['missing_company_name'] + stats['missing_email'] +
                       stats['invalid_email'] + stats['missing_last_contact'] +
                       stats['invalid_last_contact'] + stats['missing_date'] +
                       stats['invalid_date'])
        quality_score = ((total_fields - total_issues) / total_fields * 100) if total_fields > 0 else 0
        f.write(f"**Overall Data Quality:** {quality_score:.1f}%\n\n")

        f.write("## Detailed Issues by Record\n\n")
        issues_found = False
        for result in validation_results:
            if result["issues"]:
                issues_found = True
                f.write(f"### Row {result['row']}: {result['company_name']}\n\n")
                for issue in result["issues"]:
                    f.write(f"- [WARNING] {issue}\n")
                f.write("\n")

        if not issues_found:
            f.write("[OK] No issues found in any records!\n\n")

    print(f"[OK] Validation report saved: {report_file}")
    print()

    # Export raw data to CSV for reference
    csv_file = OUTPUT_DIR / "source_data_raw.csv"
    if clients:
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=clients[0].keys())
            writer.writeheader()
            writer.writerows(clients)
        print(f"[OK] Raw data exported: {csv_file}")

    print()
    print("="*80)
    print("PHASE 1 VALIDATION COMPLETE")
    print("="*80)
    print()
    print(f"Total Records: {stats['total_records']}")
    print(f"Data Quality Score: {quality_score:.1f}%")
    print()
    print("Next Steps:")
    print("- Review validation_report.md")
    print("- Proceed to Phase 2: Entity Extraction")

if __name__ == "__main__":
    main()
