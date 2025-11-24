# Entities Dropbox to GitHub Sync

This automation syncs the `/ENTITIES` folder from Dropbox to the GitHub repository `git@github.com:AdminRHS/Entities-dropbox-sync.git`.

## How It Works

1. The GitHub Action runs on a schedule (daily at 2:00 AM UTC) or can be triggered manually
2. It connects to Dropbox using the access token
3. It scans the `/ENTITIES` folder in Dropbox
4. It compares files with the current git repository
5. It downloads new and modified files
6. It deletes files that were removed from Dropbox
7. It generates a changelog
8. It commits and pushes all changes to GitHub

## Notes

- The sync excludes `.automation` folders and automation-related files
- Access tokens expire after a period; the refresh token allows automatic renewal
- The changelog is saved as `CHANGELOG.md` in the repository
- All changes are committed with a timestamp

