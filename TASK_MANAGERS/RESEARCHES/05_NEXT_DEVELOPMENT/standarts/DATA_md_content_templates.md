# DATA: единая структура Markdown

Цель: сделать все MD в `./DATA` однотипными по фронт-маттеру, заголовкам и секциям, чтобы их можно было парсить и сравнивать автоматически.

## Универсальные правила для любого файла
- Фронт-маттер (yaml) обязателен и идет первой строкой:
  ```
  ---
  category: 02_TRANSCRIPTIONS        # имя каталога верхнего уровня
  subcategory: Gap_Analysis          # подкаталог или тип
  type: transcript|analysis|report|prompt|taxonomy|log|readme
  source_id: VID-024                 # идентификатор сущности
  title: Video 024 Processing Summary
  date: 2025-11-24
  status: draft|final
  owner: <nick|dept>
  related: [VID-024, RPT-20251124]   # список ссылок-идов
  links:
    - ../../03_ANALYSIS/Gap_Analysis/VID-024_Gap_Analysis.md
    - https://...
  ---
  ```
- Далее всегда:
  1) `# <Человекочитаемый заголовок>`
  2) `## Summary` — 3–7 пунктов, что важно знать.
  3) `## Context` — источник данных, цель документа.
  4) `## Data / Content` — основное тело (транскрипт, результаты поиска, инструкция).
  5) `## Findings` — ключевые выводы (если применимо).
  6) `## Actions / Next Steps` — что делать, дедлайны, ответственные.
  7) `## Metrics / Status` — статусы, метрики, чекпоинты (если есть).
  8) `## Attachments / Links` — внутренние/внешние ссылки.
  9) `## Change Log` — даты и краткие правки.
- Нельзя пропускать разделы, если они применимы. Если данных нет — ставить `- TODO` в разделе.

## Шаблоны по каталогу/типу
Ниже только различия от универсального скелета.

### 00_SEARCH_QUEUE
- `type: log` или `report`.
- `Data / Content`: описание запроса, параметры поиска, инструменты.
- `Metrics / Status`: статус выполнения, найдено N ссылок.

### 01_VIDEO_QUEUE
- `type: log`.
- `Data / Content`: шаги пайплайна, что уже сделано, что в очереди.
- `Metrics / Status`: этап (ingest/transcribe/analyze/integrate), ETA.

### 02_TRANSCRIPTIONS (транскрипты)
- `type: transcript`.
- `Data / Content`: сам транскрипт с таймкодами или блоками.
- `Findings`: тезисы по контенту.
- `Metrics / Status`: полнота, качество, версия.

### 03_ANALYSIS (базовый)
- `type: analysis`.
- `Context`: ссылка на транскрипт и задачу.
- `Data / Content`: структура зависит от подтипа.

#### 03_ANALYSIS/Gap_Analysis
- `Data / Content`: таблица/список разрывов и критериев.
- `Actions / Next Steps`: закрытие разрывов с владельцами.

#### 03_ANALYSIS/Extractions
- `Data / Content`: извлеченные сущности (таблицы/списки).
- `Metrics / Status`: полнота, валидность.

#### 03_ANALYSIS/Integration
- `Data / Content`: что интегрировано, куда, маппинги.
- `Actions / Next Steps`: что осталось внедрить.

#### 03_ANALYSIS/Library_Mapping
- `Data / Content`: соответствия и ссылки на библиотеки.
- `Metrics / Status`: покрытие маппинга.

#### 03_ANALYSIS/Phase_Reports
- `type: report`.
- `Data / Content`: цель фазы, что сделано/не сделано.
- `Metrics / Status`: KPI/статусы фазы.

#### 03_ANALYSIS/Validation
- `type: analysis`.
- `Data / Content`: тестовые кейсы и результаты.
- `Metrics / Status`: pass/fail, блокеры.

### 04_REPORTS
- `type: report`.
- `Data / Content`: агрегированные статусы, диаграммы (описанием).
- `Metrics / Status`: глобальные KPI, прогресс.

### 05_PROMPTS
- `type: prompt`.
- `Data / Content`: сама формулировка промпта.
- `Findings`: нюансы использования, ограничения.
- `Metrics / Status`: версия промпта, A/B результаты (если есть).

### 06_TAXONOMY
- `type: taxonomy`.
- `Data / Content`: дерево/таблица таксономии.
- `Actions / Next Steps`: изменения, согласования.
- `Metrics / Status`: версии, совместимость.

### 07_SCRIPTS
- `type: readme|log`.
- `Data / Content`: как запускать, зависимости, примеры вызова.
- `Actions / Next Steps`: pending улучшения/миграции.

### ARCHIVE / legacy
- Используют ту же структуру, но `status: archived` и `Context` указывает причину переноса.

## Чек-лист миграции существующих файлов
1) Добавить фронт-маттер с `category/subcategory/type/source_id/title/date/status/owner/related/links`.  
2) Привести заголовки к порядку: `# Title`, `Summary`, `Context`, `Data / Content`, `Findings`, `Actions / Next Steps`, `Metrics / Status`, `Attachments / Links`, `Change Log`.  
3) Для подтипов из 03_ANALYSIS заменить `Data / Content` на соответствующий формат (gap list, extraction table и т.д.).  
4) Заполнить хотя бы `Summary`, `Findings`, `Actions` — без них файл считается неконсистентным.  
5) В README каждого каталога описать назначение каталога, naming и ссылку на индекс.  
6) После миграции обновить индексы (например `VIDEOS_INDEX.md`, `md_listing.*`).

## Быстрый контроль консистентности (вручную)
- Проверить, что файл начинается с `---` и содержит все поля: `category`, `subcategory`, `type`, `source_id`, `title`, `date`, `status`, `owner`, `related`, `links`.  
- Проверить наличие всех секций по порядку (как минимум заголовки).  
- Убедиться, что `category` совпадает с каталогом, а `type` с шаблоном выше.
