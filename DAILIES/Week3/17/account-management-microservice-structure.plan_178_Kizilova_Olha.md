<!-- 4b36a91c-5619-4c94-bf4b-910119ef7862 59d338e0-163b-43be-bec5-94b0d0d3bfaa -->
# Структура микросервиса управления аккаунтами (Node.js + PostgreSQL)

## 1. Структура базы данных PostgreSQL 

### 1.1 Таблица accounts

Аккаунты сервисов (Gmail, LinkedIn, телефон, GitHub и т.д.):
Connect API of Tools - in LIBRARIES

```sql
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    tool_id INTEGER NOT NULL, -- ссылка на другой микросервис (tools)
    login VARCHAR(255) NOT NULL,
    profile_link TEXT,
    password TEXT, -- зашифрован, опционально
    can_verify_others BOOLEAN DEFAULT false,
    status_id INTEGER NOT NULL, -- ссылка на другой микросервис (statuses)
    owner_id VARCHAR(64),// Who is Verifying Access / ссылка на другой микросервис (users, MongoDB), может быть NULL
    metadata JSONB DEFAULT '{}',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_used_at TIMESTAMP,
    usage_count INTEGER DEFAULT 0,
    connections INTEGER, -- количество связей (например, LinkedIn connections)
    country_id INTEGER, -- ссылка на другой микросервис (countries)
    is_approved_manager BOOLEAN DEFAULT false,
    created_date DATE -- дата создания (может отличаться от created_at)
);

CREATE INDEX idx_accounts_tool_id ON accounts(tool_id);
CREATE INDEX idx_accounts_status_id ON accounts(status_id);
CREATE INDEX idx_accounts_owner_id ON accounts(owner_id);
CREATE INDEX idx_accounts_can_verify_others ON accounts(can_verify_others);
CREATE INDEX idx_accounts_country_id ON accounts(country_id);
```

### 1.2 Таблица job_accounts

Аккаунты на сайтах вакансий:

```sql
CREATE TABLE job_accounts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    job_site_id INTEGER NOT NULL REFERENCES accounts(id) ON DELETE CASCADE, -- ссылка на accounts (сайт вакансий хранится как account)
    login VARCHAR(255) NOT NULL,
    password TEXT NOT NULL, -- зашифрован
    profile_link TEXT,
    status_id INTEGER NOT NULL, -- ссылка на другой микросервис (statuses)
    owner_id VARCHAR(64), -- ссылка на другой микросервис (users, MongoDB), может быть NULL
    available_job_posts INTEGER DEFAULT 0,
    active_job_posts INTEGER DEFAULT 0,
    metadata JSONB DEFAULT '{}',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_used_at TIMESTAMP,
    usage_count INTEGER DEFAULT 0
);

CREATE INDEX idx_job_accounts_job_site_id ON job_accounts(job_site_id);
CREATE INDEX idx_job_accounts_status_id ON job_accounts(status_id);
CREATE INDEX idx_job_accounts_owner_id ON job_accounts(owner_id);
```

### 1.3 Таблица verifications

Полиморфная связь `Account`/`JobAccount` с аккаунтами, которые их верифицируют:

```sql
CREATE TABLE verifications (
    id SERIAL PRIMARY KEY,
    verifiable_type VARCHAR(50) NOT NULL CHECK (verifiable_type IN ('account', 'job_account')),
    verifiable_id INTEGER NOT NULL,
    verification_account_id INTEGER NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(verifiable_type, verifiable_id, verification_account_id)
);

CREATE INDEX idx_verifications_verifiable ON verifications(verifiable_type, verifiable_id);
CREATE INDEX idx_verifications_verification_account_id ON verifications(verification_account_id);
```

### 1.4 Таблица plans

Планы подписки на верификацию:

```sql
CREATE TABLE plans (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    currency_id INTEGER NOT NULL, -- ссылка на другой микросервис (currencies)
    duration_days INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_plans_is_active ON plans(is_active);
```

### 1.5 Таблица verification_subscriptions

Подписки на верификацию аккаунтов с историей:

```sql
CREATE TABLE verification_subscriptions (
    id SERIAL PRIMARY KEY,
    verification_id INTEGER NOT NULL REFERENCES verifications(id) ON DELETE CASCADE,
    plan_id INTEGER REFERENCES plans(id) ON DELETE SET NULL,
    status_id INTEGER NOT NULL, -- ссылка на другой микросервис (subscription_statuses)
    started_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP, -- когда заканчивается подписка
    cancelled_at TIMESTAMP, -- когда была отменена
    auto_renew BOOLEAN DEFAULT false, -- автопродление
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_vs_verification_status ON verification_subscriptions(verification_id, status_id);
CREATE INDEX idx_vs_status_expires ON verification_subscriptions(status_id, expires_at);
CREATE INDEX idx_vs_plan_id ON verification_subscriptions(plan_id);
```

### 1.6 Таблица verification_subscription_payments

История платежей за подписки на верификацию:

```sql
CREATE TABLE verification_subscription_payments (
    id SERIAL PRIMARY KEY,
    subscription_id INTEGER NOT NULL REFERENCES verification_subscriptions(id) ON DELETE CASCADE,
    amount DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    payment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR(50), -- card, bank_transfer, etc.
    payment_status VARCHAR(50) NOT NULL DEFAULT 'pending', -- pending, completed, failed, refunded
    transaction_id VARCHAR(255), -- ID транзакции из платежной системы
    invoice_number VARCHAR(255),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_subscription_payments_subscription_id ON verification_subscription_payments(subscription_id);
CREATE INDEX idx_subscription_payments_payment_date ON verification_subscription_payments(payment_date);
CREATE INDEX idx_subscription_payments_payment_status ON verification_subscription_payments(payment_status);
```

### 1.7 Таблица user_assignments

Полиморфная связь для назначения пользователей на аккаунты или job_accounts:

```sql
CREATE TABLE user_assignments (
    id SERIAL PRIMARY KEY,
    assignable_type VARCHAR(50) NOT NULL CHECK (assignable_type IN ('account', 'job_account')),
    assignable_id INTEGER NOT NULL,
    user_id VARCHAR(64) NOT NULL, -- ссылка на другой микросервис (users, MongoDB)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(assignable_type, assignable_id, user_id)
);

CREATE INDEX idx_user_assignments_assignable ON user_assignments(assignable_type, assignable_id);
CREATE INDEX idx_user_assignments_user_id ON user_assignments(user_id);
```

### 1.8 Таблица account_documents

Документы аккаунтов (паспорта, лицензии и т.д.):

```sql
CREATE TABLE account_documents (
    id SERIAL PRIMARY KEY,
    account_id INTEGER NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
    expiration_date DATE,
    type_id VARCHAR(50) NOT NULL DEFAULT 'other' CHECK (type_id IN ('passport', 'license', 'other')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_account_documents_account_id ON account_documents(account_id);
CREATE INDEX idx_account_documents_type_id ON account_documents(type_id);
```

### 1.9 Таблица document_links

Ссылки на документы:

```sql
CREATE TABLE document_links (
    id SERIAL PRIMARY KEY,
    document_id INTEGER NOT NULL REFERENCES account_documents(id) ON DELETE CASCADE,
    url TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_document_links_document_id ON document_links(document_id);
```

### 1.10 Таблица changes

Полиморфная таблица истории изменений аккаунтов и job_accounts:

```sql
CREATE TABLE changes (
    id SERIAL PRIMARY KEY,
    verifiable_type VARCHAR(50) NOT NULL CHECK (verifiable_type IN ('account', 'job_account')),
    verifiable_id INTEGER NOT NULL,
    user_id VARCHAR(64) NOT NULL, -- ссылка на другой микросервис (users, MongoDB)
    value JSONB NOT NULL DEFAULT '{}', -- детали изменений в формате JSON
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_changes_verifiable ON changes(verifiable_type, verifiable_id);
CREATE INDEX idx_changes_user_id ON changes(user_id);
CREATE INDEX idx_changes_created_at ON changes(created_at);
```

### 1.11 Таблица password_histories

Полиморфная таблица истории паролей:

```sql
CREATE TABLE password_histories (
    id SERIAL PRIMARY KEY,
    verifiable_type VARCHAR(50) NOT NULL CHECK (verifiable_type IN ('account', 'job_account')),
    verifiable_id INTEGER NOT NULL,
    old_pass TEXT NOT NULL,
    change_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_password_histories_verifiable ON password_histories(verifiable_type, verifiable_id);
CREATE INDEX idx_password_histories_change_date ON password_histories(change_date);
```

### 1.12 Таблица account_premium_histories

История премиум статуса аккаунтов:

```sql
CREATE TABLE account_premium_histories (
    id SERIAL PRIMARY KEY,
    account_id INTEGER NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
    premium BOOLEAN NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_premium_histories_account_id ON account_premium_histories(account_id);
CREATE INDEX idx_premium_histories_dates ON account_premium_histories(start_date, end_date);
```

### 1.13 Таблица manager_histories

Полиморфная таблица истории менеджеров:

```sql
CREATE TABLE manager_histories (
    id SERIAL PRIMARY KEY,
    verifiable_type VARCHAR(50) NOT NULL CHECK (verifiable_type IN ('account', 'job_account')),
    verifiable_id INTEGER NOT NULL,
    user_id VARCHAR(64) NOT NULL, -- ссылка на другой микросервис (users, MongoDB)
    start_date DATE NOT NULL,
    end_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_manager_histories_verifiable ON manager_histories(verifiable_type, verifiable_id);
CREATE INDEX idx_manager_histories_user_id ON manager_histories(user_id);
CREATE INDEX idx_manager_histories_dates ON manager_histories(start_date, end_date);
```

### 1.14 Таблица country_histories

Полиморфная таблица истории стран:

```sql
CREATE TABLE country_histories (
    id SERIAL PRIMARY KEY,
    verifiable_type VARCHAR(50) NOT NULL CHECK (verifiable_type IN ('account', 'job_account')),
    verifiable_id INTEGER NOT NULL,
    country_id INTEGER NOT NULL, -- ссылка на другой микросервис (countries)
    start_date DATE NOT NULL,
    end_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_country_histories_verifiable ON country_histories(verifiable_type, verifiable_id);
CREATE INDEX idx_country_histories_country_id ON country_histories(country_id);
CREATE INDEX idx_country_histories_dates ON country_histories(start_date, end_date);
```

### 1.15 Итого по верификациям

- Любой `Account` (включая телефоны, Gmail и т.д.) может верифицировать другой `Account` или `JobAccount`.
- Все связи хранятся только в таблице `verifications`, фильтрация по `verifiable_type`.
- Подписки и платежи всегда ссылаются на записи `verifications` через `verification_id`.

## 2. Модели данных (JavaScript / Sequelize)

- Каждая модель — отдельный файл `*.js`, написанный по шаблону:

```javascript
'use strict';
const { Model } = require('sequelize');

module.exports = (sequelize, DataTypes) => {
  class Account extends Model {
    static associate(models) {
      // Определяем связи здесь
    }

    toApiFormat() {
      return {
        id: this.id,
        name: this.name,
        // ...остальные поля
      };
    }
  }

  Account.init(
    {
      id: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true,
      },
      name: {
        type: DataTypes.STRING(255),
        allowNull: false,
      },
      // ...определение остальных полей
    },
    {
      sequelize,
      modelName: 'Account',
      tableName: 'accounts',
      timestamps: true,
      createdAt: 'created_at',
      updatedAt: 'updated_at',
      indexes: [
        { name: 'idx_accounts_tool_status', fields: ['tool_id', 'status_id'] },
        { name: 'idx_accounts_owner', fields: ['owner_id'] },
      ],
    }
  );

  return Account;
};
```

- Для каждой модели указываем поля и обязательные/опциональные атрибуты:

### 2.1 Account
- `id`, `name`, `tool_id`, `login`, `profile_link`, `password`, `can_verify_others`, `status_id`, `owner_id` (VARCHAR(64), nullable), `metadata(JSONB)`, `notes`, `created_at`, `updated_at`, `last_used_at`, `usage_count`, `connections`, `country_id`, `is_approved_manager`, `created_date`
- Индексы: `(tool_id)`, `(status_id)`, `(owner_id)`, `(can_verify_others)`, `(country_id)`
- Ассоциации: `hasMany(JobAccount)` через `job_site_id` (алиас `jobSiteAccounts`)

### 2.2 JobAccount
- `id`, `name`, `job_site_id` (FK на `accounts.id`), `login`, `password`, `profile_link`, `status_id`, `owner_id` (VARCHAR(64), nullable), `available_job_posts`, `active_job_posts`, `metadata(JSONB)`, `notes`, `created_at`, `updated_at`, `last_used_at`, `usage_count`
- Индексы: `(job_site_id)`, `(status_id)`, `(owner_id)`
- Ассоциации: `belongsTo(Account)` через `job_site_id` (алиас `jobSite`)

### 2.3 Verification
- `id`, `verifiable_type`, `verifiable_id`, `verification_account_id`, `created_at`
- Индексы: `(verifiable_type, verifiable_id)`, `(verification_account_id)`, уникальный `(verifiable_type, verifiable_id, verification_account_id)`

### 2.4 Plan
- `id`, `name`, `description`, `price`, `currency_id` (INTEGER), `duration_days`, `is_active`, `created_at`, `updated_at`
- Индексы: `(is_active)`

### 2.5 VerificationSubscription
- `id`, `verification_id`, `plan_id`, `status_id` (INTEGER), `started_at`, `expires_at`, `cancelled_at`, `auto_renew`, `created_at`, `updated_at`
- Индексы: `(verification_id, status_id)`, `(status_id, expires_at)`, `(plan_id)`

### 2.6 VerificationSubscriptionPayment
- `id`, `subscription_id`, `amount`, `currency`, `payment_date`, `payment_method`, `payment_status`, `transaction_id`, `invoice_number`, `notes`, `created_at`
- Индексы: `(subscription_id, payment_date)`, `(payment_status)`

### 2.7 UserAssignment
- `id`, `assignable_type`, `assignable_id`, `user_id` (VARCHAR(64)), `created_at`
- Индексы: `(assignable_type, assignable_id)`, `(user_id)`, уникальный `(assignable_type, assignable_id, user_id)`

### 2.8 AccountDocument
- `id`, `account_id`, `expiration_date`, `type_id` (ENUM: 'passport', 'license', 'other'), `created_at`, `updated_at`
- Индексы: `(account_id)`, `(type_id)`

### 2.9 DocumentLink
- `id`, `document_id`, `url`, `created_at`, `updated_at`
- Индексы: `(document_id)`

### 2.10 Change
- `id`, `verifiable_type`, `verifiable_id`, `user_id` (VARCHAR(64)), `value` (JSONB), `created_at`, `updated_at`
- Индексы: `(verifiable_type, verifiable_id)`, `(user_id)`, `(created_at)`

### 2.11 PasswordHistory
- `id`, `verifiable_type`, `verifiable_id`, `old_pass`, `change_date`, `created_at`, `updated_at`
- Индексы: `(verifiable_type, verifiable_id)`, `(change_date)`

### 2.12 AccountPremiumHistory
- `id`, `account_id`, `premium`, `start_date`, `end_date`, `created_at`, `updated_at`
- Индексы: `(account_id)`, `(start_date, end_date)`

### 2.13 ManagerHistory
- `id`, `verifiable_type`, `verifiable_id`, `user_id` (VARCHAR(64)), `start_date`, `end_date`, `created_at`, `updated_at`
- Индексы: `(verifiable_type, verifiable_id)`, `(user_id)`, `(start_date, end_date)`

### 2.14 CountryHistory
- `id`, `verifiable_type`, `verifiable_id`, `country_id`, `start_date`, `end_date`, `created_at`, `updated_at`
- Индексы: `(verifiable_type, verifiable_id)`, `(country_id)`, `(start_date, end_date)`

## 3. Структура проекта Node.js

```
account-service/
├── src/
│   ├── config/
│   │   ├── database.js          # PostgreSQL connection
│   │   └── env.js               # Environment variables
│   ├── models/
│   │   ├── Account.js           # Account model
│   │   ├── JobAccount.js        # JobAccount model
│   │   ├── Verification.js
│   │   ├── Plan.js
│   │   ├── VerificationSubscription.js
│   │   ├── VerificationSubscriptionPayment.js
│   │   ├── UserAssignment.js
│   │   ├── AccountDocument.js
│   │   ├── DocumentLink.js
│   │   ├── Change.js
│   │   ├── PasswordHistory.js
│   │   ├── AccountPremiumHistory.js
│   │   ├── ManagerHistory.js
│   │   └── CountryHistory.js
│   ├── repositories/
│   │   ├── AccountRepository.js
│   │   ├── JobAccountRepository.js
│   │   ├── VerificationRepository.js
│   │   ├── SubscriptionRepository.js
│   │   └── PaymentRepository.js
│   ├── services/
│   │   ├── AccountService.js
│   │   ├── JobAccountService.js
│   │   ├── VerificationService.js
│   │   ├── SubscriptionService.js
│   │   └── PaymentService.js
│   ├── controllers/
│   │   ├── AccountController.js
│   │   ├── JobAccountController.js
│   │   ├── VerificationController.js
│   │   ├── SubscriptionController.js
│   │   └── PaymentController.js
│   ├── routes/
│   │   ├── accounts.routes.js
│   │   ├── jobAccounts.routes.js
│   │   ├── verifications.routes.js
│   │   ├── subscriptions.routes.js
│   │   └── payments.routes.js
│   ├── middleware/
│   │   ├── auth.js
│   │   ├── validation.js
│   │   └── errorHandler.js
│   ├── utils/
│   │   ├── encryption.js
│   │   ├── queryBuilder.js
│   │   └── logger.js
│   ├── migrations/
│   │   ├── 001-create-accounts.js
│   │   ├── 002-create-job-accounts.js
│   │   ├── 003-create-verifications.js
│   │   ├── 004-create-plans.js
│   │   ├── 005-create-verification-subscriptions.js
│   │   ├── 006-create-verification-subscription-payments.js
│   │   ├── 007-create-user-assignments.js
│   │   ├── 008-create-account-documents.js
│   │   ├── 009-create-document-links.js
│   │   ├── 010-create-changes.js
│   │   ├── 011-create-password-histories.js
│   │   ├── 012-create-account-premium-histories.js
│   │   ├── 013-create-manager-histories.js
│   │   └── 014-create-country-histories.js
│   ├── app.js                    # Express app
│   └── server.js                 # Server entry point
├── package.json
├── .env.example
├── README.md
└── client/
    ├── package.json
    ├── vite.config.js
    └── src/
        ├── main.jsx
        ├── App.jsx
        ├── api/
        ├── components/
        ├── pages/
        └── styles/
```

## 4. Примеры запросов

### 4.1 Получить Account с верификационными аккаунтами

```sql
SELECT 
    a.*,
    json_agg(DISTINCT jsonb_build_object(
        'id', verifier.id,
        'name', verifier.name,
        'tool_id', verifier.tool_id
    )) FILTER (WHERE verifier.id IS NOT NULL) as verification_accounts,
    json_agg(DISTINCT jsonb_build_object(
        'id', verified.id,
        'name', verified.name,
        'tool_id', verified.tool_id
    )) FILTER (WHERE verified.id IS NOT NULL) as verified_by_accounts
FROM accounts a
LEFT JOIN verifications v_account
  ON v_account.verifiable_type = 'account' AND v_account.verifiable_id = a.id
LEFT JOIN accounts verifier ON v_account.verification_account_id = verifier.id
LEFT JOIN verifications v_reverse
  ON v_reverse.verifiable_type = 'account' AND v_reverse.verification_account_id = a.id
LEFT JOIN accounts verified ON v_reverse.verifiable_id = verified.id
WHERE a.id = $1
GROUP BY a.id;
```

### 4.2 Получить JobAccount с верификационными аккаунтами

```sql
SELECT 
    ja.*,
    json_agg(DISTINCT jsonb_build_object(
        'id', verifier.id,
        'name', verifier.name,
        'tool_id', verifier.tool_id
    )) FILTER (WHERE verifier.id IS NOT NULL) as verification_accounts
FROM job_accounts ja
LEFT JOIN verifications v
  ON v.verifiable_type = 'job_account' AND v.verifiable_id = ja.id
LEFT JOIN accounts verifier ON v.verification_account_id = verifier.id
WHERE ja.id = $1
GROUP BY ja.id;
```

### 4.3 Получить Account с количеством верифицируемых аккаунтов

```sql
SELECT 
    a.*,
    COUNT(DISTINCT CASE WHEN v_account.verifiable_type = 'account' THEN v_account.verifiable_id END) as verified_accounts_count,
    COUNT(DISTINCT CASE WHEN v_job.verifiable_type = 'job_account' THEN v_job.verifiable_id END) as verified_job_accounts_count
FROM accounts a
LEFT JOIN verifications v_account
  ON v_account.verification_account_id = a.id AND v_account.verifiable_type = 'account'
LEFT JOIN verifications v_job
  ON v_job.verification_account_id = a.id AND v_job.verifiable_type = 'job_account'
WHERE a.can_verify_others = true
GROUP BY a.id;
```

### 4.4 Получить Verification с активной подпиской и платежами

```sql
SELECT 
    v.*,
    json_agg(DISTINCT jsonb_build_object(
        'id', vs.id,
        'plan_id', vs.plan_id,
        'plan_name', p.name,
        'status_id', vs.status_id,
        'started_at', vs.started_at,
        'expires_at', vs.expires_at,
        'auto_renew', vs.auto_renew,
        'payments', (
            SELECT json_agg(jsonb_build_object(
                'id', vsp.id,
                'amount', vsp.amount,
                'currency', vsp.currency,
                'payment_date', vsp.payment_date,
                'payment_status', vsp.payment_status
            ))
            FROM verification_subscription_payments vsp
            WHERE vsp.subscription_id = vs.id
        )
    )) FILTER (WHERE vs.id IS NOT NULL) as subscriptions
FROM verifications v
LEFT JOIN verification_subscriptions vs ON v.id = vs.verification_id
LEFT JOIN plans p ON vs.plan_id = p.id
WHERE v.id = $1
GROUP BY v.id;
```

### 4.5 Получить все активные подписки, которые скоро истекают

```sql
SELECT 
    vs.*,
    v.verifiable_type,
    v.verifiable_id,
    v.verification_account_id,
    a.name as verifiable_account_name,
    ja.name as verifiable_job_account_name,
    verifier.name as verification_account_name
FROM verification_subscriptions vs
JOIN verifications v ON vs.verification_id = v.id
LEFT JOIN accounts a ON v.verifiable_type = 'account' AND v.verifiable_id = a.id
LEFT JOIN job_accounts ja ON v.verifiable_type = 'job_account' AND v.verifiable_id = ja.id
LEFT JOIN accounts verifier ON v.verification_account_id = verifier.id
WHERE vs.status_id = 1 -- активный статус (ID из другого микросервиса)
  AND vs.expires_at IS NOT NULL
  AND vs.expires_at BETWEEN CURRENT_TIMESTAMP AND CURRENT_TIMESTAMP + INTERVAL '7 days'
ORDER BY vs.expires_at ASC;
```

### 4.6 Получить историю платежей за подписку

```sql
SELECT 
    vsp.*,
    p.name as plan_name,
    vs.status_id as subscription_status_id
FROM verification_subscription_payments vsp
JOIN verification_subscriptions vs ON vsp.subscription_id = vs.id
LEFT JOIN plans p ON vs.plan_id = p.id
WHERE vsp.subscription_id = $1
ORDER BY vsp.payment_date DESC;
```

### 4.7 Получить статистику по подпискам для Verification

```sql
SELECT 
    v.id,
    COUNT(DISTINCT vs.id) as total_subscriptions,
    COUNT(DISTINCT CASE WHEN vs.status_id = 1 THEN vs.id END) as active_subscriptions, -- 1 = active status_id
    COUNT(DISTINCT CASE WHEN vs.status_id = 2 THEN vs.id END) as expired_subscriptions, -- 2 = expired status_id
    SUM(CASE WHEN vsp.payment_status = 'completed' THEN vsp.amount ELSE 0 END) as total_paid_amount,
    MAX(vsp.payment_date) as last_payment_date
FROM verifications v
LEFT JOIN verification_subscriptions vs ON v.id = vs.verification_id
LEFT JOIN verification_subscription_payments vsp ON vs.id = vsp.subscription_id
WHERE v.id = $1
GROUP BY v.id;
```

## 5. API Endpoints

### 5.1 Accounts

- `GET /api/accounts` - список аккаунтов с фильтрацией
- `GET /api/accounts/:id` - детали аккаунта с верификационными связями
- `POST /api/accounts` - создание аккаунта
- `PUT /api/accounts/:id` - обновление аккаунта
- `DELETE /api/accounts/:id` - удаление аккаунта
- `GET /api/accounts/:id/verified-accounts` - список Account аккаунтов, верифицируемых через этот аккаунт
- `GET /api/accounts/:id/verified-job-accounts` - список JobAccount аккаунтов, верифицируемых через этот аккаунт

### 5.2 Job Accounts

- `GET /api/job-accounts` - список аккаунтов вакансий с фильтрацией
- `GET /api/job-accounts/:id` - детали аккаунта с верификационными связями
- `POST /api/job-accounts` - создание JobAccount аккаунта
- `PUT /api/job-accounts/:id` - обновление JobAccount аккаунта
- `DELETE /api/job-accounts/:id` - удаление JobAccount аккаунта

### 5.3 Verifications

- `GET /api/accounts?can_verify_others=true` - список Account аккаунтов, которые могут использоваться для верификации
- `GET /api/accounts?can_verify_others=true&tool_id=2` - аккаунты определенного типа для верификации
- `POST /api/accounts/:id/verifications` - добавить Account аккаунт для верификации
- `POST /api/job-accounts/:id/verifications` - добавить Account аккаунт для верификации JobAccount
- `DELETE /api/accounts/:id/verifications/:verification_account_id` - отвязать Account аккаунт верификации
- `DELETE /api/job-accounts/:id/verifications/:verification_account_id` - отвязать Account аккаунт верификации от JobAccount

### 5.4 Subscriptions

- `GET /api/verifications/:id/subscriptions` - список подписок для верификации
- `GET /api/verifications/:id/subscriptions/active` - активные подписки
- `POST /api/verifications/:id/subscriptions` - создать подписку на верификацию
- `GET /api/accounts/:id/users` - список пользователей, назначенных на аккаунт
- `POST /api/accounts/:id/users` - назначить пользователя на аккаунт
- `DELETE /api/accounts/:id/users/:user_id` - удалить назначение пользователя
- `GET /api/accounts/:id/documents` - список документов аккаунта
- `GET /api/accounts/:id/changes` - история изменений аккаунта
- `GET /api/accounts/:id/password-histories` - история паролей аккаунта
- `GET /api/accounts/:id/premium-histories` - история премиум статуса
- `GET /api/accounts/:id/manager-histories` - история менеджеров
- `GET /api/accounts/:id/country-histories` - история стран
- `PUT /api/subscriptions/:id` - обновить подписку
- `DELETE /api/subscriptions/:id` - отменить подписку
- `GET /api/subscriptions/expiring-soon` - подписки, которые скоро истекают
- `GET /api/subscriptions/:id` - детали подписки с платежами
- `GET /api/subscriptions/:id/statistics` - статистика по подписке

### 5.5 Payments

- `GET /api/subscriptions/:id/payments` - история платежей за подписку
- `POST /api/subscriptions/:id/payments` - добавить платеж
- `PUT /api/payments/:id` - обновить статус платежа
- `GET /api/payments/:id` - детали платежа

### 5.6 Filters

- `GET /api/accounts?tool_id=2&status_id=1`
- `GET /api/accounts?owner_id=2&tool_id=1`
- `GET /api/accounts?verification_accounts[]=1` - Account аккаунты, верифицируемые через указанный аккаунт
- `GET /api/job-accounts?job_site_id=1&status_id=1`
- `GET /api/job-accounts?verification_accounts[]=1` - JobAccount аккаунты, верифицируемые через указанный Account

## 6. Миграции базы данных

### 6.1 Создание структуры базы данных

Все миграции созданы с использованием Sequelize CLI и могут быть выполнены одной командой:

```bash
# Запуск всех миграций
npx sequelize-cli db:migrate

# Откат последней миграции
npx sequelize-cli db:migrate:undo

# Откат всех миграций
npx sequelize-cli db:migrate:undo:all
```

**Порядок выполнения миграций:**
1. `001-create-accounts.js` - создание таблицы accounts (owner_id может быть NULL)
2. `002-create-job-accounts.js` - создание таблицы job_accounts (job_site_id ссылается на accounts.id, owner_id может быть NULL)
3. `003-create-verifications.js` - создание полиморфной таблицы verifications
4. `004-create-plans.js` - создание таблицы plans
5. `005-create-verification-subscriptions.js` - создание таблицы verification_subscriptions
6. `006-create-verification-subscription-payments.js` - создание таблицы verification_subscription_payments
7. `007-create-user-assignments.js` - создание полиморфной таблицы user_assignments
8. `008-create-account-documents.js` - создание таблицы account_documents
9. `009-create-document-links.js` - создание таблицы document_links
10. `010-create-changes.js` - создание полиморфной таблицы changes
11. `011-create-password-histories.js` - создание полиморфной таблицы password_histories
12. `012-create-account-premium-histories.js` - создание таблицы account_premium_histories
13. `013-create-manager-histories.js` - создание полиморфной таблицы manager_histories
14. `014-create-country-histories.js` - создание полиморфной таблицы country_histories

Все миграции используют Sequelize QueryInterface и поддерживают откат (down методы).

### 6.2 Миграция данных из существующих файлов

- Чтение `Job_Account_prod.json` → преобразование в структуру job_accounts
- Чтение `Account_prod.md` (JSON внутри) → преобразование в структуру accounts
- Чтение кластеров `LeadAccount_JSON_Clusters` → объединение и преобразование в accounts
- Создание телефонных аккаунтов из номеров телефонов в metadata как отдельные accounts с соответствующим tool_id
- Создание связей в таблице verifications (verifiable_type = 'account'/'job_account')
- Определение accounts, которые могут верифицировать другие (can_verify_others = true для Gmail и phone)

## 7. Зависимости (package.json)

```json
{
  "dependencies": {
    "express": "^4.18.2",
    "pg": "^8.11.0",
    "dotenv": "^16.3.1",
    "bcrypt": "^5.1.1",
    "jsonwebtoken": "^9.0.2",
    "zod": "^3.22.4",
    "winston": "^3.10.0"
  },
  "devDependencies": {
    "nodemon": "^3.0.1",
    "eslint": "^8.57.0",
    "prettier": "^3.2.5"
  }
}
```

## 8. Frontend (React + Vite)

- **Framework**: React 18 (functional components, hooks-first подход)
- **Build Tool**: Vite для быстрой разработки и HMR
- **Styling**: кастомные CSS-модули / CSS-in-JS по необходимости, единая дизайн-система
- **State Management / Data**: React Query для загрузки/кэширования данных из микросервиса аккаунтов
- **Forms**: React Hook Form + Zod для валидации схем
- **Routing**: React Router v6 (Nested routes, Protected routes)
- **API Layer**: Typed API client (fetch/axios) с оберткой под React Query
- **Env management**: Vite env (VITE_API_URL и т.д.)
- **Testing**: Vitest + React Testing Library

### To-dos

- [ ] Создать детальную JSON структуру для всех типов аккаунтов (Account, VerificationAccount, JobAccount, JobPost) с примерами
- [ ] Разработать скрипт миграции данных из существующих файлов (Job_Account_prod.json, Account_prod.md, LeadAccount clusters) в новую структуру
- [ ] Спроектировать систему фильтрации с индексами и query builder для удобного поиска аккаунтов по различным критериям
- [ ] Создать спецификацию API endpoints для работы с аккаунтами, включая фильтрацию, верификацию и управление вакансиями
- [ ] Реализовать схему шифрования паролей и OAuth токенов, систему ролей и прав доступа