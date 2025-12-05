{
  "Video Title": "n8n Quickstart: Master Workflow Automation Fundamentals",
  "Channel/Creator": "Max Tkacz (The original Flowgrammer)",
  "Video URL": "https://youtu.be/UtXzdmpysmU",
  "Duration": "14:38",
  "Publication Date": "[Not Provided]",
  "Description": "In this video, we'll look at the best freelance and remote hiring websites. Whether you're a startup looking to scale quickly, a freelancer seeking your next project, or a company aiming to fill a specialized role remotely, this video is for you. We'll explore the top platforms that have transformed the hiring landscape, making it more flexible, diverse and accessible than ever before.",
  "Key Topics": [
    "n8n Workflow Fundamentals",
    "Triggers and Actions in n8n",
    "Data Handling and Item Passing",
    "Conditional Logic and Routing (If Node)",
    "Connecting Apps and Services (Slack Integration)",
    "Data Transformation using Expressions (Date/Time Helpers)",
    "Testing and Troubleshooting Workflows (Pin Data)",
    "Webform Automation"
  ],
  "Links Referenced": [
    {
      "Link": "community.n8n.io",
      "Description": "Official n8n community forums"
    },
    {
      "Link": "n8n.io/workflows/",
      "Description": "n8n Templates Library"
    }
  ],
  "Word-for-Word Transcription": [
    "[00:00] Hey, I'm Max, the original Flowgrammer, and welcome to your n8n quickstart. I'm going to teach you the key fundamentals to building any n8n workflow. That includes triggers and actions, how items of data work between steps in your n8n workflows, how to map data between those steps and transform it and route it based on business logic.",
    "[00:21] I'm also going to teach you how to connect to apps and services so you can perform actions in those apps and services in your app stack. And we're going to do this all with a super simple workflow. It's an installation request. So there'll be a web form and it'll send a notification to Slack. It's a simple workflow to teach you the key fundamentals of n8n that you can leverage in your actual use cases. And if you came here wanting to build some fancy AI stuff, I hear you, it's very exciting, there's a lot of hype about it right now, but I strongly recommend that you watch this video first, learn these foundations, and then jump off into that agentic future. All right, with all that in mind, let's switch to n8n and begin.",
    "[00:56] I'm here in a brand new n8n workspace, and let's start a new workflow from scratch. This is going to take us to the workflow canvas. This is where you build out your workflow, activate it, and then it runs automatically, it saves you a bunch of time. Let's add our first step to the workflow, and that's going to be a workflow trigger. In n8n, we have triggers that kick off workflows, and then we have actions that perform steps in your workflow. There's lots of different types of triggers that you can leverage. For example, if you want to kick off the workflow based on an event in an app or service that you use in your app stack, you can go on to 'On app event'. If you're building an AI chatbot, perhaps you're going to start off with our chat trigger. Since today we're creating a web form automation, let's start off with an 'On form submission', because n8n is going to give us a web form that we can give to the end user to fill out to kick off the workflow. Let's click to add that to the canvas.",
    "[01:41] This added the node to the canvas by default, the trigger node, the form trigger. And we can see that it's a trigger node because it's got this lightning bolt on it, and if I hover near it, it gets its own 'Execute workflow' button. Let's go ahead and set it up. There's various parameters that you need to fill out before you can execute a step. These are required fields, as you can see here, there's an error around the form title. So let's go ahead and give it a title: 'Request an installation'. And let's also give it a description: 'Fill out this form to request an installation. We'll reach out via email to finalize your appointment.' Next, let's add the form fields that we want the users to actually fill out. These are called 'Form Elements' in n8n. Let's add the first one, and let's ask for the email. And since an email is text, we could keep this to text, but we do have a specific 'Email' type, and this offers a bit extra data validation when the user fills that out, if they get the email wrong. So let's add that. And we won't add a placeholder for now, but let's make it required field.",
    "[02:31] And then let's also capture their preferred install date, so we can do a bit of conditional routing based on that, and I can show you how to work with data and manipulate it in n8n as well. And let's set that to a 'Date', because then it'll be a nice little date picker for the user to use. So now let's respond when the form is submitted, so it'll just say, 'Hey, great, your form was submitted', but in future, you could make this a multi-step form if you're evolving this. Now that I've filled out the parameters of my node, the next thing is we need to test it, and we do that by clicking 'Execute step'. In the case of the form trigger, this pops up a test form. This is what your end user is going to see once you activate the workflow. Let's go ahead and fill that out. [ACTION: Types 'name@email.com' and selects 19th June 2025]. Let's say my preferred install date, I need this in two days. I'm really busy, I got to get this stuff installed. So I submit that. Okay, let's go ahead and close that pop-up. And we can see that it executed successfully, and there's a green checkmark in my output here, and I have some output data here as well.",
    "[03:20] How nodes work in n8n, be it a trigger or an action, is they run their step and then they output some data, and that's what we can see here in the output. There's a few different ways to visualize that data. For example, I'm looking in JSON mode right now, because most of this data does get passed in JSON format in n8n. So this is a rather true-to-form representation of that data. I can also see it as a table, if that's useful for the type of data I'm looking at. And there's also a schema view, which extrapolates the schema of this data and shows it in a format where if I had nesting, I could also collapse it. This would be a good juncture in time to talk about n8n items, what they are, and how to work with them. So as you can see, we have '1 item' of data in my output. And if I go to my workflow, we can see the node executed successfully, it's got a green check, there's an item of data coming out of that as well. What is an item of data? Basically, each node in n8n, including this trigger node, outputs an array of items. That's its payload that it sends out that you can pipe in to the next step. Now, the one contract between nodes in n8n is that they always need to pass along this array, and it should have zero to many items. In this case, we have one item of data in here because there's one element in this top-level array, which is why there's one item here. That's going to be useful for you to know because most n8n nodes perform their step on each item of data, and a lot of folks sometimes get the looping paradigm wrong and try to add looping steps when they don't need to, because again, n8n nodes perform each step on each incoming item of data. That'll become clearer in the next step when we add some conditional routing.",
    "[04:44] Before we continue though, if I continue to test my workflow, be it from the 'Execute step' button here, or 'Execute workflow' button here, I'm going to continue seeing that pop-up and I'm going to have to fill it out. Now, in our web form, that's not too bad, there's just two form fields, but what if it's a subscription event for Stripe or something that's difficult to replicate for my main system? It's going to be really annoying to basically keep creating test data as I do that. So what you can do is pin the data in this node. So each time that we run it, it just outputs the pinned data. To do that, we can hit this 'Pin data' button here. This data is now pinned. We can see that visualizing in the canvas as well. So each time I mash this 'Execute workflow' button, it doesn't actually run, it just outputs whatever payload was sitting in there. Super useful pro tip that I highly recommend. With pinned data, once I activate my workflow, it won't be used on those production executions, but it will stay here for when I come back here for a future session, when I maybe want to test my flow.",
    "[05:33] Let's now add some conditional routing logic that routes it to Slack if the preferred install date is within 7 days, and otherwise continues the workflow. To do that, I'll click the plus button here, and since I want some conditional routing, we need to go into the 'Flow' section of my nodes panel. And here there's various things that can control the flow. What we need here is an 'If' node. If you do need to have multiple output branches, depending on more complex conditional logic, you could also opt for the 'Switch' node. In this case, we're just checking if it's under 7 days away, so we can use the 'If' node, and I'll drag and drop that onto the canvas. Just to contextualize this, we can now see I've got my pinned trigger, sending one item of data into my 'If' node. If I open it up, I can see that I've got the one item of data flowing into here, and in the 'If' node, it also has parameters that we set up to inform how the step runs. And we do this by setting up one or many conditions that we evaluate, and they might evaluate to true or false, and they'll go out the true branch or the false branch.",
    "[06:29] Let's set up the first condition. To do that, we want to check if the preferred install date is 7 days into the future of right now or not. So we can actually drag and drop that onto this value, and this turns it to an expression in n8n. Before it was set to 'Fixed', that's the default, so it just treats this as text, which I can also type. But if it's set to an expression, anything within these curly brackets will be treated as an expression that is evaluated, and we can see the evaluated result here is that date. So I can drag and drop data from previous nodes and map them into the steps for current nodes to perform the current step. Right? So, the next thing that we need to do is the operation that we want to evaluate basically value one to value two, right? Since this is a date time, we do have date and time operators, which is useful because dealing with dates and times can be a little clunky mentally, and so this kind of helps make sure that you've got sound logic for that. So let's set this to 'is before or equal to'.",
    "[07:22] And we're going to get an error because we don't have anything set in the second value yet. But for the second value, how to think of this: I have a date, we don't know what time it is, and we want to check if it's younger than 7 days from now. So we've got to get the 'now' and add seven to it, right? To do that, we can set an expression. I'll go ahead and set an expression there, and I'll do two open brackets, and in here, I see an autocomplete shows up. And in n8n, we do have a helper function to get the time right now. It's called `$now`. So let's click to add that. And we can see it's printed a date time, but we want now plus seven days. So if I hit period, I can access autocomplete and see the various helper methods that I can use. If you're familiar with JavaScript, this is also JavaScript, so you can apply JavaScript methods here as well. But the n8n team has a bunch of helper methods in addition to JavaScript for the things that JavaScript might not cover. Let's add the `plus` method, and we can see here there's a mini documentation on how to use it. We need to specify an integer on how much to increment the current date time, and the units to do that by. So days. So actually we need exactly what's in this example. So let's click to add that, and then in here, let's write `7, 'days'`. And we can see that is now 7 days in the future. If we run this, it does work because this gets cast to a date, even though this is currently a text, as you can see this little A character there. To make this a bit more robust and just to show the different methods at work, I can again hit a period here, it accesses the autocomplete, and there is a `toDateTime()` method available here. There's a bunch of others that you can look at as you're going through your use case, but this one makes it just a little bit more robust. So now we're comparing a date time to a date time. Let's test that. It's true, that's great. We could test this again, make sure the logic's working because we set a date two days in advance, so this should go to the false branch. That's working correctly. We'll set that back. Great. So now we've got conditional logic, we're routing to the true branch, and we can see it's coming out there.",
    "[09:15] Now, before we add the Slack node, let's annotate our workflow so it's a little clearer when we come back. And we can do that by actually modifying the name of this 'If' node. Let's say 'Is within 7 days?' A little tip I like to do for my conditional nodes is phrase it as a question, so it's kind of clear what the true condition means versus the false condition. And before we add the Slack step, for the false branch, just for completeness, let's actually add a 'No operation' node. Now, as the name implies, the 'No operation' node doesn't really do anything, but it can be renamed, for example, 'To-do'. There's a few more advanced use cases for it, but right now we're just going to use it as a placeholder, so it's clear later in the flow if we want to evolve that. On to the Slack step. Let's click the plus from the true branch, because if it's within 7 days, we want to send a Slack notification to someone on the team. That's going to be within 'Action in an app'. I can also just search for it from here. But just so you see where that is in the app, I would go in 'Action in an app'. I could scroll down to find it, or again, just search inline here. Let's click on Slack. Now, there's a lot of different actions in Slack. Again, I could search for that, but what we're looking for is to send a message, and so I'm going to click on the 'Send a message' action here.",
    "[10:20] And it's connected to my workflow. We can just confirm that by going back to the canvas and seeing that's going to the true branch. Now we just need to set up the Slack step. For most app nodes, you are going to have to set a credential for it. This is an entity within n8n where you add your API key or whatever that service expects, and then n8n can connect to that service on your behalf. I have already created a Slack credential for my Slack, but you can create a new one inline from here as well. You're going to see this screen here. If you're on n8n Cloud, I do recommend the OAuth route because you get the fancy just click to connect experience, you go through the Slack pop-up, and it autoconnects. Otherwise, you are going to have to go create an access token. But if you're stuck on that, you can open the n8n docs to do that, and you can also rename your credential as well. I'll use one that I already created, but that is going to be the first step. Now, the resource and operation is already set because we picked that from the nodes panel. So we're sending a message. Now we need to pick who we send this message to, right? So let's drop down here, and let's send this to a channel. And in this case, let's pick from a list, although I could also set this by ID. Again, there's an expression here. That could be a dynamic thing in a more advanced workflow in future. So let's go ahead and select a channel. Let's send it to the 'sales' channel. And let's do a simple text message, but you could use Slack blocks in future. That's what's going to allow you to have buttons and all manner of those sorts of things. And for the message text, let's set this to an expression, and let's actually open this up so I can see a bit of a bigger view. And I'm going to paste in the static text that I would like. So, 'New install request (within 7 days). Contact email: Preferred install date:'. And again here, we're just going to drag and drop values from earlier in my workflow. The most recent node is auto-expanded, but I could also map values from previous nodes as well. In this case, they're the same because the conditional node doesn't manipulate data, it just routes it. So let's go ahead and get that preferred install date and map that here as well. Now, again here, I could combine these texts, I could write a lot more, but you get the idea. I can combine static and dynamic text to send a useful notification. All right, let's test this by running it. We got a success check, which means it worked. Let's go over to Slack and confirm that. And great, we can see that came in here. Contact email name@email.com, automated with this n8n workflow. Perfect. We can open up that workflow if we ever need to troubleshoot in future. Let's run that one more time just to be sure. Worked again here, and now we see two here. Perfecto. Next, let's go back to my workflow canvas, and before we get too excited, let's save our workflow. Now that the workflow is saved, if we leave this, it's not going to work automatically yet, because we haven't activated the workflow. So far, we've run a test execution, we've done a test form, but we need to activate the workflow. And then as the workflow runs, executions are going to accrue in the 'Executions' tab of this workflow. So you can see there's a bunch of this test workflows that we just ran, signified by this beaker icon here. And if I take that production URL from the web form, so if I go here, I copy that, and in a new tab, I enter that, I can see the form is now live. And if I fill this out, let's do a different one, let's say `max@company.co`, and let's pick an install date also pretty soon, and submit that. We can see firstly that that ran really quickly. That's very cool. But then if I go into my workflow and into 'Executions', I can see I have an execution that came in that doesn't have this beaker icon. This is a production execution. I can go in here, I can inspect that, I can understand if it failed perhaps, or if I want to update the logic. And one last thing to point out, a little pro tip before you go, is that I can copy this into the editor. This is going to unpin the current data that I have, repin the data from that current execution, and now I could continue building with that latest production execution, which is super useful if you're troubleshooting or if you're just evolving your workflow. Wow, you did it. Good for you. I hope you found this video helpful. You're well on your way to becoming a Flowgrammer if you keep it up. There's a ton of resources in our global community to help you on your journey as you learn. The first place you're probably going to want to go is community.n8n.io. That's our official community forums where you can post questions. We've also got the n8n Templates Library, that's n8n.io/workflows/. Really excited for you to start your automation journey. Everyone at n8n believes that you should own the means of your automation. And so on that note, happy Flowgramming!"
  ],
  "TAXONOMY ANALYSIS": {
    "Workflows Identified": [
      {
        "WORKFLOW": "Installation Request Automation (Core)",
        "OBJECTIVE": "Automate the process of receiving an installation request via a web form, applying conditional logic based on the preferred date, and notifying the sales team via Slack if the request is urgent (within 7 days).",
        "STEPS": [
          "Trigger workflow on form submission (Webform)",
          "Apply conditional logic to check if preferred install date is within 7 days ('Is within 7 days?')",
          "If True (urgent), send Slack notification to 'sales' channel",
          "If False (not urgent), route to 'To-do' placeholder node"
        ],
        "DURATION": "Quick execution (246ms in test)",
        "COMPLEXITY": "Medium",
        "TOOLS USED": [
          "n8n (Webform, If Node, Slack Node, No Operation Node)"
        ],
        "INPUT": "User input (Email Address, Preferred Install Date)",
        "OUTPUT": "Slack notification or To-do placeholder entry"
      },
      {
        "WORKFLOW": "Node Setup and Testing (General Process)",
        "OBJECTIVE": "Configure and verify functionality of an individual workflow step.",
        "STEPS": [
          "Add node to canvas",
          "Fill out required parameters (Form Title, Description, Elements)",
          "Execute step (to generate test data)",
          "Review output data (JSON, Table, Schema views)",
          "Pin data (for consistent testing)",
          "Execute workflow (to test full flow)"
        ],
        "DURATION": "Variable (setup/testing time)",
        "COMPLEXITY": "Low",
        "TOOLS USED": [
          "n8n Editor"
        ],
        "INPUT": "Node parameters, test data",
        "OUTPUT": "Successfully executed node with verified output data"
      }
    ],
    "Action Verbs Extracted": {
      "CREATION VERBS": [
        "Build (workflow, chatbot, form)",
        "Create (workflow, test data, credential)",
        "Phrase (as a question)"
      ],
      "MODIFICATION VERBS": [
        "Transform (data)",
        "Map (data)",
        "Rename (node, credential)",
        "Update (logic)",
        "Evolve (workflow)"
      ],
      "ANALYSIS VERBS": [
        "Look at (websites)",
        "Explore (platforms)",
        "Learn (foundations)",
        "Check (logic)",
        "Evaluate (conditions)",
        "Inspect (execution)"
      ],
      "ORGANIZATION VERBS": [
        "Set up (conditions, parameters)",
        "Route (items, flow)",
        "Send (notification, message)",
        "Connect (to apps/services)",
        "Pin (data)",
        "Unpin (data)",
        "Accrue (executions)"
      ],
      "COMMUNICATION VERBS": [
        "Teach",
        "Welcome",
        "Post (questions)",
        "Share"
      ],
      "BROWSER/AGENTIC OPERATIONS": [
        "Click",
        "Run (step, workflow)",
        "Execute (step, workflow)",
        "Enter (URL)",
        "Fill out (form)",
        "Submit (form)",
        "Hover (near element)",
        "Access (autocomplete)"
      ],
      "DATA OPERATIONS": [
        "Output (data, array, payload)",
        "Pass (responses)",
        "Pipe in (payload)",
        "Cast (to a date)",
        "Increment (date time)",
        "Combine (text)",
        "Convert (types)",
        "Get (time)"
      ]
    },
    "Task Chains": [
      "Start Workflow from Scratch → Go to Workflow Canvas → Add Trigger Node (Form Submission) → Set Node Parameters → Execute Step (Test Form) → Pin Data → Add If Node (Conditional Routing) → Add Slack Node (True Branch) → Add No Operation Node (False Branch) → Save Workflow → Activate Workflow → Test Production URL → Monitor Executions",
      "Set Up Conditional Logic: Drag Preferred Install Date → Set Operator ('is before or equal to') → Set Comparison Value ($now.plus(7, 'days')) → Execute Step"
    ],
    "Responsibilities Vocabulary": {
      "Roles": [
        "Flowgrammer (Max)",
        "End User",
        "n8n Team"
      ],
      "Activities": [
        "building any n8n workflow",
        "learning these foundations",
        "connecting to apps and services",
        "performing actions in apps",
        "creating a web form automation",
        "testing my flow",
        "troubleshoot in future",
        "evolving your workflow"
      ],
      "Skills": [
        "Flowgramming",
        "Automation",
        "Troubleshooting",
        "JavaScript (expressions/methods)"
      ]
    },
    "Tools & Technologies Matrix": [
      {
        "Tool Name": "n8n",
        "Category": "Workflow Automation Platform",
        "Purpose": "Building and running automated workflows",
        "Used For": "Triggers, actions, data transformation, connecting services",
        "Mentioned With": "Slack, Google Sheets, Telegram, Notion, Airtable, etc."
      },
      {
        "Tool Name": "Slack",
        "Category": "Communication/Collaboration App",
        "Purpose": "Sending notifications/messages",
        "Used For": "Posting messages to a channel",
        "Mentioned With": "n8n (Slack Node)"
      },
      {
        "Tool Name": "Webform",
        "Category": "n8n Trigger/Input",
        "Purpose": "Collecting user input to start a workflow",
        "Used For": "Installation request submission",
        "Mentioned With": "On form submission"
      },
      {
        "Tool Name": "If Node",
        "Category": "Flow Control",
        "Purpose": "Conditional routing based on logic",
        "Used For": "Checking if date is within 7 days",
        "Mentioned With": "True/False branch"
      },
      {
        "Tool Name": "No Operation Node",
        "Category": "Utility/Flow Control",
        "Purpose": "Placeholder for future steps; performs no action",
        "Used For": "Marking a 'To-do' path",
        "Mentioned With": "To-do"
      }
    ],
    "Objects & Deliverables": [
      "Workflow",
      "Trigger",
      "Action",
      "Item (of data)",
      "Payload",
      "Expression",
      "Credential (API key, OAuth)",
      "Webform",
      "Form Elements (Email, Date)",
      "Slack message/notification",
      "Test execution",
      "Production execution",
      "n8n Docs",
      "Templates Library"
    ],
    "Integration Patterns": [
      {
        "INTEGRATION": "n8n Node Data Flow",
        "PURPOSE": "Passing output data from one node as input to the next.",
        "FLOW": "Trigger Node Output (JSON array) → Item Flow → Conditional Node Input"
      },
      {
        "INTEGRATION": "n8n + Webform",
        "PURPOSE": "Collecting external user data to trigger automation.",
        "FLOW": "User Submits Form → On Form Submission Trigger Node"
      },
      {
        "INTEGRATION": "n8n + Slack",
        "PURPOSE": "Sending automated notifications.",
        "FLOW": "Conditional Node (True Branch) → Slack Node (Post Message)"
      },
      {
        "INTEGRATION": "n8n Expressions + Data",
        "PURPOSE": "Dynamically inserting and manipulating data within steps.",
        "FLOW": "Data Field (e.g., Preferred Install Date) → Expression (`{{ $json['Preferred install date'].toDateTime() }}`) → Step Parameter"
      }
    ],
    "Business Concepts & Strategy": [
      "Flowgrammer (Self-designated expert role)",
      "Agentic Future (Advanced automation concept)",
      "App Stack (Collection of integrated software services)",
      "Global Community (Support/Learning resource)",
      "Automation Journey"
    ],
    "Optimization & Best Practices": [
      {
        "OPTIMIZATION": "Workflow Testing Efficiency",
        "TECHNIQUE": "Use 'Pin Data' on the trigger node.",
        "REASON": "Allows repeated testing of subsequent nodes without re-submitting the form/triggering the external event.",
        "EVIDENCE": "[05:04 - 05:33]"
      },
      {
        "OPTIMIZATION": "Conditional Logic Clarity",
        "TECHNIQUE": "Rename 'If' nodes as clear questions (e.g., 'Is within 7 days?').",
        "REASON": "Improves readability and maintenance of the workflow.",
        "EVIDENCE": "[09:15 - 09:30]"
      },
      {
        "OPTIMIZATION": "Date Handling Robustness",
        "TECHNIQUE": "Use `toDateTime()` helper method on input strings before comparison.",
        "REASON": "Ensures consistent data types for reliable conditional logic evaluation.",
        "EVIDENCE": "[08:44 - 08:58]"
      },
      {
        "OPTIMIZATION": "Troubleshooting/Debugging",
        "TECHNIQUE": "Use the 'Executions' tab to view production runs and copy data back to the editor.",
        "REASON": "Allows debugging production errors using real data without altering the live flow.",
        "EVIDENCE": "[13:35 - 13:57]"
      }
    ]
  }
}