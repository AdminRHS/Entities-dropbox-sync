# Parameters Data Organization by Department

This directory groups profession-level parameters into department-level summaries. It complements `parameters/organized_by_profession` by providing a department-first view.

## Directory Structure

```
parameters/
  organized_by_department/
    ├── _parameters_organization_summary.json
    ├── managers_parameters.json
    ├── developers_parameters.json
    ├── designers_parameters.json
    ├── marketers_parameters.json
    └── README.md
```

## Departments Covered

- managers (sales manager, lead generator, recruiter, project manager)
- developers (back end developer)
- designers (graphic designer)
- marketers (seo manager)

## File Format

Each department file follows:

```json
{
  "metadata": {
    "department": "string",
    "created_date": "ISO date",
    "source": "parameters/organized_by_profession"
  },
  "professions": [
    { "name": "string", "file": "relative path", "total_parameters": number }
  ],
  "summary": {
    "profession_count": number,
    "total_parameters": number
  }
}
```

## Notes

- We reference profession files to avoid duplication.
- Totals come from each profession file’s summaries.
