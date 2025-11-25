# TASK: Setup VS Code

ID: TASK-002

Category: Onboarding/Tools/VSCode

Tags: [onboarding, tools, development, ide, editor, coding]

## Objective

Install and configure Visual Studio Code (VS Code) as your primary code editor and development environment. VS Code is essential for all development work, file management, and project organization at Remote Helpers.

## Steps

1. Download VS Code
   - Visit https://code.visualstudio.com/
   - Click "Download for Windows" (or Mac/Linux as appropriate)
   - Download the stable version installer

2. Install VS Code
   - Run the downloaded installer
   - Accept the license agreement
   - Choose installation location (default is recommended)
   - Select additional tasks:
     - ✅ Add to PATH (important for command line access)
     - ✅ Create desktop icon
     - ✅ Add "Open with Code" action to Windows Explorer
   - Complete the installation

3. Launch VS Code and verify installation
   - Open VS Code from desktop icon or Start menu
   - Verify VS Code opens successfully
   - Check Help → About to confirm version

4. Configure basic settings
   - Open Settings (Ctrl+, or Cmd+,)
   - Configure essential settings:
     - Enable Auto Save (File → Auto Save)
     - Set default file encoding to UTF-8
     - Enable word wrap for better readability
     - Configure font size and family preferences

5. Install essential extensions
   - Open Extensions view (Ctrl+Shift+X or Cmd+Shift+X)
   - Install recommended extensions:
     - **Live Server** - For local web development
     - **GitLens** - Enhanced Git capabilities
     - **Prettier** - Code formatting
     - **ESLint** - JavaScript linting (if working with JS)
     - **Python** - Python support (if needed)
     - **Markdown All in One** - Enhanced Markdown support

6. Set up workspace folder structure
   - Create or open your work folder in VS Code
   - File → Open Folder → Navigate to your Dropbox work directory
   - Verify folder structure displays in Explorer sidebar

7. Configure Git integration (if applicable)
   - Verify Git is installed on your system
   - Open integrated terminal (Ctrl+` or Cmd+`)
   - Test Git commands: `git --version`
   - Configure Git user (if not already done):
     - `git config --global user.name "Your Name"`
     - `git config --global user.email "your.email@example.com"`

8. Test basic functionality
   - Create a test file (File → New File)
   - Type some code or text
   - Save the file (Ctrl+S or Cmd+S)
   - Verify file appears in Explorer sidebar
   - Test opening files by double-clicking in Explorer

## Requirements

- Accounts needed: None (for basic setup)
- Tools needed:
  - Computer with internet connection
  - Administrator rights (for installation)
  - Git (optional, for version control features)
- Prerequisites:
  - None (this is typically one of the first onboarding tasks)

## Cross References

- Related Course: COURSE-002 — VS Code Fundamentals (Original ID: 689c457e62db728ad9f2ede1)
- Related Course: COURSE-003 — VS Code Launchpad (Original ID: 68d29f8cb3a7f6de34f7b1aa)
- Related Lesson: LESSON-001 — What Is VS Code? (Original ID: 68a2dab1e9683ae5e6d5dcd3f)
- Related Lesson: LESSON-002 — Installing VS Code (Original ID: 68a2dab2e9683ae5e6d5dd41)
- Related Lesson: LESSON-003 — Why VS Code Helps Beginners (Original ID: 68a2dab1e9683ae5e6d5dcd40)
- Additional Resources:
  - VS Code official documentation: https://code.visualstudio.com/docs
  - Tool ID in taxonomy: TOOL-DEV-### (VS Code)

## Expected Outcome

After completing this task, you will have:
- VS Code installed and configured on your computer
- Essential extensions installed for development work
- Workspace folder set up for your projects
- Understanding of basic VS Code interface and navigation
- Ability to create, edit, and manage files efficiently
- Foundation for advanced VS Code features and customization

## Notes

- VS Code is the primary development tool used across all departments
- Extensions can be installed later as needed for specific projects
- VS Code settings can be synced across devices using Settings Sync
- The integrated terminal allows running commands without leaving VS Code
- VS Code supports many programming languages out of the box
- Customize your workspace as you become more familiar with the tool

## Next Steps

After completing this setup:
1. Complete VS Code Fundamentals course (COURSE-002) for comprehensive training
2. Complete VS Code Launchpad course (COURSE-003) for advanced features
3. Explore VS Code keyboard shortcuts for improved productivity
4. Customize themes and appearance to your preference
5. Set up project-specific settings as needed

