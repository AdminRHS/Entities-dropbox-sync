"""
Update Queue Status Script
Updates the status of videos in the queue
"""

import pandas as pd
from datetime import datetime
import os
import sys


def get_queue_file_path():
    """Get the path to Video_Queue_Master.csv"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    queue_dir = os.path.dirname(script_dir)
    return os.path.join(queue_dir, 'Video_Queue_Master.csv')


def load_queue():
    """Load the video queue CSV file"""
    queue_path = get_queue_file_path()
    if not os.path.exists(queue_path):
        raise FileNotFoundError(f"Queue file not found: {queue_path}")
    return pd.read_csv(queue_path)


def save_queue(df):
    """Save the video queue CSV file"""
    queue_path = get_queue_file_path()
    df.to_csv(queue_path, index=False)


def update_status(queue_id, new_status, selected_by=None):
    """
    Update the status of a video in the queue.

    Args:
        queue_id (str): Queue ID (e.g., "VQ-001")
        new_status (str): New status (Pending, Selected, Parsing, Parsed, Rejected)
        selected_by (str): Employee name (required for Selected status)

    Returns:
        bool: True if successful, False otherwise
    """

    valid_statuses = ['Pending', 'Selected', 'Parsing', 'Parsed', 'Rejected']
    if new_status not in valid_statuses:
        raise ValueError(f"Invalid status. Must be one of: {', '.join(valid_statuses)}")

    # Load queue
    queue_df = load_queue()

    # Find video by Queue_ID
    if queue_id not in queue_df['Queue_ID'].values:
        print(f"❌ Queue ID not found: {queue_id}")
        return False

    # Get index of the row
    idx = queue_df[queue_df['Queue_ID'] == queue_id].index[0]

    # Update status
    queue_df.at[idx, 'Status'] = new_status

    # Update date fields based on status
    today = datetime.now().strftime('%Y-%m-%d')

    if new_status == 'Selected':
        if selected_by:
            queue_df.at[idx, 'Selected_By'] = selected_by
        queue_df.at[idx, 'Selected_Date'] = today

    elif new_status == 'Parsed':
        queue_df.at[idx, 'Parsed_Date'] = today

    # Save queue
    save_queue(queue_df)

    video_title = queue_df.at[idx, 'Video_Title']
    print(f"✅ Updated {queue_id} ({video_title}) to status: {new_status}")

    return True


def update_multiple_status(queue_ids, new_status, selected_by=None):
    """
    Update the status of multiple videos at once.

    Args:
        queue_ids (list): List of Queue IDs
        new_status (str): New status
        selected_by (str): Employee name (required for Selected status)

    Returns:
        dict: Summary of updates
    """

    results = {
        'successful': [],
        'failed': []
    }

    for queue_id in queue_ids:
        try:
            success = update_status(queue_id, new_status, selected_by)
            if success:
                results['successful'].append(queue_id)
            else:
                results['failed'].append(queue_id)
        except Exception as e:
            print(f"Error updating {queue_id}: {str(e)}")
            results['failed'].append(queue_id)

    print(f"\n✅ Successfully updated: {len(results['successful'])} videos")
    if results['failed']:
        print(f"❌ Failed to update: {len(results['failed'])} videos")

    return results


def show_queue_summary():
    """Show summary of queue by status"""
    queue_df = load_queue()

    if queue_df.empty:
        print("Queue is empty.")
        return

    print("\n" + "=" * 60)
    print("VIDEO QUEUE SUMMARY")
    print("=" * 60)

    total = len(queue_df)
    print(f"\nTotal videos in queue: {total}")

    # Status breakdown
    status_counts = queue_df['Status'].value_counts()
    print("\nStatus Breakdown:")
    for status, count in status_counts.items():
        percentage = (count / total) * 100
        print(f"  {status:12s}: {count:3d} ({percentage:5.1f}%)")

    # Topic breakdown
    if 'Topic_Category' in queue_df.columns:
        print("\nTop Topics:")
        topic_counts = queue_df['Topic_Category'].value_counts().head(5)
        for topic, count in topic_counts.items():
            print(f"  {topic:30s}: {count:3d}")

    # Source breakdown
    if 'Research_Source' in queue_df.columns:
        print("\nResearch Sources:")
        source_counts = queue_df['Research_Source'].value_counts()
        for source, count in source_counts.items():
            print(f"  {source:12s}: {count:3d}")

    print("\n" + "=" * 60)


def list_by_status(status):
    """List all videos with a specific status"""
    queue_df = load_queue()

    if queue_df.empty:
        print("Queue is empty.")
        return

    filtered = queue_df[queue_df['Status'] == status]

    if filtered.empty:
        print(f"No videos with status: {status}")
        return

    print(f"\n{'='*80}")
    print(f"VIDEOS WITH STATUS: {status}")
    print(f"{'='*80}\n")

    for _, row in filtered.iterrows():
        print(f"Queue ID: {row['Queue_ID']}")
        print(f"Title: {row['Video_Title']}")
        print(f"Topic: {row['Topic_Category']}")
        print(f"Priority: {row['Priority_Score']}/100")
        print(f"Added by: {row['Added_By']} on {row['Added_Date']}")
        if row['Selected_By']:
            print(f"Selected by: {row['Selected_By']} on {row['Selected_Date']}")
        print("-" * 80)


# CLI interface
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("=" * 60)
        print("Update Queue Status - Command Line Interface")
        print("=" * 60)
        print("\nUsage:")
        print("  python update_queue_status.py <command> [arguments]")
        print("\nCommands:")
        print("  update <queue_id> <status> [selected_by]")
        print("      Update a single video's status")
        print("      Valid statuses: Pending, Selected, Parsing, Parsed, Rejected")
        print("\n  summary")
        print("      Show queue summary by status")
        print("\n  list <status>")
        print("      List all videos with specific status")
        print("\nExamples:")
        print("  python update_queue_status.py update VQ-001 Selected 'Niko Kar'")
        print("  python update_queue_status.py update VQ-002 Parsed")
        print("  python update_queue_status.py summary")
        print("  python update_queue_status.py list Pending")
        print("\n" + "=" * 60)
        sys.exit(1)

    command = sys.argv[1].lower()

    try:
        if command == 'update':
            if len(sys.argv) < 4:
                print("❌ Error: update command requires <queue_id> <status> [selected_by]")
                sys.exit(1)

            queue_id = sys.argv[2]
            status = sys.argv[3]
            selected_by = sys.argv[4] if len(sys.argv) > 4 else None

            update_status(queue_id, status, selected_by)

        elif command == 'summary':
            show_queue_summary()

        elif command == 'list':
            if len(sys.argv) < 3:
                print("❌ Error: list command requires <status>")
                sys.exit(1)

            status = sys.argv[2]
            list_by_status(status)

        else:
            print(f"❌ Unknown command: {command}")
            print("Valid commands: update, summary, list")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)
