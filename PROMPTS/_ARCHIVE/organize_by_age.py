"""
Organize Prompts by Age
- Last_Week folder: Files 7-14 days old
- Old folder: Files older than 14 days
"""
import os
import shutil
from datetime import datetime, timedelta

PROMPTS_DIR = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS"
LAST_WEEK_DIR = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\Last_Week"
OLD_DIR = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\Old"

# Calculate cutoff dates
now = datetime.now()
seven_days_ago = now - timedelta(days=7)
fourteen_days_ago = now - timedelta(days=14)

print("=" * 60)
print("ORGANIZING PROMPTS BY AGE")
print("=" * 60)
print(f"\nToday: {now.strftime('%Y-%m-%d %H:%M')}")
print(f"7 days ago: {seven_days_ago.strftime('%Y-%m-%d %H:%M')}")
print(f"14 days ago: {fourteen_days_ago.strftime('%Y-%m-%d %H:%M')}")

# Create folders
os.makedirs(LAST_WEEK_DIR, exist_ok=True)
os.makedirs(OLD_DIR, exist_ok=True)

# Get all .md files in root
md_files = [f for f in os.listdir(PROMPTS_DIR)
            if f.endswith('.md') and os.path.isfile(os.path.join(PROMPTS_DIR, f))]

print(f"\nFound {len(md_files)} .md files in PROMPTS root")

last_week_files = []
old_files = []
recent_files = []

# Categorize by age
for filename in md_files:
    filepath = os.path.join(PROMPTS_DIR, filename)
    mod_time = datetime.fromtimestamp(os.path.getmtime(filepath))

    if mod_time < fourteen_days_ago:
        old_files.append((filename, mod_time))
    elif mod_time < seven_days_ago:
        last_week_files.append((filename, mod_time))
    else:
        recent_files.append((filename, mod_time))

print(f"\n--- CATEGORIZATION ---")
print(f"Recent (last 7 days): {len(recent_files)} files")
print(f"Last Week (7-14 days): {len(last_week_files)} files")
print(f"Old (>14 days): {len(old_files)} files")

# Move Last Week files
print(f"\n--- MOVING TO Last_Week/ ---")
for filename, mod_time in sorted(last_week_files, key=lambda x: x[1]):
    source = os.path.join(PROMPTS_DIR, filename)
    dest = os.path.join(LAST_WEEK_DIR, filename)

    try:
        shutil.move(source, dest)
        days_old = (now - mod_time).days
        print(f"  Moved: {filename} ({days_old} days old)")
    except Exception as e:
        print(f"  ERROR: {filename} - {str(e)}")

# Move Old files
print(f"\n--- MOVING TO Old/ ---")
for filename, mod_time in sorted(old_files, key=lambda x: x[1]):
    source = os.path.join(PROMPTS_DIR, filename)
    dest = os.path.join(OLD_DIR, filename)

    try:
        shutil.move(source, dest)
        days_old = (now - mod_time).days
        print(f"  Moved: {filename} ({days_old} days old)")
    except Exception as e:
        print(f"  ERROR: {filename} - {str(e)}")

print("\n" + "=" * 60)
print("[SUCCESS] Organization complete!")
print("=" * 60)

print(f"\nFinal structure:")
print(f"  PROMPTS root: {len(recent_files)} recent files (last 7 days)")
print(f"  Last_Week/: {len(last_week_files)} files (7-14 days old)")
print(f"  Old/: {len(old_files)} files (>14 days old)")

# Show samples
if recent_files:
    print(f"\nSample recent files:")
    for filename, mod_time in sorted(recent_files, key=lambda x: x[1], reverse=True)[:5]:
        days_old = (now - mod_time).days
        print(f"  - {filename} ({days_old} days old)")

if last_week_files:
    print(f"\nSample Last_Week files:")
    for filename, mod_time in sorted(last_week_files, key=lambda x: x[1], reverse=True)[:5]:
        days_old = (now - mod_time).days
        print(f"  - {filename} ({days_old} days old)")

if old_files:
    print(f"\nSample Old files:")
    for filename, mod_time in sorted(old_files, key=lambda x: x[1])[:5]:
        days_old = (now - mod_time).days
        print(f"  - {filename} ({days_old} days old)")

print("\n[SUCCESS] Prompts organized by age!")
