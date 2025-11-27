---
category: ROOT
subcategory: root
type: analysis
source_id: id_and_status_rules
title: id and status rules
date: 2025-11-26
status: draft
owner: unknown
related: []
links: []
---

# id and status rules

## Summary
- TODO

## Context
- TODO

## Data / Content
# ID, департаменты и статусы (Phase 0)

## 1. ID patterns (regex + описание)
- Research: `^RSH-[A-Z]{2,6}-\d{3}$` (пример: `RSH-VID-001`)
- Research (старый RSR): `^RSR-\d{3}$` (пример: `RSR-002`) — подлежит миграции в RSH-формат
- Video: `^Video_\d{3}$` (пример: `Video_024`)
- Search queue: `^RSH-SRH-\d{3}$`
- Report: `^RPT-[A-Z]{2,6}-\d{3}$`
- Influencer: `^INF-[A-Z]{2,6}-\d{3}$`
- Channel: `^YT-CH-\d{3}$`
- Tool (из tool_mapping): `^TOOL-[A-Z]{2,6}-\d{3}$` (если указан)

## 2. Department / source (канонический справочник)
- `VID` — Video
- `AI` — Artificial Intelligence
- `LGN` — Learning & Growth
- `DEV` — Development
- `HR` — Human Resources
- `DESIGN` — Design
- `SALES` — Sales
- `SMM` — Social Media
- `ALL` — Meta/общие

Маппинг для «сырых» значений:
- lower-case → upper-case (`vid` → `VID`)
- синонимы: `Video` → `VID`; `AI/ML` → `AI`; `Learning` → `LGN`; `Development`/`Dev` → `DEV`; `HR Dept` → `HR`; `Design Dept` → `DESIGN`; `Sales Dept` → `SALES`; `Social`/`SMM Dept` → `SMM`; пустое → `ALL`.

## 3. Status enums (нормализованные)
- Research: `{planning, active, review, completed, archived}`
  - маппинг: `draft`→`planning`; `in_progress`→`active`; `done`→`completed`
- Video queue: `{queued, transcribing, analyzing, completed, failed}`
  - маппинг: `pending`→`queued`; `selected`→`analyzing`; `parsed`→`completed`
- Search queue: `{pending, active, completed, cancelled}`
- Tool discovery (discovered_tools): `{pending, processed, archived}`
- Reports/Markdown (если указано в тексте): `{active, archived, draft}`

## 4. Валидация (правила)
- ID: должно соответствовать regex из раздела 1; уникальность в пределах таблицы/датасета.
- Department: должно входить в справочник; иначе `UNKNOWN_DEPT` + логировать.
- Status: должно входить в enum сущности; иначе `unknown` + логировать.
- Dates: ISO 8601 (`YYYY-MM-DD` или `YYYY-MM-DDTHH:MM:SSZ`); непарсибельные даты → `null` + логировать.
- Encoding: UTF-8 для CSV/JSON/MD.

## 5. Разрешение конфликтов и логирование
- Дубликаты ID: складывать в конфликтный список и помечать записи как `duplicate`; не грузить в целевую БД до решения.
- Неизвестный department/status: нормализовать если возможно; иначе — поле `normalized_*` пустое, лог в отчёт.
- tool_mapping: ключи нормализовать в lower-case/trim; при дубликате ключа хранить первый вариант, остальные — в `tool_mapping_conflicts.json`.

## 6. Применение в скриптах
- `normalize_csv_phase0.py`: применять маппинг статусов (video/search) и нормализацию регистров; добавлять пустые поля для последующего обогащения.
- `normalize_json_phase0.py`: нормализация ключей tool_mapping, структурирование discovered_tools с `status="pending"`.
- `md_inventory.py`: для Markdown — извлекать `entity_id` и `status` по enum выше; неизвестные значения логировать в отчёт инвентаризации.


## Findings
- TODO

## Actions / Next Steps
- TODO

## Metrics / Status
- TODO

## Attachments / Links
- TODO

## Change Log
- 2025-11-26 standardization scaffold added
