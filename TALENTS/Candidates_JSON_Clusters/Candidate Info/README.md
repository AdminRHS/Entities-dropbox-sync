# Candidate Info Templates

This folder contains split template files derived from `candidate_fields_template.json`. Each file represents a logical grouping of related candidate data fields.

## Template Files

### Core Information
- **Candidate_Basic_Info.json** - Core candidate identification fields (id, name, age, company info, etc.)
- **Contact_Information.json** - Contact details (phone, email, telegram, viber, instagram)

### Professional Information
- **Work_Experience.json** - Work experience array
- **Education.json** - Education array
- **Skills.json** - Technical and professional skills array
- **Languages.json** - Language proficiencies with levels

### Financial Information
- **Candidate_Salaries.json** - Salary-related fields (expected/started salaries and currencies)

### Organizational Information
- **HR_Manager.json** - Assigned HR manager details
- **Department_Position.json** - Department and position information
- **Team_Lead.json** - Team lead information and bonus approvals
- **HR_Departments.json** - HR departments array

### Status & Process
- **Status_Information.json** - Candidate status and admin status fields
- **Interview_Information.json** - Interview scheduling and video interview data
- **Source.json** - Source information (where candidate applied from)
- **Communication.json** - Preferred communication channel

### Additional Data
- **Address.json** - Address and location information
- **URLs_And_Documents.json** - Links to resumes, portfolios, photos, test links
- **Dates_And_Times.json** - Employment start/end dates and times
- **Notes_And_Additional.json** - Notes and administrative fields

## Usage

Each template file follows this structure:
```json
{
  "template_name": "Template_Name",
  "description": "Description of the template purpose",
  "fields": {
    // Field definitions with type, description, and example
  }
}
```

## Data Files

### Candidate Listings

#### Simple Listing
- **Candidates_Simple_Listing.json** - Contains a minimal listing with only essential fields:
  - `id` - Candidate ID
  - `name_candidate` - Candidate full name
  
  This file contains 1000 entries from `Candidates_cluster_0001_cleaned.json` with just the basic identification fields. Perfect for quick lookups and simple reference lists.

#### Detailed Listing
- **Candidates_Listing.json** - Contains a listing of all candidates with additional metadata:
  - `id` - Candidate ID
  - `name_candidate` - Candidate full name
  - `folder_location` - employees profile  (e.g., "Candidates_cluster_0001_cleaned.json")
 
  
  This file contains 1000 entries from `Candidates_cluster_0001_cleaned.json` and can be used as an index to locate specific candidates in the cluster files.

### Test Data
- **Candidates_Test_Data_10.json** - Contains the first 10 candidates from `Candidates_cluster_0001_cleaned.json` with complete field data. This file is useful for:
  - Testing data processing scripts
  - Understanding the full structure of candidate records
  - Development and debugging purposes

## Notes

- Arrays with `item_type: "unknown"` (like `work_experiences`, `educations`, `hr_departments`) should be validated against actual data to determine their exact structure.
- All templates maintain the same field structure and naming conventions as the original `candidate_fields_template.json`.
- Fields marked as `NoneType` may be null in actual candidate records.
- The listing file provides quick access to candidate IDs and names without loading the full candidate data.

