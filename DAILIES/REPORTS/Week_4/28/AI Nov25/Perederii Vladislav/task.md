# Task Breakdown - November 28, 2025

## Instructions
**What**: Detailed action steps
**Include**:
- Break each plan item into specific steps
- Add links and resources
- Clear instructions for execution

**Important Note:** All work will be done manually (no AI assistant) for efficiency and due to token limits.

---

## Task 1: Continue Processing Job Site Vacancies

### Steps:
1.  **Check System Status:** Before starting, check the status of the Google Cloud account to ensure there are sufficient funds and API quotas are not near their limits.
2.  **Run the Processing Script:** Initiate the main Python script responsible for cleaning and enriching the raw vacancy data.
3.  **Monitor Performance:** Periodically check the script's logs and the output table to ensure the process is running smoothly and without errors.
4.  **Plan Next Step:** While the script is running, review the code for the next phase (searching for websites on LinkedIn) to prepare for its implementation once the current processing is complete.

### Resources and Links:
- Link to the Job Sites Data Table: `[Insert Link Here]`
- Link to Google Cloud Billing/Quota Page: `[Insert Link Here]`

### Instructions:

**Process:**
- This is a production task. The main focus is on ensuring the long-running script continues to work as expected. The secondary focus is preparing for the subsequent step in the data pipeline.

**Expected Time:** All day (monitoring in the background)

**Status:** **In Progress**

---

## Task 2: Develop and Test GPT Agent for LinkedIn Follow-ups

### Steps:
1.  **Define the Logic and Goal:**
    - Target audience: Leads with whom the last contact was 6+ months ago.
    - Goal: Send a polite, non-pushy follow-up message to re-engage them.
2.  **Engineer the Prompt:**
    - Create a new document to draft the prompt.
    - Structure it with clear roles, context, and instructions for the AI. Example:
        - **Role:** "You are a friendly and professional business development assistant."
        - **Context:** "You are writing a follow-up message on LinkedIn to a person named [Lead Name] from [Company Name]. Our last conversation was over 6 months ago."
        - **Task:** "Write a short, polite, and personalized message. Mention something relevant from their profile (e.g., a recent post or job title). The goal is to gently restart the conversation. Use this template: [Your Template Here]."
3.  **Select a Test Group:**
    - Go into the CRM and filter for a small group of 30-50 leads that fit the "6+ months old" criteria.
4.  **Execute the Test:**
    - Manually (or using an agent tool) apply the prompt to each person in the test group.
    - Carefully monitor the process to ensure messages are sent correctly and to watch for any signs of blocking from LinkedIn.
5.  **Analyze Results and Handover:**
    - Verify that the messages were sent successfully.
    - If the test is successful, clean up the prompt, add clear instructions on how to use it (where to insert names, etc.), and share the final document with the lead generation team.

### Resources and Links:
- Link to CRM: `[Insert Link Here]`
- Document for Prompt Drafting: `[Create and Insert Link Here]`

### Instructions:

**Process:**
- This is an R&D task. The main challenge is creating a prompt that sounds natural and, crucially, a process that doesn't trigger LinkedIn's anti-automation defenses. The test is the most important phase.

**Expected Time:** 2-3 hours

**Status:** **To Do**

