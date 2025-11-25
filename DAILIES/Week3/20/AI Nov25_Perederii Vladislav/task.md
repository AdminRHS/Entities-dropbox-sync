**Main Goal:** Develop and implement a two-tier Google Maps scraping system to create an enriched database of potential B2B clients. The goal is not simply to collect contacts, but to conduct a deep analysis of the local market to identify companies with clear signs of need for outstaffing resources.

**Philosophy of the Task:** We view Google Maps as a dynamic database of local businesses. Our goal is to extract from this database not only the "what" (name, website), but also the "why" (why this company might become our client). The key insight is that client reviews are a public record of a company's operational challenges and successes. By analyzing these reviews in large volumes, we can uncover hidden signals about staff shortages, quality issues, or rapid growth—all of which are triggers for approaching a client with an outstaffing proposal.

Methodology: The scraping process is divided into two stages using different tools to optimize speed and depth.

1. Phase 1: Broad, Shallow Scraping. In this stage, we use a simple and fast tool (the Instant Data Scraper browser extension) to quickly create a list of all relevant companies in a given niche and location. The goal is to quickly collect the "tip of the iceberg": company names and links to their Google Maps profiles.

2. Phase 2: Deep, Targeted Scraping. In this stage, we use a custom-developed Python script. This script takes the list of companies from Phase 1 as input and accesses the Google Maps profile for each one to collect the most valuable data set—all text and dates of all reviews. This is a slower, but much more powerful process.

**Key data for analysis:**

* **From Phase 1:** Company name, Google Maps profile link, website link.
* **From Phase 2 (Python):** Full dataset of all reviews for each company (text, date).

**Signals analyzed:**

* **Review Velocity:** Calculated based on dates. A constant influx of new reviews indicates active customer traffic and business growth.
* **Negative review topics:** AI-powered text analysis helps identify systemic issues. For example, if 15% of reviews mention "slow support" or "app bugs," this is a clear sign of a shortage of IT specialists or testers. * **Positive Review Topics:** Reviews praising "new functionality" or "rapid expansion" indicate that the company is in a phase of active growth and will likely need new talent.
* **Rating/Quantity Mismatch:** A company with thousands of reviews and an average rating of 3.5 stars is likely experiencing "growing pains"—its operational processes are struggling to keep up with the influx of clients. This is the ideal candidate.

**Expected Result:** A comprehensive Google Sheet containing not only contact information for each company collected on Google Maps, but also an AI-generated summary of its operational status, a list of key issues (derived from reviews), and an assessment of its potential as an outsourcing client. This allows the sales team to move from cold outreach to targeted, well-founded proposals. ---

### Step-by-step plan for its implementation

#### **Step 1: Preparing the technical environment**

1. **Installing Instant Data Scraper:** Install and install the Chrome extension as described in your instructions. This tool will be used for quick initial reconnaissance.

2. **Setting up the environment for the Python script:**
* **Step 2.1:** Install Python on your computer (if not already installed) from the official website `python.org`.
* **Step 2.2:** Install the necessary libraries via the terminal or command line:
```bash
pip install selenium beautifulsoup4 pandas gspread oauth2client
```
* `selenium`: for browser automation (scrolling, clicks).
* `beautifulsoup4`: for parsing the page's HTML code.
* `pandas`: for convenient data manipulation (creating tables).
* `gspread`, `oauth2client`: for directly writing data to Google Sheets.
* **Step 2.3:** Download and configure WebDriver. ChromeDriver is required for Chrome automation. Download the version that **matches your Chrome browser version**. Unzip and place the executable file `chromedriver.exe` (or `chromedriver` for Mac/Linux) in the folder with your future script or in the system directory.

3. **Configuring Google Sheets API Access:**
* Go to the Google Cloud Console and create a new project.
* Enable the "Google Drive API" and "Google Sheets API".
* Create a Service Account, generate a key in JSON format, and download the `credentials.json` file.
* Open your Google Sheet and grant access (share) to the email address of this service account (it will be specified in the `credentials.json` file).

#### **Stage 2: Phase 1 - Collecting the initial list of Companies (Instant Data Scraper)**

1. **Search on Google Maps:** Go to google.com/maps and enter a search query (e.g., 'marketing agency in London').
2. **Full list download:** Scroll to the bottom of the results sidebar to display all the companies found.
3. **Quick scraping:** Activate **Instant Data Scraper**, make sure it selects the correct table, and download the data in **CSV** format. This file will contain company names, their ratings, number of reviews, and, most importantly, links to their pages.
4. **Save:** Save the CSV file under a descriptive name, such as 'marketing_london_list.csv'. Repeat for all target niches and cities.

#### **Stage 3: Phase 2 - Writing and Running a Python Script to Collect Reviews**

1. **Script Structure:** Your Python script will perform the following actions in a loop:
* Read the CSV file obtained in Step 2 and extract from it a link to the company's Google Maps profile.
* For each link:
* Open this link using Selenium.
* Find the "Reviews" button or tab on the page and click it.
* **Automate Scrolling:** Implement a loop that will scroll the review panel down until no more reviews are loaded. This is the most important part, as by default only the first 10-20 reviews are visible.
* After all reviews have loaded, get the page's HTML.
* Pass the HTML to BeautifulSoup for parsing.
* Find all review blocks and extract the text, author name (optional), and publication date from each.
* Add the collected reviews (text and date) along with the company name to a shared data structure (e.g., a list of dictionaries in a Pandas DataFrame).
* Implement pauses (`time.sleep()`) between requests to avoid being blocked by Google.
2. **Running the Script:** Run the script from the terminal. It will open the browser, follow links, and collect data. This process may take a long time.
3. **Saving Results:** Once finished, the script should save all the collected reviews to a new CSV file (`marketing_london_reviews.csv`) or directly write them to a new tab in your Google Sheets master spreadsheet.

#### **Step 4: Analysis and Finalization**

1. **AI Analysis:** Now that you have the full dataset, use the language model API for analysis. You can do this via another Python script or via an n8n workflow that will read your feedback table.
2. **Task for AI:** For each company, send a prompt asking the AI ​​to analyze all of their feedback and identify key issues and growth opportunities.
3. **Create a final database:** Record the AI ​​findings in your master table. You now have a complete, enriched lead database.
4. **Decision Making:** Use this database for highly personalized and effective sales.



### **Task: Automate the transfer of resumes from Google Docs to Dropbox**

**Goal:** Simplify and speed up the process of transferring candidates' resumes from Google Docs to Dropbox after a successful interview.

**How ​​it should work:**

1. **Initiation:** The user opens the candidate's resume in Google Docs.
2. **Running the script:** Clicks a special button (bookmarklet) in the browser's bookmarks bar.
3. **Input:** A dialog box appears asking for the candidate's first and last name.
4. **Automated actions:**
* A script created in Google Apps Script automatically copies the open Google Doc.
* This copy is saved to a predefined folder in your Dropbox account.
* The file is named in the format "FirstName LastName - Date."
5. **Confirmation:** After the file has been successfully transferred, a success message appears on the screen.

**Key Implementation Requirements:**

* **Use Google Apps Script:** All file copying and moving logic must be implemented using this tool.
* **Launch via bookmarklet:** For ease of use and quick access, the script should be launched with a single click of a button in the browser.
* **Dynamic File Name:** It is necessary to provide the ability to enter the candidate's name, which will be used in the file name.
* **Predefined Dropbox Folder:** The path for saving files in Dropbox must be configured in advance.
* **Free Solution:** The entire process must be implemented without the use of paid services.

**Result:** As a result, you will have a simple and effective tool that allows you to transfer a resume from Google Docs to a structured Dropbox folder with a single click and the entry of a candidate's name, saving you time and eliminating routine operations.