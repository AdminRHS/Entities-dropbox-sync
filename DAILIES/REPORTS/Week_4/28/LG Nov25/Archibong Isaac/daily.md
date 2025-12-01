# Daily Log - [29.11.2025]



### **Session 1: Managing the Lead Calendar** (10am)
**Topic:** Instructions on booking calls via the "Lead Calendar" and syncing them with the internal system.

*   **Time Zone Management:** When accessing the Lead Calendar, the time zones (e.g., Eastern European Time/Kyiv) are automatically converted. You do not need to manually calculate the time difference; simply select an available slot (e.g., 10:30 AM).
*   **Syncing Calendars:** Bookings made on the Lead Calendar **do not** automatically sync to our internal (LG) calendar. After booking a call on the Lead Calendar, you must manually add the entry to the LG calendar.
*   **Data Entry:**
    *   When adding the event to the internal calendar, copy all relevant information (Company info, Lead info) from LinkedIn.
    *   **Exception:** You do not need to input the Sales or Lead email addresses in the internal calendar entry, as those are already captured in the Lead Calendar system.
*   **Communication:** Once the call is booked, notify the Sales Department (specifically Anastasia) so they can review and accept the calendar invitation.

***

### **Session 2: Project Remess & AI Graphic Generation** (12pm)
**Topic:** Introduction to the "Remess" hiring project, brand guidelines (Cat Mascot), and using ChatGPT to generate social media graphics.

**1. Brand Overview**
*   **Project:** Remess (a hiring platform).
*   **Visual Identity:** Specific color palette featuring a **Cat Mascot**. This mascot appears across the website and social media (Instagram/LinkedIn).
*   **Deliverables:** You will be creating social media graphics. Unlike previous posts that promoted specific job vacancies, these posts will focus on broader content, such as "Tools for Remote Employees" or "Work-from-Home Experiences."

**2. Technical Specifications**
*   **Platform:** LinkedIn.
*   **Format:** Square (1080 x 1080 pixels).
*   **Tools:** ChatGPT (specifically using the "Projects" feature).

**3. Setup Instructions**
*   **File Access:** Access the "Remess" folder on Google Drive. Inside, locate the `Social Media` subfolder containing:
    *   `Mascot Prompts` (Reference images of the cat).
    *   `UI Kit & Design Guidelines` (Fonts, colors).
    *   `Post References` (Examples of previous work).
*   **ChatGPT Project Setup:**
    1.  Create a new Project in ChatGPT (e.g., named "Remess Graphics").
    2.  **Crucial:** Enable "Project Memory."
    3.  Upload the **Master Prompt File** and **Mascot Reference Images** to the project knowledge base. This ensures the AI remembers the brand style.

**4. Generating Images**
*   **Prompting:** Use the "Universal Option" prompt found in the instructions. Do not worry about specific placeholders unless the post is about a specific vacancy.
*   **Workflow:**
    *   Feed the post content/text to ChatGPT.
    *   Ask it to generate the graphic title and concept.
    *   Request the image generation using the uploaded design constraints.
*   **Quality Control:** If the generated cat looks different from the mascot (e.g., wrong eyes, wrong style), explicitly remind the AI: *"Please review the uploaded mascot references and regenerate."* You can also ask for specific edits, such as *"Add a world map to the background."*

***

### **Session 3: VS Code & Daily Reporting Support** (with Dama _4pm)
**Topic:** Troubleshooting VS Code, setting up the "Codecs" extension, and automating daily reports.

**Q: Is there a specific template for the daily plans and tasks files?**
**A:** Yes. You can find the template in the `Week 1` > `Folder 05` > `Daily` folder. You can simply copy and paste this structure into your new daily file.

**Q: How do I use AI to fill out these reports automatically?**
**A:** You can use the Claude AI integration within VS Code.
1.  Open the folder containing the previous day's report.
2.  Instruct the AI: *"Please fill out the file for today (Folder 28) using the same structure as the file in Folder 05."*
3.  Ensure you provide the correct file path so the AI can locate the reference file.

**Q: I'm getting an error telling me to "Open in Legacy Account." How do I fix this?**
**A:** This is likely an extension issue.
1.  Go to the **Extensions** tab in VS Code (left sidebar).
2.  Search for **"Codecs"**.
3.  Install the first result.
4.  Once installed, try running the prompt again.