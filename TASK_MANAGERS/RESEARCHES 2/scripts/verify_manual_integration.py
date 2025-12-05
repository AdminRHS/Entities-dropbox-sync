"""
Verification System: Check if transcribed videos have been manually integrated
Scans Libraries and Task Managers for entities that came from the 22 transcribed videos
"""
import re
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

def get_base_paths():
    """Get paths to key directories"""
    dropbox = Path("C:/Users/Dell/Dropbox")

    # Check for RESEARCHES 2 folder (current location)
    researches_path = dropbox / 'ENTITIES/TASK_MANAGERS/RESEARCHES 2'
    if not researches_path.exists():
        researches_path = dropbox / 'ENTITIES/TASK_MANAGERS/RESEARCHES'

    return {
        'transcriptions': researches_path / '02_TRANSCRIPTIONS',
        'libraries': dropbox / 'ENTITIES/LIBRARIES',
        'task_managers': dropbox / 'ENTITIES/TASK_MANAGERS',
        'prompts': dropbox / 'ENTITIES/PROMPTS',
        'entities': dropbox / 'ENTITIES',
        'dropbox_root': dropbox
    }

def find_all_videos():
    """Find all transcribed videos"""
    paths = get_base_paths()
    trans_dir = paths['transcriptions']

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
            videos.append({
                'number': int(num),
                'file': vf,
                'name': vf.stem
            })
        except:
            pass

    return sorted(videos, key=lambda x: x['number'])

def extract_video_entities(video_file):
    """Extract all entities mentioned in a video transcription"""
    entities = {
        'tools': set(),
        'workflows': set(),
        'actions': set(),
        'objects': set(),
        'professions': set(),
        'skills': set(),
        'video_title': '',
        'video_url': ''
    }

    try:
        with open(video_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract video title
        title_match = re.search(r'Video Title:\s*(.+)', content)
        if title_match:
            entities['video_title'] = title_match.group(1).strip()

        # Extract video URL
        url_match = re.search(r'YouTube URL:\s*(.+)', content)
        if url_match:
            entities['video_url'] = url_match.group(1).strip()

        # Extract entity IDs
        # Tools: TOL-### or TOOL-{CATEGORY}-###
        entities['tools'] = set(re.findall(r'TOL-\d{3}', content))
        entities['tools'].update(re.findall(r'TOOL-[A-Z]+-\d{3}', content))

        # Workflows: WRF-###
        entities['workflows'] = set(re.findall(r'WRF-\d{3}', content))

        # Actions: ACT-###
        entities['actions'] = set(re.findall(r'ACT-\d{3}', content))

        # Objects: OBJ-###
        entities['objects'] = set(re.findall(r'OBJ-\d{3}', content))

        # Professions: PRF-###
        entities['professions'] = set(re.findall(r'PRF-\d{3}', content))

        # Skills: SKL-###
        entities['skills'] = set(re.findall(r'SKL-\d{3}', content))

    except Exception as e:
        print(f"Error reading {video_file}: {e}")

    return entities

def scan_libraries_for_video_references(video_num):
    """Scan Libraries for references to a specific video number"""
    paths = get_base_paths()
    libraries_dir = paths['libraries']

    references = {
        'tools': [],
        'workflows': [],
        'actions': [],
        'objects': [],
        'professions': [],
        'skills': [],
        'other': []
    }

    if not libraries_dir.exists():
        return references

    # Patterns to search for
    video_patterns = [
        f'Video_{video_num:03d}',
        f'Video {video_num:03d}',
        f'Video_{video_num}',
        f'Video {video_num}',
        f'V{video_num:03d}',
        f'V{video_num}'
    ]

    # Scan all JSON files in Libraries
    for json_file in libraries_dir.rglob('*.json'):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check if any video pattern is mentioned
            for pattern in video_patterns:
                if pattern in content:
                    # Determine category
                    if 'Tools' in str(json_file):
                        references['tools'].append(str(json_file.relative_to(libraries_dir)))
                    elif 'Workflows' in str(json_file):
                        references['workflows'].append(str(json_file.relative_to(libraries_dir)))
                    elif 'Actions' in str(json_file):
                        references['actions'].append(str(json_file.relative_to(libraries_dir)))
                    elif 'Objects' in str(json_file) or 'Responsibilities' in str(json_file):
                        references['objects'].append(str(json_file.relative_to(libraries_dir)))
                    elif 'Professions' in str(json_file):
                        references['professions'].append(str(json_file.relative_to(libraries_dir)))
                    elif 'Skills' in str(json_file):
                        references['skills'].append(str(json_file.relative_to(libraries_dir)))
                    else:
                        references['other'].append(str(json_file.relative_to(libraries_dir)))
                    break
        except:
            pass

    return references

def scan_task_managers_for_video_references(video_num):
    """Scan Task Managers for references to a specific video number"""
    paths = get_base_paths()
    tm_dir = paths['task_managers']

    references = {
        'workflows': [],
        'other': []
    }

    if not tm_dir.exists():
        return references

    # Patterns to search for
    video_patterns = [
        f'Video_{video_num:03d}',
        f'Video {video_num:03d}',
        f'Video_{video_num}',
        f'Video {video_num}',
        f'V{video_num:03d}',
        f'V{video_num}'
    ]

    # Scan workflow directories
    workflow_dirs = [
        tm_dir / 'TSM-006_Workflows',
        tm_dir / 'Workflows'
    ]

    for workflow_dir in workflow_dirs:
        if not workflow_dir.exists():
            continue

        for json_file in workflow_dir.rglob('*.json'):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Check if any video pattern is mentioned
                for pattern in video_patterns:
                    if pattern in content:
                        references['workflows'].append(str(json_file.relative_to(tm_dir)))
                        break
            except:
                pass

    # Scan other task manager files
    for json_file in tm_dir.rglob('*.json'):
        # Skip workflow directories already scanned
        if any(wd.name in str(json_file) for wd in workflow_dirs if wd.exists()):
            continue

        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check if any video pattern is mentioned
            for pattern in video_patterns:
                if pattern in content:
                    references['other'].append(str(json_file.relative_to(tm_dir)))
                    break
        except:
            pass

    return references

def check_entities_master_list(video_num):
    """Check if video is referenced in ENTITIES_MASTER_LIST.csv"""
    paths = get_base_paths()

    # Possible locations for master list
    possible_paths = [
        paths['libraries'] / 'ENTITIES_MASTER_LIST.csv',
        paths['task_managers'] / 'ENTITIES_MASTER_LIST.csv',
        Path('C:/Users/Dell/Dropbox/ENTITIES/ENTITIES_MASTER_LIST.csv')
    ]

    video_patterns = [
        f'Video_{video_num:03d}',
        f'Video {video_num:03d}',
        f'V{video_num:03d}'
    ]

    for master_path in possible_paths:
        if master_path.exists():
            try:
                with open(master_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                for pattern in video_patterns:
                    if pattern in content:
                        return True, str(master_path)
            except:
                pass

    return False, None

def scan_for_scattered_reports(video_num):
    """Scan entire Dropbox for scattered reports/files referencing this video"""
    paths = get_base_paths()
    dropbox_root = paths['dropbox_root']

    video_patterns = [
        f'Video_{video_num:03d}',
        f'Video {video_num:03d}',
        f'Video_{video_num}',
        f'Video {video_num}',
        f'V{video_num:03d}',
        f'V{video_num}'
    ]

    scattered_files = {
        'markdown': [],
        'json': [],
        'csv': [],
        'txt': [],
        'other': []
    }

    # Directories to skip (to avoid recursion issues and irrelevant files)
    skip_dirs = {
        '.git', 'node_modules', '__pycache__', 'venv', '.venv',
        'Cache', 'cache', 'temp', 'tmp', '.obsidian', '.trash'
    }

    # File extensions to scan
    scan_extensions = {'.md', '.json', '.csv', '.txt', '.yaml', '.yml'}

    try:
        # Scan ENTITIES directory thoroughly
        for file_path in dropbox_root.rglob('*'):
            # Skip directories in skip list
            if any(skip_dir in file_path.parts for skip_dir in skip_dirs):
                continue

            # Only scan files with relevant extensions
            if file_path.suffix.lower() not in scan_extensions:
                continue

            # Skip the transcription file itself
            if 'TRANSCRIPTIONS' in str(file_path) and f'Video_{video_num:03d}' in file_path.name:
                continue

            # Skip very large files (> 5MB)
            try:
                if file_path.stat().st_size > 5 * 1024 * 1024:
                    continue
            except:
                continue

            # Check file content
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                for pattern in video_patterns:
                    if pattern in content:
                        # Categorize by extension
                        ext = file_path.suffix.lower()
                        rel_path = str(file_path.relative_to(dropbox_root))

                        if ext == '.md':
                            scattered_files['markdown'].append(rel_path)
                        elif ext == '.json':
                            scattered_files['json'].append(rel_path)
                        elif ext == '.csv':
                            scattered_files['csv'].append(rel_path)
                        elif ext == '.txt':
                            scattered_files['txt'].append(rel_path)
                        else:
                            scattered_files['other'].append(rel_path)
                        break
            except:
                pass

    except Exception as e:
        print(f"Error scanning for scattered files: {e}")

    return scattered_files

def generate_verification_report(deep_scan=False):
    """Generate comprehensive verification report

    Args:
        deep_scan: If True, scan entire Dropbox for scattered reports (slow)
    """
    print("\n" + "="*120)
    print("VIDEO INTEGRATION VERIFICATION REPORT")
    print("="*120)
    print(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    if deep_scan:
        print("Mode: DEEP SCAN (includes scattered report search)")
    else:
        print("Mode: STANDARD (Libraries & Task Managers only)")
    print("="*120)

    # Find all videos
    videos = find_all_videos()
    print(f"\nTotal Videos Found: {len(videos)}")

    # Analyze each video
    results = []

    for video in videos:
        video_num = video['number']
        video_file = video['file']

        # Extract entities from transcription
        entities = extract_video_entities(video_file)

        # Scan for references in Libraries
        lib_refs = scan_libraries_for_video_references(video_num)

        # Scan for references in Task Managers
        tm_refs = scan_task_managers_for_video_references(video_num)

        # Check master list
        in_master, master_path = check_entities_master_list(video_num)

        # Scan for scattered reports (optional - can be slow)
        scattered = {'markdown': [], 'json': [], 'csv': [], 'txt': [], 'other': []}
        if deep_scan:
            print(f"  Deep scanning V{video_num:03d}...", end='\r')
            scattered = scan_for_scattered_reports(video_num)
        else:
            print(f"  Scanning V{video_num:03d}...", end='\r')

        # Count total references
        total_lib_refs = sum(len(refs) for refs in lib_refs.values())
        total_tm_refs = sum(len(refs) for refs in tm_refs.values())
        total_scattered = sum(len(refs) for refs in scattered.values())
        total_refs = total_lib_refs + total_tm_refs + total_scattered

        # Determine integration status
        if total_refs > 0 or in_master:
            status = "INTEGRATED"
        elif len(entities['tools']) > 0 or len(entities['workflows']) > 0:
            status = "PENDING"
        else:
            status = "NO ENTITIES"

        results.append({
            'video_num': video_num,
            'video_title': entities['video_title'][:40] if entities['video_title'] else 'Unknown',
            'status': status,
            'entities': entities,
            'lib_refs': lib_refs,
            'tm_refs': tm_refs,
            'scattered': scattered,
            'total_refs': total_refs,
            'total_scattered': total_scattered,
            'in_master': in_master,
            'master_path': master_path
        })

    print(" " * 50, end='\r')  # Clear scanning message

    # Summary statistics
    integrated = sum(1 for r in results if r['status'] == 'INTEGRATED')
    pending = sum(1 for r in results if r['status'] == 'PENDING')
    no_entities = sum(1 for r in results if r['status'] == 'NO ENTITIES')

    print("\n" + "="*120)
    print("INTEGRATION STATUS SUMMARY")
    print("="*120)

    if len(videos) > 0:
        print(f"\nIntegrated Videos:    {integrated}/{len(videos)} ({integrated/len(videos)*100:.1f}%)")
        print(f"Pending Integration:  {pending}/{len(videos)} ({pending/len(videos)*100:.1f}%)")
        print(f"No Entities Found:    {no_entities}/{len(videos)} ({no_entities/len(videos)*100:.1f}%)")
    else:
        print("\nNo videos found in transcriptions directory!")
        print("Check path:", get_base_paths()['transcriptions'])

    # Detailed table
    print("\n" + "="*130)
    print("DETAILED VERIFICATION TABLE")
    print("="*130)
    print(f"\n{'Video':<8} {'Title':<35} {'Status':<13} {'Entities':<10} {'Lib':<6} {'TM':<6} {'Scattered':<10} {'Master':<8}")
    print("-"*130)

    for r in results:
        video_id = f"V{r['video_num']:03d}"
        title = r['video_title'][:33]
        status = r['status']

        # Count entities
        entity_count = sum(len(r['entities'][k]) for k in ['tools', 'workflows', 'actions', 'objects', 'professions', 'skills'])

        lib_count = sum(len(refs) for refs in r['lib_refs'].values())
        tm_count = sum(len(refs) for refs in r['tm_refs'].values())
        scattered_count = r['total_scattered']
        in_master = 'YES' if r['in_master'] else 'NO'

        print(f"{video_id:<8} {title:<35} {status:<13} {entity_count:<10} {lib_count:<6} {tm_count:<6} {scattered_count:<10} {in_master:<8}")

    print("-"*130)

    # Detailed integration breakdown
    print("\n" + "="*120)
    print("INTEGRATION DETAILS - Videos with Library/Task Manager References")
    print("="*120)

    integrated_videos = [r for r in results if r['status'] == 'INTEGRATED']

    if integrated_videos:
        for r in integrated_videos:
            print(f"\n{'='*120}")
            print(f"Video {r['video_num']:03d}: {r['video_title']}")
            print(f"{'='*120}")

            # Show entity counts from transcription
            print("\nEntities in Transcription:")
            print(f"  - Tools:       {len(r['entities']['tools'])}")
            print(f"  - Workflows:   {len(r['entities']['workflows'])}")
            print(f"  - Actions:     {len(r['entities']['actions'])}")
            print(f"  - Objects:     {len(r['entities']['objects'])}")
            print(f"  - Professions: {len(r['entities']['professions'])}")
            print(f"  - Skills:      {len(r['entities']['skills'])}")

            # Show library references
            lib_total = sum(len(refs) for refs in r['lib_refs'].values())
            if lib_total > 0:
                print(f"\nLibrary References ({lib_total} files):")
                for category, refs in r['lib_refs'].items():
                    if refs:
                        print(f"  {category.capitalize()}:")
                        for ref in refs[:3]:  # Show first 3
                            print(f"    - {ref}")
                        if len(refs) > 3:
                            print(f"    ... and {len(refs)-3} more")

            # Show task manager references
            tm_total = sum(len(refs) for refs in r['tm_refs'].values())
            if tm_total > 0:
                print(f"\nTask Manager References ({tm_total} files):")
                for category, refs in r['tm_refs'].items():
                    if refs:
                        print(f"  {category.capitalize()}:")
                        for ref in refs[:3]:  # Show first 3
                            print(f"    - {ref}")
                        if len(refs) > 3:
                            print(f"    ... and {len(refs)-3} more")

            # Show scattered reports/files
            scattered_total = r['total_scattered']
            if scattered_total > 0:
                print(f"\nScattered Reports/Files ({scattered_total} files):")
                for category, refs in r['scattered'].items():
                    if refs:
                        print(f"  {category.capitalize()} files ({len(refs)}):")
                        for ref in refs[:5]:  # Show first 5
                            print(f"    - {ref}")
                        if len(refs) > 5:
                            print(f"    ... and {len(refs)-5} more")

            # Show master list status
            if r['in_master']:
                print(f"\nMaster List: YES")
                print(f"  Location: {r['master_path']}")
            else:
                print(f"\nMaster List: NO")
    else:
        print("\nNo integrated videos found.")

    # Pending videos
    print("\n" + "="*120)
    print("PENDING INTEGRATION - Videos with Entities but No References")
    print("="*120)

    pending_videos = [r for r in results if r['status'] == 'PENDING']

    if pending_videos:
        print(f"\nFound {len(pending_videos)} video(s) with extracted entities but no integration:")

        for r in pending_videos:
            entity_count = sum(len(r['entities'][k]) for k in ['tools', 'workflows', 'actions', 'objects', 'professions', 'skills'])
            print(f"\n  V{r['video_num']:03d}: {r['video_title']}")
            print(f"    Entities: {entity_count} total")
            print(f"    - Tools: {len(r['entities']['tools'])}, Workflows: {len(r['entities']['workflows'])}, Actions: {len(r['entities']['actions'])}")
            print(f"    - Objects: {len(r['entities']['objects'])}, Professions: {len(r['entities']['professions'])}, Skills: {len(r['entities']['skills'])}")
    else:
        print("\nNo pending videos - all videos with entities have been integrated!")

    # Videos with no entities
    print("\n" + "="*120)
    print("NO ENTITIES - Videos without Entity Extractions")
    print("="*120)

    no_entity_videos = [r for r in results if r['status'] == 'NO ENTITIES']

    if no_entity_videos:
        print(f"\nFound {len(no_entity_videos)} video(s) with no entity IDs in transcription:")
        for r in no_entity_videos:
            print(f"  V{r['video_num']:03d}: {r['video_title']}")
        print("\nNote: These videos may use older transcription format (pre-v4.0)")
    else:
        print("\nAll videos have entity extractions!")

    # Recommendations
    print("\n" + "="*120)
    print("RECOMMENDATIONS")
    print("="*120)

    if integrated_videos:
        print(f"\n1. UPDATE VIDEO_PROGRESS_TRACKER.csv for {len(integrated_videos)} integrated video(s):")
        for r in integrated_videos[:5]:
            print(f"   - V{r['video_num']:03d}: Mark as Complete (already in Libraries/Task Managers)")
        if len(integrated_videos) > 5:
            print(f"   ... and {len(integrated_videos)-5} more")

    if pending_videos:
        print(f"\n2. VERIFY MANUAL INTEGRATION for {len(pending_videos)} pending video(s):")
        print("   These videos have entity IDs in transcription but no file references found.")
        print("   Check if entities were manually added without video attribution.")

    if no_entity_videos:
        print(f"\n3. RE-TRANSCRIBE {len(no_entity_videos)} video(s) with PMT-004 v4.0+:")
        print("   These videos use old format without entity ID extraction.")
        print("   Re-run PMT-004 to get structured entity data.")

    print("\n" + "="*120)

    if not deep_scan:
        print("\nNOTE: Run with '--deep' flag to scan entire Dropbox for scattered reports:")
        print("  python verify_manual_integration.py --deep")
        print("  (Warning: Deep scan may take several minutes)")
    print("\n" + "="*120)

if __name__ == '__main__':
    import sys
    deep_scan = '--deep' in sys.argv or '-d' in sys.argv
    generate_verification_report(deep_scan=deep_scan)
