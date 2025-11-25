## Plan Overview

This document describes the plan and structure for all work done in the `Week_3/20` folder.  
Use it as the single source of truth for what you want to achieve today, how the work is organized, and any important constraints or assumptions.

## Objectives for Day 20

Based on the work from Day 19, the main objectives for Day 20 are:

- **Objective 1**: Complete employee data analysis for November 18th and generate comprehensive reports without direct communication
  - Final result: Consolidated report combining Discord logs, CRM activity, attendance data, and Dropbox activity for all employees
  - Success criteria: Report includes all data sources, identifies anomalies, and provides actionable insights

- **Objective 2**: Create and deliver TODO files for employees for November 21st via at least 2 channels (Discord + Email)
  - Final result: Each employee has a personalized TODO.md file in their folder with tasks based on their activity analysis
  - Success criteria: Files delivered via Discord and email, employees can access and understand their tasks

- **Objective 3**: Improve and stabilize the Action Normalization pipeline for processing employee daily reports
  - Final result: Reliable pipeline that extracts verbs, objects, and actions from daily reports with consistent accuracy
  - Success criteria: Pipeline processes all daily files correctly, generates structured action data

- **Objective 4**: Fix Discord ID matching issues and improve employee statistics calculation
  - Final result: Accurate matching between Discord IDs and employee names using profile data from Dropbox
  - Success criteria: All Discord IDs matched to employees, statistics calculated correctly

## Work Breakdown

- **Phase 1 – Data Collection & Validation**: 
  - Gather all employee data files for November 18th (Discord logs, CRM exports, attendance records, daily reports)
  - Verify data completeness and identify missing sources
  - Check existing analyzers and scripts (Action Normalization, Attendance Analyzer, Merged Final Report)

- **Phase 2 – Data Analysis & Processing**: 
  - Run Action Normalization pipeline on daily reports to extract actions and objects
  - Process Discord voice logs and match IDs to employee profiles
  - Combine data from all sources into unified employee activity reports
  - Identify anomalies and patterns in employee activity

- **Phase 3 – Task Generation**: 
  - Generate personalized TODO.md files for each employee based on their activity analysis
  - Review and refine generated tasks to ensure they are actionable and appropriate
  - Prepare delivery templates for Discord and email channels

- **Phase 4 – Delivery Setup**: 
  - Set up Discord delivery mechanism (server NITN8 or direct messages)
  - Configure email delivery using tokens from Dropbox (Secret Key, creation tokens)
  - Test delivery channels to ensure employees receive their tasks

- **Phase 5 – Documentation & Cleanup**: 
  - Document any issues found during analysis
  - Update FILES.md with new files created
  - Reflect on what worked well and what needs improvement

## Constraints and Assumptions

- **Constraints**: 
  - Must work without direct communication with employees (analysis-based task generation)
  - Need to use at least 2 delivery channels (Discord minimum, email preferred)
  - Limited time for manual review of all generated tasks
  - Discord ID matching requires profile data from Dropbox (Finance/November/public or ENTITIES/TALENTS/Employees/profiles)

- **Assumptions**: 
  - All employee data for November 18th is available in Dropbox
  - Action Normalization pipeline can process daily reports with reasonable accuracy
  - Employees have access to Discord and email accounts
  - Profile files contain Discord IDs that can be matched to voice log data
  - Existing scripts and analyzers are functional but may need adjustments

## Documentation & Notes Strategy

- **`PLANNING.md`**: High-level plan, goals, phases, and constraints for Day 20.
- **`TASK.md`**: Detailed task tracking with dates, status, and notes.
- **`NOTES.md`**: Free-form notes, ideas, meeting notes, and quick thoughts during work.
- **`README.md`**: Short description of what Day 20's folder is about and how to navigate it.
- **`FILES.md`**: Overview of all files in this folder and what each is responsible for.
- **`TODO.md`**: Personal daily TODO list with priorities and action items.

## End-of-Day Reflection

At the end of the day, briefly reflect on what was done, what went well, and what should be improved next time.

- **What was completed**: _To be filled at end of day_
- **What blocked you**: _To be filled at end of day_
- **What to do next**: _To be filled at end of day_

