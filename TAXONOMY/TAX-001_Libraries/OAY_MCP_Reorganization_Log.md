# OAY and MCP Reorganization Log

**Date:** 2025-11-19
**Purpose:** Move oa-y.com from Tools to Assets, create MCP Services category

---

## Changes Made

### 1. Created MCP_Services Directory

**Directory:** `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Tools\MCP_Services`

**Purpose:** Centralize all MCP (Model Context Protocol) services and connectors

**Note:** This is a directory for organizing MCP-related tools. "MCP Services" as a category name only appears in the Master List CSV for classification - it's not a field in the actual tool JSON files.

**Files Created:**
- `README.md` - Directory documentation
- `TOL-MCP-001_OAY_MCP_Service.json` - OAY MCP Service configuration

### 2. Moved MCP Connectors to MCP_Services Directory

**Files Relocated:**

- `CRM_MCP_Connector.json`
  - From: `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Tools\Integration_Tools\CRM_MCP_Connector.json`
  - To: `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Tools\MCP_Services\CRM_MCP_Connector.json`
- `Gmail_MCP_Connector.json`
  - From: `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Tools\Integration_Tools\Gmail_MCP_Connector.json`
  - To: `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Tools\MCP_Services\Gmail_MCP_Connector.json`
- `Google_Calendar_MCP_Connector.json`
  - From: `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Tools\Integration_Tools\Google_Calendar_MCP_Connector.json`
  - To: `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Tools\MCP_Services\Google_Calendar_MCP_Connector.json`

### 3. Created OAY Asset Entry

**Asset Registry:** `C:\Users\Dell\Dropbox\ENTITIES\ASSETS\oa-y\OAY_Asset_Registry.json`

**Classification:**
- **Type:** Asset (not Tool)
- **Reason:** oa-y.com is an educational platform/content repository, not a software tool
- **Location:** `ASSETS/oa-y/`
- **Access Method:** MCP Service (TOL-MCP-001)

### 4. Updated Master Files

**Files Updated:**
- `Tools_Master_List.csv` - Removed TOL-176 (oa-y.com), added TOL-MCP-001
- `Tools_Master_Priority.json` - Same updates
- MCP connectors recategorized with "MCP Services" label in the "Category" column of the Master List (for classification purposes only)

---

## New MCP Services Structure

### MCP_Services Directory

**Location:** `LIBRARIES/Tools/MCP_Services/`

**Note:** "MCP Services" is just a classification label used in the Master List CSV for organizing tools. The actual directory is `MCP_Services` without any "Category" designation in the tool files themselves.

**Files in this directory:**

1. **TOL-MCP-001_OAY_MCP_Service.json**
   - Purpose: Connect to oa-y.com Online Academy
   - Repository: `github:AdminRHS/oa-y-mcp-service`
   - Environment: Production
   - Connected Asset: ASSETS/oa-y/

2. **CRM_MCP_Connector.json** (TOL-177)
   - Purpose: Airtable CRM integration
   - Moved from Integration_Tools

3. **Gmail_MCP_Connector.json**
   - Purpose: Gmail integration via MCP
   - Moved from Integration_Tools

4. **Google_Calendar_MCP_Connector.json**
   - Purpose: Google Calendar integration via MCP
   - Moved from Integration_Tools

**Related Tool:**
- **TOL-162: MCP Protocol** (located in Development_Tools)
   - The base protocol specification used by all MCP services

---

## Configuration Example

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "oa-y-mcp-service": {
      "command": "npx",
      "args": ["github:AdminRHS/oa-y-mcp-service"],
      "env": {
        "APP_ENV": "prod",
        "API_TOKEN": "d383d4d1-5829-4aa1-80ce-0668d6869386",
        "API_TOKEN_LIBS": "sk_ksE_rARLjfvNSchxppLvgj6Svxvos1zuS4oZdQowOEo"
      }
    }
  }
}
```

---

## Assets vs Tools Classification

### Why oa-y.com is an Asset (not a Tool):

**Assets:**
- Content repositories
- Platforms owned by the company
- Data sources
- Educational content
- Media libraries

**Tools:**
- Software applications
- Third-party services
- Development frameworks
- Automation platforms

**oa-y.com Classification:**
- [YES] Educational platform with courses
- [YES] Content repository
- [YES] Company-owned asset
- [YES] Accessed via MCP service
- [NO] Not a software tool itself

---

## Next Steps

1. [DONE] Create MCP_Services directory
2. [DONE] Create OAY MCP Service configuration
3. [DONE] Move MCP connectors to MCP_Services directory
4. [DONE] Create OAY asset registry
5. [DONE] Update master files (added "MCP Services" as category label in CSV)
6. [TODO] Test MCP service connection
7. [TODO] Document all MCP services
8. [TODO] Update cross-references in Objects/Workflows

---

**Maintained By:** Taxonomy Team
**Status:** Complete
**Last Updated:** 2025-11-19
