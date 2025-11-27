---
category: 02_TRANSCRIPTIONS
subcategory: root
type: transcript
source_id: Video_005
title: Video 005
date: 2025-11-21
status: draft
owner: unknown
related: []
links: []
---

# Video 005

## Summary
- TODO

## Context
- TODO

## Data / Content
# Video Transcription - My Agentic Engineering Tech Stack

### 1. Metadata Section
- **Video Title**: My Agentic Engineering Tech Stack
- **Channel/Creator**: Cole
- **Video URL**: [Not Provided]
- **Duration**: 34:24
- **Publication Date**: [Not Available]

### 2. Description Section
- **Description**: [Not provided]
- **Key Topics**:
  - Agentic Engineering Tech Stack Overview
  - Core Infrastructure (Database, Caching, AI Coding, Prototyping)
  - General AI Agents (AI Agent Framework, Multi-Agent Framework, Tooling, Observability)
  - RAG Agents (File Extraction, Data Extraction, Vector Database, Memory, Knowledge Graphs)
  - Web Automation Agents (Browser Control, Automations, Crawling, Scraping)
  - Full Stack Development (API, Database, Authentication, Frontend)
  - Deployment & Infrastructure (CI/CD, Testing, Code Review, Hosting)
  - Self-Hosting Options
- **Links Referenced**:
  - The speaker mentions he will link to other videos on his channel for specific tools like `Archon`, `Docling`, `Mem0`, and `Arcade` + `LangGraph`.

### 3. Word-for-Word Transcription

[00:00] At this point, I have basically already covered all the technologies that I use throughout my content. But what I have never done before is created a single video going over my entire tech stack and why I use the tools that I use. And so that, my friend, is what I have for you today. So if you're looking to build any software going into 2026, listen up, because I got some really solid recommendations for you.

[00:23] My tech stack is AI first because I really don't see another way to do it these days. And I've been using pretty much the same tech stack, except for some of the newer technologies, for over a year now. So it doesn't change often. It is very stable. And I consider this a good thing. In fact, before we even get into all of the individual tools here, the biggest recommendation that I have for you is to find what works well for you and just stick with it.

[00:50] Now, you still want to be flexible. Like sometimes there are tools outside of your normal stack that will solve a problem better. You want to do that, but generally just finding what works well for you. The mantra that I always have is capabilities over tools. And what that means for this video specifically is instead of this being like, oh, let's dive into the nitty-gritties of every single tool here and obsess over them, I more just want this to be a resource for you.

[01:13] If there's ever a certain technology as a part of your stack that you're unsure of, then just take my recommendations so you can get right into solving the actual problem, building the actual software instead of worrying about the tools because in the end, problems come first. And so that's what I have for you in this video.

[01:32] All right, so here's how I have things laid out for you in categories. I'm going to start by going over my core infrastructure, the technologies that apply to basically anything that I am building. And then I have things split into the different types of applications. So the tech I use for basically all my AI agents, what I use for RAG agents specifically, then agents based around web automations. Then I'll get into my full stack development tech stack. And then I'll end things off with some deployment and infrastructure, and then also self-hosting options for things I haven't already covered because local AI is a big part of what I do as well.

[02:06] And for each of the technologies, I'm also going to be covering alternatives. Like a couple of alternatives for Postgres, for example. I think this will really help frame how the technology fits into my stack and also just show you that I'm not just trying to give you one tool as the end-all-be-all. I want to talk about some alternatives and how that relates to what I end up using and why I use that over some of the other options out there.

[02:29] So kicking things off with my core infrastructure, the foundation that powers everything. [TEXT: Python and TypeScript are my main programming languages btw, probably fits into "Core Infrastructure"] Not that I use these technologies all of the time, but they apply to every type of software that I build. So for my database, most of the time I am using Postgres. And I'm either using it through Neon or Superbase generally. So they are both platforms that host Postgres under the hood. And I've been using Superbase for longer, but experimenting with Neon more recently, especially because of their scalability.

[02:57] [VISUAL: Speaker shows the Supabase and Neon dashboards, which look similar.] They both look very similar and operate similarly. Like this is my dashboard for Superbase, this is the one for Neon, both running Postgres under the hood. And then I also have Postgres through Superbase as a part of the local AI package. So a lot of the stack that I cover today that's open source, I have that as a part of this single package for you to run everything on your own hardware.

[03:19] And so, yeah, Postgres is fantastic. And for anything that's open source going forward, by the way, I'll have this check mark and OSS label right here, so I don't have to just like say it every single time because that is one of the benefits of a lot of the things that I'm covering in this video. As far as alternatives, we have MongoDB and Firestore. And so just speaking to a couple of no SQL alternatives. And I used to be a big Firestore guy, even using MongoDB a bit, maybe like four or five years ago, and I switched a lot more to SQL recently because it's definitely the industry standard for building AI agents. And I feel like LLMs understand SQL a lot more than writing queries for no SQL like Firestore or MongoDB. And because of pricing and scaling, I know a lot of people including myself that have switched to SQL and Postgres is just the standard for that.

[04:05] So that is my database that powers most things. We'll see Postgres a lot going forward as well. And then for caching specifically, I use Redis. It is blazing fast. And then also we have Valkey as an open-source alternative. That's one of the things I have in the local AI package and it's completely compatible. So I can use Redis if I want something hosted and convenient, but then always switch to something local if I want. And oh, did I mention that it is blazing fast? So, great tool for caching.

[04:34] And then for my AI coding assistant, honestly probably the tool that I have open most up on my computer is Claude Code. And I'm always using it with Archon, which is my open source project. I'll link to a video right here. It's knowledge and task management for AI coding assistants. And so this enhances my AI coding experience a lot. But Claude Code is my primary driver. There are some fantastic alternatives like Cursor with their new 2.0. Codex is definitely catching up to Claude Code, but right now it is generally considered the best AI coding assistant, though it is a bit pricier and has some rate limit issues that people are dealing with right now, but it is still my daily driver. And just the features they have around slash commands and subagents and the new Claude skills is very, very cool. And so I'm using Archon along with it for everything that I'm creating. Like literally all of the different types of software that you'll see in the rest of this video, I'm building it with the help of Claude Code.

[05:27] And as much as I'm using AI coding assistants all of the time, I still love using no-code tools to help me prototype what I'm building, especially when I'm creating AI agents. And there are some good alternatives like LangFlow and Flowise. I even cover Flowise on my channel one time and it's also in the local AI package. But n8n for me is where it's at and I feel like it's going to be like that long term. It is a phenomenal platform that I've covered so much on my channel, building things like RAG agents like you're looking at right here. And so I'll use it as a tool to quickly prototype ideas, validate the tools I'm giving my agents and system prompts and things like that. And then I'll usually move to a coded solution once I'm confident in my prototype. And n8n is great because of all their app integrations. It's very AI focused. They're building in features all the time to help with creating agents. And of course, it's open source and self-hostable. And again, I'm not going to mention that as a benefit going forward, but you'll see the label right here.

[06:19] And as we move on from core infrastructure, the last thing I want to say as I'm going through everything here is that obviously I'm not listing every alternative, but I just want to list a couple to help frame the conversation. And then also for some tools, I don't actually have alternatives because I just haven't tried something comparable or I just genuinely don't think there's another tool worth looking into. And so with that, that'll take us into the next category here for the tools that I'm using for all of the AI agents that I create.

[06:47] Now, for my AI agent framework, right now I'm pretty much exclusively using Pydantic AI, which people ask me why all of the time because there are so many good alternatives, even using no framework at all. A lot of people like just using raw LLM calls and I respect that as well because a lot of these frameworks are what I like to call an abstraction distraction. You end up fighting the framework more than it's actually helping you because it's hard to really customize things once you get into the nitty-gritty of building your agents. But I feel like I don't have that issue with Pydantic AI. It's a lot easier for me to build agents than just raw LLM calls, especially when I'm swapping between different providers, but I still feel like I have all the flexibility and control that I need as if I was doing raw LLM calls.

[07:32] Plus, Pydantic AI is constantly supporting new protocols like MCP when that first came out, A2A for UI event streams, we have AGIUI, the new Vercel data streaming protocol. It's easy to just build on top of the latest in AI thanks to Pydantic AI.

[07:49] And then for multi-agent specifically, I love using LangGraph. And a lot of times I'll be actually using these two together. So Pydantic AI is how I create my individual agents, and then LangGraph is how I connect them together in more complex workflows when the use case actually calls for multi-agent. I don't want to over-engineer and always do multi-agent. So I'm only using LangGraph for the more complex use cases, but it is a lifesaver. It is so easy to manage state, human in the loop for more complex workflows, routing between my different agents, graph persistence, they have a user interface to help us visualize our graphs. LangGraph is awesome.

[08:26] And there are some alternatives. A lot of people love using CrewAI for building multi-agent. Pydantic AI graphs, so I could actually use the same framework to build multi-agent that I use for building single, but I feel like LangGraph is just the most mature, handling some of the core components of these more complex workflows like human-in-the-loop for example.

[08:45] Now, frameworks like Pydantic AI make it very easy to add tools into our AI agents. But what they don't handle is agent authorization and tool security. That is where Arcade comes in. And so for example, if your AI agent needs to get permission to access a user's account, like to view emails in their Gmail, send a message on their behalf in Slack, the agent needs some sort of way to authorize with those accounts and that is where Arcade comes in. That is a very hard thing to engineer without a tool like Arcade. And I don't actually know of any alternatives that do it the way that they do. Plus, they've recently released an MCP server SDK so we can build secure MCP servers directly with Arcade, leveraging their toolsets, leveraging their tool authorization right within the platform.

[09:31] And so I'll actually show you the docs really quickly. They have this entire guide now how we can build our own MCP servers. So it's basically building MCP servers like Fast MCP, if you've ever built a server in Python with that before, but now we can bake in the Arcade tool authorization right into these servers. And so this is a Reddit example. We got different tools to like get subreddit posts for example, get post content. But then for the ones that need authorization specifically, we just add this decorator here. So that when we call this tool, it's going to send a user through an OAuth flow. So the agent has access to their Reddit account to, for example, get their username, or submit a text on their behalf. So our agent can do things for individual users now. That's the kind of authorization that's very hard to engineer for without something like Arcade.

[10:19] And in a video on my channel that I'll link to right here, I did a demonstration incorporating Arcade into LangGraph. So I have this AI agent where for example, I can say, what emails do I have from today? And take a look at this. The agent doesn't have access to my account yet. And so it sends me this link. So I click on this link to go through an OAuth flow. So I go through this, I sign into Arcade. Now the AI agent going forward is going to have access to my account to do things on my behalf, but also just with the permissions that I set up in the application. So it's also very secure, very granular. And so authorization successful. Now if I go back to my agent, it's going to list out my emails.

[10:58] And you can do this whole OAuth flow directly through MCP as well. I just wanted to show you the example from my longer video in case you're interested in checking that out. But yeah, the last thing that is core to all of my AI agents is Langfuse. This is for agent observability. And you cannot skip this step. It is so important, especially when your agents are running in production, to be able to monitor them.

[11:20] So for every single run, you can see the token usage, the total cost, the latency, the tool calls that your agents are making. And with their LangGraph integration, so just like Arcade, they integrate with LangGraph. All my tools work very well together. You can also see the different agents in a multi-agent system and the decisions that are made, like what agents are being routed to in this execution. So without something like this, there's no way to set up evaluations, AB test our system prompts for example. When you're serious about making your agents reliable, you need a tool like this for observability.

[11:51] There are some other good options as well like LangSmith and Helicone for example, but I find Langfuse to be the most feature rich and LangSmith is very popular but also not 100% open source and self-hostable. And so that's one of the things I love about Langfuse. It's another one of those technologies that I have in the local AI package as well.

[12:08] Next up, I want to talk about all the tools that I'm using for RAG agents specifically. So I just covered what I use for all AI agents. So these four do apply in general to RAG agents too, but now these are tools specifically for data extraction, we have data storage, knowledge graphs, and then evals and even web search I would include in RAG.

[12:29] And so first of all, for data extraction, you don't always need a framework. But for more complex documents specifically, like PDFs with diagrams, Excel files, it's helpful to have something out of the box like Docling to help. And there are some good alternatives like LlamaIndex has a lot. It's a agent framework specifically for RAG. We've got Unstructured, but man, Docling has been crushing it for me pretty recently. This is actually one of the newest additions to my tech stack. A lot of before I've just been kind of doing manual extraction without a framework, but this has just made it so much easier for me.

[13:01] And it's easy to use self-hosted models and it's completely open source unlike a lot of data extraction tools. And then for website data specifically, I use Crawl4.AI. It's very fast and efficient. It automatically cleans junk. They have LLM integrations. You can send it into a website and use an LLM and just kind of like ask it for what text you want to extract specifically. So it's very, very feature rich. And so think of it this way, and I'll go to the documentation here. If you are working with files, use Docling. If you are working with websites, use Crawl4.AI. That's my decision process. These are the two core tools that I use for data extraction specifically.

[13:40] And then for storage, I love using Postgres. So not only is it my regular database that powers all my applications, but thanks to PGVector, I can basically use Postgres as a vector database. Now it's not a dedicated vector database, like something like Qdrant or Pinecone. These are alternatives that are going to be faster. So it is a tradeoff. When you have a dedicated vector database, they are faster. But the reason I like using Postgres is a lot of my RAG strategies need a regular database too. They just need a SQL database to store document data or to store user data as it relates to RAG. And so that kind of thing I really like using Postgres for and it also scales extremely well.

[14:23] And then for long-term memory specifically, the reason I have this here in my RAG agent tools is because long-term memory is just a form of RAG. It's an implementation of RAG. And I love using Mem0. I covered this on my channel as well. By the way, I'm going to keep linking to videos that relate to these technologies because like I said, I have most covered most of them in my content already. But I love Mem0 because it integrates with really any database that I want. So I can use Mem0 directly with PGVector, which is very nice. They're right next to each other and they also integrate together. And it's just super easy to add into any agent. So there are some other great long-term memory frameworks. Leda is one example that I'm not putting here because it's actually more of an AI agent framework focused on long-term memory, but Mem0, we can incorporate this with any AI agent. Like I can build my agent with Pydantic AI and then I can search for memories, inject them into the system prompt and then extract memories after. So I can kind of just sandwich my agent no matter how I build it with Mem0. And then Zep is an alternative that is not open source like Mem0, which is why I generally prefer it.

[15:28] And so that is long-term memory. Now I want to get on to the fun part here with knowledge graphs. A lot of content I've done on knowledge graphs recently. And so for knowledge graphs, there's really two parts. We have the graph database. What I like to call the engine. I love using Neo4j. They have a really beautiful UI. It's easy to query through our data and work with it. And then also one of the great things with Neo4j is that it is supported by most knowledge graph libraries, like a couple that I'm going to talk about in a second here. It's also very high speed and very, very scalable. Now the licensing is not ideal for Neo4j, even though it is open source. So when you get into commercial use, it's something to look into if you're interested in Neo4j. There are some great alternatives as well like Memgraph and FalkorDB.

[16:20] And now for the library to help us insert data into Neo4j and search our knowledge graphs here, I love using Graphiti. Covered this on my channel as well. It's very intelligent entity and relationship extraction. And so going back to our graph here, we have these different entities and then we also have information or metadata for how they relate together. And obviously, unless we have a super specific use case where we can somehow extract this deterministically, we need to use a large language model to extract entities and relationships from raw text. And that is what Graphiti helps us with. So this is where we store the data. This is how we get the data in the format to store and how we search it as well. Lightrag is another alternative. I've covered on my channel quite a bit, but Lightrag is more like vector database and knowledge graph. Graphiti is focused just on knowledge graphs. And I like to have them separated.

[17:17] And so I've even done implementations on my channel where I have agentic RAG. I give an AI agent the ability to search both a vector database and a knowledge graph depending on the user question. It's very powerful stuff. For evaluation, I love using Ragas. I don't I'm not sure if I'm pronouncing it right, Ragas, Ragas, I don't know if I'm pronouncing it right, but I love using it for setting up eval pipelines. So specialized metrics for RAG like faithfulness, relevance, very, very powerful. A tool like Langfuse we can use for agent evals overall, but that's more around like the tool calling of agents. But when you want to look at things like these metrics specifically, that's when Ragas is fantastic.

[17:56] And it also helps with automated test data set generation and works with any LLM provider. And then last but not least here, web search, you could kind of consider this a part of web automation agents, but also this just was the last spot I had to fill in this section and it is a part of RAG, right? Like retrieval augmented generation, it's not just searching your own knowledge, it's just searching the general knowledge, the wider web. And that's what Brave helps me with. And perplexity is another great tool for this as well. I definitely use both. This is more of like a high level faster implementation and then perplexity is more in detail but slower for AI agents to leverage. And Brave is privacy focused and no tracking. So it's not stupid like our AI browsers like Atlas right now. Independent index, so no Google proxy, and they also have AI search functionality built in that I leverage quite a bit.

[18:44] Next up, we got web automation agents. Now the difference between these two is when I do the data extraction, like with Crawl for AI in the web here, it's when I'm pulling documentation ahead of time to store in my knowledge base. But for web automation, this is when I'm giving tools to my AI agent to pull information from the web live. And so sometimes I'll give my agents a Crawl for AI tool so it can extract text from a specific URL live instead of as a part of my RAG pipeline. Firecrawl is another good alternative for this. But yeah, Crawl for AI is open source, fast and so feature rich.

[19:18] And then the one thing it doesn't handle well is social platforms specifically, like LinkedIn, X, Instagram, agents that have to work with that, I'll often use something like Apify or Bright Data. And then for simpler browser automations, when I just want to like quickly code up some automations for web testing or using the playwright MCP server for my AI coding assistant to be able to visually validate website changes it makes, I love using playwright. And then Puppeteer and Selenium are good options as well. I used selenium for years and years and years, but have switched to playwright within the last year here. And so yeah, it's great multi-browser support. It is in my mind the deterministic web automation king. Like I said, the playwright MCP, that's a golden nugget. It's really awesome when you're using coding assistants to work on your front ends.

[20:03] And then last but certainly not least, I saved browser base. When I want to take these things further and have an agent control a browser for me live, that is when I will use browser base. And it is a beautiful tool. I haven't found anything like it. I know there are some alternatives, but like man, this is the king for me. Managed infrastructure, all sessions are recorded and stored. You have the stagehand MCP server where you just with natural language describe a request, it'll spin up this session for you that has anti-bot detection. It's very secure, it's managed infrastructure, it'll go and navigate websites to find the information that you need. And then you can go back later and actually review the session. So I can play the session live to see what it did to extract the information it needed to based on my request. So awesome platform. And then also, they have Director, which by the way, stagehand and Director are all built on top of playwright and they've extended to work with some of the other tools like Puppeteer and Selenium. So it's deterministic web automation, but putting AI on top of it for browser control.

[21:05] So with Director, for example, I could say, get me the latest price for the Body Fortress protein powder on Amazon, just any kind of web task that I have for it. And it'll go and navigate through everything. It'll show me step by step what it did, even screenshots to go along with it. Very, very cool. It gives me the final response at the end. But then the other thing I can do is I can go to the artifacts tab here, I can go to the code and take a look at this. I can actually copy the code directly. So I can bring this into my own code base, my own automations that I have for testing or just web automations in general. It is an awesome platform. And again, it's just using these tools under the hood but applying AI on top. So an example of one, how I'm using these tools that work well together and then also how I have things in my stack that's very AI first because like I said, I don't see another way these days. It's just so powerful the tools that we have access to.

[21:55] So at this point, I've covered basically everything for AI agents specifically because that is where I focus most of my time. But I still do a lot of full stack development as well, especially because our AI agents still need back ends and front ends for a lot of our implementations. Like for example, this is the front end application that I have built for the Dynamus AI Agent Mastery course using pretty much all of the tech that I'll cover with you in the next couple of minutes here. So a chat GPT like interface here to interact with some multi-agent workflows that I have behind the scenes like this one that you're looking at right here that helps us with SEO research and social media research, competitor research, all in parallel. So very cool implementation. This is one of the many implementations that I do in the Dynamus AI agent mastery course. But yeah, I built this pretty much with all of the tech that we're seeing right here.

[22:42] And so for my APIs, I always use Fast API because I like building my AI agents with Python and so I want to have my API framework be Python as well. Flask is also good, but I think that Fast API is more feature rich. And then if you do want to build your agents and back ends with TypeScript, then I think Express is fantastic. And then for my database, Postgres, like usual, not going to cover this again, super, super standard. And then for simpler authentication, Superbase has been crushing it for me for a while now. And I know Neon has this as well, but specifically when I've been using Neon, I haven't been using it for authentication. So yeah, Superbase is my go-to.

[23:20] And then also integrates with Auth0 when you need to have more enterprise authentication, but you still want to be using Superbase as your database. You can still take advantage of the row level security that it offers. But when you have more enterprise needs for MFA, universal login with more providers, enterprise SSO with SAML or Active directory, that's when Auth0 is crucial. And there are some other platforms that are fantastic as well, like Clerk and Okta. I'm going to be fully transparent here. Auth0, like enterprise authentication is the one thing out of pretty much everything in this tech stack where I I picked Auth0 initially and I haven't really tried these other ones. I just know that they are considered to be very fantastic as well. But this is the one that I've been using for the most part if I'm not just sticking with simple Superbase authentication.

[24:08] And then for my front-end library, I am just always using React now. React is just so simple. It's what all of your AI coding assistants will prefer to use and your front-end builders like Lovable that we'll talk about in a second here. And then Vite to go along with that for the build tool. And so React plus Vite just leads to very snappy, quick to build lightweight applications, front ends for things like your AI agents. I have worked with NextJS a lot in the past and I still have a lot of respect for it, but especially because things have changed so much between recent versions, like NextJS 12 to 13, 14, 15, it keeps like breaking my code. And so I've kind of moved away from NextJS to be honest, even though I I like it a lot. Vue is another good option as well.

[24:50] And then for my component library and styling library, a lot of good options, but uh Shad CN has been great for me and then Tailwind CSS for styling as well. And so not much to say on those, those are like pretty standard these days and they work fantastic. And then I love using Claude code for most of my AI driven coding, but the one thing it doesn't do the best for me is creating beautiful UIs. And so I like taking advantage of an agentic front-end builder like Lovable, for example, that has a lot of system prompting for their agent builder behind the scenes on how to actually create UIs that are beautiful. So the kind of thing I could just do in Claude code or my standard coding assistant, but I like using tools like Lovable or Bolt.new or our very own bolt.DIY if you want a completely open source version for an agentic front-end builder. But yeah, Lovable just has great integrations and their new agent mode that's been crushing it for me recently.

[25:44] Uh and then the last UI library that I want to cover is Streamlit. And so this is like the easiest user interfaces you could possibly make because you build it directly in Python. And so I love using this as a tool to prototype things like my AI agents. So I still have a nice user interface to chat with the agent, but I don't have to build a full on React application yet. And so just defining my UIs in Python code, not having to create a back-end front-end kind of connection and things like that. And so my general process for building an AI agent, you can kind of tell from my tech stack here, is I'll start by prototyping the agent in n8n. I'll move it to code but still have a simple front end with Streamlit, and then when I'm ready, I will create a full React application with something like Lovable. And then that's where I'm really starting to build my MVP.

[26:30] And then for app monitoring and analytics, I like using Sentry. PostHog is really popular as well. I've used these this and Google Analytics before. But yeah, Sentry just has really great real-time analytics for like everything that you need and they're working on native AI features, which is why I'm starting to lean towards it over other tools. And just all the integrations they have. And then for payments, I've always used Stripe. And so I guess this is kind of similar to enterprise auth with Auth0 where I know of these other options like Lemon Squeezy and Paddle, but um yeah, Stripe just has the best developer experience from what I know and fantastic documentation.

[27:03] Next up, we've got deployment and infrastructure, everything for getting the code into production. So deployment platforms, things like CI/CD and the testing and AI code review there. And so first up, deployment platforms. And so Render is the simplest one that I lean on a lot because of its simplicity. There are a lot of other platform as a service options like fly.io or Netlify. The thing I like the most about Render, and this is pretty specific, otherwise these are pretty similar, but you can define your infrastructure as code in YAML for Render to make your deployments automated. It's just so easy to use. And also Git-based deployments. So that you can push to a repo to a certain branch, it'll automatically update like your front end for example. It's free to host front ends and scaling pretty much infinitely with their CDN, background workers and cron jobs.

[27:51] The one thing I'll say is that if I have a requirement to go more enterprise for a certain client, for example, because of SLAs or compliance, whatever, and I want to use the, you know, bare bones like AWS or Google Cloud, I do like using Google Cloud, GCP specifically, especially with their serverless functions. It's really, really nice because you don't really have true serverless when you're using a platform as a service like Render.

[28:12] And then when I am running GPU heavy workloads, like running things with local AI that I want to deploy in the cloud, I love using RunPod. There are some alternatives like Tensor Dock if you want something really, really cheap but not quite as reliable. Uh Lambda Labs as well. But yeah, RunPod as far as like super reliable GPU hosting, it is the cheapest from what I know. And then also spot instances for lower cost. And so, yeah, if you're willing to sacrifice some reliability for cost, then you get that as well. And it's just like you can get your GPUs instantly. There's no queue. It's always going to be available for you, at least from my experience. Fantastic platform.

[28:46] And then the last thing for virtual machine specifically. So like Render, they manage the infrastructure for you. If you want to own the machine and manage the machine, then Digital Ocean is what I use. So for example, hosting the local AI package in the cloud, I do that on Digital Ocean. I know a lot of others who like using Hostinger with their KVM offering or Hetzner. Uh Hetzner is very affordable as well. So, yeah, Digital Ocean is a bit of a premium over these two, but very reliable and it's got predictable pricing. I also love the integrations they're starting to add into AI, like they have the app platform for managed DBs and hosting local LLMs. They have things for RAG built into the platform. So very feature rich.

[29:26] And then as far as containerization, which is how I am deploying all of my applications except for some front ends, is I am using Docker. So it really is just like the industry standard for deploying applications, creating isolated environments to run things, uh to fix the works on my machine problem, right? Like sometimes you host an application on your machine or on some VM in the cloud and you have dependencies that are you're relying on those. And so when you go to another machine or another cloud provider, it breaks. But if you have everything in Docker, then it's guaranteed if it works in one place, as long as you have the container up and running, it will work in another place.

[30:03] And uh I know a lot of people like using Podman because of some licensing with Docker that isn't necessarily ideal. So yeah, Podman is a good alternative. I've used this a lot before. Actually my old company that I was working for before I was doing everything with, you know, YouTube and Dynamus, we moved from Docker to Podman because of the licensing cost. It was like hundreds of thousands of dollars for the company. Uh but then we ended up moving back from Podman to Docker. And um this was actually after I left the company. So I just heard from my team after. So I know that Podman isn't quite as robust as Docker, but it is still a good alternative.

[30:37] And then going down to the bottom here for CI/CD, I am always using GitHub actions. It's so simple, integrated right within my repositories that I also always have in GitHub. It's free for public repos, but uh very generous pricing for private repos. And a huge marketplace of actions. And by the way, it's like it is free for the most part for private repos. I think it's just when you're like adding team members. I don't know the pricing exactly, but it's very, very generous and yeah, it's just super easy to get it set up. And AI coding assistants, by the way, are very good at creating the YAML for your GitHub action workflows. They can help you automate things like testing in your GitHub repo.

[31:15] So for Python testing, I'm using Pytest. TypeScript, I'm using Jest. Like super, super standard. Both are really easy to use and help with things like mocking and fixtures that are really important to make your testing reliable and just doing it the right way. Uh and then last but not least in our section here for deployment and infrastructure is AI code review. And I love using Code Rabbit. And so for example, within Archon, my open source tool that I showed earlier for knowledge and task management, every single pull request that we have coming into Archon gets automatically reviewed by Code Rabbit. And man, is it thorough. Honestly, sometimes it's a bit too thorough, but there are ways to customize it within the Code Rabbit dashboard. And the biggest reason that I love using it is because it is completely free for open source repos like Archon. So if it's a public repo, you can get like just infinite AI code reviews that are very detailed completely for free. And it also includes uh security vulnerability detection.

[32:11] And then really quickly, just for some of the open source things that that didn't fit into another section, I love using Open Web UI as a local LLM chat platform. So it's like chat GPT, but it's running completely locally. You can add in your own custom agents through functions and pipelines. It's just really feature rich. They got things like RAG built right into it. Anything LLM is another good option. And then for completely local web search, I like using SearXNG. By the way, all of these I have them incorporated into the local AI package, including Ollama for serving local LLMs. Pretty much any large language model that is open source that you want to run locally, you can do it with Ollama. And then VLLM and LiteLLM are nice as well. I just find Ollama to be the easiest to use and it auto leverages multiple GPUs. So you don't have to set up fancy config and stuff, but there also are some things you can configure for quantization, like they always have all the different quantized versions of the models. You can configure the context limit for your LLMs to protect your memory. Very, very nice.

[33:05] And then for HTTPS and a TLS platform so that I can have my domains for my things that I'm running myself, I love using Caddy. And then traffic and NGINX are great. I find Caddy to be the simplest, which is why I included it here. But yeah, these are great as well. I know some people in the Dynamus community specifically that are gung-ho about using traffic. So yeah, it doesn't matter a ton. I just find Caddy to be the simplest.

[33:27] So there you go, that is my entire agentic engineering tech stack. And remember to just take these as recommendations. The most important thing is for you to find what works for you and just generally stick with it. Be willing to be adaptable as well because remember, the most important thing is to be a problem solver, not someone who's becoming an expert at specific tools. And so just use these recommendations as a way to fill holes in your tech stack if you're not sure what to use. The last thing that I want to say is that naturally, as a content creator, I end up working with some of these teams for the tools that I have chosen to use myself. Browserbase and Arcade are two of those. And so I did reach out to them for this video, especially because there's a lot of different ways to leverage their tools. I just wanted to find how they want me to showcase their tools. And so thanks to them for working with me on that. And so with that, if you appreciated this video and you're looking forward to more things on AI coding and building AI agents, I would really appreciate a like and a subscribe. And with that, I will see you in the next video.

---
# TAXONOMY ANALYSIS

## Workflows Identified

### WORKFLOW 1: Develop and Deploy an AI-Powered Application
**OBJECTIVE**: To build, test, and deploy a full-stack, AI-first software application from scratch.
**STEPS**:
  1. **Prototype** the core AI agent logic using a no-code tool like `n8n`.
  2. **Build** a simple Python-based UI for initial testing using `Streamlit`.
  3. **Develop** the backend API using `FastAPI` and the AI agent framework `Pydantic AI`.
  4. **Develop** the production frontend using `React` and `Vite`, potentially with an agentic builder like `Lovable`.
  5. **Containerize** the application using `Docker`.
  6. **Set up** CI/CD pipelines using `GitHub Actions` for automated testing and deployment.
  7. **Implement** automated testing for Python (`Pytest`) and TypeScript (`Jest`).
  8. **Integrate** automated AI code reviews with `CodeRabbit`.
  9. **Deploy** the application to a hosting platform like `Render` (for simple apps) or `DigitalOcean` (for VMs).
  10. **Monitor** the production application using `Sentry` for analytics and error tracking.
**TOOLS USED**: `n8n`, `Streamlit`, `Pydantic AI`, `FastAPI`, `React`, `Vite`, `Lovable`, `Docker`, `GitHub Actions`, `Pytest`, `Jest`, `CodeRabbit`, `Render`, `DigitalOcean`, `Sentry`.
**INPUT**: Software idea, problem to solve.
**OUTPUT**: A production-ready, full-stack AI application.

### WORKFLOW 2: Build a RAG (Retrieval-Augmented Generation) System
**OBJECTIVE**: To create a system where an AI agent can reason over a knowledge base of documents.
**STEPS**:
  1. **Extract** data from files (PDFs, etc.) using `Docling`.
  2. **Extract** data from websites using `Crawl4AI`.
  3. **Store** and **index** the extracted data as vectors in a `Postgres` database with the `PGVector` extension.
  4. **Store** structured entity-relationship data in a graph database like `Neo4j`.
  5. **Build** the AI agent using `Pydantic AI` to query the vector and graph databases.
  6. **Implement** long-term memory for the agent using `Mem0`.
  7. **Evaluate** the RAG system's performance (faithfulness, relevance) using `Ragas`.
  8. **Monitor** the agent's performance and traces using `Langfuse`.
**TOOLS USED**: `Docling`, `Crawl4AI`, `Postgres (w/ PGVector)`, `Neo4j`, `Graphiti`, `Pydantic AI`, `Mem0`, `Ragas`, `Langfuse`.
**INPUT**: A collection of documents, websites, and raw text.
**OUTPUT**: An AI agent capable of answering questions based on the provided knowledge.

## Action Verbs Extracted

### A. CREATION VERBS (Making new things)
- Build
- Create
- Generate
- Develop
- Code up

### B. MODIFICATION VERBS (Changing existing things)
- Update
- Customize
- Enhance
- Configure

### C. ANALYSIS VERBS (Understanding/Evaluating)
- Analyze
- Review
- Evaluate
- Test
- Examine
- Monitor
- Query
- Search
- Validate

### D. ORGANIZATION VERBS (Structuring/Managing)
- Organize
- Structure
- Manage
- Containerize
- Define
- Set up

### E. COMMUNICATION VERBS (Sharing/Presenting)
- Deploy
- Host
- Showcase
- Describe
- List
- Report
- Serve

## Task Chains

1. **AI Agent Prototyping**: Prototype in `n8n` → Move to code with simple UI (`Streamlit`) → Build full application (`React` + `FastAPI`) → Deploy
2. **Data Ingestion for RAG**: Extract from files (`Docling`) / websites (`Crawl4AI`) → Store in Vector DB (`Postgres` + `PGVector`) → Agent reasons over data
3. **Knowledge Graph Creation**: Extract entities/relationships from text (`Graphiti` + LLM) → Store in Graph DB (`Neo4j`) → Agent queries graph
4. **CI/CD Pipeline**: Push to `GitHub` → `GitHub Actions` triggers → Run tests (`Pytest`/`Jest`) → AI Code Review (`CodeRabbit`) → Deploy to `Render`

## Responsibilities Vocabulary

#### Professional Roles Mentioned:
- Agentic Engineer
- Content Creator
- Problem Solver

#### Responsibilities/Activities:
- "building any software" [00:18]
- "getting everything into production" [27:05]
- "reason over documents" [12:11]
- "access the web" [18:46]
- "monitoring and analytics" [26:30]
- "AI code review" [31:33]
- "building AI agents" [06:46]
- "prototyping what I'm building" [05:34]

#### Skills Mentioned:
- AI Coding
- Full Stack Development
- Web Automation
- Web Testing
- Deployment
- Infrastructure Management
- Agent Observability
- Knowledge Graph Creation

## Tools & Technologies Matrix

| Tool Name | Category | Purpose | Used For | Mentioned With |
|---|---|---|---|---|
| **Postgres** | Database | Relational & Vector Database | Storing application data, RAG documents, vector embeddings | `PGVector`, `Neon`, `Supabase` |
| **Redis** | Caching | In-memory data store | Speeding up application performance | `Valkey` |
| **Claude Code** | AI Coding | AI Coding Assistant | Writing and assisting with code development | `Archon`, `Cursor`, `Codex` |
| **n8n** | Prototyping | No-code/Low-code workflow automation | Prototyping AI agent logic and workflows | `LangFlow`, `Flowise` |
| **Pydantic AI** | AI Agent Framework | Building AI agents | Creating single, structured AI agents | `LangGraph`, `OpenAI Agents SDK` |
| **LangGraph** | Multi-Agent Framework | Orchestrating multiple AI agents | State management, routing, and graph persistence for agent teams | `CrewAI`, `Pydantic AI Graphs` |
| **Arcade** | Agent Tooling | Agent authorization and security | Handling OAuth, tool security, and building secure MCP servers | `MCP Server SDK` |
| **Langfuse** | Agent Observability | Monitoring and tracing AI agents | Tracking token usage, cost, latency, and debugging agent runs | `LangSmith`, `Helicone` |
| **Docling** | RAG - File Extraction | Document parsing and chunking | Extracting text from complex files like PDFs for RAG | `LlamaIndex`, `Unstructured` |
| **Crawl4AI** | RAG - Web Extraction | Web crawler and scraper | Extracting clean data from websites for RAG | `Firecrawl`, `Scrapy` |
| **Mem0** | Long-Term Memory | Persistent memory for AI agents | Allowing agents to remember information across sessions | `Zep` |
| **Neo4j** | Graph Database | Storing and querying graph data | Building knowledge graphs for complex RAG | `FalkorDB`, `Memgraph` |
| **Graphiti** | Knowledge Graph Framework | Building knowledge graphs from text | Extracting entities and relationships using an LLM | `Lightrag` |
| **Ragas** | RAG Evaluation | Evaluating RAG system performance | Measuring faithfulness, relevance, and other RAG metrics | `DeepEval`, `UpTrain` |
| **Brave** | Web Search | Privacy-focused web search | Providing agents with access to web search results | `Perplexity` |
| **Browserbase** | AI Browser Control | AI-driven browser automation | Allowing agents to control a browser with natural language | `Playwright` |
| **Playwright** | Browser Automation | Deterministic web automation and testing | Scripting browser actions for testing and automation | `Puppeteer`, `Selenium` |
| **Apify** | Social Scraping | Data scraping for social platforms | Extracting data from sites like LinkedIn, X, Instagram | `Bright Data` |
| **FastAPI** | API Framework | Building Python-based APIs | Creating the backend for full-stack applications | `Flask`, `Express.js` |
| **Supabase** | Backend as a Service | Simple authentication and database hosting | Simple user authentication and hosting Postgres DBs | `Neon`, `Auth0` |
| **Auth0** | Enterprise Authentication | Identity and access management | Handling enterprise-level SSO, SAML, and MFA | `Clerk`, `Okta` |
| **React** | Frontend Library | Building user interfaces | Creating the frontend for web applications | `Next.js`, `Vue` |
| **Vite** | Frontend Build Tool | Development server and build tool | Bundling and serving frontend applications | |
| **shadcn/ui** | Component Library | UI components for React | Building UIs quickly with pre-built, accessible components | `Material UI`, `Chakra UI` |
| **Tailwind CSS** | Styling Library | Utility-first CSS framework | Styling frontend components | |
| **Lovable** | Agentic Frontend Builder | AI-powered UI generator | Creating UIs by chatting with an AI agent | `v0.dev`, `Bolt.new` |
| **Streamlit** | Simple UI Library | Creating simple web apps in Python | Prototyping UIs for Python-based AI agents | |
| **Sentry** | App Monitoring | Error tracking and performance monitoring | Real-time analytics and monitoring for production apps | `PostHog`, `Google Analytics` |
| **Stripe** | Payments | Online payment processing | Handling payments and subscriptions | `Lemon Squeezy`, `Paddle` |
| **Render** | Deployment Platform | Platform as a Service (PaaS) | Simple, Git-based deployment for web apps and services | `Fly.io`, `Google Cloud` |
| **RunPod** | GPU Platform | Cloud GPU provider | Running GPU-heavy workloads like local LLMs | `TensorDock`, `Lambda Labs` |
| **DigitalOcean** | VM Platform | Cloud infrastructure provider (IaaS) | Hosting virtual machines for full control over infrastructure | `Hostinger`, `Hetzner` |
| **Docker** | Containerization | Container platform | Packaging applications into isolated environments for deployment | `Podman` |
| **GitHub Actions** | CI/CD | Automation platform | Automating build, test, and deployment pipelines | |
| **Pytest** | Python Testing | Testing framework for Python | Writing and running automated tests for Python code | |
| **Jest** | TypeScript Testing | Testing framework for JavaScript/TypeScript | Writing and running automated tests for frontend code | |
| **CodeRabbit** | AI Code Review | Automated code review tool | Reviewing pull requests with AI for quality and vulnerabilities | |
| **Open WebUI** | Local LLM Platform | Self-hosted chat interface | A local, ChatGPT-like interface for interacting with local LLMs | `AnythingLLM` |
| **SearXNG** | Local Web Search | Self-hosted metasearch engine | A private, local alternative to Brave/Perplexity for web search | |
| **Ollama** | Local LLM Serving | Running LLMs locally | Serving and managing local large language models | `vLLM`, `LiteLLM` |
| **Caddy** | HTTPS/TLS Platform | Web server with automatic HTTPS | Serving self-hosted applications with SSL/TLS encryption | `Traefik`, `Nginx` |

## Objects & Deliverables

- AI Agents (General, RAG, Web Automation)
- Full Stack Applications
- APIs (built with `FastAPI`)
- Frontend User Interfaces (built with `React`, `Streamlit`, `Lovable`)
- Knowledge Graphs
- RAG Systems
- Deployed Software (in production)
- Containerized Applications (`Docker` images)
- Automated Test Suites (`Pytest`, `Jest`)
- CI/CD Pipelines (`GitHub Actions`)

## Integration Patterns

**Pattern 1**: `Postgres` + `PGVector`
- **PURPOSE**: To use a single database for both regular relational data and vector embeddings for RAG.
- **FLOW**: Text chunks are converted to vectors and stored in `Postgres`. The agent queries `Postgres` for both structured data and semantically similar vectors.

**Pattern 2**: `Claude Code` + `Archon`
- **PURPOSE**: To enhance the AI coding experience with integrated knowledge and task management.
- **FLOW**: Developer interacts with `Claude Code`, which leverages `Archon` to access a managed knowledge base and track development tasks.

**Pattern 3**: `Pydantic AI` + `LangGraph`
- **PURPOSE**: To build complex, multi-agent systems.
- **FLOW**: Individual agents are defined and structured using `Pydantic AI`. `LangGraph` is then used to define the state and routing logic that connects these agents into a collaborative workflow.

**Pattern 4**: `Browserbase` + `Playwright`
- **PURPOSE**: To create AI agents that can control and interact with a web browser.
- **FLOW**: `Browserbase` provides a high-level, AI-driven API (`Stagehand`) that translates natural language commands into browser actions, which are executed using `Playwright` under the hood.

**Pattern 5**: `n8n` → `Streamlit` → `React`
- **PURPOSE**: A phased approach to application development, from prototype to production.
- **FLOW**: An idea is first prototyped quickly in `n8n` (no-code). It's then moved to a coded but simple UI with `Streamlit` for internal testing. Finally, a full production-grade UI is built with `React`.

## Business Concepts & Strategy

- **AI-First Approach**: The entire tech stack is built around leveraging AI as a core component, not an afterthought. [00:24]
- **Capabilities Over Tools**: The philosophy of focusing on what needs to be achieved (the capability) rather than obsessing over specific tools. The goal is to solve problems, not just use trendy tech. [01:02]
- **Stable Tech Stack**: The strategy of finding a reliable set of tools that work well together and sticking with them to increase development speed and reduce time spent on configuration and debugging. [00:37]
- **Abstraction Distraction**: A concept where overly complex frameworks can hinder development by forcing developers to "fight the framework" rather than build the solution. This justifies choosing simpler, more flexible tools. [07:06]

## Optimization & Best Practices

1. **Find What Works and Stick With It**:
   - **TECHNIQUE**: Choose a stable, reliable set of tools for your core stack and resist the urge to constantly switch to new technologies.
   - **REASON**: This minimizes time wasted on learning curves and configuration, allowing developers to focus on solving the actual business problem.
   - **EVIDENCE**: [00:46 - 00:49]

2. **Phased Prototyping to Production**:
   - **TECHNIQUE**: Start with no-code tools (`n8n`) for rapid prototyping, move to a simple code-based UI (`Streamlit`) for validation, and only then build a full-production application (`React`).
   - **REASON**: This process allows for quick iteration and validation of ideas before investing significant resources into full-stack development.
   - **EVIDENCE**: [26:12 - 26:29]

3. **Use Containerization for Portability**:
   - **TECHNIQUE**: Package all applications and their dependencies into `Docker` containers.
   - **REASON**: This solves the "it works on my machine" problem, ensuring that the application runs consistently across different environments (local, staging, production).
   - **EVIDENCE**: [29:40 - 29:43]

4. **Separate Knowledge Graph from Vector DB**:
   - **TECHNIQUE**: Use a dedicated graph database (`Neo4j`) for structured, relational knowledge and a separate vector database (`Postgres` with `PGVector`) for semantic search.
   - **REASON**: While some tools combine these, keeping them separate provides more specialized capabilities and better performance for each task.
   - **EVIDENCE**: [17:15 - 17:17]

---

## Key Takeaways for Taxonomy

- **New Tools to Add**: `Pydantic AI`, `Archon`, `Langfuse`, `Docling`, `Crawl4AI`, `Mem0`, `Graphiti`, `Ragas`, `Browserbase`, `Lovable`, `CodeRabbit`, `SearXNG`, `Caddy`.
- **New Workflows**: "Develop and Deploy AI Application", "Build RAG System".
- **New Actions**: `Prototype`, `Containerize`, `Monitor`, `Observe`, `Evaluate`, `Authorize`, `Scrape`, `Crawl`.
- **New Responsibilities**: "Agentic Engineering", "Agent Observability", "AI Code Review".
- **Integration Opportunities**: The video is rich with integration patterns, such as `Pydantic AI` + `LangGraph`, `Arcade` + `LangGraph`, `n8n` + `Streamlit`, and `Neo4j` + `Graphiti`. These demonstrate how different layers of the agentic stack connect.

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
