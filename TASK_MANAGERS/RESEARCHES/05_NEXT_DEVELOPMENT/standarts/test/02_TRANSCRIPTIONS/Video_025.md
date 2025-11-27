---
category: 02_TRANSCRIPTIONS
subcategory: root
type: transcript
source_id: Video_025
title: Video 025
date: 2025-11-24
status: draft
owner: unknown
related: []
links: []
---

# Video 025

## Summary
- TODO

## Context
- TODO

## Data / Content
{
  "video_title": "How to Automate The Entire Recruitment Process",
  "metadata": {
    "creator": "Jono",
    "duration": "13:32",
    "topics": [
      "Recruitment Automation",
      "Make.com Workflows",
      "GoHighLevel CRM",
      "Google Sheets Integration",
      "Indeed Application Parsing"
    ],
    "tools_referenced": [
      "Indeed",
      "Make.com",
      "GoHighLevel",
      "Google Sheets",
      "Gmail"
    ]
  },
  "description": "A comprehensive tutorial on automating the recruitment process using a stack of four tools: Indeed, Make.com, GoHighLevel, and Google Sheets. The video demonstrates how to parse applicant emails from Indeed, automatically create contacts in a CRM, send screening questionnaires, manage candidates via a Google Sheet dashboard, and automate interview scheduling and rejection emails.",
  "taxonomy_analysis": {
    "workflows": [
      {
        "workflow_name": "Indeed Application to CRM Pipeline",
        "objective": "Capture applicants from Indeed emails and create contacts in CRM",
        "steps": [
          "Watch Gmail for new Indeed application emails",
          "Parse email body to extract candidate name, email, and position",
          "Send data via Webhook to GoHighLevel",
          "Create or update contact in GoHighLevel",
          "Send automated email with screening form link"
        ],
        "tools_used": [
          "Gmail",
          "Make.com",
          "GoHighLevel"
        ],
        "complexity": "High",
        "input": "Indeed Email Notification",
        "output": "New CRM Contact & Screening Request Email"
      },
      {
        "workflow_name": "Screening Form to Dashboard",
        "objective": "Update recruitment dashboard with candidate screening responses",
        "steps": [
          "Candidate submits screening form",
          "Webhook triggers Make.com scenario",
          "Search for existing row in Google Sheets by Contact ID",
          "Update row with screening answers, resume link, and voice recording",
          "Update status to 'Screening Completed'"
        ],
        "tools_used": [
          "GoHighLevel",
          "Make.com",
          "Google Sheets"
        ],
        "complexity": "Medium",
        "input": "Form Submission",
        "output": "Updated Google Sheet Row"
      },
      {
        "workflow_name": "Dashboard Review & Action",
        "objective": "Manually review candidates and trigger automated follow-ups",
        "steps": [
          "Review candidate data in Google Sheets",
          "Check 'Screening Approved' or 'Rejected' box",
          "Make.com watches for sheet changes",
          "Router splits path based on checkbox",
          "If Rejected: Send rejection email",
          "If Approved: Send email with one-time booking link"
        ],
        "tools_used": [
          "Google Sheets",
          "Make.com",
          "GoHighLevel"
        ],
        "complexity": "High",
        "input": "Google Sheet Checkbox Update",
        "output": "Candidate Notification Email"
      }
    ],
    "action_verbs": {
      "creation_verbs": [
        "Create",
        "Build",
        "Generate",
        "Draft"
      ],
      "modification_verbs": [
        "Update",
        "Edit",
        "Parse",
        "Refine",
        "Filter"
      ],
      "analysis_verbs": [
        "Review",
        "Screen",
        "Evaluate",
        "Check",
        "Search"
      ],
      "organization_verbs": [
        "Organize",
        "Schedule",
        "Categorize",
        "Store",
        "Map"
      ],
      "communication_verbs": [
        "Send",
        "Notify",
        "Email",
        "Message",
        "Reply"
      ],
      "browser_agentic_operations": [
        "Watch",
        "Trigger",
        "Execute",
        "Connect"
      ],
      "data_operations": [
        "Parse",
        "Extract",
        "Webhook",
        "Scrape",
        "Import",
        "Export",
        "Match",
        "Lookup"
      ]
    },
    "task_chains": [
      "Indeed Apply -> Gmail Watch -> Parse Text -> Webhook -> Create Contact",
      "Form Submit -> Webhook -> Search Sheet Row -> Update Sheet Row",
      "Sheet Update -> Watch Changes -> Router -> Send Email"
    ],
    "responsibilities_vocabulary": {
      "roles": [
        "Business Owner",
        "Recruiter",
        "Hiring Manager"
      ],
      "activities": [
        "Reviewing applicants",
        "Automating recruitment",
        "Parsing emails",
        "Managing Google Sheets",
        "Scheduling interviews"
      ],
      "skills": [
        "Automation architecture",
        "CRM management",
        "Workflow design",
        "Data parsing"
      ]
    },
    "tools_matrix": [
      {
        "tool": "Make.com",
        "category": "Automation",
        "purpose": "Orchestrate workflows and connect apps",
        "used_for": "Parsing emails, routing data, watching sheets"
      },
      {
        "tool": "Indeed",
        "category": "Sourcing",
        "purpose": "Job posting and applicant source",
        "used_for": "Generating initial leads"
      },
      {
        "tool": "GoHighLevel",
        "category": "CRM",
        "purpose": "Manage contacts and forms",
        "used_for": "Storing candidate data, hosting forms, sending emails"
      },
      {
        "tool": "Google Sheets",
        "category": "Database",
        "purpose": "Central dashboard for review",
        "used_for": "Tracking candidates, triggering actions via checkboxes"
      },
      {
        "tool": "Gmail",
        "category": "Communication",
        "purpose": "Receive application notifications",
        "used_for": "Triggering the automation pipeline"
      }
    ],
    "objects_deliverables": [
      "Automated Recruitment Dashboard (Google Sheet)",
      "Candidate Screening Form",
      "One-time Booking Links",
      "Automated Email Sequences",
      "Parsed Candidate Data"
    ],
    "integration_patterns": [
      {
        "integration": "Gmail + Make.com",
        "purpose": "Extract data from unstructured emails",
        "flow": "Email Body -> Text Parser -> Structured Data"
      },
      {
        "integration": "Make.com + Google Sheets",
        "purpose": "Bi-directional sync for dashboard management",
        "flow": "Webhook Data -> Sheet Row; Sheet Update -> Webhook Trigger"
      },
      {
        "integration": "GoHighLevel + Make.com",
        "purpose": "Execute communication actions",
        "flow": "Webhook -> Create Contact -> Send Email"
      }
    ],
    "business_concepts": [
      "Time Savings (hours to minutes)",
      "Wide Net Hiring Strategy",
      "Automated Screening",
      "CRM Centralization"
    ],
    "optimization_techniques": [
      {
        "optimization": "Email Parsing",
        "technique": "Use regex/text split to extract data from standard notification emails",
        "reason": "Avoids manual data entry from Indeed"
      },
      {
        "optimization": "One-time Links",
        "technique": "Generate unique booking links that expire",
        "reason": "Prevents candidates from booking multiple interviews or spamming calendar"
      },
      {
        "optimization": "Hidden Form Fields",
        "technique": "Pass email/ID as hidden query parameters in form URLs",
        "reason": "Ensures data consistency and prevents duplicate contact creation"
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
- 2025-11-24 standardization scaffold added
