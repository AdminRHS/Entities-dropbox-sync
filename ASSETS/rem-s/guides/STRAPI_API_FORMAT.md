# Правильний формат даних для Strapi API

## ✅ ПРАВИЛЬНИЙ формат для PUT/POST запитів

### 1. **Relations (зв'язки)** - ТІЛЬКИ ID як NUMBER

```json
{
  "categories": 14,          // ✅ Число, НЕ масив!
  "keyword_tags": [],        // ✅ Порожній масив OK
  "skills": [],              // ✅ Порожній масив OK
  "localizations": []        // ✅ Порожній масив OK
}
```

❌ **НЕПРАВИЛЬНО:**
```json
{
  "categories": [14],                              // ❌ Масив - НЕ працює
  "categories": {"data": [{"id": 14}]},           // ❌ Об'єкт - НЕ працює
  "categories": [{"id": 14, "attributes": {...}}] // ❌ Повний об'єкт - НЕ працює
}
```

---

### 2. **Components (компоненти)** - БЕЗ поля `id`

#### ✅ ПОРОЖНІ компоненти - OK:
```json
{
  "products": [],
  "responsibilities": [],
  "tools": [],
  "seoData": null,
  "videoPreview": null
}
```

#### ✅ ЗАПОВНЕНІ компоненти - БЕЗ `id`:
```json
{
  "products": [
    { "productText": "Product 1" },
    { "productText": "Product 2" }
  ],
  "responsibilities": [
    { "responsibilityLi": "Responsibility 1" },
    { "responsibilityLi": "Responsibility 2" }
  ],
  "tools": [
    { "toolText": "Tool 1" },
    { "toolText": "Tool 2" }
  ]
}
```

❌ **НЕПРАВИЛЬНО:**
```json
{
  "products": [
    { "id": null, "productText": "Product 1" }  // ❌ id: null викликає 400 помилку!
  ]
}
```

**Помилка:** `"Some of the provided components in products are not related to the entity"`

---

### 3. **Повний приклад правильної структури**

```json
{
  "data": {
    "title": "Project Manager",
    "description": "Full description...",
    "isHot": false,
    "subTitle": "Join our team",
    "vacancySlug": "project-manager",
    "locale": "en",
    "formTitle": "Apply now",
    "videoLink": "https://youtu.be/...",
    "cardDescription": "Short description",
    "titleH1": "Project Manager Position",
    "newVersion": null,
    "productsTitle": "What You'll Deliver",
    "responsibilityTitle": "Your Key Responsibilities",
    "toolsTitle": "Tools & Technologies",
    
    "categories": 14,           // ✅ Число
    "keyword_tags": [],         // ✅ Порожній масив
    "skills": [],               // ✅ Порожній масив
    
    "products": [],             // ✅ Порожній масив або масив об'єктів БЕЗ id
    "responsibilities": [],     // ✅ Порожній масив або масив об'єктів БЕЗ id
    "tools": [],                // ✅ Порожній масив або масив об'єктів БЕЗ id
    
    "seoData": null,            // ✅ null OK
    "videoPreview": null,       // ✅ null OK
    "localizations": []         // ✅ Порожній масив
  }
}
```

---

## 🔍 Результати тестів

| Тест | Формат | Результат |
|------|--------|-----------|
| 1 | `categories: 14` (число) | ✅ 200 OK |
| 2 | `categories: [14]` (масив) | ❌ Категорія НЕ зберігається |
| 3 | Порожні компоненти `[]` | ✅ 200 OK |
| 4 | Компоненти БЕЗ `id` | ✅ 200 OK |
| 5 | Компоненти З `id: null` | ❌ 400 Error |

---

## 📝 Рекомендації для скриптів

### При експорті з Strapi (GET):
Strapi повертає relations у форматі:
```json
{
  "categories": {
    "data": [
      { "id": 14, "attributes": {...} }
    ]
  }
}
```

### При відправці в Strapi (PUT/POST):
Треба конвертувати в простий формат:
```javascript
// Конвертація categories
if (data.categories?.data) {
  data.categories = data.categories.data[0]?.id || null;
}

// Видалення id: null з компонентів
if (Array.isArray(data.products)) {
  data.products = data.products.map(item => {
    const { id, ...rest } = item;
    return rest;
  });
}
```

---

## ⚠️ Типові помилки

### 400 Error: "Some of the provided components..."
**Причина:** Компоненти містять `id: null`  
**Рішення:** Видалити поле `id` з компонентів

### 500 Internal Server Error
**Причина:** Неправильний формат relations або компонентів  
**Рішення:** Перевірити формат categories (має бути число, не масив)

### Categories не зберігаються
**Причина:** Відправка `categories: [14]` замість `categories: 14`  
**Рішення:** Конвертувати масив у число

---

**Дата створення:** 2025-12-02  
**Версія Strapi:** 4.x  
**Тестовано на:** rem-s.com API

