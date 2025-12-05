"""
Update video processing progress tracker
Tracks each video through all processing phases
"""
import csv
import sys
from datetime import datetime
from pathlib import Path

# Phase definitions (6-phase workflow)
PHASES = {
    'Phase_0_Queued': 'Video added to queue',
    'Phase_1_Transcribed': 'Full transcription + analysis (PMT-004)',
    'Phase_2_Extraction': 'Entity extraction & cross-referencing (PMT-007)',
    'Phase_3_Gap_Analysis': 'Library comparison & gap identification (PMT-009 Part 1)',
    'Phase_4_Integration': 'JSON creation & taxonomy integration (PMT-009 Part 2)',
    'Phase_5_Mapping': 'Final mapping & documentation (PMT-009 Part 3)',
    'Complete': 'All phases completed'
}

def get_progress_file():
    """Get path to progress tracker CSV"""
    base_path = Path(__file__).parent.parent
    return base_path / 'VIDEO_PROGRESS_TRACKER.csv'

def initialize_tracker():
    """Initialize progress tracker CSV if it doesn't exist"""
    progress_file = get_progress_file()

    if not progress_file.exists():
        headers = [
            'Video_ID',
            'Video_Number',
            'Title',
            'YouTube_URL',
            'Current_Phase',
            'Phase_0_Queued',
            'Phase_1_Transcribed',
            'Phase_2_Extraction',
            'Phase_3_Gap_Analysis',
            'Phase_4_Integration',
            'Phase_5_Mapping',
            'Status',
            'Employee',
            'Date_Started',
            'Date_Completed',
            'Total_Days',
            'Notes'
        ]

        with open(progress_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(headers)

        print(f"✅ Created progress tracker: {progress_file}")

def add_video_to_tracker(video_number, title, youtube_url, employee):
    """Add a new video to progress tracker"""
    initialize_tracker()
    progress_file = get_progress_file()

    video_id = f"VID-{str(video_number).zfill(3)}"

    # Read existing
    rows = []
    if progress_file.exists():
        with open(progress_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

    # Check if already exists
    for row in rows:
        if row['Video_Number'] == str(video_number):
            print(f"⚠️  Video {video_number} already exists in tracker")
            return

    # Add new video
    new_row = {
        'Video_ID': video_id,
        'Video_Number': str(video_number),
        'Title': title,
        'YouTube_URL': youtube_url,
        'Current_Phase': 'Phase_0_Queued',
        'Phase_0_Queued': datetime.now().strftime('%Y-%m-%d'),
        'Phase_1_Transcribed': '',
        'Phase_2_Extraction': '',
        'Phase_3_Gap_Analysis': '',
        'Phase_4_Integration': '',
        'Phase_5_Mapping': '',
        'Status': 'In Progress',
        'Employee': employee,
        'Date_Started': datetime.now().strftime('%Y-%m-%d'),
        'Date_Completed': '',
        'Total_Days': '',
        'Notes': ''
    }

    rows.append(new_row)

    # Write back
    if rows:
        fieldnames = list(rows[0].keys())
        with open(progress_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    print(f"✅ Added Video {video_number} to progress tracker")
    print(f"   ID: {video_id}")
    print(f"   Title: {title}")
    print(f"   Status: Phase 0 - Queued")

def update_phase(video_number, phase_name, notes=''):
    """Update video to a new phase"""
    initialize_tracker()
    progress_file = get_progress_file()

    if not progress_file.exists():
        print("❌ Error: Progress tracker not found")
        sys.exit(1)

    # Validate phase
    if phase_name not in PHASES:
        print(f"❌ Error: Invalid phase '{phase_name}'")
        print(f"Valid phases: {', '.join(PHASES.keys())}")
        sys.exit(1)

    # Read all rows
    with open(progress_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Find and update video
    found = False
    for row in rows:
        if row['Video_Number'] == str(video_number):
            # Update phase timestamp
            row[phase_name] = datetime.now().strftime('%Y-%m-%d')
            row['Current_Phase'] = phase_name

            # Update notes if provided
            if notes:
                if row['Notes']:
                    row['Notes'] += f" | {notes}"
                else:
                    row['Notes'] = notes

            # Mark as complete if final phase
            if phase_name == 'Complete':
                row['Status'] = 'Complete'
                row['Date_Completed'] = datetime.now().strftime('%Y-%m-%d')

                # Calculate total days
                if row['Date_Started']:
                    start = datetime.strptime(row['Date_Started'], '%Y-%m-%d')
                    end = datetime.now()
                    row['Total_Days'] = str((end - start).days)

            found = True
            break

    if not found:
        print(f"❌ Error: Video {video_number} not found in tracker")
        sys.exit(1)

    # Write back
    fieldnames = list(rows[0].keys())
    with open(progress_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ Updated Video {video_number}")
    print(f"   Phase: {phase_name}")
    print(f"   Description: {PHASES[phase_name]}")
    if notes:
        print(f"   Notes: {notes}")

def view_progress(video_number=None):
    """View progress for a specific video or all videos"""
    initialize_tracker()
    progress_file = get_progress_file()

    if not progress_file.exists():
        print("❌ No progress data found")
        return

    with open(progress_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if video_number:
        # Show specific video
        for row in rows:
            if row['Video_Number'] == str(video_number):
                print(f"\n{'='*60}")
                print(f"Video {video_number}: {row['Title']}")
                print(f"{'='*60}")
                print(f"Status: {row['Status']}")
                print(f"Current Phase: {row['Current_Phase']}")
                print(f"Employee: {row['Employee']}")
                print(f"Started: {row['Date_Started']}")
                if row['Date_Completed']:
                    print(f"Completed: {row['Date_Completed']}")
                    print(f"Total Days: {row['Total_Days']}")

                print(f"\nPhase Completion:")
                for phase, desc in PHASES.items():
                    if phase == 'Complete':
                        continue
                    date = row.get(phase, '')
                    status = '✅' if date else '⏳'
                    print(f"  {status} {desc}: {date if date else 'Pending'}")

                if row['Notes']:
                    print(f"\nNotes: {row['Notes']}")
                print(f"{'='*60}\n")
                return

        print(f"❌ Video {video_number} not found")
    else:
        # Show all videos summary
        print(f"\n{'='*80}")
        print(f"VIDEO PROGRESS TRACKER - SUMMARY")
        print(f"{'='*80}")
        print(f"{'Video':<10} {'Title':<30} {'Current Phase':<20} {'Status':<15}")
        print(f"{'-'*80}")

        for row in rows:
            video_num = row['Video_Number']
            title = row['Title'][:28] + '..' if len(row['Title']) > 30 else row['Title']
            phase = row['Current_Phase'].replace('Phase_', 'P').replace('_', ' ')
            status = row['Status']

            print(f"{video_num:<10} {title:<30} {phase:<20} {status:<15}")

        print(f"{'-'*80}")
        print(f"Total Videos: {len(rows)}")
        completed = sum(1 for r in rows if r['Status'] == 'Complete')
        print(f"Completed: {completed}")
        print(f"In Progress: {len(rows) - completed}")
        print(f"{'='*80}\n")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Video Progress Tracker")
        print("\nUsage:")
        print("  Add video:    python update_video_progress.py add <video_number> <title> <youtube_url> <employee>")
        print("  Update phase: python update_video_progress.py update <video_number> <phase_name> [notes]")
        print("  View progress: python update_video_progress.py view [video_number]")
        print("\nPhases:")
        for phase, desc in PHASES.items():
            print(f"  - {phase}: {desc}")
        print("\nExamples:")
        print('  python update_video_progress.py add 22 "Claude AI Tutorial" "https://youtube.com/..." "John"')
        print('  python update_video_progress.py update 22 Phase_1_Transcribed "Used PMT-004"')
        print('  python update_video_progress.py view 22')
        print('  python update_video_progress.py view')
        sys.exit(1)

    command = sys.argv[1]

    if command == 'add':
        if len(sys.argv) < 6:
            print("❌ Error: Missing arguments")
            print("Usage: python update_video_progress.py add <video_number> <title> <youtube_url> <employee>")
            sys.exit(1)

        video_number = sys.argv[2]
        title = sys.argv[3]
        youtube_url = sys.argv[4]
        employee = sys.argv[5]

        add_video_to_tracker(video_number, title, youtube_url, employee)

    elif command == 'update':
        if len(sys.argv) < 4:
            print("❌ Error: Missing arguments")
            print("Usage: python update_video_progress.py update <video_number> <phase_name> [notes]")
            sys.exit(1)

        video_number = sys.argv[2]
        phase_name = sys.argv[3]
        notes = sys.argv[4] if len(sys.argv) > 4 else ''

        update_phase(video_number, phase_name, notes)

    elif command == 'view':
        video_number = sys.argv[2] if len(sys.argv) > 2 else None
        view_progress(video_number)

    else:
        print(f"❌ Error: Unknown command '{command}'")
        print("Valid commands: add, update, view")
        sys.exit(1)
