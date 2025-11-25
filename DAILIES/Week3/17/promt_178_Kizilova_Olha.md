# История запросов - Микросервис управления аккаунтами

## Запрос 1 (Начальный запрос)

Мне необходимо разработать новый микросервис в котором будут аккаунты. Мне необходимо чтобы там хранились основные аккаунты Gmail', Так же мне необходимо будет хранить такие как LinkedIn аккаунт Job Аккаунт Аккаунт для заводимый в AI сервисах там Github сервисы Bitbucket Github Figma там Реплейксики. которые будут верифицироваться с помощью этих Google аккаунтов или логин и пароль. также само будет там линкедина аккаунты джопа канты с вакансиями на которых расположены мне необходимо что ты предложил структуру хранения аккаунтов и удобной фильтрацией. Сгенерируй собственную структуру для системы управления аккаунтами C:\Users\olgas\Dropbox\Niko Nov25\ExportCRMS\Job_Accounts\Job_Account_prod.json C:\Users\olgas\Dropbox\Niko Nov25\ExportCRMS\Account_prod.md C:\Users\olgas\Dropbox\Niko Nov25\ExportCRMS\LeadAccount_JSON_Cluster

## Запрос 2

а мождет стоит объединить Account и VerificationAccount чтоб можно было верефицировать любыми аакантуами, так как может быть верификация с помощью телефона а номер телефона будет как аккаунт

## Запрос 3

ты неправильно понял, номер телефона будет как отдельный аакаунт а другие аккаунты могут быть верефицированы с помощью этого аккаунта (телефона)

## Запрос 4

давай Account и JobAccount все ж таки разделим на разные сущности

## Запрос 5

давай service_type заменим на tool_id (которые будут браться из другого микросервиса

phone_number, verification_method, oauth_token, refresh_token, client_id  удалим  

status замени на status_id  будет браться из другого микросервиса

Модель JobPost нам не нужна

и предоставить структуру данных для проекта на Node.js, DB - Postgres

## Запрос 6

давай в JobAccount удалим linked_accounts

и будем Все поля, которые ты написал через JSONB, использовать на связи через отдельную таблицу.

## Запрос 7

запиши всю историю моих запросов в файл C:\Users\olgas\Dropbox\Nov25\Dev\Kizilova Olha\Accounts\promt.md

---

## ФИНАЛЬНЫЙ ПРОМПТ

Разработай структуру микросервиса управления аккаунтами на Node.js с базой данных PostgreSQL.

### Требования к структуре данных:

1. **Две отдельные сущности:**
   - **Account** - аккаунты сервисов (Gmail, LinkedIn, телефон, GitHub, Bitbucket, Figma, Replit, AI сервисы)
   - **JobAccount** - аккаунты на сайтах вакансий (Work.ua и т.д.)

2. **Поля для Account:**
   - id, name, tool_id (ссылка на другой микросервис), login, profile_link, password (зашифрован, опционально), can_verify_others (boolean), status_id (ссылка на другой микросервис), owner_id (VARCHAR(64), ссылка на другой микросервис, MongoDB, может быть NULL), metadata (JSONB), notes, created_at, updated_at, last_used_at, usage_count, connections (INTEGER), country_id (INTEGER, ссылка на другой микросервис), is_approved_manager (BOOLEAN), created_date (DATE)
   - **НЕ включать:** phone_number, verification_method, oauth_token, refresh_token, client_id, service_type, status, premium (история в account_premium_histories)
   - **Ассоциации:** `hasMany(JobAccount)` через `job_site_id` (алиас `jobSiteAccounts`) - account может быть job_site для job_accounts

3. **Поля для JobAccount:**
   - id, name, job_site_id (FK на `accounts.id` - сайт вакансий хранится как account в таблице accounts), login, password (зашифрован), profile_link, status_id (ссылка на другой микросервис), owner_id (VARCHAR(64), ссылка на другой микросервис, MongoDB, может быть NULL), available_job_posts, active_job_posts, metadata (JSONB), notes, created_at, updated_at, last_used_at, usage_count
   - **НЕ включать:** linked_accounts, service_type, status
   - **Ассоциации:** `belongsTo(Account)` через `job_site_id` (алиас `jobSite`)

4. **Верификация:**
   - Номер телефона - это отдельный Account аккаунт с соответствующим tool_id
   - Любые Account аккаунты (Gmail, телефон и т.д.) могут использоваться для верификации других Account или JobAccount аккаунтов
   - Все связи верификации должны быть через отдельные таблицы (НЕ через JSONB массивы)

5. **Таблица связей:**
   - `verifications` - полиморфная связь, где любой Account (включая телефон) может верифицировать другой `Account` или `JobAccount`; поля `verifiable_type`, `verifiable_id`, `verification_account_id`, `created_at`, уникальный индекс на `(verifiable_type, verifiable_id, verification_account_id)`

6. **Таблицы для подписок на верификацию:**
   - `plans` - планы подписки с полями: name, description, price, currency_id (INTEGER, ссылка на другой микросервис), duration_days, is_active
   - `verification_subscriptions` - подписки на верификацию аккаунтов с полями: verification_id, plan_id (ссылка на plans.id), status_id (INTEGER, ссылка на другой микросервис), started_at, expires_at, cancelled_at, auto_renew
   - `verification_subscription_payments` - история платежей за подписки с полями: subscription_id, amount, currency, payment_date, payment_method, payment_status, transaction_id, invoice_number

7. **Таблицы для назначения пользователей:**
   - `user_assignments` - полиморфная связь для назначения пользователей на аккаунты или job_accounts с полями: assignable_type ('account' или 'job_account'), assignable_id, user_id (VARCHAR(64), ссылка на другой микросервис)

8. **Таблицы для документов:**
   - `account_documents` - документы аккаунтов с полями: account_id, expiration_date, type_id (ENUM: 'passport', 'license', 'other')
   - `document_links` - ссылки на документы с полями: document_id, url

9. **Полиморфные таблицы истории:**
   - `changes` - история изменений аккаунтов и job_accounts с полями: verifiable_type, verifiable_id, user_id (VARCHAR(64)), value (JSONB)
   - `password_histories` - история паролей с полями: verifiable_type, verifiable_id, old_pass, change_date
   - `manager_histories` - история менеджеров с полями: verifiable_type, verifiable_id, user_id (VARCHAR(64)), start_date, end_date
   - `country_histories` - история стран с полями: verifiable_type, verifiable_id, country_id, start_date, end_date

10. **Таблица истории премиум статуса:**
    - `account_premium_histories` - история премиум статуса аккаунтов с полями: account_id, premium, start_date, end_date

11. **Дополнительные поля для accounts:**
    - `connections` (INTEGER) - количество связей (например, LinkedIn connections)
    - `country_id` (INTEGER) - ссылка на другой микросервис (countries)
    - `is_approved_manager` (BOOLEAN) - одобрен менеджером
    - `created_date` (DATE) - дата создания (может отличаться от created_at)
    - `profile_link` (TEXT) - ссылка на профиль
    - Поле `premium` удалено из accounts, так как история хранится в account_premium_histories

12. **Модель JobPost не нужна** - удалить из структуры

### Технические требования:

- Node.js (JavaScript, без TypeScript)
- PostgreSQL база данных
- SQL миграции для создания таблиц
- Описание моделей в формате JSDoc/JSON схем
- Индексы для оптимизации запросов
- Примеры SQL запросов с JOIN для получения связанных данных
- Frontend: React 18 + Vite, React Query, React Hook Form, React Router v6, кастомный CSS

### Структура проекта:

Предоставь полную структуру проекта Node.js с:
- SQL схемами для всех таблиц
- JSDoc/JS описаниями моделей
- Структурой папок проекта
- package.json с зависимостями

### Миграции базы данных:

Все миграции созданы с использованием Sequelize CLI и могут быть выполнены одной командой:

```bash
# Запуск всех миграций для создания структуры БД
npx sequelize-cli db:migrate
```

**Структура миграций (14 файлов):**
- `001-create-accounts.js` - таблица accounts с полями: connections, country_id, is_approved_manager, created_date, profile_link (owner_id может быть NULL)
- `002-create-job-accounts.js` - таблица job_accounts (job_site_id ссылается на accounts.id, owner_id может быть NULL)
- `003-create-verifications.js` - полиморфная таблица verifications
- `004-create-plans.js` - таблица plans (currency_id как INTEGER)
- `005-create-verification-subscriptions.js` - таблица verification_subscriptions (status_id как INTEGER, ссылка на plans.id)
- `006-create-verification-subscription-payments.js` - таблица verification_subscription_payments
- `007-create-user-assignments.js` - полиморфная таблица user_assignments (user_id как VARCHAR(64))
- `008-create-account-documents.js` - таблица account_documents (type_id как ENUM)
- `009-create-document-links.js` - таблица document_links
- `010-create-changes.js` - полиморфная таблица changes (value как JSONB, user_id как VARCHAR(64))
- `011-create-password-histories.js` - полиморфная таблица password_histories
- `012-create-account-premium-histories.js` - таблица account_premium_histories
- `013-create-manager-histories.js` - полиморфная таблица manager_histories (user_id как VARCHAR(64))
- `014-create-country-histories.js` - полиморфная таблица country_histories

Все миграции поддерживают откат (down методы) и используют Sequelize QueryInterface.

### Миграция данных из существующих файлов:

Учесть необходимость миграции из существующих файлов:
- C:\Users\olgas\Dropbox\Niko Nov25\ExportCRMS\Job_Accounts\Job_Account_prod.json
- C:\Users\olgas\Dropbox\Niko Nov25\ExportCRMS\Account_prod.md
- C:\Users\olgas\Dropbox\Niko Nov25\ExportCRMS\LeadAccount_JSON_Clusters

### API Endpoints:

Предоставить структуру API endpoints для:
- CRUD операции для Account
- CRUD операции для JobAccount
- Управление верификациями (связывание/отвязывание аккаунтов)
- Управление подписками на верификацию (создание, обновление, отмена подписок)
- Управление платежами за подписки (история платежей, статусы платежей)
- Фильтрация по tool_id, status_id, owner_id, can_verify_others
- Получение связанных аккаунтов через верификацию
- Получение активных/истекших подписок на верификацию

---
