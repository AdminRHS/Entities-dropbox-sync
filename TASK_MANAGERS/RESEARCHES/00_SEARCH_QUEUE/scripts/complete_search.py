"""
Mark a search task as completed and record results
"""
import csv
import sys
from datetime import datetime
from pathlib import Path

def complete_search(search_id, videos_found, notes=''):
    """Mark search as completed"""
    csv_path = Path(__file__).parent.parent / 'Search_Queue_Master.csv'

    if not csv_path.exists():
        print("❌ Error: Search queue file not found")
        sys.exit(1)

    # Read all rows
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Find and update the search
    found = False
    for row in rows:
        if row['Search_ID'] == search_id:
            row['Status'] = 'Completed'
            row['Videos_Found'] = str(videos_found)
            row['Date_Completed'] = datetime.now().strftime('%Y-%m-%d')
            if notes:
                row['Notes'] = notes
            found = True
            break

    if not found:
        print(f"❌ Error: Search ID {search_id} not found")
        sys.exit(1)

    # Write back
    fieldnames = list(rows[0].keys())
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ Search completed: {search_id}")
    print(f"   Videos found: {videos_found}")
    print(f"   Status: Completed")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python complete_search.py <search_id> <videos_found> [notes]")
        print("Example: python complete_search.py SEARCH-001 15 'Found good tutorials'")
        sys.exit(1)

    search_id = sys.argv[1]
    try:
        videos_found = int(sys.argv[2])
    except ValueError:
        print("❌ Error: videos_found must be a number")
        sys.exit(1)

    notes = sys.argv[3] if len(sys.argv) > 3 else ''

    complete_search(search_id, videos_found, notes)
