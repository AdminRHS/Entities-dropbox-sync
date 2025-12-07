# PAGE 11: DESIGN SYSTEM & STYLING GUIDE

**Complete design specifications for building a polished, professional UI**

---

## OVERVIEW

This guide provides the exact design system used in the screen_apps reference implementation. Use these patterns to create a consistent, professional interface across all 8 screens.

---

## TECH STACK

**Core:**
- React 18 + TypeScript
- Vite (build tool)
- Tailwind CSS (styling)

**UI Components:**
- shadcn/ui (headless components on Radix UI)
- Lucide React (icons)
- Recharts (charts for statistics)

**Data Management:**
- TanStack Table (data grids)
- React Hook Form + Zod (forms)
- localStorage (data storage)

---

## COLOR PALETTE

### Primary Colors

```css
/* Main Brand Color */
--accent-blue: #428eb4;
--accent-blue-hover: #28749b;
--accent-blue-light: #83CBFF;

/* Backgrounds */
--background: #f5f5f5;           /* Light mode */
--background-dark: #1a1a1a;      /* Dark mode */
--card: #ffffff;                 /* Light cards */
--card-dark: #2d2d2d;           /* Dark cards */

/* Text */
--foreground: #2d465d;           /* Primary text */
--foreground-muted: #3d5268;     /* Secondary text */
--text-gray: #666666;            /* Tertiary text */
```

### Status Colors

```css
/* Processing Status */
--status-queued: #9CA3AF;        /* Gray */
--status-selected: #60A5FA;      /* Blue */
--status-transcribing: #34D399;  /* Green */
--status-analyzed: #FBBF24;      /* Yellow */
--status-integrated: #F97316;    /* Orange */
--status-complete: #10B981;      /* Emerald */

/* Alert States */
--success: #10B981;              /* Green */
--warning: #FBBF24;              /* Yellow */
--danger: #EF4444;               /* Red */
--info: #60A5FA;                 /* Blue */
```

### Usage in Code

```javascript
// Define status color mapping
const STATUS_COLORS = {
  'QUEUED': '#9CA3AF',
  'SELECTED': '#60A5FA',
  'TRANSCRIBING': '#34D399',
  'ANALYZED': '#FBBF24',
  'INTEGRATED': '#F97316',
  'COMPLETE': '#10B981'
};

// Use in components
<span style={{ backgroundColor: STATUS_COLORS[video.status] }}
      className="px-3 py-1 rounded-full text-white text-sm">
  {video.status}
</span>
```

---

## TYPOGRAPHY

### Font Families

```css
/* Primary */
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
             'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
             sans-serif;

/* Monospace (for IDs, codes) */
font-family: 'Courier New', 'Courier', monospace;
```

### Text Styles

```css
/* Headings */
.heading-xl {
  font-size: 32px;
  font-weight: 700;
  line-height: 1.2;
}

.heading-lg {
  font-size: 24px;
  font-weight: 600;
  line-height: 1.3;
}

.heading-md {
  font-size: 20px;
  font-weight: 600;
  line-height: 1.4;
}

.heading-sm {
  font-size: 16px;
  font-weight: 500;
  line-height: 1.5;
}

/* Body Text */
.body-lg {
  font-size: 16px;
  font-weight: 400;
  line-height: 1.5;
}

.body-md {
  font-size: 14px;
  font-weight: 400;
  line-height: 1.5;
}

.body-sm {
  font-size: 12px;
  font-weight: 400;
  line-height: 1.4;
}
```

### Tailwind Classes

```html
<!-- Headings -->
<h1 class="text-3xl font-bold">Page Title</h1>
<h2 class="text-2xl font-semibold">Section Title</h2>
<h3 class="text-xl font-semibold">Subsection</h3>
<h4 class="text-lg font-medium">Card Title</h4>

<!-- Body Text -->
<p class="text-base">Normal text</p>
<p class="text-sm text-gray-600">Secondary text</p>
<p class="text-xs text-gray-500">Tertiary text</p>

<!-- Monospace -->
<span class="font-mono text-sm">VIDEO-001</span>
```

---

## SPACING SYSTEM

### Tailwind Spacing Scale

```
0   = 0px
1   = 4px
2   = 8px
3   = 12px
4   = 16px
5   = 20px
6   = 24px
8   = 32px
10  = 40px
12  = 48px
16  = 64px
20  = 80px
```

### Standard Spacing Patterns

```html
<!-- Container Padding -->
<div class="p-6">Page container</div>

<!-- Card Padding -->
<div class="p-6">Card content</div>

<!-- Section Margins -->
<section class="mb-8">Section</section>

<!-- Item Spacing -->
<div class="space-y-4">Vertical spacing between items</div>
<div class="gap-4">Grid gap</div>

<!-- Button Padding -->
<button class="px-4 py-2">Standard button</button>
<button class="px-6 py-3">Large button</button>
```

---

## COMPONENT PATTERNS

### 1. Cards

```html
<!-- Basic Card -->
<div class="bg-white rounded-lg p-6 shadow-sm hover:shadow-md transition-shadow duration-200">
  <h3 class="text-lg font-semibold mb-2">Card Title</h3>
  <p class="text-sm text-gray-600">Card content</p>
</div>

<!-- Card with Border -->
<div class="bg-white rounded-lg p-6 border border-gray-200">
  Content
</div>

<!-- Clickable Card -->
<div class="bg-white rounded-lg p-6 shadow-sm hover:shadow-md hover:scale-105 transition-all duration-200 cursor-pointer">
  Clickable content
</div>
```

### 2. Buttons

```html
<!-- Primary Button -->
<button class="px-4 py-2 bg-[#428eb4] hover:bg-[#28749b] text-white rounded-lg transition-colors duration-200 font-medium">
  Primary Action
</button>

<!-- Secondary Button (Outline) -->
<button class="px-4 py-2 border border-gray-300 hover:border-[#428eb4] hover:bg-blue-50 rounded-lg transition-colors duration-200">
  Secondary Action
</button>

<!-- Ghost Button -->
<button class="px-4 py-2 hover:bg-gray-100 rounded-lg transition-colors duration-200">
  Ghost Button
</button>

<!-- Danger Button -->
<button class="px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded-lg transition-colors duration-200">
  Delete
</button>

<!-- Icon Button -->
<button class="p-2 hover:bg-gray-100 rounded-lg transition-colors duration-200">
  <svg class="w-5 h-5"><!-- Icon --></svg>
</button>
```

### 3. Status Badges

```html
<!-- Complete Status -->
<span class="px-3 py-1 rounded-full text-sm font-medium bg-emerald-100 text-emerald-700">
  Complete
</span>

<!-- In Progress -->
<span class="px-3 py-1 rounded-full text-sm font-medium bg-blue-100 text-blue-700">
  In Progress
</span>

<!-- Warning -->
<span class="px-3 py-1 rounded-full text-sm font-medium bg-yellow-100 text-yellow-700">
  Pending
</span>

<!-- Error -->
<span class="px-3 py-1 rounded-full text-sm font-medium bg-red-100 text-red-700">
  Failed
</span>
```

```javascript
// Dynamic Status Badge Component
function StatusBadge({ status }) {
  const styles = {
    'QUEUED': 'bg-gray-100 text-gray-700',
    'SELECTED': 'bg-blue-100 text-blue-700',
    'TRANSCRIBING': 'bg-green-100 text-green-700',
    'ANALYZED': 'bg-yellow-100 text-yellow-700',
    'INTEGRATED': 'bg-orange-100 text-orange-700',
    'COMPLETE': 'bg-emerald-100 text-emerald-700'
  };

  return (
    <span className={`px-3 py-1 rounded-full text-sm font-medium ${styles[status]}`}>
      {status}
    </span>
  );
}
```

### 4. Filter Pills

```html
<!-- Multi-Select Filter Pill -->
<button class="px-3 py-1 rounded-full border border-gray-300 hover:border-[#428eb4] hover:bg-blue-50 transition-colors duration-200 text-sm">
  Filter Option
  <span class="ml-2 text-xs text-gray-500">(12)</span>
</button>

<!-- Active Filter Pill (with remove) -->
<button class="px-3 py-1 rounded-full bg-[#428eb4] text-white text-sm hover:bg-[#28749b] transition-colors duration-200">
  Active Filter
  <span class="ml-2 cursor-pointer">&times;</span>
</button>
```

### 5. Input Fields

```html
<!-- Text Input -->
<input
  type="text"
  placeholder="Search..."
  class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#428eb4] focus:border-transparent"
/>

<!-- Textarea -->
<textarea
  rows="5"
  placeholder="Enter notes..."
  class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#428eb4] focus:border-transparent resize-none"
></textarea>

<!-- Select Dropdown -->
<select class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#428eb4] focus:border-transparent">
  <option>Option 1</option>
  <option>Option 2</option>
</select>
```

### 6. Empty States

```html
<div class="flex flex-col items-center justify-center py-12 text-center">
  <svg class="w-16 h-16 text-gray-300 mb-4">
    <!-- Empty state icon -->
  </svg>
  <h3 class="text-lg font-medium text-gray-900 mb-1">No items found</h3>
  <p class="text-sm text-gray-500 mb-4">Get started by adding your first item</p>
  <button class="px-4 py-2 bg-[#428eb4] text-white rounded-lg hover:bg-[#28749b] transition-colors">
    Add Item
  </button>
</div>
```

### 7. Loading States

```html
<!-- Spinner -->
<div class="flex items-center justify-center py-12">
  <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-[#428eb4]"></div>
  <span class="ml-3 text-sm text-gray-600">Loading...</span>
</div>

<!-- Skeleton Loader (for cards) -->
<div class="bg-white rounded-lg p-6 shadow-sm animate-pulse">
  <div class="h-4 bg-gray-200 rounded w-3/4 mb-4"></div>
  <div class="h-3 bg-gray-200 rounded w-1/2"></div>
</div>
```

### 8. Error States

```html
<div class="bg-red-50 border border-red-200 rounded-lg p-4 mb-4">
  <div class="flex items-start">
    <svg class="w-5 h-5 text-red-600 mt-0.5 mr-3"><!-- Error icon --></svg>
    <div>
      <h4 class="text-sm font-medium text-red-800 mb-1">Error</h4>
      <p class="text-sm text-red-700">Something went wrong. Please try again.</p>
    </div>
  </div>
</div>
```

---

## LAYOUT PATTERNS

### 1. Page Container

```html
<div class="min-h-screen bg-gray-50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Page content -->
  </div>
</div>
```

### 2. Header Section

```html
<header class="mb-8">
  <div class="flex items-center justify-between">
    <div>
      <h1 class="text-3xl font-bold text-gray-900">Page Title</h1>
      <p class="text-sm text-gray-600 mt-1">Page description</p>
    </div>
    <button class="px-4 py-2 bg-[#428eb4] text-white rounded-lg hover:bg-[#28749b]">
      Action
    </button>
  </div>
</header>
```

### 3. Two-Column Layout

```html
<div class="flex gap-6">
  <!-- Sidebar (fixed width) -->
  <aside class="w-64 flex-shrink-0">
    <div class="bg-white rounded-lg p-6 shadow-sm">
      Filters & Navigation
    </div>
  </aside>

  <!-- Main Content (flexible) -->
  <main class="flex-1">
    Main content area
  </main>
</div>
```

### 4. Grid Layouts

```html
<!-- Responsive Grid (1-2-3-4 columns) -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
  <!-- Grid items -->
</div>

<!-- Stats Cards (1-2-4 columns) -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
  <!-- Stat cards -->
</div>

<!-- Two-Column (1-2 columns) -->
<div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
  <!-- Two sections -->
</div>
```

### 5. Vertical Spacing

```html
<!-- Section Spacing -->
<div class="space-y-8">
  <section>Section 1</section>
  <section>Section 2</section>
  <section>Section 3</section>
</div>

<!-- Card List -->
<div class="space-y-4">
  <div class="card">Card 1</div>
  <div class="card">Card 2</div>
</div>
```

---

## SPECIFIC SCREEN PATTERNS

### Video Card with YouTube Embed

```html
<div class="bg-white rounded-lg overflow-hidden shadow-sm hover:shadow-md transition-shadow duration-200">
  <!-- YouTube Iframe -->
  <div class="relative pb-[56.25%] h-0 overflow-hidden bg-black">
    <iframe
      src="https://www.youtube.com/embed/VIDEO_ID"
      class="absolute top-0 left-0 w-full h-full"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen>
    </iframe>
  </div>

  <!-- Card Content -->
  <div class="p-4">
    <h3 class="font-semibold text-gray-900 mb-2 line-clamp-2">
      Video Title Goes Here
    </h3>
    <p class="text-sm text-gray-600 mb-3">Channel Name</p>

    <div class="flex items-center justify-between">
      <span class="text-xs text-gray-500">11:30</span>
      <span class="px-3 py-1 rounded-full text-xs font-medium bg-blue-100 text-blue-700">
        Queued
      </span>
    </div>
  </div>
</div>
```

### Progress Tracker

```html
<div class="space-y-3">
  <!-- Completed Step -->
  <div class="flex items-start border-l-4 border-green-500 bg-green-50 p-4 rounded-r-lg">
    <span class="text-2xl mr-3">✅</span>
    <div class="flex-1">
      <div class="font-semibold text-gray-900">Queued</div>
      <div class="text-sm text-gray-600">2024-12-01</div>
    </div>
  </div>

  <!-- Current Step -->
  <div class="flex items-start border-l-4 border-orange-500 bg-orange-50 p-4 rounded-r-lg">
    <span class="text-2xl mr-3">⏳</span>
    <div class="flex-1">
      <div class="font-semibold text-gray-900">Transcribing</div>
      <div class="text-sm text-gray-600">In progress...</div>
    </div>
  </div>

  <!-- Pending Step -->
  <div class="flex items-start border-l-4 border-gray-300 bg-gray-50 p-4 rounded-r-lg">
    <span class="text-2xl mr-3">⏹</span>
    <div class="flex-1">
      <div class="font-semibold text-gray-900">Analyzed</div>
      <div class="text-sm text-gray-600">Not started</div>
    </div>
  </div>
</div>
```

### Stats Card

```html
<div class="bg-white rounded-lg p-6 shadow-sm">
  <div class="flex items-center justify-between mb-2">
    <h4 class="text-sm font-medium text-gray-600">Total Videos</h4>
    <svg class="w-5 h-5 text-[#428eb4]"><!-- Icon --></svg>
  </div>
  <div class="text-3xl font-bold text-gray-900 mb-1">24</div>
  <div class="text-sm text-gray-500">
    <span class="text-green-600 font-medium">+3</span> from last week
  </div>
</div>
```

### Filter Panel (Collapsible)

```html
<div class="bg-white rounded-lg p-4 shadow-sm">
  <h3 class="font-semibold text-gray-900 mb-4">Filters</h3>

  <!-- Filter Section -->
  <div class="mb-6">
    <button
      class="w-full flex items-center justify-between text-left font-medium text-gray-900 mb-3"
      onclick="toggleSection('status')">
      <span>Status</span>
      <svg class="w-4 h-4 transition-transform" id="status-icon">
        <!-- Chevron icon -->
      </svg>
    </button>

    <div id="status-filters" class="space-y-2">
      <label class="flex items-center">
        <input type="checkbox" class="rounded mr-2" />
        <span class="text-sm text-gray-700">Queued</span>
        <span class="ml-auto text-xs text-gray-500">(12)</span>
      </label>
      <label class="flex items-center">
        <input type="checkbox" class="rounded mr-2" />
        <span class="text-sm text-gray-700">Complete</span>
        <span class="ml-auto text-xs text-gray-500">(8)</span>
      </label>
    </div>
  </div>

  <!-- Clear Filters -->
  <button class="w-full px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors text-sm font-medium">
    Clear All Filters
  </button>
</div>
```

---

## RESPONSIVE DESIGN

### Breakpoints

```css
/* Mobile First */
@media (min-width: 640px)  { /* sm */ }
@media (min-width: 768px)  { /* md */ }
@media (min-width: 1024px) { /* lg */ }
@media (min-width: 1280px) { /* xl */ }
```

### Responsive Patterns

```html
<!-- Hide on Mobile, Show on Desktop -->
<div class="hidden lg:block">Desktop only</div>

<!-- Show on Mobile, Hide on Desktop -->
<div class="block lg:hidden">Mobile only</div>

<!-- Responsive Padding -->
<div class="px-4 sm:px-6 lg:px-8">Responsive padding</div>

<!-- Responsive Grid Columns -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
  <!-- Responsive grid -->
</div>

<!-- Responsive Text Size -->
<h1 class="text-2xl sm:text-3xl lg:text-4xl font-bold">
  Responsive heading
</h1>
```

---

## ANIMATIONS & TRANSITIONS

### Standard Transitions

```css
/* Default transition (200ms) */
transition-colors duration-200
transition-shadow duration-200
transition-transform duration-200

/* Slower transition (300ms) */
transition-all duration-300 ease-in-out

/* Fast transition (150ms) */
transition-opacity duration-150
```

### Hover Effects

```html
<!-- Card Hover -->
<div class="hover:shadow-md transition-shadow duration-200">

<!-- Button Hover -->
<button class="hover:bg-blue-700 transition-colors duration-200">

<!-- Scale on Hover -->
<div class="hover:scale-105 transition-transform duration-200">

<!-- Opacity on Hover -->
<div class="hover:opacity-80 transition-opacity duration-150">
```

### Loading Animation

```html
<div class="animate-spin rounded-full h-8 w-8 border-b-2 border-[#428eb4]"></div>
```

### Pulse Animation (skeleton)

```html
<div class="animate-pulse bg-gray-200 h-4 rounded"></div>
```

---

## ACCESSIBILITY

### Best Practices

```html
<!-- Proper Labels -->
<label for="search" class="sr-only">Search videos</label>
<input id="search" type="text" />

<!-- Button with ARIA -->
<button aria-label="Close dialog" class="...">
  <svg><!-- X icon --></svg>
</button>

<!-- Keyboard Navigation -->
<button
  tabindex="0"
  onKeyDown={(e) => e.key === 'Enter' && handleClick()}
  class="...">
  Action
</button>

<!-- Focus States -->
<button class="focus:outline-none focus:ring-2 focus:ring-[#428eb4] focus:ring-offset-2">
  Focus visible
</button>
```

---

## IMPLEMENTATION CHECKLIST

When building each screen:

✅ Use exact color palette (#428eb4 primary)
✅ Apply consistent spacing (p-4, p-6, gap-4)
✅ Use rounded-lg for cards and buttons
✅ Add hover states with transitions (200-300ms)
✅ Include empty, loading, and error states
✅ Make responsive (mobile-first)
✅ Add proper focus states for accessibility
✅ Use status-based colors for badges
✅ Implement filter pills for multi-select
✅ Add smooth shadow transitions on cards

---

## NEXT STEPS

**Apply this design system to:**
- All 8 screens (Topics, Queue, Processing, Library, etc.)
- Statistics dashboard
- Advanced features

**Test on:**
- Mobile devices (320px - 768px)
- Tablets (768px - 1024px)
- Desktops (1024px+)

Your app will now have a **consistent, professional design** that matches the screen_apps reference implementation.
