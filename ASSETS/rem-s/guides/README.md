# 📚 Guides - Документація для роботи з REM-S проектом

## 📂 Структура документації

### 🤖 AI Workflows

1. **[AI_COLLECTIONS_WORKFLOW.md](AI_COLLECTIONS_WORKFLOW.md)**
   - Повна інструкція для AI про роботу з колекціями Strapi
   - Автоматизація експорту/імпорту вакансій, категорій тощо
   - Порційна відправка великої кількості файлів
   - Типові помилки та їх вирішення
   - **Для:** AI асистент

2. **[AI_PAGES_WORKFLOW.md](AI_PAGES_WORKFLOW.md)**
   - Інструкція для AI про роботу з окремими сторінками (Pages)
   - Експорт/імпорт контенту сторінок
   - **Для:** AI асистент

---

### 📖 Collections (Колекції Strapi)

Документація для роботи з колекціями (вакансії, категорії тощо):

**Папка:** [`collections/`](collections/)

1. **[collections/AI_COLLECTIONS_WORKFLOW.md](collections/AI_COLLECTIONS_WORKFLOW.md)**
   - AI інструкція з детальними сценаріями
   - Експорт, створення, оновлення, видалення вакансій
   - Порційна відправка
   - **Для:** AI асистент (основний гайд)

2. **[collections/MANUAL_COLLECTIONS_GUIDE.md](collections/MANUAL_COLLECTIONS_GUIDE.md)**
   - Мануальна робота з колекціями
   - Для технічних спеціалістів
   - Робота напряму з JSON файлами
   - **Для:** Технічні користувачі

3. **[collections/ДЛЯ_КОРИСТУВАЧІВ.md](collections/ДЛЯ_КОРИСТУВАЧІВ.md)**
   - Спрощена інструкція для нетехнічних користувачів
   - Робота через чат з AI
   - **Для:** Рекрутери, контент-менеджери

4. **[collections/README.md](collections/README.md)**
   - Загальний огляд документації по колекціях
   - Швидкі посилання

---

### 📝 Формати даних

**[STRAPI_API_FORMAT.md](STRAPI_API_FORMAT.md)**
- Повна специфікація форматів для Strapi API
- Relations (categories, skills, keyword_tags)
- Components (products, responsibilities, tools)
- Типові помилки та їх вирішення
- Результати тестування
- **Для:** Розробники, AI асистент

---

## 🚀 Швидкий старт

### Для AI асистента:
1. Читай **[collections/AI_COLLECTIONS_WORKFLOW.md](collections/AI_COLLECTIONS_WORKFLOW.md)** перед роботою
2. Використовуй **[STRAPI_API_FORMAT.md](STRAPI_API_FORMAT.md)** як довідник форматів

### Для розробників:
1. Ознайомся з **[STRAPI_API_FORMAT.md](STRAPI_API_FORMAT.md)**
2. При потребі використовуй **[collections/MANUAL_COLLECTIONS_GUIDE.md](collections/MANUAL_COLLECTIONS_GUIDE.md)**

### Для рекрутерів/контент-менеджерів:
1. Читай **[collections/ДЛЯ_КОРИСТУВАЧІВ.md](collections/ДЛЯ_КОРИСТУВАЧІВ.md)**
2. Працюй через чат з AI
3. **Ніколи не редагуй файли вручну!**

---

## ⚠️ Важливі правила

### Папки:
- ✅ **`updated/`** - ТІЛЬКИ тут робити зміни!
- ❌ **`exported/`** - НЕ чіпати! Резервна копія з сайту

### Формати:
- ✅ `categories: 14` (число для single relation)
- ❌ `categories: [14]` (масив НЕ працює!)
- ✅ Components БЕЗ поля `id`

### Відправка:
- ✅ Якщо файлів 50+ - порційна відправка
- ✅ Команди працюють на всіх платформах (Windows/Mac/Linux)

---

## 📊 Структура проекту

```
ENTITIES/ASSETS/rem-s/
├── guides/                          ← ВИ ТУТ
│   ├── README.md                    ← Цей файл
│   ├── STRAPI_API_FORMAT.md         ← Формати даних
│   ├── AI_PAGES_WORKFLOW.md         ← AI для Pages
│   └── collections/                 ← Документація колекцій
│       ├── AI_COLLECTIONS_WORKFLOW.md     ← AI інструкція (основна)
│       ├── MANUAL_COLLECTIONS_GUIDE.md    ← Мануальна робота
│       ├── ДЛЯ_КОРИСТУВАЧІВ.md            ← Для нетехнічних
│       └── README.md
│
├── scripts/                         ← Скрипти Node.js
│   ├── collections-export/          ← Експорт з Strapi
│   ├── collections-update/          ← Відправка на Strapi
│   ├── pages-export/
│   └── pages-update/
│
├── exported/                        ← Дані з сайту (НЕ редагувати!)
│   └── collections/
│
└── updated/                         ← Робоча папка (редагувати ТУТ!)
    └── collections/
```

---

## 🔗 Корисні посилання

- **Strapi Admin:** https://strapi.rem-s.com/admin
- **Сайт:** https://rem-s.com
- **Node.js:** https://nodejs.org/

---

**Остання оновлення:** 2025-12-02















