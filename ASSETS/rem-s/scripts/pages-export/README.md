# Strapi Single Types Export Script

Скрипт для експорту single types з Strapi CMS у формат JSON.

## Встановлення

```bash
npm install
```

## Використання

### Експорт з токеном

```bash
node strapi-single-types-export.js <token>
```

або через environment variable:

```bash
STRAPI_TOKEN=your_token_here node strapi-single-types-export.js
```

### Тестовий режим (без токена)

```bash
node strapi-single-types-export.js --test
```

## Експортовані Single Types

- About (about-us)
- Contact (contact)
- Header (header)
- Home (home-page)
- NotFound (not-found)
- ThankYou (thank-you)
- VacancyPage (vacancy-page)
- VacancyListData (vacancy-list-data)
- VideoInterview (videointerview)

## Локалі

Експортуються дані для локалей: `en`, `uk`, `pl`, `ru` (без slovak).

## Структура експорту

```
exported/pages/
  About/
    en.json
    uk.json
    pl.json
    ru.json
  Contact/
    en.json
    uk.json
    pl.json
    ru.json
  ...
```

## Формат JSON

Кожен файл містить плаский об'єкт без структури `data.attributes` - тільки текстові поля з `attributes`.

## Трекер статусів

Скрипт створює та оновлює файл `status-tracker.json` зі статусами експорту:

```json
{
  "About": {
    "en": "exported",
    "uk": "exported",
    "pl": "pending",
    "ru": "exported"
  },
  ...
}
```

### Статуси:
- `pending` - дані ще не збережені або застарілі
- `exported` - актуальна версія у файлі
- `error` - помилка під час експорту

## API Endpoint

```
https://strapi.rem-s.com/api/{endpoint}?populate=*&locale={locale}
```

Headers:
```
Authorization: Bearer {token}
Content-Type: application/json
```

