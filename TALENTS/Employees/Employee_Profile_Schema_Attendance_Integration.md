# Employee Profile Schema - Attendance Analyzer Integration

## Overview
Integration plan for connecting the `attendance_analyzer` system with the Employee Profile Schema, enabling automatic population of attendance metrics, work patterns, and risk assessments into employee profiles.

---

## Integration Architecture

### Data Flow
```
Discord Voice Log (crm_export_*.json)
    ↓
attendance_analyzer (employee_analytics.py)
    ↓
Attendance Metrics & Analysis
    ↓
Employee Profile Schema (Employee_Profile_Schema.md)
    ↓
Employee Profile (profiles/*/Profile*.md)
```

---

## Key Integration Points

### 1. Employee Identification Matching

**Primary Keys**:
- **Employee ID** (`Profile*.md` → `ID` field)
- **Discord User ID** (`Profile*.md` → `Discord ID` field)

**Matching Strategy**:
```python
# Priority 1: Match by Employee ID (most reliable)
employee_id_match = attendance_df['Employee ID'] == profile['ID']

# Priority 2: Match by Discord User ID (fallback)
discord_id_match = attendance_df['Discord User ID'] == profile['Discord ID']
```

**Example Mapping**:
- Profile: `ID: 37226`, `Discord ID: 910144676881903646`
- Attendance: `Employee ID: 37226`, `Discord User ID: 910144676881903646`
- **Match**: ✓ Both identifiers match

---

## Schema Field Mapping

### 2.1 Attendance Metrics → Employee.Metrics

| Attendance Analyzer Field | Schema Field | Type | Description |
|---------------------------|-------------|------|--------------|
| `Working_Hours` | `Employee.Metrics.AvgWorkingHours` | Number | Average working hours per day |
| `Working_Hours_Raw` | `Employee.Metrics.TotalWorkingHours` | Number | Total working hours (raw) |
| `Records Count` | `Employee.Metrics.AttendanceRecords` | Number | Number of attendance records |
| `Status` | `Employee.Metrics.AttendanceStatus` | String | Active/No Records |
| `Has_Activity` | `Employee.Metrics.IsActive` | Boolean | Has activity records |

**Schema Addition**:
```json
{
  "metrics": {
    "attendance": {
      "avg_working_hours": 8.5,
      "total_working_hours": 170.0,
      "attendance_records": 20,
      "attendance_status": "Active",
      "is_active": true,
      "last_check_in": "2025-11-17 07:03:20",
      "last_check_out": "2025-11-17 16:10:50"
    }
  }
}
```

### 2.2 Work Patterns → Employee.WorkPatterns

| Attendance Analyzer Field | Schema Field | Type | Description |
|---------------------------|-------------|------|--------------|
| `Arrival_Category` | `Employee.WorkPatterns.ArrivalPattern` | String | Very Early Bird/Early Bird/On Time/Late Arrival |
| `Duration_Category` | `Employee.WorkPatterns.DurationPattern` | String | Standard/Short Day/Overtime/Excessive Hours |
| `Check_In_Hour` | `Employee.WorkPatterns.AvgCheckInHour` | Number | Average check-in hour (0-23) |
| `Check_Out_Hour` | `Employee.WorkPatterns.AvgCheckOutHour` | Number | Average check-out hour (0-23) |

**Schema Addition**:
```json
{
  "work_patterns": {
    "arrival_pattern": "Early Bird",
    "duration_pattern": "Standard",
    "avg_check_in_hour": 7.5,
    "avg_check_out_hour": 16.2,
    "typical_start_time": "07:00-09:00",
    "typical_end_time": "16:00-18:00"
  }
}
```

### 2.3 Risk Assessment → Employee.Metrics.Risk

| Attendance Analyzer Field | Schema Field | Type | Description |
|---------------------------|-------------|------|--------------|
| `Risk_Category` | `Employee.Metrics.RiskCategory` | String | Normal/Medium Risk/High Risk/Inactive |
| `Total_Anomalies` | `Employee.Metrics.TotalAnomalies` | Number | Total number of anomalies detected |
| `Anomaly_Short_Day` | `Employee.Metrics.Anomalies.ShortDays` | Number | Count of short days |
| `Anomaly_Long_Day` | `Employee.Metrics.Anomalies.LongDays` | Number | Count of long days |
| `Anomaly_Late_Arrival` | `Employee.Metrics.Anomalies.LateArrivals` | Number | Count of late arrivals |
| `Anomaly_Early_Departure` | `Employee.Metrics.Anomalies.EarlyDepartures` | Number | Count of early departures |
| `Anomaly_Late_Departure` | `Employee.Metrics.Anomalies.LateDepartures` | Number | Count of late departures |
| `Missing_Checkout` | `Employee.Metrics.Anomalies.MissingCheckouts` | Number | Count of missing checkouts |

**Schema Addition**:
```json
{
  "metrics": {
    "risk": {
      "risk_category": "Normal",
      "total_anomalies": 0,
      "anomalies": {
        "short_days": 0,
        "long_days": 0,
        "late_arrivals": 0,
        "early_departures": 0,
        "late_departures": 0,
        "missing_checkouts": 0
      }
    }
  }
}
```

### 2.4 Status Updates → Employee.Position.Status

**Integration Rule**:
- If `Risk_Category == "Inactive"` AND `Has_Activity == False` → Consider updating Status
- If `Risk_Category == "High Risk"` → Flag for review (don't auto-update Status)
- If employee in Left folder → Status = "LEFT" (existing rule)

**Schema Addition**:
```json
{
  "position": {
    "status": "Work",
    "attendance_status": "Active",
    "risk_flag": false,
    "last_attendance_review": "2025-11-17"
  }
}
```

---

## Extended Schema Structure

### Complete Employee Profile with Attendance Integration

```json
{
  "id": 37226,
  "name": "Artemchuk Nikolay",
  "contacts": {
    "discord_id": "910144676881903646"
  },
  "position": {
    "status": "Work",
    "attendance_status": "Active"
  },
  "metrics": {
    "attendance": {
      "avg_working_hours": 8.5,
      "total_working_hours": 170.0,
      "attendance_records": 20,
      "is_active": true,
      "last_check_in": "2025-11-17 07:03:20",
      "last_check_out": "2025-11-17 16:10:50",
      "attendance_rate": 95.0
    },
    "risk": {
      "risk_category": "Normal",
      "total_anomalies": 0,
      "anomalies": {
        "short_days": 0,
        "long_days": 0,
        "late_arrivals": 0,
        "early_departures": 0,
        "late_departures": 0,
        "missing_checkouts": 0
      }
    },
    "activity_frequency": "High",
    "workload": "VERY HIGH",
    "organization_score": 95,
    "completion_rate": 98
  },
  "work_patterns": {
    "arrival_pattern": "Early Bird",
    "duration_pattern": "Standard",
    "avg_check_in_hour": 7.5,
    "avg_check_out_hour": 16.2,
    "typical_start_time": "07:00-09:00",
    "typical_end_time": "16:00-18:00",
    "consistency_score": 92
  },
  "source_files": {
    "profile": "Nov25/AI/Artemchuk Nikolay/Profile Project manager, Lead generator Artemchuk Nikolay.md",
    "attendance_data": "Voice Log Discord/crm_export_2025-11-18.json",
    "attendance_analysis": "attendance_analyzer/output/reports/attendance_report_2025-11-18.xlsx"
  }
}
```

---

## Integration Implementation

### Phase 1: Data Collection Script

**File**: `ENTITIES/TALENTS/Employees/scripts/integrate_attendance.py`

**Functionality**:
1. Load attendance analyzer output (Excel/CSV)
2. Load employee profiles from `profiles/` directory
3. Match employees by Employee ID and Discord ID
4. Extract attendance metrics
5. Update employee profile schema data

**Pseudocode**:
```python
def integrate_attendance_data():
    # Load attendance analysis
    attendance_df = load_attendance_analysis()
    
    # Load all profiles
    profiles = load_all_profiles()
    
    # Match and merge
    for profile in profiles:
        employee_id = profile['ID']
        discord_id = profile['Discord ID']
        
        # Find matching attendance record
        attendance_record = find_matching_record(
            attendance_df, 
            employee_id, 
            discord_id
        )
        
        if attendance_record:
            # Update profile with attendance data
            profile['metrics']['attendance'] = extract_attendance_metrics(attendance_record)
            profile['metrics']['risk'] = extract_risk_metrics(attendance_record)
            profile['work_patterns'] = extract_work_patterns(attendance_record)
            
            # Save updated profile
            save_profile(profile)
```

### Phase 2: Schema Extension

**Update**: `Employee_Profile_Schema.md`

**New Sections**:
- **Attendance Data Source** (Priority P1)
- **Attendance Metrics Mapping**
- **Work Patterns Mapping**
- **Risk Assessment Mapping**
- **Status Update Rules**

### Phase 3: Automated Workflow

**Integration with attendance_analyzer**:

```python
# Enhanced employee_analytics.py
class EmployeeAnalytics:
    def export_to_profile_schema(self):
        """Export attendance data to Employee Profile Schema format"""
        profile_data = []
        
        for _, row in self.df.iterrows():
            profile_entry = {
                "employee_id": row['Employee ID'],
                "discord_id": row['Discord User ID'],
                "metrics": {
                    "attendance": {
                        "avg_working_hours": row['Working_Hours'],
                        "attendance_records": row['Records Count'],
                        "is_active": row['Has_Activity']
                    },
                    "risk": {
                        "risk_category": row['Risk_Category'],
                        "total_anomalies": row['Total_Anomalies']
                    }
                },
                "work_patterns": {
                    "arrival_pattern": row['Arrival_Category'],
                    "duration_pattern": row['Duration_Category']
                }
            }
            profile_data.append(profile_entry)
        
        return profile_data
```

---

## Data Source Priority Update

### Updated Priority Matrix

| Priority | Source | Use Case | Update Frequency |
|----------|--------|----------|------------------|
| **P0** | Profile*.md | Core employee data | On creation/update |
| **P1** | **attendance_analyzer** | **Attendance metrics, risk assessment** | **Daily** |
| **P1** | daily.md | Work activities, skills, tools | Daily |
| **P1** | Overview Nov25 | Performance reviews, role | Monthly/Quarterly |
| **P2** | plans.md | Current projects, goals | Weekly |
| **P2** | task.md | Task patterns, skills | Weekly |
| **P3** | README.md | Workflow compliance | On change |
| **P3** | notes.md | Learning, preferences | As needed |
| **P4** | JSON files | Structured data, templates | On creation |
| **P4** | Folder structure | Activity metrics | Monthly |

---

## Integration Rules

### Rule 1: Employee Matching
- **Primary**: Match by Employee ID (numeric string)
- **Secondary**: Match by Discord User ID (if Employee ID missing)
- **Fallback**: Match by Name (fuzzy matching, low confidence)

### Rule 2: Data Merging
- **Attendance data** supplements existing profile data
- **Never overwrite** core profile fields (ID, Name, Contact Info)
- **Update** metrics fields with latest attendance analysis
- **Append** historical data to work_history array

### Rule 3: Status Updates
- **Automatic**: Update `attendance_status` based on `Has_Activity`
- **Manual Review**: Flag `High Risk` employees for manual status review
- **No Auto-Update**: Never automatically change `Status` to "Fired" or "LEFT" based on attendance alone

### Rule 4: Anomaly Handling
- **Track**: All anomalies stored in `metrics.risk.anomalies`
- **Alert**: High Risk employees flagged in `metrics.risk.risk_flag`
- **Historical**: Maintain anomaly history for trend analysis

---

## Output Integration

### Attendance Analyzer Outputs → Schema Fields

| Analyzer Output | Schema Destination | Format |
|----------------|-------------------|--------|
| Excel Report → Full Data sheet | `Employee.Metrics.Attendance.*` | JSON |
| Excel Report → Anomalies sheet | `Employee.Metrics.Risk.*` | JSON |
| Excel Report → Statistics sheet | `Employee.Metrics.Statistics.*` | JSON |
| CSV Export | `Employee.Metrics.Attendance.RawData` | Array |
| Summary Report | `Employee.Metrics.Attendance.Summary` | Text |
| Visualizations | `Employee.Metrics.Attendance.Charts` | File paths |

---

## Workflow Integration

### Daily Workflow

```
1. Discord Voice Log Bot collects data → crm_export_YYYY-MM-DD.json
2. attendance_analyzer runs analysis → Excel/CSV reports
3. Integration script matches employees → Updates profiles
4. Schema validation → Ensures data integrity
5. Profile update → Saves enriched profiles
```

### Weekly Workflow

```
1. Aggregate weekly attendance data
2. Calculate weekly metrics (avg hours, consistency)
3. Update Employee.Metrics.Attendance.Weekly
4. Generate weekly attendance report
5. Flag anomalies for review
```

### Monthly Workflow

```
1. Aggregate monthly attendance data
2. Calculate monthly trends
3. Update Employee.Metrics.Attendance.Monthly
4. Generate monthly attendance report
5. Update risk assessments
6. Generate department-level statistics
```

---

## Schema Validation Extensions

### New Validation Rules

11. **Attendance Data**: If attendance data exists, `metrics.attendance.is_active` must be boolean
12. **Risk Category**: `metrics.risk.risk_category` must be one of: Normal, Medium Risk, High Risk, Inactive
13. **Working Hours**: `metrics.attendance.avg_working_hours` must be between 0 and 24
14. **Anomaly Count**: `metrics.risk.total_anomalies` must be non-negative integer
15. **Discord ID Match**: If `contacts.discord_id` exists, should match attendance data Discord User ID

---

## Cross-Entity Relationships

### LIBRARIES Taxonomy Integration

```
Employee (TALENTS)
  ├─ Attendance Status → STS-### (Statuses taxonomy)
  ├─ Risk Category → STS-### (Statuses taxonomy)
  └─ Work Patterns → PRM-### (Parameters taxonomy)
```

### TASK_MANAGERS Integration

```
Employee Attendance Metrics
  ├─ Anomalies → TSK-### (Task: Review attendance anomalies)
  ├─ High Risk → TSK-### (Task: Employee review meeting)
  └─ Inactive → TSK-### (Task: Check employee status)
```

---

## Example Integration Output

### Before Integration
```markdown
# Employee Profile

**ID:** 37226
**Name:** Artemchuk Nikolay
**Discord ID:** 910144676881903646
**Status:** Work
```

### After Integration
```markdown
# Employee Profile

**ID:** 37226
**Name:** Artemchuk Nikolay
**Discord ID:** 910144676881903646
**Status:** Work

## Attendance Metrics

- **Average Working Hours:** 8.5h/day
- **Attendance Status:** Active
- **Risk Category:** Normal
- **Total Anomalies:** 0
- **Arrival Pattern:** Early Bird (7:00-9:00)
- **Last Check-In:** 2025-11-17 07:03:20
- **Last Check-Out:** 2025-11-17 16:10:50
```

---

## Implementation Checklist

### Phase 1: Schema Extension
- [ ] Update `Employee_Profile_Schema.md` with attendance fields
- [ ] Document attendance data source mapping
- [ ] Add validation rules for attendance data
- [ ] Update integration points section

### Phase 2: Integration Script
- [ ] Create `scripts/integrate_attendance.py`
- [ ] Implement employee matching logic
- [ ] Implement data extraction functions
- [ ] Implement profile update functions
- [ ] Add error handling and logging

### Phase 3: Attendance Analyzer Enhancement
- [ ] Add `export_to_profile_schema()` method
- [ ] Add profile matching functionality
- [ ] Generate schema-compatible JSON output
- [ ] Add integration test cases

### Phase 4: Workflow Integration
- [ ] Create daily automation workflow
- [ ] Create weekly aggregation workflow
- [ ] Create monthly reporting workflow
- [ ] Add notification system for anomalies

### Phase 5: Testing & Validation
- [ ] Test employee matching (ID, Discord ID)
- [ ] Test data extraction and mapping
- [ ] Test profile updates
- [ ] Validate schema compliance
- [ ] Test error handling

---

## Benefits of Integration

1. **Automated Metrics**: Attendance metrics automatically populate employee profiles
2. **Risk Detection**: Early identification of attendance issues
3. **Performance Tracking**: Historical attendance data for performance reviews
4. **Data Consistency**: Single source of truth for attendance metrics
5. **Workflow Automation**: Reduced manual data entry
6. **Cross-System Integration**: Attendance data available across ENTITIES ecosystem

---

## Notes

- **Data Privacy**: Attendance data is sensitive; ensure proper access controls
- **Historical Data**: Maintain historical attendance records for trend analysis
- **Anomaly Thresholds**: Configurable in `attendance_analyzer/config/analysis_config.json`
- **Update Frequency**: Daily updates recommended for real-time insights
- **Manual Override**: Allow manual updates for exceptional cases
- **Audit Trail**: Log all attendance data updates for compliance

---

**Created**: 2025-01-18
**Last Updated**: 2025-01-18
**Integration Version**: 1.0
**Related Systems**: attendance_analyzer, Employee Profile Schema, Discord Voice Log Bot

