# PROMPT: Collect and Consolidate All ENTITIES Taxonomy Folders

## Context

You are helping maintain a structured knowledge base for the **ENTITIES** workspace.
Over time, multiple `Taxonomy`-related folders have been created in different locations
(e.g. under `LIBRARIES`, `PROMPTS`, `TASK_MANAGERS`, backup folders, and integration paths).

We now want **one central canonical Taxonomy hub** at:

- `ENTITIES/TAXONOMY/`

Your task is to:

- Locate **all Taxonomy-related folders** that logically belong under ENTITIES.
- Copy their contents into the central `ENTITIES/TAXONOMY` folder.
- Preserve traceability by clearly logging where each folder came from.
- Do **not** delete originals – just prepare a clear list of sources
  so they can be reviewed and optionally deleted later.

## Scope and Targets

When scanning the filesystem, treat as in-scope any folder that:

- Has `Taxonomy` or `Taxonomy_Integration` in its path or name, **and**
- Is part of, or clearly related to, the ENTITIES structure.

Examples (non-exhaustive):

- `ENTITIES/LIBRARIES/Taxonomy/`
- `ENTITIES/PROMPTS/Taxonomy/`
- `ENTITIES/TASK_MANAGERS/Taxonomy/`
- `ENTITIES/PROMPTS/PROMPTS/Taxonomy_Integration/`
- Backups or archives that contain ENTITIES Taxonomy structures, such as:
  - `Taxonomy_Backup_/Taxonomy/Entities/...`
  - `ARCHIVE/Libs 25/Taxonomy/Entities/LIBRARIES/Prompts/Taxonomy_Integration/`
  - `DEPARTMENT_CONSOLIDATION_BACKUP_.../TASK_MANAGERS/.../Taxonomy_Integration/`

If you are unsure whether a folder belongs to ENTITIES Taxonomy,
err on the side of **including it** but mark it clearly in the log as "needs review".

## Rules for Destination Structure

- If `ENTITIES/TAXONOMY/` does **not** exist, create it.
- Under `ENTITIES/TAXONOMY/`, mirror the **logical origin** of the content so that
  different sources do not overwrite each other.

For example:

- From `ENTITIES/LIBRARIES/Taxonomy/` → copy into:
  - `ENTITIES/TAXONOMY/LIBRARIES__Taxonomy/`
- From `ENTITIES/PROMPTS/Taxonomy/` → copy into:
  - `ENTITIES/TAXONOMY/PROMPTS__Taxonomy/`
- From `ENTITIES/PROMPTS/PROMPTS/Taxonomy_Integration/` → copy into:
  - `ENTITIES/TAXONOMY/PROMPTS__Video_Processing__Taxonomy_Integration/`
- From `Taxonomy_Backup_/Taxonomy/Entities/DEPARTMENTS/...` → copy into:
  - `ENTITIES/TAXONOMY/BACKUP__Taxonomy__Entities__DEPARTMENTS__/...`

Use a consistent convention:

- Join the key path segments with double underscores `__`.
- Keep all nested subfolders and files intact under that root.

## Operational Instructions

1. **Discovery Phase**

   - Traverse the entire workspace starting from the root
     (e.g. `c:\Users\Dell\Dropbox\`).
   - Find every directory whose name or path contains `Taxonomy` or `Taxonomy_Integration`.
   - Filter to those that are part of or clearly associated with ENTITIES, including
     backups and archives.

2. **Logging and Source List**

   For each discovered folder that you decide to include:

   - Add a line to a **sources list** in memory with:
     - Full original path
     - A short origin tag (e.g. `LIBRARIES`, `PROMPTS`, `TASK_MANAGERS`, `BACKUP`, etc.)
     - A review flag: `ok` or `needs_review`

   Example log entry structure:

   - `[ok] LIBRARIES | c:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Taxonomy\`
   - `[ok] PROMPTS | c:\Users\Dell\Dropbox\ENTITIES\PROMPTS\Taxonomy\`
   - `[needs_review] BACKUP | c:\Users\Dell\Dropbox\Taxonomy_Backup_\Taxonomy\Entities\DEPARTMENTS\...`

3. **Copy Phase (No Deletions)**

   - Ensure `ENTITIES/TAXONOMY/` exists (create it if needed).
   - For each source folder:
     - Determine an appropriate destination subfolder name using the rules above.
     - Copy **all** contents (files + subfolders) into that destination.
     - If the destination already exists, do **not** silently overwrite; instead:
       - Prefer merging without data loss.
       - If a conflict occurs, either:
         - Skip the conflicting item and note it in the report, or
         - Create a variant name (e.g. append `_v2` or `_from_BACKUP`).

   - Do **not** delete, rename, or otherwise mutate the original source folders.

4. **Idempotency Requirements**

   The operation should be safe to run multiple times:

   - Before copying a file/folder, check if an identical item already exists
     at the destination.
   - If it does, skip or deduplicate rather than overwriting.
   - The log should make it clear which items were newly copied vs. skipped
     due to existing identical content.

5. **Final Output / Report**

   After processing all Taxonomy folders, produce a clear, human-readable report that includes:

   - **Summary**
     - Confirmation that `ENTITIES/TAXONOMY/` exists and has been populated.
     - Count of source folders processed.
     - Count of files/folders copied and skipped.

   - **Sources Checklist for Future Deletion**

     A list formatted so it can be used as a deletion checklist later, e.g.:

     ```text
     [ ] [ok] LIBRARIES | c:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Taxonomy\
     [ ] [ok] PROMPTS | c:\Users\Dell\Dropbox\ENTITIES\PROMPTS\Taxonomy\
     [ ] [needs_review] BACKUP | c:\Users\Dell\Dropbox\Taxonomy_Backup_\Taxonomy\Entities\DEPARTMENTS\...
     ```

   - **Conflicts and Issues**

     - Any folders or files that could not be copied, with reasons.
     - Any ambiguous folders where it was unclear whether they belong to ENTITIES,
       clearly marked as `needs_review`.

## Core Instruction (One-Sentence Version)

Collect all ENTITIES-related Taxonomy folders (including integrations and backups),
copy them into a structured, conflict-safe `ENTITIES/TAXONOMY/` hub without deleting
originals, and output a detailed checklist of all source locations for future manual
review and possible deletion.
