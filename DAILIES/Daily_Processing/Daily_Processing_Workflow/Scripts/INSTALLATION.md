# Installation Guide - Daily Processing Automation

**Version:** 1.0
**Date:** 2025-11-25
**Target Users:** Daily processing team members

---

## Prerequisites

### System Requirements

- **Operating System:** macOS, Linux, or Windows
- **Python Version:** 3.7 or higher (3.11+ recommended)
- **Disk Space:** ~100 MB (for Python packages)
- **Internet:** Required for AI API calls

### Check Python Installation

```bash
# Check if Python 3 is installed
python3 --version

# Should show: Python 3.x.x (where x >= 7)
```

**If Python is not installed:**
- **macOS:** `brew install python3` (requires Homebrew)
- **Linux:** `sudo apt-get install python3` (Ubuntu/Debian)
- **Windows:** Download from https://python.org

---

## Step 1: Install Python Dependencies

### Option A: Using pip (Recommended)

```bash
# Install Anthropic library (for Claude AI)
pip3 install anthropic

# OR install OpenAI library (alternative)
pip3 install openai

# OR install both
pip3 install anthropic openai
```

### Option B: Using requirements.txt

Create a file named `requirements.txt`:

```txt
anthropic>=0.25.0
openai>=1.0.0
```

Then install:

```bash
pip3 install -r requirements.txt
```

### Verify Installation

```bash
# Check if packages are installed
pip3 list | grep anthropic
pip3 list | grep openai

# Should show:
# anthropic    0.x.x
# openai       1.x.x
```

---

## Step 2: Set Up API Keys

### Get Your API Key

**For Claude (Anthropic):**
1. Go to https://console.anthropic.com
2. Sign up or log in
3. Navigate to API Keys
4. Create a new key (starts with `sk-ant-api03-...`)
5. Copy the key (you won't see it again!)

**For OpenAI:**
1. Go to https://platform.openai.com
2. Sign up or log in
3. Navigate to API Keys
4. Create a new key (starts with `sk-...`)
5. Copy the key

### Set Environment Variable

**macOS / Linux:**

```bash
# Add to your shell profile (~/.bashrc, ~/.zshrc, or ~/.bash_profile)
echo 'export ANTHROPIC_API_KEY="sk-ant-api03-YOUR-KEY-HERE"' >> ~/.zshrc

# OR for OpenAI
echo 'export OPENAI_API_KEY="sk-YOUR-KEY-HERE"' >> ~/.zshrc

# Reload shell configuration
source ~/.zshrc

# Verify it's set
echo $ANTHROPIC_API_KEY
```

**Windows (PowerShell):**

```powershell
# Set for current session
$env:ANTHROPIC_API_KEY = "sk-ant-api03-YOUR-KEY-HERE"

# Set permanently (requires admin)
[System.Environment]::SetEnvironmentVariable('ANTHROPIC_API_KEY', 'sk-ant-api03-YOUR-KEY-HERE', 'User')

# Verify
echo $env:ANTHROPIC_API_KEY
```

**Windows (Command Prompt):**

```cmd
# Set for current session
set ANTHROPIC_API_KEY=sk-ant-api03-YOUR-KEY-HERE

# Set permanently
setx ANTHROPIC_API_KEY "sk-ant-api03-YOUR-KEY-HERE"

# Verify
echo %ANTHROPIC_API_KEY%
```

---

## Step 3: Verify Installation

### Quick Test

```bash
# Navigate to scripts directory
cd "/Users/nikolay/Library/CloudStorage/Dropbox/ENTITIES/DAILIES/Daily_Processing/Daily_Processing_Workflow/Scripts"

# Test Python import
python3 -c "import anthropic; print('✅ Anthropic installed')"
python3 -c "import openai; print('✅ OpenAI installed')"

# Test API key is set
python3 -c "import os; print('✅ API key set' if os.environ.get('ANTHROPIC_API_KEY') else '❌ API key not set')"
```

### Test Collection Script (No API Required)

```bash
# Run dry-run collection
python3 collect_daily_files.py --week 4 --day 24 --dry-run

# Should show:
# [DRY RUN] Daily File Collection
# Date: 2025-11-25
# ...
# Total Employees Processed: 52
# Total Files Collected: 165
```

---

## Step 4: First Run

### Test with Dry Run

```bash
# Test complete workflow without making changes
python3 run_daily_processing.py --dry-run

# This will:
# - Preview collection (no files copied)
# - Preview extraction (no API calls)
# - Preview assignment (no files created)
# - Preview distribution (no tasks.md created)
```

### Run First Production Test

```bash
# Run on limited data (5 files for testing)
python3 run_daily_processing.py --limit 5

# Monitor output for any errors
# Check workspace folder for results:
# /ENTITIES/DAILIES/Daily_Processing/2025-11-25_Collection/
```

### Verify Results

```bash
# Check workspace was created
ls "/Users/nikolay/Library/CloudStorage/Dropbox/ENTITIES/DAILIES/Daily_Processing"

# Should see:
# 2025-11-25_Collection/
#   ├── 01_Collected_Files/
#   ├── 02_Extracted_Tasks/
#   ├── 03_Gap_Analysis/
#   ├── 04_Task_Templates/
#   ├── 05_Distribution_Plan/
#   └── 06_Processing_Log.md
```

---

## Common Issues & Solutions

### Issue 1: "python3: command not found"

**Solution:**
```bash
# Try just 'python'
python --version

# Or install Python 3
# macOS: brew install python3
# Linux: sudo apt-get install python3
```

### Issue 2: "No module named 'anthropic'"

**Solution:**
```bash
# Install the package
pip3 install anthropic

# If pip3 not found, try:
python3 -m pip install anthropic
```

### Issue 3: "ANTHROPIC_API_KEY environment variable not set"

**Solution:**
```bash
# Set the key temporarily
export ANTHROPIC_API_KEY='your-key-here'

# Then run the script
python3 extract_tasks_batch.py

# To make permanent, add to ~/.zshrc or ~/.bashrc
echo 'export ANTHROPIC_API_KEY="your-key-here"' >> ~/.zshrc
source ~/.zshrc
```

### Issue 4: "Permission denied"

**Solution:**
```bash
# Make scripts executable
chmod +x *.py

# Or run with python3 explicitly
python3 collect_daily_files.py
```

### Issue 5: API Rate Limiting

**Solution:**
```bash
# Process in smaller batches
python3 extract_tasks_batch.py --limit 10

# Wait between batches
sleep 60  # Wait 1 minute
python3 extract_tasks_batch.py --limit 10
```

### Issue 6: "Workspace not found"

**Solution:**
```bash
# Run collection first
python3 collect_daily_files.py

# Then run other scripts
python3 extract_tasks_batch.py
```

---

## Directory Structure

### Expected Folder Structure

```
Dropbox/
├── ENTITIES/
│   └── DAILIES/
│       └── Daily_Processing/
│           ├── Daily_Processing_Workflow/
│           │   ├── Scripts/              ← You are here
│           │   │   ├── collect_daily_files.py
│           │   │   ├── extract_tasks_batch.py
│           │   │   ├── assign_tasks.py
│           │   │   ├── distribute_tasks.py
│           │   │   ├── run_daily_processing.py
│           │   │   ├── README.md
│           │   │   └── INSTALLATION.md (this file)
│           │   ├── Guides/
│           │   └── Support_Files/
│           ├── Archive/
│           └── YYYY-MM-DD_Collection/ (created by scripts)
└── Nov25/                               ← Employee folders
    ├── AI/
    ├── Design/
    ├── LG/
    ├── Video/
    ├── Sales/
    ├── Dev/
    └── HR/
```

---

## Daily Usage

### Morning Routine

```bash
# 1. Navigate to scripts folder
cd "/Users/nikolay/Library/CloudStorage/Dropbox/ENTITIES/DAILIES/Daily_Processing/Daily_Processing_Workflow/Scripts"

# 2. Ensure API key is set (one-time, persists)
echo $ANTHROPIC_API_KEY  # Should show your key

# 3. Run automation
python3 run_daily_processing.py

# Expected duration: ~27 minutes
# Expected output: Success messages for each step
```

### Alternative: Run Steps Individually

```bash
# Step 1: Collect files (2 min)
python3 collect_daily_files.py

# Step 2: Extract tasks (10 min)
python3 extract_tasks_batch.py

# Step 3: Assign tasks (10 min)
python3 assign_tasks.py

# Step 4: Distribute tasks (5 min)
python3 distribute_tasks.py
```

---

## Uninstallation

### Remove Python Packages

```bash
pip3 uninstall anthropic openai
```

### Remove API Keys

```bash
# Edit shell profile
nano ~/.zshrc  # or ~/.bashrc

# Remove line:
# export ANTHROPIC_API_KEY="..."

# Save and reload
source ~/.zshrc
```

### Remove Scripts (Optional)

```bash
# Delete scripts folder
rm -rf "/Users/nikolay/Library/CloudStorage/Dropbox/ENTITIES/DAILIES/Daily_Processing/Daily_Processing_Workflow/Scripts"
```

---

## Getting Help

### Documentation

- **Main README:** `README.md` (in same folder)
- **Milestone Docs:** `/ENTITIES/DAILIES/PLANS/Week_4/MLT-*.md`
- **Workflow Guide:** [GDS-001](../Guides/GDS-001_Daily_Task_Processing_Instructions.md)

### Support

- **Script Issues:** Check `README.md` troubleshooting section
- **API Issues:** Check provider documentation
  - Anthropic: https://docs.anthropic.com
  - OpenAI: https://platform.openai.com/docs

### Testing Before Production

```bash
# Always test with dry-run first
python3 run_daily_processing.py --dry-run

# Test with limited files
python3 run_daily_processing.py --limit 5

# Test without extraction (if API not ready)
python3 run_daily_processing.py --skip-extraction
```

---

## Security Best Practices

### API Key Security

- ✅ **DO:** Store in environment variables
- ✅ **DO:** Use shell profile (~/.zshrc)
- ❌ **DON'T:** Commit keys to git
- ❌ **DON'T:** Share keys in chat/email
- ❌ **DON'T:** Hard-code in scripts

### Key Rotation

```bash
# When rotating keys:
# 1. Get new key from provider
# 2. Update environment variable
export ANTHROPIC_API_KEY="new-key-here"

# 3. Update in shell profile
nano ~/.zshrc
# Replace old key with new key

# 4. Test
python3 extract_tasks_batch.py --limit 1
```

---

## Performance Tips

### Speed Up Processing

1. **Use Claude (faster than OpenAI):**
   ```bash
   python3 run_daily_processing.py --ai-provider claude
   ```

2. **Process in batches during testing:**
   ```bash
   python3 run_daily_processing.py --limit 20
   ```

3. **Skip extraction if already done:**
   ```bash
   python3 run_daily_processing.py --skip-extraction
   ```

### Reduce API Costs

1. **Test with dry-run (free):**
   ```bash
   python3 run_daily_processing.py --dry-run
   ```

2. **Use limit flag during development:**
   ```bash
   python3 extract_tasks_batch.py --limit 5
   ```

3. **Monitor usage:**
   - Check Anthropic console: https://console.anthropic.com
   - Check OpenAI usage: https://platform.openai.com/usage

---

## Checklist

### Installation Complete ✅

- [ ] Python 3.7+ installed
- [ ] pip3 working
- [ ] anthropic or openai package installed
- [ ] API key obtained from provider
- [ ] API key set in environment variable
- [ ] API key persisted in shell profile
- [ ] Test dry-run successful
- [ ] First production test (--limit 5) successful
- [ ] Full documentation read

### Ready for Production ✅

- [ ] All scripts tested individually
- [ ] Complete workflow tested (run_daily_processing.py)
- [ ] Results verified in workspace folder
- [ ] API costs monitored
- [ ] Training completed
- [ ] Emergency contact identified

---

**Installation Guide Version:** 1.0
**Last Updated:** 2025-11-25
**Next Review:** 2025-12-25

**Questions?** See README.md or contact AI & Automation Team
