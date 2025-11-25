# LG Team Setup Instructions - Complete Step-by-Step Guide

## Overview

This guide provides detailed instructions for setting up the essential tools for LG (Lead Generation) team members: Dropbox, VS Code/Cursor IDE, Claude Code Extension, and Git Bash. These instructions are extracted from the LG Dropbox call transcript and formatted for independent execution.

---

## Prerequisites

**Accounts Required:**

- LG Dropbox account (corporate subscription purchased - no device limit)
- LG Claude/Cloud account (purchased 30.10)
- LG account credentials for VS Code/Cursor

**Important Notes:**

- Claude Code Extension is purchased on: admin, Dev, Niko, HR, Sales, LG accounts (purchased 30.10)
- Cursor Pro is purchased on: admin, Dev, Niko, DD, LG accounts
- All LG team members should use LG account credentials for all tools
- Ensure stable internet connection before starting
- Estimated total setup time: 30-45 minutes

---

## Part 1: Dropbox Setup

### Step 1.1: Check Current Dropbox Status

1. Open Dropbox Desktop application
2. Check which account you're logged into (may be admin account or personal account)
3. Verify if you have access to "Nov 25" or "ELG NOV25" folders
4. Note: If you see many department folders you don't need, you're likely on admin account

### Step 1.2: Logout from Current Account

1. Right-click on Dropbox icon in system tray (bottom-right corner)
2. Click on your account name/email
3. Select "Logout" or "Sign out"
4. Confirm logout if prompted

### Step 1.3: Close Dropbox Completely

1. Right-click Dropbox icon in system tray
2. Select "Quit Dropbox" or "Close"
3. Wait for Dropbox to fully close (icon should disappear from tray)

### Step 1.4: Uninstall Dropbox Desktop

**For Windows:**

1. Press Windows key or click Start menu
2. Type "Settings" and open Settings app
3. Click on "Apps" (or "Apps & features")
4. In search box, type "Dropbox"
5. Find "Dropbox" application in the list
6. Click on it, then click "Uninstall"
7. Follow uninstall wizard prompts
8. **Important:** This removes locally downloaded files to free up disk space

**Alternative Method (Control Panel):**

1. Press Windows key + R
2. Type "control" and press Enter
3. Go to "Programs" → "Uninstall a program"
4. Find Dropbox, right-click, select "Uninstall"

### Step 1.5: Clean Up Remaining Files (Optional but Recommended)

1. Navigate to your Dropbox folder location (usually C:\Users\[YourName]\Dropbox)
2. Delete any remaining files/folders if they exist
3. This ensures clean reinstallation

### Step 1.6: Download Fresh Dropbox Installer

1. Open web browser
2. Go to Google and search "dropbox desktop"
3. Click on official Dropbox website result (dropbox.com)
4. Look for "Download" button
5. **Important:** Download the Desktop app, NOT the web version
6. Skip any prompts for web version
7. Save installer to Downloads folder or Desktop

### Step 1.7: Install Dropbox

1. Navigate to Downloads folder
2. Double-click the Dropbox installer file
3. Follow installation wizard:

- Click "Next" through initial screens
- Accept license agreement if prompted
- Choose installation location (default is fine)
- Click "Install"

4. Wait for installation to complete
5. Click "Finish" when done

### Step 1.8: Login with LG Account

1. Dropbox Desktop should launch automatically after installation
2. If not, search for "Dropbox" in Start menu and open it
3. Login window will appear
4. **Enter LG account credentials** (not admin, not personal)
5. Complete authentication if 2FA is enabled
6. Wait for Dropbox to initialize

### Step 1.9: Configure Selective Sync (CRITICAL)

1. After login, Dropbox will show sync options
2. Click "Choose folders to sync" or "Selective Sync"
3. **Select ONLY these folders:**

- ELG NOV25 (or "Nov 25" / "LG Nov 25" - exact name may vary)
- ELG (if available and needed)

4. **DO NOT select:**

- Other department folders (AI, Design, Dev, Video, etc.)
- Old archive folders
- Any folders you don't actively need

5. Click "OK" or "Update" to confirm
6. **Note:** Files with cloud icon (☁️) don't take local disk space. Only files you open will download locally.

### Step 1.10: Verify Dropbox Setup

1. Open File Explorer
2. Navigate to Dropbox folder
3. Confirm you see "ELG NOV25" or "Nov 25" folder
4. Open the folder and verify structure:

- Should see named folders for each team member
- Each folder should contain dated subfolders (03, 04, 05, etc.)

5. Check that files show cloud icon (not fully downloaded yet - this is normal)

---

## Part 2: IDE Setup (VS Code or Cursor)

### Step 2.1: Choose Your IDE

**Option A: VS Code (Free)**

- Recommended if you're comfortable with VS Code
- Free, widely used

**Option B: Cursor Pro (Paid - Available)**

- Recommended as it can replace VS Code
- More powerful AI features
- Already purchased for ELG team

**Decision:** Choose one. If unsure, start with VS Code. You can switch later.

### Step 2.2: Install VS Code (If Chosen)

1. Open web browser
2. Search "VS Code download" or go to code.visualstudio.com
3. Click "Download for Windows" (or your OS)
4. Save installer to Downloads
5. Run installer:

- Accept license agreement
- Choose installation location (default OK)
- Check "Add to PATH" (important)
- Check "Create desktop icon" (optional)
- Click "Install"

6. Click "Finish" when done

### Step 2.3: Install Cursor (If Chosen)

1. Open web browser
2. Search "Cursor IDE download" or go to cursor.sh
3. Download Cursor installer for Windows
4. Run installer:

- Follow installation prompts
- Accept defaults or customize as needed
- Complete installation

### Step 2.4: Login to IDE with LG Account

1. Open VS Code or Cursor
2. Look for account/login icon (usually top-right corner)
3. Click on it
4. If already logged in with different account:

- Click on account name
- Select "Sign Out" or "Logout"

5. Sign in with **LG account credentials**
6. Complete authentication if required

### Step 2.5: Open Dropbox Folder in IDE

1. In VS Code/Cursor, go to File → Open Folder (or Ctrl+K, Ctrl+O)
2. Navigate to Dropbox folder
3. Select "ELG NOV25" or "Nov 25" folder
4. Click "Select Folder"
5. IDE should now show your Dropbox folder structure in sidebar

---

## Part 3: Claude Code Extension Setup

### Step 3.1: Install Claude Code Extension

1. In VS Code or Cursor, click on Extensions icon (left sidebar - looks like four squares)
2. Alternatively, press Ctrl+Shift+X
3. In search box, type "Claude" or "Claude Code"
4. Find "Claude Code" extension (by Anthropic)
5. Click "Install" button
6. Wait for installation to complete

### Step 3.2: Authenticate Claude Code Extension

1. After installation, look for Claude icon in top-right corner of IDE
2. Click on Claude icon
3. A popup or browser window will open for authentication
4. **Login with LG account** (Claude/Cloud purchased on LG account on 30.10)
5. Complete authentication flow
6. You may see "Claude Subscription" confirmation

### Step 3.3: Verify Claude Extension Works

1. Open any file in your Dropbox folder (e.g., daily.md)
2. Click on Claude icon again
3. Type a test message in Claude chat
4. Verify you get a response
5. If error occurs, check account credentials match LG account

### Step 3.4: Restart IDE (Important)

1. Close VS Code/Cursor completely
2. Check system tray - ensure no instances running
3. Reopen VS Code/Cursor
4. Verify Claude extension still works after restart

---

## Part 4: Git Bash Installation

### Step 4.1: Download Git for Windows

1. Open web browser
2. Search "Git for Windows download" or go to git-scm.com/download/win
3. Look for "64-bit Git for Windows Setup" link
4. **Important:** Copy only the download link URL (the part between angle brackets: <https://...>)
5. Click the link or copy URL and paste in browser address bar
6. Download will start automatically

### Step 4.2: Install Git Bash

1. Navigate to Downloads folder
2. Find Git installer (usually named something like "Git-2.x.x-64-bit.exe")
3. Double-click installer
4. Follow installation wizard:

- Click "Next" through welcome screens
- Accept default components (Git Bash, Git GUI, etc.)
- Choose default editor (VS Code or Cursor if listed, otherwise default)
- Choose default branch name (default "main" is fine)
- Adjust PATH environment (default "Git from command line and also from 3rd-party software" recommended)
- Choose HTTPS transport backend (default OpenSSL)
- Configure line ending conversions (default "Checkout Windows-style, commit Unix-style" recommended)
- Configure terminal emulator (default MinTTY recommended)
- Choose default behavior of "git pull" (default recommended)
- Choose credential helper (default recommended)
- Configure extra options (defaults OK)
- Enable experimental features (optional, defaults OK)

5. Click "Install"
6. Wait for installation to complete
7. Click "Finish"

### Step 4.3: Verify Git Bash Installation

1. Press Windows key
2. Search "Git Bash"
3. Open Git Bash application
4. A terminal window should open with command prompt
5. Type `git --version` and press Enter
6. Should display Git version number (confirms installation successful)
7. Close Git Bash for now

**Why Git Bash is Needed:**

- Claude Code Extension uses Git Bash to execute local commands
- When Claude agent needs to create folders/files, it triggers Git Bash commands
- This enables automated file operations

---

## Part 5: Account Access Summary

### Account Information Reference

**Claude/Cloud Accounts (Purchased 30.10):**

- Available on: admin, DW, NIKA, HR, Sales, **LG**
- **LG team members should use LG account**

**Cursor Pro Accounts:**

- Available on: admin, DW, NIKA, ADD, **ELG**
- ELG team has access to Cursor Pro

**Dropbox Accounts:**

- LG team has corporate Dropbox subscription
- No device limit (previously limited to 3-4 devices)
- All LG members should use LG Dropbox account

### Account Login Checklist

- [ ] Dropbox: Logged in with LG account
- [ ] VS Code/Cursor: Logged in with LG account  
- [ ] Claude Code Extension: Authenticated with LG account
- [ ] All tools verified working with LG credentials

---

## Part 6: Verification and Testing

### Step 6.1: Verify All Installations

Check each component:

**Dropbox:**

- [ ] Dropbox Desktop running in system tray
- [ ] Logged in with LG account
- [ ] Can see "ELG NOV25" folder
- [ ] Files show cloud icon (not fully synced yet - normal)

**IDE (VS Code/Cursor):**

- [ ] IDE opens successfully
- [ ] Logged in with LG account
- [ ] Can open Dropbox folder in IDE
- [ ] See file structure in sidebar

**Claude Code Extension:**

- [ ] Extension installed and visible
- [ ] Claude icon appears in IDE
- [ ] Can open Claude chat
- [ ] Can send/receive messages in Claude

**Git Bash:**

- [ ] Git Bash opens successfully
- [ ] `git --version` command works
- [ ] No error messages

### Step 6.2: Test Workflow

1. Open your personal folder in "ELG NOV25" (find your name)
2. Open today's date folder (e.g., "05")
3. Open "daily.md" file
4. In Claude chat, ask: "Can you help me edit this file?"
5. Verify Claude responds
6. This confirms all components work together

---

## Troubleshooting

### Issue: Dropbox shows "Syncing..." for too long

**Solution:**

- Files with cloud icon don't download until opened - this is normal
- Only open files you need to work with
- Check internet connection

### Issue: Can't login to Claude Extension

**Solution:**

- Verify you're using LG account (not personal or admin)
- Check that Claude was purchased on LG account (30.10)
- Try logging out and back in
- Restart IDE

### Issue: Git Bash not found

**Solution:**

- Verify installation completed successfully
- Check if Git Bash appears in Start menu
- May need to restart computer after installation
- Reinstall Git for Windows if needed

### Issue: IDE won't open Dropbox folder

**Solution:**

- Verify Dropbox folder exists in File Explorer
- Check that you have read/write permissions
- Try opening parent folder first, then navigate to ELG NOV25

### Issue: Multiple Dropbox folders on computer

**Solution:**

- This happens if Dropbox was installed multiple times
- Check all Dropbox locations and delete old ones
- Keep only the current installation location

---

## Post-Setup Next Steps

### 1. Read Your Read Me File

- Navigate to your personal folder in ELG NOV25
- Open "Read Me" file
- Read instructions about daily.md, plan.md, and task.md files
- Understand the workflow: daily → plans → tasks

### 2. Watch Training Video

- Video will be shared in main Discord chat
- ~3:40 minutes long
- Shows complete workflow demonstration
- Watch before starting work

### 3. Practice with Dropbox Chat Agent

- In Dropbox, click chat icon (top-right, next to search)
- This is the Dropbox AI agent
- Can help create folders, move files, fill templates
- Test by asking it to create a test folder

### 4. Understand File Structure

- Each team member has named folder
- Inside: dated folders (03, 04, 05, etc.) for each work day
- Each date folder contains: daily.md, plan.md, task.md templates
- Fill daily.md with your activities, then generate plans and tasks

---

## Support and Resources

**If you encounter issues:**

1. Check this guide first
2. Review troubleshooting section
3. Ask in team Discord channel
4. Contact setup support person (assigned during group sessions)

**Important Reminders:**

- Always use LG account for all tools
- Files with cloud icon don't take disk space (only opened files download)
- Sync only necessary folders to save disk space
- Restart IDE after installing Claude extension
- Git Bash is required for Claude agent to work with files

---

## Quick Reference Checklist

Use this checklist to track your setup progress:

- [ ] **Dropbox:**
  - [ ] Logged out from old account
  - [ ] Uninstalled old Dropbox
  - [ ] Installed fresh Dropbox
  - [ ] Logged in with LG account
  - [ ] Configured selective sync (ELG NOV25 only)
  - [ ] Verified folder structure visible

- [ ] **IDE (VS Code or Cursor):**
  - [ ] Installed chosen IDE
  - [ ] Logged in with LG account
  - [ ] Opened Dropbox folder in IDE
  - [ ] Verified file structure visible

- [ ] **Claude Code Extension:**
  - [ ] Installed extension
  - [ ] Authenticated with LG account
  - [ ] Restarted IDE
  - [ ] Tested Claude chat functionality

- [ ] **Git Bash:**
  - [ ] Downloaded Git for Windows
  - [ ] Installed Git Bash
  - [ ] Verified installation (git --version works)

- [ ] **Verification:**
  - [ ] All tools working together
  - [ ] Read Read Me file
  - [ ] Watched training video
  - [ ] Tested basic workflow

---

**Setup Complete!** You're now ready to start using the LG team workflow system.

