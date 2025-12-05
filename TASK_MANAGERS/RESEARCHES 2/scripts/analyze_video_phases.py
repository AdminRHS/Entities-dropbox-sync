"""
Analyze video processing phases and show table view of gaps
Shows which videos are lacking in which phases
"""
import csv
from pathlib import Path
from datetime import datetime
from collections import defaultdict

def get_progress_file():
    """Get path to progress tracker CSV"""
    base_path = Path(__file__).parent.parent
    return base_path / 'VIDEO_PROGRESS_TRACKER.csv'

def get_transcriptions_dir():
    """Get transcriptions directory"""
    base_path = Path(__file__).parent.parent
    return base_path / '02_TRANSCRIPTIONS'

def find_all_videos():
    """Find all transcribed videos"""
    trans_dir = get_transcriptions_dir()
    if not trans_dir.exists():
        return []

    video_files = sorted(trans_dir.glob('Video_*.md'))
    videos = []

    for vf in video_files:
        # Skip special files
        if any(x in vf.name for x in ['_Processing', '_Taxonomy', '_ExecutionFlow', '_Queue', '_Discovery']):
            continue

        # Extract video number
        try:
            num = vf.stem.replace('Video_', '').replace('Video_0', '')
            videos.append(int(num))
        except:
            pass

    return sorted(videos)

def load_progress_data():
    """Load progress tracker data"""
    progress_file = get_progress_file()

    if not progress_file.exists():
        return {}

    video_data = {}
    with open(progress_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            video_num = int(row['Video_Number'])
            video_data[video_num] = row

    return video_data

def analyze_phases():
    """Analyze which videos are in which phases"""
    # Find all videos
    all_videos = find_all_videos()

    # Load progress data
    progress_data = load_progress_data()

    # Phase definitions
    phases = [
        'Phase_0_Queued',
        'Phase_1_Transcribed',
        'Phase_2_Extraction',
        'Phase_3_Gap_Analysis',
        'Phase_4_Integration',
        'Phase_5_Mapping',
        'Complete'
    ]

    # Analyze each video
    results = []

    for video_num in all_videos:
        if video_num in progress_data:
            row = progress_data[video_num]
            video_info = {
                'video_number': video_num,
                'title': row['Title'][:40] + '...' if len(row['Title']) > 40 else row['Title'],
                'current_phase': row['Current_Phase'],
                'status': row['Status'],
                'phases': {}
            }

            for phase in phases:
                video_info['phases'][phase] = row.get(phase, '') != ''
        else:
            # Video exists but not in tracker
            video_info = {
                'video_number': video_num,
                'title': 'Not in tracker',
                'current_phase': 'Phase_1_Transcribed (assumed)',
                'status': 'Unknown',
                'phases': {
                    'Phase_0_Queued': True,
                    'Phase_1_Transcribed': True,  # File exists, so transcribed
                    'Phase_2_Extraction': False,
                    'Phase_3_Gap_Analysis': False,
                    'Phase_4_Integration': False,
                    'Phase_5_Mapping': False,
                    'Complete': False
                }
            }

        results.append(video_info)

    return results, phases

def generate_table_report():
    """Generate table view of video phases"""
    results, phases = analyze_phases()

    print("\n" + "="*120)
    print("VIDEO PROCESSING PHASE ANALYSIS")
    print("="*120)
    print(f"Total Videos Found: {len(results)}")
    print(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("="*120)

    # Table header
    print(f"\n{'Video':<8} {'Title':<30} {'Current Phase':<25} {'P0':<4} {'P1':<4} {'P2':<4} {'P3':<4} {'P4':<4} {'P5':<4} {'Done':<4}")
    print("-"*120)

    # Phase statistics
    phase_stats = defaultdict(int)

    for video in results:
        # Count phase completion
        for phase, completed in video['phases'].items():
            if completed:
                phase_stats[phase] += 1

        # Format row
        video_num = f"V{video['video_number']:03d}"
        title = video['title'][:28]
        current = video['current_phase'].replace('Phase_', 'P').replace('_', ' ')[:23]

        # Phase indicators
        p0 = 'YES' if video['phases']['Phase_0_Queued'] else 'NO '
        p1 = 'YES' if video['phases']['Phase_1_Transcribed'] else 'NO '
        p2 = 'YES' if video['phases']['Phase_2_Extraction'] else 'NO '
        p3 = 'YES' if video['phases']['Phase_3_Gap_Analysis'] else 'NO '
        p4 = 'YES' if video['phases']['Phase_4_Integration'] else 'NO '
        p5 = 'YES' if video['phases']['Phase_5_Mapping'] else 'NO '
        done = 'YES' if video['phases']['Complete'] else 'NO '

        print(f"{video_num:<8} {title:<30} {current:<25} {p0:<4} {p1:<4} {p2:<4} {p3:<4} {p4:<4} {p5:<4} {done:<4}")

    print("-"*120)

    # Summary statistics
    print("\n" + "="*120)
    print("PHASE COMPLETION STATISTICS")
    print("="*120)

    total_videos = len(results)

    print(f"\n{'Phase':<30} {'Completed':<12} {'Percentage':<12} {'Missing':<12}")
    print("-"*70)

    phase_names = {
        'Phase_0_Queued': 'Phase 0: Queued',
        'Phase_1_Transcribed': 'Phase 1: Transcribed',
        'Phase_2_Extraction': 'Phase 2: Extraction',
        'Phase_3_Gap_Analysis': 'Phase 3: Gap Analysis',
        'Phase_4_Integration': 'Phase 4: Integration',
        'Phase_5_Mapping': 'Phase 5: Mapping',
        'Complete': 'Complete'
    }

    for phase in phases:
        completed = phase_stats[phase]
        percentage = (completed / total_videos * 100) if total_videos > 0 else 0
        missing = total_videos - completed

        print(f"{phase_names[phase]:<30} {completed:<12} {percentage:>5.1f}%      {missing:<12}")

    print("-"*70)

    # Bottleneck analysis
    print("\n" + "="*120)
    print("BOTTLENECK ANALYSIS")
    print("="*120)

    # Find videos stuck at each phase
    bottlenecks = defaultdict(list)

    for video in results:
        current_phase = video['current_phase']
        if video['status'] != 'Complete':
            bottlenecks[current_phase].append(video['video_number'])

    if bottlenecks:
        print(f"\n{'Phase':<35} {'Videos Stuck':<10} {'Video Numbers'}")
        print("-"*120)

        for phase in phases[:-1]:  # Exclude 'Complete'
            if phase in bottlenecks:
                videos = bottlenecks[phase]
                video_list = ', '.join([f"V{v:03d}" for v in sorted(videos)[:10]])
                if len(videos) > 10:
                    video_list += f"... (+{len(videos)-10} more)"

                print(f"{phase_names.get(phase, phase):<35} {len(videos):<10} {video_list}")
    else:
        print("\nNo bottlenecks - all videos are complete!")

    # Recommendations
    print("\n" + "="*120)
    print("RECOMMENDATIONS")
    print("="*120)

    # Find next videos to process
    phase_priority = [
        'Phase_1_Transcribed',
        'Phase_2_Extraction',
        'Phase_3_Gap_Analysis',
        'Phase_4_Integration',
        'Phase_5_Mapping'
    ]

    for phase in phase_priority:
        videos_at_phase = [v for v in results if v['current_phase'] == phase and v['status'] != 'Complete']
        if videos_at_phase:
            next_phase_idx = phases.index(phase) + 1
            next_phase = phases[next_phase_idx]
            next_phase_name = phase_names[next_phase]

            video_nums = ', '.join([f"V{v['video_number']:03d}" for v in sorted(videos_at_phase, key=lambda x: x['video_number'])[:5]])

            print(f"\n>> {len(videos_at_phase)} video(s) ready for {next_phase_name}:")
            print(f"   Videos: {video_nums}")

            # Show command
            if next_phase == 'Phase_2_Extraction':
                print(f"   Run: PMT-007 (Objects Library Extraction)")
            elif next_phase == 'Phase_3_Gap_Analysis':
                print(f"   Run: PMT-009 Part 1 (Gap Analysis)")
            elif next_phase == 'Phase_4_Integration':
                print(f"   Run: PMT-009 Part 2 (Integration)")
            elif next_phase == 'Phase_5_Mapping':
                print(f"   Run: PMT-009 Part 3 (Mapping)")

            break

    print("\n" + "="*120)

def generate_gap_report():
    """Generate detailed gap report"""
    results, phases = analyze_phases()

    # Find videos missing each phase
    gaps = defaultdict(list)

    for video in results:
        for phase in phases:
            if not video['phases'][phase]:
                gaps[phase].append(video['video_number'])

    print("\n" + "="*120)
    print("DETAILED GAP REPORT - Videos Missing Each Phase")
    print("="*120)

    phase_names = {
        'Phase_0_Queued': 'Phase 0: Queued',
        'Phase_1_Transcribed': 'Phase 1: Transcribed',
        'Phase_2_Extraction': 'Phase 2: Extraction',
        'Phase_3_Gap_Analysis': 'Phase 3: Gap Analysis',
        'Phase_4_Integration': 'Phase 4: Integration',
        'Phase_5_Mapping': 'Phase 5: Mapping',
        'Complete': 'Complete'
    }

    for phase in phases:
        if gaps[phase]:
            print(f"\n{phase_names[phase]}:")
            print(f"Missing: {len(gaps[phase])} videos")

            video_list = ', '.join([f"Video_{v:03d}" for v in sorted(gaps[phase])])
            print(f"Videos: {video_list}")
        else:
            print(f"\n{phase_names[phase]}: All videos complete")

    print("\n" + "="*120)

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == 'gaps':
        generate_gap_report()
    else:
        generate_table_report()
