# 📋 Implementation Plan - Discord Server Restructure

## 🎯 Overview

This document provides a step-by-step plan to implement the recommended Discord server improvements.

**Estimated Time:** 2-4 hours (depending on testing and rollback considerations)
**Risk Level:** Low-Medium
**Reversibility:** High (all changes can be undone)

---

## ✅ Pre-Implementation Checklist

Before starting:

- [ ] **Backup complete** - Run export script or manual backup
- [ ] **Stakeholder approval** - Get sign-off from server owner and department leads
- [ ] **Communication sent** - Announce changes to server members
- [ ] **Test environment ready** (optional) - Create test category for dry run
- [ ] **Moderators briefed** - Train team on new structure
- [ ] **Rollback plan ready** - Document how to undo changes
- [ ] **Timing confirmed** - Schedule during low-activity period

---

## 📅 Implementation Phases

### Phase 1: Quick Wins (30-45 minutes)

**Goal:** Low-risk improvements with immediate impact

#### 1.1 Standardize Channel Naming ⏱️ 15 min

**Action:** Rename channels to use hyphens consistently

**Channels to rename:**

```
HR Category:
- hr_main → hr-main
- hr_reports → hr-reports
- hr_crm → hr-crm
- hr_refusal → hr-refusal
- hr_plans → hr-plans

Sales Category:
- sale_main → sale-main
- sales_calls_summary → sales-calls-summary

Admin Category:
- admin_reports → admin-reports
```

**Steps:**
1. Right-click channel → Edit Channel
2. Change name (replace _ with -)
3. Save
4. Verify no broken integrations/bots

**Rollback:** Simple rename back to original

---

#### 1.2 Create Archive Category ⏱️ 5 min

**Action:** Add category at bottom of server for future use

**Steps:**
1. Right-click in channel list → Create Category
2. Name: `📦 Archive`
3. Position at bottom (below srv-log)
4. Lock permissions (everyone: view=off, send=off)

**Purpose:** Ready for archiving unused channels later

---

#### 1.3 Optimize Channel Order ⏱️ 15 min

**Action:** Standardize order within each category (text first, then voice)

**Do for each category:**
1. Drag channels to reorder
2. Standard order: info → main chat → specialized text → voice

**Example: HR Category**
```
1. hr-main (main chat)
2. hr-reports (specialized)
3. hr-crm (specialized)
4. hr-refusal (specialized)
5. hr-plans (specialized)
6. hr-courses (specialized)
7. presale (specialized)
8. HR FM (voice)
9. Conference room (voice)
```

---

### Phase 2: Structural Changes (60-90 minutes)

**Goal:** Reorganize categories and channels

⚠️ **Important:** Test each change before proceeding to next

#### 2.1 Merge Inner Client into Admin ⏱️ 5 min

**Action:** Move single channel to Admin category

**Steps:**
1. Drag `#🕸️oa-y` from "Inner Client" to "💬Admin" category
2. Position near bottom of Admin channels
3. Verify permissions maintained
4. Delete empty "Inner Client" category

**Rollback:** Recreate category and move channel back

---

#### 2.2 Dissolve Projects Category ⏱️ 20 min

**Action:** Distribute voice channels to respective departments

**Channel Movements:**

```
Finance Projects → 💰Finance
   - Position below "Finance Main" voice channel

Video Projects → 🎨Designers
   - Position in voice section

Designers Projects → 🎨Designers
   - Position in voice section (next to Video Projects)

LG Projects → 🎯Lead Generation
   - Position after LG Training voice

SMM Projects → 📈Sales
   - Position after project-sales voice

T-C-Alliance FM → 💬Admin (or appropriate category)
   - Determine best fit with team
```

**Steps for each channel:**
1. Click and drag voice channel to target category
2. Position appropriately
3. Verify permissions (should inherit from category)
4. Test access with regular member account

**After all moved:**
1. Verify "📂Projects" is empty
2. Delete category

**Rollback:** Recreate Projects category and move channels back

---

#### 2.3 Consolidate Training Rooms ⏱️ 30 min

**Option A: Merge Categories (Recommended)**

**Steps:**
1. Rename "🚀Onboarding" → "📚Learning & Onboarding"
2. Move Learning Hub text channels to renamed category:
   - 🎩our-mentors
   - general-info
   - 🧩discussions-room
3. Consolidate voice rooms:
   - Keep: Training Room 1, Training Room 2
   - Rename: Learning Room 1 → Study Hall
   - Archive: Training Room 3, Learning Room 2, Learning Room 3
4. Reorganize order:
   - Text channels first
   - Voice channels last
5. Delete empty "📚Learning Hub" category

**Final Structure:**
```
📚Learning & Onboarding
├── 📸selfie (text)
├── 🤝onboarding-chat (text)
├── 📊reports (text)
├── 🎩our-mentors (text)
├── general-info (text)
├── 🧩discussions-room (text)
├── Training Room 1 (voice)
├── Training Room 2 (voice)
└── Study Hall (voice)
```

**Option B: Keep Separate** (Alternative)

**Steps:**
1. Archive: Training Room 3, Learning Room 3
2. Rename categories for clarity:
   - "🚀Onboarding" → "🚀New Employee Onboarding"
   - "📚Learning Hub" → "📚Ongoing Education"

**Rollback:** Recreate original categories, move channels back, restore from archive

---

### Phase 3: Advanced Optimization (60+ minutes)

**Goal:** Implement dynamic voice channels

⚠️ **Note:** This phase is optional and can be done later

#### 3.1 Set Up Voice Channel Bot ⏱️ 30 min

**Recommended Bot:** AutoVoice (https://autovoice.xyz/)

**Steps:**
1. Go to https://autovoice.xyz/
2. Click "Invite" and select your server
3. Grant required permissions
4. Go to server → type `/setup`
5. Follow bot setup wizard:
   - Create "Join to Create" channel in Lead Generation
   - Set template: "LG Team {number}"
   - Set auto-delete timer: 5 minutes after empty
   - Set user limit: 10 (optional)

**Alternative Bots:**
- Voice Master: https://voicemaster.xyz/
- Tempvoice: https://tempvoice.xyz/

---

#### 3.2 Replace Static LG Voice Channels ⏱️ 20 min

**Action:** Archive color-coded rooms, implement dynamic system

**Steps:**
1. Keep permanent channels:
   - 📢LG FM
   - 📢LG Admin
   - 🏛️LG Training
2. Archive color-coded channels:
   - ⬜LG White → Move to Archive
   - 🟥LG Red → Move to Archive
   - 🟫 LG Brown → Move to Archive
   - 🟦 LG Blue → Move to Archive
3. Create new "Join to Create" channel (via bot):
   - Name: ➕ Join to Create LG Room
   - Position below LG Training

**Test:**
1. Join "Join to Create" channel
2. Verify new room is created
3. Leave room
4. Wait 5 minutes, verify auto-deletion

**Rollback:** Restore channels from archive if bot doesn't work as expected

---

#### 3.3 Team Training ⏱️ 15 min

**Action:** Brief LG team on new voice system

**Communication:**
```
📢 @Lead Generation Team

New voice channel system:

✅ Join "➕ Join to Create LG Room"
✅ Private room auto-created for you
✅ Invite team members as needed
✅ Room auto-deletes 5 min after empty

Questions? Ask in #lg-hub
```

---

## 📢 Communication Plan

### Before Implementation

**1 Week Before:**
```
📢 @everyone

Server restructure scheduled for [DATE] at [TIME]

Changes:
• Better organization (fewer categories)
• Consistent naming
• Dynamic voice channels for LG team

Expected downtime: ~30 minutes
Details: [link to announcement channel]
```

**1 Day Before:**
```
⏰ Reminder: Server restructure tomorrow at [TIME]
Bookmark any important channels - some will move!
```

### During Implementation

**Start:**
```
🔧 Server restructure in progress...
Please don't create new channels during this time.
ETA: 30-60 minutes
```

**After Each Phase:**
```
✅ Phase [X] complete
- [List of changes]
- [Next phase starting...]
```

### After Implementation

**Completion:**
```
✅ Restructure complete!

What changed:
• [List major changes]
• [Provide updated server map]

Issues? Report in #admin-chat
Feedback? Let us know in #[feedback-channel]

Thanks for your patience! 🎉
```

**1 Week Later:**
```
📊 Restructure feedback check-in

How's the new structure working?
React: 👍 Great | 😐 OK | 👎 Issues

Share details in replies ⬇️
```

---

## 🔄 Rollback Plan

If critical issues occur:

### Quick Rollback (Undo Last Change)

**For moved channel:**
1. Drag back to original category
2. Restore original position

**For renamed channel:**
1. Edit → restore original name

**For deleted category:**
1. Create category with original name
2. Restore channels from archive

### Full Rollback (Nuclear Option)

**If using Discord bot:**
1. Use backup JSON file
2. Run restore script (if available)

**Manual full rollback:**
1. Stop all changes
2. Reference `exported/current-structure/`
3. Recreate structure manually
4. Takes 2-4 hours depending on extent of changes

---

## ✅ Post-Implementation Checklist

After all changes:

- [ ] **Test navigation** - Can you find all channels?
- [ ] **Verify permissions** - Check with different roles
- [ ] **Test bots** - Ensure integrations still work
- [ ] **Check pins/bookmarks** - Update if needed
- [ ] **Update documentation** - Server map, onboarding guides
- [ ] **Collect feedback** - Ask team for issues
- [ ] **Monitor activity** - Watch for confusion/questions
- [ ] **Update backups** - Export new structure

---

## 📊 Success Metrics

Measure after 2 weeks:

1. **User Feedback** (survey)
   - Target: 4+ stars average

2. **Channel Activity**
   - Compare message counts pre/post
   - Target: Maintained or increased

3. **Voice Usage**
   - LG dynamic channels: track creation count
   - Target: 5+ rooms created per day

4. **Support Questions**
   - "Where is X channel?" tickets
   - Target: 50% reduction

5. **Navigation Time** (optional user test)
   - Time to find specific channel
   - Target: 20% faster

---

## 🆘 Troubleshooting

### Issue: Bot can't move channels
**Solution:** Check bot has "Manage Channels" permission

### Issue: Members can't find moved channels
**Solution:**
- Post updated server map
- Use search function
- Pin announcements in main channels

### Issue: Permissions broken after move
**Solution:**
- Channels inherit category permissions
- Manually fix: Right-click → Edit → Permissions

### Issue: Voice bot not working
**Solution:**
- Check bot has "Manage Channels" permission
- Try `/setup` again
- Contact bot support
- Rollback to static channels temporarily

---

## 📚 Additional Resources

- Discord Server Setup Guide: https://support.discord.com/hc/en-us/articles/206143407
- Channel Organization: https://discord.com/moderation
- AutoVoice Docs: https://docs.autovoice.xyz/
- Backup Script: `scripts/export-structure/`

---

**Document Version:** 1.0.0
**Last Updated:** 2025-12-10
**Status:** Ready for Implementation
**Approved By:** [Pending]
