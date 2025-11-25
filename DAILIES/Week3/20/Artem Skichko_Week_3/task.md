# Task Breakdown - [21.11.2025]

## Instructions
**What**: Detailed action steps
**Include**:
- Break each plan item into specific steps
- Add links and resources
- Clear instructions for execution

---

## Task 1: Resolve Google OAuth 500 Error in upload_crms

### Steps:
1. Contact Auth service team/maintainers via Slack/email to request:
   - Access to Auth service logs for the 500 error
   - Information about required redirect URI registration
   - Documentation for `/api/auth/google` endpoint parameters

2. Review the error details:
   - Check if `http://localhost:3000/oauth-callback` is registered as allowed redirect URI
   - Verify if `upload_crms` service is configured in Auth service
   - Identify missing parameters (state, client_id, etc.)

3. Document findings:
   - Create a summary of backend requirements
   - List all required query parameters
   - Note any configuration changes needed

4. Coordinate with backend team:
   - Share frontend implementation details (already sending service parameter)
   - Request redirect URI registration if needed
   - Verify service configuration exists

5. Test OAuth flow once backend is configured:
   - Test Google login button click
   - Verify redirect to Google works
   - Check callback handling
   - Confirm token exchange and user login

### Resources and Links:
- Auth service: `https://userdev.anyemp.com`
- Frontend code: `upload_crms/client/src/services/auth.js`
- OAuth callback handler: `upload_crms/client/src/pages/OAuthCallback.jsx`
- Config file: `upload_crms/client/src/config.js`
- Documentation: `upload_crms/prompt-cursor-skichko.md`

### Instructions:
- Start by reaching out to Auth service team first thing in the morning
- While waiting for response, review frontend implementation to ensure it's correct
- Document all communication and findings for future reference
- Test thoroughly once backend configuration is updated
- Update daily.md with progress and outcomes

---

## Task 2: Verify CI Pipeline for Dashboard Project

### Steps:
1. Check CI pipeline status:
   - Review recent CI runs for Dashboard project
   - Verify `update_data.py` executes successfully
   - Check for any import-related errors

2. Test locally to match CI environment:
   - Run `update_data.py` from different directory structures
   - Verify `sys.path` modifications work correctly
   - Confirm `reports.generate_snapshot` imports successfully

3. Review CI configuration:
   - Check if CI uses same directory structure as expected
   - Verify Python path settings in CI config
   - Ensure all dependencies are available

4. Monitor next CI run:
   - Watch for any ModuleNotFoundError
   - Verify script completes successfully
   - Check that reports are generated correctly

5. Document results:
   - Note any issues found
   - Update documentation if needed
   - Share findings with team if relevant

### Resources and Links:
- Script: `Dashboard project/update_data.py`
- CI configuration files (check project repository)
- Reports module: `reports/generate_snapshot.py`

### Instructions:
- Check CI status first to see if there are any current failures
- Test the script locally in a clean environment to simulate CI
- If issues found, apply the same fix pattern used today
- Document all findings in daily.md

---

## Task 3: Test and Verify lead_gen_analytics Dashboard Enhancements

### Steps:
1. Test hover effects in production/staging:
   - Verify table hover effects (summary-table, matrix-table, segmentation-table)
   - Test chart card hover effects
   - Check both light and dark theme compatibility

2. Test for edge cases:
   - Test with different screen sizes (responsive design)
   - Verify hover effects don't interfere with click events
   - Check performance with large datasets

3. Verify theme switching:
   - Switch between light and dark themes
   - Ensure hover colors are appropriate for each theme
   - Check for any visual glitches

4. Gather user feedback:
   - Ask team members to test the new hover effects
   - Collect feedback on UX improvements
   - Note any suggestions for further enhancements

5. Document test results:
   - Record any bugs or issues found
   - Note performance observations
   - List user feedback received

### Resources and Links:
- Dashboard: lead_gen_analytics project
- CSS files with hover effects
- Theme configuration files

### Instructions:
- Start with manual testing of all hover effects
- Test in different browsers if possible
- Document any issues immediately
- Consider accessibility improvements based on feedback

---

## Task 4: Apply Configuration Centralization Pattern to Other Projects

### Steps:
1. Identify projects with direct env access:
   - Search for `process.env` usage in other projects
   - Find `import.meta.env` direct access in frontend projects
   - List projects that would benefit from centralization

2. Prioritize projects:
   - Start with most active/maintained projects
   - Focus on projects with multiple env variable accesses
   - Consider projects with similar structure to upload_crms

3. Create migration plan:
   - Design config file structure for each project
   - Plan migration steps
   - Estimate time needed

4. Apply pattern to one project:
   - Create config file (config.js or config.ts)
   - Update all direct env accesses to use config
   - Test thoroughly
   - Document changes

5. Review and iterate:
   - Check if pattern works well
   - Adjust approach if needed
   - Plan for remaining projects

### Resources and Links:
- Reference implementation: `upload_crms/client/src/config.js`
- Backend reference: `upload_crms/src/config/index.ts`
- Pattern documentation: `upload_crms/prompt-cursor-skichko.md`

### Instructions:
- Start by identifying projects, don't rush into implementation
- Use upload_crms as a reference for the pattern
- Test each migration thoroughly before moving to next project
- Document learnings and improvements to the pattern

---

## Reminder
- Break down each plan into steps
- Add all necessary links and resources
- Write clear execution instructions
- Start with high-priority tasks in the morning
- Use AI tools (NotebookLM, Gemini AI) to assist with tasks
- Document progress in daily.md throughout the day
- Test thoroughly before considering tasks complete
- Apply learned skills immediately to reinforce learning
