# Task Breakdown - [20.11.2025]

## Instructions
**What**: Detailed action steps
**Include**:
- Break each plan item into specific steps
- Add links and resources
- Clear instructions for execution

---

## Task 1: New Projects from Lillia - Initial Setup and Task Review (High Priority)

### Steps:
1. Check email for repository access invitations from Lillia
2. Verify access to both new project repositories (check GitHub/GitLab notifications)
3. Clone first project repository to local machine:
   - Navigate to appropriate directory
   - Run `git clone [repository-url]`
   - Verify clone was successful
4. Clone second project repository to local machine
5. Review README files for both projects:
   - Read setup instructions
   - Note required dependencies
   - Check for Docker setup requirements
   - Identify environment variable requirements
6. Set up first project (start with clearer setup instructions):
   - Create `.env.local` or `.env` file as instructed
   - Add required API keys and configuration
   - Install dependencies: `npm install` or `yarn install`
   - Check for Docker setup: `docker-compose up` if applicable
   - Verify project runs locally: `npm run dev` or equivalent
7. Set up second project:
   - Follow same steps as first project
   - Document any differences in setup process
8. Review task boards for both projects:
   - Check GitHub Issues, Jira, or project management tool
   - Identify first priority tasks
   - Note task descriptions, requirements, and acceptance criteria
9. Test basic functionality for both projects:
   - Verify authentication works (if applicable)
   - Test main features/endpoints
   - Check database connectivity (if applicable)
10. Document any blockers or setup issues:
    - Create notes file with issues encountered
    - Note missing dependencies or unclear instructions
    - Prepare questions for Lillia if needed

### Resources and Links:
- Email inbox (check for repository invitations)
- GitHub/GitLab repositories (provided by Lillia)
- Project README files
- Lillia's contact (Slack/email for questions)
- Docker documentation (if Docker setup required)
- Node.js/npm documentation (for dependency installation)

### Instructions:
- Start with the project that has clearer setup instructions
- If access not received, contact Lillia immediately
- Document all setup steps for future reference
- If blockers encountered, don't spend more than 30 minutes troubleshooting before asking for help
- Test each project independently before moving to next
- Keep notes on differences between projects for learning

---

## Task 2: Upload CRMS Project - Begin Feature Development (High Priority)

### Steps:
1. Review project repository for issues and feature requests:
   - Check GitHub Issues tab
   - Look for "good first issue" or "help wanted" labels
   - Review open pull requests to understand current work
   - Check project roadmap or milestones
2. Identify quick wins or small improvements:
   - Look for small bug fixes
   - Find UI/UX improvements
   - Identify missing error handling
   - Check for code quality improvements (linting, formatting)
3. Test authentication flow end-to-end:
   - Start backend server: `npm run dev` in root directory
   - Start frontend: `cd client && npm run dev`
   - Ensure API Gateway is running on correct port
   - Ensure Auth Service is running on port 3001
   - Test login with email/password
   - Test Google OAuth login
   - Verify token is stored in localStorage
   - Test protected route access
   - Test token refresh mechanism
   - Test logout functionality
4. Verify file upload functionality:
   - Navigate to media library page
   - Click upload button
   - Select test file(s)
   - Verify upload completes successfully
   - Check file appears in media library
   - Verify file is accessible via public URL
   - Check database record created correctly
5. Check media library browsing:
   - Navigate through folder hierarchy
   - Verify folders display correctly
   - Check assets display with correct metadata
   - Test folder creation
   - Test folder navigation
   - Verify breadcrumb navigation works
6. Select one small improvement to implement:
   - Choose based on complexity and impact
   - Create new branch: `git checkout -b feature/[feature-name]`
   - Implement the change
   - Test locally
   - Commit changes: `git commit -m "feat: [description]"`
7. Prepare for code review:
   - Review own code for quality
   - Ensure follows project's code style
   - Check for any console.logs or debug code
   - Push branch: `git push origin feature/[feature-name]`
   - Create pull request if ready

### Resources and Links:
- Upload CRMS repository: `upload_crms` directory
- GitHub Issues: Repository issues page
- API Gateway: Running on port 3000/4000 (verify in logs)
- Auth Service: Running on port 3001
- Backend API: `http://localhost:1489`
- Frontend: `http://localhost:3000` or configured port
- Postman/Insomnia: For API testing
- Browser DevTools: For frontend debugging

### Instructions:
- Start with smallest, most impactful change to get familiar with codebase
- Test thoroughly before committing
- Follow existing code patterns and style
- Ask questions if unclear about project structure
- Document any assumptions or decisions made
- Keep changes small and focused

---

## Task 3: Lead Gen Analytics - Testing and Documentation (High Priority)

### Steps:
1. Review existing test suite:
   - Open `aggregates.test.js` file
   - Review test structure and patterns
   - Check test coverage report if available: `npm run test:coverage`
   - Identify which aggregation functions still need tests
2. Identify remaining aggregation functions to test:
   - Review `buildDailySnapshots` function
   - Review `buildStepPerformanceDataset` function
   - Review `buildSourceQualityDataset` function
   - Review `buildTeamLoadCapacity` function
   - Review `buildLeadTimelineDetails` function
   - Check for other utility functions that need testing
3. Write unit tests for next priority function:
   - Create test cases for `buildDailySnapshots`:
     - Test with empty data
     - Test with single day data
     - Test with multiple days data
     - Test delta calculations
     - Test edge cases (missing data, null values)
   - Use real production data samples for realistic tests
   - Fix test expectations based on actual outputs
4. Run tests and verify they pass:
   - Run: `npm test`
   - Check for any failing tests
   - Fix any issues found
   - Verify test coverage increased
5. Test export functionality with real data:
   - Open dashboard in browser
   - Navigate to Day Summary table
   - Test Excel export: Click export button, verify file downloads
   - Test PDF export: Click export button, verify file downloads
   - Test CSV export for Team Load table
   - Test PDF export for Country Segmentation
   - Verify exported files contain correct data
   - Check formatting is correct in exported files
6. Verify GitHub Actions integration:
   - Check `.github/workflows/` directory for workflow files
   - Review workflow configuration
   - Test workflow locally if possible: `act` tool or manual trigger
   - Verify snapshot generation script is called correctly
   - Check output directory for generated reports
   - Verify email delivery configuration (if applicable)
7. Document `formatters.js` module usage:
   - Create documentation file: `docs/formatters.md` or add to existing docs
   - Document all exported functions:
     - Function signatures
     - Parameters and return types
     - Usage examples
     - Locale support
   - Add code examples for common use cases
   - Document how to add new formatters
   - Include migration guide for teams using old formatting code
8. Share documentation with team:
   - Commit documentation to repository
   - Share link in team chat/Slack
   - Request feedback from team members
9. Review and optimize test execution time:
   - Run full test suite: `npm test`
   - Measure execution time
   - Identify slow tests
   - Optimize if needed (mock heavy operations, parallel execution)

### Resources and Links:
- Lead Gen Analytics repository
- Test file: `aggregates.test.js`
- Formatters module: `formatters.js`
- Export functions: `app/exports.js`
- GitHub Actions workflows: `.github/workflows/`
- Snapshot script: `reports/generate_snapshot.py`
- Jest documentation: https://jestjs.io/
- Real production data samples

### Instructions:
- Focus on testing critical aggregation functions first
- Use real data samples to catch edge cases
- Document as you go to avoid forgetting details
- Test exports with actual data, not just mock data
- Verify GitHub Actions workflow works before considering complete
- Share documentation early for team feedback

---

## Task 4: Code Quality Improvements (Medium Priority)

### Steps:
1. Review code from new projects (after setup):
   - Open first new project in IDE
   - Browse through main source files
   - Identify code patterns and architecture
   - Note any repeated code patterns
   - Check for existing utility modules
2. Identify opportunities for centralized utilities:
   - Look for repeated formatting code
   - Find duplicate validation logic
   - Identify common transformation functions
   - Check for repeated API call patterns
3. Apply learned patterns where appropriate:
   - Create shared utility modules if needed
   - Extract repeated code into reusable functions
   - Apply DRY (Don't Repeat Yourself) principles
   - Ensure consistent code style
4. Review second new project:
   - Follow same analysis process
   - Compare patterns between projects
   - Note similarities and differences
5. Document architectural decisions:
   - Create notes file: `docs/architecture-notes.md`
   - Document patterns discovered
   - Note best practices observed
   - Record any anti-patterns to avoid
6. Apply patterns to upload_crms if applicable:
   - Review upload_crms codebase
   - Identify if centralized utilities would help
   - Consider creating shared modules if needed
   - Refactor if time permits

### Resources and Links:
- New project repositories (after setup)
- Upload CRMS codebase
- Lead Gen Analytics `formatters.js` as reference
- Code review tools and linters
- Documentation templates

### Instructions:
- Don't over-engineer - only extract utilities if they're used in multiple places
- Follow existing project patterns rather than imposing new ones
- Document decisions for future reference
- Focus on high-impact improvements first

---

## Task 5: Knowledge Consolidation (Medium Priority)

### Steps:
1. Create quick reference guide for upload_crms:
   - Create file: `docs/upload_crms-quick-reference.md`
   - Document project structure:
     - Backend architecture overview
     - Frontend architecture overview
     - Key directories and their purposes
   - Document key workflows:
     - Authentication flow diagram/steps
     - File upload flow
     - Media library browsing flow
   - List important files and their purposes
   - Include common commands (start server, run tests, etc.)
2. Document API Gateway integration patterns:
   - Create file: `docs/api-gateway-patterns.md`
   - Document backend middleware pattern:
     - How to validate tokens via Gateway
     - Error handling approach
     - Request/response flow
   - Document frontend pattern:
     - How to include tokens in requests
     - Automatic token refresh on 401
     - Handling authentication errors
   - Include code examples
   - Note common pitfalls and solutions
3. Document TypeORM patterns and best practices:
   - Create file: `docs/typeorm-patterns.md`
   - Document entity relationships:
     - OneToMany/ManyToOne examples
     - Hierarchical structures (parent-child)
   - Document query patterns:
     - Finding entities with relations
     - Filtering and sorting
   - Note schema synchronization in development
   - Include best practices for production
4. Organize documentation:
   - Create `docs/` directory if it doesn't exist
   - Organize files logically
   - Create index/README in docs directory
   - Link related documents
5. Review and refine documentation:
   - Read through created documents
   - Ensure clarity and completeness
   - Add missing information
   - Fix any errors or unclear sections

### Resources and Links:
- Upload CRMS project structure
- API Gateway codebase (if accessible)
- TypeORM documentation: https://typeorm.io/
- Express middleware documentation
- React authentication patterns
- Existing project documentation

### Instructions:
- Keep documentation concise but complete
- Use code examples to illustrate patterns
- Focus on practical, actionable information
- Update documentation as you learn more
- Share with team if it would be helpful

---

## Task 6: Verify API Gateway Port Configuration (Blocker Mitigation)

### Steps:
1. Check API Gateway logs to confirm actual port:
   - Open terminal where API Gateway is running
   - Look for log message: "API Gateway запущен на порту [PORT]"
   - Note the actual port number
2. Verify port in upload_crms configuration:
   - Open `upload_crms/.env` file
   - Check `API_GATEWAY_URL` value
   - Verify port matches actual Gateway port
   - Open `upload_crms/client/.env` file
   - Check `VITE_API_GATEWAY_URL` value
   - Verify port matches actual Gateway port
3. Update configuration if needed:
   - If ports don't match, update both `.env` files
   - Change to correct port (e.g., `http://localhost:4000/api` if Gateway on 4000)
   - Save files
4. Restart services:
   - Stop backend server (Ctrl+C)
   - Stop frontend server (Ctrl+C)
   - Restart backend: `npm run dev` in root
   - Restart frontend: `cd client && npm run dev`
5. Test connectivity:
   - Try to login via frontend
   - Check browser console for errors
   - Verify API calls go to correct port
   - Test protected routes

### Resources and Links:
- API Gateway terminal/logs
- `upload_crms/.env` file
- `upload_crms/client/.env` file
- Browser DevTools Network tab
- API Gateway repository (if accessible)

### Instructions:
- Always verify actual port from logs, don't assume
- Update both backend and frontend `.env` files
- Restart services after configuration changes
- Test immediately after changes

---

## Task 7: Verify Auth Service Availability (Blocker Mitigation)

### Steps:
1. Check if Auth Service is running:
   - Look for Auth Service terminal window
   - Check for "Server started" or similar message
   - Verify port 3001 is being used
2. Check Auth Service logs for errors:
   - Review terminal output for error messages
   - Look for database connection errors
   - Check for missing environment variables
   - Note any configuration issues
3. Start Auth Service if not running:
   - Navigate to Auth Service repository directory
   - Check for `.env` file with required configuration
   - Install dependencies if needed: `npm install`
   - Start service: `npm run dev`
   - Verify it starts without errors
4. Test Auth Service connectivity:
   - Use Postman or curl to test health endpoint
   - Test: `GET http://localhost:3001/health` (or equivalent)
   - Verify response is successful
5. Test authentication flow:
   - Try login via upload_crms frontend
   - Check if authentication works
   - Verify tokens are generated correctly
   - Test token validation

### Resources and Links:
- Auth Service repository (aus-users-service or similar)
- Auth Service terminal/logs
- Postman/curl for testing
- `upload_crms` frontend for integration testing
- Auth Service README/documentation

### Instructions:
- Auth Service must be running for authentication to work
- Check logs first before restarting
- Verify all required environment variables are set
- Test connectivity before assuming it's working

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
