Creation of file that will include the information about project employees (iDs, names, rate that they work for the project, start date and possible end date. Also ID and name of the client)


Creating a new month Google Sheet named December 2025-processing:

1. Go to Google Sheets, named November 2025, file, make a copy, named it December 2025. Folder the same as the previous months and checkbox "Share it with the same people" and push "Make a copy." 
2. In the created file, first of all, need to check if all the tabs are necessary. I mean, some tabs are adding only to the specific months and not obligatory to be created in all months, but there are a lot of tabs that are typically the same for all the months. 
3. Make edits to all the data that already known such as people who left or fired in the previous month. They should be removed from the December file. 
4. Also in tab "Months" we need to check if any project is already finished or it will be finished by the 1st of December. So we need to remove such a project from December file. So the data should be actual as of the 1st of December 
5. For those projects with a finish date that we are not already sure about, we need to check it with a different color just to take it into control and make edits as soon as we get some new information about it. 
6. Correct the data in the tab "Any Employee". That is the tab concerning those employees that were started after April 28. And this is the tab about our investments in these employees. We need to check if all the data is correct and actual. Check all formulas because it comes with import range from previous months so just check if all data is up to date. 
7. Concerning the currencies as a rule we estimate the exchange rate as of the first of the actual month. So we need to control it and on the 1st of December we will need to check if the exchange rate is correct or we should edit it. 
8. Check all the active companies. Remove from tab agreements those companies that and their collaboration in previous months.
9. Go to the Google sheet document called "Balance Full". Then go to the tab "Clients Revenue All". There is all our clients and the collaboration. We need to add new months data for those purposes. At one column for new months, add a new column left. Insert one column left. Name it with the name of needed months in our case it would be December 25. Then we need to fill all the data with the formulas. It describes how much revenue we receive from each company for the current month.
10. Then do the same thing for tab Client Profit All. This tab shows how much profit we get from each company that equals revenue from this company minus salary of the employee that works for this project.
11. Then come back to the monthly for December and check the formulas in tab "Agreements" where we can see clients' revenue, clients' profit, and total clients' revenue and total clients' profit that are all calculated with the help of formulas And comes from the document balance full.
12. Then move to tab Payments. Here we have a list of all active or inactive clients that should pay us. It consists of payments for current months and also from those payments that were issued for previous month services but still unpaid in current months.
13. Then go to the Transactions tab. It shows our balances in all our banking accounts. Depend on currencies. It consists of:
- Initial balance (that could be final balance from the previous months)
- Income
- Exchange expenses
- Salaries
- Final balance
That is all counted with formulas. If money is coming to our banking accounts, it displayed here in this tab.
14. Move to tab Balance. Here we have all financial indicators for current months. We need to change formulas and in this way it would be strictly according to the current months, not previous one.
15. Expenses tab is for counting all the expenses of our company for different categories. It consists of software, AI tools, taxes, advertisements, founder salaries, extra costs, bonuses, etc. We need to count here only those expenses which were made in the current month.


Create an automation in n8n project. 

This will be the project that will take by schedule the tab from Google Sheets concerning the employees of our company with their employee ID, employee name, status, rate, department, profession, position, and may be start date. This will be the input. The main challenge is to take only specific columns not the whole sheet. I will try to make these automations to take specific columns from the sheet, process it to output a file and then upload this output file into the folder at Dropbox.

1. Go to n8n under Niko account. Move to personal tab. Click on FIN folder. It shows workflows that exist here. Click "Create workflow." 
2. Click at first step. We need to choose which will be the trigger for this workflow. We will need the trigger on a schedule. Tap on it.

In parameters we need to choose Trigger rules. Trigger interval. We will need to choose for example hours. Let it be 4 hours for example. Set it.

When everything is set just click somewhere on the page to save it. Well done! First step is completed! We now have scheduled trigger! 
3. Now we need to set the second step. Click at the plus near our first step and select what we want to do. Here would be the second step that will be Google Sheets. We need to choose Google Sheets from the list and now we need to choose actions that will be required. There are a lot of actions and we need to choose which one is suitable for our situation and for our task.

Document action sheet within document actions. We need to get rows in sheet. Then choose the settings credential to connect with. We have this it's fin Google Sheets Niko. Then we will need a resource.

Here we need to change a sheet within document operation get rows. Document will be by ID. Select the ID of document needed. Paste it here. Then we need to choose which sheet we need. Choose from list and then just choose the needed tab in our case it's Employees tab. 
4. Next step will be edit fields set to modify add or remove data. There are two options:
- Manual mapping
- JSON menu mapping
Edit item fields one-by-one or JSON customize item output with JSON. Let's choose option manual mapping and try it. For this step we need to execute previous nodes to use input that data. Click "Execute previous notes" and as we have the data from the Google Sheets that we chose previously, what we need is:
- Column 1: Employee ID 
- Column 2: Employee Name
- Column 3: Status
- Column 4: Rate
- Column 5: Department
- Column 6: Profession
- Column 7: Position
- Column 15: Start date
- Column 29: Shift
save it and click "Execute step". Here we go! We have employee ID, employee name, status, rate, department, profession, position, start date, and shift.
5. Step 4: Code Node (Function)
In this step, use the Function node to convert your selected columns into a markdown-formatted table.

Set the mode to Run Once for All Items.

Paste the following JavaScript in the code section to format your Google Sheets data as a markdown table:

javascript
const headers = [
  "Employee ID", 
  "Employee Name", 
  "Status", 
  "Rate", 
  "Department", 
  "Profession", 
  "Position", 
  "Start date", 
  "Shift"
];

const keys = [
  "col_1", 
  "col_2", 
  "col_3", 
  "col_4", 
  "col_5", 
  "col_6", 
  "col_7", 
  "col_15", 
  "col_29"
];

let md = '| ' + headers.join(' | ') + ' |\n';
md += '| ' + headers.map(() => '---').join(' | ') + ' |\n';

let dataItems = $input.all();
const isHeaderRow = keys.every((key, idx) => {
  const val = dataItems[0]?.json[key]?.toString().trim().toLowerCase();
  return val === headers[idx].toLowerCase();
});
if (isHeaderRow) {
  dataItems = dataItems.slice(1);
}
for (const item of dataItems) {
  md += '| ' + keys.map(key => (item.json[key] ?? '')).join(' | ') + ' |\n';
}

return [{ markdownText: md }];
The output will be a single field called markdownText containing your table as markdown text.​

6. Step 5: Convert to File
This step saves the markdown data as a .md file.

Add the Convert to File node.

In Text Input Field, enter: markdownText

Set the output file name (for example, Employees_Public_Nov25.md).

The output will be a binary markdown file ready for export.​

7. Step 6: Dropbox Upload
To automatically upload your markdown file to Dropbox:

Add a Dropbox node.

Set the operation type to Upload File.

In the File Content field, select the output of your previous node (the binary markdown file).

Specify the Dropbox path where the file should be saved (e.g., /Public/Employees_Public_Nov25.md).

After executing these steps, your processed and formatted data from Google Sheets is saved as a markdown file and published to Dropbox automatically.

