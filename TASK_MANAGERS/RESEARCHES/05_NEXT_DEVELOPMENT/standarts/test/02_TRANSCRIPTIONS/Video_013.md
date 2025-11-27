---
category: 02_TRANSCRIPTIONS
subcategory: root
type: transcript
source_id: Video_013
title: Video 013
date: 2025-11-21
status: draft
owner: unknown
related: []
links: []
---

# Video 013

## Summary
- TODO

## Context
- TODO

## Data / Content
# Andrew Ng’s Agentic AI Course | Crash Course (Save 8 Hours)

### 1. Metadata Section
- **Video Title**: Andrew Ng’s Agentic AI Course | Crash Course (Save 8 Hours)
- **Channel/Creator**: Jenn Jun
- **Video URL**: [https://www.youtube.com/watch?v=R260afA3-3E](https://www.youtube.com/watch?v=R260afA3-3E)
- **Duration**: 30:22
- **Publication Date**: May 20, 2024

### 2. Description Section
- **Description**: I took Andrew Ng’s Agentic AI course for you so that you can learn everything you need to know about Agentic AI in under 30 minutes instead of 8 hours :) This is the most underrated but important topic of AI in 2024 so I highly recommend you spend the time to really learn the concepts.
- **Key Topics**:
  - Introduction to Agentic Workflows
  - Reflection Pattern
  - Tool Use Pattern
  - Practical Tips for Building Agentic AI (Evaluations)
  - Patterns for Highly Autonomous Agents (Planning, Multi-agent systems)
- **Links Referenced**:
  - **HubSpot's free AI Agents resource**: https://clickhubspot.com/6n4
  - **The Ajent No-Code Cohort**: https://www.theajent.com
  - **Twitter/X**: https://x.com/jennjunod
  - **LinkedIn**: https://www.linkedin.com/in/jennjun/
  - **Newsletter**: https://www.theajent.com/newsletter
  - **The Agentic AI Course**: https://www.deeplearning.ai/short-cou...
  - **Building effective agents (Anthropic)**: https://www.anthropic.com/news/buildi...

### 3. Word-for-Word Transcription

[00:00] I took Andrew Ng's agentic AI course for you.
[00:02] So here's the CliffsNotes version to save you the eight hours.
[00:06] I've been really looking forward to this one.
[00:07] But it is not enough for you to just listen to me talk about stuff.
[00:10] So, at the end of this video, I have included a little assessment.
[00:13] Because research shows that immediately reviewing information after you learn it is the best way to retain that information.
[00:18] Now, without further ado, let's go.
[00:21] A portion of this video is sponsored by HubSpot Media.
[00:26] Let's first go over the structure of the course.
[00:28] The agentic AI course has five modules.
[00:31] Module one, introduction to agentic workflows, covers the foundations of agentic AI and is what the rest of the course is built on top of.
[00:38] Module two is a deep dive into the reflection pattern, a common pattern for agentic workflows.
[00:43] Module three covers tool use, another common agentic pattern.
[00:47] The course also covers lots of examples and ways to improve the results.
[00:50] Module four is called practical tips for building agentic AI, and this module is by far the most important module.
[00:57] I have not seen this information, especially on evaluations, being covered to this depth anywhere else.
[01:03] It's what everybody talks about, but nobody has actually really covered it well, and this course does it well.
[01:08] And finally, module five is patterns for highly autonomous agents, where Andrew covers more experimental agentic workflows.
[01:14] A taste for the future.
[01:17] Alright, let's jump into module one, the fundamentals.
[01:20] Starting off by defining agentic AI.
[01:22] An agentic AI workflow is a process where an LLM-based app executes multiple steps to complete a task.
[01:23] An agentic AI workflow is defined as a process where an LLM based app executes multiple steps to complete a task.
[01:30] For example, if you want your agentic AI workflow to help you write an essay on tea ceremonies.
[01:36] First, the LLM will need to come up with an essay outline about tea ceremonies.
[01:40] Then it will need to think to itself, do I need any web research?
[01:43] It decides that it does, and it will then do research on tea ceremonies across different locations and across different times.
[01:50] Next, it will then write a first draft, but that's not good enough.
[01:53] It would then consider what parts would need more revision and more research.
[01:57] Maybe it would even request a human review at this point if it's really quite unsure about tea ceremonies.
[02:02] Then finally, it would revise the draft and have the final draft ready.
[02:05] This is an example of an agentic AI workflow that is less autonomous since it's quite clear what the steps are to be taken in order to get the final result.
[02:14] But you can also have more autonomous agents too.
[02:18] Using the same essay writing agentic workflow, and a more autonomous workflow would look something like you,
[02:24] similarly tell the LLM to, you know, write an essay about tea ceremonies,
[02:28] but instead of directing it to go write an outline and then do the web research and then etc, etc, you can just give the LLM a set of tools
[02:35] like web search and new search, and maybe archive search for more research papers too.
[02:40] And you let the LLM itself decide which tool it's going to use to gather the right information,
[02:45] find the best sources, compile it together, then write the essay draft.
[02:49] It will also have the autonomy of how it's going to reflect on how it is that it can improve things, whether it wants to call a human reviewer or not until the agent itself feels satisfied and produces the final result.
[03:00] It's the same input and the output that you want is the same as well, but you can see that one is very linear and the steps are well very well defined, less autonomous, and you have the much more autonomous version where the agent has access to tools and a lot more freedom to decide how it's going to get to that final essay.
[03:14] There's of course pros and cons to being less autonomous versus more autonomous.
[03:18] Like if you're less autonomous, the steps are predefined, they're clear, and most of all, you have a lot more control over what is happening and the final result.
[03:26] On the other hand, if something is more autonomous, the agent gets to make a lot more decisions for itself,
[03:31] and you can end up with really creative, really great results that are beyond what you imagine.
[03:35] But the downside is that you would then have less control, and it could also potentially come up with results that may not be what you're looking for at all.
[03:42] In any case, with agentic AI workflows, there is this spectrum of autonomy
[03:46] that you, the person building the agentic workflow gets to choose how autonomous you want it to be.
[03:51] Very explicitly though, Andrew in the course emphasizes that he rejects this notion of like a binary, something is either an agent or it's not an agent,
[03:58] which is pretty much like what the people on X has been debating about for like the past few years.
[04:02] What is actually considered an agent?
[04:04] But Andrew is basically like, no guys, no guys, just don't think about it that way, okay?
[04:06] Let's just call things like agentic AI, and as long as it involves multiple steps, it's agentic AI, and you can just be on the spectrum of least autonomous to more autonomous.
[04:15] paraphrasing a little bit here.
[04:16] Anyways, what we all can agree on though is if you wrap a LLM, a model in an agentic workflow, it is going to be much better than just calling it directly.
[04:24] This is a fact. It would also be often times faster and more modular, meaning that you can change things a lot more easily.
[04:30] So that is why agentic AI is so popular and very much worth building.
[04:36] Okay, let's now cover from a practical perspective, what are the building blocks of agentic AI?
[04:41] Andrew's building blocks for agentic AI is pretty simplistic actually.
[04:44] It involves just three components.
[04:47] Let's start off by addressing the first two, which is models and tools.
[04:50] Models just refers to the AI model that can be large language models or it can be like other types of AI models, multi-modal models, like video generation models, audio generation models, any type of model.
[05:00] And then there are tools, which are basically functions and capabilities that you're giving your AI agent
[05:05] so that it's able to perform different types of tasks.
[05:07] Examples of this will include being able to use external software through their APIs, stuff like web search, getting real-time data, be able to check emails, things like that.
[05:16] Information retrieval, so being able to access certain types of databases, and code execution, being able to write code to be able to do things like math, data analysis, building stuff.
[05:26] So all of these are tools.
[05:28] There is also a third component, which I will talk about in a little bit, because when you are first thinking about creating an agentic system, you're really just thinking about how do you take these building blocks of different models and different tools and chain them together and put them together in such a way to achieve the results that you want.
[05:43] For example, say you wanted to develop an agentic AI system with the goal to respond to a customer email for your company.
[05:51] This is an example of the type of email that you may get.
[05:53] Subject line here is wrong item shipped. It's like, hi, I ordered a blue KitchenPro blender. Here's the order number, but received a red toaster instead.
[05:59] I need the blender for my daughter's birthday party this weekend. Can you help?
[06:03] Susan Jones.
[06:03] If you want to create an AI workflow that is able to accomplish this task,
[06:07] the easiest way to do this is to actually think to yourself, how would I go about doing this task?
[06:12] Like, how would a human do this?
[06:14] Okay, so the first step would be you need to extract key information,
[06:17] including the order number, the fact that it was supposed to be a blue Kitchen Pro blender, but they got a red toaster instead, and the timeline. The daughter's birthday party is for the weekend.
[06:26] Then you would go and find the relevant customer record, which would likely include looking into an orders database to see what was actually recorded.
[06:33] Then you would determine what possibly could have went wrong and then send a email reply back.
[06:39] Now we need to translate these three steps into what an LLM would do.
[06:42] Well, for the first one extracting key information,
[06:44] the LLM is able to extract that information just by itself.
[06:47] But for the next step, which is finding the relevant customer record, the LLM would actually need a tool that would allow it to look into the orders database.
[06:54] So you would need to provide that with that tool for orders database query.
[06:58] And then finally, for writing and sending a response, the LLM would be able to draft the response, but in order to actually send that email, it would need to have access to another tool that allows it to send the email.
[07:09] Makes sense. This is how the building blocks of models and tools are coming together here.
[07:12] You have the large language models and the different tools that it requires.
[07:16] Of course, the type of large language model you want to use on each of these steps
[07:19] could vary depending on what it's supposed to be doing exactly and how it is that you're actually going to build this type of tool also varies.
[07:25] But don't worry too much about this. We're going to go into a lot more detail later in the video.
[07:29] But here what I want you to just make clear is that you're basically taking
[07:33] a goal and then translating that into a sequence of steps,
[07:37] in which you would then use the building blocks of models and tools in order to accomplish those steps.
[07:42] So the ideal situation after your AI system goes through these steps is that it would come up with a wonderful email that says something like, oh thank you so much for emailing the company.
[07:51] After looking at your order number, we did notice that it does correspond to a blue blender.
[07:56] And we apologize that you received a red toaster instead.
[08:00] We will send you a blender with expedited shipping so you can get it tomorrow
[08:04] and make it for your daughter's birthday on the weekend.
[08:07] And you can keep the red toaster as well.
[08:09] Then the customer, Susan Jones would probably be very happy.
[08:12] But what happens if your agent doesn't give you this wonderful email,
[08:15] and it's that it writes something like, oh thank you for shopping with us.
[08:18] As you can see, we are so much better than Rival Corp, our competitor.
[08:21] Or something like, sure, we'll issue a refund and not actually address the issue.
[08:25] That is why you need the third component of Andrew's framework, which is evaluations.
[08:30] Evaluations, as its name suggests, is all about evaluating the results of your agents.
[08:36] It's like the other half of building an AI agent.
[08:38] Not good enough to just build an agent. You actually got to make sure it works properly, right?
[08:41] And I am so glad that this course covers so much in depth about Evals.
[08:46] I will be covering this in a lot more detail in module 4, but very briefly, an evaluation in this case is making sure that your AI agent doesn't actually talk about your competitors, because that's kind of like in poor taste.
[08:58] So how do we do this? Well, first we can compile a list of all the competitors that we don't want to be mentioned, like Compco and Rivalco or the other Co.
[09:05] Then you can actually write a small snippet of code, like this, if competitor is in response, then the num competitor mentioned is plus or equal to one.
[09:14] What this basically does is check for the email responses and if any of these competitors are mentioned in the response, then you would just increment the counter of number of competitor mentions to one more.
[09:25] Of course, ideally you want this counter, the number of competitor mentions to be equal to zero, but you know, if it does show up, you would have a way now of tracking how many times it shows up and where it is showing up.
[09:35] This is a very objective way to determine if these competitors are actually still showing up, and you can use this counter as a way to then tweak your prompt, tweak your system, and do stuff to it to try to lower this number so that it eventually goes to zero.
[09:51] Don't worry about it if any of the details seem a little bit hazy, I'll be going into a lot more detail later in the video.
[09:55] But I just want you to understand here that see by having like an evaluation like this where you can measure the occurrence of this bad behavior, you now have an objective way to improve your system to decrease the bad behavior.
[10:08] If you didn't have this eval, this way of measuring the bad behavior, then you can like kind of think that you are improving your system, but you don't actually objectively know if you're improving the system.
[10:17] That is why evaluations are so important.
[10:20] This is an example of a very objective code-based approach for evaluating a result.
[10:26] There's another one called a LLM as a judge in which you're actually using another large language model to rate the results and evaluate the results of your agent.
[10:35] Anyway, this course is an excellent introduction to agentic AI.
[10:38] But when you're ready to start building your own AI agents with business impact,
[10:42] there are many other factors that you do need to consider, which is why I highly recommend that you check out the free Master AI agent resource from HubSpot Media.
[10:50] It provides good practical frameworks and examples on how to get started with building useful AI agents with business impact.
[10:56] It also includes real use cases in marketing, sales and operations that you can directly use to start implementing your own agents to do things like
[11:02] content production optimization, process large amounts of data,
[11:05] customize outreach and much, much more.
[11:08] There's also a second downloadable resource called how to use AI agents
[11:10] that has an excellent checklist to guide your organization through each phase of implementing AI agents.
[11:15] This is so useful and it's something that we actually use in our company whenever we're launching a new agent.
[11:20] Really recommend you check out the resource linked over here, also in the description.
[11:23] Thank you so much HubSpot Media for providing practical free resources on building AI agents and for sponsoring this portion of the video.
[11:29] Now, back to the video.
[11:30] of course. But first, let's move on to modules two and three, which are covering what are known as agentic design patterns.
[11:36] And what are agentic design patterns, you may ask?
[11:39] Well, remember we talked about earlier about sending that email for the blender and the toaster.
[11:43] Got to first decompose that task,
[11:45] and then translate that into a combination of large language model and tool use.
[11:50] So you could just kind of like figure that out yourself with any type of task that you want your agentic AI to do.
[11:57] But luckily, we do have a lot of precedents now for specific types of tasks and specific types of design patterns, like how it is that we're decomposing and fitting together the pieces that has proven to show really good results.
[12:09] Because more likely than not, whatever it is that you're trying to accomplish will converge to one of these design patterns.
[12:14] In this course, Andrew covers four design patterns, two that are less autonomous and two that are more experimental and more autonomous.
[12:21] Let's now talk about the first design pattern, which is reflection.
[12:25] The reflection design pattern is super intuitive.
[12:27] For example, if you tell a human, hey, go write this email and they're like,
[12:29] you know, distracted or they just like had lunch, so they just write some sloppy email.
[12:34] But if you go like, hey, reflect on this and improve the email, probably the result you're going to get is going to be a lot better.
[12:40] exactly the same with AI.
[12:42] If you tell an AI to write an email, it will first do a first draft, which might not be that great.
[12:46] But if you tell it to go back and reflect on it and improve it, you will end up having much better results.
[12:51] The second step, asking to reflect on it and come up with another draft is literally the reflection design pattern.
[12:56] Simple but powerful.
[12:58] And remember how it is that we can actually go about tweaking this and improving the system systematically is by having the whole like evaluation section.
[13:03] The course also provides code examples of how to implement design patterns like the reflection pattern, which you can see over here, but I'm not going to go into too much detail about this.
[13:10] You can actually go and try out the implementation with code if you want to.
[13:14] in the course, it's actually free to get this code.
[13:17] So I'll link it in the description.
[13:18] By the way, don't be discouraged and like rage quit right now if you don't know how to code.
[13:21] This is absolutely doable with no code as well. They just don't show it in the course.
[13:24] Like we teach the full no code approach for doing this in our agent bootcamp ourselves.
[13:28] I also do have a video over here that covers the basics of how to implement agents using the no code approach too.
[13:34] Okay, let's go on to the second design pattern called tool use.
[13:38] So this part I did get like a little confused because we did talk about tools
[13:41] when we talked about the building blocks, right, of like models and tools and evaluations.
[13:46] But I think Andrew included this as like a full-on design pattern because he wanted to emphasize like how much tool use can elevate the performance of an agent.
[13:54] So, we'll go through it.
[13:55] Firstly, to define tool use, you're letting your agent have access to tools that's able to implement and do certain things that it normally cannot do just as a model itself.
[14:04] For example, if you have an agentic AI workflow in which you want to be like booking meetings and stuff,
[14:09] you would need to give your agent access to a calendar booking tool.
[14:12] With tool use, you can make it like very strict, telling your agent that you have to use this exact tool to do this exact thing,
[14:17] or you can make it more autonomous,
[14:19] and give your agents more like a selection of tools that it can choose from, and it can get to choose which tool it wants to use to accomplish a task.
[14:26] But whatever tools it is that you choose to give your AI agent and how much you restrict how it's using the tools, the key here is that you do need to define the tool and you need to let your agent know that you gave them access to these tools and what the tools are in the system prompt itself, or else your agent will just be like,
[14:41] what is this? I don't know what this is.
[14:44] Like for example, if you have a personal assistant, agentic AI system,
[14:47] and you tell it to find a free slot on Thursday in my calendar and make an appointment with Alice,
[14:52] you would need to give it tools such as make appointment, check calendar, and delete appointment, and tell it in the system prompt, you have access to the tool of make appointment, which is for making an appointment booking.
[15:03] check calendar, which is for checking a calendar to check for availabilities,
[15:07] delete appointment in order to delete existing appointments.
[15:10] Then you can tell your agent to like, you know,
[15:12] find that time slot between you and Alice.
[15:14] and it should be able to use the tools at its disposal in order to accomplish the task.
[15:19] So, how does that you can actually define these tools for your agent?
[15:22] There's actually quite a few different ways of doing this.
[15:25] The most simple approach, if you're using code, is to literally just like write a function for it.
[15:29] And then give it access via an AI agent through some type of framework.
[15:33] The example that they showed in the course is called the AI suite.
[15:36] But there's like a lot of other frameworks that you can use as well.
[15:38] I'm not going to go into too much detail about this, but if you are interested in implementing this, there is an assignment in the course as well,
[15:45] which I will link in the description.
[15:47] So, yeah, keep that in mind.
[15:51] Andrew also explains that there's other ways for you to give your agent tools as well.
[15:53] For example, through something called MCP, which is the model context protocol.
[15:56] This is a protocol that was developed by Anthropic that standardizes the way that tools are defined
[16:01] so that it's very easy for agents to have access to different tools without having to like write custom functions for each of them.
[16:08] MCPs are actually really cool. A lot of developers are actually building MCPs and like selling their MCPs and stuff like that as well.
[16:13] So if you are interested in learning more about it, I do have a full video, which I'll link over here that goes into the depths of MCPs.
[16:19] But for now, let's move on to the much anticipated module four.
[16:26] Practical tips for building agentic AI.
[16:29] Where we talk a lot now about evaluations.
[16:32] The missing piece of agentic AI development and what makes this course so valuable.
[16:36] To properly define it, evaluations or evals are agent evaluation mechanisms that refer to the processes and criteria used to assess the performance of agents within a system.
[16:45] We already talked about why we need evals and why it is the third major building block because you can build an AI agent, but how do you even know how good it is and how do you know how to improve it if you don't measure the results?
[16:55] And that is where evaluations come in.
[16:57] For example, say you have an invoice extraction agent.
[16:59] So you give the system PDF invoices, which then converts into text.
[17:03] Then the LLM extracts four required fields like the biller, biller address, amount due, and due date.
[17:08] It has access to a tool called update database, which will then use in order to update the database with a new invoice and the record is created.
[17:16] Simple linear agentic workflow here.
[17:18] Now, if we want to evaluate this agentic workflow,
[17:20] one approach of doing this is to just now take 10 to 20 different invoices and then feed it through the agent and then make a record of the results.
[17:29] You might notice that invoice one was fine, and it was able to extract the four required fields and everything is great.
[17:34] But you found that invoice two, it actually mixed up the dates between the due date and the invoice date.
[17:40] Uh, invoice three was okay as well, and then you keep on going and you find that invoice 19, it also mixed up the dates and invoice 20, it mixed up the dates as well.
[17:46] This is actually the most practical way of doing this.
[17:48] So, from collecting this data, you notice that one of the tendencies of this agentic workflow is that it mixes up dates, which is not good. We actually want to improve that.
[17:57] So we want to build an eval for this to set a metric for us to improve.
[18:02] One thing to note here is that often times you don't actually know what evals that you should be building before you actually build out your system and start running examples through it.
[18:10] It's actually kind of hard to think through like what are the potential like places of failure for your system until you try it out.
[18:16] So that's why the general recommendation is to just like build something quickly, quick and dirty,
[18:20] and then just start passing through different examples and collecting that data to decide what the evals should be.
[18:26] Say we want to create an eval now for date extraction because we notice that it gets the date extraction wrong a lot.
[18:31] So how do we go about doing this?
[18:33] Well, step number one is to manually extract the due dates from the 10 to 20 invoices that you pass through.
[18:39] Then you want to specify the output format of the data in the prompt itself.
[18:43] So then you can extract the date from the LLM response using code.
[18:46] And finally, compare the large language model result to the ground truth.
[18:50] Does the extracted data equal to the actual data?
[18:54] This is an example of an evaluation that uses code.
[18:57] If you actually want to implement evaluation using code yourself, by the way, also in the course, there is the code for this that you can run yourself.
[19:04] This is an example of an evaluation that you can implement so that in the future, as you're like tweaking your prompts and like changing things around,
[19:11] you can actually measure if your invoice agent system is becoming more accurate or less accurate at date extraction.
[19:18] Hopefully, more accurate.
[19:19] There are a lot of other types of doing it and the way that the course frames it is that you can think about Evals as falling under two different axes.
[19:27] This date extraction eval is an example of an objective eval because the result is that the extracted date is either equal to the actual date or it's not equal to the actual date.
[19:37] Very objective, either right or wrong.
[19:39] With this type of eval system, you can usually implement it pretty easily just through code.
[19:44] Another type of eval is a subjective eval.
[19:46] This is when the result isn't just like a yes or no binary kind of situation.
[19:50] An example of a subjective eval is if you're trying to say,
[19:52] assess the result of a research agent.
[19:56] The agent is supposed to research on a certain topic and then output like some sort of essay at the end.
[20:00] So if you give it a prompt like research and write an essay about recent black hole science,
[20:04] there's no way to objectively evaluate how good the research is and how good the essay ends up.
[20:10] You can't just like, you know, count the number of words or something like that.
[20:13] So what you need to do to create this kind of eval is first, choose a few different topics that you're going to be using as a prompt.
[20:20] Like maybe something about black holes, something about robot harvesting, renting versus buying a home in Seattle, etc, etc.
[20:26] So for each of these prompts, you need to actually manually establish a ground truth annotation, which are like golden standard talking points
[20:32] that you know needs to be researched and needs to be part of the final essay as well.
[20:37] For example, with black holes, this could be stuff like event horizon, radio telescope.
[20:41] For robotic harvesting, it could be like RoboPick and Pinchers.
[20:44] To actually do this, you probably need to like find someone who actually knows these topics, or you yourself know these topics as well. So this part is manual.
[20:50] But then the second part is when you can use the LLM as a judge.
[20:52] So you have another type of LLM to count how many of these topics actually appear in the research and the final result.
[21:00] The reason why you need to use a LLM to count this and not just like objectively use code to count this, is because a certain term can appear in a lot of different iterations.
[21:09] Like the term event horizon could be like event horizon, but it could also be like uppercase, lowercase, could be the horizon, the type of event at the horizon, or like when the horizon is near, something like that.
[21:19] There's like so many different types of iterations of this that you need an LLM to be able to capture all the different types of these iterations.
[21:26] Then you can get the LLM to give you a final score for each prompt, basically upon how many of these terms were captured in the final result.
[21:33] This on screen now is an example of a prompt for the LLM as a judge.
[21:37] Then the second axis of this 2x2 matrix for the different types of Evals is whether something has a per example ground truth or does not have a per example ground truth.
[21:50] Both the examples that we just talked about, the invoice example and the LLM research and essay writing example,
[21:56] are agenting systems that have a per example ground truth.
[21:59] This means that for every example, every input that we give,
[22:02] there is a established ground truth for that example.
[22:06] Like the invoice extraction has a specific date that is the correct result that is different for all the different examples.
[22:11] And the topics for the research agent are different for each of the examples too.
[22:15] However, you can also have Evals that have no per example ground truth,
[22:19] meaning that there is a singular universal standard that is there for every single example.
[22:24] Say if you have an agentic system that is for marketing copy length,
[22:28] and you just want to make sure that the marketing copy length is always less than 10 words.
[22:32] So the number 10 is like the universal magical number.
[22:35] This is also an objective eval, so you can actually write code, so you can literally just write if the length of the text is less than or equal to 10,
[22:41] then that is good. If it's not, then it's bad.
[22:43] The final quadrant of this 2x2 matrix is when you have something that is subjective and does not have a per example ground truth.
[22:50] Say you have an agentic system that is supposed to create different graphs.
[22:54] The judging of the graph is going to be subjective. The result of the graph is going to be subjective, and the way that you judge it is based off of this universal criteria
[23:02] where you would ask the LLM as a judge to grade the graph to see whether it has axis labels,
[23:08] are the colors easy to see? Is there any overlapping text? etc, etc.
[23:13] So that would be like a universal grading criteria.
[23:17] Okay, great. That covers the four general types of Evals that you can make.
[23:22] Some of the tips that the course suggests, when you're creating these Evals.
[23:25] Firstly is to just quick and dirty is okay to start.
[23:28] Just create something and then just create some Evals and just get started like that.
[23:32] You can always continue to expand the set of Evals.
[23:34] You want to try to use a lot of different examples to try to capture all the different types of errors that you can change into Evals.
[23:42] And finally, you want to look for places where the performance of the agentic system is worse than humans.
[23:47] These are the best areas for improvement.
[23:49] Great. That was the module on Evals. Even if you implement just like a few of these different Evals, you'll be setting up a system that will help you dramatically improve the results of your agents.
[23:59] I feel like Evals are such an open secret and by implementing them, massive return on investment.
[24:06] Alright, we're almost done.
[24:07] We're at module five, which is the patterns for highly autonomous agents.
[24:11] We're going to be covering two of the more experimental agents that are also more autonomous.
[24:15] The two patterns that we've covered earlier, reflection and tool use,
[24:18] are less autonomous and they're more predictable.
[24:20] Well, for these experimental ones, planning and multi-agent systems,
[24:24] these are less predictable, less controllable, but if you get it right, the results can be really, really good.
[24:29] Let's start off with planning and jump straight to an example.
[24:32] Say you have a customer service agent, in which you have an inventory database of different types of products in a store.
[24:38] You have like ID, name, description, price, and stock.
[24:41] An example of a customer query that the agent would receive would be like, do you have any round sunglasses in stock that are under $100?
[24:48] So you see this is actually a pretty difficult query because it involves the customer service agent to have to go through the data set and first like find what are the round styles.
[24:57] Then it has to go pick out which of these are in stock. And finally, which of these prices are less than $100.
[25:03] To be able to come up with the final answer of, yes, we have our classic sunglasses, which are a classic round metal frame and costs $60.
[25:09] And of course, this is just a single example of the kind of questions that customers will be asking,
[25:13] and there's a broad range of questions that will be asked and that can be answered by using this database.
[25:18] However, there is no like set path for you to actually answer these questions.
[25:22] Each time you would have to figure out and plan out what is the way to actually answer these questions.
[25:28] This is where the planning design pattern comes in.
[25:30] Going back to that example of asking the question, do you have any round sunglasses in stock that are under $100?
[25:35] The planning design pattern will first have an LLM figure out what is the plan to answer this question given the set of tools that it has.
[25:42] Like it has tools like get item descriptions, check inventory, process item return, etc, etc.
[25:47] So it would use this information and the information of the database and come up with a plan like number one, have to use get item description tool to find the round sunglasses.
[25:55] Second step is to use check inventory to see if results are in stock.
[25:59] And third step is to use get item price to see if in-stock results are less than $100.
[26:03] Then the agent will take that plan and execute each of these steps to get the final result.
[26:07] By the way, if you want to dig into this and actually implement these evals yourself, there is again assignment in the course, which I will link below.
[26:15] What is cool about this planning design pattern is that the plan is not predetermined.
[26:19] So the agent system has to actually figure out the plan first and then go and execute each of the steps, which means of course that the downside of this planning design pattern is that you don't actually know what the plan is.
[26:28] So it's actually very hard to troubleshoot and anticipate what kind of result you're going to get until it actually goes through the process itself.
[26:35] The upside of this is the increase in the amount of flexibility.
[26:37] And sometimes it is pretty magical to witness an agent be able to plan out super complex tasks and then execute it and get like crazy good results.
[26:46] This is the kind of magic that more autonomous systems have.
[26:49] Less control, but more probability of really cool results.
[26:54] The other more experimental autonomous design pattern is a multi-agentic workflow.
[26:59] The idea of a multi-agent system is to take an agentic system and actually have it be multiple different agents working together to produce a final result.
[27:08] The intuition for why this can be better is kind of like a company, right? Like if you have like one person trying to do all the different tasks in a company,
[27:14] it's probably not going to do the best job and it's going to get overwhelmed because it has to do like so many different things and juggle so many different things at the same time.
[27:21] But if you have different people in that company that specialize in different things,
[27:25] each person would be able to focus better on their specific task and when you put it together, it's going to produce a better result.
[27:30] That's why we usually have multiple people in the company and not just like the CEO trying to do everything themselves.
[27:34] So that's the same intuition for developing multi-agent systems.
[27:37] For example, say you have a marketing team agentic system, and instead of just having one agent, you actually divide that into three different sub agents,
[27:45] a researcher, a graphic designer, and a writer.
[27:48] So that when you receive a query, like create a summer marketing campaign for sunglasses, your research agent will focus on conducting research and figuring out that here are current sunglasses trends and competitor offerings.
[27:59] It would pass along that information to a graphic designer agent, which will then come up with like five different data visualizations and five different artwork options for the report.
[28:08] It would then pass all of this to the final writer agent, which will then compile everything together and write the final report.
[28:15] So this would be a marketing team agentic system that's able to generate reports for a marketing campaign on a specific topic.
[28:21] There's actually quite a lot of research done on multi-agent systems and in our bootcamp as well, we have a whole week that covers multi-agent systems because the results can be really, really good, much, much better than if you just use a single agent.
[28:33] This course doesn't cover too much into it though, but I will leave a link in the description for an Anthropic article that goes into a lot more detail about multi-agent systems.
[28:40] I also have a video that covers multi-agent systems as well, which you can check out at this link over here if you prefer like a video approach.
[28:47] Anyways, for this course, they also have code-based assignments where you can implement these more autonomous systems too.
[28:52] Oh my god, okay, we have come to the end of this video of this crash course.
[28:57] I literally had, let's see, 93 pages of notes, which I have condensed for you guys here.
[29:02] Overall, I think this course was really quite good.
[29:04] It has a very good overview of all of the different parts of building agentic AI.
[29:10] My critique though, if I may,
[29:12] Andrew does approach from a very like researchy, theoretical perspective, which makes sense given his background as like a research scientist.
[29:18] But I do feel like he didn't really cover like the actual process of deployment and what does that actually look like when you put it into the world and get users to start using your agents and stuff like that.
[29:27] That's like a whole other beast which we cover a lot in our bootcamp as well because we're coming from like a more practical approach so that we're building these agents and actually deploying them and people are using them and, you know, you're hopefully making money from them as well.
[29:38] Another critique that I do have is that the assignments here, they're all like based upon code.
[29:43] If you didn't know any better, you would have the misconception that you have to know how to code in order to implement these systems, and that is not true.
[29:50] So I just want to like make that super clear for you guys too.
[29:52] You can do this with no code as well.
[29:54] I'll link in the description some of the videos that I cover in which you can implement these systems with no code completely.
[30:00] All right, as promised, here is the little assessment in which if you can answer these questions, then congratulations.
[30:05] You are going to be able to retain all the information we've just covered from this 8-hour course.
[30:09] Please write your answers in the comments.
[30:12] All right, thank you so much for watching until the end of this video.
[30:13] I really hope that you learned a lot about agentic AI and you're super excited to start building your own agents as well.
[30:19] And I will see you guys in the next video or live stream.
[30:22] Bye bye.

---
# TAXONOMY ANALYSIS

## 4. Workflows Identification

WORKFLOW: Essay Writing (Less Autonomous)
OBJECTIVE: Write an essay on a given topic with a predefined sequence of steps.
STEPS:
  1. Come up with an essay outline.
  2. Conduct web research on the topic.
  3. Write a first draft.
  4. Consider parts for revision and more research.
  5. Request human review (optional).
  6. Revise the draft to create the final version.
DURATION: Not mentioned
COMPLEXITY: Low
TOOLS USED: Web Search
INPUT: Essay topic (e.g., "tea ceremonies")
OUTPUT: Final essay draft

WORKFLOW: Essay Writing (More Autonomous)
OBJECTIVE: Write an essay on a given topic, allowing the agent to decide the process.
STEPS:
  1. Decide which tools to use for information gathering.
  2. Gather information from the best sources.
  3. Compile the information.
  4. Write the essay draft.
  5. Reflect on how to improve the draft.
  6. Decide whether to call a human reviewer.
  7. Produce the final result when satisfied.
DURATION: Not mentioned
COMPLEXITY: Medium
TOOLS USED: Web Search, New Search, Archive Search
INPUT: Essay topic (e.g., "tea ceremonies")
OUTPUT: Final essay draft

WORKFLOW: Customer Email Response
OBJECTIVE: Respond to a customer email regarding a shipping error.
STEPS:
  1. Extract key information from the email (order number, items, timeline).
  2. Find the relevant customer record using a database tool.
  3. Determine what went wrong with the order.
  4. Draft a response email.
  5. Send the email using an email tool.
DURATION: Not mentioned
COMPLEXITY: Medium
TOOLS USED: Orders Database Query Tool, Email Sending Tool, LLM
INPUT: Customer email with an issue
OUTPUT: Sent email response to the customer

WORKFLOW: Invoice Data Extraction
OBJECTIVE: Extract structured data from PDF invoices and store it in a database.
STEPS:
  1. Convert PDF invoice into text.
  2. Extract required fields (biller, address, amount, due date) using an LLM.
  3. Use an `update database` tool to add the extracted information.
  4. Create a new record in the database.
DURATION: Not mentioned
COMPLEXITY: Low
TOOLS USED: PDF-to-Text Converter, LLM, Update Database Tool
INPUT: PDF Invoices
OUTPUT: New structured records in a database

WORKFLOW: Customer Query Answering (Planning Pattern)
OBJECTIVE: Answer complex customer queries by dynamically planning and executing steps using a product database.
STEPS:
  1. **Plan Phase**: Generate a multi-step plan to answer the query.
     a. Plan to use `get item description` tool to find products matching a criteria (e.g., "round sunglasses").
     b. Plan to use `check inventory` tool to see if the found items are in stock.
     c. Plan to use `get item price` tool to filter for price constraints (e.g., "under $100").
  2. **Execution Phase**: Execute the generated plan step-by-step.
  3. Synthesize the results into a final answer.
DURATION: Not mentioned
COMPLEXITY: High
TOOLS USED: Get Item Descriptions, Check Inventory, Get Item Price
INPUT: Customer query (e.g., "any round sunglasses in stock under $100?")
OUTPUT: A direct answer to the customer's query

WORKFLOW: Multi-Agent Marketing Campaign Creation
OBJECTIVE: Create a marketing campaign report by dividing tasks among specialized agents.
STEPS:
  1. **Researcher Agent**: Conducts research on trends and competitors.
  2. **Information Pass-off**: Researcher passes findings to the Graphic Designer.
  3. **Graphic Designer Agent**: Creates data visualizations and artwork options.
  4. **Information Pass-off**: Graphic Designer passes visuals and research to the Writer.
  5. **Writer Agent**: Compiles all information and writes the final report.
DURATION: Not mentioned
COMPLEXITY: High
TOOLS USED: Multiple specialized AI agents
INPUT: Marketing campaign topic (e.g., "summer marketing campaign for sunglasses")
OUTPUT: A complete marketing campaign report

## 5. Action Verbs & Operations

#### A. CREATION VERBS (Making new things)
- Build
- Come up with
- Create
- Develop
- Draft
- Generate
- Make
- Produce
- Write

#### B. MODIFICATION VERBS (Changing existing things)
- Change
- Customize
- Expand
- Improve
- Revise
- Tweak
- Update

#### C. ANALYSIS VERBS (Understanding/Evaluating)
- Analyze
- Assess
- Check
- Compare
- Consider
- Determine
- Evaluate
- Find
- Figure out
- Grade
- Look for
- Look into
- Measure
- Notice
- Rate
- Research
- Review
- See
- Test

#### D. ORGANIZATION VERBS (Structuring/Managing)
- Arrange
- Chain
- Compile
- Decompose
- Define
- Focus
- Organize
- Plan
- Prioritize
- Standardize
- Structure
- Track

#### E. COMMUNICATION VERBS (Sharing/Presenting)
- Address
- Answer
- Ask
- Communicate
- Cover
- Emphasize
- Explain
- Pass along
- Report
- Talk
- Tell

#### F. BROWSER/AGENTIC OPERATIONS (AI Agent & Automation Actions)
- Accomplish
- Access
- Automates
- Choose
- Decide
- Delete
- Execute
- Give access
- Go through
- Implement
- Interact
- Launch
- Let
- Perform
- Put together
- Run
- Use
- Work

#### G. DATA OPERATIONS (Processing, Transforming, Moving Data)
- Capture
- Collect
- Convert
- Count
- Extract
- Feed
- Filter
- Gather
- Look up
- Process
- Provide
- Query
- Record

## 6. Task Chains

TASK CHAIN: Less Autonomous Essay Writing
`Come up with outline` → `Conduct research` → `Write first draft` → `Consider revisions` → `Revise draft` → `Final Essay`

TASK CHAIN: Customer Email Response
`Extract key info from email` → `Query orders database` → `Determine issue` → `Draft & send email reply` → `Resolved Customer Issue`

TASK CHAIN: Invoice Processing
`Convert PDF to text` → `Extract required fields` → `Update database` → `Record Created`

TASK CHAIN: Dynamic Query Planning
`Receive query` → `Generate plan (e.g., Find → Check Stock → Check Price)` → `Execute plan` → `Synthesize answer` → `Customer Answer`

TASK CHAIN: Multi-Agent Marketing Report
`Researcher agent conducts research` → `Passes info to Graphic Designer` → `Designer creates visuals` → `Passes all to Writer` → `Writer compiles and writes` → `Final Report`

## 7. Responsibilities Vocabulary

#### Professional Roles Mentioned:
- Research Scientist
- CEO
- Researcher
- Graphic Designer
- Writer
- Personal Assistant
- Customer Service Agent

#### Responsibilities/Activities:
- "write an essay on tea ceremonies"
- "respond to a customer email"
- "invoice extraction"
- "booking meetings"
- "finding a free slot on Thursday in my calendar"
- "create a summer marketing campaign for sunglasses"
- "deploying agents"
- "evaluating the results of your agents"
- "content production optimization"
- "process large amounts of data"

#### Skills Mentioned:
- Coding
- No-code implementation
- Prompt tweaking
- System evaluation
- Data analysis
- Information retrieval

## 8. Tools & Technologies Matrix

| Tool Name | Category | Purpose | Used For | Mentioned With |
|-----------|----------|---------|----------|----------------|
| LLM | Model | Core intelligence for agents | Task execution, drafting, analysis, judging | Agentic Workflows |
| HubSpot Media | Resource | Practical frameworks and checklists | Building business-impact AI agents | Marketing, Sales, Ops |
| Web Search | Tool | Information Retrieval | Researching topics like tea ceremonies | New Search, Archive Search |
| New Search | Tool | Information Retrieval | Gathering current information | Web Search |
| Archive Search | Tool | Information Retrieval | Finding research papers | Web Search |
| Orders Database Query | Tool | Data Retrieval | Finding customer records from a database | Customer Email Response |
| Email Sending Tool | Tool | Communication | Sending automated email replies | Customer Email Response |
| Calendar Booking Tool | Tool | Scheduling | Making, checking, and deleting appointments | Personal Assistant Agent |
| AI Suite | Framework | Development | A code-based framework to give agents tools | Implementing agents |
| MCP | Protocol | Tool Standardization | Standardizing the way tools are defined for agents | Anthropic |
| Update Database Tool | Tool | Data Writing | Adding new invoice records to a database | Invoice Extraction |
| Get Item Descriptions | Tool | Data Retrieval | Querying a product database for descriptions | Customer Query Planning |
| Check Inventory | Tool | Data Retrieval | Checking if a product is in stock | Customer Query Planning |
| Get Item Price | Tool | Data Retrieval | Querying a product database for prices | Customer Query Planning |

## 9. Objects & Deliverables

- Essay (final draft)
- Email response
- Invoice record (in a database)
- Marketing campaign report
- Data visualizations
- Artwork options
- Code snippets
- Graphs (with axis labels)
- Marketing copy (less than 10 words)
- Research notes
- Essay outline

## 10. Integration Patterns

INTEGRATION: LLM + Database Query Tool + Email Tool
PURPOSE: Automate customer service responses for order issues.
FLOW: Customer email (Input) → LLM `extracts` data → Database Query Tool `finds` order → LLM `drafts` response → Email Tool `sends` email (Output)

INTEGRATION: PDF Processor + LLM + Database Tool
PURPOSE: Automate invoice data entry.
FLOW: PDF invoice (Input) → PDF Processor `converts` to text → LLM `extracts` fields → Database Tool `updates` database (Output)

INTEGRATION: Researcher Agent + Graphic Designer Agent + Writer Agent
PURPOSE: Create a comprehensive marketing report using specialized agents.
FLOW: Research findings (Researcher Output) → `becomes` → Input for Graphic Designer → Visuals (Designer Output) + Research → `becomes` → Input for Writer → Final Report (Writer Output)

## 11. Business Concepts & Strategy

- **Spectrum of Autonomy**: The concept that agentic systems are not a binary (agent/not agent), but exist on a spectrum from less autonomous (predefined steps) to more autonomous (agent decides steps).
- **Agentic Design Patterns**: Reusable templates for building agents, including **Reflection**, **Tool Use**, **Planning**, and **Multi-Agent Systems**.
- **Evaluations (Evals)**: A critical component of agent development for measuring performance and driving systematic improvement. The "other half of building an agent".
- **LLM as a Judge**: A technique for subjective evaluations where one LLM is used to grade the output of another agent based on a rubric.
- **Ground Truth**: The correct, verified data used as a benchmark in evaluations. Can be "per-example" (unique for each input) or universal (the same standard for all inputs).
- **Return on Investment (ROI)**: Mentioned in the context of implementing Evals, which have a "massive return on investment" by improving agent performance.
- **Modular Design**: Agentic workflows are more modular, meaning components can be changed more easily than in a monolithic system.

## 12. Optimization & Best Practices

OPTIMIZATION: Information Retention
TECHNIQUE: Immediately review information after you learn it.
REASON: Research shows it is the best way to retain information.
EVIDENCE: [00:13]

OPTIMIZATION: LLM Performance
TECHNIQUE: Wrap a Large Language Model (LLM) in an agentic workflow instead of calling it directly.
REASON: The result is much better, often faster, and more modular.
EVIDENCE: [04:16]

OPTIMIZATION: Agent Development Process
TECHNIQUE: Build a "quick and dirty" version of the agent first, then run examples through it to identify failure points.
REASON: It's hard to predict all failure modes upfront. Collecting data on failures helps decide which evaluations (Evals) to build for systematic improvement.
EVIDENCE: [18:16]

OPTIMIZATION: Improving Agent Performance
TECHNIQUE: Use objective, code-based or LLM-as-a-judge evaluations (Evals) to measure bad behavior or inaccuracies.
REASON: Evals provide an objective metric, allowing you to tweak prompts and systems and know for sure if you are improving performance.
EVIDENCE: [10:08]

OPTIMIZATION: Task Quality (Reflection Pattern)
TECHNIQUE: After generating a first draft, instruct the agent to "go back and reflect on it and improve it."
REASON: Just like with humans, a second, revised draft is almost always better than the first.
EVIDENCE: [12:46]

OPTIMIZATION: Finding Areas for Improvement
TECHNIQUE: Look for places where the performance of the agentic system is worse than a human's.
REASON: These are the best and most impactful areas for improvement.
EVIDENCE: [23:42]

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
