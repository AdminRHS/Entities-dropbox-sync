# SETTINGS Entity Documentation

**Entity Type:** SETTINGS  
**Domain:** System Configuration  
**Purpose:** Core system settings, configurations, and reference data  
**Created:** November 1, 2025  
**Last Updated:** November 1, 2025

---

## 📋 Overview

The SETTINGS entity domain manages core system settings, configurations, and reference data. It provides centralized configuration management, consistent reference data, flexible permission system, localization support (5 languages, 7+ countries), and user experience customization.

---

## 🗂️ Sub-Entities

### 1. Countries_Cities_Languages
**Purpose:** Geographic and language reference data

**Key Attributes:**
- Country name and code (ISO 3166)
- Cities and regions
- Language name and code (ISO 639)
- Language proficiency levels (A1-A2, B1, B2, C1, C2)
- Regional settings
- Time zones

**Supported Languages:**
- English (primary business language)
- Russian (many team members)
- Ukrainian (regional team members)
- Polish (European operations)
- German (European clients and team members)

**File Structure:**
```
Countries_Cities_Languages/
├── Countries.json
├── Cities.json
├── Languages.json
└── Language_Proficiency_Levels.json
```

---

### 2. Currencies_Rates
**Purpose:** Financial settings and exchange rates

**Key Attributes:**
- Currency code (ISO 4217)
- Currency name
- Exchange rates (base currency: USD)
- Rate update frequency
- Historical rates
- Payment methods

**Supported Currencies:**
- USD (US Dollar) - Primary
- EUR (Euro)
- UAH (Ukrainian Hryvnia)
- PLN (Polish Zloty)
- Other currencies as needed

**File Structure:**
```
Currencies_Rates/
├── Currencies.json
├── Exchange_Rates.json
└── Payment_Methods.json
```

---

### 3. Permissions
**Purpose:** Access control and permission management

**Key Attributes:**
- Permission name
- Permission type
- Resource (what the permission applies to)
- Action (what can be done)
- Role/Profession mapping
- User-specific permissions

**Sub-Entities:**
- **Permission_Types:** Categories of permissions (Read, Write, Delete, Admin)
- **Profession_Permissions:** Permissions assigned to specific roles
- **User_Permissions:** Individual user permission overrides

**File Structure:**
```
Permissions/
├── Permission_Types.json
├── Profession_Permissions.json
└── User_Permissions.json
```

---

### 4. Notifications
**Purpose:** System-level and user-specific notification settings

**Key Attributes:**
- Notification type
- Trigger conditions
- Delivery method (Email, Discord, In-app)
- Frequency settings
- User preferences
- Notification templates

**Sub-Entities:**
- **Push_Notifications:** System-level notification settings
- **User_Notifications:** User-specific notification preferences

**File Structure:**
```
Notifications/
├── Push_Notifications.json
└── User_Notifications.json
```

---

### 5. Calendar_Configurations
**Purpose:** Calendar settings and scheduling configurations

**Key Attributes:**
- Calendar name
- Calendar type (work, personal, project)
- Working hours
- Time zones
- Holiday definitions
- Recurrence patterns
- User-specific calendar settings

**Sub-Entities:**
- **Holiday:** Holiday definitions by country/region
- **Calendar:** Calendar configurations and templates
- **Calendar_Users:** User-specific calendar settings

**File Structure:**
```
Calendar_Configurations/
├── Holidays.json
├── Calendar_Templates.json
└── User_Calendars.json
```

---

## 🔗 Relationships

### Primary Relationships

1. **SETTINGS → All Entities**
   - Provides reference data (countries, currencies)
   - Controls permissions and access
   - Configures system behavior

2. **SETTINGS ↔ TALENTS**
   - Employee language preferences
   - Employee time zone settings
   - Employee notification preferences

3. **SETTINGS ↔ BUSINESSES**
   - Client country and currency
   - Client time zone
   - Client language preferences

4. **SETTINGS ↔ TASK_MANAGERS**
   - Task scheduling uses calendar settings
   - Task notifications use notification settings
   - Task permissions use permission settings

---

## 📊 Example Settings

### Language Proficiency Levels
```json
{
  "level": "C1",
  "name": "Proficient User - Advanced",
  "description": "Can understand a wide range of demanding, longer texts",
  "cefr_level": "C1",
  "typical_users": "Native-like proficiency for professional use"
}
```

### Holiday Definition
```json
{
  "holiday_id": "HOL-001",
  "name": "New Year's Day",
  "date": "2025-01-01",
  "countries": ["USA", "Ukraine", "Poland"],
  "type": "Public Holiday",
  "recurrence": "Yearly"
}
```

### Permission Definition
```json
{
  "permission_id": "PERM-001",
  "name": "Create Job Posting",
  "type": "Write",
  "resource": "JOBS/Job_Postings",
  "action": "Create",
  "professions": ["HR Manager", "Recruiter"],
  "description": "Permission to create new job postings"
}
```

---

## 📝 File Naming Convention

**Pattern:** `SETTINGS_[Type]_[Name]_[Version].json`

**Examples:**
- `SETTINGS_Countries_Supported_v1.json`
- `SETTINGS_Languages_Proficiency_Levels_v1.json`
- `SETTINGS_Permissions_Job_Posting_Create_v1.json`
- `SETTINGS_Calendar_Holidays_2025_v1.json`

---

## 📋 Metadata Template

Every settings file should include:

```json
{
  "entity_type": "SETTINGS",
  "sub_entity": "Countries_Cities_Languages",
  "setting_id": "SET-001",
  "setting_name": "Supported Countries",
  "setting_type": "Reference Data",
  "description": "List of countries where Remote Helpers operates",
  "countries": [
    {
      "code": "US",
      "name": "United States",
      "cities": ["New York", "Los Angeles", "San Francisco"],
      "time_zone": "America/New_York",
      "currency": "USD"
    },
    {
      "code": "UA",
      "name": "Ukraine",
      "cities": ["Kyiv", "Lviv", "Kharkiv"],
      "time_zone": "Europe/Kiev",
      "currency": "UAH"
    }
  ],
  "last_updated": "2025-01-01",
  "version": "1.0",
  "tags": ["countries", "reference_data", "localization"]
}
```

---

## 🔄 Settings Management Workflow

### 1. Define Setting
- Create setting definition
- Specify data structure
- Set default values
- Document usage

### 2. Configure Setting
- Set system-wide values
- Configure environment-specific overrides
- Set user-specific preferences

### 3. Apply Setting
- Settings applied to relevant entities
- Permissions enforced
- Notifications sent
- Calendars updated

### 4. Monitor Setting
- Track setting usage
- Measure impact
- Optimize based on data

---

## 🎯 Business Value

- **Centralized Configuration:** Single source of truth for system settings
- **Consistent Reference Data:** Standardized countries, currencies, languages
- **Flexible Permissions:** Role-based and user-specific access control
- **Localization Support:** Multi-language and multi-country operations
- **User Customization:** Personalized notification and calendar preferences

---

## 📚 Related Documents

- `../TALENTS/` - Employee settings and preferences
- `../BUSINESSES/` - Client country and currency settings
- `../TASK_MANAGERS/` - Task scheduling and notification settings
- `../ACCOUNTS/` - Parameters that may reference settings

---

**Last Updated:** November 1, 2025

