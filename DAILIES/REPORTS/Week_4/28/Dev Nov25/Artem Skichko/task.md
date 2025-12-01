# Task Breakdown - [29.11.2025]

## Instructions
**What**: Detailed action steps
**Include**:
- Break each plan item into specific steps
- Add links and resources
- Clear instructions for execution

---

## Task 1: Розширити скрипт оновлення для всіх single types

**Priority:** High | **Estimated Time:** 1-2 hours

### Steps:
1. Відкрити файл `strapi-single-types-update.js` в редакторі
2. Знайти функцію `scanUpdatedFiles()` (приблизно рядок 69)
3. Видалити обмеження на About entity (видалити фільтр `const aboutType = SINGLE_TYPES.find(...)`)
4. Відновити цикл по всіх `SINGLE_TYPES` замість обробки тільки About
5. Оновити коментарі в функції, щоб відображали обробку всіх типів
6. Зберегти файл та перевірити синтаксис: `node -c strapi-single-types-update.js`
7. Запустити dry-run тест: `node strapi-single-types-update.js --dry-run`
8. Перевірити, що скрипт знаходить файли для всіх 10 single types

### Resources and Links:
- Файл: `Dropbox/ENTITIES/ASSETS/rem-s/scripts/pages-export/strapi-single-types-update.js`
- Документація: `Dropbox/ENTITIES/ASSETS/rem-s/scripts/pages-export/README-UPDATE.md`
- Приклад роботи: `Dropbox/ENTITIES/ASSETS/rem-s/scripts/pages-export/logs/update-2025-11-28T15-29-16-930Z.log`

### Instructions:
- Використовувати dry-run режим для тестування перед реальними змінами
- Перевірити, що всі 10 single types присутні в `SINGLE_TYPES` масиві
- Звернути увагу на структуру папок `updated/pages/{Entity}/` - всі мають містити файли для 4 локалей

---

## Task 2: Протестувати оновлення для Contact, Footer, Header, Home

**Priority:** High | **Estimated Time:** 1-2 hours

### Steps:
1. Перевірити наявність файлів у `updated/pages/Contact/`, `updated/pages/Footer/`, `updated/pages/Header/`, `updated/pages/Home/`
2. Переконатися, що кожна папка містить файли для всіх 4 локалей (en.json, uk.json, pl.json, ru.json)
3. Запустити dry-run тест для цих entity: `node strapi-single-types-update.js --dry-run`
4. Перевірити лог-файл на наявність помилок або попереджень
5. Якщо все добре, запустити реальне оновлення з backup: `node strapi-single-types-update.js --confirm --backup <token>`
6. Спостерігати за процесом оновлення, перевіряти повідомлення в консолі
7. Перевірити лог-файл після завершення: `logs/update-{timestamp}.log`
8. Перевірити в Strapi адмін-панелі, що дані оновилися коректно
9. Якщо використано `--export-after`, перевірити, що експорт виконався успішно

### Resources and Links:
- Папка з файлами: `Dropbox/ENTITIES/ASSETS/rem-s/updated/pages/`
- Логи: `Dropbox/ENTITIES/ASSETS/rem-s/scripts/pages-export/logs/`
- Strapi адмін: `https://strapi.rem-s.com/admin`
- API токен: (збережений в daily.md)

### Instructions:
- **ВАЖЛИВО:** Завжди використовувати `--backup` при реальних оновленнях
- Перевіряти кожен entity окремо, не всі разом
- Якщо виникають помилки, перевірити структуру JSON файлів
- Переконатися, що системні поля (createdAt, updatedAt, id) видалені перед оновленням

---

## Task 3: Перевірити логування та коректність оновлень

**Priority:** High | **Estimated Time:** 30-60 minutes

### Steps:
1. Відкрити останній лог-файл у папці `logs/`
2. Перевірити, що всі операції залоговані з timestamp
3. Перевірити наявність повідомлень про успішні оновлення
4. Перевірити, що немає помилок або попереджень
5. Порівняти кількість оновлених файлів з очікуваною
6. Перевірити в Strapi, що дані відображаються коректно для кожної локалі
7. Перевірити фронтенд (якщо доступний), що дані завантажуються правильно
8. Якщо є помилки, проаналізувати їх та виправити

### Resources and Links:
- Логи: `Dropbox/ENTITIES/ASSETS/rem-s/scripts/pages-export/logs/`
- Скрипт: `Dropbox/ENTITIES/ASSETS/rem-s/scripts/pages-export/strapi-single-types-update.js`
- Strapi API: `https://strapi.rem-s.com/api/`

### Instructions:
- Звернути увагу на формат логів: `[timestamp] message`
- Перевірити кольорове форматування в консолі (info, success, error, warning)
- Якщо є помилки, перевірити структуру даних у JSON файлах
- Документувати будь-які проблеми для подальшого вирішення

---

## Task 4: Розробити скрипт експорту для collection types

**Priority:** Medium | **Estimated Time:** 3-4 hours

### Steps:
1. Створити новий файл `strapi-collection-types-export.js` у папці `pages-export/`
2. Використати `strapi-single-types-export.js` як основу
3. Адаптувати для collection types (Vacancies, Categories, Skills, Keyword tags)
4. Реалізувати масові вибірки через API (можливо з пагінацією)
5. Додати обробку draft state (фільтрація опублікованих записів)
6. Реалізувати можливість експорту по конкретних ID
7. Додати валідацію повноти даних (перевірка кількості записів)
8. Створити структуру папок `exported/collections/{Entity}/`
9. Додати логування та статус-трекер
10. Протестувати на одній колекції (наприклад, Categories)
11. Створити документацію README-COLLECTIONS.md

### Resources and Links:
- Приклад скрипта: `Dropbox/ENTITIES/ASSETS/rem-s/scripts/pages-export/strapi-single-types-export.js`
- Strapi API документація: `https://docs.strapi.io/dev-docs/api/rest`
- Структура: `Dropbox/ENTITIES/ASSETS/rem-s/exported/collections/`

### Instructions:
- Почати з простої колекції (Categories) для тестування
- Врахувати, що collection types мають ID та можуть бути в draft state
- Реалізувати пагінацію, якщо записів багато
- Додати можливість експорту окремих записів по ID для тестування

---

## Task 5: Реалізувати обробку draft state для вакансій

**Priority:** Medium | **Estimated Time:** 2-3 hours

### Steps:
1. Вивчити структуру вакансій у Strapi (перевірити draft/published state)
2. Додати параметр `publicationState: 'live'` до API запитів для експорту
3. Реалізувати фільтрацію draft записів у скрипті експорту
4. Додати опцію `--include-drafts` для експорту draft записів (опціонально)
5. Протестувати експорт тільки опублікованих вакансій
6. Порівняти кількість експортованих записів з кількістю в Strapi
7. Додати логування кількості пропущених draft записів
8. Оновити документацію з інформацією про draft state

### Resources and Links:
- Strapi API: `https://strapi.rem-s.com/api/vacancies`
- Документація Strapi: `https://docs.strapi.io/dev-docs/api/rest#publication-state`
- Скрипт експорту: `Dropbox/ENTITIES/ASSETS/rem-s/scripts/pages-export/strapi-collection-types-export.js`

### Instructions:
- За замовчуванням експортувати тільки опубліковані записи
- Додати можливість експорту draft записів через опцію (для адміністраторів)
- Логувати кількість пропущених draft записів для прозорості

---

## Task 6: Створити скрипт для масового оновлення

**Priority:** Medium | **Estimated Time:** 2-3 hours

### Steps:
1. Створити новий файл `strapi-bulk-update.js` у папці `pages-export/`
2. Реалізувати читання з одного JSON файлу з масивом оновлень
3. Додати валідацію структури файлу (масив об'єктів з entity, locale, data)
4. Реалізувати обробку кожного оновлення з використанням існуючої логіки
5. Додати rate limiting для запобігання перевантаження API
6. Додати детальне логування кожного кроку
7. Реалізувати можливість відновлення після помилок (resume functionality)
8. Додати dry-run режим та підтвердження
9. Протестувати на невеликому наборі даних
10. Створити документацію з прикладами формату файлу

### Resources and Links:
- Приклад: `Dropbox/ENTITIES/ASSETS/rem-s/scripts/pages-export/strapi-single-types-update.js`
- Структура: `Dropbox/ENTITIES/ASSETS/rem-s/updated/bulk/`

### Instructions:
- Почати з простої структури файлу (масив об'єктів)
- Додати можливість часткового оновлення (тільки певні поля)
- Реалізувати обробку помилок з можливістю продовження
- Завжди використовувати backup перед масовим оновленням

---

## Reminder
- Break down each plan into steps
- Add all necessary links and resources
- Write clear execution instructions
- Start with high-priority tasks in the morning
- Use AI tools (NotebookLM, Gemini AI) to assist with tasks
- Document progress in daily.md throughout the day
- Test thoroughly before considering tasks complete
- Apply learned skills immediately to reinforce learning
