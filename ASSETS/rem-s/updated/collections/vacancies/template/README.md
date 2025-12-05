# Темплейт вакансії для Strapi API

## 📄 Файл: `vacancy-template-filled-example.json`

Цей темплейт використовується для створення нових вакансій через Strapi API.

---

## ⚠️ КРИТИЧНО ВАЖЛИВО: Формат полів

### ✅ ПРАВИЛЬНА структура

Темплейт має відповідати точному формату, який очікує Strapi API:

```json
{
  "id": null,
  "attributes": {
    "title": "string",
    "description": "string (Markdown)",
    "locale": "uk|en|ru|pl",
    "vacancySlug": "string",
    "cardDescription": "string",
    "titleH1": "string",
    "subTitle": "string",
    "isHot": false,
    "newVersion": null,
    "productsTitle": null,
    "responsibilityTitle": null,
    "toolsTitle": null,
    "formTitle": "",
    "videoLink": "",
    "categories": 48,
    "keyword_tags": [],
    "skills": [],
    "videoPreview": null,
    "products": [],
    "responsibilities": [],
    "tools": [],
    "seoData": null,
    "localizations": []
  }
}
```

---

## 🔗 Relations (зв'язки з іншими колекціями)

### ⚠️ КРИТИЧНО: Формат categories - ЧИСЛО, НЕ МАСИВ!

Relations передаються по-різному:
- **categories** (single relation) - **ТІЛЬКИ ЧИСЛО**
- **keyword_tags, skills** (many relations) - **МАСИВИ**

#### ✅ ПРАВИЛЬНО:
```json
"categories": 48,           // ✅ Число для single relation
"keyword_tags": [],         // ✅ Масив для many relation
"skills": [],               // ✅ Масив для many relation
"localizations": []         // ✅ Масив
```

#### ❌ НЕПРАВИЛЬНО:
```json
// НЕ ТАК - categories як масив:
"categories": [48]  // ❌ НЕ ЗБЕРІГАЄТЬСЯ!

// НЕ ТАК - з обгорткою data:
"categories": { "data": [{ "id": 48 }] }

// НЕ ТАК - з attributes:
"categories": { "data": [{ "id": 48, "attributes": {...} }] }
```

**ВАЖЛИВО:** Якщо відправити `"categories": [48]`, Strapi прийме запит (200 OK), але **НЕ ЗБЕРЕЖЕ** категорію!

---

## 🆔 ID категорій по мовах

### Українська (uk)
- developers: `48`
- designers: `47`
- translators: `49`
- managers: `50`
- marketers: `51`
- tutors: `52`
- other: `53`

### Англійська (en)
- developers: `11`
- designers: `16`
- translators: `12`
- managers: `14`
- marketers: `15`
- tutors: `13`
- other: `45`

### Російська (ru)
- developers: `25`
- designers: `24`
- translators: `26`
- managers: `27`
- marketers: `28`
- tutors: `29`
- other: `43`

### Польська (pl)
- developers: `30`
- designers: `34`
- translators: `31`
- managers: `32`
- marketers: `33`
- tutors: `39`

---

## 📦 Компоненти (динамічні зони)

### products, responsibilities, tools

Ці поля - масиви об'єктів БЕЗ ID:

#### ✅ ПРАВИЛЬНО:
```json
"products": [
  {
    "productTitle": "Назва продукту",
    "productText": "Опис продукту"
  }
]

"responsibilities": [
  {
    "responsibilityLi": "Обов'язок 1"
  }
]

"tools": [
  {
    "toolText": "Інструмент 1"
  }
]
```

#### ❌ НЕПРАВИЛЬНО:
```json
// НЕ ТАК - з ID:
"products": [
  {
    "id": null,
    "productTitle": "...",
    "productText": "..."
  }
]
```

**ПРАВИЛО:** Для нових записів компоненти створюються БЕЗ `id`. Strapi сам додасть ID після створення.

---

## 📝 SEO дані

### Формат: об'єкт БЕЗ ID або null

#### ✅ ПРАВИЛЬНО:
```json
// Якщо SEO немає:
"seoData": null

// Якщо SEO є:
"seoData": {
  "seoTitle": "Заголовок для SEO",
  "seoDescription": "Опис для SEO"
}
```

#### ❌ НЕПРАВИЛЬНО:
```json
// НЕ ТАК - з ID:
"seoData": {
  "id": null,
  "seoTitle": "...",
  "seoDescription": "..."
}
```

---

## 🎬 Медіа поля

### videoPreview: завжди null

```json
"videoPreview": null
```

**Примітка:** Медіа файли завантажуються окремо через Strapi Media Library.

---

## 🌐 Локалізації

### localizations: завжди порожній масив для нових вакансій

```json
"localizations": []
```

**Примітка:** Локалізації створюються автоматично Strapi після публікації основної вакансії.

---

## ❗ Часті помилки

### 1. Categories не зберігаються - відправлено як масив
```json
// ❌ НЕПРАВИЛЬНО (200 OK, але НЕ зберігається):
"categories": [48]

// ✅ ПРАВИЛЬНО:
"categories": 48
```

### 2. Помилка 500: категорія з attributes
```json
// ❌ НЕПРАВИЛЬНО:
"categories": { "data": [{ "id": 48, "attributes": {...} }] }

// ✅ ПРАВИЛЬНО:
"categories": 48
```

### 3. Помилка 400: неправильний ID категорії
```json
// ❌ НЕПРАВИЛЬНО (uk, але ID з en):
"locale": "uk",
"categories": [11]  // це ID для en!

// ✅ ПРАВИЛЬНО:
"locale": "uk",
"categories": [48]  // правильний ID для uk
```

### 4. Помилка 500: компоненти з ID
```json
// ❌ НЕПРАВИЛЬНО:
"products": [{ "id": null, "productTitle": "...", "productText": "..." }]

// ✅ ПРАВИЛЬНО:
"products": [{ "productTitle": "...", "productText": "..." }]
```

---

## 🔍 Як перевірити правильність темплейту

1. **categories, keyword_tags, skills, localizations** - масиви чисел (ID) або порожні масиви
2. **products, responsibilities, tools** - масиви об'єктів БЕЗ поля `id`
3. **seoData** - об'єкт БЕЗ поля `id` або `null`
4. **videoPreview** - завжди `null`
5. **isHot** - boolean (`true` або `false`)
6. **newVersion, productsTitle, responsibilityTitle, toolsTitle** - `null` або рядок
7. **formTitle, videoLink** - порожній рядок або рядок

---

## 📚 Додаткова інформація

- Скрипт `script-collections-update.js` автоматично витягує `attributes` з файлу
- Strapi API очікує формат: `{ data: attributes }`
- ID вакансії (`id: null`) створюється автоматично на бекенді
- Timestamps (`createdAt`, `updatedAt`, `publishedAt`) встановлюються автоматично

---

**Останнє оновлення:** 2025-12-02


