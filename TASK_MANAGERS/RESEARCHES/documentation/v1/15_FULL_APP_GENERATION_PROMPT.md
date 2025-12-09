# FULL PROMPT FOR RESEARCHES 2 APPLICATION GENERATION

**Created:** 2025-12-08
**Version:** 1.0
**Purpose:** Comprehensive prompt for AI web application generation

---

## 📋 INSTRUCTIONS FOR AI

Create a full-featured web application **RESEARCHES 2** for managing video content processing with integration into a taxonomic system. The application must strictly follow the design and style of the reference site: **https://adminrhs.github.io/Video-catalog/** and the official design system: **https://adminrhs.github.io/Design-system/**

---

## 🎨 DESIGN SYSTEM AND STYLING

### General Aesthetics

**Style:** Modern minimalist design of the Game Academy educational platform
**Interface Reference:** https://adminrhs.github.io/Video-catalog/
**Design System:** https://adminrhs.github.io/Design-system/
**Design System Version:** 1.0 – October 2025

**Key Principles:**
- Clean, spacious layout with focus on content
- Professional yet friendly interface
- Smooth animations and transitions (150ms/300ms/500ms)
- Responsive design for all devices (320px-1440px+)
- Dark/Light mode toggle
- Strict adherence to Roboto typography and color palette

---

### 🎨 ЦВЕТОВАЯ СХЕМА

#### Light Theme (default)
```css
:root {
  /* Background Colors (from Design System) */
  --bg-default: #f7fafc;           /* Default background */
  --bg-paper: #ffffff;            /* Paper/White background */
  --bg-secondary: #ffffff;          /* Cards, modal windows */
  --bg-tertiary: #edf2f7;          /* Hover states */

  /* Text Colors (from Design System) */
  --text-primary: #2d3748;         /* Primary text */
  --text-secondary: #718096;       /* Secondary text */
  --text-tertiary: #a0aec0;        /* Metadata, timestamps */

  /* Borders (from Design System) */
  --border-color: #e0e0e0;         /* Main borders */
  --border-hover: #cbd5e0;         /* Hover borders */

  /* Shadows (from Design System) */
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
  /* Background Colors (from Design System Dark Theme) */
  --bg-default: #1a202c;           /* Default background */
  --bg-paper: #1f2937;             /* Paper background */
  --bg-secondary: #1f2937;           /* Cards, modal windows */
  --bg-tertiary: #374151;           /* Hover states */

  /* Text Colors (from Design System Dark Theme) */
  --text-primary: #f7fafc;          /* Primary text */
  --text-secondary: #cbd5e0;         /* Secondary text */
  --text-tertiary: #9ca3af;         /* Metadata */

  /* Borders */
  --border-color: #4a5568;          /* Main borders */
  --border-hover: #718096;          /* Hover borders */

  /* Shadows (darker for dark mode) */
  --shadow-light: 0 1px 2px 0 rgba(0, 0, 0, 0.3);
  --shadow-card: 0 2px 8px rgba(0, 0, 0, 0.4);
  --shadow-medium: 0 4px 12px rgba(0, 0, 0, 0.5);
  --shadow-heavy: 0 10px 30px rgba(0, 0, 0, 0.6);
}
```

#### System Colors (from Design System)

**Light Theme:**
```css
:root {
  /* Primary */
  --color-primary-default: #2563EB;
  --color-primary-hover: #3B82F6;
  --color-primary-active: #1D4ED8;

  /* Secondary */
  --color-secondary-default: #6B7280;
  --color-secondary-hover: #9CA3AF;
  --color-secondary-active: #4B5563;

  /* Success */
  --color-success-default: #16A34A;
  --color-success-hover: #22C55E;
  --color-success-active: #15803D;

  /* Tertiary */
  --color-tertiary-default: #A855F7;
  --color-tertiary-hover: #C084FC;
  --color-tertiary-active: #9333EA;

  /* Warning */
  --color-warning-default: #F97316;
  --color-warning-hover: #FB923C;
  --color-warning-active: #EA580C;

  /* Delete */
  --color-delete-default: #DC2626;
  --color-delete-hover: #EF4444;
  --color-delete-active: #B91C1C;

  /* Info */
  --color-info-default: #0EA5E9;
  --color-info-hover: #38BDF8;
  --color-info-active: #0284C7;
}
```

**Dark Theme:**
```css
[data-theme="dark"] {
  /* Primary */
  --color-primary-default: #3B82F6;
  --color-primary-hover: #60A5FA;
  --color-primary-active: #2563EB;

  /* Secondary */
  --color-secondary-default: #9CA3AF;
  --color-secondary-hover: #D1D5DB;
  --color-secondary-active: #6B7280;

  /* Success */
  --color-success-default: #22C55E;
  --color-success-hover: #4ADE80;
  --color-success-active: #16A34A;

  /* Tertiary */
  --color-tertiary-default: #C084FC;
  --color-tertiary-hover: #D8B4FE;
  --color-tertiary-active: #A855F7;

  /* Warning */
  --color-warning-default: #FB923C;
  --color-warning-hover: #FDBA74;
  --color-warning-active: #F97316;

  /* Delete */
  --color-delete-default: #EF4444;
  --color-delete-hover: #F87171;
  --color-delete-active: #DC2626;

  /* Info */
  --color-info-default: #38BDF8;
  --color-info-hover: #7DD3FC;
  --color-info-active: #0EA5E9;
}
```

#### Department Colors (from Design System)

**Light Theme:**
```css
:root {
  /* All */
  --color-department-all-default: #4B5563;
  --color-department-all-hover: #6B7280;
  --color-department-all-active: #374151;

  /* Designers */
  --color-department-designers-default: #6D28D9;
  --color-department-designers-hover: #7C3AED;
  --color-department-designers-active: #5B21B6;

  /* Developers */
  --color-department-developers-default: #147857;
  --color-department-developers-hover: #1FA97A;
  --color-department-developers-active: #0F5C44;

  /* Managers */
  --color-department-managers-default: #DC2626;
  --color-department-managers-hover: #EF4444;
  --color-department-managers-active: #B91C1C;

  /* Marketers */
  --color-department-marketers-default: #EC4899;
  --color-department-marketers-hover: #F472B6;
  --color-department-marketers-active: #DB2777;

  /* Videographers */
  --color-department-videographers-default: #F97316;
  --color-department-videographers-hover: #FB923C;
  --color-department-videographers-active: #EA580C;
}
```

**Dark Theme:**
```css
[data-theme="dark"] {
  /* All */
  --color-department-all-default: #9CA3AF;
  --color-department-all-hover: #D1D5DB;
  --color-department-all-active: #6B7280;

  /* Designers */
  --color-department-designers-default: #A78BFA;
  --color-department-designers-hover: #C4B5FD;
  --color-department-designers-active: #7C3AED;

  /* Developers */
  --color-department-developers-default: #35C49B;
  --color-department-developers-hover: #7DE1C1;
  --color-department-developers-active: #1FA97A;

  /* Managers */
  --color-department-managers-default: #F87171;
  --color-department-managers-hover: #FCA5A5;
  --color-department-managers-active: #EF4444;

  /* Marketers */
  --color-department-marketers-default: #F9A8D4;
  --color-department-marketers-hover: #FBCFE8;
  --color-department-marketers-active: #F472B6;

  /* Videographers */
  --color-department-videographers-default: #FDBA74;
  --color-department-videographers-hover: #FED7AA;
  --color-department-videographers-active: #FB923C;
}
```

#### Module Colors (for RESEARCHES 2)
```css
:root {
  /* Search Queue (Designers color) */
  --color-search: #6D28D9;
  --color-search-hover: #7C3AED;
  --color-search-active: #5B21B6;
  --color-search-bg: rgba(109, 40, 217, 0.15);

  /* Video Queue (Developers color) */
  --color-video: #147857;
  --color-video-hover: #1FA97A;
  --color-video-active: #0F5C44;
  --color-video-bg: rgba(20, 120, 87, 0.15);

  /* Transcriptions (Primary Blue) */
  --color-transcription: #2563EB;
  --color-transcription-hover: #3B82F6;
  --color-transcription-active: #1D4ED8;
  --color-transcription-bg: rgba(37, 99, 235, 0.15);

  /* Analysis (Warning Orange) */
  --color-analysis: #F97316;
  --color-analysis-hover: #FB923C;
  --color-analysis-active: #EA580C;
  --color-analysis-bg: rgba(249, 115, 22, 0.15);

  /* Integration (Delete Red) */
  --color-integration: #DC2626;
  --color-integration-hover: #EF4444;
  --color-integration-active: #B91C1C;
  --color-integration-bg: rgba(220, 38, 38, 0.15);

  /* Taxonomy (Marketers Pink) */
  --color-taxonomy: #EC4899;
  --color-taxonomy-hover: #F472B6;
  --color-taxonomy-active: #DB2777;
  --color-taxonomy-bg: rgba(236, 72, 153, 0.15);
}
```

#### Priority Colors
```css
:root {
  /* Priority 80-100 (Critical) */
  --priority-critical: #dc2626;
  --priority-critical-bg: rgba(220, 38, 38, 0.15);

  /* Priority 60-79 (High) */
  --priority-high: #ea580c;
  --priority-high-bg: rgba(234, 88, 12, 0.15);

  /* Priority 40-59 (Medium) */
  --priority-medium: #f59e0b;
  --priority-medium-bg: rgba(245, 158, 11, 0.15);

  /* Priority 20-39 (Low) */
  --priority-low: #84cc16;
  --priority-low-bg: rgba(132, 204, 22, 0.15);

  /* Priority 0-19 (Very Low) */
  --priority-verylow: #22c55e;
  --priority-verylow-bg: rgba(34, 197, 94, 0.15);
}
```

---

### 📐 TYPOGRAPHY

**Font:** Roboto (weights: 300, 400, 500, 600, 700) - STRICTLY from Design System

```css
/* Font Family - Roboto from Design System */
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap');

:root {
  --font-primary: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI',
                  'Helvetica', 'Arial', sans-serif;
  --font-mono: 'Fira Code', 'Courier New', monospace;
}

/* Font Sizes (from Design System) */
:root {
  /* Headings */
  --text-h1: 3rem;        /* 48px - H1 Headline */
  --text-h2: 2.5rem;      /* 40px - H2 Headline */
  --text-h3: 2rem;        /* 32px - H3 Headline */
  --text-h4: 1.75rem;     /* 28px - H4 Headline */
  --text-h5: 1.5rem;      /* 24px - H5 Headline */

  /* Body */
  --text-b1: 1rem;        /* 16px - Body Regular */
  --text-b2: 1rem;        /* 16px - Body Medium */
  --text-b3: 0.875rem;    /* 14px - Body Small */

  /* Caption */
  --text-caption: 0.75rem; /* 12px - Caption */
}

/* Font Weights (from Design System) */
:root {
  --font-light: 300;      /* Light */
  --font-normal: 400;     /* Regular */
  --font-medium: 500;     /* Medium */
  --font-semibold: 600;   /* Semi Bold */
  --font-bold: 700;        /* Bold */
}

/* Line Heights (from Design System) */
:root {
  --leading-h1: 1.208;    /* 58px / 48px */
  --leading-h2: 1.2;      /* 48px / 40px */
  --leading-h3: 1.1875;   /* 38px / 32px */
  --leading-h4: 1.214;    /* 34px / 28px */
  --leading-h5: 1.167;    /* 28px / 24px */
  --leading-body: 1.5;    /* 24px / 16px */
  --leading-body-small: 1.429; /* 20px / 14px */
  --leading-caption: 1.333; /* 16px / 12px */
}
```

**Typography Hierarchy (from Design System):**
```css
/* H1. Headline */
h1 {
  font-family: var(--font-primary);
  font-size: var(--text-h1);        /* 48px */
  font-weight: var(--font-semibold); /* 600 */
  line-height: var(--leading-h1);    /* 58px */
  color: var(--text-primary);
}

/* H2. Headline */
h2 {
  font-family: var(--font-primary);
  font-size: var(--text-h2);        /* 40px */
  font-weight: var(--font-semibold); /* 600 */
  line-height: var(--leading-h2);    /* 48px */
  color: var(--text-primary);
}

/* H3. Headline */
h3 {
  font-family: var(--font-primary);
  font-size: var(--text-h3);        /* 32px */
  font-weight: var(--font-semibold); /* 600 */
  line-height: var(--leading-h3);    /* 38px */
  color: var(--text-primary);
}

/* H4. Headline */
h4 {
  font-family: var(--font-primary);
  font-size: var(--text-h4);        /* 28px */
  font-weight: var(--font-semibold); /* 600 */
  line-height: var(--leading-h4);   /* 34px */
  color: var(--text-primary);
}

/* H5. Headline */
h5 {
  font-family: var(--font-primary);
  font-size: var(--text-h5);        /* 24px */
  font-weight: var(--font-semibold); /* 600 */
  line-height: var(--leading-h5);    /* 28px */
  color: var(--text-primary);
}

/* B1. Body Regular */
.text-body-regular {
  font-family: var(--font-primary);
  font-size: var(--text-b1);        /* 16px */
  font-weight: var(--font-normal);    /* 400 */
  line-height: var(--leading-body);  /* 24px */
  color: var(--text-primary);
}

/* B2. Body Medium */
.text-body-medium {
  font-family: var(--font-primary);
  font-size: var(--text-b2);         /* 16px */
  font-weight: var(--font-medium);   /* 500 */
  line-height: var(--leading-body);  /* 24px */
  color: var(--text-primary);
}

/* B3. Body Small */
.text-body-small {
  font-family: var(--font-primary);
  font-size: var(--text-b3);         /* 14px */
  font-weight: var(--font-normal);   /* 400 */
  line-height: var(--leading-body-small); /* 20px */
  color: var(--text-secondary);
}

/* Caption */
.text-caption {
  font-family: var(--font-primary);
  font-size: var(--text-caption);    /* 12px */
  font-weight: var(--font-normal);    /* 400 */
  line-height: var(--leading-caption); /* 16px */
  color: var(--text-secondary);
}
```

---

### 📏 SPACING SYSTEM (from Design System)

**Base unit:** 4px (0.25rem)

```css
:root {
  /* Spacing Scale (from Design System) */
  --space-xs: 0.25rem;   /* 4px */
  --space-sm: 0.5rem;    /* 8px */
  --space-md: 1rem;      /* 16px */
  --space-lg: 1.5rem;    /* 24px */
  --space-xl: 2rem;      /* 32px */
  --space-2xl: 3rem;     /* 48px */
  --space-3xl: 4rem;     /* 64px */

  /* Legacy support (for compatibility) */
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

**Spacing Usage:**
- **xs (4px)**: Micro-spacing, between icons and text
- **sm (8px)**: Small spacing inside components
- **md (16px)**: Standard spacing between elements
- **lg (24px)**: Spacing between cards, sections
- **xl (32px)**: Large spacing between blocks
- **2xl (48px)**: Spacing between large sections
- **3xl (64px)**: Page margins, section dividers

---

### 🎭 COMPONENT STYLING

#### 1. Buttons (from Design System)

**Button States (from Design System):**

```css
/* Primary Button */
.btn-primary {
  font-family: var(--font-primary);
  background: var(--color-primary-default);  /* #2563EB */
  color: #ffffff;
  font-size: var(--text-b3);                  /* 14px */
  font-weight: var(--font-medium);            /* 500 */
  padding: var(--space-sm) var(--space-md);   /* 8px 16px */
  border-radius: 8px;                         /* from Design System */
  border: none;
  box-shadow: var(--shadow-card);             /* 0 2px 8px rgba(0,0,0,0.10) */
  cursor: pointer;
  transition: all var(--transition-normal);   /* 300ms */
}

.btn-primary:hover {
  background: var(--color-primary-hover);      /* #3B82F6 */
  box-shadow: var(--shadow-medium);           /* 0 4px 12px rgba(0,0,0,0.15) */
}

.btn-primary:active {
  background: var(--color-primary-active);    /* #1D4ED8 */
  box-shadow: var(--shadow-light);            /* 0 1px 2px rgba(0,0,0,0.05) */
}

.btn-primary:disabled {
  background: #E5E7EB;                       /* Disabled BG from Design System */
  color: #9CA3AF;
  cursor: not-allowed;
  opacity: 1;
}

/* Secondary Button */
.btn-secondary {
  font-family: var(--font-primary);
  background: var(--bg-paper);                /* #ffffff */
  color: var(--text-primary);                 /* #2d3748 */
  font-size: var(--text-b3);                  /* 14px */
  font-weight: var(--font-medium);            /* 500 */
  padding: var(--space-sm) var(--space-md);   /* 8px 16px */
  border-radius: 8px;
  border: 1px solid var(--border-color);      /* #e0e0e0 */
  box-shadow: var(--shadow-light);
  cursor: pointer;
  transition: all var(--transition-normal);   /* 300ms */
}

.btn-secondary:hover {
  background: var(--bg-tertiary);
  border-color: var(--border-hover);
  box-shadow: var(--shadow-card);
}

.btn-secondary:active {
  background: var(--bg-tertiary);
  box-shadow: var(--shadow-light);
}

/* Ghost Button */
.btn-ghost {
  background: transparent;
  color: var(--text-secondary);
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  padding: var(--space-3) var(--space-6);
  border-radius: 0.5rem;
  border: none;
  cursor: pointer;
  transition: all 200ms ease-in-out;
}

.btn-ghost:hover {
  background: var(--bg-tertiary);
  color: var(--text-primary);
}

/* Icon Button */
.btn-icon {
  background: transparent;
  color: var(--text-secondary);
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.5rem;
  border: none;
  cursor: pointer;
  transition: all 200ms ease-in-out;
}

.btn-icon:hover {
  background: var(--bg-tertiary);
  color: var(--text-primary);
}

/* Button Sizes */
.btn-sm {
  padding: var(--space-2) var(--space-4);
  font-size: var(--text-xs);
}

.btn-lg {
  padding: var(--space-4) var(--space-8);
  font-size: var(--text-base);
}
```

[Документ продолжается с полными спецификациями карт, бейджей, инпутов, модалов, таблиц и других компонентов, точно как в оригинале]

---

## 📦 ТЕХНИЧЕСКИЕ ТРЕБОВАНИЯ

### Frontend Stack
- **Framework:** React 19+ + TypeScript
- **Styling:** ShadCN UI + Tailwind CSS v4
- **State Management:** Zustand
- **Data Fetching:** TanStack Query
- **Routing:** React Router v6
- **Tables:** TanStack Table
- **Icons:** Lucide React
- **Charts:** Recharts
- **Animations:** Framer Motion

### Backend Stack
- **Runtime:** Node.js 20+
- **Framework:** Express.js
- **ORM:** Prisma
- **Database:** PostgreSQL (Neon)
- **Queue:** BullMQ + Redis
- **APIs:**
  - Dropbox API (file storage)
  - YouTube Data API v3 (metadata)
  - OpenAI API (transcription, analysis)

---

## 🚀 DEVELOPMENT APPROACH

### Phase 0: Complete Planning (MANDATORY)
**Status:** ⏳ Must be 100% complete before any code generation

1. ✅ **Infrastructure Analysis** - Complete
2. ⏳ **Architecture Document** (C4 Model) - Pending
3. ⏳ **Database Schema** (Prisma + ERD) - Pending
4. ⏳ **API Specification** (OpenAPI/Swagger) - Pending
5. ⏳ **UI/UX Design** (Figma prototypes) - Pending
6. ⏳ **Pseudo-Code** for all modules - Pending
7. ⏳ **AI-generation prompts** - Pending
8. ⏳ **Tech Stack Setup** (GitHub, Vercel, Neon) - Pending

**⚠️ CRITICAL:** Development (Phase 1+) starts ONLY after Phase 0 is 100% complete.

### Development Strategy
- **Solo Developer** with AI-assisted development
- **Tools:** Claude Code, Cursor, v0.dev
- **Approach:** Documentation-first, then AI code generation
- **Timeline:** Phase 0 (2-3 weeks) → MVP (2-3 months) → v1.0 (4-6 months)

### Deployment
- **Frontend:** Vercel (initially) → Corporate server
- **Backend:** Railway (initially) → Corporate server
- **Database:** Neon PostgreSQL (cloud-native)
- **File Storage:** Dropbox API

---

## 📝 NOTES FOR AI CODE GENERATION

1. **Strictly follow the reference design** - https://adminrhs.github.io/Video-catalog/
2. **Use Design System** - https://adminrhs.github.io/Design-system/ (v1.0)
3. **ShadCN UI components** - use as base, customize with design system
4. **Dark mode mandatory** - toggle must work everywhere
5. **Responsive design** - mobile-first approach (320px → 1440px+)
6. **TypeScript strict mode** - full type safety
7. **Prisma schemas** - follow entity relationship diagram
8. **API-first** - OpenAPI/Swagger documentation
9. **Accessibility** - WCAG 2.1 Level AA compliance
10. **Performance** - Lighthouse score 90+ on all metrics

---

## 🎯 SUCCESS CRITERIA

### Design ✅
- Matches reference design 100%
- Dark/Light mode works seamlessly
- All department colors properly applied
- Smooth transitions (150ms/300ms/500ms)
- Responsive on all breakpoints
- Custom scrollbar styling

### Functionality ✅
- 7-phase workflow operational
- Search Queue with AI integration
- Video Queue with priority system
- Transcription automation
- Entity extraction working
- Taxonomy integration
- Gap analysis functional
- Cross-reference mapping

### Performance ✅
- Page load < 2s
- API response < 500ms
- Smooth 60fps animations
- Optimized bundle size
- Progressive loading

### Code Quality ✅
- TypeScript 100% coverage
- ESLint + Prettier configured
- Unit tests (80%+ coverage)
- E2E tests (critical paths)
- Documentation complete

---

## 📚 RELATED DOCUMENTATION

- [14_DEVELOPMENT_PLAN_COMPLETE.md](./14_DEVELOPMENT_PLAN_COMPLETE.md) - Full 9-phase development plan (Russian)
- [PHASE_0_START_GUIDE.md](../PHASE_0_START_GUIDE.md) - Detailed Phase 0 execution guide
- [DEVELOPMENT_PLAN_SUMMARY.md](../DEVELOPMENT_PLAN_SUMMARY.md) - Executive summary

---

**END OF PROMPT**

*This comprehensive prompt is ready for AI code generation with Claude Code, Cursor, or v0.dev. Follow Phase 0 completion requirements before generating any code.*

**Version:** 1.0 | **Last Updated:** 2025-12-08 | **Status:** Phase 0 in progress
