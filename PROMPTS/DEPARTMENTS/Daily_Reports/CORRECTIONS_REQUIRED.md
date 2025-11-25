# Daily Reports v2.0 - Corrections Required

**Date:** 2025-11-19
**Status:** Pending Application

---

## Global Find & Replace Operations

### 1. Step Template Code Correction
```
Find: STP-###
Replace: STT-###

Find: STP (Step Template)
Replace: STT (Step Template)

Find: Step-Template-###
Replace: STT-###
```

### 2. Entity Format to Token-Efficient Pattern

**Projects:**
```
Find: PRT-001: AI Tutorial Research to Taxonomy Integration
Replace: PRT-001_AI_Tutorial_Research

Find: PRT-003: HR Automation Implementation
Replace: PRT-003_HR_Automation

Find: PRT-007: System Analysis
Replace: PRT-007_System_Analysis
```

**Milestones:**
```
Find: MLT-001: Content Analysis
Replace: MLT-001_Content_Analysis

Find: MLT-002: Data Inventory
Replace: MLT-002_Data_Inventory

Find: MLT-010: CV Screening Setup
Replace: MLT-010_CV_Screening_Setup
```

**Tasks:**
```
Find: TST-015: Extract Taxonomy from Tutorial Videos
Replace: TST-015_Extract_Taxonomy_Tutorial_Videos

Find: TST-055: Process Department Task Files
Replace: TST-055_Process_Department_Task_Files

Find: TST-058: Extract Tasks from Daily Files
Replace: TST-058_Extract_Tasks_Daily_Files
```

**Steps:**
```
Find: STP-155: Conduct Client Brand Discovery Session
Replace: STT-155_Conduct_Client_Brand_Discovery

Find: STP-201: Review Code Pull Request
Replace: STT-201_Review_Code_Pull_Request
```

### 3. CSV Path Corrections
```
Find: TASK_MANAGERS/DATA/Projects_Master.csv
Replace: TASK_MANAGERS/Project_Templates/Project_Templates_Master_List.csv

Find: TASK_MANAGERS/DATA/Milestones_Master.csv
Replace: TASK_MANAGERS/Milestone_Templates/Milestone_Templates_Master_List.csv

Find: TASK_MANAGERS/DATA/Tasks_Master.csv
Replace: TASK_MANAGERS/Task_Templates/Task_Templates_Master_List.csv
```

### 4. Remove Deprecated Department
```
Find: SMM, MKT,
Replace: SMM,

Find: MKT,
Replace: (remove if standalone)
```

---

## Files Requiring Corrections

1. ✅ REPORT_OUTPUT_SCHEMA_v2.md
2. ✅ ENTITY_MAPPING_GUIDE.md
3. ✅ IMPLEMENTATION_PLAN_v2_Upgrade.md

---

## Execution Priority

**High Priority (Before Phase 2):**
1. STT code correction (affects all entity references)
2. Token-efficient format (reduces prompt size)
3. CSV paths (scripts will fail otherwise)

**Medium Priority:**
4. MKT removal (cosmetic, doesn't block)

---

**Status:** Ready for systematic correction