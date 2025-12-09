# DESIGN SYSTEM REFERENCE (Insert at top of each prompt)

---

## 🎨 DESIGN SYSTEM v1.0 (October 2025)

**References:**
- **Video Catalog**: https://adminrhs.github.io/Video-catalog/
- **Design System**: https://adminrhs.github.io/Design-system/
- **Complete JSON**: `./design-system.json` ← **USE THIS AS SINGLE SOURCE OF TRUTH**
- **Integration Guide**: `./DESIGN-SYSTEM-INTEGRATION-GUIDE.md`
- **Analysis Report**: `./design-system-analysis.md`

---

### ⚡ QUICK REFERENCE

**DO**:
```typescript
import designSystem from './design-system.json';
const buttonColor = designSystem.designSystem.colorPalette.systemColors.light.primary.default;
```

**DON'T**:
```typescript
const buttonColor = '#2563EB';  // ❌ Never hardcode!
```

---

### 📊 KEY VALUES (From JSON)

**Colors:**
- Primary: #2563EB (hover: #3B82F6, active: #1D4ED8)
- Search Module: #6D28D9 (Designers Purple)
- Video Module: #147857 (Developers Green)
- Priority Critical: #DC2626, High: #EA580C, Medium: #F59E0B, Low: #84CC16, Very Low: #22C55E

**Typography:**
- Font: Roboto (weights: 300, 400, 500, 600, 700)
- H1: 48px/600/58px line-height
- H2: 40px/600/48px line-height
- Body: 16px/400/24px line-height
- Caption: 12px/400/16px line-height

**Spacing:**
- Base: 4px
- xs: 4px, sm: 8px, md: 16px, lg: 24px, xl: 32px, 2xl: 48px, 3xl: 64px

**Border Radius:**
- Buttons: 8px (lg)
- Cards/Inputs: 12px (xl)
- Tags: 20px (pill)

**Shadows:**
- sm: 0 1px 3px rgba(0,0,0,0.12)
- md: 0 2px 8px rgba(0,0,0,0.10)
- lg: 0 3px 6px rgba(0,0,0,0.16)
- xl: 0 10px 20px rgba(0,0,0,0.19)

**Transitions:**
- Fast: 150ms ease-in-out
- Normal: 300ms ease-in-out
- Slow: 500ms ease-in-out

**Components Specs:**
- Button padding (md): 10px 20px
- Input padding (md): 12px 16px
- Sidebar width: 256px (expanded), 80px (collapsed)
- Sidebar bg: #1F2937 (dark even in light theme!)
- Scrollbar width: 6px

---

### 🎯 PIXEL-PERFECT CHECKLIST

- [ ] All values from `design-system.json`, no hardcoded values
- [ ] Dark mode supported (light + dark variants)
- [ ] Module colors applied (#6D28D9 for Search, #147857 for Video)
- [ ] Roboto font loaded (300, 400, 500, 600, 700)
- [ ] Spacing uses 4px base unit
- [ ] Border radius: buttons 8px, cards/inputs 12px
- [ ] Shadows from design system
- [ ] Transitions: 150ms/300ms/500ms ease-in-out
- [ ] Sidebar is #1F2937 (dark) even in light theme
- [ ] Scrollbar is 6px width
- [ ] All states: default, hover, active, focus, disabled

---

**📦 INTEGRATION**: See `DESIGN-SYSTEM-INTEGRATION-GUIDE.md` for complete implementation examples

---
