# LIBRARIES Migration Policy

**Created:** 2025-12-26  
**Purpose:** Document the migration policy for LIBRARIES folder structure

---

## Core Principle

**Only root folders are renamed to `LBS_XXX_Name` format. Internal folder structure remains unchanged.**

---

## Migration Rules

### ✅ What Changes

**Root Folder Names:**
- `Tools/` → `LBS_003_Tools/`
- `Skills/` → `../TALENTS/Skills/`
- `Professions/` → `LBS_005_Professions/`
- `DEPARTMENTS/` → `LBS_006_Departments/`
- `Responsibilities/Actions/` → `Responsibilities/Actions/`
- `Responsibilities/Objects/` → `Responsibilities/Objects/`
- `Responsibilities/Parameters/` → `Responsibilities/Parameters/`
- `Taxonomy/` → `Taxonomy/`
- `Archive/` → `Archive/`

### ❌ What Does NOT Change

**Internal Folder Structure:**
- `LBS_003_Tools/AI_Tools/` - **Keep as-is** (NOT `By_Category/AI/`)
- `LBS_003_Tools/Development_Tools/` - **Keep as-is** (NOT `By_Category/Development/`)
- `LBS_003_Tools/Social_Media_Platforms/` - **Keep as-is** (NOT `By_Category/Social_Media/`)
- `../TALENTS/Skills/Master/` - **Keep as-is**
- `../TALENTS/Skills/By_Department/` - **Keep as-is**
- `LBS_005_Professions/Individual/` - **Keep as-is** (if exists)
- All other internal subfolders - **Keep original names**

---

## Examples

### ✅ Correct Structure

```
LIBRARIES/
├── LBS_003_Tools/              # Root renamed
│   ├── AI_Tools/               # Internal: original name kept
│   ├── Development_Tools/       # Internal: original name kept
│   └── Social_Media_Platforms/ # Internal: original name kept
├── ../TALENTS/Skills/             # Root renamed
│   ├── Master/                 # Internal: original name kept
│   └── By_Department/          # Internal: original name kept
└── LBS_005_Professions/        # Root renamed
    ├── Master/                 # Internal: original name kept
    └── Individual/              # Internal: original name kept
```

### ❌ Incorrect Structure (DO NOT DO THIS)

```
LIBRARIES/
├── LBS_003_Tools/
│   └── By_Category/            # ❌ Don't reorganize internal structure
│       ├── AI/
│       └── Development/
```

---

## Path Reference Updates

When updating path references in files:

**Update root paths:**
- `LIBRARIES/Tools/` → `LIBRARIES/LBS_003_Tools/`
- `Tools/AI_Tools/` → `LBS_003_Tools/AI_Tools/` (root changes, internal stays same)

**Do NOT reorganize:**
- `Tools/AI_Tools/` → `LBS_003_Tools/By_Category/AI/` ❌

---

## Rationale

1. **Minimal Disruption:** Only root folder names change, reducing migration complexity
2. **Familiar Structure:** Users see familiar folder names when navigating inside
3. **Easier Maintenance:** Less reorganization means fewer broken references
4. **Clear Separation:** Root-level naming provides organization without changing working structure

---

**Last Updated:** 2025-12-26


