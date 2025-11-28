# Custom Instructions: Design System Quick Reference

**Quick reference for AdminRHS-AI-Catalog design system**

---

## Color Palette

```typescript
// Use these exact hex values in your code

const COLORS = {
  // Primary Colors
  accentBlue: '#428eb4',
  accentBlueHover: '#28749b',
  accentBlueLight: '#83CBFF',

  // Backgrounds
  background: '#f5f5f5',
  backgroundDark: '#1a1a1a',
  card: '#ffffff',
  cardDark: '#2d2d2d',

  // Text
  foreground: '#2d465d',
  foregroundDark: '#e0e0e0',
  mutedForeground: '#3d5268',

  // Phase Colors (Video Processing)
  phase0: '#9CA3AF',  // Gray - Search
  phase1: '#60A5FA',  // Blue - Transcription
  phase2: '#34D399',  // Green - Extraction
  phase3: '#FBBF24',  // Yellow - Gap Analysis
  phase4: '#F97316',  // Orange - Integration
  phase5: '#A78BFA',  // Purple - Mapping
  complete: '#10B981', // Emerald - Complete

  // Status Colors
  success: '#10B981',
  warning: '#FBBF24',
  danger: '#EF4444',
  info: '#60A5FA',
};
```

---

## SVG Icons (24x24px)

### Search Icon
```tsx
<svg width="24" height="24" viewBox="0 0 24 24" fill="none">
  <path d="M11 18C14.866 18 18 14.866 18 11C18 7.13401 14.866 4 11 4C7.13401 4 4 7.13401 4 11C4 14.866 7.13401 18 11 18Z" stroke="currentColor" strokeWidth="2"/>
  <path d="M20 20L17 17" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
</svg>
```

### Filter Icon
```tsx
<svg width="24" height="24" viewBox="0 0 24 24" fill="none">
  <path d="M4 6H20M7 12H17M10 18H14" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
</svg>
```

### Upload Icon
```tsx
<svg width="24" height="24" viewBox="0 0 24 24" fill="none">
  <path d="M12 15V3M12 3L8 7M12 3L16 7" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
  <path d="M2 17L2 19C2 20.1046 2.89543 21 4 21L20 21C21.1046 21 22 20.1046 22 19L22 17" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
</svg>
```

---

## Typography

```css
/* Headings */
.heading-xl { font-size: 32px; font-weight: 700; }
.heading-lg { font-size: 24px; font-weight: 600; }
.heading-md { font-size: 20px; font-weight: 600; }
.heading-sm { font-size: 16px; font-weight: 500; }

/* Body */
.body-lg { font-size: 16px; font-weight: 400; }
.body-md { font-size: 14px; font-weight: 400; }
.body-sm { font-size: 12px; font-weight: 400; }

/* Monospace (for IDs, codes) */
.mono { font-family: 'Courier New', monospace; }
```

---

## Component Patterns

### Card with Hover Effect
```tsx
<div className="bg-white rounded-lg p-6 shadow-sm hover:shadow-md transition-shadow duration-200">
  {/* Card content */}
</div>
```

### Status Badge
```tsx
<span className="px-3 py-1 rounded-full text-sm font-medium bg-emerald-100 text-emerald-700">
  Complete
</span>
```

### Button Primary
```tsx
<button className="px-4 py-2 bg-accent-blue hover:bg-accent-blue-hover text-white rounded-lg transition-colors">
  Action
</button>
```

### Filter Pill (Multi-select)
```tsx
<button className="px-3 py-1 rounded-full border border-gray-300 hover:border-accent-blue hover:bg-blue-50 transition-colors">
  Filter Option
</button>
```

---

## Spacing System

```css
/* Use Tailwind spacing scale */
padding: p-1 (4px), p-2 (8px), p-4 (16px), p-6 (24px), p-8 (32px)
margin: m-1 (4px), m-2 (8px), m-4 (16px), m-6 (24px), m-8 (32px)
gap: gap-2 (8px), gap-4 (16px), gap-6 (24px)
```

---

## Animation/Transitions

```css
/* Hover transitions */
transition-colors duration-200
transition-shadow duration-200
transition-transform duration-200

/* Expandable panels */
transition-all duration-300 ease-in-out

/* Loading spinners */
animate-spin
```

---

## Responsive Breakpoints

```css
/* Mobile first approach */
sm: 640px   /* Small devices */
md: 768px   /* Tablets */
lg: 1024px  /* Desktops */
xl: 1280px  /* Large desktops */
```

---

**Quick Copy Templates:**

### Empty State
```tsx
<div className="flex flex-col items-center justify-center py-12 text-center">
  <div className="text-gray-400 mb-4">
    {/* Icon here */}
  </div>
  <h3 className="text-lg font-medium text-gray-900">No items found</h3>
  <p className="text-sm text-gray-500 mt-1">Get started by adding your first item</p>
</div>
```

### Loading State
```tsx
<div className="flex items-center justify-center py-12">
  <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-accent-blue"></div>
  <span className="ml-3 text-sm text-gray-600">Loading...</span>
</div>
```

### Error State
```tsx
<div className="bg-red-50 border border-red-200 rounded-lg p-4">
  <p className="text-sm text-red-800">Something went wrong. Please try again.</p>
</div>
```

---

**Created:** 2025-11-28
**Purpose:** Quick design system reference for Lovable
