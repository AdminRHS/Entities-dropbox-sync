import json
import re
from pathlib import Path
from datetime import datetime
from collections import Counter

# Configuration
ENTITIES_FILE = Path(r"C:\Users\Dell\Dropbox\ENTITIES\IMPORTS\2025-11-21_Sales_Nov25\entities_extracted.json")
CLIENTS_DIR = Path(r"C:\Users\Dell\Dropbox\Nov25\Sales Nov25\Clients")
OUTPUT_DIR = Path(r"C:\Users\Dell\Dropbox\ENTITIES\IMPORTS\2025-11-21_Sales_Nov25")

def load_entities():
    """Load entities from JSON file"""
    with open(ENTITIES_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def find_transcript_files():
    """Find all transcript markdown files"""
    transcripts = []

    if CLIENTS_DIR.exists():
        for md_file in CLIENTS_DIR.rglob("*.md"):
            if md_file.name.lower() != "readme.md":
                transcripts.append(md_file)

    return transcripts

def match_company_to_transcript(company_name, transcript_path):
    """Try to match company name to transcript file"""
    company_lower = company_name.lower()
    path_lower = str(transcript_path).lower()

    # Clean company name for matching
    company_clean = re.sub(r'[^\w\s]', '', company_lower).strip()
    words = company_clean.split()

    # Check if any significant word from company name is in the path
    for word in words:
        if len(word) > 3:  # Only significant words
            if word in path_lower:
                return True

    return False

def extract_transcript_info(transcript_path):
    """Extract useful information from transcript"""
    info = {
        "file_path": str(transcript_path),
        "summary": "",
        "services_discussed": [],
        "budget_mentioned": False,
        "next_steps": [],
        "attendees": [],
        "meeting_date": None,
        "key_insights": []
    }

    try:
        with open(transcript_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract meeting date from filename
        date_match = re.search(r'(\d{4})[_\-](\d{2})[_\-](\d{2})', transcript_path.name)
        if date_match:
            info["meeting_date"] = f"{date_match.group(1)}-{date_match.group(2)}-{date_match.group(3)}"

        # Extract summary section
        summary_match = re.search(r'(?:summary|overview)[\s\S]{0,50}?[:\n]([\s\S]{100,500}?)(?:\n#{1,3}|\nNext steps|\Z)', content, re.IGNORECASE)
        if summary_match:
            info["summary"] = summary_match.group(1).strip()[:300]  # First 300 chars

        # Look for service keywords
        service_keywords = {
            "lead generation": ["lead gen", "lead generation", "leadgen", "prospecting"],
            "design": ["design", "ui/ux", "graphic design", "branding"],
            "development": ["development", "developer", "coding", "programming", "web dev"],
            "content writing": ["content", "writing", "copywriting", "blog"],
            "social media": ["social media", "smm", "social marketing", "instagram", "linkedin"],
            "AI/automation": ["ai", "automation", "chatbot", "machine learning"],
            "virtual assistant": ["virtual assistant", "va", "admin support"],
        }

        content_lower = content.lower()
        for service, keywords in service_keywords.items():
            if any(keyword in content_lower for keyword in keywords):
                info["services_discussed"].append(service)

        # Check for budget mentions
        if re.search(r'\$\d{1,3}(?:,?\d{3})*(?:\.\d{2})?|\d+\s*(?:per|/)\s*(?:hour|month|week)', content_lower):
            info["budget_mentioned"] = True

        # Extract next steps
        next_steps_match = re.search(r'next steps?[\s\S]{0,50}?[:\n]([\s\S]{50,300}?)(?:\n#{1,3}|\Z)', content, re.IGNORECASE)
        if next_steps_match:
            steps_text = next_steps_match.group(1)
            # Find bullet points or numbered lists
            steps = re.findall(r'[-*•]\s*([^\n]+)', steps_text)
            if not steps:
                steps = re.findall(r'\d+\.\s*([^\n]+)', steps_text)
            info["next_steps"] = steps[:5]  # Max 5 steps

        # Extract attendees
        attendees_match = re.search(r'(?:attendees?|participants?)[\s\S]{0,50}?[:\n]([\s\S]{20,200}?)(?:\n#{1,3}|\n\n)', content, re.IGNORECASE)
        if attendees_match:
            attendees_text = attendees_match.group(1)
            attendees = re.findall(r'[-*•]?\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)', attendees_text)
            info["attendees"] = attendees[:5]

        # Extract key insights (look for decision-maker roles, company size hints, etc.)
        if re.search(r'\b(?:ceo|cto|cfo|founder|director|manager|head of)\b', content_lower):
            info["key_insights"].append("Senior decision maker involved")

        if re.search(r'\b(?:\d+\s*employees?|\d+[\s-]person team|\d+\s*staff)\b', content_lower):
            size_match = re.search(r'\b(\d+)\s*(?:employees?|person team|staff)\b', content_lower)
            if size_match:
                info["key_insights"].append(f"Company size: ~{size_match.group(1)} employees")

        if re.search(r'\b(?:urgent|asap|as soon as possible|immediately)\b', content_lower):
            info["key_insights"].append("Urgent need identified")

    except Exception as e:
        print(f"  [WARNING] Error processing {transcript_path.name}: {e}")

    return info

def enrich_entity(entity, transcripts):
    """Enrich entity with transcript data"""
    enrichment = {
        "enriched": False,
        "transcript_info": None,
        "new_tags": [],
        "updated_fields": []
    }

    # Try to match this entity to a transcript
    for transcript_path in transcripts:
        if match_company_to_transcript(entity['company_name'], transcript_path):
            print(f"  [MATCH] {entity['company_id']}: {entity['company_name']} -> {transcript_path.name}")

            transcript_info = extract_transcript_info(transcript_path)
            enrichment["transcript_info"] = transcript_info
            enrichment["enriched"] = True

            # Update communication history
            if transcript_info["meeting_date"] or transcript_info["summary"]:
                comm_entry = {
                    "date": transcript_info["meeting_date"] or "Unknown",
                    "type": "call_transcript",
                    "summary": transcript_info["summary"][:200] if transcript_info["summary"] else "Call transcript available",
                    "file_path": transcript_info["file_path"]
                }
                entity['communication_history'].append(comm_entry)
                enrichment["updated_fields"].append("communication_history")

            # Add service tags
            for service in transcript_info["services_discussed"]:
                tag = service.lower().replace(" ", "_").replace("/", "_")
                if tag not in entity['tags']:
                    entity['tags'].append(tag)
                    enrichment["new_tags"].append(tag)

            # Update industry if unknown and we can infer from services
            if entity['industry'] == "Unknown" and transcript_info["services_discussed"]:
                if "development" in transcript_info["services_discussed"]:
                    entity['industry'] = "Technology"
                    enrichment["updated_fields"].append("industry")
                elif "lead generation" in transcript_info["services_discussed"]:
                    entity['industry'] = "Marketing"
                    enrichment["updated_fields"].append("industry")

            # Add insights to notes
            if transcript_info["key_insights"]:
                insights_text = " | ".join(transcript_info["key_insights"])
                if entity['notes']:
                    entity['notes'] += f" | Insights: {insights_text}"
                else:
                    entity['notes'] = f"Insights: {insights_text}"
                enrichment["updated_fields"].append("notes")

            # Update decision makers if we found attendees
            if transcript_info["attendees"] and len(entity['decision_makers']) == 1:
                # Add additional decision makers
                for attendee in transcript_info["attendees"]:
                    if attendee not in [dm['name'] for dm in entity['decision_makers']]:
                        entity['decision_makers'].append({
                            "name": attendee,
                            "title": "Unknown",
                            "email": ""
                        })
                if len(entity['decision_makers']) > 1:
                    enrichment["updated_fields"].append("decision_makers")

            # Add budget tag if mentioned
            if transcript_info["budget_mentioned"] and "budget_discussed" not in entity['tags']:
                entity['tags'].append("budget_discussed")
                enrichment["new_tags"].append("budget_discussed")

            break  # Only use first matching transcript

    return enrichment

def main():
    print("="*80)
    print("PHASE 3: DATA ENRICHMENT")
    print("="*80)
    print()

    # Load entities
    print(f"Loading entities from: {ENTITIES_FILE}")
    entities = load_entities()
    print(f"[OK] Loaded {len(entities)} entities")
    print()

    # Find transcripts
    print(f"Searching for transcripts in: {CLIENTS_DIR}")
    transcripts = find_transcript_files()
    print(f"[OK] Found {len(transcripts)} transcript files")
    print()

    # Enrich entities
    print("Matching entities to transcripts and enriching data...")
    print()

    enrichment_stats = {
        "total_entities": len(entities),
        "enriched_count": 0,
        "new_tags_added": 0,
        "fields_updated": Counter(),
        "services_found": Counter(),
    }

    enrichment_log = []

    for entity in entities:
        enrichment = enrich_entity(entity, transcripts)

        if enrichment["enriched"]:
            enrichment_stats["enriched_count"] += 1
            enrichment_stats["new_tags_added"] += len(enrichment["new_tags"])

            for field in enrichment["updated_fields"]:
                enrichment_stats["fields_updated"][field] += 1

            if enrichment["transcript_info"]:
                for service in enrichment["transcript_info"]["services_discussed"]:
                    enrichment_stats["services_found"][service] += 1

            enrichment_log.append({
                "company_id": entity['company_id'],
                "company_name": entity['company_name'],
                "new_tags": enrichment["new_tags"],
                "updated_fields": enrichment["updated_fields"],
                "services": enrichment["transcript_info"]["services_discussed"] if enrichment["transcript_info"] else []
            })

    print()
    print(f"[OK] Enriched {enrichment_stats['enriched_count']} entities")
    print(f"[OK] Added {enrichment_stats['new_tags_added']} new tags")
    print()

    # Save enriched entities
    enriched_file = OUTPUT_DIR / "entities_enriched.json"
    with open(enriched_file, 'w', encoding='utf-8') as f:
        json.dump(entities, f, indent=2, ensure_ascii=False)
    print(f"[OK] Enriched entities saved: {enriched_file}")
    print()

    # Generate enrichment report
    report_file = OUTPUT_DIR / "enrichment_report.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# Phase 3: Data Enrichment Report\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("---\n\n")

        f.write("## Summary\n\n")
        f.write(f"- **Total Entities:** {enrichment_stats['total_entities']}\n")
        f.write(f"- **Entities Enriched:** {enrichment_stats['enriched_count']}\n")
        f.write(f"- **Enrichment Rate:** {(enrichment_stats['enriched_count']/enrichment_stats['total_entities']*100):.1f}%\n")
        f.write(f"- **New Tags Added:** {enrichment_stats['new_tags_added']}\n")
        f.write(f"- **Transcript Files Found:** {len(transcripts)}\n\n")

        f.write("## Fields Updated\n\n")
        if enrichment_stats['fields_updated']:
            f.write("| Field | Count |\n")
            f.write("|-------|-------|\n")
            for field, count in enrichment_stats['fields_updated'].most_common():
                f.write(f"| {field} | {count} |\n")
            f.write("\n")
        else:
            f.write("No fields were updated during enrichment.\n\n")

        f.write("## Services Identified\n\n")
        if enrichment_stats['services_found']:
            f.write("| Service | Count |\n")
            f.write("|---------|-------|\n")
            for service, count in enrichment_stats['services_found'].most_common():
                f.write(f"| {service} | {count} |\n")
            f.write("\n")
        else:
            f.write("No services were identified from transcripts.\n\n")

        f.write("## Enrichment Details\n\n")
        if enrichment_log:
            for log in enrichment_log:
                f.write(f"### {log['company_id']}: {log['company_name']}\n\n")
                if log['new_tags']:
                    f.write(f"**New Tags:** {', '.join(log['new_tags'])}\n\n")
                if log['updated_fields']:
                    f.write(f"**Updated Fields:** {', '.join(log['updated_fields'])}\n\n")
                if log['services']:
                    f.write(f"**Services Discussed:** {', '.join(log['services'])}\n\n")
                f.write("\n")
        else:
            f.write("No entities were enriched with transcript data.\n\n")

        f.write("## Entities Without Transcript Data\n\n")
        unenriched = [e for e in entities if not any(
            log['company_id'] == e['company_id'] for log in enrichment_log
        )]
        if unenriched:
            f.write(f"**Count:** {len(unenriched)}\n\n")
            f.write("| Company ID | Company Name | Sub-Entity |\n")
            f.write("|------------|--------------|------------|\n")
            for entity in unenriched[:20]:  # Show first 20
                f.write(f"| {entity['company_id']} | {entity['company_name']} | {entity['sub_entity']} |\n")
            if len(unenriched) > 20:
                f.write(f"\n*... and {len(unenriched) - 20} more*\n")
            f.write("\n")
        else:
            f.write("All entities have been enriched!\n\n")

        f.write("## Recommendations\n\n")
        f.write("1. **Manual Review:** Review entities without transcript data for additional enrichment opportunities\n")
        f.write("2. **Industry Classification:** Update 'Unknown' industries based on available information\n")
        f.write("3. **Company Size:** Add company size information from call notes or research\n")
        f.write("4. **Location Data:** Add geographic location information where available\n")
        f.write("5. **Revenue Estimates:** Add lifetime value and revenue estimates for clients\n\n")

    print(f"[OK] Enrichment report saved: {report_file}")
    print()

    print("="*80)
    print("PHASE 3 COMPLETE")
    print("="*80)
    print()
    print(f"Enrichment Rate: {(enrichment_stats['enriched_count']/enrichment_stats['total_entities']*100):.1f}%")
    print(f"Entities Enriched: {enrichment_stats['enriched_count']} / {enrichment_stats['total_entities']}")
    print()
    print("Next Steps:")
    print("- Review enrichment_report.md")
    print("- Review entities_enriched.json")
    print("- Proceed to Phase 4: JSON File Generation")

if __name__ == "__main__":
    main()
