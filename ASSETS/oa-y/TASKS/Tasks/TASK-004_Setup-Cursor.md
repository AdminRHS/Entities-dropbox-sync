# TASK: Setup Cursor

ID: TASK-004

Category: Onboarding/Tools/Cursor

Tags: [onboarding, tools, development, ide, ai-editor, coding]

## Objective

Install and configure Cursor, an AI-powered code editor with integrated multiple LLM models for AI-assisted development. Cursor provides advanced AI features including Agents view, file-aware context, and built-in browser for local development.

## Steps

1. **Download Cursor**
   - Visit https://cursor.sh/
   - Click "Download" or "Get Started"
   - Select your operating system (Windows/Mac/Linux)
   - Download the installer

2. **Install Cursor**
   - Run the downloaded installer
   - Follow installation wizard prompts
   - Accept license agreement
   - Choose installation location (default is recommended)
   - Complete the installation
   - Launch Cursor when installation completes

3. **Sign in to Cursor**
   - Open Cursor application
   - Click "Sign In" or account icon (usually top-right corner)
   - Sign in with your work account credentials
   - If you have a Cursor Pro account provided by company, use those credentials
   - Complete authentication if required

4. **Configure basic settings**
   - Open Settings (Ctrl+, or Cmd+,)
   - Configure essential settings:
     - Enable Auto Save
     - Set default file encoding to UTF-8
     - Configure font size and family preferences
     - Enable word wrap for better readability
     - Set up file associations if needed

5. **Set up AI model preferences**
   - Navigate to Settings → AI Models
   - Configure available models:
     - **GPT-5** - For visual design analysis and comprehensive documentation
     - **Claude/Sonnet 4.5** - For component implementation
     - **Composer** - For code generation and editing
   - Set default model for different tasks
   - Configure API keys if using custom models

6. **Enable Agents view**
   - Navigate to View → Agents (or use keyboard shortcut)
   - Familiarize yourself with Agents interface
   - Understand how to create and manage agent tasks
   - Agents view enables task-based workflows

7. **Configure file referencing**
   - Learn to use @ symbol for file referencing
   - Practice referencing files in chat: `@filename.md`
   - Understand how Cursor maintains codebase-aware context
   - Test file referencing with sample files

8. **Set up workspace folder**
   - File → Open Folder
   - Navigate to your Dropbox work directory
   - Select your work folder
   - Verify folder structure displays in Explorer sidebar
   - Cursor will index files for AI context

9. **Configure Git integration**
   - Verify Git is installed on your system
   - Open integrated terminal (Ctrl+` or Cmd+`)
   - Test Git commands: `git --version`
   - Configure Git user if not already done:
     - `git config --global user.name "Your Name"`
     - `git config --global user.email "your.email@example.com"`
   - Verify Git integration in Cursor

10. **Set up built-in browser**
    - Understand Cursor's built-in browser feature
    - Learn to preview localhost development
    - Configure browser settings if needed
    - Test browser preview functionality

11. **Configure context management**
    - Understand how Cursor manages context across chats
    - Learn to maintain context for long conversations
    - Practice using context effectively
    - Configure context limits if needed

12. **Install essential extensions (optional)**
    - Open Extensions view (Ctrl+Shift+X or Cmd+Shift+X)
    - Consider installing:
      - **GitLens** - Enhanced Git capabilities
      - **Prettier** - Code formatting
      - **ESLint** - JavaScript linting (if working with JS)
      - **Python** - Python support (if needed)
      - **Markdown All in One** - Enhanced Markdown support

13. **Test basic functionality**
    - Create a test file (File → New File)
    - Type some code or text
    - Test AI chat functionality (Ctrl+L or Cmd+L)
    - Test Composer mode for code generation
    - Verify file appears in Explorer sidebar
    - Test saving files (Ctrl+S or Cmd+S)

14. **Familiarize yourself with key features**
    - **Chat (Ctrl+L / Cmd+L):** AI chat for questions and assistance
    - **Composer (Ctrl+I / Cmd+I):** Inline code editing with AI
    - **Agents View:** Task-based workflow management
    - **File References (@):** Reference files in chat for context
    - **Terminal:** Integrated terminal for commands
    - **Browser:** Built-in browser for localhost preview

## Requirements

- Accounts needed:
  - Cursor account (free tier available, Pro tier recommended)
  - Work account credentials (if company provides Cursor Pro)
- Tools needed:
  - Computer with internet connection
  - Administrator rights (for installation)
  - Git (optional, for version control features)
- Prerequisites:
  - TASK-002: Setup VS Code (recommended, but Cursor can replace VS Code)
  - Basic understanding of code editors
  - Internet connection for AI features

## Cross References

- Related Course: COURSE-006 — Cursor Fundamentals (Original ID: 6895eca862db728ad919c84e)
- Related Lesson: LESSON-006 — What Is Cursor (Original ID: 68a2dab2e9683ae5e6d5dd22)
- Related Lesson: LESSON-007 — Why Cursor Helps Beginners (Original ID: 68a2dab2e9683ae5e6d5dd23)
- Related Lesson: LESSON-008 — Installing Cursor (Original ID: 68a2dab2e9683ae5e6d5dd24)
- Related Lesson: LESSON-009 — Interface Overview (Original ID: 68a2dab2e9683ae5e6d5dd25)
- Related Lesson: LESSON-010 — Working Together in Cursor (Original ID: 68a2dab2e9683ae5e6d5dd2c)
- Related Task: TASK-002 — Setup VS Code (alternative IDE option)
- Additional Resources:
  - Cursor official documentation: https://cursor.com
  - Tool ID in taxonomy: TOOL-AI-041 (Cursor in taxonomy system)
  - Advanced Prompting course includes Cursor-specific lessons

## Expected Outcome

After completing this task, you will have:
- Cursor installed and configured on your computer
- AI models configured for different development tasks
- Workspace folder set up for your projects
- Understanding of Cursor's AI-powered features
- Ability to use Chat, Composer, and Agents view
- Knowledge of file referencing with @ symbol
- Integrated Git and terminal ready for use
- Foundation for AI-assisted development workflows

## Notes

- **Cursor vs VS Code:** Cursor can replace VS Code entirely, offering more powerful AI features
- **AI Models:** Cursor supports multiple models - configure based on your needs
- **Agents View:** Powerful feature for task-based workflows - explore after basic setup
- **File References:** Use @ symbol to reference files in chat for better context
- **Built-in Browser:** Useful for localhost development and preview
- **Context Management:** Cursor maintains context across conversations - use effectively
- **Pro Account:** Company may provide Cursor Pro accounts - check with HR/IT
- **Resource Usage:** AI features consume resources - monitor computer performance
- **Keyboard Shortcuts:** Learn shortcuts for Chat (Ctrl+L) and Composer (Ctrl+I) for efficiency

## Key Features Overview

### Chat (Ctrl+L / Cmd+L)
- Ask questions about your codebase
- Get explanations and help
- Reference files using @ symbol
- Maintains context across conversation

### Composer (Ctrl+I / Cmd+I)
- Inline code editing with AI
- Generate code based on instructions
- Edit existing code with AI assistance
- Multi-file editing capabilities

### Agents View
- Task-based workflow management
- Create and track agent tasks
- Manage complex development workflows
- Coordinate multiple AI interactions

### File Referencing (@)
- Reference files in chat: `@filename.md`
- Provide context to AI
- Codebase-aware assistance
- Multiple file references supported

## Next Steps

After completing Cursor setup:
1. Complete Cursor Fundamentals course (COURSE-006) for comprehensive training
2. Practice using Chat for code questions
3. Learn Composer mode for code generation
4. Explore Agents view for task management
5. Master file referencing with @ symbol
6. Customize settings to your workflow preferences
7. Integrate with your development projects

