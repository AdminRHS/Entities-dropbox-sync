"""
Add Video to Queue Script (Simple CSV Version - No Pandas Required)
Adds a video to the Video_Queue_Master.csv with metadata extraction
"""

import csv
from datetime import datetime
import re
import os
import sys

# Add parent directory to path to import calculate_priority
sys.path.insert(0, os.path.dirname(__file__))
from calculate_priority import calculate_priority_score


def extract_video_id(url):
    """
    Extract YouTube video ID from URL.

    Supported URL formats:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    - https://www.youtube.com/embed/VIDEO_ID
    - https://m.youtube.com/watch?v=VIDEO_ID

    Args:
        url (str): YouTube video URL

    Returns:
        str: Video ID (11 characters) or None if not found
    """
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([a-zA-Z0-9_-]{11})',
        r'v=([a-zA-Z0-9_-]{11})'
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return None


def get_queue_file_path():
    """Get the path to Video_Queue_Master.csv"""
    # Get script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to TSM-008_Video_Queue
    queue_dir = os.path.dirname(script_dir)
    # Path to CSV file
    return os.path.join(queue_dir, 'Video_Queue_Master.csv')


def load_queue():
    """Load the video queue CSV file"""
    queue_path = get_queue_file_path()

    if not os.path.exists(queue_path):
        # Create empty queue with headers
        headers = [
            'Queue_ID', 'Video_ID', 'Video_Title', 'Channel_Name', 'Channel_URL',
            'Video_URL', 'Views', 'Likes', 'Comments', 'Publish_Date', 'Duration',
            'Added_By', 'Added_Date', 'Status', 'Selected_By', 'Selected_Date',
            'Parsed_Date', 'Topic_Category', 'Research_Source', 'Priority_Score', 'Notes'
        ]
        with open(queue_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
        return []

    # Read existing queue
    with open(queue_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


def save_queue(queue_data):
    """Save the video queue CSV file"""
    queue_path = get_queue_file_path()

    if not queue_data:
        # Write empty file with headers only
        headers = [
            'Queue_ID', 'Video_ID', 'Video_Title', 'Channel_Name', 'Channel_URL',
            'Video_URL', 'Views', 'Likes', 'Comments', 'Publish_Date', 'Duration',
            'Added_By', 'Added_Date', 'Status', 'Selected_By', 'Selected_Date',
            'Parsed_Date', 'Topic_Category', 'Research_Source', 'Priority_Score', 'Notes'
        ]
        with open(queue_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
        return

    # Get fieldnames from first row
    fieldnames = list(queue_data[0].keys())

    with open(queue_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(queue_data)


def generate_queue_id(queue_data):
    """
    Generate next Queue_ID in format VQ-001, VQ-002, etc.

    Args:
        queue_data (list): Current queue data

    Returns:
        str: Next Queue_ID
    """
    if not queue_data:
        return 'VQ-001'

    # Get all IDs and find max
    ids = [row['Queue_ID'] for row in queue_data if row.get('Queue_ID', '').startswith('VQ-')]

    if not ids:
        return 'VQ-001'

    # Extract numbers and find max
    numbers = []
    for queue_id in ids:
        try:
            num = int(queue_id.split('-')[1])
            numbers.append(num)
        except (IndexError, ValueError):
            continue

    if not numbers:
        return 'VQ-001'

    next_num = max(numbers) + 1
    return f'VQ-{next_num:03d}'


def add_video(video_url, added_by, topic_category, research_source, notes="",
              video_title=None, channel_name=None, views=0, likes=0, comments=0,
              publish_date=None, duration="00:00:00"):
    """
    Add video to queue with metadata extraction.

    Args:
        video_url (str): YouTube video URL
        added_by (str): Employee name who added the video
        topic_category (str): Research topic (e.g., "Design Research", "Video Editing")
        research_source (str): Tool used (Perplexity, Gemini, GPT, DeepSeek, YouTube)
        notes (str): Optional notes about the video
        video_title (str): Video title (if known, otherwise "[To be extracted]")
        channel_name (str): Channel name (if known, otherwise "[To be extracted]")
        views (int): View count (default 0)
        likes (int): Like count (default 0)
        comments (int): Comment count (default 0)
        publish_date (str): Publication date YYYY-MM-DD (default today)
        duration (str): Video duration HH:MM:SS (default "00:00:00")

    Returns:
        str: Queue ID assigned to the video
    """

    # Extract video ID
    video_id = extract_video_id(video_url)
    if not video_id:
        raise ValueError(f"Could not extract video ID from URL: {video_url}")

    # Load queue
    queue_data = load_queue()

    # Check if video already in queue
    for row in queue_data:
        if row.get('Video_ID') == video_id:
            existing_queue_id = row.get('Queue_ID')
            print(f"⚠️  Video already in queue: {existing_queue_id}")
            return existing_queue_id

    # Generate Queue ID
    queue_id = generate_queue_id(queue_data)

    # Calculate priority score
    priority_metadata = {
        'views': views,
        'likes': likes,
        'publish_date': publish_date if publish_date else datetime.now().strftime('%Y-%m-%d')
    }
    priority_score = calculate_priority_score(priority_metadata)

    # Create metadata dictionary
    metadata = {
        'Queue_ID': queue_id,
        'Video_ID': video_id,
        'Video_Title': video_title if video_title else '[To be extracted]',
        'Channel_Name': channel_name if channel_name else '[To be extracted]',
        'Channel_URL': '[To be extracted]',
        'Video_URL': video_url,
        'Views': str(views),
        'Likes': str(likes),
        'Comments': str(comments),
        'Publish_Date': publish_date if publish_date else datetime.now().strftime('%Y-%m-%d'),
        'Duration': duration,
        'Added_By': added_by,
        'Added_Date': datetime.now().strftime('%Y-%m-%d'),
        'Status': 'Pending',
        'Selected_By': '',
        'Selected_Date': '',
        'Parsed_Date': '',
        'Topic_Category': topic_category,
        'Research_Source': research_source,
        'Priority_Score': str(priority_score),
        'Notes': notes
    }

    # Add to queue
    queue_data.append(metadata)

    # Save queue
    save_queue(queue_data)

    print(f"✅ Video added to queue: {queue_id}")
    print(f"   Video ID: {video_id}")
    print(f"   Title: {metadata['Video_Title']}")
    print(f"   Topic: {topic_category}")
    print(f"   Priority Score: {priority_score}/100")
    print(f"   Queue size: {len(queue_data)} videos")

    return queue_id


# CLI interface
if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("=" * 60)
        print("Add Video to Queue - Command Line Interface")
        print("=" * 60)
        print("\nUsage:")
        print("  python add_video_to_queue_simple.py <video_url> <added_by> <topic> <source> [notes]")
        print("\nRequired Arguments:")
        print("  video_url    YouTube video URL")
        print("  added_by     Employee name (e.g., 'Niko Kar')")
        print("  topic        Research topic (e.g., 'Design Research', 'Video Editing')")
        print("  source       Research tool (Perplexity, Gemini, GPT, DeepSeek, YouTube)")
        print("\nOptional Arguments:")
        print("  notes        Free text notes about the video")
        print("\nExample:")
        print("  python add_video_to_queue_simple.py \\")
        print("    'https://youtube.com/watch?v=dQw4w9WgXcQ' \\")
        print("    'Niko Kar' \\")
        print("    'UI Design Trends' \\")
        print("    'Perplexity' \\")
        print("    'Found via deep research on 2025 design trends'")
        print("\n" + "=" * 60)
        sys.exit(1)

    video_url = sys.argv[1]
    added_by = sys.argv[2]
    topic = sys.argv[3]
    source = sys.argv[4]
    notes = sys.argv[5] if len(sys.argv) > 5 else ""

    try:
        queue_id = add_video(video_url, added_by, topic, source, notes)
        print(f"\n✅ Success! Queue ID: {queue_id}")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)
