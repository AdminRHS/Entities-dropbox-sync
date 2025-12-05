https://youtu.be/s_YfqQ_KHYA?si=st6hwcheTIbqCOgs

Video Transcription: Kimi K2 Thinking AI Model
1. Metadata Section
Video Title: Not Provided. Based on content: "Kimi K2 Thinking: A New Frontier Open-Source AI Model"
Channel/Creator: Matthew Berman
Video URL: Not Provided.
Duration: 14:31
Publication Date: Not Provided.
2. Description Section
Description: This video introduces Kimi K2 Thinking, a new open-source, open-weights AI model from Moonshot Labs, a Chinese AI company. The creator, Matthew Berman, claims it is a "frontier level model" that outperforms competitors like GPT-5 and Claude 4.5 on several difficult benchmarks. The video details its capabilities, including long-chain reasoning, tool use (web search, browsing, code execution), and its performance on benchmarks like Humanity's Last Exam and BrowseComp. It also showcases several practical examples of the model's coding and data analysis abilities, such as creating interactive websites, data dashboards, and even music.
Key Topics:
Introduction to Kimi K2 Thinking by Moonshot Labs.
Comparison of Kimi K2 Thinking with GPT-5, Claude Sonnet 4.5, and DeepSeek.
Benchmark performance analysis (Humanity's Last Exam, BrowseComp, SWE-bench).
Demonstration of agentic capabilities: tool use, web browsing, coding.
Examples of outputs: Word clone, math visualizations, data analysis dashboards, music creation.
Discussion on the rise of Chinese open-source AI models.
Cost and efficiency of training frontier models.
Links Referenced:
kimi.com: The chat interface for using the Kimi K2 Thinking model.
getvultr.com/berman: Sponsor link for Vultr cloud services.
3. Word-for-Word Transcription
[00:00] We may have another DeepSeek moment on our hands. Moonshot Labs, a Chinese frontier AI company just released a completely open-source, completely open-weights frontier-level model that is better than GPT-5, better than Claude 4.5 on some of the hardest benchmarks. Let me break it all down for you.
[00:24] [VISUAL: Vultr logo appears] And this video is brought to you by Vultr, more on them later. [TEXT: Introducing Kimi K2 Thinking] This is Kimi K2 Thinking. This is a thinking model that is capable of thinking for a long time and using tools in its thought process. And already, people are saying this is an incredible model. We've done some initial tests, I'm going to show you that towards the end of the video.
[00:44] All right, so let's get into the details. Built as a thinking agent, it reasons step-by-step while using tools, achieving state-of-the-art performance on Humanity's Last Exam (HLE), BrowseComp, and other benchmarks. It can execute up to 200 to 300 sequential tool calls without human interference, reasoning coherently across hundreds of steps to solve the most complex problems. This is Moonshot's attempt to scale up test-time reasoning for the Kimi series of models, and they have created an incredible model.
[01:19] All right, let's look at some of the benchmarks. [VISUAL: Bar chart comparing Kimi, GPT-5, and Claude on "Humanity's Last Exam"] Here is Humanity's Last Exam. This is one of the hardest benchmarks on the planet. And look at this. Kimi K2 Thinking coming in with a score of 44.9 as compared to GPT-5 at 41.7. It beats GPT-5 at Humanity's Last Exam. A fully open-source, fully open-weights model now is better than frontier models out of the U.S. closed-source labs.
[01:48] [VISUAL: Bar charts for "Agentic Search"] And Claude Sonnet 4.5 thinking, scoring a 32. It is also incredibly good at agentic browsing and search. In fact, they even built an agentic mode into Kimi, which they haven't released yet. It should be released pretty soon, but look at this. Agentic search for BrowseComp, K2 Thinking scoring a 60.2 versus 54.9 for GPT-5 and a measly 24.1 for Claude Sonnet 4.5 thinking.
[02:15] [VISUAL: Bar charts for "Coding"] We have SWE-bench Verified, although it is coming in last place amongst GPT-5 and Claude Sonnet 4.5 thinking, it is still a very good score at 71 versus 74 for GPT-5 and 77 for Claude. Then we have LiveCodeBench V6, which is a competitive programming benchmark. 83.1 for Kimi K2, 87 for GPT-5, and 64 for Sonnet 4.5 thinking.
[02:41] All right, so let me show you this example. [VISUAL: A complex mathematical problem is displayed on screen] Here it is solving a PhD-level mathematics problem. And it does so with 23 tool calls in its chain of thought. So check this out. I'm not going to be able to explain what's going on here, but I just want to show you it actually kind of going through the process of solving this. So here's the question. Now we have "Reasoning Completed," we can go in and we can actually see all of the crazy reasoning that's happening at every different step.
[03:09] Scroll down, we can see it also did web search. So, hyperbolic normal distribution PDF. So it was actually looking for references for sources to help inform how to solve the problem. Goes back and forth again. And basically, it's just super impressive between searching for more information, reasoning, searching for more information. I am blown away by its capability. And then at the very end, it got the right answer, and again, I'm not going to be able to explain how or why, but here we are.
[03:37] [VISUAL: "Agentic Coding" section with examples] It is also incredibly good at coding, of course. And we have multiple examples provided by the Kimi team. [VISUAL: Example 1 - A web-based Word clone called "WebWord"] So check this out, a component-heavy website, essentially a Word clone. And we can see here, I can delete stuff. We have different fonts, we have different font sizes, italics, bold, underline, strikethrough, all of these work. Even if I click save, it saves the document to my local computer.
[04:03] [VISUAL: Example 2 - A math explainer showing gradient descent] Next, look at this example. We have a math explainer, visualization of gradient descent. And again, this is created all using a single prompt. And so we actually can see a

full visualization of gradient descent. This is going to be great for me who uses a lot of B-roll and a lot of explainer visuals, so I'm definitely going to be checking this out.
[04:23] [VISUAL: Example 3 - A simulation of a virus attacking cells in a bloodstream] Here's a model test that I've used in the past. I don't know if they've seen one of my videos or not, but this is basically the exact test that I've run on previous models. Here we go. Simulation of virus attacking cells in a bloodstream. We have different sliders for the number of viruses, as you can see here. We have the replication rate. We have the types of viruses: aggressive, stealth, and fast replicating. Number of white blood cells, white blood cell speed, detection range, and so on. So, very cool.
[04:53] [VISUAL: Example 4 - A vinyl record simulation where text forms the grooves] We also have this vinyl simulation, drop the needle to play. So we have kind of like a circular set of words and then I drop the needle and it starts playing. Now it doesn't have any sound, which is kind of weird. I would have thought it had sound, but it doesn't. But it still looks very cool.
[05:25] [VISUAL: Example 5 - Making music in a coding environment called Strudel] And then last, it allows you to create live music using Strudel, which I had not heard of, but looks very cool. [SOUND: Electronic music starts playing] So Strudel, I believe, is a coding language that allows you to create music. So, very cool examples. And stick around, I'm going to show you one more example later in the video of a test that my team ran on Kimi K2 and I was blown away by it.
[06:44] [VISUAL: Text section on "Agentic Search and Browsing"] Kimi K2 Thinking is also really good at search and integrating the information from search into its thinking process, and then running subsequent searches based on everything it learned so far. So on BrowseComp, a challenging benchmark designed to evaluate model's ability to continuously browse, search, and reason over hard-to-find real-world web information, Kimi K2 Thinking achieved a score of 60.2%, significantly outperforming the human baseline of 29.2%. Kimi K2 Thinking can execute 200-300 sequential tool calls driven by long-horizon planning and adaptive reasoning.
[07:18] [VISUAL: A complex logic puzzle prompt is shown] Now, look at this complex logical problem that Kimi K2 was given. So, "The information below is about an individual who is an alumnus of a university founded after 1860 but before 1890, was a university athlete and later played for a professional American football team briefly, starred in a science fiction film about an alien invasion that was released after 2010 but before 2020," and so on. So it's kind of like a teaser problem.
[07:45] And so look at its thinking. It's reasoning, it's reasoning, it does a search, reasoning some more, does another search, and back and forth it goes until it finally comes up with Jimmy Gary Jr.
[07:56] [VISUAL: "Practical Writing" and "Personal & Emotional" sections] They also say Kimi K2 is really good at creative writing, but I'm usually pretty doubtful that AI is any good at that.
[08:03] [VISUAL: A full benchmark table comparing Kimi K2, GPT-5, Claude, DeepSeek, and Grok-4] So if you want to check out the full benchmarks, they're right here and I will also drop a link to this in the description below.
[08:09] [VISUAL: A series of tweets reacting to the Kimi K2 release] Alright, now let me give you a few reactions from some AI leaders throughout the web on Kimi K2 Thinking's release. Alright, first, Emad Mostaque, friend of the live show, founder of Stability AI, says, "Congratulations to @Kimi_Moonshot for achieving state of the art on many benchmarks & open sourcing the model! The gap between closed & open continues to narrow even as the cost of increasingly economically valuable tokens collapses. K2 has its own unique vibe too, try it out!!"
[08:37] Now he goes on to talk about the cost of the new model's training. Listen to this. "Base Kimi K2 model used 2.8m H800 hours with 14.8 trillion tokens, about 
5.6
m
w
o
r
t
h
.
"
W
h
i
c
h
,
b
y
t
h
e
w
a
y
,
i
s
c
r
a
z
y
t
o
t
h
i
n
k
a
b
o
u
t
t
h
a
t
t
h
e
s
e
f
r
o
n
t
i
e
r
m
o
d
e
l
s
a
r
e
g
e
t
t
i
n
g
s
o
c
h
e
a
p
t
o
t
r
a
i
n
.
T
h
e
n
h
e
s
a
y
s
,
"
D
e
t
a
i
l
s
o
f
p
o
s
t
t
r
a
i
n
i
n
g
f
o
r
r
e
a
s
o
n
i
n
g
n
o
t
g
i
v
e
n
,
b
u
t
i
t
i
s
l
i
k
e
l
y
m
a
x
20
5.6mworth."Which,bytheway,iscrazytothinkaboutthatthesefrontiermodelsaregettingsocheaptotrain.Thenhesays,"Detailsofposttrainingforreasoningnotgiven,butitislikelymax20
3m for sota if they had Blackwell chip access." Very interesting to think about. The cost of training frontier models is dropping so quickly.
[09:14] [VISUAL: Tweet from Sebastian Raschka comparing DeepSeek R1 and Kimi K2 Thinking architectures] All right, and of course, everyone's thinking, how does this compare to DeepSeek? Can you believe in 2025, at the very beginning of 2025, we had the DeepSeek moment with R1, and now at the end of 2025, we have the Kimi K2 moment. An incredibly both open-source, open-weights models.
[09:33] [VISUAL: Detailed architectural diagrams] So on the left, we have DeepSeek R1, 671 billion parameters, and Kimi K2 Thinking is a trillion parameters. The vocabulary size, bigger is better, 129,000 versus 160,000 on the vocab size for Kimi K2 Thinking. Both of them are mixture of experts with the DeepSeek having 256 and Kimi K2 Thinking having 384 experts. So more experts. And interestingly, even though this is a bigger model, there are 37 billion parameters active during inference for DeepSeek and 32 billion active during inference for this new Kimi K2 Thinking model. So even less, more efficient. And they are equal context lengths at 128,000. Thank you to Sebastian Raschka for putting this together.
[10:24] And by the way, if you want to learn to use Kimi K2 Thinking and other models, you should download "The Subtle Art of Not Getting Replaced" ebook. [VISUAL: Ebook cover appears] This ebook contains 100 different use cases that you can use AI for today. Real-world use cases. So check it out, download it, let me know what you think.
[10:43] [VISUAL: Blog post by Nathan Lambert titled "5 Thoughts on Kimi K2 Thinking"] Nathan Lambert of interconnects.ai, expert at all things training, had this to say about Kimi K2 Thinking. He says early reports it has a distinctive style in writing, which is very welcome. And interestingly, he says it's a 256K context length. I thought it was only 128, but it seems like it might actually be 256. Trillion total parameters, 32 billion active parameters, we just talked about that.
[11:08] And I think really the crux of his writing and what I've been thinking about a lot is right here in this section. "China's rise. At the start of the year, most people loosely following AI probably knew of 0 AI labs. Now, and towards wrapping up 2025, I'd say all of DeepSeek, Owen, and Kimi are becoming household names. They all have seasons of their best releases and different strengths. It took many Chinese companies only 6 months to catch up to the open frontier in ballpark of performance. Now the question is if they can offer something in a niche of the frontier that has real demand for users." So it really seems like not only has open-source open-weights caught up to frontier models, but also they're kind of just coming out of China. We had an open-weights model from OpenAI, but it's not a frontier model, that is GPT-5. We haven't had another version of Llama from Meta, and so yeah, China is really pushing the open-source, open-weights frontier.
[12:06] [VISUAL: A complex web app development task being shown to Kimi K2] Alright, now let me show you what my team created with Kimi K2 Thinking. You can get to this on kimi.com. "Analyze the relationship between population density and healthcare facility accessibility in Ghana. 1. Download the latest WorldPop population raster and any open dataset of health facility coordinates. 2. Compute the average population density within a 10km radius around each facility. 3. Rank the top 10 districts by lowest per-capita facility coverage. 4. Generate a choropleth map and a bar chart comparing the results."
[12:39] Okay, so check this out. It is writing a to-do, and this is OK Computer, and this is something specific to Kimi. So this is kind of like a scratchpad and an environment that it can run in. So this is just beyond impressive. So, boom, created a full to-do list, started marking off the to-dos, as you can see, did some searches, browsing, here we go. You can actually see the browse happen. So here it went to WorldPop, clicked around all of this stuff happened. We only gave it one piece of feedback. "This part of it is a mess" and "just go debug and fix it." And watch this. Let me show you the end result.
[13:16] [VISUAL: A polished, interactive data dashboard titled "Healthcare Accessibility in Ghana"] Here we go. Remember, this is created entirely by Kimi K2 Thinking and one piece of feedback. So, "Healthcare Accessibility in Ghana." Boom. Executive summary. The page looks nice. Here we have an interactive map where you actually have an overlay. It tells you more information about the healthcare facility. And remember, it downloaded all this information. It just found it. District-level disparities. Here we have more interactive charts. Look at this. This is just unreal. All these different types of charts and graphs. So, so impressive. At the bottom, we have even more. Forgive the colors, I'm just using dark mode everything. It would look a lot better if I turned that off. We have limitations and next steps, data sources and methodology. You can download the CSVs of the facility analysis, district coverage, and underserved areas. And again, all of this created in just a few minutes with really one prompt. So impressive.
[14:11] [VISUAL: Vultr logo] And once again, thank you to Vultr for sponsoring this video. Click through the link in the description below. Let them know I sent you. Try out incredible open-source models. Thanks again to Vultr. So that's it. My team is fully testing the Kimi K2 Thinking model. We're going to put together a full testing video most likely. So stick around for that. If you enjoyed this video, please consider giving a like and subscribe and I'll see you in the next one.
TAXONOMY ANALYSIS
Workflows Identified
WORKFLOW 1: Analyze Healthcare Data and Create a Dashboard
OBJECTIVE: To analyze the relationship between population density and healthcare facility accessibility in Ghana and generate an interactive web dashboard.
STEPS:
Define the core question and objectives.
Create a to-do list (plan of action).
Search for and download the WorldPop population raster data.
Search for and download health facility coordinates for Ghana.
Explore and clean the data.
Compute the average population density within a 10km radius around each facility.
Rank the top 10 districts by lowest per-capita facility coverage.
Generate a choropleth map.
Generate a bar chart comparing results.
Assemble all elements into a comprehensive analysis dashboard (HTML report).
Debug and fix overlapping elements based on user feedback.
Deploy the final website.
DURATION: A few minutes.
COMPLEXITY: High.
TOOLS USED: Kimi K2 Thinking, OK Computer (internal environment), Web Browser (tool), Code Interpreter (implied).
INPUT: A 4-step natural language prompt detailing the analysis requirements.
OUTPUT: A fully interactive, multi-section HTML dashboard with maps, charts, executive summary, and downloadable CSV files.
WORKFLOW 2: Create a Web-Based Word Processor
OBJECTIVE: To build a functional clone of a word processor application (like Microsoft Word) that runs in a web browser.
STEPS:
Develop the user interface with a toolbar.
Implement rich text editing features (bold, italic, underline, strikethrough).
Implement font and font size selection.
Implement "Save" functionality to download the document as an HTML file.
DURATION: Not specified (created from a single prompt).
COMPLEXITY: Medium-High.
TOOLS USED: Kimi K2 Thinking.
INPUT: A single prompt to "create a Word clone".
OUTPUT: A functional, interactive web application.
WORKFLOW 3: Create an Animated Math Visualization
OBJECTIVE: To create an animated visualization explaining the concept of Gradient Descent in 2D.
STEPS:
Generate code to plot a 2D grid with contours.
Animate the path of gradient descent from a starting point to the minimum.
Display changing coordinate and function values during the animation.
Render the animation as a video.
DURATION: Not specified (created from a single prompt).
COMPLEXITY: Medium.
TOOLS USED: Kimi K2 Thinking.
INPUT: A single prompt to "create a visualization of gradient descent".
OUTPUT: An animated video explaining a mathematical concept.
Action Verbs & Operations
A. CREATION VERBS
Create
Generate
Build
Develop
Write
B. MODIFICATION VERBS
Fix
Debug
Update
C. ANALYSIS VERBS
Analyze
Compare
Evaluate
Test
Reason
Compute
Rank
Explore
Understand
D. ORGANIZATION VERBS
Plan
Mark off
E. COMMUNICATION VERBS
Break down
Show
Report (implied in dashboard)
F. DATA & SYSTEM VERBS
Download
Search
Browse
Execute
Click
Save
Deploy
Task Chains
Data Analysis Dashboard Creation: Define task → Search for data → Download datasets → Execute code (compute & rank) → Generate visualizations → Assemble HTML report → Receive feedback → Debug & fix → Deploy final dashboard.
Web App Creation: Receive prompt (e.g., "Word clone") → Generate HTML/CSS/JS → Deploy interactive application.
Complex Reasoning: Receive puzzle → Break down attributes → Search for information → Reason based on findings → Refine search → Synthesize information → Provide final answer.
Responsibilities Vocabulary
Professional Roles Mentioned:
Data Analyst (implied by the Ghana healthcare task)
Web Developer (implied by the Word clone and dashboard tasks)
AI Researcher (implied by model training discussions)
Responsibilities/Activities:
"achieving state of the art on many benchmarks"
"open sourcing the model"
"solving a PhD-level mathematics problem"
"creating a component-heavy website"
"analyzing the relationship between population density and healthcare facility"
"generating a choropleth map and a bar chart"
"fully testing the... model"
Skills Mentioned:
Reasoning
Tool-use
Coding
Data analysis
Web browsing
Long-horizon planning
Adaptive reasoning
Tools & Technologies Matrix
Tool Name	Category	Purpose	Used For	Mentioned With
Kimi K2 Thinking	Large Language Model	Open-source agentic AI model	Reasoning, tool-use, coding, data analysis	GPT-5, Claude 4.5, DeepSeek R1
DeepSeek R1	Large Language Model	Open-source frontier AI model	Comparison for architecture and performance	Kimi K2 Thinking
GPT-5	Large Language Model	Closed-source frontier AI model	Benchmark comparison	Kimi K2 Thinking, Claude 4.5
Claude Sonnet 4.5	Large Language Model	Closed-source AI model	Benchmark comparison	Kimi K2 Thinking, GPT-5
Vultr	Cloud Computing	GPU and cloud infrastructure provider	Running and deploying AI models	Kimi K2 Thinking
Strudel	Creative Coding	A coding language for live music creation	Generating music from code	Kimi K2 Thinking
OK Computer	AI Environment	Kimi's internal environment for code execution and tool use	Running the steps for the Ghana analysis	Kimi K2 Thinking
WorldPop	Data Source	A dataset for population distribution	Providing raster data for the Ghana analysis	Kimi K2 Thinking
Objects & Deliverables
Interactive Web Dashboard
Web Application (Word clone)
Animated Visualization (Gradient descent video)
Live Music Composition
Data Files (CSV)
Choropleth Map
Bar Chart
Logical Puzzle Solution
To-Do List / Plan of Action
Integration Patterns
INTEGRATION: Kimi K2 Thinking + Web Search + Web Browser + Code Interpreter (OK Computer)
PURPOSE: To perform complex, multi-step data analysis tasks from a single prompt, from data acquisition to final report generation.
FLOW: Natural language prompt → Kimi generates a plan → Kimi uses Web Search to find data sources → Kimi uses Web Browser to navigate and download files → Kimi uses Code Interpreter to process data and generate charts/maps → Kimi assembles everything into an HTML dashboard.
Business Concepts & Strategy
Open-Source vs. Closed-Source Models: The video highlights the narrowing gap, with open-source models from China (Kimi, DeepSeek) now competing with and even surpassing closed-source U.S. models (GPT-5, Claude) on specific tasks.
Cost of Training: Mentioned that training a frontier model like Kimi K2 costs approximately 
5.6
m
i
l
l
i
o
n
∗
∗
,
w
i
t
h
t
h
e
p
o
t
e
n
t
i
a
l
t
o
b
e
u
n
d
e
r
∗
∗
5.6million∗∗,withthepotentialtobeunder∗∗
3 million with newer hardware (Blackwell chips), indicating a rapid decrease in the cost of developing SOTA AI.
Rise of Chinese AI Labs: A significant theme is the emergence of Chinese companies (Moonshot, DeepSeek) as major players in the open-source AI space, rapidly catching up to the performance of Western labs.
Agentic AI as a Product: The entire demonstration of Kimi K2 is a showcase of agentic capabilities—the ability to plan, use tools, and execute complex tasks autonomously—as the primary value proposition.
Optimization & Best Practices
OPTIMIZATION: Model Efficiency (Inference)
TECHNIQUE: Using a Mixture-of-Experts (MoE) architecture with a higher number of experts but activating fewer parameters during inference.
REASON: This allows the model to have a vast total parameter count (1 trillion) for knowledge storage while remaining computationally efficient and cheaper to run by only using a small fraction (32 billion) of those parameters for any given task.
EVIDENCE: [09:55 - 10:15] Comparison between DeepSeek R1 (37B active) and Kimi K2 (32B active) shows Kimi is more efficient despite being a larger overall model.