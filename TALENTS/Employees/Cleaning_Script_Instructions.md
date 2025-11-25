# Employee Data Cleaning Script Implementation Guide

## Overview

This guide provides step-by-step instructions for implementing automated cleaning of the Employees.json file.

**Source:** `C:\Users\Dell\Dropbox\Nov25\AI Nov25\Niko AI\ExportCRMS\Employees.json`
**Target:** Create cleaned version preserving all meaningful data
**Expected Reduction:** 30-40% file size

---

## Prerequisites

### Option 1: JavaScript/Node.js
- Node.js installed (v14+ recommended)
- Basic command line knowledge

### Option 2: Python
- Python installed (3.7+ recommended)
- Basic command line knowledge

### Option 3: Manual
- Text editor with regex support (VS Code, Sublime, etc.)
- JSON validator

---

## Implementation Option 1: Node.js Script (Recommended)

### Step 1: Create the Cleaning Script

Create a file named `clean_employees.js` with the following content:

```javascript
const fs = require('fs');
const path = require('path');

// Configuration
const INPUT_FILE = 'C:\\Users\\Dell\\Dropbox\\Nov25\\AI Nov25\\Niko AI\\ExportCRMS\\Employees.json';
const OUTPUT_FILE = 'C:\\Users\\Dell\\Dropbox\\Nov25\\AI Nov25\\Niko AI\\Employees\\Employees_Cleaned.json';
const BACKUP_FILE = 'C:\\Users\\Dell\\Dropbox\\Nov25\\AI Nov25\\Niko AI\\ExportCRMS\\Employees_BACKUP.json';

console.log('🧹 Employee Data Cleaning Script');
console.log('=================================\n');

// Step 1: Create backup
console.log('📦 Creating backup...');
try {
  fs.copyFileSync(INPUT_FILE, BACKUP_FILE);
  console.log('✅ Backup created:', BACKUP_FILE);
} catch (error) {
  console.error('❌ Failed to create backup:', error.message);
  process.exit(1);
}

// Step 2: Read the file
console.log('\n📖 Reading employee data...');
let data;
try {
  const fileContent = fs.readFileSync(INPUT_FILE, 'utf8');
  data = JSON.parse(fileContent);
  console.log(`✅ Loaded ${data.data.employees.length} employees`);
} catch (error) {
  console.error('❌ Failed to read file:', error.message);
  process.exit(1);
}

// Statistics
const stats = {
  presaleIdRemoved: 0,
  emptyArraysRemoved: 0,
  nullFieldsRemoved: 0,
  emptyStringsRemoved: 0,
  duplicateStructuresRemoved: 0
};

// Step 3: Define cleaning function
function cleanObject(obj, parentKey = '', depth = 0) {
  // Handle arrays
  if (Array.isArray(obj)) {
    const cleaned = obj.map(item => cleanObject(item, parentKey, depth + 1))
                      .filter(item => item !== null && item !== undefined);

    // Return null for empty arrays (will be removed by parent)
    return cleaned.length > 0 ? cleaned : null;
  }

  // Handle objects
  if (obj !== null && typeof obj === 'object') {
    const cleaned = {};

    for (const [key, value] of Object.entries(obj)) {
      // PRIORITY 1: Always remove presale_id
      if (key === 'presale_id') {
        stats.presaleIdRemoved++;
        continue;
      }

      // PRIORITY 1: Remove duplicate structures
      if (key === 'employee_detail' && parentKey === 'user') {
        stats.duplicateStructuresRemoved++;
        continue;
      }

      // Remove hr_details if it's a duplicate (simplified - you may need more logic)
      if (key === 'hr_details') {
        // Skip - handled by keeping candidate instead
        continue;
      }

      // PRIORITY 2: Remove null values
      if (value === null) {
        stats.nullFieldsRemoved++;
        continue;
      }

      // PRIORITY 2: Remove empty strings and whitespace-only strings
      if (typeof value === 'string') {
        if (value === '') {
          stats.emptyStringsRemoved++;
          continue;
        }
        if (value.trim() === '' && key !== 'description') {
          stats.emptyStringsRemoved++;
          continue;
        }
      }

      // PRIORITY 2: Remove empty arrays
      if (Array.isArray(value) && value.length === 0) {
        stats.emptyArraysRemoved++;
        continue;
      }

      // Recursively clean nested structures
      const cleanedValue = cleanObject(value, key, depth + 1);

      // Only add if the cleaned value is not null/undefined
      if (cleanedValue !== null && cleanedValue !== undefined) {
        // For arrays, don't add if empty after cleaning
        if (Array.isArray(cleanedValue) && cleanedValue.length === 0) {
          stats.emptyArraysRemoved++;
          continue;
        }

        cleaned[key] = cleanedValue;
      } else {
        stats.nullFieldsRemoved++;
      }
    }

    return Object.keys(cleaned).length > 0 ? cleaned : null;
  }

  // Return primitive values as-is
  return obj;
}

// Step 4: Clean the data
console.log('\n🧹 Cleaning employee data...');
const originalSize = JSON.stringify(data).length;

data.data.employees = data.data.employees.map(emp => cleanObject(emp, 'employee'))
                                          .filter(emp => emp !== null);

const cleanedSize = JSON.stringify(data).length;

// Step 5: Write cleaned data
console.log('\n💾 Writing cleaned data...');
try {
  fs.writeFileSync(OUTPUT_FILE, JSON.stringify(data, null, 2), 'utf8');
  console.log('✅ Cleaned file saved:', OUTPUT_FILE);
} catch (error) {
  console.error('❌ Failed to write file:', error.message);
  process.exit(1);
}

// Step 6: Display statistics
console.log('\n📊 Cleaning Statistics');
console.log('=====================');
console.log(`presale_id fields removed:    ${stats.presaleIdRemoved.toLocaleString()}`);
console.log(`Empty arrays removed:         ${stats.emptyArraysRemoved.toLocaleString()}`);
console.log(`Null fields removed:          ${stats.nullFieldsRemoved.toLocaleString()}`);
console.log(`Empty strings removed:        ${stats.emptyStringsRemoved.toLocaleString()}`);
console.log(`Duplicate structures removed: ${stats.duplicateStructuresRemoved.toLocaleString()}`);
console.log(`\nTotal employees: ${data.data.employees.length}`);
console.log(`Original size:   ${(originalSize / 1024 / 1024).toFixed(2)} MB`);
console.log(`Cleaned size:    ${(cleanedSize / 1024 / 1024).toFixed(2)} MB`);
console.log(`Reduction:       ${((1 - cleanedSize / originalSize) * 100).toFixed(1)}%`);

console.log('\n✅ Cleaning complete!');
console.log(`📁 Cleaned file: ${OUTPUT_FILE}`);
console.log(`📦 Backup file:  ${BACKUP_FILE}`);
```

### Step 2: Run the Script

```bash
# Navigate to the script directory
cd "C:\Users\Dell\Dropbox\Nov25\AI Nov25\Niko AI\Employees"

# Run the script
node clean_employees.js
```

### Step 3: Verify the Output

The script will display statistics showing:
- Number of fields removed by category
- File size before and after
- Percentage reduction

---

## Implementation Option 2: Python Script

### Step 1: Create the Cleaning Script

Create a file named `clean_employees.py`:

```python
#!/usr/bin/env python3
import json
import shutil
from pathlib import Path

# Configuration
INPUT_FILE = r'C:\Users\Dell\Dropbox\Nov25\AI Nov25\Niko AI\ExportCRMS\Employees.json'
OUTPUT_FILE = r'C:\Users\Dell\Dropbox\Nov25\AI Nov25\Niko AI\Employees\Employees_Cleaned.json'
BACKUP_FILE = r'C:\Users\Dell\Dropbox\Nov25\AI Nov25\Niko AI\ExportCRMS\Employees_BACKUP.json'

print('🧹 Employee Data Cleaning Script')
print('=' * 40)
print()

# Statistics
stats = {
    'presale_id_removed': 0,
    'empty_arrays_removed': 0,
    'null_fields_removed': 0,
    'empty_strings_removed': 0,
    'duplicate_structures_removed': 0
}

# Step 1: Create backup
print('📦 Creating backup...')
try:
    shutil.copy2(INPUT_FILE, BACKUP_FILE)
    print(f'✅ Backup created: {BACKUP_FILE}')
except Exception as e:
    print(f'❌ Failed to create backup: {e}')
    exit(1)

# Step 2: Read the file
print('\n📖 Reading employee data...')
try:
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f'✅ Loaded {len(data["data"]["employees"])} employees')
except Exception as e:
    print(f'❌ Failed to read file: {e}')
    exit(1)

# Step 3: Define cleaning function
def clean_object(obj, parent_key='', depth=0):
    """Recursively clean object by removing null, empty, and unwanted fields"""

    # Handle lists
    if isinstance(obj, list):
        cleaned = []
        for item in obj:
            cleaned_item = clean_object(item, parent_key, depth + 1)
            if cleaned_item is not None:
                cleaned.append(cleaned_item)

        # Return None for empty lists (will be removed by parent)
        return cleaned if len(cleaned) > 0 else None

    # Handle dictionaries
    if isinstance(obj, dict):
        cleaned = {}

        for key, value in obj.items():
            # PRIORITY 1: Always remove presale_id
            if key == 'presale_id':
                stats['presale_id_removed'] += 1
                continue

            # PRIORITY 1: Remove duplicate structures
            if key == 'employee_detail' and parent_key == 'user':
                stats['duplicate_structures_removed'] += 1
                continue

            # Remove hr_details (assuming candidate exists)
            if key == 'hr_details':
                continue

            # PRIORITY 2: Remove null values
            if value is None:
                stats['null_fields_removed'] += 1
                continue

            # PRIORITY 2: Remove empty strings and whitespace-only strings
            if isinstance(value, str):
                if value == '':
                    stats['empty_strings_removed'] += 1
                    continue
                if value.strip() == '' and key != 'description':
                    stats['empty_strings_removed'] += 1
                    continue

            # PRIORITY 2: Remove empty lists
            if isinstance(value, list) and len(value) == 0:
                stats['empty_arrays_removed'] += 1
                continue

            # Recursively clean
            cleaned_value = clean_object(value, key, depth + 1)

            # Only add if cleaned value is not None
            if cleaned_value is not None:
                # For lists, don't add if empty after cleaning
                if isinstance(cleaned_value, list) and len(cleaned_value) == 0:
                    stats['empty_arrays_removed'] += 1
                    continue

                cleaned[key] = cleaned_value
            else:
                stats['null_fields_removed'] += 1

        return cleaned if len(cleaned) > 0 else None

    # Return primitive values as-is
    return obj

# Step 4: Clean the data
print('\n🧹 Cleaning employee data...')
original_json = json.dumps(data)
original_size = len(original_json)

cleaned_employees = []
for emp in data['data']['employees']:
    cleaned_emp = clean_object(emp, 'employee')
    if cleaned_emp is not None:
        cleaned_employees.append(cleaned_emp)

data['data']['employees'] = cleaned_employees

cleaned_json = json.dumps(data)
cleaned_size = len(cleaned_json)

# Step 5: Write cleaned data
print('\n💾 Writing cleaned data...')
try:
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f'✅ Cleaned file saved: {OUTPUT_FILE}')
except Exception as e:
    print(f'❌ Failed to write file: {e}')
    exit(1)

# Step 6: Display statistics
print('\n📊 Cleaning Statistics')
print('=' * 40)
print(f"presale_id fields removed:    {stats['presale_id_removed']:,}")
print(f"Empty arrays removed:         {stats['empty_arrays_removed']:,}")
print(f"Null fields removed:          {stats['null_fields_removed']:,}")
print(f"Empty strings removed:        {stats['empty_strings_removed']:,}")
print(f"Duplicate structures removed: {stats['duplicate_structures_removed']:,}")
print(f"\nTotal employees: {len(data['data']['employees'])}")
print(f"Original size:   {original_size / 1024 / 1024:.2f} MB")
print(f"Cleaned size:    {cleaned_size / 1024 / 1024:.2f} MB")
print(f"Reduction:       {(1 - cleaned_size / original_size) * 100:.1f}%")

print('\n✅ Cleaning complete!')
print(f'📁 Cleaned file: {OUTPUT_FILE}')
print(f'📦 Backup file:  {BACKUP_FILE}')
```

### Step 2: Run the Script

```bash
# Navigate to the script directory
cd "C:\Users\Dell\Dropbox\Nov25\AI Nov25\Niko AI\Employees"

# Run the script
python clean_employees.py
```

---

## Implementation Option 3: Manual Cleaning with Text Editor

### Step 1: Create Backup

1. Copy `Employees.json`
2. Rename copy to `Employees_BACKUP.json`

### Step 2: Open in Text Editor

Use VS Code or similar editor with regex support.

### Step 3: Find & Replace (Regex Mode)

**⚠️ WARNING:** Test on a small section first! These regex patterns need careful testing.

#### Remove presale_id fields:

**Find:** `"presale_id":\s*null,?\s*\n`
**Replace:** (empty)

Run this multiple times until no matches found.

#### Remove empty arrays:

**Find:** `"(\w+)":\s*\[\],?\s*\n`
**Replace:** (empty)

#### Remove null fields:

**Find:** `"(\w+)":\s*null,?\s*\n`
**Replace:** (empty)

**Note:** This is aggressive - be careful with fields that should be preserved even if null.

#### Remove empty strings:

**Find:** `"(\w+)":\s*"",?\s*\n`
**Replace:** (empty)

### Step 4: Fix Trailing Commas

After removing fields, you'll have trailing commas before closing braces/brackets.

**Find:** `,(\s*[}\]])`
**Replace:** `$1`

### Step 5: Validate JSON

Use a JSON validator:
- Online: jsonlint.com
- VS Code: Built-in JSON validation
- Command line: `node -e "JSON.parse(require('fs').readFileSync('Employees_Cleaned.json'))"`

---

## Validation Checklist

After cleaning, verify the following:

### 1. Employee Count
```bash
# Node.js
node -e "console.log(JSON.parse(require('fs').readFileSync('Employees_Cleaned.json')).data.employees.length)"

# Python
python -c "import json; print(len(json.load(open('Employees_Cleaned.json'))['data']['employees']))"
```

**Expected:** 224 employees

### 2. Required Fields Present

Manually check a few employees to ensure they still have:
- `id`, `company_id`, `user_id`, `employee_id`
- `name_eng`, `name_ua`
- `user` object with `id`, `email`, `name`
- `department`, `position`, `designation` objects

### 3. JSON Validity

The file should parse without errors.

### 4. Spot Check Data Integrity

Open both original and cleaned files, compare 2-3 random employees:
- Ensure no meaningful data was lost
- Only null/empty values should be removed

### 5. File Size Reduction

Check file sizes:

```bash
# Windows PowerShell
dir "Employees.json","Employees_Cleaned.json" | Select-Object Name,Length
```

**Expected:** 30-40% reduction

---

## Advanced: Custom Cleaning Rules

If you need more specific cleaning rules, modify the script:

### Example 1: Keep Certain Null Fields

```javascript
// In the cleanObject function, add exceptions:
const KEEP_NULL_FIELDS = ['last_date', 'end_date', 'reason_dismissal'];

if (value === null) {
  if (!KEEP_NULL_FIELDS.includes(key)) {
    stats.nullFieldsRemoved++;
    continue;
  }
}
```

### Example 2: Remove Test Data

```javascript
// Before cleaning, filter out test records:
data.data.employees = data.data.employees.filter(emp => {
  // Remove gibberish names
  if (emp.name_eng && /[а-я]{3,}/.test(emp.name_eng)) {
    return false;
  }
  return true;
});
```

### Example 3: Normalize String Booleans

```javascript
function normalizeBoolean(value) {
  if (value === '0') return false;
  if (value === '1') return true;
  return value;
}

// Apply during cleaning:
if (BOOLEAN_FIELDS.includes(key)) {
  cleaned[key] = normalizeBoolean(cleanedValue);
} else {
  cleaned[key] = cleanedValue;
}
```

---

## Troubleshooting

### Error: "Unexpected end of JSON input"

**Problem:** Original file is corrupted or incomplete.
**Solution:** Verify the original file is valid JSON first.

### Error: File size didn't reduce much

**Problem:** Cleaning rules may be too conservative.
**Solution:** Check stats output - verify fields are actually being removed.

### Error: Employees missing after cleaning

**Problem:** Aggressive cleaning removed entire employee records.
**Solution:** Review the cleaning logic - may need to be less strict.

### Error: Application can't read cleaned file

**Problem:** Application expects certain fields to exist even if null.
**Solution:** Add exceptions for fields the application requires.

---

## Post-Cleaning Steps

### 1. Test with Application

Load the cleaned file in your application and test:
- Can all employees be viewed?
- Are all features working?
- No unexpected errors?

### 2. Performance Testing

Compare performance:
- Load time for original vs cleaned
- Query performance
- Memory usage

### 3. Deploy

If everything works:
1. Keep backup of original
2. Replace original with cleaned version
3. Update any documentation

### 4. Monitor

Watch for:
- Any missing data reports
- Application errors
- Performance improvements

---

## Best Practices

1. **Always Backup:** Never clean the only copy of data
2. **Test First:** Run on a subset before full dataset
3. **Validate After:** Always verify cleaned data is valid and complete
4. **Document Changes:** Note what was cleaned and why
5. **Keep Original:** Don't delete the original file for at least 30 days
6. **Review Stats:** Check cleaning statistics to ensure expected results
7. **Spot Check:** Manually review random samples before and after

---

## Next Steps

After successfully cleaning the employee data:

1. **Review** the `Fields_To_Remove.json` for complete field list
2. **Execute** your chosen cleaning method
3. **Validate** the results using the checklist
4. **Test** with your application
5. **Document** any issues or additional cleaning needed

For questions or issues, refer to:
- `Cleaning_Prompt.md` - Detailed cleaning instructions
- `Employee_Unit_Template.json` - Data structure reference
- `Fields_To_Remove.json` - Complete field list

---

## Summary

| Method | Difficulty | Speed | Accuracy | Recommended For |
|--------|-----------|-------|----------|-----------------|
| Node.js Script | Medium | Fast | High | Developers, Automated cleaning |
| Python Script | Medium | Fast | High | Python users, Data scientists |
| Manual/Regex | High | Slow | Medium | One-time cleanup, Small changes |

**Recommended:** Use the Node.js or Python script for consistent, repeatable, and safe cleaning.
