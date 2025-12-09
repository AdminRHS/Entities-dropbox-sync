# DESIGN SYSTEM - CSS VARIABLES REFERENCE

**Created:** 2025-12-08
**Version:** 1.0
**Source:** https://adminrhs.github.io/Design-system/
**Purpose:** Quick reference for all CSS variables from the Design System

---

## 📋 OVERVIEW

This document contains all CSS custom properties (variables) extracted from the official Design System v1.0 (October 2025). Use these variables consistently across the entire RESEARCHES 2 application to maintain design consistency.

**Reference:** https://adminrhs.github.io/Video-catalog/

---

## 🎨 COLOR SYSTEM

### Background Colors

#### Light Theme
```css
:root {
  --bg-default: #f7fafc;      /* Default page background */
  --bg-paper: #ffffff;        /* Paper/White surface */
  --bg-secondary: #ffffff;    /* Cards, modals */
  --bg-tertiary: #edf2f7;     /* Hover states, subtle backgrounds */
}
```

#### Dark Theme
```css
[data-theme="dark"] {
  --bg-default: #1a202c;      /* Default page background */
  --bg-paper: #1f2937;        /* Paper surface */
  --bg-secondary: #1f2937;    /* Cards, modals */
  --bg-tertiary: #374151;     /* Hover states */
}
```

---

### Text Colors

#### Light Theme
```css
:root {
  --text-primary: #2d3748;    /* Primary text (headings, body) */
  --text-secondary: #718096;  /* Secondary text (labels, descriptions) */
  --text-tertiary: #a0aec0;   /* Tertiary text (metadata, timestamps) */
}
```

#### Dark Theme
```css
[data-theme="dark"] {
  --text-primary: #f7fafc;    /* Primary text */
  --text-secondary: #cbd5e0;  /* Secondary text */
  --text-tertiary: #9ca3af;   /* Tertiary text */
}
```

---

### Border Colors

#### Light Theme
```css
:root {
  --border-color: #e0e0e0;    /* Default borders */
  --border-hover: #cbd5e0;    /* Border on hover */
}
```

#### Dark Theme
```css
[data-theme="dark"] {
  --border-color: #4a5568;    /* Default borders */
  --border-hover: #718096;    /* Border on hover */
}
```

---

### Shadow System

#### Light Theme
```css
:root {
  --shadow-light: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-card: 0 2px 8px rgba(0, 0, 0, 0.10);
  --shadow-medium: 0 4px 12px rgba(0, 0, 0, 0.15);
  --shadow-heavy: 0 10px 30px rgba(0, 0, 0, 0.15);
  --shadow-inset: inset 0 2px 4px rgba(0, 0, 0, 0.06);
}
```

#### Dark Theme
```css
[data-theme="dark"] {
  --shadow-light: 0 1px 2px 0 rgba(0, 0, 0, 0.3);
  --shadow-card: 0 2px 8px rgba(0, 0, 0, 0.4);
  --shadow-medium: 0 4px 12px rgba(0, 0, 0, 0.5);
  --shadow-heavy: 0 10px 30px rgba(0, 0, 0, 0.6);
}
```

---

## 🎨 SEMANTIC COLORS

### Primary (Blue)

#### Light Theme
```css
:root {
  --color-primary-default: #2563EB;
  --color-primary-hover: #3B82F6;
  --color-primary-active: #1D4ED8;
}
```

#### Dark Theme
```css
[data-theme="dark"] {
  --color-primary-default: #3B82F6;
  --color-primary-hover: #60A5FA;
  --color-primary-active: #2563EB;
}
```

---

### Secondary (Gray)

#### Light Theme
```css
:root {
  --color-secondary-default: #6B7280;
  --color-secondary-hover: #9CA3AF;
  --color-secondary-active: #4B5563;
}
```

#### Dark Theme
```css
[data-theme="dark"] {
  --color-secondary-default: #9CA3AF;
  --color-secondary-hover: #D1D5DB;
  --color-secondary-active: #6B7280;
}
```

---

### Success (Green)

#### Light Theme
```css
:root {
  --color-success-default: #16A34A;
  --color-success-hover: #22C55E;
  --color-success-active: #15803D;
}
```

#### Dark Theme
```css
[data-theme="dark"] {
  --color-success-default: #22C55E;
  --color-success-hover: #4ADE80;
  --color-success-active: #16A34A;
}
```

---

### Tertiary (Purple)

#### Light Theme
```css
:root {
  --color-tertiary-default: #A855F7;
  --color-tertiary-hover: #C084FC;
  --color-tertiary-active: #9333EA;
}
```

#### Dark Theme
```css
[data-theme="dark"] {
  --color-tertiary-default: #C084FC;
  --color-tertiary-hover: #D8B4FE;
  --color-tertiary-active: #A855F7;
}
```

---

### Warning (Orange)

#### Light Theme
```css
:root {
  --color-warning-default: #F97316;
  --color-warning-hover: #FB923C;
  --color-warning-active: #EA580C;
}
```

#### Dark Theme
```css
[data-theme="dark"] {
  --color-warning-default: #FB923C;
  --color-warning-hover: #FDBA74;
  --color-warning-active: #F97316;
}
```

---

### Delete/Error (Red)

#### Light Theme
```css
:root {
  --color-delete-default: #DC2626;
  --color-delete-hover: #EF4444;
  --color-delete-active: #B91C1C;
}
```

#### Dark Theme
```css
[data-theme="dark"] {
  --color-delete-default: #EF4444;
  --color-delete-hover: #F87171;
  --color-delete-active: #DC2626;
}
```

---

### Info (Cyan)

#### Light Theme
```css
:root {
  --color-info-default: #0EA5E9;
  --color-info-hover: #38BDF8;
  --color-info-active: #0284C7;
}
```

#### Dark Theme
```css
[data-theme="dark"] {
  --color-info-default: #38BDF8;
  --color-info-hover: #7DD3FC;
  --color-info-active: #0EA5E9;
}
```

---

## 🏢 DEPARTMENT COLORS

### All Departments

#### Light Theme
```css
:root {
  --color-department-all-default: #4B5563;
  --color-department-all-hover: #6B7280;
  --color-department-all-active: #374151;
}
```

#### Dark Theme
```css
[data-theme="dark"] {
  --color-department-all-default: #9CA3AF;
  --color-department-all-hover: #D1D5DB;
  --color-department-all-active: #6B7280;
}
```

---

### Designers (Purple)

#### Light Theme
```css
:root {
  --color-department-designers-default: #6D28D9;
  --color-department-designers-hover: #7C3AED;
  --color-department-designers-active: #5B21B6;
}
```

#### Dark Theme
```css
[data-theme="dark"] {
  --color-department-designers-default: #A78BFA;
  --color-department-designers-hover: #C4B5FD;
  --color-department-designers-active: #7C3AED;
}
```

---

### Developers (Green)

#### Light Theme
```css
:root {
  --color-department-developers-default: #147857;
  --color-department-developers-hover: #1FA97A;
  --color-department-developers-active: #0F5C44;
}
```

#### Dark Theme
```css
[data-theme="dark"] {
  --color-department-developers-default: #35C49B;
  --color-department-developers-hover: #7DE1C1;
  --color-department-developers-active: #1FA97A;
}
```

---

### Managers (Red)

#### Light Theme
```css
:root {
  --color-department-managers-default: #DC2626;
  --color-department-managers-hover: #EF4444;
  --color-department-managers-active: #B91C1C;
}
```

#### Dark Theme
```css
[data-theme="dark"] {
  --color-department-managers-default: #F87171;
  --color-department-managers-hover: #FCA5A5;
  --color-department-managers-active: #EF4444;
}
```

---

### Marketers (Pink)

#### Light Theme
```css
:root {
  --color-department-marketers-default: #EC4899;
  --color-department-marketers-hover: #F472B6;
  --color-department-marketers-active: #DB2777;
}
```

#### Dark Theme
```css
[data-theme="dark"] {
  --color-department-marketers-default: #F9A8D4;
  --color-department-marketers-hover: #FBCFE8;
  --color-department-marketers-active: #F472B6;
}
```

---

### Videographers (Orange)

#### Light Theme
```css
:root {
  --color-department-videographers-default: #F97316;
  --color-department-videographers-hover: #FB923C;
  --color-department-videographers-active: #EA580C;
}
```

#### Dark Theme
```css
[data-theme="dark"] {
  --color-department-videographers-default: #FDBA74;
  --color-department-videographers-hover: #FED7AA;
  --color-department-videographers-active: #FB923C;
}
```

---

## 🔬 MODULE COLORS (RESEARCHES 2)

### Search Queue (Purple - Designers)
```css
:root {
  --color-search: #6D28D9;
  --color-search-hover: #7C3AED;
  --color-search-active: #5B21B6;
  --color-search-bg: rgba(109, 40, 217, 0.15);
}
```

### Video Queue (Green - Developers)
```css
:root {
  --color-video: #147857;
  --color-video-hover: #1FA97A;
  --color-video-active: #0F5C44;
  --color-video-bg: rgba(20, 120, 87, 0.15);
}
```

### Transcriptions (Blue - Primary)
```css
:root {
  --color-transcription: #2563EB;
  --color-transcription-hover: #3B82F6;
  --color-transcription-active: #1D4ED8;
  --color-transcription-bg: rgba(37, 99, 235, 0.15);
}
```

### Analysis (Orange - Warning)
```css
:root {
  --color-analysis: #F97316;
  --color-analysis-hover: #FB923C;
  --color-analysis-active: #EA580C;
  --color-analysis-bg: rgba(249, 115, 22, 0.15);
}
```

### Integration (Red - Managers)
```css
:root {
  --color-integration: #DC2626;
  --color-integration-hover: #EF4444;
  --color-integration-active: #B91C1C;
  --color-integration-bg: rgba(220, 38, 38, 0.15);
}
```

### Taxonomy (Pink - Marketers)
```css
:root {
  --color-taxonomy: #EC4899;
  --color-taxonomy-hover: #F472B6;
  --color-taxonomy-active: #DB2777;
  --color-taxonomy-bg: rgba(236, 72, 153, 0.15);
}
```

---

## ⭐ PRIORITY COLORS

### Critical (80-100)
```css
:root {
  --priority-critical: #dc2626;
  --priority-critical-bg: rgba(220, 38, 38, 0.15);
}
```

### High (60-79)
```css
:root {
  --priority-high: #ea580c;
  --priority-high-bg: rgba(234, 88, 12, 0.15);
}
```

### Medium (40-59)
```css
:root {
  --priority-medium: #f59e0b;
  --priority-medium-bg: rgba(245, 158, 11, 0.15);
}
```

### Low (20-39)
```css
:root {
  --priority-low: #84cc16;
  --priority-low-bg: rgba(132, 204, 22, 0.15);
}
```

### Very Low (0-19)
```css
:root {
  --priority-verylow: #22c55e;
  --priority-verylow-bg: rgba(34, 197, 94, 0.15);
}
```

---

## 📐 TYPOGRAPHY

### Font Family
```css
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap');

:root {
  --font-primary: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI',
                  'Helvetica', 'Arial', sans-serif;
  --font-mono: 'Fira Code', 'Courier New', monospace;
}
```

### Font Sizes
```css
:root {
  /* Headings */
  --text-h1: 3rem;        /* 48px */
  --text-h2: 2.5rem;      /* 40px */
  --text-h3: 2rem;        /* 32px */
  --text-h4: 1.75rem;     /* 28px */
  --text-h5: 1.5rem;      /* 24px */

  /* Body */
  --text-b1: 1rem;        /* 16px - Body Regular */
  --text-b2: 1rem;        /* 16px - Body Medium */
  --text-b3: 0.875rem;    /* 14px - Body Small */

  /* Caption */
  --text-caption: 0.75rem; /* 12px */
}
```

### Font Weights
```css
:root {
  --font-light: 300;      /* Light */
  --font-normal: 400;     /* Regular */
  --font-medium: 500;     /* Medium */
  --font-semibold: 600;   /* Semi Bold */
  --font-bold: 700;       /* Bold */
}
```

### Line Heights
```css
:root {
  --leading-h1: 1.208;         /* 58px */
  --leading-h2: 1.2;           /* 48px */
  --leading-h3: 1.1875;        /* 38px */
  --leading-h4: 1.214;         /* 34px */
  --leading-h5: 1.167;         /* 28px */
  --leading-body: 1.5;         /* 24px */
  --leading-body-small: 1.429; /* 20px */
  --leading-caption: 1.333;    /* 16px */
}
```

---

## 📏 SPACING SYSTEM

### Base Scale (Design System)
```css
:root {
  --space-xs: 0.25rem;   /* 4px */
  --space-sm: 0.5rem;    /* 8px */
  --space-md: 1rem;      /* 16px */
  --space-lg: 1.5rem;    /* 24px */
  --space-xl: 2rem;      /* 32px */
  --space-2xl: 3rem;     /* 48px */
  --space-3xl: 4rem;     /* 64px */
}
```

### Extended Scale (Legacy Support)
```css
:root {
  --space-0: 0;
  --space-1: 0.25rem;    /* 4px */
  --space-2: 0.5rem;     /* 8px */
  --space-3: 0.75rem;    /* 12px */
  --space-4: 1rem;       /* 16px */
  --space-5: 1.25rem;    /* 20px */
  --space-6: 1.5rem;     /* 24px */
  --space-8: 2rem;       /* 32px */
  --space-10: 2.5rem;    /* 40px */
  --space-12: 3rem;      /* 48px */
  --space-16: 4rem;      /* 64px */
  --space-20: 5rem;      /* 80px */
  --space-24: 6rem;      /* 96px */
}
```

---

## ⏱️ TRANSITIONS & ANIMATIONS

### Duration
```css
:root {
  --transition-fast: 150ms ease-in-out;      /* Micro-interactions */
  --transition-normal: 300ms ease-in-out;    /* Standard transitions */
  --transition-slow: 500ms ease-in-out;      /* Page transitions */
}
```

---

## 📐 Z-INDEX LAYERS

```css
:root {
  --z-dropdown: 1000;    /* Dropdown menus */
  --z-sticky: 1020;      /* Sticky elements */
  --z-fixed: 1030;       /* Fixed elements */
  --z-backdrop: 1040;    /* Modal backgrounds */
  --z-modal: 1050;       /* Modal windows */
  --z-popover: 1060;     /* Popover elements */
  --z-tooltip: 1070;     /* Tooltips */
}
```

---

## 📱 RESPONSIVE BREAKPOINTS

```css
:root {
  /* Design System Breakpoints */
  --breakpoint-mobile: 320px;
  --breakpoint-tablet: 768px;
  --breakpoint-desktop: 992px;
  --breakpoint-large: 1200px;
  --breakpoint-extra-large: 1440px;

  /* Legacy Support */
  --screen-sm: 640px;
  --screen-md: 768px;
  --screen-lg: 1024px;
  --screen-xl: 1280px;
  --screen-2xl: 1536px;
}
```

---

## 🎯 USAGE GUIDELINES

### Color Usage
- **Primary (Blue):** Main actions, links, active states
- **Secondary (Gray):** Secondary actions, neutral elements
- **Success (Green):** Positive actions, completed states
- **Warning (Orange):** Warnings, medium priority
- **Delete (Red):** Destructive actions, errors, high priority
- **Info (Cyan):** Informational messages
- **Tertiary (Purple):** Tertiary actions, special features

### Module Colors
- **Search Queue:** Purple (#6D28D9) - Search tasks, queries
- **Video Queue:** Green (#147857) - Video items, queue management
- **Transcriptions:** Blue (#2563EB) - Transcription process
- **Analysis:** Orange (#F97316) - Analysis phase
- **Integration:** Red (#DC2626) - Integration tasks
- **Taxonomy:** Pink (#EC4899) - Entity management

### Priority Colors
| Priority | Range | Color | Stars |
|----------|-------|-------|-------|
| Critical | 80-100 | Red (#dc2626) | ⭐⭐⭐⭐⭐ |
| High | 60-79 | Orange (#ea580c) | ⭐⭐⭐⭐ |
| Medium | 40-59 | Yellow (#f59e0b) | ⭐⭐⭐ |
| Low | 20-39 | Light Green (#84cc16) | ⭐⭐ |
| Very Low | 0-19 | Green (#22c55e) | ⭐ |

### Typography Usage
- **H1 (48px/600):** Page titles, main headlines
- **H2 (40px/600):** Section titles
- **H3 (32px/600):** Subsection titles
- **H4 (28px/600):** Card titles
- **H5 (24px/600):** Small section headers
- **Body Regular (16px/400):** Default body text
- **Body Medium (16px/500):** Emphasized text
- **Body Small (14px/400):** Secondary text, labels
- **Caption (12px/400):** Metadata, timestamps

### Spacing Usage
- **xs (4px):** Icon-text gap, micro-spacing
- **sm (8px):** Small gaps inside components
- **md (16px):** Standard element spacing
- **lg (24px):** Card gaps, section spacing
- **xl (32px):** Large block spacing
- **2xl (48px):** Major section dividers
- **3xl (64px):** Page margins

---

## 📦 IMPLEMENTATION

### Tailwind CSS Configuration

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#2563EB',
          hover: '#3B82F6',
          active: '#1D4ED8',
        },
        search: {
          DEFAULT: '#6D28D9',
          hover: '#7C3AED',
          active: '#5B21B6',
        },
        // ... add all other colors
      },
      fontFamily: {
        sans: ['Roboto', 'system-ui', 'sans-serif'],
        mono: ['Fira Code', 'monospace'],
      },
      fontSize: {
        h1: ['3rem', { lineHeight: '1.208', fontWeight: '600' }],
        h2: ['2.5rem', { lineHeight: '1.2', fontWeight: '600' }],
        // ... add all other sizes
      },
      spacing: {
        xs: '0.25rem',
        sm: '0.5rem',
        md: '1rem',
        lg: '1.5rem',
        xl: '2rem',
        '2xl': '3rem',
        '3xl': '4rem',
      },
    },
  },
}
```

### CSS Variables Import

```css
/* globals.css */
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap');

:root {
  /* Copy all variables from above sections */
}

[data-theme="dark"] {
  /* Copy all dark theme overrides */
}
```

---

## 📚 RELATED DOCUMENTS

- [15_FULL_APP_GENERATION_PROMPT.md](./15_FULL_APP_GENERATION_PROMPT.md) - Complete AI generation prompt
- [14_DEVELOPMENT_PLAN_COMPLETE.md](./14_DEVELOPMENT_PLAN_COMPLETE.md) - Full development plan
- Design System Reference: https://adminrhs.github.io/Design-system/
- Video Catalog Reference: https://adminrhs.github.io/Video-catalog/

---

**Version:** 1.0 | **Last Updated:** 2025-12-08 | **Status:** Production Ready ✅
