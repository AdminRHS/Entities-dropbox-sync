"""
Export Queue Script
Exports the video queue to various formats (CSV, JSON, Markdown)
"""

import pandas as pd
import json
from datetime import datetime
import os
import sys


def get_queue_file_path():
    """Get the path to Video_Queue_Master.csv"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    queue_dir = os.path.dirname(script_dir)
    return os.path.join(queue_dir, 'Video_Queue_Master.csv')


def get_exports_dir():
    """Get the exports directory path"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    queue_dir = os.path.dirname(script_dir)
    exports_dir = os.path.join(queue_dir, 'exports')

    # Create exports directory if it doesn't exist
    if not os.path.exists(exports_dir):
        os.makedirs(exports_dir)

    return exports_dir


def load_queue():
    """Load the video queue CSV file"""
    queue_path = get_queue_file_path()
    if not os.path.exists(queue_path):
        raise FileNotFoundError(f"Queue file not found: {queue_path}")
    return pd.read_csv(queue_path)


def export_to_csv(status_filter=None):
    """
    Export queue to CSV format.

    Args:
        status_filter (str): Optional status filter (Pending, Selected, etc.)

    Returns:
        str: Path to exported file
    """
    queue_df = load_queue()

    if status_filter:
        queue_df = queue_df[queue_df['Status'] == status_filter]

    timestamp = datetime.now().strftime('%Y-%m-%d')
    filename = f"queue_export_{timestamp}"
    if status_filter:
        filename += f"_{status_filter}"
    filename += ".csv"

    export_path = os.path.join(get_exports_dir(), filename)
    queue_df.to_csv(export_path, index=False)

    print(f"✅ Exported {len(queue_df)} videos to CSV: {export_path}")
    return export_path


def export_to_json(status_filter=None):
    """
    Export queue to JSON format.

    Args:
        status_filter (str): Optional status filter

    Returns:
        str: Path to exported file
    """
    queue_df = load_queue()

    if status_filter:
        queue_df = queue_df[queue_df['Status'] == status_filter]

    # Convert to dictionary format
    videos = queue_df.to_dict('records')

    # Create export structure
    export_data = {
        'export_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'total_videos': len(videos),
        'status_filter': status_filter if status_filter else 'All',
        'videos': videos
    }

    timestamp = datetime.now().strftime('%Y-%m-%d')
    filename = f"queue_export_{timestamp}"
    if status_filter:
        filename += f"_{status_filter}"
    filename += ".json"

    export_path = os.path.join(get_exports_dir(), filename)

    with open(export_path, 'w', encoding='utf-8') as f:
        json.dump(export_data, f, indent=2, ensure_ascii=False)

    print(f"✅ Exported {len(videos)} videos to JSON: {export_path}")
    return export_path


def export_to_markdown(status_filter=None):
    """
    Export queue to Markdown table format.

    Args:
        status_filter (str): Optional status filter

    Returns:
        str: Path to exported file
    """
    queue_df = load_queue()

    if status_filter:
        queue_df = queue_df[queue_df['Status'] == status_filter]

    timestamp_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    filename_timestamp = datetime.now().strftime('%Y-%m-%d')
    filename = f"queue_export_{filename_timestamp}"
    if status_filter:
        filename += f"_{status_filter}"
    filename += ".md"

    export_path = os.path.join(get_exports_dir(), filename)

    with open(export_path, 'w', encoding='utf-8') as f:
        # Header
        f.write("# Video Queue Export\n\n")
        f.write(f"**Export Date**: {timestamp_str}\n\n")
        f.write(f"**Total Videos**: {len(queue_df)}\n\n")
        if status_filter:
            f.write(f"**Status Filter**: {status_filter}\n\n")

        f.write("---\n\n")

        # Summary stats
        f.write("## Summary\n\n")

        status_counts = queue_df['Status'].value_counts()
        f.write("### By Status\n\n")
        for status, count in status_counts.items():
            f.write(f"- **{status}**: {count}\n")
        f.write("\n")

        if 'Topic_Category' in queue_df.columns:
            topic_counts = queue_df['Topic_Category'].value_counts().head(5)
            f.write("### Top Topics\n\n")
            for topic, count in topic_counts.items():
                f.write(f"- **{topic}**: {count}\n")
            f.write("\n")

        f.write("---\n\n")

        # Videos table
        f.write("## Videos\n\n")

        # Sort by priority score (highest first)
        queue_df_sorted = queue_df.sort_values('Priority_Score', ascending=False)

        # Table header
        f.write("| Queue ID | Title | Channel | Topic | Status | Priority | Added By | Added Date |\n")
        f.write("|----------|-------|---------|-------|--------|----------|----------|------------|\n")

        # Table rows
        for _, row in queue_df_sorted.iterrows():
            title = str(row['Video_Title'])[:50]  # Truncate long titles
            channel = str(row['Channel_Name'])[:30]
            topic = str(row['Topic_Category'])[:20]
            status = str(row['Status'])
            priority = f"{row['Priority_Score']}/100"
            added_by = str(row['Added_By'])
            added_date = str(row['Added_Date'])

            f.write(f"| {row['Queue_ID']} | {title} | {channel} | {topic} | {status} | {priority} | {added_by} | {added_date} |\n")

        f.write("\n---\n\n")

        # Detailed list
        f.write("## Detailed Listing\n\n")

        for _, row in queue_df_sorted.iterrows():
            f.write(f"### {row['Queue_ID']}: {row['Video_Title']}\n\n")
            f.write(f"- **Channel**: {row['Channel_Name']}\n")
            f.write(f"- **Video URL**: {row['Video_URL']}\n")
            f.write(f"- **Views**: {row['Views']:,}\n")
            f.write(f"- **Likes**: {row['Likes']:,}\n")
            f.write(f"- **Publish Date**: {row['Publish_Date']}\n")
            f.write(f"- **Duration**: {row['Duration']}\n")
            f.write(f"- **Topic**: {row['Topic_Category']}\n")
            f.write(f"- **Research Source**: {row['Research_Source']}\n")
            f.write(f"- **Priority Score**: {row['Priority_Score']}/100\n")
            f.write(f"- **Status**: {row['Status']}\n")
            f.write(f"- **Added By**: {row['Added_By']} on {row['Added_Date']}\n")

            if row['Selected_By']:
                f.write(f"- **Selected By**: {row['Selected_By']} on {row['Selected_Date']}\n")

            if row['Notes']:
                f.write(f"- **Notes**: {row['Notes']}\n")

            f.write("\n")

    print(f"✅ Exported {len(queue_df)} videos to Markdown: {export_path}")
    return export_path


def export_all_formats(status_filter=None):
    """Export to all formats (CSV, JSON, Markdown)"""
    print("\nExporting to all formats...\n")

    csv_path = export_to_csv(status_filter)
    json_path = export_to_json(status_filter)
    md_path = export_to_markdown(status_filter)

    print(f"\n✅ All exports complete!")
    print(f"\nExported files:")
    print(f"  CSV:      {csv_path}")
    print(f"  JSON:     {json_path}")
    print(f"  Markdown: {md_path}")

    return {'csv': csv_path, 'json': json_path, 'markdown': md_path}


# CLI interface
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("=" * 60)
        print("Export Queue - Command Line Interface")
        print("=" * 60)
        print("\nUsage:")
        print("  python export_queue.py <format> [status_filter]")
        print("\nFormats:")
        print("  csv        Export to CSV format")
        print("  json       Export to JSON format")
        print("  markdown   Export to Markdown format")
        print("  all        Export to all formats")
        print("\nOptional Status Filter:")
        print("  Pending, Selected, Parsing, Parsed, Rejected")
        print("\nExamples:")
        print("  python export_queue.py csv")
        print("  python export_queue.py json Pending")
        print("  python export_queue.py markdown Selected")
        print("  python export_queue.py all")
        print("\n" + "=" * 60)
        sys.exit(1)

    format_type = sys.argv[1].lower()
    status_filter = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        if format_type == 'csv':
            export_to_csv(status_filter)
        elif format_type == 'json':
            export_to_json(status_filter)
        elif format_type == 'markdown' or format_type == 'md':
            export_to_markdown(status_filter)
        elif format_type == 'all':
            export_all_formats(status_filter)
        else:
            print(f"❌ Unknown format: {format_type}")
            print("Valid formats: csv, json, markdown, all")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)
