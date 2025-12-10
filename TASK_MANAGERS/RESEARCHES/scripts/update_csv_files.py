#!/usr/bin/env python3
"""
CSV Files Update Script
Updates Search_Queue_Master.csv and Video_Queue_Master.csv
to ensure ID stability and field compliance with ID System Standard.
"""

import csv
import re
from datetime import datetime
from pathlib import Path

# Base path (assuming script is in RESEARCHES/scripts/)
BASE_PATH = Path(__file__).parent.parent

# File paths
SEARCH_QUEUE_FILE = BASE_PATH / "00_SEARCH_QUEUE" / "Search_Queue_Master.csv"
VIDEO_QUEUE_FILE = BASE_PATH / "01_VIDEO_QUEUE" / "Video_Queue_Master.csv"

# Department code mapping
DEPARTMENT_MAPPING = {
    'AI': 'AID',  # AI Development
    'VIDEO': 'VID',
    'DESIGN': 'DGN',
    'DEV': 'DEV',
    'SMM': 'SMM',
    'HR': 'HR',
}

def backup_file(file_path: Path) -> Path:
    """Create timestamped backup of file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = file_path.parent / f"{file_path.stem}.backup.{timestamp}{file_path.suffix}"
    
    import shutil
    shutil.copy2(file_path, backup_path)
    print(f"✅ Backup created: {backup_path}")
    return backup_path

def validate_search_id(search_id: str) -> bool:
    """Validate Search Queue ID format: SEARCH-XXX"""
    pattern = r'^SEARCH-\d{3}$'
    return bool(re.match(pattern, search_id))

def validate_vq_id(queue_id: str) -> bool:
    """Validate Video Queue ID format: VQ-XXX"""
    pattern = r'^VQ-\d{3}$'
    return bool(re.match(pattern, queue_id))

def validate_video_id(video_id: str) -> bool:
    """Validate YouTube Video ID format: 11 alphanumeric characters"""
    pattern = r'^[a-zA-Z0-9_-]{11}$'
    return bool(re.match(pattern, video_id))

def validate_department(dept: str) -> bool:
    """Validate department code"""
    valid_codes = ['VID', 'AID', 'DEV', 'SMM', 'DGN', 'HR', 'SEC', 'QA', 'MKT', 'SLS', 'LGN']
    return dept.upper() in valid_codes

def update_search_queue():
    """Update Search Queue CSV file"""
    print("\n" + "=" * 60)
    print("UPDATING SEARCH QUEUE")
    print("=" * 60)
    
    if not SEARCH_QUEUE_FILE.exists():
        print(f"⚠️  File not found: {SEARCH_QUEUE_FILE}")
        return
    
    # Backup
    backup_file(SEARCH_QUEUE_FILE)
    
    # Read current file
    rows = []
    with open(SEARCH_QUEUE_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            rows.append(row)
    
    # Update records
    updates_made = []
    issues_found = []
    
    for row in rows:
        search_id = row['Search_ID']
        
        # Validate ID format
        if not validate_search_id(search_id):
            issues_found.append(f"{search_id}: Invalid ID format (should be SEARCH-XXX)")
        
        # Update Department code
        dept = row['Department']
        if dept in DEPARTMENT_MAPPING:
            new_dept = DEPARTMENT_MAPPING[dept]
            row['Department'] = new_dept
            updates_made.append(f"{search_id}: Department '{dept}' → '{new_dept}'")
        elif not validate_department(dept):
            issues_found.append(f"{search_id}: Invalid Department code '{dept}'")
        
        # Validate Status
        valid_statuses = ['Assigned', 'In_Progress', 'Completed']
        if row['Status'] not in valid_statuses:
            issues_found.append(f"{search_id}: Invalid Status '{row['Status']}'")
    
    # Write updated file
    if updates_made or issues_found:
        with open(SEARCH_QUEUE_FILE, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        
        if updates_made:
            print(f"✅ Updated {len(updates_made)} record(s):")
            for update in updates_made:
                print(f"   - {update}")
        
        if issues_found:
            print(f"\n⚠️  Found {len(issues_found)} issue(s):")
            for issue in issues_found:
                print(f"   - {issue}")
    else:
        print("✅ No updates needed - file is compliant")

def update_video_queue():
    """Update Video Queue CSV file"""
    print("\n" + "=" * 60)
    print("UPDATING VIDEO QUEUE")
    print("=" * 60)
    
    if not VIDEO_QUEUE_FILE.exists():
        print(f"⚠️  File not found: {VIDEO_QUEUE_FILE}")
        return
    
    # Backup
    backup_file(VIDEO_QUEUE_FILE)
    
    # Read current file
    rows = []
    with open(VIDEO_QUEUE_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            rows.append(row)
    
    # Update records
    updates_made = []
    issues_found = []
    placeholder_ids = []
    
    for row in rows:
        queue_id = row['Queue_ID']
        
        # Validate Queue_ID format
        if not validate_vq_id(queue_id):
            issues_found.append(f"{queue_id}: Invalid Queue_ID format (should be VQ-XXX)")
        
        # Check for placeholder Video_IDs
        video_id = row['Video_ID']
        if not validate_video_id(video_id):
            placeholder_ids.append({
                'queue_id': queue_id,
                'video_id': video_id,
                'title': row['Video_Title']
            })
            issues_found.append(f"{queue_id}: Invalid Video_ID '{video_id}' (should be 11 characters)")
        
        # Remove Channel_URL placeholder
        if row['Channel_URL'] == '[To be extracted]':
            row['Channel_URL'] = ''
            updates_made.append(f"{queue_id}: Removed Channel_URL placeholder")
        
        # Validate Status
        valid_statuses = ['Pending', 'Selected', 'Parsing', 'Parsed', 'Rejected']
        if row['Status'] not in valid_statuses:
            issues_found.append(f"{queue_id}: Invalid Status '{row['Status']}'")
        
        # Validate Priority_Score
        try:
            priority = float(row['Priority_Score'])
            if priority < 0 or priority > 100:
                issues_found.append(f"{queue_id}: Priority_Score out of range ({priority})")
        except ValueError:
            issues_found.append(f"{queue_id}: Invalid Priority_Score '{row['Priority_Score']}'")
    
    # Write updated file
    if updates_made or issues_found:
        with open(VIDEO_QUEUE_FILE, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        
        if updates_made:
            print(f"✅ Updated {len(updates_made)} record(s):")
            for update in updates_made:
                print(f"   - {update}")
        
        if issues_found:
            print(f"\n⚠️  Found {len(issues_found)} issue(s):")
            for issue in issues_found:
                print(f"   - {issue}")
        
        # Report placeholder IDs
        if placeholder_ids:
            print(f"\n❌ CRITICAL: Found {len(placeholder_ids)} placeholder Video_IDs:")
            for item in placeholder_ids:
                print(f"   - {item['queue_id']}: '{item['video_id']}'")
                print(f"     Title: {item['title']}")
            print("\n   ACTION REQUIRED: Replace placeholder IDs with real YouTube video IDs")
            print("   YouTube Video IDs are 11 characters (e.g., dQw4w9WgXcQ)")
    else:
        print("✅ No updates needed - file is compliant")

def validate_all_ids():
    """Validate all IDs for sequential numbering"""
    print("\n" + "=" * 60)
    print("VALIDATING ID SEQUENCES")
    print("=" * 60)
    
    # Check Search Queue IDs
    if SEARCH_QUEUE_FILE.exists():
        search_ids = []
        with open(SEARCH_QUEUE_FILE, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                search_id = row['Search_ID']
                if validate_search_id(search_id):
                    num = int(search_id.split('-')[1])
                    search_ids.append(num)
        
        if search_ids:
            search_ids.sort()
            print(f"\nSearch Queue IDs: {len(search_ids)} found")
            print(f"  Range: SEARCH-{search_ids[0]:03d} to SEARCH-{search_ids[-1]:03d}")
            
            # Check for gaps
            expected = list(range(1, search_ids[-1] + 1))
            gaps = [i for i in expected if i not in search_ids]
            if gaps:
                print(f"  ⚠️  Gaps found: {[f'SEARCH-{g:03d}' for g in gaps]}")
            else:
                print(f"  ✅ No gaps - sequential numbering maintained")
            
            print(f"  Next available: SEARCH-{search_ids[-1] + 1:03d}")
    
    # Check Video Queue IDs
    if VIDEO_QUEUE_FILE.exists():
        vq_ids = []
        with open(VIDEO_QUEUE_FILE, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                queue_id = row['Queue_ID']
                if validate_vq_id(queue_id):
                    num = int(queue_id.split('-')[1])
                    vq_ids.append(num)
        
        if vq_ids:
            vq_ids.sort()
            print(f"\nVideo Queue IDs: {len(vq_ids)} found")
            print(f"  Range: VQ-{vq_ids[0]:03d} to VQ-{vq_ids[-1]:03d}")
            
            # Check for gaps
            expected = list(range(1, vq_ids[-1] + 1))
            gaps = [i for i in expected if i not in vq_ids]
            if gaps:
                print(f"  ⚠️  Gaps found: {[f'VQ-{g:03d}' for g in gaps]}")
            else:
                print(f"  ✅ No gaps - sequential numbering maintained")
            
            print(f"  Next available: VQ-{vq_ids[-1] + 1:03d}")

def main():
    """Main execution"""
    print("=" * 60)
    print("CSV FILES UPDATE SCRIPT")
    print("ID System Standard Compliance Update")
    print("=" * 60)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Update Search Queue
    update_search_queue()
    
    # Update Video Queue
    update_video_queue()
    
    # Validate ID sequences
    validate_all_ids()
    
    print("\n" + "=" * 60)
    print("UPDATE PROCESS COMPLETE")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Review updated files")
    print("2. Replace placeholder Video_IDs with real YouTube IDs (if any)")
    print("3. Verify all changes are correct")
    print("4. Run validation script to verify compliance")

if __name__ == "__main__":
    main()
