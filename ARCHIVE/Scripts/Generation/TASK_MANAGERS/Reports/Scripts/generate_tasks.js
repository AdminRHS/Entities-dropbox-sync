const fs = require('fs');
const path = require('path');

const BASE_DIR = __dirname;

// Read and parse YAML blocks from department files
function extractYAMLBlocks(filePath) {
    const content = fs.readFileSync(filePath, 'utf8');
    const yamlPattern = /```yaml\n([\s\S]*?)```/g;
    const blocks = [];
    let match;

    while ((match = yamlPattern.exec(content)) !== null) {
        blocks.push(match[1]);
    }

    return blocks;
}

// Parse YAML content to extract metadata
function parseYAML(yaml) {
    const extractField = (pattern) => {
        const match = yaml.match(pattern);
        return match ? match[1] : '';
    };

    return {
        taskId: extractField(/template_id:\s*(\S+)/),
        taskName: extractField(/task_template_name:\s*"([^"]+)"/),
        status: extractField(/status:\s*"([^"]+)"/) || 'Active',
        reusability: extractField(/reusability_score:\s*"([^"]+)"/) || 'High',
        automation: extractField(/ranking:\s*"([^"]+)"/) || 'Medium',
        action: extractField(/action:\s*"([^"]+)"/),
        object: extractField(/object:\s*"([^"]+)"/),
        tool: extractField(/tool:\s*"([^"]+)"/),
        time: yaml.match(/estimated_time:\s*"([^"]+)"/)?.[1] || 'Variable'
    };
}

// Generate individual task file
function generateTaskFile(yaml, deptName, deptCode) {
    const info = parseYAML(yaml);

    return `# ${info.taskId}: ${info.taskName}

**Department:** ${deptName}
**Status:** ${info.status}
**Reusability:** ${info.reusability}
**Automation Potential:** ${info.automation}

---

## Quick Info

- **Action:** ${info.action}
- **Object:** ${info.object}
- **Tool:** ${info.tool}
- **Estimated Time:** ${info.time}

---

## Full Template

\`\`\`yaml
${yaml.trim()}
\`\`\`

---

## Navigation

- [Back to ${deptName} Tasks](../../Tasks_${deptCode}.md)
- [All Tasks Listing](../../TASKS_LISTING.md)
- [Master Index](../../INDEX.md)

---

**Source:** Extracted from Tasks_${deptCode}.md
**Date:** 2025-11-10
`;
}

// Process a department
function processDepartment(deptCode, deptName) {
    const deptFile = path.join(BASE_DIR, `Tasks_${deptCode}.md`);

    if (!fs.existsSync(deptFile)) {
        console.log(`Warning: ${deptFile} not found`);
        return [];
    }

    console.log(`Processing ${deptName} (${deptCode})...`);

    const yamlBlocks = extractYAMLBlocks(deptFile);
    const createdFiles = [];

    yamlBlocks.forEach(yaml => {
        try {
            const info = parseYAML(yaml);
            const content = generateTaskFile(yaml, deptName, deptCode);
            const filePath = path.join(BASE_DIR, 'Task_Templates', deptCode, `${info.taskId}.md`);

            fs.writeFileSync(filePath, content, 'utf8');
            createdFiles.push(filePath);
            console.log(`  Created: ${info.taskId}.md`);
        } catch (error) {
            console.error(`  Error creating file: ${error.message}`);
        }
    });

    return createdFiles;
}

// Main function
function main() {
    const departments = [
        ['AI', 'AI'],
        ['', 'Content Ops']
        ['DESIGN', 'Design'],
        ['DEV', 'Dev'],
        ['HR', 'HR'],
        ['LG', 'LG'],
        ['OPS', 'Ops'],
        ['SALES', 'Sales'],
        ['VIDEO', 'Video']
    ];

    let allFiles = [];

    departments.forEach(([deptCode, deptName]) => {
        const files = processDepartment(deptCode, deptName);
        allFiles = allFiles.concat(files);
        console.log(`  Total files created for ${deptName}: ${files.length}\n`);
    });

    console.log(`\n=== SUMMARY ===`);
    console.log(`Total files created: ${allFiles.length}`);
}

main();
