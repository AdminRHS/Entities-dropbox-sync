# TASK: Setup Git & GitHub

ID: TASK-011

Category: Onboarding/Development/Git

Tags: [onboarding, git, github, version-control, development]

## Objective

Install Git and set up GitHub account for version control, code collaboration, and project management. Git is essential for developers and used by other departments for document version control.

## Steps

1. **Download Git**
   - Visit https://git-scm.com/downloads
   - Select your operating system
   - Download Git installer
   - Run the installer

2. **Install Git**
   - Follow installation wizard
   - Accept license agreement
   - Choose installation location (default recommended)
   - Select components:
     - ✅ Git Bash Here
     - ✅ Git GUI Here
     - ✅ Associate .git* files
   - Choose default editor (VS Code recommended)
   - Configure line ending conversions (recommend "Checkout as-is, commit Unix-style")
   - Complete installation

3. **Configure Git User Information**
   - Open Git Bash or terminal
   - Configure your name:
     ```
     git config --global user.name "Your Name"
     ```
   - Configure your email:
     ```
     git config --global user.email "your.email@example.com"
     ```
   - Verify configuration:
     ```
     git config --global --list
     ```

4. **Create GitHub Account**
   - Visit https://github.com/signup
   - Enter username (professional format)
   - Enter work email address
   - Create strong password
   - Complete account verification
   - Choose plan (Free plan is sufficient)

5. **Set Up SSH Key (Recommended)**
   - Generate SSH key:
     ```
     ssh-keygen -t ed25519 -C "your.email@example.com"
     ```
   - Press Enter to accept default file location
   - Enter passphrase (optional but recommended)
   - Copy public key:
     ```
     cat ~/.ssh/id_ed25519.pub
     ```
   - Add SSH key to GitHub:
     - Go to GitHub → Settings → SSH and GPG keys
     - Click "New SSH key"
     - Paste public key
     - Add descriptive title
     - Save key

6. **Test Git Installation**
   - Open terminal/Git Bash
   - Verify Git version:
     ```
     git --version
     ```
   - Test Git configuration:
     ```
     git config --list
     ```

7. **Set Up GitHub Desktop (Optional)**
   - Download GitHub Desktop from https://desktop.github.com/
   - Install GitHub Desktop
   - Sign in with GitHub account
   - Configure Git user information
   - Test cloning a repository

8. **Configure Git in VS Code**
   - Open VS Code
   - Git should be automatically detected
   - Verify Git is working:
     - Open any folder
     - Check Source Control panel
     - Initialize repository if needed

9. **Learn Basic Git Commands**
   - `git init` - Initialize repository
   - `git clone <url>` - Clone repository
   - `git add .` - Stage changes
   - `git commit -m "message"` - Commit changes
   - `git push` - Push to remote
   - `git pull` - Pull from remote
   - `git status` - Check status

10. **Set Up First Repository**
    - Create new repository on GitHub
    - Clone repository locally
    - Make initial commit
    - Push to GitHub
    - Verify repository appears on GitHub

11. **Configure Git Credentials**
    - Set up credential helper:
      ```
      git config --global credential.helper store
      ```
    - Or use GitHub CLI for authentication
    - Test authentication with push/pull

## Requirements

- Accounts needed:
  - GitHub account (can create during setup)
  - Work email (for GitHub account)
- Tools needed:
  - Internet connection
  - Administrator rights (for Git installation)
- Prerequisites:
  - TASK-002: Setup VS Code (recommended for Git integration)
  - Basic understanding of command line (helpful but not required)

## Cross References

- Related Course: COURSE-013 — Git & GitHub for Beginners (Original ID: 68dd0219b3a7f6de349119df)
- Related Task: TASK-002 — Setup VS Code (Git integration)
- Related Task: TASK-004 — Setup Cursor (Git integration)
- Additional Resources:
  - Git official documentation
  - GitHub official documentation
  - GitHub Desktop documentation

## Expected Outcome

After completing this task, you will have:
- Git installed and configured
- GitHub account created
- Git user information configured
- SSH key set up (if chosen)
- GitHub Desktop installed (optional)
- Git integrated with VS Code/Cursor
- Understanding of basic Git commands
- First repository set up
- Ready for version control workflows

## Notes

- **Git is essential** - Required for all development work
- **GitHub account** - Use work email for professional account
- **SSH keys** - Recommended for secure authentication
- **Git configuration** - Set user name and email globally
- **VS Code integration** - Git works seamlessly with VS Code
- **GitHub Desktop** - Optional GUI for Git operations
- **Basic commands** - Learn essential Git commands
- **Repository management** - Understand how to create and manage repos

## Common Issues and Solutions

**Issue: Git not recognized in terminal**
- Verify Git is installed
- Check PATH environment variable
- Restart terminal/IDE
- Reinstall Git if needed

**Issue: Cannot push to GitHub**
- Verify SSH key is added to GitHub
- Check authentication credentials
- Verify repository permissions
- Test SSH connection: `ssh -T git@github.com`

**Issue: Git credentials not saving**
- Configure credential helper
- Use GitHub CLI for authentication
- Set up SSH keys instead of HTTPS

## Next Steps

After completing Git & GitHub setup:
1. Complete Git & GitHub for Beginners course (COURSE-013)
2. Practice basic Git workflows
3. Learn branching and merging
4. Understand pull requests
5. Set up repository templates
6. Learn advanced Git features

