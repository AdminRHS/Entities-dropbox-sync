# ПОЛНЫЙ ПРОМПТ ДЛЯ ГЕНЕРАЦИИ RESEARCHES 2 APPLICATION

**Дата создания:** 2025-12-08
**Версия:** 1.0
**Назначение:** Comprehensive prompt для AI-генерации веб-приложения

---

## 📋 ИНСТРУКЦИИ ДЛЯ AI

Создай полнофункциональное веб-приложение **RESEARCHES 2** для управления обработкой видеоконтента с интеграцией в таксономическую систему. Приложение должно строго следовать дизайну и стилистике референсного сайта: **https://adminrhs.github.io/Video-catalog/**

---

## 🎨 ДИЗАЙН-СИСТЕМА И СТИЛИСТИКА

### Общая эстетика

**Стиль:** Современный минималистичный дизайн образовательной платформы
**Референсы:**
- https://adminrhs.github.io/Video-catalog/
- https://adminrhs.github.io/Design-system/
**Ключевые принципы:**
- Чистый, просторный layout с акцентом на контент
- Профессиональный, но дружелюбный интерфейс
- Плавные анимации и переходы
- Responsive design для всех устройств
- Dark/Light mode toggle

---

### 🎨 ЦВЕТОВАЯ СХЕМА

#### Light Mode (из обеих дизайн-систем)
```css
:root {
  /* Backgrounds */
  --bg-primary: #f7fafc;           /* Background Default */
  --bg-secondary: #ffffff;         /* Background Paper (white) */
  --bg-tertiary: #edf2f7;          /* Hover states */

  /* Text (из Design System) */
  --text-primary: #2d3748;         /* Text Primary (darker) */
  --text-secondary: #718096;       /* Text Secondary */
  --text-tertiary: #a0aec0;        /* Tertiary text */
  --text-contrast: #ffffff;        /* White text on dark backgrounds */

  /* Primary Colors (Game Academy Design System) */
  --color-primary: #4299e1;        /* Primary Main */
  --color-primary-light: #63b3ed;  /* Primary Light */
  --color-primary-dark: #3182ce;   /* Primary Dark */

  /* Semantic Colors */
  --color-secondary: #ed8936;      /* Secondary Orange */
  --color-success: #48BB78;        /* Success Green */
  --color-error: #d32f2f;          /* Error Red */
  --color-info: #0288d1;           /* Info Blue */

  /* Borders (Design System) */
  --border-color: #e0e0e0;         /* Standard borders */
  --border-hover: #cbd5e0;         /* Hover borders */

  /* Shadows (Game Academy Design System) */
  --shadow-light: 0 1px 3px rgba(0, 0, 0, 0.12);
  --shadow-card: 0 2px 8px rgba(0, 0, 0, 0.10);
  --shadow-medium: 0 3px 6px rgba(0, 0, 0, 0.16);
  --shadow-heavy: 0 10px 20px rgba(0, 0, 0, 0.19);
  --shadow-inset: inset 2px 2px 5px #e0e0e0, inset -2px -2px 5px #ffffff;

  /* Border Radius (Design System) */
  --radius-sm: 4px;      /* Small elements, tags */
  --radius-md: 8px;      /* Buttons, inputs */
  --radius-lg: 12px;     /* Cards, modals */
  --radius-xl: 16px;     /* Large containers */
  --radius-full: 50%;    /* Pills, avatars */
  --radius-pill: 20px;   /* Pill-shaped tags */
}
```

#### Dark Mode (из Design System)
```css
[data-theme="dark"] {
  /* Backgrounds (Design System) */
  --bg-primary: #1a202c;           /* Background Default (dark) */
  --bg-secondary: #1f2937;         /* Background Paper (dark gray) */
  --bg-tertiary: #374151;          /* Hover states */

  /* Text */
  --text-primary: #f7fafc;         /* Text Primary (white) */
  --text-secondary: #cbd5e0;       /* Text Secondary (lighter gray) */
  --text-tertiary: #9ca3af;        /* Tertiary text */
  --text-contrast: #1a202c;        /* Dark text on light backgrounds */

  /* Borders (Design System) */
  --border-color: #374151;         /* Borders (dark) */
  --border-hover: #4a5568;         /* Hover borders */

  /* Shadows (темнее для dark mode) */
  --shadow-light: 0 1px 3px rgba(0, 0, 0, 0.4);
  --shadow-card: 0 2px 8px rgba(0, 0, 0, 0.3);
  --shadow-medium: 0 3px 6px rgba(0, 0, 0, 0.4);
  --shadow-heavy: 0 10px 20px rgba(0, 0, 0, 0.5);
}
```

#### Department/Module Colors
```css
:root {
  /* Search Queue */
  --color-search: #6D28D9;         /* Deep Purple */
  --color-search-light: #A78BFA;   /* Light Purple (dark mode) */
  --color-search-bg: rgba(109, 40, 217, 0.15);

  /* Video Queue */
  --color-video: #147857;          /* Forest Green */
  --color-video-light: #34D399;    /* Light Green (dark mode) */
  --color-video-bg: rgba(20, 120, 87, 0.15);

  /* Transcriptions */
  --color-transcription: #4299e1;  /* Primary Blue */
  --color-transcription-light: #63b3ed;
  --color-transcription-bg: rgba(66, 153, 225, 0.15);

  /* Analysis */
  --color-analysis: #F97316;       /* Orange */
  --color-analysis-light: #FB923C;
  --color-analysis-bg: rgba(249, 115, 22, 0.15);

  /* Integration */
  --color-integration: #DC2626;    /* Bright Red */
  --color-integration-light: #F87171;
  --color-integration-bg: rgba(220, 38, 38, 0.15);

  /* Taxonomy */
  --color-taxonomy: #EC4899;       /* Hot Pink */
  --color-taxonomy-light: #F472B6;
  --color-taxonomy-bg: rgba(236, 72, 153, 0.15);
}
```

#### Status Colors
```css
:root {
  /* Success */
  --color-success: #10b981;
  --color-success-light: #34d399;
  --color-success-bg: rgba(16, 185, 129, 0.15);

  /* Warning */
  --color-warning: #f59e0b;
  --color-warning-light: #fbbf24;
  --color-warning-bg: rgba(245, 158, 11, 0.15);

  /* Error */
  --color-error: #ef4444;
  --color-error-light: #f87171;
  --color-error-bg: rgba(239, 68, 68, 0.15);

  /* Info */
  --color-info: #3b82f6;
  --color-info-light: #60a5fa;
  --color-info-bg: rgba(59, 130, 246, 0.15);
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

### 📐 TYPOGRAPHY (Game Academy Design System)

```css
/* Font Family (Roboto из Design System) */
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap');

:root {
  --font-primary: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI',
                  'Helvetica', 'Arial', sans-serif;
  --font-mono: 'Fira Code', 'Courier New', monospace;
}

/* Heading Sizes (из Design System) */
:root {
  --text-h1: 48px;        /* H1, line-height: 58px (1.208) */
  --text-h2: 40px;        /* H2, line-height: 48px (1.2) */
  --text-h3: 32px;        /* H3, line-height: 38px (1.188) */
  --text-h4: 28px;        /* H4, line-height: 34px (1.214) */
  --text-h5: 24px;        /* H5, line-height: 28px (1.167) */

  /* Body & Utility Sizes */
  --text-body: 16px;      /* B1/B2, line-height: 24px (1.5) */
  --text-body-sm: 14px;   /* B3, line-height: 20px (1.429) */
  --text-caption: 12px;   /* Caption, line-height: 16px (1.333) */

  /* Legacy naming (for compatibility) */
  --text-xs: 0.75rem;     /* 12px */
  --text-sm: 0.875rem;    /* 14px */
  --text-base: 1rem;      /* 16px */
  --text-lg: 1.125rem;    /* 18px */
  --text-xl: 1.25rem;     /* 20px */
  --text-2xl: 1.5rem;     /* 24px */
  --text-3xl: 1.875rem;   /* 30px */
  --text-4xl: 2.25rem;    /* 36px */
  --text-5xl: 3rem;       /* 48px */
}

/* Font Weights (Roboto weights) */
:root {
  --font-light: 300;
  --font-normal: 400;
  --font-medium: 500;
  --font-semibold: 600;
  --font-bold: 700;
}

/* Line Heights (из Design System) */
:root {
  --leading-h1: 58px;     /* 1.208 ratio */
  --leading-h2: 48px;     /* 1.2 ratio */
  --leading-h3: 38px;     /* 1.1875 ratio */
  --leading-h4: 34px;     /* 1.214 ratio */
  --leading-h5: 28px;     /* 1.167 ratio */
  --leading-body: 24px;   /* 1.5 ratio */
  --leading-body-sm: 20px;/* 1.429 ratio */
  --leading-caption: 16px;/* 1.333 ratio */

  /* Generic line heights */
  --leading-none: 1;
  --leading-tight: 1.25;
  --leading-snug: 1.375;
  --leading-normal: 1.5;
  --leading-relaxed: 1.625;
  --leading-loose: 2;
}
```

**Typography Hierarchy (Design System):**
```css
/* Headings (Design System specs) */
h1, .text-h1 {
  font-size: var(--text-h1);           /* 48px */
  font-weight: var(--font-semibold);   /* 600 */
  line-height: var(--leading-h1);      /* 58px */
  color: var(--text-primary);
}

h2, .text-h2 {
  font-size: var(--text-h2);           /* 40px */
  font-weight: var(--font-semibold);   /* 600 */
  line-height: var(--leading-h2);      /* 48px */
  color: var(--text-primary);
}

h3, .text-h3 {
  font-size: var(--text-h3);           /* 32px */
  font-weight: var(--font-semibold);   /* 600 */
  line-height: var(--leading-h3);      /* 38px */
  color: var(--text-primary);
}

h4, .text-h4 {
  font-size: var(--text-h4);           /* 28px */
  font-weight: var(--font-semibold);   /* 600 */
  line-height: var(--leading-h4);      /* 34px */
  color: var(--text-primary);
}

h5, .text-h5 {
  font-size: var(--text-h5);           /* 24px */
  font-weight: var(--font-semibold);   /* 600 */
  line-height: var(--leading-h5);      /* 28px */
  color: var(--text-primary);
}

/* Body Text (Design System) */
.text-body-regular {
  font-size: var(--text-body);         /* 16px - B1 */
  font-weight: var(--font-normal);     /* 400 */
  line-height: var(--leading-body);    /* 24px */
  color: var(--text-primary);
}

.text-body-medium {
  font-size: var(--text-body);         /* 16px - B2 */
  font-weight: var(--font-medium);     /* 500 */
  line-height: var(--leading-body);    /* 24px */
  color: var(--text-primary);
}

.text-body-small {
  font-size: var(--text-body-sm);      /* 14px - B3 */
  font-weight: var(--font-normal);     /* 400 */
  line-height: var(--leading-body-sm); /* 20px */
  color: var(--text-secondary);
}

/* Caption */
.text-caption {
  font-size: var(--text-caption);      /* 12px */
  font-weight: var(--font-normal);     /* 400 */
  line-height: var(--leading-caption); /* 16px */
  color: var(--text-tertiary);
}

/* Labels (uppercase, medium weight) */
.text-label {
  font-size: var(--text-body-sm);      /* 14px */
  font-weight: var(--font-medium);     /* 500 */
  line-height: var(--leading-body-sm); /* 20px */
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
```

---

### 📏 SPACING SYSTEM (Design System - 4px base)

```css
:root {
  /* Spacing Scale (4px base unit из Design System) */
  --space-0: 0;
  --space-xs: 4px;       /* xs */
  --space-sm: 8px;       /* sm */
  --space-md: 16px;      /* md */
  --space-lg: 24px;      /* lg */
  --space-xl: 32px;      /* xl */
  --space-2xl: 48px;     /* 2xl */
  --space-3xl: 64px;     /* 3xl */

  /* Legacy naming (for compatibility) */
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
- **Micro spacing** (1-2): Внутри компонентов, между иконками и текстом
- **Small spacing** (3-4): Между элементами внутри карточек
- **Medium spacing** (5-6): Между карточками, секциями
- **Large spacing** (8-12): Между крупными блоками
- **Extra large** (16-24): Page margins, section dividers

---

### 🎭 COMPONENT STYLING

#### 1. Buttons

```css
/* Primary Button */
.btn-primary {
  background: var(--color-transcription);
  color: #ffffff;
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  padding: var(--space-3) var(--space-6);
  border-radius: 0.5rem;
  border: none;
  box-shadow: var(--shadow-sm);
  cursor: pointer;
  transition: all 200ms ease-in-out;
}

.btn-primary:hover {
  background: #3182ce;
  box-shadow: var(--shadow-md);
  transform: translateY(-1px);
}

.btn-primary:active {
  transform: translateY(0);
  box-shadow: var(--shadow-sm);
}

.btn-primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Secondary Button */
.btn-secondary {
  background: var(--bg-secondary);
  color: var(--text-primary);
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  padding: var(--space-3) var(--space-6);
  border-radius: 0.5rem;
  border: 1px solid var(--border-color);
  box-shadow: var(--shadow-sm);
  cursor: pointer;
  transition: all 200ms ease-in-out;
}

.btn-secondary:hover {
  background: var(--bg-tertiary);
  border-color: var(--border-hover);
  box-shadow: var(--shadow-md);
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

#### 2. Cards

```css
/* Base Card */
.card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 0.75rem;
  padding: var(--space-6);
  box-shadow: var(--shadow-sm);
  transition: all 300ms ease-in-out;
}

.card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

/* Video Card (как на референсе) */
.video-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  transition: all 300ms ease-in-out;
  cursor: pointer;
}

.video-card:hover {
  box-shadow: var(--shadow-lg);
  transform: translateY(-4px);
}

.video-card-thumbnail {
  width: 100%;
  aspect-ratio: 16/9;
  object-fit: cover;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.video-card-content {
  padding: var(--space-4);
}

.video-card-title {
  font-size: var(--text-base);
  font-weight: var(--font-semibold);
  color: var(--text-primary);
  margin-bottom: var(--space-2);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.video-card-meta {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  font-size: var(--text-xs);
  color: var(--text-tertiary);
}

/* Search Task Card */
.search-task-card {
  background: var(--bg-secondary);
  border-left: 4px solid var(--color-search);
  border-radius: 0.5rem;
  padding: var(--space-5);
  box-shadow: var(--shadow-sm);
  transition: all 300ms ease-in-out;
}

.search-task-card:hover {
  box-shadow: var(--shadow-md);
  border-left-width: 6px;
}
```

#### 3. Badges

```css
/* Base Badge */
.badge {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  padding: var(--space-1) var(--space-3);
  font-size: var(--text-xs);
  font-weight: var(--font-medium);
  border-radius: 9999px;
  transition: all 200ms ease-in-out;
}

/* Status Badges */
.badge-success {
  background: var(--color-success-bg);
  color: var(--color-success);
  border: 1px solid var(--color-success);
}

.badge-warning {
  background: var(--color-warning-bg);
  color: var(--color-warning);
  border: 1px solid var(--color-warning);
}

.badge-error {
  background: var(--color-error-bg);
  color: var(--color-error);
  border: 1px solid var(--color-error);
}

.badge-info {
  background: var(--color-info-bg);
  color: var(--color-info);
  border: 1px solid var(--color-info);
}

/* Priority Badges */
.badge-priority-critical {
  background: var(--priority-critical-bg);
  color: var(--priority-critical);
  border: 1px solid var(--priority-critical);
}

.badge-priority-high {
  background: var(--priority-high-bg);
  color: var(--priority-high);
  border: 1px solid var(--priority-high);
}

.badge-priority-medium {
  background: var(--priority-medium-bg);
  color: var(--priority-medium);
  border: 1px solid var(--priority-medium);
}

.badge-priority-low {
  background: var(--priority-low-bg);
  color: var(--priority-low);
  border: 1px solid var(--priority-low);
}

/* Department Badges */
.badge-search {
  background: var(--color-search-bg);
  color: var(--color-search);
  border: 1px solid var(--color-search);
}

.badge-video {
  background: var(--color-video-bg);
  color: var(--color-video);
  border: 1px solid var(--color-video);
}

/* Dot Badge (notification counter) */
.badge-dot {
  width: 1.5rem;
  height: 1.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.625rem;
  font-weight: var(--font-bold);
  background: var(--color-error);
  color: white;
  border-radius: 9999px;
}
```

#### 4. Inputs

```css
/* Text Input */
.input {
  width: 100%;
  background: var(--bg-secondary);
  color: var(--text-primary);
  font-size: var(--text-sm);
  padding: var(--space-3) var(--space-4);
  border: 1px solid var(--border-color);
  border-radius: 0.5rem;
  transition: all 200ms ease-in-out;
}

.input:hover {
  border-color: var(--border-hover);
}

.input:focus {
  outline: none;
  border-color: var(--color-transcription);
  box-shadow: 0 0 0 3px var(--color-transcription-bg);
}

.input::placeholder {
  color: var(--text-tertiary);
}

/* Textarea */
.textarea {
  width: 100%;
  min-height: 8rem;
  background: var(--bg-secondary);
  color: var(--text-primary);
  font-size: var(--text-sm);
  padding: var(--space-3) var(--space-4);
  border: 1px solid var(--border-color);
  border-radius: 0.5rem;
  resize: vertical;
  transition: all 200ms ease-in-out;
}

.textarea:focus {
  outline: none;
  border-color: var(--color-transcription);
  box-shadow: 0 0 0 3px var(--color-transcription-bg);
}

/* Select Dropdown */
.select {
  width: 100%;
  background: var(--bg-secondary);
  color: var(--text-primary);
  font-size: var(--text-sm);
  padding: var(--space-3) var(--space-4);
  border: 1px solid var(--border-color);
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 200ms ease-in-out;
}

.select:hover {
  border-color: var(--border-hover);
}

.select:focus {
  outline: none;
  border-color: var(--color-transcription);
  box-shadow: 0 0 0 3px var(--color-transcription-bg);
}

/* Search Input (с иконкой) */
.search-input-wrapper {
  position: relative;
  width: 100%;
}

.search-input {
  width: 100%;
  padding-left: 2.75rem;
}

.search-input-icon {
  position: absolute;
  left: var(--space-3);
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-tertiary);
  pointer-events: none;
}
```

#### 5. Modals

```css
/* Modal Overlay */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  animation: fadeIn 200ms ease-in-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

/* Modal Content */
.modal {
  background: var(--bg-secondary);
  border-radius: 1rem;
  box-shadow: var(--shadow-xl);
  max-width: 90vw;
  max-height: 90vh;
  overflow: hidden;
  animation: slideUp 300ms ease-out;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Modal Sizes */
.modal-sm {
  width: 400px;
}

.modal-md {
  width: 600px;
}

.modal-lg {
  width: 800px;
}

.modal-xl {
  width: 1200px;
}

/* Modal Header */
.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-6);
  border-bottom: 1px solid var(--border-color);
}

.modal-title {
  font-size: var(--text-xl);
  font-weight: var(--font-semibold);
  color: var(--text-primary);
}

.modal-close {
  background: transparent;
  border: none;
  color: var(--text-secondary);
  cursor: pointer;
  padding: var(--space-2);
  border-radius: 0.5rem;
  transition: all 200ms ease-in-out;
}

.modal-close:hover {
  background: var(--bg-tertiary);
  color: var(--text-primary);
}

/* Modal Body */
.modal-body {
  padding: var(--space-6);
  overflow-y: auto;
  max-height: calc(90vh - 150px);
}

/* Modal Footer */
.modal-footer {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: var(--space-3);
  padding: var(--space-6);
  border-top: 1px solid var(--border-color);
}
```

#### 6. Sidebar Navigation

```css
/* Sidebar (как на референсе) */
.sidebar {
  position: fixed;
  left: 0;
  top: 0;
  bottom: 0;
  width: 16rem;
  background: var(--bg-secondary);
  border-right: 1px solid var(--border-color);
  transition: width 300ms ease-in-out;
  z-index: 100;
  overflow: hidden;
}

.sidebar.collapsed {
  width: 5rem;
}

/* Sidebar Header */
.sidebar-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-6);
  border-bottom: 1px solid var(--border-color);
}

.sidebar-logo {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  font-size: var(--text-xl);
  font-weight: var(--font-bold);
  color: var(--text-primary);
}

.sidebar.collapsed .sidebar-logo-text {
  display: none;
}

/* Sidebar Menu */
.sidebar-menu {
  padding: var(--space-4);
}

.sidebar-menu-item {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-3) var(--space-4);
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  color: var(--text-secondary);
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 200ms ease-in-out;
  text-decoration: none;
}

.sidebar-menu-item:hover {
  background: var(--bg-tertiary);
  color: var(--text-primary);
}

.sidebar-menu-item.active {
  background: var(--color-transcription-bg);
  color: var(--color-transcription);
}

.sidebar.collapsed .sidebar-menu-item-text {
  display: none;
}

/* Badge на пунктах меню */
.sidebar-menu-item-badge {
  margin-left: auto;
}

.sidebar.collapsed .sidebar-menu-item-badge {
  display: none;
}
```

#### 7. Tables

```css
/* Table Container */
.table-container {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: var(--shadow-sm);
}

/* Table */
.table {
  width: 100%;
  border-collapse: collapse;
}

.table thead {
  background: var(--bg-tertiary);
  border-bottom: 1px solid var(--border-color);
}

.table th {
  padding: var(--space-4) var(--space-5);
  text-align: left;
  font-size: var(--text-sm);
  font-weight: var(--font-semibold);
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.table td {
  padding: var(--space-4) var(--space-5);
  font-size: var(--text-sm);
  color: var(--text-primary);
  border-bottom: 1px solid var(--border-color);
}

.table tbody tr {
  transition: background 150ms ease-in-out;
}

.table tbody tr:hover {
  background: var(--bg-tertiary);
}

.table tbody tr:last-child td {
  border-bottom: none;
}
```

#### 8. Filters & Tabs

```css
/* Filter Buttons (как на референсе) */
.filter-group {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  flex-wrap: wrap;
}

.filter-button {
  background: transparent;
  color: var(--text-secondary);
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  padding: var(--space-2) var(--space-4);
  border: 1px solid var(--border-color);
  border-radius: 9999px;
  cursor: pointer;
  transition: all 200ms ease-in-out;
}

.filter-button:hover {
  background: var(--bg-tertiary);
  color: var(--text-primary);
  border-color: var(--border-hover);
}

.filter-button.active {
  background: var(--color-transcription-bg);
  color: var(--color-transcription);
  border-color: var(--color-transcription);
}

/* Department Filter Buttons */
.filter-button.department-search.active {
  background: var(--color-search-bg);
  color: var(--color-search);
  border-color: var(--color-search);
}

.filter-button.department-video.active {
  background: var(--color-video-bg);
  color: var(--color-video);
  border-color: var(--color-video);
}
```

#### 9. Scrollbar Styling

```css
/* Custom Scrollbar (как на референсе) */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: #f5f5f5;
  border-radius: 4px;
}

[data-theme="dark"] ::-webkit-scrollbar-track {
  background: #2d3748;
}

::-webkit-scrollbar-thumb {
  background: #e0e0e0;
  border-radius: 4px;
  transition: background 200ms ease;
}

[data-theme="dark"] ::-webkit-scrollbar-thumb {
  background: #424242;
}

::-webkit-scrollbar-thumb:hover {
  background: #cbd5e0;
}

[data-theme="dark"] ::-webkit-scrollbar-thumb:hover {
  background: #4a5568;
}
```

---

### ✨ ANIMATIONS & TRANSITIONS

```css
/* Плавные переходы (как на референсе) */
:root {
  --transition-fast: 150ms ease-in-out;
  --transition-base: 200ms ease-in-out;
  --transition-slow: 300ms ease-in-out;
  --transition-slower: 500ms ease-in-out;
}

/* Fade In Animation */
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

/* Slide Up Animation */
@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Slide Down Animation */
@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Scale In Animation */
@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

/* Spin Animation */
@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

/* Pulse Animation */
@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}

/* Wave Animation (для voice search, как на референсе) */
@keyframes fluid-wave {
  0%, 100% {
    transform: scaleY(0.1);
  }
  50% {
    transform: scaleY(1);
  }
}

.wave-bar {
  width: 4px;
  height: 100%;
  background: #63b3ed;
  border-radius: 2px;
  animation: fluid-wave 1.2s ease-in-out infinite;
}

.wave-bar:nth-child(1) { animation-delay: -1.4s; }
.wave-bar:nth-child(2) { animation-delay: -1.2s; }
.wave-bar:nth-child(3) { animation-delay: -1.0s; }
.wave-bar:nth-child(4) { animation-delay: -0.8s; }
.wave-bar:nth-child(5) { animation-delay: -0.6s; }
```

---

### 📱 RESPONSIVE DESIGN

```css
/* Breakpoints */
:root {
  --screen-sm: 640px;
  --screen-md: 768px;
  --screen-lg: 1024px;
  --screen-xl: 1280px;
  --screen-2xl: 1536px;
}

/* Mobile First Approach */

/* Mobile (default) */
.container {
  padding: var(--space-4);
}

.grid {
  display: grid;
  gap: var(--space-4);
  grid-template-columns: 1fr;
}

/* Tablet */
@media (min-width: 768px) {
  .container {
    padding: var(--space-6);
  }

  .grid {
    grid-template-columns: repeat(2, 1fr);
    gap: var(--space-6);
  }

  .sidebar {
    display: block;
  }

  .main-content {
    margin-left: 16rem;
  }

  .sidebar.collapsed + .main-content {
    margin-left: 5rem;
  }
}

/* Desktop */
@media (min-width: 1024px) {
  .container {
    padding: var(--space-8);
  }

  .grid {
    grid-template-columns: repeat(3, 1fr);
  }

  .modal-md {
    width: 700px;
  }

  .modal-lg {
    width: 900px;
  }
}

/* Large Desktop */
@media (min-width: 1280px) {
  .container {
    max-width: 1280px;
    margin: 0 auto;
  }

  .grid {
    grid-template-columns: repeat(4, 1fr);
  }
}
```

---

### 🎯 COMPONENT SPECIFIC DESIGNS

#### Search Results Modal (ключевой компонент)

```css
.search-results-modal {
  width: 900px;
  max-height: 90vh;
}

.search-results-header {
  padding: var(--space-6);
  border-bottom: 1px solid var(--border-color);
}

.search-results-title {
  font-size: var(--text-2xl);
  font-weight: var(--font-bold);
  color: var(--text-primary);
  margin-bottom: var(--space-2);
}

.search-results-subtitle {
  font-size: var(--text-sm);
  color: var(--text-secondary);
}

.search-results-actions {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-4) var(--space-6);
  background: var(--bg-tertiary);
  border-bottom: 1px solid var(--border-color);
}

.search-results-body {
  padding: var(--space-6);
  overflow-y: auto;
  max-height: calc(90vh - 250px);
}

.search-results-list {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

.search-result-item {
  display: flex;
  gap: var(--space-4);
  padding: var(--space-4);
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 0.75rem;
  transition: all 200ms ease-in-out;
  cursor: pointer;
}

.search-result-item:hover {
  background: var(--bg-tertiary);
  border-color: var(--color-transcription);
  box-shadow: var(--shadow-md);
}

.search-result-item.selected {
  background: var(--color-transcription-bg);
  border-color: var(--color-transcription);
  border-width: 2px;
}

.search-result-checkbox {
  flex-shrink: 0;
  width: 1.25rem;
  height: 1.25rem;
  margin-top: 0.25rem;
}

.search-result-thumbnail {
  flex-shrink: 0;
  width: 160px;
  aspect-ratio: 16/9;
  border-radius: 0.5rem;
  overflow: hidden;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.search-result-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.search-result-title {
  font-size: var(--text-base);
  font-weight: var(--font-semibold);
  color: var(--text-primary);
}

.search-result-channel {
  font-size: var(--text-sm);
  color: var(--text-secondary);
}

.search-result-meta {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  font-size: var(--text-xs);
  color: var(--text-tertiary);
}

.search-result-priority {
  margin-left: auto;
  flex-shrink: 0;
}

.search-results-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-6);
  border-top: 1px solid var(--border-color);
  background: var(--bg-tertiary);
}

.search-results-selected-count {
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  color: var(--text-secondary);
}
```

#### Priority Stars Display

```css
.priority-stars {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
}

.priority-star {
  font-size: var(--text-base);
  line-height: 1;
}

/* Priority 80-100: 5 stars (red) */
.priority-critical .priority-star {
  color: var(--priority-critical);
}

/* Priority 60-79: 4 stars (orange) */
.priority-high .priority-star {
  color: var(--priority-high);
}

/* Priority 40-59: 3 stars (yellow) */
.priority-medium .priority-star {
  color: var(--priority-medium);
}

/* Priority 20-39: 2 stars (light green) */
.priority-low .priority-star {
  color: var(--priority-low);
}

/* Priority 0-19: 1 star (green) */
.priority-verylow .priority-star {
  color: var(--priority-verylow);
}

.priority-number {
  font-size: var(--text-xs);
  font-weight: var(--font-medium);
  color: var(--text-secondary);
  margin-left: var(--space-1);
}
```

#### Dashboard Stats Cards

```css
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--space-6);
  margin-bottom: var(--space-8);
}

.stat-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 0.75rem;
  padding: var(--space-6);
  box-shadow: var(--shadow-sm);
  transition: all 200ms ease-in-out;
}

.stat-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

.stat-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: var(--space-3);
}

.stat-card-icon {
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.5rem;
  font-size: var(--text-xl);
}

.stat-card-icon.search {
  background: var(--color-search-bg);
  color: var(--color-search);
}

.stat-card-icon.video {
  background: var(--color-video-bg);
  color: var(--color-video);
}

.stat-card-value {
  font-size: var(--text-4xl);
  font-weight: var(--font-bold);
  color: var(--text-primary);
  line-height: 1;
  margin-bottom: var(--space-2);
}

.stat-card-label {
  font-size: var(--text-sm);
  color: var(--text-secondary);
  margin-bottom: var(--space-3);
}

.stat-card-change {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  font-size: var(--text-xs);
  font-weight: var(--font-medium);
  padding: var(--space-1) var(--space-2);
  border-radius: 9999px;
}

.stat-card-change.positive {
  background: var(--color-success-bg);
  color: var(--color-success);
}

.stat-card-change.negative {
  background: var(--color-error-bg);
  color: var(--color-error);
}
```

---

### 🌓 Dark Mode Toggle

```css
/* Dark Mode Toggle Button */
.theme-toggle {
  position: relative;
  width: 3.5rem;
  height: 2rem;
  background: var(--bg-tertiary);
  border: 1px solid var(--border-color);
  border-radius: 9999px;
  cursor: pointer;
  transition: all 200ms ease-in-out;
}

.theme-toggle:hover {
  background: var(--border-hover);
}

.theme-toggle-slider {
  position: absolute;
  top: 2px;
  left: 2px;
  width: 1.5rem;
  height: 1.5rem;
  background: white;
  border-radius: 9999px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 300ms ease-in-out;
  box-shadow: var(--shadow-sm);
}

[data-theme="dark"] .theme-toggle-slider {
  transform: translateX(1.5rem);
  background: var(--bg-primary);
}

.theme-toggle-icon {
  font-size: var(--text-xs);
}
```

---

## 🏗️ LAYOUT STRUCTURE

### Main Application Layout

```html
<div class="app" data-theme="light">
  <!-- Sidebar Navigation -->
  <aside class="sidebar">
    <div class="sidebar-header">
      <div class="sidebar-logo">
        <span class="sidebar-logo-icon">🔬</span>
        <span class="sidebar-logo-text">RESEARCHES 2</span>
      </div>
      <button class="btn-icon sidebar-toggle">
        <span>☰</span>
      </button>
    </div>

    <nav class="sidebar-menu">
      <a href="/dashboard" class="sidebar-menu-item active">
        <span class="sidebar-menu-item-icon">📊</span>
        <span class="sidebar-menu-item-text">Dashboard</span>
      </a>

      <a href="/search-queue" class="sidebar-menu-item">
        <span class="sidebar-menu-item-icon">🔍</span>
        <span class="sidebar-menu-item-text">Search Queue</span>
        <span class="sidebar-menu-item-badge badge-dot">5</span>
      </a>

      <a href="/video-queue" class="sidebar-menu-item">
        <span class="sidebar-menu-item-icon">📹</span>
        <span class="sidebar-menu-item-text">Video Queue</span>
        <span class="sidebar-menu-item-badge badge-dot">128</span>
      </a>

      <a href="/transcriptions" class="sidebar-menu-item">
        <span class="sidebar-menu-item-icon">📝</span>
        <span class="sidebar-menu-item-text">Transcriptions</span>
      </a>

      <a href="/analysis" class="sidebar-menu-item">
        <span class="sidebar-menu-item-icon">🔬</span>
        <span class="sidebar-menu-item-text">Analysis</span>
      </a>

      <a href="/integration" class="sidebar-menu-item">
        <span class="sidebar-menu-item-icon">🔗</span>
        <span class="sidebar-menu-item-text">Integration</span>
      </a>

      <a href="/taxonomy" class="sidebar-menu-item">
        <span class="sidebar-menu-item-icon">🗂️</span>
        <span class="sidebar-menu-item-text">Taxonomy</span>
      </a>
    </nav>

    <div class="sidebar-footer">
      <button class="theme-toggle">
        <span class="theme-toggle-slider">
          <span class="theme-toggle-icon">☀️</span>
        </span>
      </button>
    </div>
  </aside>

  <!-- Main Content Area -->
  <main class="main-content">
    <!-- Page Header -->
    <header class="page-header">
      <div class="page-header-left">
        <h1 class="page-title">Search Queue</h1>
        <p class="page-subtitle">Manage video search tasks and assignments</p>
      </div>
      <div class="page-header-right">
        <button class="btn-primary">
          <span>➕</span>
          <span>New Search Task</span>
        </button>
      </div>
    </header>

    <!-- Page Content -->
    <div class="page-content">
      <!-- Content goes here -->
    </div>
  </main>
</div>
```

---

## ⚡ ФУНКЦИОНАЛЬНЫЕ ТРЕБОВАНИЯ

### 1. Search Queue Module

**Страница: `/search-queue`**

**Компоненты:**
1. **Search Queue Dashboard**
   - List всех search tasks (карточки)
   - Filters: Status (All/Assigned/Completed), Department, Employee
   - Sort: By Date, By Priority
   - Search bar для поиска по topic

2. **Create Search Task Modal**
   - Form fields:
     - Employee (dropdown)
     - Department (dropdown)
     - Topic (text input)
     - Search Type (dropdown с промптами)
     - Custom Query (textarea, если Custom selected)
     - Notes (textarea)
   - Actions:
     - Cancel
     - Create & Execute

3. **Search Results Modal**
   - Header: "Search Results - SEARCH-XXX"
   - Found X videos
   - Select All / Deselect All buttons
   - Scrollable list of video results:
     - Checkbox для selection
     - Thumbnail preview
     - Video title
     - Channel name
     - Duration, views, upload date
     - Priority badge (⭐⭐⭐⭐⭐ 95)
   - Footer:
     - "X videos selected"
     - Cancel button
     - "Add Selected to Video Queue" button

4. **Search Task Card**
   - SEARCH-XXX ID
   - Topic title
   - Employee & Department
   - Status badge
   - Date assigned
   - Actions:
     - Execute Search
     - View Details
     - Complete

**Interactions:**
1. Click "New Search Task" → Open Create Modal
2. Fill form → Click "Create & Execute"
3. Backend executes search (YouTube API or AI)
4. Open Search Results Modal with found videos
5. User selects videos → Click "Add Selected to Video Queue"
6. Videos added to Video Queue
7. Search task status updated to "Completed"

**API Endpoints:**
- `GET /api/search-queue` - Get all tasks
- `POST /api/search-queue/create` - Create new task
- `POST /api/search-queue/:id/execute` - Execute search
- `POST /api/search-queue/:id/add-to-video-queue` - Add videos
- `PUT /api/search-queue/:id/complete` - Complete task

---

### 2. Video Queue Module

**Страница: `/video-queue`**

**Компоненты:**
1. **Video Queue Dashboard**
   - Stats cards:
     - Total videos
     - Queued
     - In Progress
     - Completed
   - Filter buttons:
     - Status (All/Queued/Selected/In_Progress/Completed)
     - Priority (All/Critical/High/Medium/Low)
     - Department
   - Sort dropdown:
     - By Priority (High to Low)
     - By Date Added (Newest First)
     - By Views
   - Grid/List view toggle
   - Export button (CSV/JSON/Markdown)

2. **Add Video Manually Modal**
   - YouTube URL input (with "Fetch Metadata" button)
   - Auto-filled fields from YouTube API:
     - Title
     - Channel
     - Duration
     - Views
     - Upload Date
     - Thumbnail preview
   - Manual fields:
     - Topic
     - Employee (dropdown)
     - Source
     - Notes
   - Auto-calculated priority display
   - Actions:
     - Cancel
     - Add to Queue

3. **Video Card**
   - VQ-XXX ID
   - Thumbnail image
   - Video title (2 lines max with ellipsis)
   - Channel name
   - Metadata row:
     - Duration (⏱ 18:42)
     - Views (👁 125K)
     - Upload date (📅 2025-11-28)
   - Topic tag
   - Employee name
   - Priority badge (⭐⭐⭐⭐⭐ 95)
   - Status badge
   - Actions:
     - View (opens YouTube in new tab)
     - Move to Phase 1
     - Edit
     - Delete

4. **Video Queue Stats Dashboard**
   - Priority Distribution (Pie Chart)
   - Videos by Department (Bar Chart)
   - Videos by Status (Donut Chart)
   - Recent Activity Timeline
   - Top Channels (List)

**Interactions:**
1. Click "Add Video Manually" → Open Add Video Modal
2. Paste YouTube URL → Click "Fetch Metadata"
3. Auto-fill metadata from YouTube API
4. Fill Topic, Employee → Auto-calculate priority
5. Click "Add to Queue" → Video added with VQ-XXX ID
6. Video appears in dashboard grid
7. Click "Move to Phase 1" → Create VIDEO-XXX, move to Transcriptions

**API Endpoints:**
- `GET /api/video-queue` - Get all videos
- `POST /api/video-queue/add` - Add video manually
- `POST /api/video-queue/add-batch` - Add multiple videos
- `GET /api/video-queue/:id/metadata` - Fetch YouTube metadata
- `PUT /api/video-queue/:id/priority` - Recalculate priority
- `PUT /api/video-queue/:id/status` - Update status
- `POST /api/video-queue/:id/move-to-phase-1` - Move to transcriptions
- `GET /api/video-queue/dashboard` - Get dashboard stats

---

### 3. Dashboard Module

**Страница: `/dashboard` (главная)**

**Компоненты:**
1. **Overview Stats**
   - 4 stat cards:
     - Total Videos Processed
     - Videos in Progress
     - Entities Extracted
     - Library Coverage %

2. **Recent Activity Feed**
   - Timeline of recent actions:
     - Search task created
     - Videos added to queue
     - Transcription completed
     - Integration done

3. **Quick Actions**
   - New Search Task
   - Add Video
   - View Queue
   - Generate Report

4. **Charts**
   - Processing Timeline (Gantt Chart)
   - Phase Distribution (Pie Chart)
   - Employee Performance (Bar Chart)

5. **Module Status Cards**
   - Search Queue: X tasks active
   - Video Queue: X videos queued
   - Transcriptions: X in progress
   - Analysis: X completed
   - Integration: X pending
   - Taxonomy: X entities total

---

## 🎭 INTERACTIVE BEHAVIORS

### Hover States
- All buttons: slight scale (1.02) + shadow increase
- All cards: translateY(-2px) + shadow increase
- Sidebar items: background color change
- Links: color change + underline

### Loading States
- Button: show spinner + disable
- Modal: skeleton loader while fetching
- Cards: pulse animation while loading

### Empty States
- Empty search results: illustration + "No videos found" message
- Empty queue: illustration + "No videos yet" + "Add Video" CTA
- Empty tasks: illustration + "No tasks assigned" + "Create Task" CTA

### Error States
- Form validation: red border + error message below field
- API error: toast notification (top-right)
- Network error: banner at top with retry button

### Success States
- Task created: green toast notification
- Videos added: green toast + auto-close after 3s
- Action completed: checkmark animation

---

## 📦 ТЕХНИЧЕСКИЕ ТРЕБОВАНИЯ

### Frontend Stack
- **Framework:** React 18 + TypeScript
- **Styling:** Tailwind CSS 3 (configured with design tokens above)
- **UI Components:** shadcn/ui (pre-configured)
- **State Management:** Zustand
- **Data Fetching:** React Query (TanStack Query)
- **Routing:** React Router v6
- **Icons:** Lucide React или Heroicons
- **Charts:** Recharts
- **Animations:** Framer Motion

### Backend Stack
- **Runtime:** Node.js 18+
- **Framework:** Express.js 4
- **APIs:**
  - Google Sheets API (для хранения)
  - Dropbox API (для файлов)
  - YouTube Data API v3 (для метаданных)
  - OpenAI API (optional, для AI search)

### File Structure
```
researches-app/
├── client/                    # Frontend
│   ├── src/
│   │   ├── components/
│   │   │   ├── ui/            # shadcn/ui base components
│   │   │   ├── search-queue/
│   │   │   ├── video-queue/
│   │   │   ├── dashboard/
│   │   │   └── common/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── hooks/
│   │   ├── store/
│   │   ├── styles/
│   │   │   ├── globals.css    # CSS variables above
│   │   │   └── components.css # Component styles
│   │   └── App.tsx
│   └── package.json
│
├── server/                    # Backend
│   ├── src/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── utils/
│   │   └── app.js
│   └── package.json
│
└── README.md
```

---

## 🎯 ПРИОРИТЕТ РАЗРАБОТКИ

### Phase 1: Core Design System (1-2 days)
1. Setup Tailwind CSS с всеми CSS variables
2. Создать base components (Button, Badge, Input, Modal, Card)
3. Настроить dark mode toggle
4. Создать sidebar navigation layout
5. Responsive breakpoints

### Phase 2: Search Queue (2-3 days)
1. Search Queue Dashboard
2. Create Search Task Modal
3. Search Results Modal (ключевой компонент!)
4. Backend API integration
5. YouTube search integration

### Phase 3: Video Queue (2-3 days)
1. Video Queue Dashboard
2. Add Video Manual Modal
3. Video Cards with priority system
4. Stats Dashboard
5. YouTube metadata integration

### Phase 4: Dashboard & Polish (1-2 days)
1. Main Dashboard
2. Charts & visualizations
3. Polish animations
4. Test dark mode
5. Responsive testing

---

## ✅ КРИТЕРИИ ГОТОВНОСТИ

### Дизайн
- ✅ Соответствует референсу: https://adminrhs.github.io/Video-catalog/
- ✅ Dark/Light mode работает корректно
- ✅ Все цвета из палитры department colors используются
- ✅ Smooth transitions (300ms) на всех элементах
- ✅ Responsive на всех устройствах
- ✅ Custom scrollbar styling применен

### Функционал
- ✅ Search Queue: создание, выполнение, результаты
- ✅ Video Queue: добавление, приоритизация, статусы
- ✅ Modals: открытие, закрытие, overlay
- ✅ API integration: все endpoints работают
- ✅ YouTube API: метаданные загружаются
- ✅ Priority Calculator: корректный расчет 0-100

### UX
- ✅ Все hover states работают
- ✅ Loading states показываются
- ✅ Error handling реализован
- ✅ Success notifications показываются
- ✅ Empty states с CTA кнопками
- ✅ Smooth scrolling

---

## 📝 ПРИМЕЧАНИЯ ДЛЯ AI

1. **Строго следуй дизайну референса** - цвета, spacing, typography, animations
2. **Используй все CSS variables** - не hardcode values
3. **Обязательно dark mode** - переключение должно работать везде
4. **Search Results Modal - ключевой компонент** - максимум внимания
5. **Priority system важен** - звезды должны отображаться корректно
6. **Responsive обязателен** - mobile, tablet, desktop
7. **Smooth animations** - все transitions 200-300ms
8. **Department colors** - каждый модуль имеет свой цвет
9. **shadcn/ui** - используй их компоненты как base
10. **TypeScript** - строгая типизация везде

---

## 🚀 КОМАНДЫ ДЛЯ СТАРТА

```bash
# Backend
cd server
npm install
npm run dev

# Frontend
cd client
npm install
npm run dev

# Open browser
http://localhost:3000
```

---

**КОНЕЦ ПРОМПТА**

*Этот промпт содержит полное описание дизайна, стилей, компонентов и функционала для генерации приложения RESEARCHES 2 с дизайном как на https://adminrhs.github.io/Video-catalog/*

**Готов к использованию в AI! 🎨✨**
