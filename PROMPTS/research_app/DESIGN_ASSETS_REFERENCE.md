# Research App - Design Assets Reference

## Overview

The Research App prompts now integrate the **AdminRHS-AI-Catalog** design system created by Eleonora Safonova from the Design Department.

---

## 🎨 Design System Location

**Source**: `Nov25/Design Nov25/Safonova Eleonora/AdminRHS-AI-Catalog-4/remake AI Catalog/`

### Directory Structure

```
remake AI Catalog/
├── index.html          # Complete UI implementation (116KB)
├── js/icons/           # 12 SVG icons (ready to use)
├── logo/               # Department logos (designer, developer, manager, etc.)
├── mascots/            # Character illustrations (13 PNG files)
├── photo/              # App icons (ChatGPT, Claude, Gemini, etc.)
└── photo-light/        # Light mode app icons
```

---

## Available Icons (SVG)

### Location: `js/icons/`

| Icon | File | Use Case in Research App |
|------|------|-------------------------|
| 🔍 Search | `search.svg` | Search bar, video search |
| 🔽 Filter | `filter.svg` | Filter panels, dropdown menus |
| ☁️ Upload | `upload.svg` | Transcription file upload |
| ✏️ Edit | `edit.svg` | Edit video details, modify prompts |
| ➕ Create | `create.svg` | Add new video/search |
| 🤖 AI | `ai.svg` | AI processing indicators |
| ⚡ Lightning | `lightning.svg` | Quick actions, priority items |
| 💎 Diamond | `diamond.svg` | Premium features |
| 🔒 Lock | `lock.svg` | Permissions, restricted content |
| 🌙 Moon | `moon.svg` | Dark mode toggle |
| ☀️ Sun | `sun.svg` | Light mode toggle |
| ✓ Check | `acc.svg` | Completed status |

### Icon Implementation Example

```html
<!-- Search Icon -->
<svg width="24" height="24" viewBox="0 0 24 24" fill="none">
  <path d="M11 18C14.866 18 18 14.866 18 11C18 7.13401 14.866 4 11 4C7.13401 4 4 7.13401 4 11C4 14.866 7.13401 18 11 18Z" stroke="#6A8EA9" stroke-width="2"/>
  <path d="M20 20L17 17" stroke="#6A8EA9" stroke-width="2" stroke-linecap="round"/>
</svg>
```

---

## Color System

### CSS Variables (Light Mode)

```css
:root {
  --background: #f5f5f5;
  --foreground: #2d465d;          /* Soft cool black */
  --card: #ffffff;
  --card-foreground: #2a4054;
  --border: rgba(0, 0, 0, 0.08);
  --muted-foreground: #3d5268;    /* Secondary text */
  --destructive: #d4183d;
  --accent-blue: #428eb4;
  --accent-blue-hover: #28749b;
  --accent-blue-light: #83CBFF;
  --badge-freemium-icon: #F59E0B; /* Yellow */
  --badge-paid-icon: #DC2626;     /* Red */
  --badge-free-icon: #16A34A;     /* Green */
}
```

### CSS Variables (Dark Mode)

```css
.dark {
  --background: #1a1a1a;
  --foreground: #e0e0e0;
  --card: #2d2d2d;
  --card-foreground: #e0e0e0;
  --border: rgba(248, 62, 62, 0.1);
  --muted-foreground: #b0b0b0;
  --badge-freemium-icon: #FCD34D;
  --badge-paid-icon: #F87171;
  --badge-free-icon: #86EFAC;
}
```

### Research App Phase Colors

```css
/* Extend with phase-specific colors */
--phase-0: #9CA3AF;  /* Gray - Search */
--phase-1: #60A5FA;  /* Blue - Transcription */
--phase-2: #34D399;  /* Green - Extraction */
--phase-3: #FBBF24;  /* Yellow - Gap Analysis */
--phase-4: #F97316;  /* Orange - Integration */
--phase-5: #A78BFA;  /* Purple - Mapping */
--complete: #10B981; /* Emerald - Complete */
```

---

## UI Component Patterns

### 1. Header Design

```css
.header {
  width: 100%;
  height: 90px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 48px;
  box-shadow: 0 10px 15px -3px rgba(0,0,0,0.08);
  background: linear-gradient(135deg, #e8f2ff 0%, #f5f3ff 35%, #ecf6ff 70%, #fdfbff 100%);
}

.header-title h1 {
  font-size: 56px;
  font-weight: 800;
  background: linear-gradient(100deg, #7cafe6 0%, #6e92c2 30%, #a391f0 70%, #869ee1 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}
```

**Adapt for Research App**:
- Title: "Research Management System"
- Subtitle: "Queue Management" or "Video Processing"

### 2. Search Bar

```css
.search-input {
  width: 100%;
  max-width: 250px;
  padding: 10px 16px 10px 40px;
  font-size: 15.2px;
  height: 42px;
  border-radius: 10px;
  transition: width 0.3s ease;
}

.search-input:focus {
  width: 100%;
  max-width: 350px; /* Expands on focus */
}
```

**Adapt for Research App**:
- Search videos by title, channel, topic
- Search queue items by keywords

### 3. Filter Panel (Collapsible Left-Side)

**Key Features**:
- Collapsible panel with toggle button
- Multi-select pill buttons
- Active filters display with removable tags
- "Clear All" button (enabled only when filters active)

**HTML Structure** (from `index.html`):

```html
<div class="filter-panel">
  <button class="filter-toggle">
    <svg><!-- filter icon --></svg>
  </button>

  <div class="filter-groups">
    <div class="filter-group">
      <button class="group-title">Category</button>
      <div class="group-options">
        <button class="pill-button">AI Assistant</button>
        <button class="pill-button">Automation</button>
      </div>
    </div>
  </div>

  <div class="active-filters">
    <span class="filter-tag">Free <button>×</button></span>
  </div>
</div>
```

**Adapt for Research App**:

**Queue Management App Filters**:
- Status: Pending, Selected, Transcribing, Parsed, Completed
- Department: VID, AID, HRM, FIN, MKT, ALL
- Priority: High, Medium, Low
- Date Range: Last 7 days, Last 30 days, All time

**Video Processing App Filters**:
- Phase: 0, 1, 2, 3, 4, 5, Complete
- Status: Not Started, In Progress, Completed, Failed
- Employee: Filter by assigned employee

### 4. Card Layout (Expandable)

```css
.card {
  background: var(--card);
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  transition: all 0.3s ease;
}

.card:hover {
  box-shadow: 0 8px 20px rgba(66, 142, 180, 0.2); /* Blue shadow */
}
```

**Interaction**:
- Click on card title to expand
- "+N more" button reveals additional items
- Smooth expand/collapse animation

**Adapt for Research App**:
- Video queue items as cards
- Phase progress cards with status indicators
- Search queue items with expandable details

### 5. Button Styles

```css
.pill-button {
  padding: 8px 16px;
  border-radius: 20px;
  border: 1px solid var(--border);
  background: transparent;
  transition: all 0.2s ease;
}

.pill-button.selected {
  background: var(--accent-blue);
  color: white;
  border-color: var(--accent-blue);
}

.pill-button:hover {
  background: var(--accent-blue-light);
  border-color: var(--accent-blue);
}
```

---

## Typography

### Font Stack

```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif;
```

### Typography Hierarchy

| Element | Size | Weight | Use Case |
|---------|------|--------|----------|
| H1 (Page Title) | 56px | 800 | "AI Catalog", "Research Management" |
| H2 (Section) | 32px | 700 | Section headers |
| H3 (Card Title) | 20px | 600 | Video titles, card headers |
| Body | 16px | 400 | General text |
| Small | 14px | 400 | Metadata, descriptions |
| Caption | 12px | 400 | Labels, timestamps |

---

## Custom Scrollbar

```css
::-webkit-scrollbar {
  width: 10px;
  height: 10px;
}

::-webkit-scrollbar-track {
  background: var(--background);
}

::-webkit-scrollbar-thumb {
  background-color: #0096E1;
  border-radius: 20px;
  border: 2px solid var(--background);
}

::-webkit-scrollbar-thumb:hover {
  background-color: #00aaff;
}
```

---

## Animation & Transitions

### Smooth Transitions

```css
/* Panel open/close */
.filter-panel {
  transition: transform 0.3s ease, opacity 0.3s ease;
}

/* Hover effects */
.card, .button {
  transition: all 0.2s ease;
}

/* Search bar expand */
.search-input {
  transition: width 0.3s ease;
}
```

---

## Integration Instructions

### For AI Builders (Lovable, v0, Cursor)

1. **Copy Color Variables**
   - Use CSS variables from AdminRHS-AI-Catalog
   - Add phase-specific colors for Research App

2. **Import SVG Icons**
   - Copy icon SVGs from `js/icons/` folder
   - Use as inline SVG or create React components

3. **Adapt UI Patterns**
   - Filter panel → Video/Search filtering
   - Card layout → Queue items display
   - Search bar → Video/queue search

4. **Maintain Consistency**
   - Same border-radius: 10-12px
   - Same shadows: `0 2px 8px rgba(0,0,0,0.05)`
   - Same spacing: 16-24px padding
   - Same hover effects: Blue shadow on cards

---

## Example: Queue Management Dashboard

```typescript
// Header with gradient title (from AdminRHS-AI-Catalog)
<header className="bg-gradient-to-r from-blue-50 via-purple-50 to-blue-50 h-[90px] flex items-center justify-between px-12 shadow-lg">
  <h1 className="text-5xl font-extrabold bg-gradient-to-r from-[#7cafe6] via-[#6e92c2] to-[#a391f0] bg-clip-text text-transparent">
    Research Queue Management
  </h1>

  <div className="flex items-center gap-4">
    {/* Search bar with icon (from AdminRHS-AI-Catalog) */}
    <div className="relative">
      <svg className="absolute left-3 top-3 w-5 h-5 text-[#6A8EA9]">
        {/* search.svg */}
      </svg>
      <input
        type="text"
        placeholder="Search videos..."
        className="pl-10 pr-4 py-2 w-64 focus:w-80 transition-all duration-300 rounded-lg border border-gray-200"
      />
    </div>

    {/* Dark mode toggle */}
    <button className="p-2 rounded-lg hover:bg-gray-100">
      <svg>{/* moon.svg or sun.svg */}</svg>
    </button>
  </div>
</header>
```

---

## Resources

### Design Files

- **Main HTML**: `index.html` (116KB - complete implementation)
- **Icons Folder**: `js/icons/` (12 SVG files)
- **Implementation Notes**: `remake prompts.md` (design iteration history)

### Design Department Contact

- **Designer**: Eleonora Safonova
- **Department**: Design Nov25
- **Project**: AdminRHS-AI-Catalog-4

---

## Quick Reference

### Most Used Icons for Research App

| Component | Icon | Path |
|-----------|------|------|
| Search Bar | 🔍 | `js/icons/search.svg` |
| Upload Zone | ☁️ | `js/icons/upload.svg` |
| Filter Panel | 🔽 | `js/icons/filter.svg` |
| AI Processing | 🤖 | `js/icons/ai.svg` |
| Quick Actions | ⚡ | `js/icons/lightning.svg` |
| Edit Button | ✏️ | `js/icons/edit.svg` |

### Color Quick Reference

| Use Case | Light Mode | Dark Mode |
|----------|-----------|-----------|
| Background | `#f5f5f5` | `#1a1a1a` |
| Card | `#ffffff` | `#2d2d2d` |
| Primary Text | `#2d465d` | `#e0e0e0` |
| Accent Blue | `#428eb4` | `#83CBFF` |
| Phase 2 (Extract) | `#34D399` | `#34D399` |
| Phase 3 (Analyze) | `#FBBF24` | `#FBBF24` |

---

**End of Design Assets Reference**
