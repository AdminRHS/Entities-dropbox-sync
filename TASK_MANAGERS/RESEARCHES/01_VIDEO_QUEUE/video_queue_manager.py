#!/usr/bin/env python3
"""
Video Queue Manager for PRT-008 VIDEO Workflow
Manages video processing queue with automated transcription routing

Usage:
    python video_queue_manager.py init                           # Create new queue
    python video_queue_manager.py add --video video.json         # Add video to queue
    python video_queue_manager.py process                        # Process next video
    python video_queue_manager.py batch --max 5                  # Process 5 videos
    python video_queue_manager.py status                         # Show queue status
"""

import json
import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

class VideoQueueManager:
    def __init__(self, base_path: str = None):
        if base_path is None:
            base_path = Path(__file__).parent
        else:
            base_path = Path(base_path)

        self.queue_dir = base_path
        self.queue_dir.mkdir(parents=True, exist_ok=True)

        self.reports_dir = base_path.parent.parent / "REPORTS" / "Videos"
        self.reports_dir.mkdir(parents=True, exist_ok=True)

        self.metadata_dir = self.reports_dir / "Metadata"
        self.metadata_dir.mkdir(parents=True, exist_ok=True)

    def get_queue_file(self, queue_id: str = None) -> Path:
        """Get path to queue file (active or specified)"""
        if queue_id is None:
            # Find active queue
            queue_files = sorted(self.queue_dir.glob("QUEUE_*.json"), reverse=True)
            if queue_files:
                return queue_files[0]  # Most recent
            else:
                # Create new queue
                queue_id = f"QUEUE_{datetime.now().strftime('%Y-%m-%d')}"
                return self.queue_dir / f"{queue_id}.json"
        else:
            return self.queue_dir / f"{queue_id}.json"

    def load_queue(self, queue_file: Path) -> Dict:
        """Load queue from JSON file"""
        if queue_file.exists():
            with open(queue_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            return None

    def save_queue(self, queue: Dict, queue_file: Path):
        """Save queue to JSON file"""
        with open(queue_file, 'w', encoding='utf-8') as f:
            json.dump(queue, f, indent=2, ensure_ascii=False)

    def initialize_queue(self, videos: List[Dict] = None) -> str:
        """Initialize new video processing queue"""
        queue_id = f"QUEUE_{datetime.now().strftime('%Y-%m-%d_%H%M%S')}"
        queue_file = self.queue_dir / f"{queue_id}.json"

        if videos is None:
            videos = []

        queue = {
            "queue_id": queue_id,
            "created_date": datetime.now().isoformat(),
            "total_videos": len(videos),
            "status": "active",
            "videos": videos,
            "statistics": {
                "queued": len([v for v in videos if v.get('processing_status') == 'queued']),
                "in_progress": 0,
                "completed": 0,
                "failed": 0
            }
        }

        self.save_queue(queue, queue_file)

        print(f"✅ Queue initialized: {queue_id}")
        print(f"   File: {queue_file}")
        print(f"   Total videos: {len(videos)}")

        return queue_id

    def auto_select_transcription_method(self, duration_seconds: int, file_size_mb: int = None) -> str:
        """
        Auto-select transcription method based on video properties

        Logic:
        - ≤ 40 min (2400s) AND ≤ 100MB → Google AI Studio
        - > 40 min OR > 100MB → TurboScribe
        - Default → Google AI Studio
        """
        MAX_GOOGLE_DURATION = 2400  # 40 minutes
        MAX_GOOGLE_SIZE_MB = 100

        if duration_seconds <= MAX_GOOGLE_DURATION:
            if file_size_mb is None or file_size_mb <= MAX_GOOGLE_SIZE_MB:
                return "google_ai_studio"

        # Exceeds limits → use TurboScribe
        return "turboscribe"

    def parse_duration_to_seconds(self, duration_str: str) -> int:
        """Convert duration string (MM:SS or HH:MM:SS) to seconds"""
        parts = duration_str.split(':')
        if len(parts) == 2:
            minutes, seconds = map(int, parts)
            return minutes * 60 + seconds
        elif len(parts) == 3:
            hours, minutes, seconds = map(int, parts)
            return hours * 3600 + minutes * 60 + seconds
        else:
            return 0

    def add_video_to_queue(self, video_metadata: Dict, queue_id: str = None) -> bool:
        """Add single video to queue"""
        queue_file = self.get_queue_file(queue_id)
        queue = self.load_queue(queue_file)

        if queue is None:
            # Create new queue
            queue_id = self.initialize_queue()
            queue_file = self.get_queue_file(queue_id)
            queue = self.load_queue(queue_file)

        # Auto-assign video ID if not present
        if 'video_id' not in video_metadata:
            existing_ids = [v.get('video_id', '') for v in queue['videos']]
            # Extract numeric part from VIDEO_XXX
            nums = [int(id.split('_')[1]) for id in existing_ids if id.startswith('VIDEO_')]
            next_num = max(nums) + 1 if nums else 1
            video_metadata['video_id'] = f"VIDEO_{next_num:03d}"

        # Parse duration if string
        if 'duration' in video_metadata and isinstance(video_metadata['duration'], str):
            video_metadata['duration_seconds'] = self.parse_duration_to_seconds(video_metadata['duration'])

        # Auto-select transcription method
        duration_seconds = video_metadata.get('duration_seconds', 0)
        file_size_mb = video_metadata.get('file_size_mb')
        video_metadata['transcription_method'] = self.auto_select_transcription_method(
            duration_seconds, file_size_mb
        )

        # Set processing status
        video_metadata['processing_status'] = 'queued'
        video_metadata['queued_at'] = datetime.now().isoformat()

        # Add to queue
        queue['videos'].append(video_metadata)
        queue['total_videos'] = len(queue['videos'])
        queue['statistics']['queued'] += 1

        # Save
        self.save_queue(queue, queue_file)

        print(f"✅ Added to queue: {video_metadata.get('title', video_metadata['video_id'])}")
        print(f"   Video ID: {video_metadata['video_id']}")
        print(f"   Duration: {video_metadata.get('duration', 'N/A')}")
        print(f"   Transcription method: {video_metadata['transcription_method']}")
        print(f"   Queue: {queue['queue_id']}")

        return True

    def get_next_queued_video(self, queue: Dict) -> Optional[Dict]:
        """Find next video with status='queued' (by priority)"""
        # Sort by priority: High > Medium > Low
        priority_order = {'High': 0, 'Medium': 1, 'Low': 2}

        queued_videos = [v for v in queue['videos'] if v.get('processing_status') == 'queued']

        if not queued_videos:
            return None

        # Sort by priority, then by score
        queued_videos.sort(
            key=lambda v: (
                priority_order.get(v.get('priority', 'Medium'), 1),
                -v.get('score', 0)
            )
        )

        return queued_videos[0]

    def update_video_status(self, queue: Dict, video_id: str, status: str, error: str = None):
        """Update video processing status in queue"""
        for video in queue['videos']:
            if video.get('video_id') == video_id:
                old_status = video.get('processing_status')
                video['processing_status'] = status

                if status == 'in_progress':
                    video['started_at'] = datetime.now().isoformat()
                    queue['statistics']['queued'] -= 1
                    queue['statistics']['in_progress'] += 1

                elif status == 'completed':
                    video['completed_at'] = datetime.now().isoformat()
                    queue['statistics']['in_progress'] -= 1
                    queue['statistics']['completed'] += 1

                elif status == 'failed':
                    video['failed_at'] = datetime.now().isoformat()
                    video['error'] = error
                    queue['statistics']['in_progress'] -= 1
                    queue['statistics']['failed'] += 1

                break

    def process_next_video(self, queue_id: str = None) -> bool:
        """Process next video in queue"""
        queue_file = self.get_queue_file(queue_id)
        queue = self.load_queue(queue_file)

        if queue is None:
            print("❌ No active queue found")
            return False

        # Find next video
        next_video = self.get_next_queued_video(queue)

        if not next_video:
            print("✅ Queue empty - all videos processed")
            return False

        video_id = next_video['video_id']
        print(f"\n🎬 Processing: {next_video.get('title', video_id)}")
        print(f"   Video ID: {video_id}")
        print(f"   Duration: {next_video.get('duration', 'N/A')}")
        print(f"   Method: {next_video.get('transcription_method')}")
        print(f"   Priority: {next_video.get('priority', 'Medium')}")

        # Update status to in_progress
        self.update_video_status(queue, video_id, 'in_progress')
        self.save_queue(queue, queue_file)

        try:
            # Step 1: Save metadata
            metadata_file = self.metadata_dir / f"{video_id}_metadata.json"
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(next_video, f, indent=2, ensure_ascii=False)
            print(f"   ✅ Metadata saved: {metadata_file}")

            # Step 2: Instructions for manual transcription
            print(f"\n   📋 TRANSCRIPTION INSTRUCTIONS:")
            print(f"   ---------------------------------")

            if next_video.get('transcription_method') == 'google_ai_studio':
                print(f"   Method: Google AI Studio")
                print(f"   1. Open: https://aistudio.google.com/")
                print(f"   2. Paste video URL: {next_video.get('video_url')}")
                print(f"   3. Upload video file (if URL doesn't work)")
                print(f"   4. Click 'Generate' and wait for transcription")
                print(f"   5. Copy transcript and save as:")
                print(f"      {self.reports_dir / f'{video_id}.md'}")

            elif next_video.get('transcription_method') == 'turboscribe':
                print(f"   Method: TurboScribe")
                print(f"   1. Open: https://turboscribe.ai/")
                print(f"   2. Paste video URL: {next_video.get('video_url')}")
                print(f"   3. Settings: English, Timestamps ON, Speaker labels ON")
                print(f"   4. Click 'Transcribe' and wait for processing")
                print(f"   5. Download SRT file")
                print(f"   6. Convert using: python convert_turboscribe.py {video_id}.srt")

            print(f"\n   ⏳ Waiting for manual completion...")
            print(f"   After transcription, run:")
            print(f"   python video_queue_manager.py complete --video {video_id}")

            return True

        except Exception as e:
            print(f"   ❌ Error: {e}")
            self.update_video_status(queue, video_id, 'failed', error=str(e))
            self.save_queue(queue, queue_file)
            return False

    def mark_video_complete(self, video_id: str, queue_id: str = None):
        """Mark video as completed after manual transcription"""
        queue_file = self.get_queue_file(queue_id)
        queue = self.load_queue(queue_file)

        if queue is None:
            print("❌ No active queue found")
            return

        # Check if transcript exists
        transcript_file = self.reports_dir / f"{video_id}.md"
        if not transcript_file.exists():
            print(f"❌ Transcript not found: {transcript_file}")
            print(f"   Please save transcript before marking complete")
            return

        # Update status
        self.update_video_status(queue, video_id, 'completed')
        self.save_queue(queue, queue_file)

        print(f"✅ Marked as completed: {video_id}")
        print(f"   Transcript: {transcript_file}")
        print(f"\n   📋 NEXT STEPS:")
        print(f"   1. Extract taxonomy: python extract_taxonomy.py {video_id}")
        print(f"   2. Populate libraries: python populate_libraries.py {video_id}")

    def show_status(self, queue_id: str = None):
        """Show current queue status"""
        queue_file = self.get_queue_file(queue_id)
        queue = self.load_queue(queue_file)

        if queue is None:
            print("❌ No active queue found")
            return

        print(f"\n📊 Queue Status: {queue['queue_id']}")
        print(f"   Created: {queue['created_date']}")
        print(f"   Total videos: {queue['total_videos']}")
        print(f"\n   Status Breakdown:")
        stats = queue.get('statistics', {})
        print(f"   - Queued:      {stats.get('queued', 0)}")
        print(f"   - In Progress: {stats.get('in_progress', 0)}")
        print(f"   - Completed:   {stats.get('completed', 0)}")
        print(f"   - Failed:      {stats.get('failed', 0)}")

        # Show next 5 videos in queue
        queued_videos = [v for v in queue['videos'] if v.get('processing_status') == 'queued']
        if queued_videos:
            print(f"\n   📋 Next videos to process:")
            for i, video in enumerate(queued_videos[:5], 1):
                print(f"   {i}. {video.get('video_id')} - {video.get('title', 'N/A')[:50]}")
                print(f"      Priority: {video.get('priority')} | Duration: {video.get('duration')}")


def main():
    parser = argparse.ArgumentParser(description='Video Queue Manager')
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Initialize queue
    init_parser = subparsers.add_parser('init', help='Initialize new queue')
    init_parser.add_argument('--videos', type=str, help='JSON file with videos list')

    # Add video
    add_parser = subparsers.add_parser('add', help='Add video to queue')
    add_parser.add_argument('--video', type=str, required=True, help='Video metadata JSON file')
    add_parser.add_argument('--queue', type=str, help='Queue ID')

    # Process video
    process_parser = subparsers.add_parser('process', help='Process next video')
    process_parser.add_argument('--queue', type=str, help='Queue ID')

    # Mark complete
    complete_parser = subparsers.add_parser('complete', help='Mark video as completed')
    complete_parser.add_argument('--video', type=str, required=True, help='Video ID')
    complete_parser.add_argument('--queue', type=str, help='Queue ID')

    # Batch process
    batch_parser = subparsers.add_parser('batch', help='Batch process multiple videos')
    batch_parser.add_argument('--max', type=int, help='Max videos to process')
    batch_parser.add_argument('--queue', type=str, help='Queue ID')

    # Show status
    status_parser = subparsers.add_parser('status', help='Show queue status')
    status_parser.add_argument('--queue', type=str, help='Queue ID')

    args = parser.parse_args()

    manager = VideoQueueManager()

    if args.command == 'init':
        videos = []
        if args.videos:
            with open(args.videos, 'r') as f:
                videos = json.load(f)
        manager.initialize_queue(videos)

    elif args.command == 'add':
        with open(args.video, 'r', encoding='utf-8') as f:
            video_metadata = json.load(f)
        manager.add_video_to_queue(video_metadata, args.queue)

    elif args.command == 'process':
        manager.process_next_video(args.queue)

    elif args.command == 'complete':
        manager.mark_video_complete(args.video, args.queue)

    elif args.command == 'batch':
        processed = 0
        max_videos = args.max if args.max else 999
        while processed < max_videos:
            success = manager.process_next_video(args.queue)
            if not success:
                break
            processed += 1

    elif args.command == 'status':
        manager.show_status(args.queue)

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
