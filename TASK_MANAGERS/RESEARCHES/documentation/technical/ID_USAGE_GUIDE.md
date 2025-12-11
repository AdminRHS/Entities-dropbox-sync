# ID Usage Guide - Практическое руководство

**Document ID:** DOC-RES-019
**Version:** 1.0
**Date:** 2025-12-10
**Status:** ✅ Complete
**Purpose:** Практическое руководство по работе с ID в единой экосистеме

---

## Содержание

1. [Быстрый старт](#1-быстрый-старт)
2. [Выбор правильного ID](#2-выбор-правильного-id)
3. [Создание нового ID](#3-создание-нового-id)
4. [Использование существующих ID](#4-использование-существующих-id)
5. [Связывание ID](#5-связывание-id)
6. [Частые ошибки](#6-частые-ошибки)
7. [Примеры использования](#7-примеры-использования)
8. [Чек-листы](#8-чек-листы)

---

## 1. Быстрый старт

### Шаг 1: Определите тип сущности

**Вопрос:** Что вы создаете?

- 📹 **Видео** → используйте `Video_XXX`
- 📋 **Задачу** → используйте `TASK-XXX`
- 🐛 **Проблему** → используйте `ISS-RES-XXX`
- 📄 **Документ** → используйте `DOC-RES-XXX`
- 🔄 **Изменение** → используйте `CHG-RES-YYYYMMDD-XXX`
- 🛠️ **Инструмент** → используйте `TOL-{CAT}-XXX`
- 📊 **Workflow** → используйте `WRF-{CAT}-XXX`

### Шаг 2: Проверьте следующий доступный ID

Откройте: [ID_MASTER_REGISTRY.md](./ID_MASTER_REGISTRY.md)

Найдите секцию для вашего типа ID и посмотрите значение "Next Available".

### Шаг 3: Создайте ID

Используйте формат из реестра и создайте свою сущность с новым ID.

### Шаг 4: Обновите реестр

После создания обновите `ID_MASTER_REGISTRY.md`, указав новый "Next Available" ID.

---

## 2. Выбор правильного ID

### Дерево решений

```
Создаете новую сущность?
│
├─ YES → Где она будет использоваться?
│   │
│   ├─ Только в RESEARCHES
│   │   │
│   │   ├─ Видео → Video_XXX
│   │   ├─ Очередь видео → VQ-XXX
│   │   ├─ Поиск → SEARCH-XXX
│   │   ├─ Документация → DOC-RES-XXX
│   │   ├─ Проблема → ISS-RES-XXX
│   │   ├─ Изменение → CHG-RES-YYYYMMDD-XXX
│   │   └─ Research Entity → RSR-XXX
│   │
│   ├─ Везде (глобально)
│   │   │
│   │   ├─ Задача → TASK-XXX
│   │   ├─ Навык → SKL-XXX
│   │   └─ Профессия → PRF-XXX
│   │
│   └─ В ENTITIES библиотеках
│       │
│       ├─ Workflow → WRF-{CAT}-XXX
│       ├─ Инструмент → TOL-{CAT}-XXX
│       ├─ Объект → OBJ-{CAT}-XXX
│       └─ Действие → ACT-XXX
│
└─ NO → Используете существующий ID
    └─ Проверьте в ID_MASTER_REGISTRY.md
```

### Таблица выбора по области применения

| Область применения | Правильный ID | Неправильный ID |
|-------------------|---------------|-----------------|
| Новая задача в любом модуле | ✅ `TASK-043` | ❌ `TASK-RES-043` |
| Проблема в RESEARCHES | ✅ `ISS-RES-013` | ❌ `ISS-013` |
| Изменение от 10.12.2025 | ✅ `CHG-RES-20251210-001` | ❌ `CHG-001` |
| AI инструмент | ✅ `TOL-AI-225` | ❌ `TOL-225` |
| Security workflow | ✅ `WRF-SEC-015` | ❌ `WRF-015` |
| Новое видео | ✅ `Video_029` | ❌ `Video-029` |

---

## 3. Создание нового ID

### Процесс создания (пошагово)

#### Шаг 1: Проверка реестра

```bash
# Откройте файл
G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES\documentation\technical\ID_MASTER_REGISTRY.md

# Найдите секцию для вашего типа ID
# Например, для Issues ищите "Issue IDs (ISS-RES-XXX)"
```

**Пример из реестра:**
```
Current Status:
- Total Issues: 12
- Next Available: ISS-RES-013
```

#### Шаг 2: Формирование ID

**Правила:**
- Используйте точный формат из реестра
- Сохраняйте регистр (UPPERCASE для префиксов)
- Используйте правильные разделители (hyphen `-` или underscore `_`)
- Применяйте zero-padding (001, не 1)

**Примеры:**

✅ **Правильно:**
```
ISS-RES-013  (Issue)
TASK-043     (Task)
TOL-AI-225   (AI Tool)
Video_029    (Video - legacy format)
CHG-RES-20251210-001 (Change)
```

❌ **Неправильно:**
```
iss-res-13   (lowercase, no padding)
TASK_043     (wrong separator)
TOL-225      (missing category)
Video-029    (wrong separator for legacy)
CHG-20251210-001 (missing module)
```

#### Шаг 3: Создание файла/записи

**Для файлов markdown:**
```markdown
# [Entity Name]

**ID:** ISS-RES-013
**Type:** Issue
**Status:** OPEN
**Created:** 2025-12-10
**Priority:** MEDIUM

...
```

**Для JSON файлов:**
```json
{
  "id": "TOL-AI-225",
  "name": "New AI Tool",
  "type": "tool",
  "category": "AI",
  "created_date": "2025-12-10",
  "created_by": "username"
}
```

**Для CSV файлов:**
```csv
Video_ID,Title,Status,Created_Date
Video_029,"New Video Title",Processing,2025-12-10
```

#### Шаг 4: Обновление реестра

После создания ID обновите [ID_MASTER_REGISTRY.md](./ID_MASTER_REGISTRY.md):

**Было:**
```markdown
**Current Status:**
- **Total Issues:** 12
- **Next Available:** ISS-RES-013
```

**Стало:**
```markdown
**Current Status:**
- **Total Issues:** 13
- **Next Available:** ISS-RES-014
```

#### Шаг 5: Документирование (если значительное)

Для важных изменений создайте запись в changelog:

```markdown
### CHG-RES-20251210-002

**Type:** FEATURE
**Date:** 2025-12-10
**Description:** Created new issue ISS-RES-013 for database optimization
**Files Affected:**
- documentation/issues/06_Issues_Registry.md (updated)
- documentation/technical/ID_MASTER_REGISTRY.md (updated)
**Related IDs:**
- ISS-RES-013 (created)
```

---

## 4. Использование существующих ID

### Ссылки в Markdown

**Синтаксис:**
```markdown
See [ISS-RES-011](../issues/06_Issues_Registry.md#iss-res-011)
Related to [Video_024](../../02_TRANSCRIPTIONS/Video_024.md)
Resolves [TASK-001](../phases/07_Development_Roadmap.md#task-001)
```

**Лучшие практики:**
1. Используйте полный ID (с префиксом)
2. Добавляйте markdown ссылки где возможно
3. Используйте относительные пути
4. Добавляйте якоря (#section) для точной навигации

### Ссылки в JSON

**Формат:**
```json
{
  "id": "WRF-SEC-014",
  "name": "Secure OAuth Implementation",
  "related_entities": {
    "source_video": "Video_024",
    "uses_tools": ["TOL-AI-223", "TOL-DEV-042"],
    "requires_skills": ["SKL-065", "SKL-042"],
    "created_objects": ["OBJ-SEC-008"]
  },
  "metadata": {
    "created_from_issue": "ISS-RES-008",
    "implemented_in_task": "TASK-008"
  }
}
```

### Ссылки в CSV

**Формат:**
```csv
Video_ID,Related_Issues,Related_Tasks,Entities_Created
Video_024,"ISS-RES-008|ISS-RES-009","TASK-008","TOL-AI-223|WRF-SEC-014"
```

**Примечание:** Используйте pipe `|` как разделитель для множественных значений в CSV.

---

## 5. Связывание ID

### Принцип двусторонних связей

**Всегда создавайте связи в обе стороны!**

#### Пример: Video → Tool

**Файл 1:** `02_TRANSCRIPTIONS/Video_024.md`
```markdown
## Created Entities

This video analysis resulted in creation of:
- [TOL-AI-223](../../ENTITIES/LIBRARIES/LBS_003_Tools/TOL-AI-223.json) - Browse AI
- [WRF-SEC-014](../../ENTITIES/TASK_MANAGERS/TSM-006_Workflows/WRF-SEC-014.json) - Secure OAuth
```

**Файл 2:** `ENTITIES/LIBRARIES/LBS_003_Tools/TOL-AI-223.json`
```json
{
  "id": "TOL-AI-223",
  "name": "Browse AI",
  "source_video": "Video_024",
  "discovered_date": "2025-11-15",
  "documentation_link": "../../TASK_MANAGERS/RESEARCHES/02_TRANSCRIPTIONS/Video_024.md"
}
```

### Типы связей

#### 1. Создание (Creation)
```
Video_024 → creates → TOL-AI-223
TOL-AI-223 → created_by → Video_024
```

#### 2. Использование (Usage)
```
WRF-025 → uses → TOL-AI-223
TOL-AI-223 → used_in → WRF-025
```

#### 3. Решение проблемы (Resolution)
```
TASK-001 → resolves → ISS-RES-001
ISS-RES-001 → resolved_by → TASK-001
```

#### 4. Реализация (Implementation)
```
CHG-RES-20251203-001 → implements → TASK-001
TASK-001 → implemented_in → CHG-RES-20251203-001
```

#### 5. Требование (Requirement)
```
WRF-025 → requires → SKL-065
SKL-065 → required_by → WRF-025
```

### Шаблон связей

```json
{
  "id": "ENTITY-ID",
  "relationships": {
    "creates": ["ID1", "ID2"],
    "created_by": "ID3",
    "uses": ["ID4", "ID5"],
    "used_in": ["ID6"],
    "requires": ["ID7"],
    "required_by": ["ID8", "ID9"],
    "resolves": ["ID10"],
    "resolved_by": "ID11",
    "implements": "ID12",
    "implemented_in": "ID13",
    "references": ["ID14", "ID15"],
    "referenced_by": ["ID16"]
  }
}
```

---

## 6. Частые ошибки

### ❌ Ошибка 1: Неправильный формат

**Неправильно:**
```
video_024      (lowercase)
Video-024      (wrong separator)
ISS-RES-13     (no zero-padding)
TOL-223        (missing category)
task-042       (lowercase prefix)
```

**Правильно:**
```
Video_024
Video_024
ISS-RES-013
TOL-AI-223
TASK-042
```

### ❌ Ошибка 2: Использование модуля для глобальных ID

**Неправильно:**
```
TASK-RES-042   (TASK - глобальный, не нужен -RES-)
SKL-RES-066    (SKL - глобальный, не нужен -RES-)
```

**Правильно:**
```
TASK-042
SKL-066
```

### ❌ Ошибка 3: Отсутствие категории где необходимо

**Неправильно:**
```
TOL-223        (AI tool без категории)
WRF-014        (Security workflow без категории)
OBJ-015        (SMM object без категории)
```

**Правильно:**
```
TOL-AI-223
WRF-SEC-014
OBJ-SMM-015
```

### ❌ Ошибка 4: Односторонние связи

**Неправильно:**
```markdown
# Video_024.md
Created: TOL-AI-223

# TOL-AI-223.json
{} // Нет ссылки обратно на Video_024
```

**Правильно:**
```markdown
# Video_024.md
Created: TOL-AI-223

# TOL-AI-223.json
{
  "source_video": "Video_024"
}
```

### ❌ Ошибка 5: Повторное использование удаленных ID

**Неправильно:**
```
// Удалили Video_015
// Создаем новое видео и называем Video_015
❌ НЕТ! Используйте Video_029 (следующий доступный)
```

**Правильно:**
```
// Удалили Video_015
// Документируем gap в ID_MASTER_REGISTRY.md
// Используем Video_029 для нового видео
```

---

## 7. Примеры использования

### Сценарий 1: Создание нового видео

**Контекст:** Вы добавляете новое видео в очередь обработки.

**Шаг 1:** Проверяем реестр
```
Video: Video_001 - Video_028 (gap at 015)
Next Available: Video_029
```

**Шаг 2:** Добавляем в Video Queue
```csv
VQ-043,Video_029,"New Tutorial Title","Channel Name",...
```

**Шаг 3:** Создаем файл транскрипции
```markdown
# Video_029: New Tutorial Title

**Video ID:** Video_029
**Queue ID:** VQ-043
**Channel:** Channel Name
...
```

**Шаг 4:** Обновляем реестр
```
Next Available: Video_030
```

### Сценарий 2: Регистрация новой проблемы

**Контекст:** Обнаружена проблема с производительностью.

**Шаг 1:** Проверяем реестр
```
Issues: ISS-RES-001 to ISS-RES-012
Next Available: ISS-RES-013
```

**Шаг 2:** Создаем запись в Issues Registry
```markdown
### ISS-RES-013: Database query performance degradation

**Priority:** HIGH
**Status:** OPEN
**Identified:** 2025-12-10
**Category:** Performance

**Description:**
Database queries for video metadata taking 5+ seconds.

**Impact:**
- Slow dashboard loading
- Poor user experience
- Timeout errors

**Proposed Solution:**
Add indexes on frequently queried columns.

**Related Files:**
- `scripts/database_queries.py`
- `02_TRANSCRIPTIONS/Video_*.md`

**Effort Estimate:** 2-3 hours
```

**Шаг 3:** Обновляем реестр
```
Total Issues: 13
Next Available: ISS-RES-014
```

### Сценарий 3: Создание инструмента из видео

**Контекст:** В Video_024 обнаружен новый AI инструмент.

**Шаг 1:** Создаем Research Entity wrapper
```markdown
# RSR-025: Browse AI from Video_024

**Research Entity ID:** RSR-025
**Source Video:** Video_024
**Entity Type:** Tool
**Target ID:** TOL-AI-225
```

**Шаг 2:** Создаем Tool entity
```json
{
  "id": "TOL-AI-225",
  "name": "Browse AI",
  "category": "AI",
  "subcategory": "Web_Automation",
  "source_video": "Video_024",
  "research_entity": "RSR-025",
  "created_date": "2025-12-10",
  "features": [
    "no-code",
    "web-scraping",
    "automation"
  ]
}
```

**Шаг 3:** Обновляем Video_024
```markdown
## Created Entities

- [TOL-AI-225] Browse AI (AI/Web_Automation)
  - Research Entity: RSR-025
  - File: ENTITIES/LIBRARIES/LBS_003_Tools/TOL-AI-225.json
```

**Шаг 4:** Обновляем все реестры
```
Tools (AI): TOL-AI-001 to TOL-AI-225
Next Available: TOL-AI-226

Research Entities: RSR-001 to RSR-025
Next Available: RSR-026
```

### Сценарий 4: Документирование изменения

**Контекст:** Завершили автоматизацию Phase 2.

**Шаг 1:** Создаем changelog entry
```markdown
### CHG-RES-20251210-001

**Type:** FEATURE
**Date:** 2025-12-10
**Author:** Development Team
**Description:** Automated Phase 2 extraction using video_extraction_automator.py

**Files:**
- scripts/video_extraction_automator.py (NEW)
- scripts/config.py (UPDATED)
- documentation/technical/ID_MASTER_REGISTRY.md (UPDATED)

**Impact:**
- Time savings: 25-35 minutes per video
- Across 100 videos/year: 50-75 hours saved
- Consistency improved: 95%+ accuracy

**Related Issues:**
- ISS-RES-005 (Non-Automated Phase 2) - RESOLVED

**Related Tasks:**
- TASK-006 (Create video_extraction_automator.py) - COMPLETED
```

**Шаг 2:** Обновляем Issue status
```markdown
### ISS-RES-005: Non-Automated Phase 2

**Status:** ✅ RESOLVED
**Resolved Date:** 2025-12-10
**Resolved By:** CHG-RES-20251210-001
```

---

## 8. Чек-листы

### ✅ Чек-лист создания нового ID

- [ ] Проверил [ID_MASTER_REGISTRY.md](./ID_MASTER_REGISTRY.md)
- [ ] Использовал правильный формат для типа ID
- [ ] Применил zero-padding (001, not 1)
- [ ] Использовал правильный разделитель (- или _)
- [ ] Префиксы в UPPERCASE
- [ ] Добавил категорию где необходимо (TOL-AI, WRF-SEC)
- [ ] Создал файл/запись с новым ID
- [ ] Обновил ID_MASTER_REGISTRY.md
- [ ] Создал bidirectional links (если применимо)
- [ ] Задокументировал в changelog (если значительное)

### ✅ Чек-лист создания связей

- [ ] Определил тип связи (creates, uses, resolves, etc.)
- [ ] Создал ссылку в первом файле (A → B)
- [ ] Создал обратную ссылку во втором файле (B → A)
- [ ] Использовал правильное поле для типа связи
- [ ] Проверил, что оба ID существуют
- [ ] Использовал полные ID (с префиксами)
- [ ] Добавил markdown links где возможно
- [ ] Проверил правильность путей

### ✅ Чек-лист перед коммитом

- [ ] Все новые ID есть в ID_MASTER_REGISTRY.md
- [ ] Все bidirectional links созданы
- [ ] Форматы ID валидны (regex проверка)
- [ ] Нет дубликатов ID
- [ ] Changelog обновлен (если нужно)
- [ ] Документация обновлена
- [ ] Нет сломанных ссылок
- [ ] Relative paths корректны

---

## Быстрая справка

### Форматы ID (шпаргалка)

```
MODULE-SPECIFIC (RESEARCHES):
├─ Video_XXX              → Video_029
├─ VQ-XXX                 → VQ-043
├─ SEARCH-XXX             → SEARCH-016
├─ DOC-RES-XXX            → DOC-RES-019
├─ ISS-RES-XXX            → ISS-RES-013
├─ PHS-RES-XXX            → PHS-RES-001 to PHS-RES-009 (FIXED)
├─ CHG-RES-YYYYMMDD-XXX   → CHG-RES-20251210-001
├─ RSH-TAX-XXX            → RSH-TAX-002
└─ RSR-XXX                → RSR-026

GLOBAL:
├─ TASK-XXX               → TASK-043
├─ SKL-XXX                → SKL-067
└─ PRF-XXX                → PRF-016

CATEGORIZED:
├─ WRF-{CAT}-XXX          → WRF-SEC-015
├─ TOL-{CAT}-XXX          → TOL-AI-226
└─ OBJ-{CAT}-XXX          → OBJ-SMM-017
```

### Regex для валидации

```regex
Video:      ^Video_\d{3}$
VQ:         ^VQ-\d{3}$
SEARCH:     ^SEARCH-\d{3}$
DOC-RES:    ^DOC-RES-\d{3}$
ISS-RES:    ^ISS-RES-\d{3}$
PHS-RES:    ^PHS-RES-\d{3}$
TASK:       ^TASK-\d{3}$
CHG-RES:    ^CHG-RES-\d{8}-\d{3}$
RSH-TAX:    ^RSH-TAX-\d{3}$
RSR:        ^RSR-\d{3}$
WRF:        ^WRF-([A-Z]{3}-)?\d{3}$
TOL:        ^TOO?L-([A-Z]{2,3}-)?\d{3}$
OBJ:        ^OBJ-([A-Z]{3}-)?\d{3}$
SKL:        ^SKL-\d{3}$
PRF:        ^PRF-\d{3}$
```

---

## Связанные документы

- [04_ID_System_Standard.md](./04_ID_System_Standard.md) - Полная спецификация ID системы
- [ID_MASTER_REGISTRY.md](./ID_MASTER_REGISTRY.md) - Реестр всех активных ID
- [ID_ECOSYSTEM_VISUAL_MAP.md](../diagrams/ID_ECOSYSTEM_VISUAL_MAP.md) - Визуальная карта экосистемы
- [06_Issues_Registry.md](../issues/06_Issues_Registry.md) - Реестр проблем
- [14_Changelog_System.md](../changelog/14_Changelog_System.md) - Система отслеживания изменений

---

## Получение помощи

### Если возникли вопросы:

1. **Проверьте документацию:**
   - [04_ID_System_Standard.md](./04_ID_System_Standard.md) - полная спецификация
   - [ID_MASTER_REGISTRY.md](./ID_MASTER_REGISTRY.md) - текущие ID

2. **Используйте примеры:**
   - Найдите похожую сущность
   - Посмотрите, как у нее оформлен ID
   - Следуйте тому же паттерну

3. **Проверьте с помощью regex:**
   - Используйте паттерны из Quick Reference
   - Validate формат перед созданием

4. **Спросите команду:**
   - Technical Architect - для вопросов по структуре
   - QA Team - для вопросов по Issues
   - Documentation Team - для вопросов по DOC-RES

---

**Document Owner:** Technical Writing Team
**Review Cycle:** Monthly
**Next Review:** 2026-01-10
**Version History:**
- v1.0 (2025-12-10): Initial practical guide

**Generated by:** Claude Code (Anthropic)
**Changelog Entry:** CHG-RES-20251210-001

---

**End of Document**
