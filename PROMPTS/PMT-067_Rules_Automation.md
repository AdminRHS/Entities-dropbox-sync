We need to automate the process of collecting and splitting relevat data within company document system. 
The plan will be next:
1. User will record his activity in daily.md files, like 'Dropbox/Nov25/AI/Artemchuk Nikolay/06/daily.md'
2. After saving new info in daily file, script must automaticly process daily activity using last version of main prompt file - 'Dropbox/MAIN PROMPT v3.md
3. After processing daily activity, system must automaticaly fill users plans.md and task.md files inside users folder. For example:
'Dropbox/Nov25/AI/Artemchuk Nikolay/06/plans.md'
'Dropbox/Nov25/AI/Artemchuk Nikolay/06/task.md'
4. Also must work the automation rule 'Dropbox/.cursor/rules/prompt-saving-rules.mdc' that will collect users prompting activity and save his work to department log file? for example 'Dropbox/Nov25/AI/AI prompt log.md'
5. And we need to create automation script that will process department tasks file, for example 'Dropbox/Nov25/AI/AI Department Tasks - November 2025.md', and split that tasks between relevant users that are mentioned as **Owner:**, to users tasks for next days, for example 'Dropbox/Nov25/AI/Artemchuk Nikolay/06/task.md'