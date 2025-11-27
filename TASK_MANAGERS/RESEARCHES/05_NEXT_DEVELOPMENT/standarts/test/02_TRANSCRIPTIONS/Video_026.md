---
category: 02_TRANSCRIPTIONS
subcategory: root
type: transcript
source_id: Video_026
title: Video 026
date: 2025-11-24
status: draft
owner: unknown
related: []
links: []
---

# Video 026

## Summary
- TODO

## Context
- TODO

## Data / Content
[
  {
    "video_title": "Automated Sales Dashboard Creation with n8n and Lovable",
    "description": "This video demonstrates how to create an automated sales dashboard using two distinct workflows in n8n. The first workflow ingests sales data from incoming emails, parses it with an AI agent, and updates a Google Sheet. The second workflow exposes this data via a secure webhook, which is then used by Lovable to build and display a dynamic, real-time sales dashboard with various charts and metrics.",
    "tags": [
      "n8n",
      "automation",
      "sales dashboard",
      "lovable",
      "webhook",
      "ai agent",
      "google sheets",
      "no-code",
      "workflow automation"
    ],
    "transcript": [
      {
        "start": "00:00",
        "end": "00:06",
        "text": "Hello everyone and welcome to another lesson. I'm very happy to have you here with me today."
      },
      {
        "start": "00:06",
        "end": "00:10",
        "text": "Today we're going to do an exciting sales dashboard."
      },
      {
        "start": "00:10",
        "end": "00:28",
        "text": "So the the idea is today we're going to be able to, uh, I mean, all of us, we have income. I mean, most of the the people who watch my channel are people who have side income, side streams of income, and they make money on the side."
      },
      {
        "start": "00:28",
        "end": "00:58",
        "text": "Uh, and I thought that maybe we can do an automation and uh tie that up with a lovable interface so we can do a sales dashboard that will give us the current sales, this month sales, past month sales, and uh also a year overview with pie shop with charts and pie charts. So we're going to we're going to do that today and I'm going to explain to you how we're going to do that step by step."
      },
      {
        "start": "00:58",
        "end": "01:07",
        "text": "So, uh, that being said, let's go over first the first, um, the because it's split into two workflows."
      },
      {
        "start": "01:07",
        "end": "01:14",
        "text": "So the first workflow is the workflow that we see in front of us, which is it starts with an email trigger."
      },
      {
        "start": "01:14",
        "end": "01:29",
        "text": "So this uh this waits on any email that is coming uh through your attached uh account. Uh I have a I don't have here a Gmail account. I have my uh my personal uh domain account."
      },
      {
        "start": "01:29",
        "end": "01:42",
        "text": "Um so if you have for example a domain, mine is AI autokit.io. I have an for example info at AI autokit.io, so you can uh put that in here."
      },
      {
        "start": "01:42",
        "end": "01:56",
        "text": "And what I'm saying is uh email trigger. So anything that is unseen, anything, any email that I get that is unseen, just uh give me a notification or trigger this whole workflow, okay?"
      },
      {
        "start": "01:56",
        "end": "02:04",
        "text": "This is the first step. The second step is we will check if the uh if the sender is within these domains."
      },
      {
        "start": "02:04",
        "end": "02:29",
        "text": "Okay? So because we don't want to uh to have every email because we're probably getting uh sales data from specific emails. For example, an example would be Stripe. So whenever we're going to get an email from Stripe or for example uh notification at stripe.com, whenever we get an email from that, it will be true and it will continue to the next check."
      },
      {
        "start": "02:30",
        "end": "02:45",
        "text": "So first, we check is it from the emails that we usually get sales from? And then, uh, here we have an or between them, so they don't have to all be true to continue. Any of them is true, just continue."
      },
      {
        "start": "02:45",
        "end": "03:18",
        "text": "And then the next one would would be subject check. And here we're saying that if the if the subject contains sold or sale or sold or payment of, then proceed and continue. The reason why is sometimes, for example from Stripe, we don't get always uh notifications or emails on that we've made money. Sometimes we'll get emails, uh marketing emails, sometimes uh tax invoices, sometimes things that are not related to payments."
      },
      {
        "start": "03:18",
        "end": "03:26",
        "text": "And this is why I have this check. It will check that only the uh the emails that have this in the title."
      },
      {
        "start": "03:26",
        "end": "03:41",
        "text": "And then after both of these are done and it is true, it will go to our AI thinking agent and this agent has uh I've put as Deepseek R1 as the brain and it has a structured output as this schema."
      },
      {
        "start": "03:41",
        "end": "04:07",
        "text": "So basically what we're saying here inside of this agent is we're we're going to take the uh we're going to take the uh the subject of the email, whether if the text plain is true, take it, if it's not, take the text.html. So if this uh if the text plain is is exists, take it."
      },
      {
        "start": "04:07",
        "end": "04:39",
        "text": "Then we're saying that you're an expert email analyzer and then we say that you need to uh output this JSON product amount, date and type. And then sources to keep in mind. So we're saying what's what what is the email source? Here if it's domain one, if it comes for example from Stripe, then it's a store related. If it comes from whatever other domain, it's newsletter, if it comes whatever domain it's affiliate. This will uh will uh categorize our uh sales information."
      },
      {
        "start": "04:39",
        "end": "04:57",
        "text": "And then of course, as I said, I want a structured. So here the structure would be product, it's a string, price, it's a number, date, so uh all of that would be uh you we would have all of that."
      },
      {
        "start": "04:57",
        "end": "05:01",
        "text": "And then we need to update the the database and the database is this one. So I have some mock data here."
      },
      {
        "start": "05:01",
        "end": "05:27",
        "text": "So the the database is called sales and it has product, price, type and date. This is all what we need to have uh the dashboard. And here it will keep on updating uh it will keep on updating the whole thing with new information as it gets. So whatever new email that I will get, this will be triggered and then it will update the the database with new information."
      },
      {
        "start": "05:29",
        "end": "06:08",
        "text": "So if we can see here, this is a test run that I had before. An email that uh landed in my inbox and it went through the true true. Uh the output was template one uh and then the as the product, the price was 18, the date gave me the date and the uh and the type is uh gave me store exactly as I have it. And then it updated the the database. So this is part one of the whole uh workflow."
      },
      {
        "start": "06:08",
        "end": "06:14",
        "text": "The second one, uh and this is a very interesting one, and this is the one that will uh keep on updating our dashboard."
      },
      {
        "start": "06:14",
        "end": "06:23",
        "text": "So what this one is, it starts with a webhook and this webhook has a uh has of course a production URL."
      },
      {
        "start": "06:23",
        "end": "06:31",
        "text": "But what what's important is that I've put a credentials for this. So I can create new credentials."
      },
      {
        "start": "06:31",
        "end": "06:43",
        "text": "And I could have authorization and then I put a I generate a long uh string of text as a password for example and I hit save."
      },
      {
        "start": "06:43",
        "end": "06:58",
        "text": "This will give our webhook a password and authorization. That means that no one can access this because it's very important this is sales data information for us and we don't want anyone to access this except the people that are authorized."
      },
      {
        "start": "06:59",
        "end": "07:24",
        "text": "So you can you can create your own authorization for your own webhooks. Just as any API, other API has authorization. Now you can with this with a webhook, you can create your own authorization and you can name it whatever you want. You can name it authorization or you can name it your name here, you can name it whatever you want and you can put the uh the long uh the key uh for here and save and it will be saved."
      },
      {
        "start": "07:25",
        "end": "07:38",
        "text": "And of course, use the production URL, don't use the test URL. And then in the respond, you should always uh say respond to webhook node because there's a respond to webhook at the end."
      },
      {
        "start": "07:38",
        "end": "08:03",
        "text": "So when this is triggered, what we do is we go, we all, we we just go and get the sales information from here. So what we're doing is that we we're saying get me all information from this database. And then we aggregate them into one field, all item into one field, and then we'll respond with every with all the items that we got back to the webhook."
      },
      {
        "start": "08:05",
        "end": "08:28",
        "text": "All right, so now that we have both of our workflows uh ready to go. So this is active, this is active, everything is ready to go. Uh so this will wait for any sales email, it will update our database and this will wait for any uh calls from our dashboard to get all the information."
      },
      {
        "start": "08:28",
        "end": "09:17",
        "text": "Now what we want to do is go to Lovable. So I go to Lovable here and here I put a long uh uh a long prompt on what I want uh exactly for the dashboard. So this prompt that I wrote here, I've done a lot of iterations on it in order to get a single prompt that gets me the dashboard that I want. Uh and as you can see also, I've attached an an image that I created that I've made so that it follows the visual style of that image that I created."
      },
      {
        "start": "09:17",
        "end": "09:51",
        "text": "this whole prompt, you you can get it with both of these workflows uh as JSONs uh so you can create your own dashboard easily by just importing uh you say import from file for both of these workflows and then uh you take the uh you take the prompt and the picture and you can create your own custom sales dashboard or you can sell this for clients uh by creating dashboards for them."
      },
      {
        "start": "09:51",
        "end": "10:17",
        "text": "So obviously we're going to we're going to wait for this until it finishes because it's going to take a a couple of uh minutes to get our dashboard finished and running. Uh so uh I'm going to wait for this to finish and then I'll get back to you. I'll pause this video. So when this is finished, we can see the final product."
      },
      {
        "start": "10:18",
        "end": "10:35",
        "text": "So as you can see, it's still running. I just wanted to give you an update. Uh so once it's over, I'll I'll get back to you guys and see what what it's done. It's not very long, but it's just thinking through and editing."
      },
      {
        "start": "10:35",
        "end": "10:45",
        "text": "All right, it just finished. As you can see, we have our dashboard here. Let's see if we can open it in a new tab. There you go."
      },
      {
        "start": "10:46",
        "end": "11:23",
        "text": "Now how beautiful is this? So we have our sales dashboard. uh here our sidebar like menu. Uh it has the word sales and it is it comes with a logo. It has the current month sales and gives us a how the trend is from last month. It it gives us the last month sales, it gives us this year and the total sales so far. And here it gives us a uh daily sales by type and here it specifies the types that we have."
      },
      {
        "start": "11:23",
        "end": "11:34",
        "text": "And here it gives us the general uh pie chart of uh what are the divisions by by type. Now, how beautiful is that?"
      },
      {
        "start": "11:34",
        "end": "12:20",
        "text": "So that was all made from the first the uh prompt that we gave it and then the image that we supplied it in order to make this dashboard. Uh of course, let's get back to N8N. So this is all taking information from this webhook. As you can see here, if we go to executions, here you say you can see it it executed this one and it uh it gave the information back. It gave us 163 and then it aggregated them and then sent it back to the webhook."
      },
      {
        "start": "12:20",
        "end": "12:57",
        "text": "So for example, this one, if we uh if we copy this one and then we paste it in here and we put a really ridiculous number here, like uh let's say 340 and then we change the date to today's date for example, and then we waited on it until it saves and then we go back here and then we uh refresh this, we should see a a change in the dashboard. There you go."
      },
      {
        "start": "12:57",
        "end": "13:02",
        "text": "As you can see here, we made $340 and the uh the whole price changed and here it changed as well."
      },
      {
        "start": "13:02",
        "end": "13:32",
        "text": "So as you can see, it's a live dashboard that takes information from a live webhook. Uh I hope you guys enjoyed this lesson. Uh I will put everything so the uh both of these JSONs, I will put them and the image and the prompt uh available uh inside of my community. I'll put a link to my community below so you can access all that and you can make your own sales beautiful sales dashboard like this one. Uh I hope you guys enjoyed this one. Uh please give it a like, subscribe for more videos and see you in the next one."
      }
    ]
  }
]

## Findings
- TODO

## Actions / Next Steps
- TODO

## Metrics / Status
- TODO

## Attachments / Links
- TODO

## Change Log
- 2025-11-24 standardization scaffold added
