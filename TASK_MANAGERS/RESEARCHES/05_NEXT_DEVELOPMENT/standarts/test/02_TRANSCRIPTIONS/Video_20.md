---
category: 02_TRANSCRIPTIONS
subcategory: root
type: transcript
source_id: Video_20
title: Video 20
date: 2025-11-22
status: draft
owner: unknown
related: []
links: []
---

# Video 20

## Summary
- TODO

## Context
- TODO

## Data / Content
{
  "Video Title": "To-Do List App with JavaScript - From Scratch to Functional!",
  "Channel/Creator": "Codynn",
  "Video URL": "[Not Provided]",
  "Duration": "18:56",
  "Publication Date": "[Not Provided]",
  "Description": "End product of our JavaScript Beginner Series. We are diving into something super exciting. We are building a Task Manager App or a To-Do List App with the help of JavaScript. Imagine having a simple app where you can add tasks, delete them when we are done, and even fetch tasks from an external source, all using JavaScript.",
  "Key Topics": [
    "JavaScript To-Do List App Development",
    "DOM Manipulation (getElementById, createElement, innerHTML, appendChild, remove)",
    "Event Listeners (click)",
    "Asynchronous JavaScript (fetch API, async/await)",
    "Task Addition and Deletion"
  ],
  "Links Referenced": [
    "Boilerplate HTML/CSS/JS files (mentioned in description)"
  ],
  "Word-for-Word Transcription": [
    "[00:00] Hello everybody and welcome back to the end product of our JavaScript Beginner Series. When starting this series, we told you guys that we would be coding a real-life project with the help of the things that we learned throughout the series. And today is the day for that. Today we are diving into something super exciting. We are building a Task Manager App or a To-Do List App with the help of JavaScript. And imagine having a simple app where you can add tasks, delete them when we are done, and even fetch tasks from an external source, all using JavaScript. So that is pretty cool in my opinion.",
    "[00:34] And by the end of this video, we will have a web app or a webpage which is something similar to this. [VISUAL: Shows the Task Manager interface with input field, 'Add Task' button, and 'Fetch API Tasks' button]. So, in this Task Manager App, we can add tasks. Suppose, 'Teach our viewers how to make this'. [ACTION: Types text and hits Enter]. Hit enter and add this to our list of tasks. And when we are done with the task, we can click this delete button right here to remove this task from our list.",
    "[01:02] And we can add multiple tasks as much as we want. Remove all of them. And even fetch tasks from an API. [ACTION: Clicks 'Fetch API Tasks' and five tasks appear]. So, like this. Now, without wasting any time, let's start with coding this. [01:16] [VISUAL: Codynn logo transition] We have opened our coding compiler and this is the web dev section of the compiler. And this right here is our default boilerplate code for this video or this project. And it consists of a simple input field where we can enter our tasks, and it consists of a button which adds our task to the task list, and also another button which fetches API tasks from an API. And an unordered list for holding our list items. So, this is the HTML code and we have created a simple CSS file to style our heading, our input field, our Add Task button, and our Fetch API Tasks button.",
    "[02:01] So, since we have our main focus on JavaScript, we will not be focusing on these. These files will be provided to you guys in the description. And let's get to our JavaScript code. So, first things first, in order to make this website interactive, we have to select each individual element that we want to interact with. So, for that, I am going to create four variables to select our necessary elements. So, `const taskInput` for our input field, `const addTaskButton` as the name suggests for our task button, or Add Task button, and a selector for or a variable for selecting our `taskList` itself, and finally a variable for selecting our `fetchTasksButton`. So `fetchTasksButton`.",
    "[03:02] So I'm going to select each of these elements which I have mentioned by using a selector called `document.getElementById`, which we have discussed in our previous lessons. So if you don't know about that, please do check it out. So `taskInput` equals `document.getElementById()`. So I'm just going to write down this for each of the variable that we have defined. So [ACTION: Copies and pastes `document.getElementById()` three times]. And I'm going to check out what IDs do these element have. So, for our input field we have given it an ID of `taskInput`, for our Add Task button, `addTask`, our task list, `tasklist` ID, and for this button right here we have given an ID `fetchTasks`. So I'm going to write these IDs in our selectors. So `taskInput`, and then our `addTask`, our `tasklist`, and our `fetchTasks`.",
    "[04:24] Now, once we are done selecting our necessary elements, we can head over to making them interactive. Now, in order to do that, we will have to create a function which takes the task that we enter in this input field, and on the click of this button, it will add that task onto our task list. And for that, it should create a new list element by fetching the value that is entered into this input field. So, we have to create a function which will create a list element first, and then append that element to our unordered list. So, I want you guys to pause the video and try it out for yourself. And if you have any difficulties, you can always check it out right here. So, let's get onto it.",
    "[05:06] First, we'll create a function by using the function keyword, and let's name this function `addTask`. So, let's say we have to store whatever the user or we ourselves enter inside this place into a variable. Let's create a variable for that, for storing our input. So `const taskText` let's say, equals now we have already selected this input field right here from our DOM. So this field is called `taskInput`. So I'll say `taskInput` and for fetching its value, we'll write `.value`.",
    "[05:49] And we have to create an element first. So `const li` equals `document.createElement` and our element is a list item, so we'll give it a tag of `li`. So this is our list item right here. Now we want to add content to the newly created list element, and we want that content to be the task that the user enters here. So we will change its inner HTML by using `li.innerHTML` equals we'll create a set of backticks to use our `taskText` variable dynamically, by writing a dollar sign then `taskText`. And let's say we have to create a button which deletes the task as well. So I'll create a button `class='delete'` let's say. I'll give it a class of `delete`. And then I'll say 'Delete' or you can add an emoji of a delete X or cross button right here. I'll for now I'll add 'Delete' and then button.",
    "[07:07] So, this will be the content of our newly created list item. And after creation of the list item, we have to add that list item to our task list. So, our parent element is the unordered list, which we have selected in the variable called `taskList`. So `taskList.appendChild`. And the child we want to append is our `li` variable right here, which we have created. So, after adding our task to our task list, we want to clear the input field for the user to enter another task, if the user wants to do so. So, for that, we'll do `taskInput.value` equals an empty string, which means clearing the input field. So, this is it for our `addTask` function.",
    "[08:04] And I have noticed that this C should be capital right here, and this function is now complete. Now, we want to make it so that whenever a user clicks on this Add Task button, this `addTask` function executes. And we will achieve that through the use of event listeners. So we have discussed that in our JavaScript Beginner Series. And we do that by setting or attaching an event listener to this Add Task button. So we have selected this button in this variable right here. So `addTaskButton.addEventListener` and let's say we should execute this function on 'click', and then the function to be executed is `addTask`. So, by doing this, we have attached an event listener to this button right here, which when clicked adds our task from the input field onto our task list. So, let's see what happens if we enter, um, let's say 'Take out the trash' and click on this button.",
    "[09:15] So, we can see that this 'Take out the trash', which is our task, has been added onto our task list. So our function and our event listener is working perfectly. Now, if we want to delete this task right here, we would naturally click on the delete button. But we can see that clicking on it does nothing. So, this is because we have not created a function that deletes the task, and we have not attached it to the delete button. And in order to make the delete button functional, we'll have to do just that. So, this will help us delete the task that we have already completed. And we'll now head on to creating a function which deletes the task. So, let's say `deleteTask`.",
    "[10:00] And this function will take a parameter which is `e`, and you can assume this as the event object, which we had discussed previously. It contains all the details regarding the event that is triggered. And we will open the function right here, and we will create a condition which reads: `if (e.target.classList.contains('delete'))` [10:30] a delete class, which we had added to our buttons, or our delete buttons when we created this right here. So this class 'delete'. If it contains the 'delete' class, it will remove its parent element. So `e.target.parentElement.remove()`. So, the reason I typed `parentElement.remove()`: when we create the delete button, it is a child element of our list element. So first we create the list element right here, and then we have created a button element inside the list element. So since we want to delete the whole list item itself from our task list, we remove the parent. So, when the delete button is clicked, it will remove its parent element, that is the newly created list item.",
    "[11:21] So, inside this `deleteTask` function, this first line essentially asks if we have clicked on something that has the class 'delete'. So `classList.contains('delete')` asks if we have clicked on something that has the class 'delete', and if the condition is true, it removes its parent element. So, now that we have created the function, let's see this in action. Now, in order to see this in action, we have to attach this function to our task list, or our unordered list. So, to do that, we will have to use the `taskList.addEventListener` on 'click' and then `deleteTask`, our function. Now, let's see if this works. So, I'll use 'Wash the dishes' as our example, and hit 'Add Task'. The `addTask` function is working fine. Now let's see if we can delete this task. [ACTION: Clicks Delete].",
    "[12:28] And as you can see, the task that had been added has been successfully deleted from our task list. So, we have already created a basic version of our To-Do List App where we can add tasks and delete tasks after they're done. So, we have already created a basic version of our To-Do List App where we can add tasks to our task list, and after they are done, we can delete them right away with one click on the delete button. So, we can take this app to another level by fetching tasks from an external API. Now, this is not entirely necessary, but in order to use and demonstrate the fetching mechanism in JavaScript, and in order to incorporate that into our To-Do List App, we will be doing just that. So, we'll create an asynchronous function which is `async function fetchTasks()` that will fetch tasks from an API. So `try` `const response = await fetch('https://jsonplaceholder.typicode.com/todos?_limit=5')`.",
    "[13:46] And then in another variable that is `const data`, we will await a response and then convert it into a JavaScript object. So `response.json()`. And after that, we'll be using something called a `forEach` loop. So, since we have stored our `response.json()`, which returns an array, in the variable called `data`, we'll use a `forEach` loop to loop through each item in the array. So `data.forEach(task => { ... })`. Now, each item that is present in the array is stored in this `task` variable. So, for each item in the array, we want to execute a certain code. In this case, for every task in the data array, we want to create a new list element and add that list element to our list or unordered list, which is our task list. So, for that, we will have to create a list variable like we did in our previous function, that is `addTask`, and then use `document.createElement` and our element that we want to create is a list element. So this. And in a similar way as we did before, we want to change its inner HTML and use our backticks to use the value of `task.title`.",
    "[15:25] So, which stores the title or which uses the title of each task item that is present in the array that we receive from the API. So `task.title`. And then we create a button for deleting the task. So `button class='delete'` let's say it's class is 'delete'. And then it says 'Delete' and then we'll close our button. So, we have changed its inner HTML and now we will append this item, our list item, by using `appendChild` to our unordered list, which is our task list. So this. And after writing the code for our try block, we have to write a catch block for any errors that might occur. So `catch(error)` and let's say `console.error('An error occurred while fetching tasks: ' + error)`.",
    "[16:49] So, we did make a function for fetching tasks from an API and adding them to our task list. Now, let's attach that function to our Fetch API Tasks button. Now, we'll use our `fetchTasksButton` and use `.addEventListener`. Let's say we have to trigger that event on 'click', and then we have to trigger this function. So `fetchTasks`. And let's not forget to close our function right here. We'll close this. And then we'll see if our code works as intended. So, let's say 'Finish the project video' and 'Add Task'. So it has been added to our task list and then 'Delete', so it is being deleted as well. And let's see if our newly created Fetch API Tasks or `fetchTasks` function works. So, let's click on this. And we can observe that our Fetch API Tasks button is working fine, which means that our `fetchTasks` function is working fine as well. And let's see if we can delete the task that we just fetched from an API. And delete, delete, delete, delete, delete. So we can see that our `deleteTask` function that we created previously is working well on this Fetch API Tasks button as well. So, delete, delete, delete, delete, delete, delete.",
    "[18:21] So, in this video, we built a simple yet functional Task Manager App by using JavaScript. And let's quickly recap what we did. We created a function and added it to our button so that we could add tasks to the list. We can delete tasks from the list, and we can fetch API tasks from an external API and display them on our screen. So, if you found this project video helpful, don't forget to like, share, and subscribe for more beginner-friendly JavaScript projects. So, let me know in the comments how your Task Manager App turned out, and we'll catch you in the next video. Thank you."
  ],
  "TAXONOMY ANALYSIS": {
    "Workflows Identified": [
      {
        "WORKFLOW": "Create To-Do List App (Task Manager)",
        "OBJECTIVE": "Build a functional web application allowing users to manage tasks.",
        "STEPS": [
          "Select necessary DOM elements (input, buttons, list container)",
          "Implement addTask function (handle user input, create list item, clear input)",
          "Implement deleteTask function (handle click event on delete button, remove parent element)",
          "Implement fetchTasks function (handle asynchronous API request, parse JSON, iterate through data, display tasks)",
          "Attach event listeners to buttons and task list container"
        ],
        "DURATION": "Approx. 18 minutes (tutorial time)",
        "COMPLEXITY": "Medium",
        "TOOLS USED": [
          "JavaScript",
          "HTML",
          "CSS",
          "Codynn Compiler",
          "JSON Placeholder API"
        ],
        "INPUT": "Boilerplate HTML/CSS code, External API endpoint",
        "OUTPUT": "Functional Task Manager Web App"
      },
      {
        "WORKFLOW": "Add Task Workflow",
        "OBJECTIVE": "Allow user to input and persist a new task on the list.",
        "STEPS": [
          "Enter task text into input field",
          "Click 'Add Task' button",
          "Execute `addTask` function",
          "Fetch value from input field",
          "Create new list item (`li`) element",
          "Set `li.innerHTML` with task text and 'Delete' button",
          "Append new `li` to `taskList` (UL)",
          "Clear input field value"
        ],
        "DURATION": "Instantaneous (on click)",
        "COMPLEXITY": "Low",
        "TOOLS USED": [
          "JavaScript (DOM methods)",
          "HTML (Input, Button, UL/LI)"
        ],
        "INPUT": "User-entered task string",
        "OUTPUT": "New list item appended to the DOM"
      },
      {
        "WORKFLOW": "Fetch API Tasks Workflow",
        "OBJECTIVE": "Retrieve external tasks from an API and display them.",
        "STEPS": [
          "Click 'Fetch API Tasks' button",
          "Execute `fetchTasks` asynchronous function",
          "Await HTTP response using `fetch`",
          "Await conversion of response to JSON data array",
          "Loop through each task object in the data array (`forEach`)",
          "For each task, create list item (`li`)",
          "Set `li.innerHTML` using `task.title` and 'Delete' button",
          "Append new `li` to `taskList`"
        ],
        "DURATION": "Dependent on network latency",
        "COMPLEXITY": "Medium",
        "TOOLS USED": [
          "JavaScript (async/await, fetch, forEach)",
          "JSON Placeholder API"
        ],
        "INPUT": "API URL",
        "OUTPUT": "Multiple list items populated from external data"
      }
    ],
    "Action Verbs Extracted": {
      "CREATION VERBS": [
        "Create (function, variables, element, button)",
        "Build",
        "Code",
        "Write"
      ],
      "MODIFICATION VERBS": [
        "Delete (tasks)",
        "Remove (parent element)",
        "Change (inner HTML)",
        "Clear (input field)",
        "Style"
      ],
      "ANALYSIS VERBS": [
        "Discuss",
        "Assume",
        "Check out",
        "Observe",
        "Read (condition)"
      ],
      "ORGANIZATION VERBS": [
        "Select (elements)",
        "Store (response, data, value)",
        "Append (child)",
        "Loop through (array)",
        "Hold (list items)",
        "Convert (to JavaScript object)"
      ],
      "COMMUNICATION VERBS": [
        "Provide",
        "Share",
        "Subscribe",
        "Recap",
        "Demonstrate",
        "Display"
      ],
      "BROWSER/AGENTIC OPERATIONS": [
        "Click",
        "Execute (function)",
        "Enter (task)"
      ],
      "DATA OPERATIONS": [
        "Fetch (tasks, value)",
        "Await (response, JSON)",
        "Contains (class list)",
        "Return (array)"
      ]
    },
    "Task Chains": [
      "Select Elements → Create addTask Function → Create deleteTask Function → Create fetchTasks Function → Attach Event Listeners",
      "User Enters Task → Click Add Task → Get Value → Create LI + Button → Append LI → Clear Input",
      "User Clicks Delete Button → Check if target contains 'delete' class → Remove Parent Element (LI)",
      "Click Fetch API Tasks → Await Fetch (API URL) → Await Response.JSON → ForEach Task in Data → Create LI (Title + Delete Button) → Append LI"
    ],
    "Responsibilities Vocabulary": {
      "Roles": [
        "Viewer",
        "User"
      ],
      "Activities": [
        "coding a real-life project",
        "building a Task Manager App",
        "making them interactive",
        "selecting necessary elements",
        "storing input",
        "fetching tasks from an external API",
        "attaching an event listener"
      ],
      "Skills": [
        "JavaScript programming",
        "DOM manipulation",
        "Event handling"
      ]
    },
    "Tools & Technologies Matrix": [
      {
        "Tool Name": "JavaScript",
        "Category": "Programming Language",
        "Purpose": "Core logic and interactivity",
        "Used For": "DOM manipulation, function creation, asynchronous requests",
        "Mentioned With": "HTML, CSS, fetch API"
      },
      {
        "Tool Name": "HTML",
        "Category": "Markup Language",
        "Purpose": "Structure the web page elements",
        "Used For": "Defining input fields, buttons, and lists",
        "Mentioned With": "CSS, JavaScript"
      },
      {
        "Tool Name": "CSS",
        "Category": "Styling Language",
        "Purpose": "Visual presentation and layout",
        "Used For": "Styling the Task Manager interface",
        "Mentioned With": "HTML"
      },
      {
        "Tool Name": "Codynn Compiler",
        "Category": "Development Environment",
        "Purpose": "Hosting and executing web development code",
        "Used For": "Writing and testing HTML/CSS/JS",
        "Mentioned With": "Web dev section"
      },
      {
        "Tool Name": "JSON Placeholder API",
        "Category": "External API (Dummy Data)",
        "Purpose": "Source external tasks data",
        "Used For": "Fetching sample 'todos' array",
        "Mentioned With": "fetch"
      }
    ],
    "Objects & Deliverables": [
      "To-Do List App",
      "Task Manager App",
      "Web App/Webpage",
      "Tasks (list items)",
      "Input field",
      "Add Task button",
      "Delete button",
      "Fetch API Tasks button",
      "Unordered list (UL)",
      "List item (LI)",
      "Variables",
      "Functions",
      "Event listeners",
      "API data (JSON array)"
    ],
    "Integration Patterns": [
      {
        "INTEGRATION": "HTML + JavaScript (DOM Selection)",
        "PURPOSE": "Connect front-end elements to JavaScript logic for manipulation.",
        "FLOW": "HTML Element ID → becomes → JavaScript Variable (document.getElementById)"
      },
      {
        "INTEGRATION": "JavaScript + HTML (Event Handling)",
        "PURPOSE": "Trigger JavaScript functions based on user interaction.",
        "FLOW": "Button/List Element → addEventListener('click') → Function Execution"
      },
      {
        "INTEGRATION": "JavaScript + External API",
        "PURPOSE": "Retrieve external data for display.",
        "FLOW": "JavaScript (async fetch) → API Endpoint → Await Response → Parse JSON → Data Array"
      }
    ],
    "Business Concepts & Strategy": [
      "Beginner Series (Educational structure)",
      "Real-life project (Practical application of skills)"
    ],
    "Optimization & Best Practices": [
      {
        "OPTIMIZATION": "DOM Interaction Efficiency (Deletion)",
        "TECHNIQUE": "Use event delegation by attaching the listener to the parent list (`taskList`) and checking `e.target.classList` for 'delete'.",
        "REASON": "Avoids attaching a new listener to every dynamically created list item.",
        "EVIDENCE": "[11:45 - 12:12]"
      },
      {
        "OPTIMIZATION": "Input Clearing",
        "TECHNIQUE": "Set `taskInput.value = ''` after successful task addition.",
        "REASON": "Improves user experience for adding subsequent tasks.",
        "EVIDENCE": "[07:42 - 08:04]"
      },
      {
        "OPTIMIZATION": "Asynchronous Data Handling",
        "TECHNIQUE": "Use `async/await` and `try/catch` with the `fetch` API.",
        "REASON": "Manages network requests efficiently and handles potential errors gracefully.",
        "EVIDENCE": "[13:15 - 16:48]"
      }
    ]
  }
}

## Findings
- TODO

## Actions / Next Steps
- TODO

## Metrics / Status
- TODO

## Attachments / Links
- TODO

## Change Log
- 2025-11-22 standardization scaffold added
