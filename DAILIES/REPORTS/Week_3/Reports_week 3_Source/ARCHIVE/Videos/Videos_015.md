# VS Code gets 6 NEW Game-Changing AI Features & VS Code Agent Mode

### 1. Metadata Section
- **Video Title**: VS Code gets 6 NEW Game-Changing AI Features
- **Channel/Creator**: James Montemagno & Vlad Vlot (content from two separate videos is concatenated)
- **Video URL**: https://youtu.be/0D__JqyaUYA?si=zQniZfhwystxTX54
- **Duration**: 10:56
- **Publication Date**: Not Provided

### 2. Description Section
- **Description**: This video showcases several new and experimental AI-powered features in Visual Studio Code, primarily focusing on GitHub Copilot's Agent Mode. It covers how to discover and install MCP Servers to extend agent capabilities, how to configure agent behavior with allow/deny lists and max request limits, a feature to temporarily snooze code completions, and how to automatically generate custom instructions for a project. A second segment demonstrates a practical use case of Agent Mode by building a complete to-do list web application using Python and Django from scratch, highlighting the iterative development process with an AI agent.
- **Key Topics**:
  - VS Code AI Features
  - GitHub Copilot Agent Mode
  - MCP (Model Control Protocol) Servers
  - Terminal Command Allow/Deny Lists
  - Agent Request Limits
  - Generating Custom Instructions
  - Snoozing Code Completions
  - Building a Python/Django app with an AI Agent
- **Links Referenced**:
  - [awesome-copilot GitHub Repo](https://github.com/awesome-copilot/): A repository for custom chat modes, instructions, and prompts for GitHub Copilot.
  - [VS Code MCP Servers Page](https://code.visualstudio.com/insider/mcp): A marketplace to discover and install MCP Servers for agent mode.

### 3. Word-for-Word Transcription

**Speaker 1: James Montemagno**

[00:00] New AI features are being added to VS Code every single day just about. And I want to show you five, yes, five. Okay, actually six if you stick around for a bonus one at the end. New features that I think you're absolutely going to love that change the way that you use agent mode and code completions every single day inside of VS code. So let's get into it.

[TEXT: DEV TIPS TECH TUTORIALS JM James Montemagno]

[00:31] All right, let's talk about MCP servers. First and foremost, it's easier to see what you have installed either inside your project or as a user inside of VS Code and also install them. If you go over to extensions, you can see of course your installed and recommended extensions, but you also see a new MCP server section here. Now I don't have any installed at a user level or inside of my project. So I can click on this MCP servers.

[00:54] This will bring me to the VS code page where I can browse different MCP servers available. Now, there's of course tons available out there, but it's kind of a curated list of things like GitHub, Docs, markdown, Hugging Face, Notion, Zapier, Memory, Firecrawl, Clarity, Stripe, Azure DevOps, Azure. Let's go ahead and install GitHub. So I want to have at my root all the time.

[01:14] So I'm going to say install GitHub. It's going to open up VS Code and give me this nice page to explore the MCP server. So I can actually browse all of it here, manifest, go to the repo, everything like that. It's kind of like an extension, right? And it even shows me how to show, uh, set it up here. But I can just click install. And boom, it's here, right? It's awesome. I can go ahead and at any time go into settings. I can say start server, show output, configuration, model access and more.

[01:40] So I'm going to say start server and then it'll just log me into GitHub just like that. And now when I go to my tools, I can see all of them built in and my GitHub MCP server. So I have everything authenticated just like that. Now, this isn't creating a new mcp.json file in my .vs code folder.

[02:01] I can go up here and say MCP. And when I do that, I'll see list server, browse resources, reset cache tools, trust, show installed servers, list servers. Now I'm going to see the open workspace folder or open user configuration. The workspace is the one that I just talked about, mcp.json. But the open user configuration is one that's sort of in the application root for any time I use VS code anywhere and that's where it's configured automatically. So I can see it right there. Of course, if I don't want it there, I can just copy and paste this directly into a new mcp.json file. Anyways, MCP servers easier to install than ever.

[02:35] [TEXT: TERMINAL ALLOW OR DENY LIST]
[02:39] When I'm using agent mode, I'm often adding new features, functionality, fixing bugs, and doing a lot more. And I often want it to build the solution or projects and run tests. So when I do this normally, let's see what happens. So if I come in and say, how do I build this solution? What are the commands? Right, so I'm just going to ask it what it is.

[03:00] And it's going to tell me here probably to build it, do a dotnet restore, a dotnet build, a dotnet run. So I could say, okay, let's build it. So now what it's going to say is, okay, cool, dotnet build. Let's run this command, which is something that would do all the time, but it's going to ask me to continue. You don't really need to ask me to build the project if you're implementing stuff, just go ahead and build it. So now, if you go into settings, if you go ahead and go down to extensions and go down to GitHub Copilot under experimental, in this case, it may be in preview or automatic and stable by the time you watch this, but there is a new allow list and a deny list. So you can specify what commands you want it to automatically run without any prompting.

[03:42] So if I go in and say add, dotnet build, and hit okay here. Now we can go back and I could say, let's build it. And now it will automatically run that build. This is so nice when working with agent mode to specify what commands you want it to automatically run. It's super nice to go in, have your allow list and your deny list, anything that you want. So PowerShell, bash, anything like that, specify them here. So I have .NET build, .NET run, .NET test, have everything automatically set up.

[04:16] [TEXT: AGENT MAX REQUESTS]
[04:20] Okay, one of my other favorite features is a new setting. Just go into your settings and say max requests. All right. This is key. This defaults to 20. So when you're working in agent mode, you often have it have long-running operations. The default for max request before it asks you to continue is 20. Set it higher. I set it to 100. Set it to 10,000. Just whatever you want. It'll just keep going and keep grinding until it finishes. It'll never ask you for continue ever again. Combine that with the allowed deny list and that is a game changer.

[04:56] [TEXT: GENERATE CUSTOM INSTRUCTIONS]
[04:59] All right, I showed this other one in another video, but I'm going to tell you again. Go into your settings of the agent mode, hit generate instructions. This will automatically go through and analyze your entire code base. It will create and or update your co-pilot instructions, giving it a full overview of everything in your project, how to run it, how to add features, and a whole lot more. It will analyze your best practices, your coding conventions, and a lot more. So every time you make a call with agent mode, it will automatically send these and then you can specify them even more details if you want to. As you make changes to your project, go back in, go inside of here, play around, hit generate instructions again. You can run it with different models, anything that you want. It's basically running a big prompt and it is a game changer when working with co-pilot instructions inside of VS Code or Visual Studio or anywhere that you're using co-pilot.

[06:02] [TEXT: PAUSE CODE COMPLETIONS]
[06:06] Okay, I love code completions. When I'm typing code, which I still do, I say group dot and it automatically fills in this ghost text, this code completion recommendation that I can just tab, tab, tab, tab, tab and go, go, go, go, go. Sometimes you're in a flow, you might be demoing, you want to do something. You can now click this little co-pilot icon down here and you can configure if you want code completions on for all files, the type of file you're in, if you want next edit suggestions, or what I like is this little snooze button. You can add 5 minutes at a time so you can automatically snooze the code completions. So now if I come back over and I say group dot, I don't get any code completions coming in so I can just write, I still get my intelligence, I still get everything that I want, but now I'm just back in the flow. I can come back in, I see this little Z right there. If I tap on it again, I can go ahead and cancel, come back in, and now I'll start to get my code completions again coming in just like that, which is super awesome.

[07:04] [TEXT: GPT 4.1 BEAST MODE]
[07:07] Okay, the last thing I want to talk about is the awesome copilot repo on the GitHub org. Has a bunch of custom instructions and prompts and custom chat modes which basically let you identify behaviors for tools when working with agent mode. So things for example like planning mode or DBA or PRD type chat creation inside of here, refining requirements or issue chat, and you can basically scope down what tools are available and give it additional instructions when working in that mode. My favorite is this one from Burke Holland, 4.1 Beast mode, which for all intents and purposes gives when working with GPT 4.1 additional behaviors that do much more in-depth planning and execution. So it goes through and he worked really close looking at all the open AI documentation and identified this workflow and understanding what it needs to do. So let's go ahead and put this chat mode in. I'm going to go to raw, I'm going to copy this, I'm going to go over into my build, and I'm going to say settings, modes, and then I can add a new chat mode file in my .github/chatmodes here. and I'm going to say beast mode. You can even add them like system wide and paste that in. Okay, so now I just have a single product endpoint here. Let me say, let's add a new user endpoint and create a new web UI in the front end for managing them. Now here, I could use just normal agent mode, but I'm going to go into the agent mode custom beast mode. Now I can still select the different models, but I'm going to go ahead and select just 4.1 that it's been optimized for and hit go. Now what I like about this is that 4.1 is going to now identify all the steps that it needs. It's identified eight different steps that it needs to execute, like data entities, product data context, the endpoints, the program file, and a lot more. And it's going to go and update along the way of everything that it is doing. So this is really, really neat as it adds files. And this has been a complete game changer for me when I'm working with agent mode and 4.1 because it is super duper quick.

[09:20] Those are just some of my new favorite features when working with agent mode and code completions inside of VS Code, but there are so many to explore. What are your favorite features? Let me know in the comments below. If you enjoyed this video and you've tried out some of the features, give it a thumbs up, share it with a friend, and don't forget to subscribe, jam that notification bell so you get notified every time I put out new videos right here on YouTube. So until next time, I'm James. Thanks for watching.

**Speaker 2: Vlad Vlot**

[10:00] If you are using VS Code and you want to supercharge your development, watch this video till the end because we are going to talk about VS Code agent mode.

[10:12] Hey guys, my name is Vlad, and welcome back to my channel. Thank you so much for coming back, and thank you so much for your support. In this video, we're going to talk about new functionality inside VS Code, and it's called VS Code agent mode. Imagine having an AI assistant that could not only suggest the code, but also understand complex tasks, help you execute different commands, understand your code base, debug application, and much more. And this is what AI agent is about. If you want to deep dive with me in this mode, I recommend you watch this video till the end because it's really useful if you are ready, then let's get started.

[10:55] So what exactly is VS Code agent mode? Think of it as an autonomous AI pair programmer integrated directly into your VS Code editor. Unlike traditional code completion or simpler AI chat interactions, AI agent mode is designed for multi-steps complex coding tasks. Basically, you give agent mode a high-level task in plain English. For example, you can ask an agent to create for you new website or improve existing website. It doesn't have to be a website, it could be any code base. Basically, AI agent will analyze your request, try to look at your code base, then it will plan the work, and then it will start to write the code. Depending on the settings, it could ask you different questions. It will suggest you to set up different dependencies and shows you what it's going to do next. And the good things, you can control all the steps or you can allow the agent do its on its own. If you ever worked with Firebace Studio or Replit or Cursor AI, it's a similar thing. To get started, you need to have the latest VS Code. You can download it from VS Code website. It's available for Mac, Windows, and Linux. And you also need access to GitHub Copilot. It is an AI-powered code assistant. And if you don't have Copilot, you can subscribe for free plan.

[12:16] Okay, let's get started. Uh open VS Code. Then in the left panel, click on the extension button and search for Copilot extension. You would need to set up Copilot and Copilot chat. After that at the top of the screen and at the bottom right hand corner, you will see Copilot icon. To use Copilot, you would need to have GitHub account. If you don't have one, you have to create it. Then inside the extension, log into your GitHub account. You don't see it in my screen because I already logged in, but if you will click on the Copilot icon, you will see that you have to sign up first. Once you log in, you can open the chat. This is Copilot chat. Currently it is in ask mode. Let me make it a bit bigger. Inside the chat at the bottom section, you will see the small menu. This menu, you can select different AI models. In my case, I have only two models available, and you also can change the mode of the chat. And as you could see in my case, I have three options, ask, edit, and agent. If you don't see agent in your list, you need to turn it on. Go to the settings, search for the agent, and then turn on this checkbox. And then after that it will be available in the menu.

[13:31] Okay, let's go back to the chat, then select the agent from the drop down menu. And then in the chat window, write your first prompt. For example, we can ask agent to create for us to-do application using Python and Django framework. Ideally, to give to the agent better prompt, but in this tutorial, I intentionally give the simple prompt just to show you how you can adjust the application by providing additional details later. Once you finish with your prompt, press submit and then follow the instructions on your screen. Most of the time, you just have to click the continue button. And in some cases, you would be required to run some command inside the terminal. For instance now, agent suggests to create new folder for the my application. It should be an empty folder. So let me delete some file from my current folder and let me rerun the prompt again. To rerun the prompt, I simply click this button and then you will see the agent in action. It will try to understand the current environment setup and suggest some dependency or additional tools to install it. All you need, just press the continue button. Sometimes it could be even some extensions for VS Code. Press the continue button and wait for the next step. As you could see, the agent suggests me to install Django framework because it's not available on my computer. All you need, just continue, press continue. Sometimes you will see the error in the terminal, and the good things is that VS Code can catch this error and suggest the fix. So you don't have to copy and paste the error. VS Code and Copilot see everything. Maybe some of you think that it's not ideal scenario when you have to read through each uh step and press continue all the time. There's actually settings that uh allows you to uh make the agent do everything on its own without your confirmation, but I wouldn't recommend you to use these settings because we want to control the things that's going on. So it's safer to click continue button. Okay, so we set up the virtual environments and we set up Django framework. Let's say to agent uh to continue. I will speed up the video a little bit because at current steps we just have to press the continue and accept the suggestions from agent. Okay, seems our application is ready. Let's uh use the command that agent suggests to run the server. Okay. Uh let's open the URL and see our application. You can click on this URL or you can copy and paste it in your browser. Here you go. As you could see, it's so funny. It's not to-do list application yet. So, let's uh adjust the prompt and ask an agent to actually add the functionality of to-do list. All you need to do, just open the chat again and explain to the agent what's wrong with the application and ask what it should does for you. Like I mentioned in my first step, uh the prompt is quite important. The more descriptive you prompt, the better result you will get. Otherwise, you would need to communicate with the agents uh through multiple iterations to get the desired result.

[16:49] Okay, let me speed up the video a little bit again. Okay, seems the agent finished its work, and let's see the result. Let's refresh the page. And as you could see, right now, it looks a little bit better. At least we have some functionality. Let's check if it's actually working. Okay, seems it's working. I can see the uh the task in my to-do list. So, let's try to delete the task. Okay, seems this functionality is working. However, the application looks a little bit ugly. So, I would go back to the chat and try to improve the visual part of this application. I will tell to the agent add bootstrap styling and make the application is prettier. And let's see for the result. Okay, seems the agent finished its work, and let's check the result. And as you could see, this time my application looks a bit better. The agent added uh bootstrap styling, and let's check the functionality. I will try to add some task in my to-do list. And seems everything is working fine. This is my simple to-do application that I've made with Django just in about 10 minutes. It is really simple example, but as you could see, it's demonstrate for you the power of the agent. Of course, during your development, everything could goes not that smooth as in my example. Maybe also sometimes you would need to track the changes in the different files. And to do that, you can use this menu. This menu allows you to jump between different change in different files. You can accept the change or you can undo the change. If you want to accept all changes at once, you just click this button.

[18:05] If you will be interested to continue explore the agent inside VS Code, the next time I could talk about tools and MCP servers. Just let me know in comments below if you are interested. And if I will have a lot of requests, I will create a separate video about the tools and MCP servers. And that's it. As you can see, it's really powerful, it's so easy to use and you can try it absolutely free. If you like this video, please click like. If you don't like this video, it's okay. Please share with me your feedback in comments below and I will try to do my best to improve my future videos. Subscribe to my channel if you haven't subscribed yet. Watch my other videos because they're really useful. And I hope to see you in my next videos. Bye.

---

## TAXONOMY EXTRACTION REQUIREMENTS

### 4. Workflows Identification

```
WORKFLOW: Discover and Install an MCP Server
OBJECTIVE: To extend the capabilities of GitHub Copilot's Agent Mode by adding tools for external services like GitHub.
STEPS:
  1. Navigate to the Extensions tab in VS Code.
  2. Select the "MCP SERVERS" section.
  3. Click the link to browse for available MCP servers on the Visual Studio Code website.
  4. Select a server (e.g., GitHub) and click "Install".
  5. Allow the browser to open the link in VS Code.
  6. Click the "Install" button within the VS Code extension page for the MCP Server.
  7. Right-click the newly installed server in the MCP SERVERS list and select "Start Server".
  8. Authenticate with the required service (e.g., GitHub).
  9. Verify the new tools are available in the Copilot chat tool selection.
DURATION: 2-3 minutes
COMPLEXITY: Low
TOOLS USED: VS Code, GitHub Copilot, Web Browser
INPUT: A need to interact with an external service via Agent Mode.
OUTPUT: An installed and running MCP server, providing new tools to the Copilot agent.
```

```
WORKFLOW: Automate Terminal Commands in Agent Mode
OBJECTIVE: To allow Copilot Agent to run specific, trusted terminal commands without requiring user confirmation for each execution.
STEPS:
  1. Open VS Code Settings.
  2. Navigate to Extensions > GitHub Copilot Chat > Experimental.
  3. Locate the "Agent: Terminal: Allow List" setting.
  4. Click "Add Item".
  5. Enter the command you wish to auto-approve (e.g., `dotnet build`).
  6. Save the settings.
  7. In Agent Mode, issue a prompt that would trigger the command (e.g., "let's build it").
  8. Observe the command running automatically in the terminal without a confirmation prompt.
DURATION: 1-2 minutes to configure
COMPLEXITY: Low
TOOLS USED: VS Code Settings, GitHub Copilot Agent Mode
INPUT: A repetitive terminal command that requires confirmation in Agent Mode.
OUTPUT: The specified command runs automatically when invoked by the agent, speeding up the workflow.
```

```
WORKFLOW: Generate Custom Project Instructions for Copilot
OBJECTIVE: To automatically analyze a codebase and create a detailed instruction file (`copilot-instructions.md`) to give the Copilot agent project-specific context.
STEPS:
  1. Open the Copilot Chat panel in VS Code.
  2. Click the settings/sparkle icon.
  3. Select "Generate Instructions" from the menu.
  4. Wait for Copilot to analyze the entire codebase.
  5. Review the newly created or updated `.github/copilot-instructions.md` file.
  6. The file now contains a project overview, architecture details, developer workflows, and coding conventions.
  7. Use Agent Mode with the enhanced context for more accurate and relevant responses.
DURATION: 1-5 minutes depending on project size
COMPLEXITY: Low
TOOLS USED: VS Code, GitHub Copilot Agent Mode
INPUT: An existing codebase/project.
OUTPUT: A detailed `copilot-instructions.md` file that provides deep context about the project to the AI agent.
```

```
WORKFLOW: Create a To-Do App with VS Code Agent Mode
OBJECTIVE: To build a functional web application from scratch using an AI agent with iterative prompts.
STEPS:
  1. Open an empty folder in VS Code.
  2. Activate Agent Mode in Copilot Chat.
  3. Provide an initial high-level prompt: "create a complete to-do app using python language and django framework".
  4. Follow agent instructions, such as installing Python extensions and dependencies.
  5. Allow the agent to create the project structure, models, views, and templates.
  6. Run the application to verify the initial result.
  7. Provide a follow-up prompt to improve the UI: "add bootstrap styling and make the application prettier".
  8. Provide another prompt to add functionality: "add authentication support and dark and light theme".
  9. Follow agent steps to create a superuser and test the login functionality.
DURATION: 10-15 minutes
COMPLEXITY: Medium
TOOLS USED: VS Code, GitHub Copilot Agent Mode, Python, Django, Web Browser
INPUT: An empty folder and a high-level prompt.
OUTPUT: A functional to-do list web application with a database, user authentication, and styled UI.
```

### 5. Action Verbs & Operations

#### A. CREATION VERBS (Making new things)
- Create
- Build
- Generate
- Set up
- Write
- Develop
- Add

#### B. MODIFICATION VERBS (Changing existing things)
- Edit
- Change
- Fix
- Update
- Configure
- Copy
- Paste
- Refine
- Improve
- Adjust
- Set

#### C. ANALYSIS VERBS (Understanding/Evaluating)
- See
- Show
- Browse
- Explore
- Review
- Analyze
- Check
- Investigate
- Read
- Understand
- Identify
- Validate
- Watch

#### D. ORGANIZATION VERBS (Structuring/Managing)
- Manage
- Plan
- Organize
- Scope down

#### E. COMMUNICATION VERBS (Sharing/Presenting)
- Show
- Tell
- Ask
- Share
- Report
- Specify
- Explain

#### F. BROWSER/AGENTIC OPERATIONS (AI Agent & Automation Actions)
- Opens
- Clicks
- Navigates
- Runs
- Executes
- Asks
- Logs in
- Suggests
- Applies
- Fills in
- Automates
- Installs
- Authenticates
- Goes through

#### G. DATA OPERATIONS (Processing, Transforming, Moving Data)
- Extract
- Convert
- Copy
- Paste
- Fetch
- Update

### 6. Task Chains

```
TASK CHAIN: MCP Server Setup
Navigate to Extensions → Browse MCP Servers website → Click "Install" in browser → Open in VS Code → Click "Install" in VS Code → Start Server → Authenticate → New tools available for agent
```
```
TASK CHAIN: Automated Build
Ask agent to build → Agent prompts for permission → User configures "Allow List" in settings → Ask agent to build again → Agent automatically runs `dotnet build` in terminal
```
```
TASK CHAIN: Iterative App Development with AI Agent
Initial prompt (create to-do app) → Agent creates basic version → User provides feedback (add styling) → Agent adds Bootstrap CSS → User provides feedback (add auth) → Agent implements login system → A styled, functional app is created
```
```
TASK CHAIN: Generating Project Context for AI
Click "Generate Instructions" in Copilot → Agent analyzes entire codebase → Agent creates/updates `copilot-instructions.md` → Agent has improved project context for future tasks
```

### 7. Responsibilities Vocabulary

#### Professional Roles Mentioned:
- User
- Developer
- Pair Programmer
- Database Administrator (DBA)
- Prompt Engineer
- Strategic Planning & Architecture Assistant

#### Responsibilities/Activities:
- "using agent mode"
- "using code completions"
- "installing MCP servers"
- "configuring agent mode"
- "adding new features"
- "fixing bugs"
- "building the solution"
- "running tests"
- "generating instructions"
- "analyzing the codebase"
- "typing code"
- "managing users"
- "debugging your application"

#### Skills Mentioned:
- Coding
- Debugging
- Strategic planning
- Prompt engineering
- In-depth planning and execution

### 8. Tools & Technologies Matrix

| Tool Name | Category | Purpose | Used For | Mentioned With |
|---|---|---|---|---|
| Visual Studio Code (VS Code) | Code Editor | The primary development environment | All coding and agent interaction tasks | GitHub Copilot, MCP Servers |
| GitHub Copilot | AI Assistant | AI-powered code completion and agentic tasks | Code completions, Agent Mode, generating instructions | VS Code, GPT-4.1, MCP Servers |
| MCP Servers | Agent Extension | Extend agent capabilities to external services | Connecting to databases, invoking APIs, specialized tasks | GitHub Copilot Agent Mode |
| GitHub MCP Server | MCP Server | Provides agent tools to interact with GitHub APIs | Accessing repos, issues, pull requests | VS Code, Copilot Agent Mode |
| .NET | Framework | Software development framework | Building the example application | `dotnet build`, `dotnet run` |
| GPT-4.1 | AI Model | The language model powering advanced agent features | "Beast Mode" custom chat mode | GitHub Copilot |
| Python | Programming Language | General-purpose programming | Building the to-do list application | Django, VS Code Agent Mode |
| Django | Web Framework | A Python-based web framework | Creating the backend for the to-do list app | Python, VS Code Agent Mode |
| awesome-copilot | Resource | GitHub repository | Storing and sharing custom chat modes and instructions | GitHub Copilot |
| Bootstrap | CSS Framework | Front-end styling | Improving the visual design of the generated web app | Django, HTML |

### 9. Objects & Deliverables

- `mcp.json` configuration file
- `.github/copilot-instructions.md` file (custom instructions)
- `.github/chatmodes/` directory and files
- A complete to-do list web application (built with Python/Django)
- `User` data model
- API endpoints (for products, users)
- Web UI (frontend for managing users)
- Code completions (ghost text)
- Terminal commands

### 10. Integration Patterns

```
INTEGRATION: VS Code + GitHub Copilot
PURPOSE: Provide AI-assisted development directly within the editor.
FLOW: User types code → Copilot provides ghost text suggestions → User accepts. OR User opens chat → Issues command in Agent Mode → Copilot acts on files/terminal.
```
```
INTEGRATION: GitHub Copilot Agent Mode + MCP Servers (e.g., GitHub)
PURPOSE: Extend the agent's capabilities beyond the local workspace to interact with external APIs and services.
FLOW: User installs GitHub MCP Server → Agent gains new tools (e.g., `githubRepo`) → User can ask agent to perform actions on GitHub repositories.
```
```
INTEGRATION: GitHub Copilot Agent Mode + Custom Instructions (`copilot-instructions.md`)
PURPOSE: To provide deep, project-specific context to the AI, improving the accuracy and relevance of its actions.
FLOW: User triggers "Generate Instructions" → Copilot analyzes the project and creates a detailed markdown file → On subsequent agent requests, Copilot uses this file as foundational knowledge.
```
```
INTEGRATION: VS Code Agent Mode + Python/Django
PURPOSE: To automate the creation of a full-stack web application from a high-level prompt.
FLOW: User prompts agent to create app → Agent uses terminal to set up Python virtual environment and install Django → Agent creates and edits `.py` and `.html` files for models, views, and templates → A runnable web app is produced.
```

### 11. Business Concepts & Strategy

- **Developer Productivity**: The core theme is using AI to accelerate development workflows, from writing code to managing projects.
- **Agentic Workflows**: Shifting from simple code completion to delegating complex, multi-step tasks to an autonomous AI agent.
- **Context-Aware Assistance**: The importance of providing AI with deep project-specific context (via custom instructions) to move beyond generic advice.
- **Extensibility**: The concept of extending AI capabilities through a protocol like MCP, creating an ecosystem of tools for the agent.

### 12. Optimization & Best Practices

```
OPTIMIZATION: Agent Mode Efficiency
TECHNIQUE: Increase the "Chat: Agent: Max Requests" setting in VS Code from the default of 20 to a much higher number (e.g., 100 or 10000).
REASON: Prevents the agent from stopping and asking for permission to continue during complex, long-running tasks, allowing it to complete the entire workflow without interruption.
EVIDENCE: [04:20 - 04:55]
```
```
OPTIMIZATION: Uninterrupted Coding Flow
TECHNIQUE: Use the "Snooze" feature for code completions, accessible from the Copilot status bar icon.
REASON: Temporarily disables ghost text suggestions for a set period (e.g., 5 minutes), which is useful during presentations, live demos, or when you need to focus on typing without distractions.
EVIDENCE: [06:21 - 06:40]
```
```
OPTIMIZATION: Agent Command Execution Speed
TECHNIQUE: Add frequently used and trusted terminal commands (like `dotnet build` or `npm install`) to the "Agent: Terminal: Allow List" in experimental settings.
REASON: This bypasses the confirmation prompt for these specific commands, allowing the agent to execute them automatically and speeding up the development loop.
EVIDENCE: [03:20 - 03:56]
```
```
OPTIMIZATION: Agent Context and Accuracy
TECHNIQUE: Use the "Generate Instructions" feature to automatically create a `copilot-instructions.md` file for your project.
REASON: This provides the agent with a deep understanding of the project's architecture, data flow, coding conventions, and developer workflows, leading to more accurate and contextually relevant actions and code generation.
EVIDENCE: [04:59 - 05:33]
```