# Projects Library

Each file in this directory represents a reusable project or workflow blueprint that links tasks back to our existing `Actions`, `Responsibilities`, and `Objects` libraries.

Recommended JSON fields:

- `project_workflow_id`: Stable identifier (`WF-<slug>-###`).
- `name` + `description`: High-level summary of the workflow.
- `category`: Aligns with the process categories already defined (e.g., `Creation`, `Analysis`).
- `related_actions` / `related_objects`: Canonical lists that reference the Libraries catalog.
- `tasks`: Ordered collection of responsibilities broken into 2–3 word phrases (`action + object`) with any supporting details/checklists.

Use short responsibility names (e.g., `Generate product image`, `Adjust prompt accuracy`, `Save prompt IDs`) so downstream automation can map them to existing taxonomy items.  
Add new files per workflow (one JSON per project).
