# Custom Instructions: Project Setup

**Use these custom instructions when starting a new Lovable project for the Research Management System**

---

## Lovable Custom Instructions

Paste this into Lovable's **Custom Instructions** settings before building any screens:

```
You are building a Research Management System for Remote Helpers with these requirements:

DESIGN SYSTEM (AdminRHS-AI-Catalog):
- Primary color: #428eb4 (accent-blue)
- Hover color: #28749b (accent-blue-hover)
- Background: #f5f5f5 (light mode), #1a1a1a (dark mode)
- Card background: #ffffff (light), #2d2d2d (dark)
- Use friendly, educational aesthetic
- All icons should be 24x24px inline SVG
- Typography: System fonts, clear hierarchy

TECH STACK:
- React 18 + TypeScript + Vite
- Supabase (PostgreSQL database with real-time)
- shadcn/ui components only
- TanStack Query for data fetching
- TanStack Table for data grids
- Recharts for charts/visualizations
- Tailwind CSS for styling
- NO other component libraries

CODE STANDARDS:
- Use TypeScript with strict types
- Functional components with hooks only
- Extract reusable components
- Use const for immutable values
- Descriptive variable names (no abbreviations)
- Comments for complex logic only
- Error boundaries for error handling

FILE STRUCTURE:
src/
  ├── components/       # Reusable UI components
  ├── lib/             # Utilities (supabase.ts, etc.)
  ├── data/            # Mock data for testing
  ├── types/           # TypeScript interfaces
  └── App.tsx

SUPABASE SETUP:
- Enable real-time on all tables
- Use Row Level Security (RLS)
- Connection string from environment variables
- Use typed Supabase client

MOCK DATA FIRST:
- Always start with mock data for rapid development
- Add Supabase integration after UI is working
- Include toggle to switch between mock/real data

NAMING CONVENTIONS:
- Components: PascalCase (VideoQueueTable)
- Files: kebab-case (video-queue-table.tsx)
- Variables: camelCase (videoQueue)
- Constants: UPPER_SNAKE_CASE (MOCK_DATA)
- Types/Interfaces: PascalCase (VideoQueue)

ACCESSIBILITY:
- All interactive elements keyboard accessible
- ARIA labels on icons/buttons
- Semantic HTML elements
- Color contrast minimum AA standard
- Focus states visible

PERFORMANCE:
- Lazy load heavy components
- Memoize expensive calculations
- Debounce search inputs
- Virtual scrolling for large lists
- Optimize re-renders with React.memo

ALWAYS:
- Show loading states
- Handle errors gracefully
- Provide user feedback (toasts, modals)
- Make UI responsive (mobile-first)
- Test with sample data before Supabase
```

---

## Environment Variables Template

Create `.env` file:

```bash
# Supabase Configuration
VITE_SUPABASE_URL=your_supabase_url_here
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key_here

# OpenRouter API (for Video Processing app)
VITE_OPENROUTER_API_KEY=your_openrouter_key_here

# App Configuration
VITE_APP_NAME="Research Management System"
VITE_DAILY_BUDGET=50
```

---

## Initial Package.json Dependencies

```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "@supabase/supabase-js": "^2.38.0",
    "@tanstack/react-query": "^5.8.0",
    "@tanstack/react-table": "^8.10.0",
    "recharts": "^2.10.0",
    "react-router-dom": "^6.20.0",
    "@radix-ui/react-slot": "^1.0.2",
    "@radix-ui/react-dialog": "^1.0.5",
    "@radix-ui/react-dropdown-menu": "^2.0.6",
    "@radix-ui/react-select": "^2.0.0",
    "@radix-ui/react-tabs": "^1.0.4",
    "@radix-ui/react-toast": "^1.1.5",
    "@radix-ui/react-progress": "^1.0.3",
    "lucide-react": "^0.294.0",
    "class-variance-authority": "^0.7.0",
    "clsx": "^2.0.0",
    "tailwind-merge": "^2.1.0"
  },
  "devDependencies": {
    "typescript": "^5.3.0",
    "vite": "^5.0.0",
    "@vitejs/plugin-react": "^4.2.0",
    "tailwindcss": "^3.3.0",
    "autoprefixer": "^10.4.16",
    "postcss": "^8.4.32"
  }
}
```

---

## Supabase Client Setup

```typescript
// src/lib/supabase.ts

import { createClient } from '@supabase/supabase-js';

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY;

if (!supabaseUrl || !supabaseAnonKey) {
  throw new Error('Missing Supabase environment variables');
}

export const supabase = createClient(supabaseUrl, supabaseAnonKey);
```

---

## Tailwind Config

```javascript
// tailwind.config.js

/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        background: 'hsl(var(--background))',
        foreground: 'hsl(var(--foreground))',
        card: 'hsl(var(--card))',
        'accent-blue': '#428eb4',
        'accent-blue-hover': '#28749b',
        'accent-blue-light': '#83CBFF',
      },
    },
  },
  plugins: [],
}
```

---

## Global CSS Variables

```css
/* src/index.css */

@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: 0 0% 96%;
    --foreground: 210 24% 28%;
    --card: 0 0% 100%;
    --card-foreground: 210 24% 28%;
    --border: 0 0% 92%;
    --accent-blue: #428eb4;
    --accent-blue-hover: #28749b;
  }

  .dark {
    --background: 0 0% 10%;
    --foreground: 0 0% 88%;
    --card: 0 0% 18%;
    --card-foreground: 0 0% 88%;
    --border: 0 0% 24%;
  }
}
```

---

## Usage

1. **Start new Lovable project**
2. **Add custom instructions** (copy from above)
3. **Configure environment** (Supabase URL, keys)
4. **Install dependencies** (Lovable handles this)
5. **Start building screens** (one at a time)

---

**Created:** 2025-11-28
**Purpose:** Lovable project configuration and setup
