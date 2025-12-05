"""
Assign a new video search task to an employee
"""
import csv
import sys
from datetime import datetime
from pathlib import Path

def generate_search_id():
    """Generate next available SEARCH-XXX ID"""
    csv_path = Path(__file__).parent.parent / 'Search_Queue_Master.csv'

    if not csv_path.exists():
        return 'SEARCH-001'

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        return 'SEARCH-001'

    # Get max ID
    max_num = 0
    for row in rows:
        search_id = row.get('Search_ID', '')
        if search_id.startswith('SEARCH-'):
            try:
                num = int(search_id.split('-')[1])
                max_num = max(max_num, num)
            except:
                pass

    return f'SEARCH-{str(max_num + 1).zfill(3)}'

def assign_search(employee, department, topic, search_query='', notes=''):
    """Assign a new search task"""
    csv_path = Path(__file__).parent.parent / 'Search_Queue_Master.csv'

    search_id = generate_search_id()

    new_row = {
        'Search_ID': search_id,
        'Employee': employee,
        'Department': department,
        'Topic': topic,
        'Search_Query': search_query,
        'Status': 'Assigned',
        'Videos_Found': '0',
        'Date_Assigned': datetime.now().strftime('%Y-%m-%d'),
        'Date_Completed': '',
        'Notes': notes
    }

    # Read existing
    rows = []
    if csv_path.exists():
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

    # Add new row
    rows.append(new_row)

    # Write back
    fieldnames = ['Search_ID', 'Employee', 'Department', 'Topic', 'Search_Query',
                  'Status', 'Videos_Found', 'Date_Assigned', 'Date_Completed', 'Notes']

    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ Search task assigned: {search_id}")
    print(f"   Employee: {employee}")
    print(f"   Department: {department}")
    print(f"   Topic: {topic}")

    return search_id

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python assign_search.py <employee> <department> <topic> [search_query] [notes]")
        print("Example: python assign_search.py 'John Doe' 'AI' 'Claude AI tutorials' 'Claude tutorial' 'Focus on recent videos'")
        sys.exit(1)

    employee = sys.argv[1]
    department = sys.argv[2]
    topic = sys.argv[3]
    search_query = sys.argv[4] if len(sys.argv) > 4 else ''
    notes = sys.argv[5] if len(sys.argv) > 5 else ''

    assign_search(employee, department, topic, search_query, notes)
