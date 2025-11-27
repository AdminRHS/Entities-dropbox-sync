---
category: 02_TRANSCRIPTIONS
subcategory: root
type: transcript
source_id: Video_009
title: Video 009
date: 2025-11-21
status: draft
owner: unknown
related: []
links: []
---

# Video 009

## Summary
- TODO

## Context
- TODO

## Data / Content

Model
ThinkingThoughts
Auto
Expand to view model thoughts

chevron_right
Video Transcription Custom Instructions - Taxonomy Analysis Focus
1. Metadata Section
Video Title: 3 Prompts To Get INCREDIBLE App Designs From AI
Channel/Creator: Chris Ashby
Video URL: [Not Provided]
Duration: [Not Visible]
Publication Date: [Not Available]
2. Description Section
Description: [Not provided]
Key Topics:
A three-prompt process for generating high-quality app designs using AI.
How to extract a design style from an inspiration image.
How to create a comprehensive design system guide for an AI coding tool.
Using Dribbble for design inspiration.
Leveraging AI coding tools like Cursor with models like GPT-5 and Claude/Sonnet.
Building a showcase app with Vite, React, and Tailwind CSS to test the design system.
Links Referenced:
Skool.com/aiapps: A link to the creator's community, the "AI App Builders Academy".
3. Word-for-Word Transcription
[00:00] If you're struggling to get great design out of AI coding tools, or you're just getting the same old purple gradients, then this is the video for you. I'm going to teach you exactly how to get incredible designed UIs and show you the exact three prompt process that I use to extract the design style from any design system available and turn that into a usable framework and guide that your AI coding tool can use to follow that style exactly.
[00:26] And by the end of this video, you'll be able to create apps with incredible looking design, no matter what you're building. If you don't know me, my name is Chris and for the last 15 years I've been designing apps and advising startups on product and design. And with that said, let's get into the three prompts and find your perfect design style for your app.
[00:43] [VISUAL: Animated title card with "Build Great Products"]
[00:51] So let me walk you through how to create an actual incredibly well designed design system for your app that you're building with AI coding tools. And the first thing that we're going to do here is we're going to go to Dribbble, which if you don't know, Dribbble is basically a website that has a ton of visual inspiration that you can search and look at and it kind of tends to skew towards apps and user interfaces and websites and that sort of thing. But what we're not going to, what we're not going to do here is we're not going to just search for something that we like the look of that we think looks nice.
[01:21] We're actually going to search for a design system. And if you don't know what a design system is, a design system is a set of components. A component would be like a button, like a form, a card. Um for example, like this is a card here and it has these hover elements on these, um and this image on the left with a button on it and an arrow right. All of these are user interface components that make up a design system that you would have in your app.
[01:50] And the reason we want to create a design system and the reason we want to use a design system for inspiration is because a design system gives your AI coding tool and it gives our app like all of the possible components that we could ever possibly want to build in our app. Um bordering on like some more complex stuff, but it's going to give us a great foundation to start from. So the first thing I'm going to do here is I'm going to search for a design system. You can search for like design system in a specific color if you want to do it in a specific color or you're unsure.
[02:18] And you'll get all of these different design systems laid out here. Now, I wouldn't go for something that looks like more like a poster like this, because this is going to like skew the AI's interpretation of what this design looks like. What you want to go for is a screenshot of a design system that is pretty flat like this that includes a bunch of UI components. But I wouldn't actually go for this one because this all the elements in this are a little bit too small.
[02:45] What we want to do is we want to find something where it's really, really clear all of the individual components and we can extract the style from it very easily. So something like this works really, really well. Maybe, maybe not this because it's got the purple dashed borders around these, which kind of the AI is going to pick up that is going to add these purple dashed borders into our style guide and we actually don't want that. We're kind of ignoring that element here. We probably want something more like this, which just has all of the UI components or like a a a few UI components laid out in a style.
[03:19] It's super, super clear. There's nothing else on here apart from the UI components, the colors, the typography and the kind of way that it's designed. So what we're going to do is we're going to start from this screenshot of a design system that is clear and visible and doesn't have anything else on the image. That's your starting point. From here, what we're going to do, we're going to jump into Cursor for this and I you can use Cursor for this and then go back to Lovable or Bolt.
[03:47] And I would recommend using Cursor because what we're going to do here is we're going to go through these three steps, these three prompts. The first prompt is basically going to be outlining a a high level description of what this design is. So let's copy this to our clipboard. and let's open Cursor.
[04:07] And what we're going to do here is we're going to open a project. So I'm going to open a new project, just create a new project. Let's just go to the folder here with, with this project. I've already created a folder for it. If you haven't, just create a new folder in Cursor. If you don't have Cursor, just go over to cursor.com and download Cursor and open it and you'll just need to open a open a project, open a folder. A project is basically a folder with all of your files in, all of your code files in.
[04:39] And what we're going to use this to do is actually to create a style guide, a design system um for our application. And we can take that file, we can take that style guide and actually put it into our code base in Lovable or Bolt or whatever tool we're using or you can just continue building in Cursor if you want to. Um you can kind of use it anywhere you want. And how we're going to start doing this is we're going to jump over to Agents view here at the top.
[05:03] And this is going to give us an interface which is more focused on this kind of just chat style interface. And we're going to be using a few different AI models here as well. So we're going to be using GPT-5 for analyzing design style and writing out these design system descriptions. GPT-5 tends to be better at visual and user interface um elements. Um and Anthropic, like Claude 4.5, those those models tend to be better at writing code.
[05:33] Cursor 2.0 also has their new composer one model, which is super fast, but I I wouldn't want to use this for this. Cursor uh Cursor's composer model is more for like quick fixes, bug fixes, any any small tasks that are relatively easy that you want to just get done very quickly from a code point of view. What we're going to do here though is not necessarily uh code to start off with, although we are going to write this in a specific file format that makes it easy for our AI to read the style.
[06:01] So what we're going to do is we're just going to paste this um screenshot in here. So now what we're going to do in Cursor is we're going to add this prompt in here and this says deeply analyze the design of the attached screenshot to create a design.json file. If you don't know what JSON is, it's essentially just a data file format. So it's a type of code that basically will allow us to store different types of data and that makes it really, really easy for AI to read because it can understand the data format and structure of that.
[06:34] It's very kind of structured data basically. Um and it will give the AI like a really clear idea of the different kind of categories of design and the different definitions for each of the elements within each of the components and the design style that we're working with as well. So we're going to use JSON for this to kind of give the AI a little bit of an easier time creating our designs. Um we're then going to say deeply so um in this project that describes the style and design of every component needed in a design system, a high level like a creative director.
[07:05] So we're kind of creating this design.json file and we're doing it at a high level. We don't want to specify all of the exact little details of the design at the moment because what I've found from like just adding a screenshot and creating all of the details just from that screenshot is that the AI will tend to generalize and it will fill in the gaps where it doesn't have information and it will kind of just default to like its basic styling if it doesn't really know what the screenshot is.
[07:32] So I want to just give it create like a vague like, well not vague, I want to create like a detailed overall description of the design style from this from this design system screenshot that we've given it here. Capture high level guidelines for structure, spacing, fonts, colors, design style and design principles so I can use this file as the design guidelines for my app. The goal with this file is to instruct AI to be able to replicate this look easily in a project. So we want this to be written in a way that is going to be easy for AI to understand.
[08:02] And we also want to capture all of these elements of the design system, so spacing, fonts, colors, design style and principles, basically an overall guideline of what we're going to do here. We've set it to GPT-5, so let's send this off here. And this is basically going to create a little to do list for us to analyze the screenshot first and then identify what the design style and patterns are and then create that design.json file in our project here. So let's come back once that's written the file to our project and see what it's done.
[08:32] So we can now see that Cursor has created our design.json file in our project. Um it's analyzed this screenshot. It went through all of these to-dos here basically. And if I go to this design.json file. So let's just jump over to the editor view and open this design.json file here. We can see that we've basically got, and this is why I mean like JSON is like a structured data format basically.
[08:59] Um we've got all of these kind of all of this information about the style. So brand, we've got essence, tone of voice, keywords, optimistic, clear, helpful. It's extracted that from like the image of like the design system that we gave it, which is pretty good. Uh style, so design language, soft round white surfaces floating on a citrus canvas with subtle shadows and clean typography. Vivid purple is the primary accent, lime green is used for positive actions and highlights. We've got some principles here, so softness over sharpness, generous um border radius and pill shapes, airy spacing, hierarchy, low contrast, human first visuals, clarity and restraint, which I think is a pretty good summary of the screenshot that we put in.
[09:40] And it's also outlined some styles here, some rough styles that it can use. So we've got border radius, break points, grids, some colors here, some neutral colors. It's not given us too much, so it's kept it at a pretty high level and then typography with some different font options that we've got here as well. And yeah, overall it's given us a ton of stuff here to use as the foundation for building our app just from that screenshot. So let's jump back over to the agents view here. I'm going to click keep all in Cursor, which basically is going to save this file that it's created to our project here.
[10:18] You can see it was all in green before that means that it was new code, new text that it'd written. So we decided to keep that. So we're going to keep that and then we're going to do a follow-up prompt here. And for that I'm going to do a new agent. So generally it's really good in Cursor or whatever tool you're using when you do a new task, when you build a new feature, when you when you want to get the AI to do something that that is maybe slightly different to the task that you got it to do before, create a new agent, create a new chat, clear your chat context.
[10:46] It's really, really good practice. So let's click new agent here. And for this, I'm going to change it to Sonnet 4.5. And we're going to put in this next prompt here as well.
[10:56] Quick break in the episode to talk about my community for people building apps with AI. It's called the AI App Builders Academy. Inside you'll learn how to plan, build, launch, and grow a profitable app with AI in just 21 days. And you'll also get access to more advanced courses like how to build with Claude Code, how to build mobile apps, how to build AI agents, and more with new lessons being released every single week. On top of that, you'll also get over three million dollars worth of AI deals so that you can start building at zero cost.
[11:23] And also access to our weekly Q&A sessions where you can get unstuck on your app building journey. And if you sign up to our VIP annual plan, which is offered at a 60% discount, you'll also get access to monthly group coaching and workshops as well as our community demo day where you can pitch your app idea to me and other VIP founders to get business and strategic advice on your app. This community is full of people building real applications with AI and getting real paying customers.
[11:51] And this is the lowest price that it's ever going to be because we increase the price for every 50 members that join the community. And so if you want to lock in your price and start building your app business today, then just head over to skool.com/aiapps to find out more. I'll see you there.
[12:07] So what we're going to say is we're going to say, let's create a simple screen that contains every UI component that would exist in a design system on a mock dashboard following the design style outlined in design.json, and you can add these files into your chat in Cursor. All you do is click is press @ and then you select the file you want to add. So we'd add like design.json there. I'm going to remove that because it's already in the chat.
[12:31] Build this as a Vite app using React and translate all styling into Tailwind version 3. And we want to use this because this is the primary kind of um foundation of most apps built using AI coding tools. If you build using Lovable or Bolt, it's it's going to build it with Next.js, Vite, React, and Tailwind as kind of the foundation like technology underneath it. So we're basically creating our design system in a really familiar foundation that AI coding tools will know exactly how to use.
[13:16] And then I've said just run this locally, which means just run the project locally on a local development server so that we can see what it looks like and if we're happy with it. And so we've selected 4.5 here as well, Sonnet 4.5 as the model because Sonnet 4.5 is generally better for coding tasks like this. You can use GPT-5 for coding tasks, but I would say it's better at visual stuff and it doesn't do the more um structural or like complex tasks as well.
[13:43] And Sonnet 4.5 is just a generally a kind of all round um general purpose coding model that you can use for any coding any coding task if you're not sure. So let's send this off to Cursor in a new chat. And you'll be able to see here on the left we've got a new in progress um agent and in progress chat that's kind of loading here. And this is thinking it's kind of loading, it's going through um, it's creating a comprehensive Vite plus React plus Tailwind 3 app that showcases all the UI components from the design system.
[14:14] Let me break this down into steps. And it's going to do all these to-dos to kind of build our app for us. You could also create this just as a simple HTML page if you're building a website with all the components on and that would actually be more straightforward for the coding agent to do here as well. As you build in Cursor, you're going to get these requests come up that Cursor is asking us to look at and do. I'm just going to click run on all of these.
[14:37] This is basically going to go through and set up a Vite um React app. It's got a permission error here, but it will be able to go through and do it. Um so it's setting up the project structure manually and creating all of this code along with all these design components in our project based on the design.json file that we already created here. And this is creating a folder called design system showcase. It doesn't matter too much about this because what we're going to use this for is we're just using this to create a detailed um kind of design system that we can go and use in any other tool we want or that we can use in the foundation of our application, even if we continue working in this project.
[15:23] So you can actually do this step and just use this as the first prompt to kind of start creating your app in Cursor. If you want to create your if you want to create your app or your first page of your app using design.json as a reference, that is a really good way of doing it. If you're building something else, you can take the file that we're going to create in the third prompt over to any tool to use to give it direction for your design system.
[15:40] So let's wait for Cursor to come back here and build this app and we can see what all of our kind of mock components look like on a dashboard. So this is now saying that this is successfully running. So our app is running locally. It's built our app for us. What's included? It's done this project setup, which is a familiar kind of like um AI friendly web app setup using Vite and React and Tailwind. It's added all of these core UI elements here.
[16:04] So we've got avatar buttons, icon button, cards, progress bars, calendars, profile summary, typography scale, color palette examples, all of that sort of stuff and it all follows design.json. And basically this says it's app is now running at local host. If you don't know what local host is, this is a URL basically. We're running our app on a local development server on our machine and that is how developers work to basically build apps and check how they work before they actually deploy them to the web or deploy them to whatever kind of like deployment environment they're working with.
[16:39] And it's created all of these files here that we can see for us. And what we're going to do here basically is we're going to use the browser inside of Cursor to check this so we don't even have to leave Cursor to go to this website address. We can copy and paste this local host 5173 address and put it into our browser and get it that way. But if you're in Cursor, all we have to do is just click this web kind of like globe icon in the chat down here, which says connect to browser.
[17:03] and then you just click browser tab and that opens a browser tab on the right along with all of the files that it has just created. And what we're going to do now we're in this browser view. I'm just going to shrink these chats down a little bit so that we can see this better is we're going to copy this and then paste that into the browser in Cursor. And what you can see here is all of our design components listed out on a screen here with all of our headings, our styling, our components.
[17:33] Some of these have a little bit, there's tiny issues with some of these, like that's a little slightly too far on the right on that toggle. But it's working nicely. Um this is all just front end. You've got these buttons with hover states and we've got all of the kind of styling that we need, these different types of buttons here, primary, secondary, tertiary, we've got all of these kind of cards with the icons added in, the avatar setup, avatar stacks, progress indicators and these kind of pills and then buttons, the primary, secondary, success and ghost buttons, icon buttons, a calendar view here.
[18:11] So this is, this is the majority of the components that we'll need in our app, in our design in the design system for our app. And this basically gives us a great foundation. You can already see like um compared to the screenshot if I go back to the screenshot here, this is really, really similar to this screenshot that we've added in to kind of follow this style. It's pretty much, barring like some specific fonts, it's like almost identical. And that is really the power of like doing it this way, extracting all of the information into a design.json file and doing that at a high level.
[18:47] And what we're going to do now is the third prompt is we're basically going to create our full comprehensive design system document that any AI tool will be able to follow. So let's, uh let's just um move this, we can keep this up here for now. I'm just going to expand this view a little bit. Let's click new agent here. And what we're going to do is we're going to go back to GPT-5. So we want to use GPT-5 for this. Um actually first let's go back to this chat and then just make sure if you want to keep everything here, you just click keep all.
[19:22] So we're going to click keep all on these changes. And uh we did that on the previous one. So let's just check our files are all there. So we've got design.json and we've got all of our app files here as well for our design system. Let's just reload um this local host so we've make sure we've got it on the right. And then what we're going to do is we're going to create a new agent here. And we're going to do this third prompt.
[19:45] So this third prompt is basically to create a comprehensive design system um in a JSON file that any AI coding tool can read based off of this design that we've created on the right. And if you do want to make any tweaks to to the design components on the right, what you can do here is you can actually create a new agent and do all of these little design tweaks before you do this third prompt just to make sure you've got everything right.
[20:09] And this is going to and that's going to basically make make sure that all of your components are kind of like working and set up exactly as you want before you create the full like comprehensive style guide. So this prompt says, in this project, create a folder named 'design' and create a design-system.json file in this folder that outlines the exact styling for all components and styles in this app, along with a high-level design guidelines. The goal with this file is to create a comprehensive guide for AI to follow when building new features in this app.
[20:39] And let's change this to GPT-5 uh because GPT-5 is generally better at writing uh code for UI um and information about UI and extracting UI styles and all of that sort of stuff. And let's send that off to be done. And that is going to create that design-system.json file in our project here. And we can either use that design-system.json file to reference in Cursor as we're building our app and kind of keep this page, this design system page separate from our app.
[21:06] So we've always got it there as a reference within our app project or we can copy all of the information on the design-system.json file and give that to Lovable or Bolt in order to design our app in a specific style. So we can either copy and paste it into Bolt or Lovable or you can copy and paste it into the knowledge section in Bolt or Lovable so that it always follows that style guide when it's building stuff.
[21:32] You might, if you've already built something in Lovable or Bolt, you've already built an app and you want to translate the style into something new. You might want to use a prompt that's like refactor the entire UI of my app. Do not change anything functional but follow these exact design guidelines and then paste in your full design-system.json file into Lovable or Bolt. That is a way that you could do it. Or you could add it if you're building something from scratch, you can always add it in, you can add it in your first prompt if you just want to start from design.
[22:03] Although that might be a lot of text and could confuse the AI when it's building the first version of your app or you can add it into the knowledge in the settings in Lovable or Bolt. If you want any new feature that you're building to follow a specific set of rules or if you're just doing work on the UI and you only want to focus on those changes. So let's wait for GPT-5 to be done here and then come back and have a look at our design-system.json file.
[22:29] So GPT-5 has now finished writing our design-system.json file. Let's have a look at what this file uh actually includes. And you'll be able to see how much detail it includes here. This is um, we'll go back to this view. It's 646 lines of text, which is basically every single thing in our design system for all of our components that we need for our app. It's got all of the brand information, the meta information.
[22:57] A lot of this is the same as what we had in our design.json file, but this is just more specific detail based on the actual components that it's built here. And this is actually a really nice view um looking at it here to see like all of these laid out next to each other. Um and it's given it every single, every single definition for all of the components that we've got in our kind of design style system like our design system guide and page that we've built here.
[23:24] Every single style, um all of the variables. This is all written in um it's all in Tailwind as well, or specific to Tailwind, so it will work with any of these kind of app building tools that use Tailwind kind of as their base kind of style system in their app. Or if you're building any app that uses Tailwind as styling, which is a very high chance that you're going to be doing that because that is seems to be just the um styling kind of framework that all apps are using nowadays.
[23:53] Um we've got a bunch down here on guidelines as well, which is super useful. So you've got structure, spacing, fonts, colors, style, accessibility, motion, interaction, data visualization, content, do's and don'ts. And why this is a really good place to work from is because now you have all of these rules set up, you can also change this file as you build if you want to do slight tweaks to it as well, we've got our foundation.
[24:20] Now we can do tweaks as we go, especially if you're working in something like Cursor where you can see all of these files separately and just go in and make tweaks. And if I do want to build any feature um in my app, I can just go to create a new agent here in Cursor and I can just do @ reference my design-system.json in any changes that I'm making um to my app. And even like if I want to make specific changes in the browser, um I can also using the browser and selecting a specific element, I can even use the select element view in Cursor to actually just select.
[24:51] So we would maybe basically like go down to this toggle here and say like, okay, this button um actually on the right hand side, it doesn't have enough spacing. Can you update that and can you update design-system.json as well to reflect those changes? And that will keep our design system and style guide up to date with everything that we build.
[25:10] So you can see how by following this simple three prompt framework for taking a screenshot, extracting the design style from that screenshot, creating a guide for the UI to follow when building your app, then building your app using Tailwind and translating all of that all of that design guidance into Tailwind and React styling, and then actually creating a design system framework kind of off the back of that app that you've built and adding that to a folder in your project so that you can reference that design system at any time, can actually give you much better results when you're building your app using AI coding tools.
[25:47] And this is so much better than just dropping in a screenshot and asking it to copy it, you're actually getting a complete set of components all with defined styles, all listed out in a comprehensive guide that your AI coding tool can follow step by step. And if you are building an app with AI or you want to get started and try it out, then I've got a community helping people do just that over at skool.com/aiapps.
[26:10] You'll learn how to build your app from scratch in 21 days and also a ton of other things like building mobile apps, building AI agents and more. So head over there to check that out. If you enjoyed the video, don't forget to like and subscribe. It means a lot to the channel. Thank you for watching and I'll see you next time.
TAXONOMY EXTRACTION REQUIREMENTS
4. Workflows Identification
code
Code
WORKFLOW: AI-Assisted Design System Generation
DEPARTMENT: Design / Development
OBJECTIVE: To extract a design style from a visual inspiration (screenshot) and generate a comprehensive, reusable design system framework and a showcase app for an AI coding tool.
STEPS:
  1. Finds visual inspiration for a design system on Dribbble.
  2. Extracts a high-level design language from a screenshot using an AI prompt (GPT-5 in Cursor).
  3. Generates a basic `design.json` file with initial style guidelines.
  4. Builds a mock dashboard/showcase app using another AI prompt (Claude/Sonnet in Cursor) to visualize all UI components based on the initial style guide.
  5. Refines the design components in the showcase app.
  6. Creates a comprehensive, detailed design system file (`design-system.json`) based on the refined components and initial style guide.
  7. Uses the final design system file as a guide for all future app development to ensure consistency.
DURATION: A few minutes per prompt.
COMPLEXITY: Medium
TOOLS USED: Dribbble, Cursor, GPT-5, Claude/Sonnet 4.5, Vite, React, Tailwind CSS
INPUT: A screenshot of a design system from Dribbble.
OUTPUT: A comprehensive `design.json` file (style guide) and a functional showcase app (Vite+React) demonstrating the design system.
4B. Task Templates Extraction
code
Code
TASK: EXTRACT_DESIGN-STYLE_FROM_IMAGE
TASK_ID: TBD
DEPARTMENT: Design / AI
ACTION: Extract
OBJECT: Design Style
CONTEXT: From inspiration image using AI analysis
COMPLEXITY: Low
TIME_ESTIMATE: 1-2 minutes
PARENT_PROJECT: AI_App_Design_System_Setup
STEPS_USED: [
  SEARCH_DRIBBBLE_FOR_INSPIRATION,
  SELECT_FLAT_DESIGN_SYSTEM_SCREENSHOT,
  PASTE_SCREENSHOT_INTO_CURSOR,
  EXECUTE_DESIGN_ANALYSIS_PROMPT
]
SKILLS_REQUIRED: [
  "analyzed design styles via Cursor"
]
TOOLS: [Dribbble, Cursor, GPT-5]
INPUT: Screenshot of a design system.
OUTPUT: A `design.json` file containing high-level design guidelines (brand, colors, typography, principles).
SUCCESS_CRITERIA: The generated JSON file accurately captures the key visual elements and principles of the source image.
REUSABLE_IN: [
  New app kickoff projects,
  Website redesigns,
  Brand identity creation,
  Component library setup
]
code
Code
TASK: GENERATE_UI-COMPONENT_SHOWCASE-APP
TASK_ID: TBD
DEPARTMENT: Development / AI
ACTION: Generate
OBJECT: UI Component Showcase App
CONTEXT: Based on an initial design style guide
COMPLEXITY: Medium
TIME_ESTIMATE: 5-10 minutes
PARENT_PROJECT: AI_App_Design_System_Setup
STEPS_USED: [
  REFERENCE_DESIGN_JSON_IN_PROMPT,
  EXECUTE_SHOWCASE_APP_GENERATION_PROMPT,
  RUN_APP_LOCALLY,
  REVIEW_GENERATED_UI_COMPONENTS
]
SKILLS_REQUIRED: [
  "generated UI components via Cursor",
  "built web apps via Vite"
]
TOOLS: [Cursor, Claude/Sonnet 4.5, Vite, React, Tailwind CSS]
INPUT: `design.json` file and a prompt to build a mock dashboard.
OUTPUT: A running local instance of a Vite+React app displaying all standard UI components (buttons, cards, calendar, etc.) styled according to the `design.json` file.
SUCCESS_CRITERIA: App runs locally and visually represents the intended design style across all components.
REUSABLE_IN: [
  Creating a live style guide,
  Prototyping new features,
  Testing component variations
]
code
Code
TASK: CREATE_COMPREHENSIVE_DESIGN-SYSTEM_GUIDE
TASK_ID: TBD
DEPARTMENT: Design / AI
ACTION: Create
OBJECT: Design System Guide
CONTEXT: As a detailed JSON file for AI consumption
COMPLEXITY: Medium
TIME_ESTIMATE: 2-5 minutes
PARENT_PROJECT: AI_App_Design_System_Setup
STEPS_USED: [
  ITERATE_ON_SHOWCASE_APP_DESIGN,
  EXECUTE_COMPREHENSIVE_GUIDE_GENERATION_PROMPT,
  SAVE_DESIGN-SYSTEM_JSON
]
SKILLS_REQUIRED: [
  "created design systems via GPT-5"
]
TOOLS: [Cursor, GPT-5]
INPUT: The initial `design.json` file, the code for the showcase app, and a prompt to create a final, detailed guide.
OUTPUT: A `design-system.json` file with detailed definitions for every UI component, style, and design principle for the app.
SUCCESS_CRITERIA: The generated file is detailed enough to be used by an AI to consistently build new features matching the established design language.
REUSABLE_IN: [
  Onboarding new developers,
  Maintaining brand consistency across projects,
  Automating UI generation for new features
]
4C. Step Templates Extraction
code
Code
STEP: SEARCH_DRIBBBLE_FOR_INSPIRATION
STEP_ID: TBD
ACTION: Search
OBJECT: Design Inspiration
TOOL: Dribbble
PARENT_TASKS: [EXTRACT_DESIGN-STYLE_FROM_IMAGE]
COMPLEXITY: Low
TIME_ESTIMATE: 2-5 minutes
INPUT: Search term "design system".
OUTPUT: A list of visual examples of design systems.
PREREQUISITES: [Access to Dribbble.com]
INSTRUCTIONS:
  1. Navigate to Dribbble.com.
  2. Use the search bar to look for "design system".
  3. Browse the results for a suitable inspiration image.
REUSABLE_IN: [Any design or branding task requiring visual research.]
code
Code
STEP: SELECT_FLAT_DESIGN_SYSTEM_SCREENSHOT
STEP_ID: TBD
ACTION: Select
OBJECT: Screenshot
TOOL: Dribbble
PARENT_TASKS: [EXTRACT_DESIGN-STYLE_FROM_IMAGE]
COMPLEXITY: Low
TIME_ESTIMATE: 1 minute
INPUT: Dribbble search results.
OUTPUT: A single, clear screenshot of a design system.
PREREQUISITES: [SEARCH_DRIBBBLE_FOR_INSPIRATION completed]
INSTRUCTIONS:
  1. From the search results, look for an image that is "pretty flat".
  2. Ensure the image clearly shows a variety of UI components (buttons, cards, forms).
  3. Avoid images that look like posters or are overly stylized with extra elements (e.g., dashed borders not part of the UI).
  4. Copy the selected image to the clipboard.
REUSABLE_IN: [Tasks requiring a clean visual reference for AI analysis.]
code
Code
STEP: EXECUTE_DESIGN_ANALYSIS_PROMPT
STEP_ID: TBD
ACTION: Execute
OBJECT: AI Prompt
TOOL: Cursor (with GPT-5)
PARENT_TASKS: [EXTRACT_DESIGN-STYLE_FROM_IMAGE]
COMPLEXITY: Low
TIME_ESTIMATE: 1-2 minutes
INPUT: Screenshot and a specific prompt to analyze the design.
OUTPUT: A `design.json` file with high-level design guidelines.
PREREQUISITES: [Screenshot copied, Cursor open]
INSTRUCTIONS:
  1. Open the "Agents" view in Cursor.
  2. Paste the screenshot into the chat.
  3. Use the prompt: "Deeply analyze the design of the attached screenshot to create a design.json file..."
  4. Ensure the AI model is set to GPT-5.
  5. Run the prompt and save the generated `design.json` file.
REUSABLE_IN: [Any workflow that starts with visual analysis to generate structured data.]
code
Code
STEP: EXECUTE_SHOWCASE_APP_GENERATION_PROMPT
STEP_ID: TBD
ACTION: Execute
OBJECT: AI Prompt
TOOL: Cursor (with Claude/Sonnet)
PARENT_TASKS: [GENERATE_UI-COMPONENT_SHOWCASE-APP]
COMPLEXITY: Medium
TIME_ESTIMATE: 5-10 minutes
INPUT: `design.json` file and a prompt to build a Vite+React app.
OUTPUT: A fully coded Vite+React app project.
PREREQUISITES: [`design.json` file exists in the project]
INSTRUCTIONS:
  1. Create a new agent chat in Cursor.
  2. Set the model to Claude/Sonnet 4.5.
  3. Use the prompt: "Let's make a simple screen that contains every UI component... following the design style outlined in @design.json..."
  4. Add the `design.json` file to the chat context using the "@" symbol.
  5. Specify the tech stack (Vite, React, Tailwind CSS).
  6. Instruct the AI to run the app locally.
  7. Approve the terminal commands the AI wants to run.
REUSABLE_IN: [Prototyping, building demo applications, creating component libraries.]
4D. Project Templates Extraction
code
Code
PROJECT: AI_App_Design_System_Setup
PROJECT_ID: TBD
DEPARTMENT: Design / Development
DESCRIPTION: A repeatable project to establish a consistent and high-quality design system for a new AI-built application, starting from a single inspiration image.
DURATION: Less than 1 hour.
COMPLEXITY: Medium

PHASE 1: Style Extraction and Definition
  DESCRIPTION: Analyze visual inspiration to create a foundational style guide.
  DURATION: 5-10 minutes
  OUTPUT: A `design.json` file with high-level brand and style attributes.

  MILESTONE: Initial Design Language Captured
    DESCRIPTION: Generate a machine-readable file describing the core design aesthetic.
    DELIVERABLE: `design.json` file.
    TASKS:
      - TASK: EXTRACT_DESIGN-STYLE_FROM_IMAGE (TIME: 1-2 min)
        STEPS: [
          SEARCH_DRIBBBLE_FOR_INSPIRATION,
          SELECT_FLAT_DESIGN_SYSTEM_SCREENSHOT,
          PASTE_SCREENSHOT_INTO_CURSOR,
          EXECUTE_DESIGN_ANALYSIS_PROMPT
        ]

PHASE 2: Component Showcase and Refinement
  DESCRIPTION: Build a live example of the design system components for review and iteration.
  DURATION: 10-15 minutes
  OUTPUT: A locally running web app showcasing all UI components.

  MILESTONE: Visual Components Built
    DESCRIPTION: Generate a mock dashboard application that uses the extracted design style.
    DELIVERABLE: A running Vite+React application.
    TASKS:
      - TASK: GENERATE_UI-COMPONENT_SHOWCASE-APP (TIME: 5-10 min)
        STEPS: [
          REFERENCE_DESIGN_JSON_IN_PROMPT,
          EXECUTE_SHOWCASE_APP_GENERATION_PROMPT,
          RUN_APP_LOCALLY,
          REVIEW_GENERATED_UI_COMPONENTS
        ]

PHASE 3: Comprehensive Guide Generation
  DESCRIPTION: Create a final, detailed design system document for ongoing development.
  DURATION: 5-10 minutes
  OUTPUT: A comprehensive `design-system.json` file.

  MILESTONE: Final Design System Documented
    DESCRIPTION: Generate a detailed JSON file that consolidates all design rules for future AI tasks.
    DELIVERABLE: `design-system.json` file.
    TASKS:
      - TASK: CREATE_COMPREHENSIVE_DESIGN-SYSTEM_GUIDE (TIME: 2-5 min)
        STEPS: [
          ITERATE_ON_SHOWCASE_APP_DESIGN,
          EXECUTE_COMPREHENSIVE_GUIDE_GENERATION_PROMPT,
          SAVE_DESIGN-SYSTEM_JSON
        ]
5. Action Verbs & Operations
A. CREATION VERBS
Create, Build, Design, Make, Write
B. MODIFICATION VERBS
Update, Change, Tweak, Refactor, Translate
C. ANALYSIS VERBS
Analyze, Find, Search, Look at, Check, Review
D. ORGANIZATION VERBS
Organize, Structure, Plan
E. COMMUNICATION VERBS
Teach, Show, Advise, Describe, Instruct, Outline
F. BROWSER/AGENTIC OPERATIONS
Automates, Executes, Runs, Opens, Clicks, Selects, Fills in, Follows, Builds
G. DATA OPERATIONS
Extract, Generate, Capture, Add, Paste, Copy, Save, Read
6. Task Chains
code
Code
TASK CHAIN: 3-Prompt Design System Generation
[Find inspiration on Dribbble] → [Prompt 1: Extract high-level style to design.json (GPT-5)] → [Prompt 2: Build showcase app from design.json (Claude/Sonnet)] → [Prompt 3: Create comprehensive design-system.json from all components (GPT-5)] → [Final Design System Guide]
7. Responsibilities Vocabulary
7A. Professional Roles Mentioned:
Designer
Product Advisor
Startup Advisor
App Builder
Creative Director
Developer
7B. Skills Extraction
code
Code
SKILL: ANALYZE_DESIGN-STYLES_VIA_CURSOR
SKILL_ID: TBD
SKILL_PHRASE: "analyzed design styles via Cursor"
DIFFICULTY: Beginner
PROFESSIONS: [UI/UX Designer, AI Prompt Engineer, Frontend Developer]
PARENT_TASKS: [EXTRACT_DESIGN-STYLE_FROM_IMAGE]
WORKFLOWS: [AI-Assisted Design System Generation]
TOOLS_REQUIRED: [Cursor, GPT-5]
TIME_TO_LEARN: 10 minutes
DESCRIPTION: The ability to use Cursor with GPT-5 to analyze a screenshot of a UI and extract its core design principles, colors, typography, and spacing into a structured format like JSON.
code
Code
SKILL: GENERATE_UI-COMPONENTS_VIA_CURSOR
SKILL_ID: TBD
SKILL_PHRASE: "generated UI components via Cursor"
DIFFICULTY: Intermediate
PROFESSIONS: [Frontend Developer, AI Engineer, Full-Stack Developer]
PARENT_TASKS: [GENERATE_UI-COMPONENT_SHOWCASE-APP]
WORKFLOWS: [AI-Assisted Design System Generation]
TOOLS_REQUIRED: [Cursor, Claude/Sonnet, Vite, React, Tailwind CSS]
TIME_TO_LEARN: 1-2 hours
DESCRIPTION: The ability to prompt an AI coding assistant (Cursor with Claude/Sonnet) to build a functional web application (e.g., a mock dashboard) based on a provided style guide (`design.json`), correctly implementing all specified UI components and styling.
code
Code
SKILL: CREATE_DESIGN-SYSTEMS_VIA_GPT-5
SKILL_ID: TBD
SKILL_PHRASE: "created design systems via GPT-5"
DIFFICULTY: Intermediate
PROFESSIONS: [Lead Designer, Design Systems Engineer, AI Prompt Engineer]
PARENT_TASKS: [CREATE_COMPREHENSIVE_DESIGN-SYSTEM_GUIDE]
WORKFLOWS: [AI-Assisted Design System Generation]
TOOLS_REQUIRED: [Cursor, GPT-5]
TIME_TO_LEARN: 30 minutes
DESCRIPTION: The ability to synthesize an initial style guide and a codebase of implemented components into a single, comprehensive design system document (JSON format) that can be used as a definitive reference for future AI-driven development.
7C. Responsibilities/Activities:
"Designing apps"
"Advising startups on product and design"
"Building apps with AI"
"Following a style guide"
"Creating a mock dashboard"
8. Tools & Technologies Matrix
Tool Name	Category	Purpose	Used For	Mentioned With
Dribbble	Design Inspiration	A platform for designers to share their work.	Finding visual inspiration for design systems.	-
Cursor	AI Coding Environment	An AI-first code editor.	Running prompts, generating code, browsing the local app.	GPT-5, Claude/Sonnet, Vite, React
GPT-5	AI Model (OpenAI)	Advanced AI model for analysis and generation.	Analyzing design screenshots and creating detailed guidelines.	Cursor
Claude/Sonnet	AI Model (Anthropic)	Advanced AI model, strong in coding tasks.	Generating the React/Vite/Tailwind showcase app code.	Cursor
Vite	Web Development Tool	A modern frontend build tool.	Setting up and running the React showcase app.	React, Tailwind CSS
React	JavaScript Library	A library for building user interfaces.	Creating the components of the showcase app.	Vite, Tailwind CSS
Tailwind CSS	CSS Framework	A utility-first CSS framework for styling.	Applying the extracted design style to the app components.	React, Vite
JSON	Data Format	A lightweight data-interchange format.	Storing the structured design system guidelines.	Design System
Lovable / Bolt	AI App Builders	Platforms for building apps with AI.	Alternative tools for applying the generated design system.	Cursor
Skool	Community Platform	Platform for hosting online communities and courses.	Hosting the "AI App Builders Academy".	-
9. Objects & Deliverables
Design System: The complete set of components, styles, and guidelines.
UI Components: Individual elements like buttons, cards, forms, calendars, toggles.
Style Guide: The comprehensive document (design-system.json) detailing all design rules.
Showcase App: A mock dashboard application built with Vite and React to demonstrate the design system.
JSON Files: design.json and design-system.json used to store structured design data.
Prompts: The specific text instructions given to the AI.
Code Files: The set of files making up the Vite/React project.
10. Integration Patterns
code
Code
INTEGRATION: Dribbble + Cursor (GPT-5) + Cursor (Claude/Sonnet)
PURPOSE: To create a complete, AI-ready design system from a single image.
FLOW: [Inspiration Screenshot (Dribbble)] → [becomes] → [Input for Prompt 1 in Cursor (GPT-5)] → [Output: high-level `design.json`] → [becomes] → [Input for Prompt 2 in Cursor (Claude/Sonnet)] → [Output: Showcase App] → [becomes] → [Input for Prompt 3 in Cursor (GPT-5)] → [Final `design-system.json` guide]
11. Business Concepts & Strategy
Design Consistency: The core strategy is to use a comprehensive design system to ensure that an AI coding tool builds all new features with a consistent look and feel.
Improving AI Output Quality: The process is designed to overcome the common problem of AI generating generic or poor-quality designs ("same old purple gradients").
Scalable Design: By creating a machine-readable guide (.json), the design can be easily applied and scaled across an entire application by an AI agent, saving significant development time.
AI-First Workflow: The entire process is tailored for an AI-first development environment, where the design guide is created specifically for an AI to consume and follow.
12. Optimization & Best Practices
code
Code
OPTIMIZATION: AI Design Input
TECHNIQUE: Use a "pretty flat" screenshot of a design system from Dribbble, not an overly stylized or poster-like image.
REASON: A clean, clear input with distinct UI components prevents the AI from getting confused by extraneous visual elements (like borders or complex backgrounds) and allows for a more accurate extraction of the core design language.
EVIDENCE: [02:22 - 02:45]
code
Code
OPTIMIZATION: AI Task Separation
TECHNIQUE: Use different AI models for different tasks: GPT-5 for visual analysis and guideline creation, and Claude/Sonnet for code generation.
REASON: Different models have different strengths. GPT-5 is better at visual interpretation, while Claude models are often better at writing structured code. This specialization leads to better results for each step.
EVIDENCE: [05:12 - 05:33]
code
Code
OPTIMIZATION: Workflow Context Management
TECHNIQUE: Create a new agent/chat for each distinct task in the workflow (e.g., one for analysis, one for app building).
REASON: This clears the chat context and prevents the AI from getting confused by previous, irrelevant instructions, leading to more focused and accurate output for the current task.
EVIDENCE: [10:31 - 10:46]
13. Reusability Analysis
Task Reusability:
code
Code
TASK: EXTRACT_DESIGN-STYLE_FROM_IMAGE
REUSABLE_IN:
  - Quickly creating a theme for a new website.
  - Generating brand guidelines for a marketing campaign.
  - Prototyping different visual directions for a client.
  - Creating a style guide for an existing app by screenshotting it.
VARIATIONS:
  - EXTRACT_COLOR-PALETTE_FROM_IMAGE (a simpler version focused only on colors).
  - EXTRACT_TYPOGRAPHY-RULES_FROM_WEBSITE (providing a URL instead of an image).
Step Reusability:
code
Code
STEP: EXECUTE_DESIGN_ANALYSIS_PROMPT
REUSABLE_IN:
  - Any task that needs to convert visual information into a structured data format.
  - Analyzing user-uploaded images to extract properties.
  - Creating metadata from product photos.
SIMILAR_STEPS:
  - EXECUTE_CODE_ANALYSIS_PROMPT (analyzing code instead of an image).
  - EXECUTE_TEXT_ANALYSIS_PROMPT (extracting entities and concepts from text).
14. Success Metrics & Performance Data
code
Code
METRIC: Design Quality
WORKFLOW/TASK: AI-Assisted Design System Generation
VALUE: "Incredible looking design"
CONTEXT: Compared to the "same old purple gradients" often produced by generic AI coding tools.
BENCHMARK: The goal is to match the quality of a professionally designed system found on Dribbble. The generated showcase app is "almost identical" to the inspiration.
code
Code
METRIC: Design Consistency
WORKFLOW/TASK: AI-Assisted Design System Generation
VALUE: A comprehensive guide that an AI can follow "step by step".
CONTEXT: This ensures all future features built by the AI will adhere to the same design language, preventing visual fragmentation.
BENCHMARK: Manual development, where consistency can drift over time. This system enforces consistency programmatically.
code
Code
METRIC: Development Speed
WORKFLOW/TASK: AI-Assisted Design System Generation
VALUE: The entire process from inspiration to a running showcase app and a detailed design system is completed within the video's timeframe (a few minutes per prompt).
CONTEXT: This is significantly faster than a manual process of documenting a design system and coding components from scratch.
BENCHMARK: Manual design system creation and implementation can take days or weeks. This workflow reduces it to under an hour.

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
