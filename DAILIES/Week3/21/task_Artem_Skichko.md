# Task Breakdown - [22.11.2025]

## Instructions
**What**: Detailed action steps
**Include**:
- Break each plan item into specific steps
- Add links and resources
- Clear instructions for execution

---

## Task 1: Upload CRMS - Test and Refine isPublic System

### Steps:
1. **Test Public File Access (Unauthenticated)**
   - Open browser in incognito/private mode (no auth token)
   - Navigate to MediaLibrary
   - Verify public files (isPublic: true) load correctly
   - Check browser console for errors
   - Verify images display using direct URL (`<img src>`)

2. **Test Private File Access (Authenticated)**
   - Login to the application
   - Navigate to MediaLibrary
   - Verify private files (isPublic: false) load correctly
   - Check that files are loaded via fetch with Authorization header
   - Verify blob URLs are created and displayed correctly
   - Check browser console for blob URL creation logs

3. **Test Private File Access (Unauthenticated)**
   - Open browser in incognito mode
   - Try to access a private file directly via URL
   - Verify 401 Unauthorized response is returned
   - Check error message is clear and helpful

4. **Test Edge Cases**
   - Test with expired JWT token (wait for expiration or manually expire)
   - Test with invalid JWT token (corrupted token)
   - Test with network failure (disable network, try to load private file)
   - Test with missing token (null/undefined in localStorage)
   - Verify proper error handling for each case

5. **Verify Blob URL Cleanup**
   - Open browser DevTools → Memory tab
   - Load multiple private files
   - Close/unmount components
   - Check for memory leaks (blob URLs should be revoked)
   - Verify `URL.revokeObjectURL()` is called in cleanup

6. **Test File Upload with isPublic**
   - Upload new file without specifying isPublic (should default to true)
   - Upload new file with isPublic: false
   - Verify both cases work correctly
   - Check database to confirm isPublic value is saved

7. **Test Update isPublic via UI**
   - Open EditAssetModal for existing file
   - Toggle between Public/Private
   - Save changes
   - Verify change persists after page refresh
   - Check database to confirm update

8. **Test Windows Path Handling**
   - Verify files uploaded on Windows display correctly
   - Check that extractFileName handles backslashes
   - Verify no double paths in URLs
   - Test with various path formats

### Resources and Links:
- Project: `upload_crms`
- Backend: `src/controllers/uploads.ts` (sendMediaFile)
- Backend: `src/middlewares/auth.ts` (optionalAuthenticateToken)
- Frontend: `client/src/services/api.js` (fetchPrivateMediaFile, getMediaFileUrl)
- Frontend: `client/src/components/AssetItem.jsx`
- Frontend: `client/src/components/EditAssetModal.jsx`
- Database: Check `assets` table for `isPublic` column

### Instructions:
- Start with basic functionality tests (public/private access)
- Use browser DevTools Network tab to verify API calls
- Use browser DevTools Console to check for errors
- Use browser DevTools Memory tab to check for leaks
- Document any issues found in daily.md
- Test on different browsers (Chrome, Firefox, Edge)

---

## Task 2: Upload CRMS - Remove Diagnostic Logging

### Steps:
1. **Locate Diagnostic Logs**
   - Open `client/src/services/api.js`
   - Find `fetchPrivateMediaFile` function
   - Locate all `console.log` statements with debug information

2. **Review Logs**
   - Check what information is being logged
   - Determine if any logs are still needed for production
   - Identify logs that should be removed

3. **Remove or Replace Logs**
   - Remove unnecessary console.log statements
   - Replace with proper error logging if needed
   - Consider using a logging library for production (optional)

4. **Test After Removal**
   - Verify functionality still works without logs
   - Check browser console is clean (no debug logs)
   - Ensure error handling still works correctly

### Resources and Links:
- File: `upload_crms/client/src/services/api.js`
- Function: `fetchPrivateMediaFile` (around line 151-245)

### Instructions:
- Keep error logging (console.error) for production debugging
- Remove only debug/informational logs
- Test thoroughly after removal

---

## Task 3: Dashboard Project - Review Performance Metrics

### Steps:
1. **Access Performance Metrics**
   - Open Dashboard application
   - Check if `getPerfMetrics()` function is accessible
   - Call `getPerfMetrics()` in browser console
   - Review collected Core Web Vitals data

2. **Document Baseline Metrics**
   - Record FCP (First Contentful Paint) value
   - Record LCP (Largest Contentful Paint) value
   - Record CLS (Cumulative Layout Shift) value
   - Record FID (First Input Delay) value
   - Note the timestamp and conditions

3. **Compare with Previous Performance**
   - If available, compare with metrics before optimizations
   - Identify improvements or regressions
   - Document findings

4. **Create Performance Report**
   - Create a simple document or note with metrics
   - Include date, browser, and conditions
   - Note any concerns or areas for improvement

5. **Set Up Monitoring (Optional)**
   - Consider setting up automated performance monitoring
   - Research tools for Core Web Vitals tracking
   - Document recommendations

### Resources and Links:
- Project: Dashboard project
- File: `src/lib/perf-metrics.ts`
- Function: `getPerfMetrics()`
- Browser DevTools: Performance tab, Lighthouse

### Instructions:
- Run performance test on clean browser (no extensions)
- Test on same network conditions if possible
- Document all metrics for future comparison
- Use Lighthouse for additional performance insights

---

## Task 4: Dashboard Project - Verify Cache Performance

### Steps:
1. **Test Cache Functionality**
   - Open Dashboard application
   - Open browser DevTools → Application → Local Storage
   - Check for cached data entries
   - Verify TTL (Time To Live) is working (5 minutes)

2. **Test Cache Invalidation**
   - Make a change (add/edit/delete employee or card)
   - Verify cache is cleared after mutation
   - Check localStorage is updated correctly

3. **Test Stale-While-Revalidate**
   - Load dashboard (should use cached data immediately)
   - Check Network tab for background refresh
   - Verify UI doesn't block while cache refreshes
   - Verify fresh data appears after background update

4. **Test Network Failure Handling**
   - Disable network (DevTools → Network → Offline)
   - Try to load dashboard
   - Verify stale data from cache is used
   - Re-enable network and verify refresh works

5. **Review Cache TTL**
   - Consider if 5 minutes is optimal
   - Test with different TTL values if needed
   - Document findings

### Resources and Links:
- Project: Dashboard project
- File: `src/frontend-api.ts`
- Browser DevTools: Application → Local Storage, Network tab

### Instructions:
- Use browser DevTools to inspect cache behavior
- Test various scenarios (normal, offline, mutations)
- Document cache hit/miss rates if possible

---

## Task 5: Lead Gen Analytics - Add Keyboard Navigation to Modals

### Steps:
1. **Add ESC Key Handler**
   - Open `app/modals.js`
   - Find `showChartTooltipModal` function
   - Add event listener for 'keydown' event
   - Check if key is 'Escape' (key === 'Escape' || keyCode === 27)
   - Call close modal function if ESC is pressed

2. **Add Focus Management**
   - When modal opens, focus on first interactive element (or modal itself)
   - When modal closes, return focus to trigger element
   - Add `tabindex` attributes as needed

3. **Add ARIA Attributes**
   - Add `role="dialog"` to modal
   - Add `aria-modal="true"`
   - Add `aria-labelledby` pointing to modal title
   - Add `aria-describedby` pointing to modal content

4. **Test Keyboard Navigation**
   - Test ESC key closes modal
   - Test Tab key navigates through modal elements
   - Test Shift+Tab for reverse navigation
   - Test Enter/Space on buttons
   - Verify focus is trapped within modal

5. **Test with Screen Reader (Optional)**
   - Use browser screen reader (Chrome: ChromeVox, Firefox: NVDA)
   - Verify modal is announced correctly
   - Verify content is readable

### Resources and Links:
- Project: lead_gen_analytics
- File: `app/modals.js`
- File: `index.html` (modal structure)
- MDN: Keyboard navigation patterns
- WAI-ARIA: Dialog pattern

### Instructions:
- Start with ESC key (most important)
- Add ARIA attributes for accessibility
- Test thoroughly with keyboard only (no mouse)
- Document any issues

---

## Task 6: Lead Gen Analytics - Test Modal Responsiveness

### Steps:
1. **Test on Different Screen Sizes**
   - Open Dashboard in browser
   - Use DevTools → Toggle device toolbar
   - Test on mobile (375px, 414px)
   - Test on tablet (768px, 1024px)
   - Test on desktop (1920px)

2. **Verify Modal Sizing**
   - Check modal width is appropriate for each screen size
   - Verify modal doesn't overflow viewport
   - Check modal is centered correctly
   - Verify content is readable on all sizes

3. **Test Touch Interactions**
   - On mobile device or emulator, test tapping chart elements
   - Verify modal opens correctly
   - Test closing modal via buttons
   - Test closing modal via overlay tap

4. **Test Dark Theme on Mobile**
   - Verify dark theme works on mobile
   - Check text contrast is good
   - Verify modal is readable

5. **Document Issues**
   - Note any responsive design issues
   - Create list of improvements needed
   - Prioritize fixes

### Resources and Links:
- Project: lead_gen_analytics
- File: `index.html` (modal CSS classes)
- Browser DevTools: Device toolbar
- CSS: `chart-tooltip-modal` class

### Instructions:
- Use browser DevTools device emulation
- Test on actual mobile device if possible
- Document all responsive issues found

---

## Task 7: Code Quality - Review and Update Documentation

### Steps:
1. **Review Upload CRMS Documentation**
   - Check `upload_crms/README.md`
   - Update with isPublic feature information
   - Document API changes
   - Add migration guide for existing files

2. **Review Dashboard Documentation**
   - Check Dashboard project README
   - Document performance optimizations
   - Document new modular architecture
   - Add setup instructions if missing

3. **Create API Documentation**
   - Document isPublic parameter in upload endpoints
   - Document isPublic in update endpoint
   - Document optional authentication for media files
   - Add examples if needed

4. **Update Code Comments**
   - Add JSDoc comments to new functions
   - Update existing comments if needed
   - Ensure complex logic is explained

### Resources and Links:
- `upload_crms/README.md`
- Dashboard project README
- API endpoints documentation

### Instructions:
- Keep documentation concise but complete
- Include examples where helpful
- Update as you work, don't leave for end of day

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
