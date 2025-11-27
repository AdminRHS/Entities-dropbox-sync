---
category: 02_TRANSCRIPTIONS
subcategory: root
type: transcript
source_id: Video_008
title: Video 008
date: 2025-11-21
status: draft
owner: unknown
related: []
links: []
---

# Video 008

## Summary
- TODO

## Context
- TODO

## Data / Content
# How to Connect Claude to Any App (No-Code)

### 1. Metadata Section
- **Video Title**: How to Connect Claude to Any App (No-Code)
- **Channel/Creator**: D-Squared
- **Video URL**: [Not provided]
- **Duration**: [Not provided, approx. 12:41 based on transcript]
- **Publication Date**: [Not provided]

### 2. Description Section
- **Description**: [Not provided]
- **Key Topics**:
  - How to connect Claude AI to any application without writing code.
  - Utilizing Claude's new "Skills" feature, specifically the 'mcp-builder' skill.
  - Creating custom connectors with full read, write, and send access for apps like Gmail and Google Calendar.
  - Automating daily tasks such as drafting morning emails, responding to subscribers, and updating CRM records.
  - The power of stacking multiple connectors to create complex, automated workflows.
  - A step-by-step process for setting up custom connectors locally using the Claude Desktop app.
- **Links Referenced**:
  - [30-Day AI Insight Series - Link not provided]
  - [Work with D-Squared - Link not provided]

### 3. Word-for-Word Transcription

[00:00] You can now connect Claude to literally any application that you use without writing a single line of code. Now, most recent videos are talking about Claude's new skills feature, but they're missing the single most powerful skill. The one that allows you to build any type of connector. This is how you get past the basic read-only tools that most AI platforms offer today.

[00:19] I'm talking full read, write, and even send access on your Gmail, calendar, and CRM. And I'm going to show you the simple two-sentence prompts that make it all work. Let's get into it.

[00:29] [VISUAL: Screen shows a presentation slide titled "Claude Skills Interface"] The way we're able to create these custom connectors for any app to connect Claude to is skills, specifically Claude skills. So Claude skills, you can enable by going to settings. So when you're in Claude, you want to go to your little circle here, your profile. You go inside of settings. Once you're inside of settings, you want to go to capabilities. And under capabilities, they have a new section here called skills.

[00:48] So skills are basically a subset of prompts and code that are packaged up to achieve a certain task. The specific task that we care about when it comes to a skill, and the certain skill we want to enable is going to be the MCP builder. [VISUAL: Screen switches to Claude's capabilities settings page, highlighting "mcp-builder"] So here I'm in my settings. I've gone to settings, I've gone to capabilities.

[01:03] And in here you can see we have a specific skill I've enabled called MCP builder. So MCP in our context right now is simply a connector. It's going to build an MCP that allows us to connect our AI to really any app. And you'll see in a bit, it's ridiculously easy to initiate this skill and have it build really any type of connector I want to use to then connect my AI to any app.

[01:23] [VISUAL: Screen shows a slide titled "Why Build Custom Connectors?"] But the first question we want to answer here is why would I want to create a custom connector? Because oftentimes when you look at Claude and other types of tools, they already have connectors enabled. So if I go to connectors under here, you can see there's tons of them available. So these ones that have the logos already, these are connectors that they've provided me. So if I go to browse connectors, that button there, you can see there's tons and tons of connectors that I can use. Many of these are useful and a lot of people will get benefit from them. But the issue is sometimes they don't have a connector to an application that I'm already using. And that's not the only issue.

[01:52] Outside of sometimes those connectors being limited in what they provide, many of these connectors, not just in Claude, but also ChatGPT, are read-only, meaning you can't actually have the AI take action on your behalf in that app. And that for me is like 80% of the usefulness of these applications being connected to my AI.

[02:08] So by creating custom connectors, we get the benefit of not only really connecting it to any application that we're already using, but also we can give it read and write access, which then allows us to get a lot more benefit from these AIs. And a quick note on that, with great power comes great responsibility. So if you're allowing the AI to write into different things, you need to ensure you're not connecting it to some production database or some sort of critical data set related to your clients. You don't want it deleting things it shouldn't.

[02:31] And so don't run with scissors too fast. Just make sure you're connecting these AIs to systems that you know it's okay to either have it delete stuff because you have backups or something along those lines.

[02:40] [VISUAL: Screen shows the Claude Desktop app download page] And the connectors we're building today are going to be run locally. They can be deployed in the cloud and run different places through your phone, your tablet, etc. But I wanted to start locally first with this video to make it easy on you and understand exactly how to deploy these locally, set them up, and run them easily. With that being said, you need to download Claude's desktop app to take advantage of these custom connectors within Claude.

[02:59] So you can download it. There's a link that's easily accessible. Just Google, you know, Claude desktop and you'll see there's different ways to download it for Windows and Mac. Now that we have that downloaded, I want to show some practical use cases of where I use these custom connectors day in and day out. [VISUAL: Screen shows "Daily Use Cases" slide with icons for Gmail and a CRM] So here are some daily use cases that I have. The first one is morning emails.

[03:16] So every morning when I wake up, I immediately allow Claude to go through all my unread emails from the previous night and draft a series of responses to them. I'll then go through the drafts based off the tone and way that I like to write. I either send it immediately or make some minor edits. That's the first use case. Our second use case is probably once every three to five days.

[03:34] I have a series of subscribers to my newsletter that respond to basic questions I ask when they subscribe to the AI Insights newsletter. When they subscribe, they usually come back with their location and a few other things. That starts to pile up. So I'll maybe have 20 or 25 emails I need to respond to every couple of days. If that's the case, I'll then have AI go in there and respond to those emails based off of how I've responded to previous emails in that context. So it's writing in my tone and my preference.

[03:57] Quick pause, new regular programming. This video is brought to you by me. Two quick things. First, below is a 30-day AI insights series, completely free. You'll get 30 insights in your inbox, how you can apply AI to your business and your work. The second thing is if you'd like to work with me, below are a series of offerings to see if there's a good fit between the two of us. That being said, let's get back into the video.

[04:17] [VISUAL: Daily Use Cases slide] And finally, we have CRM updates. So I often have recurring meetings and there's a lot of stuff I need to update inside of my CRM. What I can do is I can drop one file into a project and have the AI go off and do everything for me, which includes updating the CRM. And this is where the true power starts to get unlocked when you connect Claude to a variety of apps.

[04:34] [VISUAL: Screen shows a flowchart titled "Power of Stacking Connectors"] And there's one example I want to show you of the power of stacking connectors. So what this image shows is we're actually going to have an AI use multiple different connectors to achieve a more complex and more useful task for me. So what we're going to do is to start out, we're going to drop a meeting transcript into the AI. And this is going to be in a dedicated Claude project that knows exactly what to do with said transcript.

[04:54] Once I've dropped in this meeting transcript that happens for recurring meetings, specifically AI coaching, it will process that transcript inside of the Claude project. And the first thing it will do is it'll go to my Google calendar, grab the attendees from that specific meeting. It'll then draft an email inside of Gmail to those attendees in a specific structure and tone that I prefer for these types of follow-ups. It'll then go to the CRM and make a series of updates. It'll update that the meeting happened, it'll update wins from the meeting and a series of other things. All of this is completely automated and happens between, I would say one and four minutes.

[05:25] And this is where the true beauty lies when it comes to allowing your AIs such as Claude and others to connect to other applications, creating very structured system prompts inside of projects for Claude and GPT, and then allowing the AI to then go off and take that action for you so you don't have to do it yourself. By doing this, you're compounding time saved as well. So I've saved probably 15 hours a week by just having these types of automations set up inside of my different projects for my different AIs that I use.

[05:49] Now that we have a good understanding of the benefits and the use cases associated, let's talk a bit about how to go about doing this and what's behind the scenes. So you've seen me say MCPs and connectors back and forth interchangeably and they're basically synonymous things. Behind the scenes, MCP is what really a connector is. So our skill that Claude is going to provide is going to build an MCP server that's going to allow our AI, Claude, to connect to different types of applications.

[06:12] So in this case, we're going to have an MCP server that allows us to connect to Google Calendar, and then another MCP server that allows us to connect to Gmail. And we could also have the other one to our CRM, too. And the beautiful thing about this skill that I'm going to show you how to use is that you don't have to write any code. You write just a few lines for the prompt, and then automatically it creates a MCP server for each application you want to connect your AI to.

[06:33] And when I say the prompt is simple, it is extremely simple. So here is the first prompt to create our Gmail connector, so allowing Claude to connect to Gmail. And it's just one line. And there's really two really important parts here inside of this prompt. The first one is we're explicitly asking Claude to use the MCP builder skill to then create our MCP. In addition to that, we're also asking it to give it specific access to Gmail.

[06:56] And you can see that here where we're asking it to read, write, and send email on our behalf inside of Gmail. Those are the two important parts you want to include in your prompt. After that, as you can see, if I click into this example here, what's going to happen, and this is the actual conversation I had to create this connector. This is the prompt I just showed you. It's going to do a few things. First, it's going to go off and research the different types of documentation associated to that specific application.

[07:20] So this is Gmail. It's looking up all the documentation associated to that, so it knows what code to write. After it's read through all that information, it's going to write the code for us. And better yet, not just going to write the code for us, but it's going to give us very specific instructions on how to configure this on our own machine to run locally. And if I go down here, you can see it gives us a quick start guide of exactly what to do.

[07:39] And the best part here is that if you don't know how to do any of this stuff, you can have AI assist you in the process every step of the way. So that's the first example. Now if we come here, you can see another example for Google Calendar. Again, this prompt isn't very complicated. It's just two sentences. As you can see, the first part of this prompt is explicitly stating that we want it to use the MCP builder skill.

[07:59] In addition to that, we're stating that we want it to create an MCP for this specific application, which is Google Calendar. And then, again, the really important part is we're saying what type of access it should have. So it should have read, write, delete, create events, etcetera access. And then at the end, I'm even giving it my intent of what I'm going to do with this. So I'm asking it I want it to be able to in the end grab attendees from each meeting. And once it's grabbed the attendees from the meeting, it'll then copy that out to somewhere else.

[08:24] So that's our basic prompt. And again, if I go into this link and I go into the conversation, this is the exact prompt I just showed you. And then below this, all the same steps. So it's going to go off, it's going to research the documentation associated to that specific application. It's going to write all the code and the files for us, and it's going to give us specific instructions on exactly what I need to do to set this up on my machine.

[08:44] [VISUAL: Slide titled "Pro Tip"] Now, one pro tip that you need to keep into consideration here is that when you're creating these MCPs via the skill, I recommend ensuring that you have the best model available to you in Claude. And right now that's going to be Sonnet 4.5. The reason you want the best model available to you is that it's very good at creating connectors. And the reason it's very good at creating connectors is that it's very good at writing code and also calling tools over a long period of time. And if we choose the right model at the right time, then it's going to be very effective at getting the task done efficiently.

[09:11] [VISUAL: Slide titled "Simple Setup Process"] And when creating any of these connectors that are going to be deployed locally on your machine, there's always going to be a few steps you're always going to have to take. And these are what I wanted to show you here. So the first step is going to be obviously saving the files that Claude's created onto your machine. You're going to want to create a folder, and you can name this folder really whatever you want, but ideally it's named after the application you're going to connect Claude to. So you could name it Gmail, you can name it Google Calendar, you can name it whatever else. You want to copy and paste all those files into that folder.

[09:36] Once you've done this, you're then going to need to get the credentials for that application that AI is going to connect to. So if you're connecting it to Gmail, Google Calendar, AirTable, etc, you need to get the specific credentials that it's asked you to get to then provide to the AI. These steps will vary based off the application you're connecting to. If you're at all confused by this, just have AI assist you with that process. Ask it to give you step-by-step instructions on how to get these credentials for said task.

[10:00] After that, you want to then configure Claude to then use this very specific MCP and or connector you just created. And the cool thing about this is that if you use a tool like Cursor or any other tool that has access to your desktop and knows how to write code, it'll be able to most likely do all this for you. And I want to show you just how easy that is. So if I show you just one example, here's an example I have for Cursor.

[10:19] So this is Cursor, a bunch of code. Kind of ignore everything except for the chat on the left hand side. [TEXT: Right side] And what I've highlighted here is all I've given the AI. I've simply said, I want you to connect this specific MCP to my desktop app for Claude. How do I do that specifically, where is it housed, etcetera? After typing that, it goes off and it does everything for me. It configured everything for me. And then I had some errors, so I just pasted those errors back in. I said I'm getting some errors when trying to open Claude.

[10:44] I then gave it the errors again. It fixed all the code. And if I scroll to the very bottom, it's done. It finished everything for me and it was readily accessible. So it was maybe one or two iterations of me going back and forth with the AI, providing it some errors and asking it to do a task for me. And that's it. You're done. It's very simple. The connectors are set up and all you have to do is either explicitly tell the AI that you want it to use that connector, and or it'll implicitly infer what you want to do based off of the context you've given it in the prompt.

[11:09] One key thing to ensure is that the connectors are turned on. And the way that we can do that is if you go to your settings inside of Claude on your desktop, you go to your connectors and you scroll through and you make sure that it's configured. So here you can see that all the different ones that I've created that are custom, you can see that it has the local dev sign saying that this is something local and I've developed myself and that it's configured and set up. As long as this is good and there's no red signs and no failures, you're good to go.

[11:32] [VISUAL: Slide titled "Key Takeaways"] And as a quick recap, we can now create specific connectors with the MCP builder skill with one to two lines for a prompt and connect Claude to any application. And the importance of creating custom connectors is that sometimes these aren't readily available for us that are provided from Anthropic or OpenAI. And also, they often don't have write access, which degrades their ability to be useful for me and you.

[11:53] Next, I highly recommend you start local, run these configurations locally, get used to it locally. Once you're confident in building a few connectors, then you can start researching and figuring out how to deploy these in the cloud, so you can then access them from anywhere. And finally, the most important thing is you want to stack connectors in projects, so Claude projects, GPT projects to get completely automated workflows to save yourself tons of time and become a lot more productive utilizing AI within your day-to-day work.

[12:18] And that's it. So if you enjoyed this, please be sure to share with your friends. And as a reminder, two things. First thing, below is a 30-day AI insight series, completely free. You'll get 30 insights in your inbox for how you can apply AI to your business and your work. The second thing is if you'd like to work with me, below are a series of offerings to see if there's a good fit between the two of us. With that being said, there's probably a video around here that the YouTube gods thinks that you'll love. So you should totally check it out. See you next time, Internet.

---

# TAXONOMY ANALYSIS

## 4. Workflows Identification

WORKFLOW: Enable Claude Skills
OBJECTIVE: To activate the custom 'Skills' feature within the Claude AI platform.
STEPS:
  1. Navigate to your profile icon.
  2. Go to `Settings`.
  3. Select the `Capabilities` tab.
  4. Find the `Skills` section.
  5. Toggle on the desired skills, specifically the `mcp-builder` skill.
DURATION: 1-2 minutes
COMPLEXITY: Low
TOOLS USED: Claude
INPUT: User account in Claude.
OUTPUT: `mcp-builder` skill is enabled.

---

WORKFLOW: Create a Custom Application Connector (MCP)
OBJECTIVE: To generate a custom connector for an application (e.g., Gmail) using Claude's `mcp-builder` skill.
STEPS:
  1. Open Claude and ensure the `mcp-builder` skill is enabled.
  2. Write a prompt explicitly asking Claude to use the `mcp-builder` skill.
  3. Specify the target application (e.g., "create an MCP for Gmail").
  4. Define the required permissions (e.g., "the ability to read, write, and send email").
  5. Run the prompt.
  6. Claude researches the application's API and documentation.
  7. Claude writes the necessary code and configuration files.
  8. Follow the provided instructions to deploy the connector.
DURATION: 5-10 minutes
COMPLEXITY: Medium
TOOLS USED: Claude, Sonnet 4.5
INPUT: A two-sentence prompt.
OUTPUT: A custom, locally-runnable connector (MCP server) for the specified application.

---

WORKFLOW: Automated Morning Email Drafting
OBJECTIVE: To automatically draft responses to all unread emails from the previous night.
STEPS:
  1. Trigger the workflow (presumably via a prompt).
  2. Claude connects to Gmail using a custom connector.
  3. Claude reads all unread emails.
  4. Claude drafts a series of responses based on the user's tone and past replies.
  5. The user reviews the drafts.
  6. The user sends or makes minor edits before sending.
DURATION: Automated part is a few minutes.
COMPLEXITY: Medium
TOOLS USED: Claude, Custom Gmail Connector
INPUT: Unread emails in a Gmail account.
OUTPUT: Draft email responses ready for review.

---

WORKFLOW: Automated Newsletter Subscriber Reply
OBJECTIVE: To auto-respond to new newsletter subscribers who answer initial questions.
STEPS:
  1. A new subscriber replies to a welcome email.
  2. Claude's workflow is triggered.
  3. Claude reads the subscriber's reply using the Gmail connector.
  4. Claude drafts and sends a personalized response based on the subscriber's location and answers, mimicking the user's tone.
DURATION: Automated
COMPLEXITY: Medium
TOOLS USED: Claude, Custom Gmail Connector, Newsletter Platform (implied)
INPUT: Subscriber reply email.
OUTPUT: A sent personalized email to the subscriber.

---

WORKFLOW: Stacked Connector Automation (Post-Meeting)
OBJECTIVE: To automate all post-meeting follow-up tasks by stacking multiple custom connectors.
STEPS:
  1. Drop a meeting transcript file into a dedicated Claude project.
  2. Claude processes the transcript.
  3. **(Stack 1)** Claude uses the Google Calendar connector to get the list of meeting attendees.
  4. **(Stack 2)** Claude uses the Gmail connector to draft a follow-up email (recap) to all attendees.
  5. **(Stack 3)** Claude uses the CRM connector to update the relevant records with meeting notes, outcomes, and 'wins'.
DURATION: 1-4 minutes (automated)
COMPLEXITY: High
TOOLS USED: Claude, Custom Google Calendar Connector, Custom Gmail Connector, Custom CRM Connector
INPUT: A meeting transcript file (.txt, .md, etc.).
OUTPUT: Sent follow-up email and updated CRM records.

---

WORKFLOW: Simple Setup Process for Local Connectors
OBJECTIVE: To deploy a custom-built connector on a local machine.
STEPS:
  1. Save the files generated by Claude into a dedicated local folder.
  2. Set up application credentials (e.g., from Google Cloud Console) as instructed by Claude.
  3. Configure the Claude Desktop app to recognize and use the new local connector.
  4. Start using the connector.
DURATION: 5 minutes (as per video text)
COMPLEXITY: Low to Medium
TOOLS USED: Claude Desktop, Local file system, Google Cloud Console (or similar)
INPUT: Generated code files from Claude.
OUTPUT: A running, locally deployed application connector.

## 5. Action Verbs & Operations

#### A. CREATION VERBS (Making new things)
- Create
- Build
- Write
- Draft
- Generate

#### B. MODIFICATION VERBS (Changing existing things)
- Update
- Edit
- Configure
- Set up
- Fix

#### C. ANALYSIS VERBS (Understanding/Evaluating)
- Research
- Review
- Look at
- See
- Check
- Diagnose
- Ensure
- Infer

#### D. ORGANIZATION VERBS (Structuring/Managing)
- Organize
- Manage
- Plan

#### E. COMMUNICATION VERBS (Sharing/Presenting)
- Show
- Send
- Respond
- Ask
- Tell

#### F. BROWSER/AGENTIC OPERATIONS (AI Agent & Automation Actions)
- Connect
- Use (a tool/skill)
- Run
- Deploy
- Take action
- Automate
- Initiate
- Process
- Go to
- Grab
- Drop
- Call (a tool)

#### G. DATA OPERATIONS (Processing, Transforming, Moving Data)
- Get
- Read
- Copy
- Paste
- Save
- Delete
- Apply
- Access

## 6. Task Chains

TASK CHAIN: Custom Connector Creation
Enable `mcp-builder` skill → Write two-sentence prompt defining app & permissions → Claude researches API → Claude writes code & instructions → Deploy connector locally.

---

TASK CHAIN: Daily Email Automation
Wake up → Trigger Claude → Claude reads unread emails → Claude drafts responses → User reviews & sends.

---

TASK CHAIN: Post-Meeting Automated Workflow
Drop meeting transcript → Claude Project processes it → Get attendees from Google Calendar → Send recap via Gmail → Update CRM.

## 7. Responsibilities Vocabulary

#### Professional Roles Mentioned:
- AI Coach

#### Responsibilities/Activities:
- "Connecting Claude to any application"
- "Building any type of connector"
- "Drafting responses to all unread emails"
- "Responding to newsletter subscribers"
- "Updating the CRM"
- "Stacking connectors for automated workflows"
- "Setting up app credentials"
- "Configuring Claude"
- "Running configurations locally"

#### Skills Mentioned:
- Writing prompts
- Configuring systems
- Writing code (though the goal is no-code)
- Tool calling

## 8. Tools & Technologies Matrix

| Tool Name | Category | Purpose | Used For | Mentioned With |
|-----------|----------|---------|----------|----------------|
| **Claude** | AI Language Model | Core AI for processing and generation | Creating connectors, drafting emails, updating CRM | MCP Builder, Gmail, Google Calendar |
| **Claude Desktop App** | Application | Local interface for Claude | Running custom local connectors | MCPs, Gmail, Google Calendar |
| **MCP Builder (Skill)**| Claude Skill / Code Gen | To automatically generate connector code | Building MCP servers for any application | Prompts, Gmail, Google Calendar |
| **MCP (Model-Contact Protocol)** | Technology / Server | The connector itself, acting as a bridge | Connecting Claude to external apps | Gmail, Google Calendar, CRM |
| **Gmail** | Email Service | Communication and automation target | Reading, writing, sending, and drafting emails | Custom Connector, MCP |
| **Google Calendar** | Calendar Service | Scheduling and automation target | Getting meeting attendees, creating events | Custom Connector, MCP |
| **CRM** (unnamed, Airtable shown) | Business Software | Customer Relationship Management | Automatically updating meeting notes and client wins | Custom Connector, Automation |
| **ChatGPT** | AI Language Model | Comparison | Mentioned as having similar read-only limitations | Claude |
| **Sonnet 4.5** | AI Language Model | Claude's advanced model | Recommended model for code and tool calling | Pro Tip, MCP Builder |
| **Cursor** | Code Editor | AI-powered code editor | Assisting with the local setup and configuration of connectors | Claude Desktop, Local Deployment |

## 9. Objects & Deliverables

- **Custom Connectors (MCPs)**: The primary output, which are locally run servers.
- **Draft Emails**: Automatically generated email responses.
- **Sent Emails**: Automated replies to subscribers or meeting recaps.
- **CRM Updates**: Updated records in a CRM system.
- **Meeting Transcripts**: The input file that triggers a complex workflow.
- **Code Files**: The Python code, dependencies, and scripts generated by the `mcp-builder` skill.
- **Configuration Files**: JSON and other files needed to configure the connectors and Claude Desktop.
- **App Credentials**: Specifically `credentials.json`, required for authentication.

## 10. Integration Patterns

INTEGRATION: **Claude (mcp-builder skill) + Target Application (e.g., Gmail)**
PURPOSE: To create a functional, no-code connector that gives Claude read/write access to an application.
FLOW: A prompt in Claude → triggers `mcp-builder` skill → generates an MCP server (code) → which is then run locally → to connect the Claude Desktop App to the Gmail API.

---

INTEGRATION: **Meeting Transcript + Claude Project + [Google Calendar Connector + Gmail Connector + CRM Connector]**
PURPOSE: To fully automate post-meeting administrative tasks.
FLOW: Meeting transcript (file) → dropped into a Claude Project → Claude uses Google Calendar connector to get attendees → then uses Gmail connector to send them a recap → and finally uses the CRM connector to log the meeting details. This is a "stacked connector" pattern.

## 11. Business Concepts & Strategy

- **Read vs. Write Access**: Highlighting the limitation of "read-only" tools and the power of enabling "read-write" access for AIs to take action.
- **Productivity Compounding**: The idea that automating small, repetitive tasks (like email and CRM updates) saves a significant amount of time over a week (mentioned "15 hours a week").
- **Workflow Automation**: The core concept of using AI and connectors to create automated, multi-step processes that handle administrative work.
- **Local-First Deployment**: A strategy to start by building and testing connectors on a local desktop for simplicity before deploying to the cloud for wider access.

## 12. Optimization & Best Practices

OPTIMIZATION: **Connector Creation Quality**
TECHNIQUE: Use the `Sonnet 4.5` model when running the `mcp-builder` skill.
REASON: It is the best model for code generation and tool calling, which creates better, more effective connectors.
EVIDENCE: [08:44 - 09:03]

---

OPTIMIZATION: **Workflow Development**
TECHNIQUE: Start by building and running custom connectors locally on the desktop app first.
REASON: It simplifies the initial setup and testing process. Once confident, you can then deploy to the cloud for remote access.
EVIDENCE: [11:53 - 12:03]

---

OPTIMIZATION: **Task Efficiency**
TECHNIQUE: Stack multiple connectors within a single Claude Project.
REASON: Allows for the creation of complex, fully automated workflows that handle multi-step tasks (like post-meeting follow-ups) with a single trigger, saving significant time.
EVIDENCE: [04:35 - 05:48], [12:05 - 12:18]

## Findings
- TODO

## Actions / Next Steps
- TODO

## Metrics / Status
- TODO

## Attachments / Links
- TODO

## Change Log
- 2025-11-21 standardization scaffold added
