const fs = require('fs');
const path = require('path');

const BASE_DIR = __dirname;

// Department configurations with their task details
const departments = {
    'AI': {
        name: 'AI',
        code: 'AI',
        totalTasks: 13,
        avgAutomation: 63,
        reusability: { veryHigh: 8, high: 3, medium: 2 },
        relatedDepts: ['Ops (Library management, reporting architecture)', 'Video (Content production, transcription)', 'Sales (Customer information extraction)', 'HR (Employee data systems)']
    },
    '': {
        name: 'Content Ops',
        code: ''
        totalTasks: 1,
        avgAutomation: 50,
        reusability: { veryHigh: 1, high: 0, medium: 0 },
        relatedDepts: ['Ops (Reporting architecture, task management)', 'Design (Infographic creation, visual design)', 'Sales (Social media management)']
    },
    'DESIGN': {
        name: 'Design',
        code: 'DESIGN',
        totalTasks: 10,
        avgAutomation: 28,
        reusability: { veryHigh: 7, high: 2, medium: 1 },
        relatedDepts: ['Dev (Developer coordination, landing page implementation)', 'HR (Employee status management, data quality)', 'Ops (Project management, client relationships)']
    },
    'DEV': {
        name: 'Dev',
        code: 'DEV',
        totalTasks: 5,
        avgAutomation: 60,
        reusability: { veryHigh: 4, high: 1, medium: 0 },
        relatedDepts: ['AI (MCP integration, tool implementation)', 'Sales (Lead generation, web scraping)', 'Ops (Production infrastructure, deployment)']
    },
    'HR': {
        name: 'HR',
        code: 'HR',
        totalTasks: 6,
        avgAutomation: 52,
        reusability: { veryHigh: 2, high: 4, medium: 0 },
        relatedDepts: ['AI (Tool-calling automation, employee data structure)', 'LG (Technical documentation, onboarding guides)', 'Ops (Process automation, employee management)']
    },
    'LG': {
        name: 'LG',
        code: 'LG',
        totalTasks: 3,
        avgAutomation: 27,
        reusability: { veryHigh: 2, high: 1, medium: 0 },
        relatedDepts: ['AI (Video scripting, automation support)', 'HR (Onboarding processes)', 'Ops (Performance tracking, reporting)']
    },
    'OPS': {
        name: 'Ops',
        code: 'OPS',
        totalTasks: 7,
        avgAutomation: 58,
        reusability: { veryHigh: 6, high: 1, medium: 0 },
        relatedDepts: ['AI (Task extraction, automation development)', 'Admin (Transcript processing, daily operations)', 'All departments (Reporting, task management, library usage)']
    },
    'SALES': {
        name: 'Sales',
        code: 'SALES',
        totalTasks: 4,
        avgAutomation: 48,
        reusability: { veryHigh: 2, high: 2, medium: 0 },
        relatedDepts: ['Dev (Web scraping, automation development)', 'AI (NLP analysis, lead qualification)', 'Ops (CRM integration, workflow optimization)']
    },
    'VIDEO': {
        name: 'Video',
        code: 'VIDEO',
        totalTasks: 4,
        avgAutomation: 60,
        reusability: { veryHigh: 2, high: 1, medium: 1 },
        relatedDepts: ['AI (Content scripting, AI video generation)', 'Content Ops (Multi-platform content strategy)', 'HR (Employee status management)', 'Design (Visual content creation)']
    }
};

// Read task files from directory
function getTaskFiles(deptCode) {
    const taskDir = path.join(BASE_DIR, 'Task_Templates', deptCode);
    const files = fs.readdirSync(taskDir).filter(f => f.startsWith('TASK-') && f.endsWith('.md'));

    return files.map(file => {
        const content = fs.readFileSync(path.join(taskDir, file), 'utf8');
        const taskId = file.replace('.md', '');
        const nameMatch = content.match(/# ([^:]+):\s*(.+)/);
        const taskName = nameMatch ? nameMatch[2].trim() : '';
        const automationMatch = content.match(/\*\*Automation Potential:\*\*\s*(.+)/);
        const automation = automationMatch ? automationMatch[1].trim() : '';
        const reusabilityMatch = content.match(/\*\*Reusability:\*\*\s*(.+)/);
        const reusability = reusabilityMatch ? reusabilityMatch[1].trim() : '';

        return { taskId, taskName, automation, reusability };
    }).sort((a, b) => a.taskId.localeCompare(b.taskId));
}

// Generate department file content
function generateDepartmentFile(deptCode, deptInfo) {
    const tasks = getTaskFiles(deptCode);

    // Build task list table
    const taskRows = tasks.map(task =>
        `| ${task.taskId} | ${task.taskName} | ${task.automation} | ${task.reusability} | [View Template](./Task_Templates/${deptCode}/${task.taskId}.md) |`
    ).join('\n');

    // Get top 3 most automated tasks
    const sortedByAutomation = [...tasks].sort((a, b) => {
        const getAutomationValue = (str) => {
            if (str.includes('>80')) return 90;
            if (str.includes('60-80')) return 70;
            if (str.includes('40-60')) return 50;
            return 30;
        };
        return getAutomationValue(b.automation) - getAutomationValue(a.automation);
    });

    const topAutomated = sortedByAutomation.slice(0, 3).map((task, i) =>
        `${i + 1}. [${task.taskName}](./Task_Templates/${deptCode}/${task.taskId}.md) - ${task.automation}`
    ).join('\n');

    // Get top 3 most frequently used (by reusability)
    const sortedByReusability = [...tasks].sort((a, b) => {
        const getReusabilityValue = (str) => {
            if (str.includes('Very High')) return 3;
            if (str.includes('High')) return 2;
            return 1;
        };
        return getReusabilityValue(b.reusability) - getReusabilityValue(a.reusability);
    });

    const mostUsed = sortedByReusability.slice(0, 3).map((task, i) =>
        `${i + 1}. [${task.taskName}](./Task_Templates/${deptCode}/${task.taskId}.md) - ${task.reusability}`
    ).join('\n');

    const relatedDeptsList = deptInfo.relatedDepts.map(d => `- ${d}`).join('\n');

    return `# ${deptInfo.name} Task Templates
**Department:** ${deptInfo.name}
**Department Code:** ${deptCode}
**Total Tasks:** ${deptInfo.totalTasks}
**Date:** 2025-11-10
**Source:** Consolidated from all extraction phases

---

## Task List

| ID | Task Name | Automation | Reusability | Template File |
|----|-----------|------------|-------------|---------------|
${taskRows}

---

## Department Statistics

**Total Tasks:** ${deptInfo.totalTasks}
**Average Automation Potential:** ${deptInfo.avgAutomation}%

**Reusability Distribution:**
- Very High: ${deptInfo.reusability.veryHigh} tasks
- High: ${deptInfo.reusability.high} tasks
- Medium: ${deptInfo.reusability.medium} tasks

**Related Departments:**
${relatedDeptsList}

---

## Quick Access

**Most Automated Tasks:**
${topAutomated}

**Most Frequently Used:**
${mostUsed}

---

## Navigation

- [All Tasks Listing](./TASKS_LISTING.md)
- [Projects Listing](./PROJECTS_LISTING.md)
- [Skills Listing](./SKILLS_LISTING.md)
- [Master Index](./INDEX.md)

---

**Version:** 2.0 (Restructured)
**Last Updated:** 2025-11-10
**Organization:** Individual task files in Task_Templates/${deptCode}/ subdirectory
`;
}

// Main function
function main() {
    Object.keys(departments).forEach(deptCode => {
        const deptInfo = departments[deptCode];
        const content = generateDepartmentFile(deptCode, deptInfo);
        const filePath = path.join(BASE_DIR, `Tasks_${deptCode}.md`);

        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`Created: Tasks_${deptCode}.md`);
    });

    console.log('\n=== SUMMARY ===');
    console.log(`Total department files rewritten: ${Object.keys(departments).length}`);
}

main();
