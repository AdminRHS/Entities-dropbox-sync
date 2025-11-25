"""
List all checklist items with their names, no project/milestone cross-references
"""
import json
from pathlib import Path

# Base directory
SCRIPT_DIR = Path(__file__).resolve().parent
CHECKLIST_DIR = SCRIPT_DIR / "By_Project"

def load_json(file_path):
    """Load JSON file"""
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None

def main():
    import sys
    import io
    # Force UTF-8 output
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    print("=" * 80)
    print("Checklist Items Listing")
    print("=" * 80)

    # Find all checklist JSON files
    checklist_files = sorted(CHECKLIST_DIR.rglob("CHK-*.json"))

    print(f"\nTotal checklist items: {len(checklist_files)}\n")

    # Print header
    print(f"{'ID':<45} {'Name':<70}")
    print(f"{'-' * 45} {'-' * 70}")

    # Load and display each checklist item
    all_items = []
    for file_path in checklist_files:
        data = load_json(file_path)
        if data:
            checklist_id = data.get('checklist_item_id', file_path.stem)
            item_name = data.get('item_name', 'N/A')

            # Truncate name if too long
            display_name = item_name[:68] + "..." if len(item_name) > 68 else item_name

            print(f"{checklist_id:<45} {display_name:<70}")

            all_items.append({
                "id": checklist_id,
                "name": item_name,
                "file": str(file_path.relative_to(SCRIPT_DIR))
            })

    # Save to JSON
    output = {
        "total_items": len(all_items),
        "items": all_items
    }

    output_path = SCRIPT_DIR / "checklist_items_simple_listing.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\n{'-' * 115}")
    print(f"Total: {len(all_items)} checklist items")
    print(f"Saved to: checklist_items_simple_listing.json")
    print("=" * 80)

if __name__ == "__main__":
    main()
