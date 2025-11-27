# DATA LISTINGS (Phase 0 оперативный срез)

Цель: показать лучшие варианты каталогизации CSV/JSON/Markdown источников, сверить фактические схемы таблиц и зафиксировать число активных сущностей по двум витринам данных.

## Итог кратко
- Нашлись 3 CSV (2 очереди + мастер-список), 11 JSON (инфлюенсеры, каналы, ToDo-бэклоги, archive mappings) и 191 Markdown-файл.
- Активные сущности: 25 исследований (100% `Active`), 5 видео в очереди (Pending/Selected/Parsed), 0 поисковых задач в очереди.
- Расхождение с целевой схемой Phase 0: поля и кейсы в CSV/JSON не стандартизированы; `tool_mapping.json` содержит дубликаты ключей по регистру.

## Data Listing 1 — Структурированные источники (CSV/JSON)

### CSV
| Файл | Строк | Статусы | Колонки (факт) |
| --- | --- | --- | --- |
| `DATA/00_SEARCH_QUEUE/Search_Queue_Master.csv` | 0 | — | Search_ID, Employee, Department, Topic, Search_Query, Status, Videos_Found, Date_Assigned, Date_Completed, Notes |
| `DATA/01_VIDEO_QUEUE/Video_Queue_Master.csv` | 5 | Pending:3 / Selected:1 / Parsed:1 | Queue_ID, Video_ID, Video_Title, Channel_Name, Channel_URL, Video_URL, Views, Likes, Comments, Publish_Date, Duration, Added_By, Added_Date, Status, Selected_By, Selected_Date, Parsed_Date, Topic_Category, Research_Source, Priority_Score, Notes |
| `DATA/RESEARCHES_Master_List.csv` | 25 | Active:25 | RSR_ID, Name, Description, Department, Category, File_Path, Status |

### JSON
| Файл | Записей | Структура/замечания |
| --- | --- | --- |
| `DATA/ARCHIVE/04_INFLUENCER_DATA/Influencer_Database.json` | 6 | Вложенные блоки (platforms, content_classification, discovery, engagement_metrics, tracking); поля отличаются от схемы в PHASE_0 (нет flat `platform`, `subscriber_count`) |
| `DATA/ARCHIVE/04_INFLUENCER_DATA/YouTube_Channels.json` | 6 | Каналы с метриками и связью `influencer_id`; структура устойчивая |
| `DATA/ARCHIVE/Pre_Taxonomy_Cleanup/ToDo/*.json` (4 файла) | 26 всего (10/6/6/4) | `tools_to_research` со статусом `pending`; хорошая схема (entity_type, research_session, tools_to_research[…]) |
| `DATA/ARCHIVE/Pre_Taxonomy_Cleanup/Research_Reports/Extractions/discovered_tools.json` | 253 | Плоский массив строк, без схемы — нужен маппинг полей перед импортом |
| `DATA/ARCHIVE/Pre_Taxonomy_Cleanup/Research_Reports/Extractions/tool_mapping.json` | ≈253 | Объект key→{tool_id, category, file_path}; содержит дубли ключей по регистру — не парсится через `ConvertFrom-Json` без нормализации |
| `DATA/ARCHIVE/Pre_Taxonomy_Cleanup/TSM-008_Video_Queue/VIDEO-001_ToDo_List_Tutorial_Project_Template.json` | 1 | Шаблон с множеством массивов (milestones, task_sequence, etc.); можно использовать как reference-схему |
| `DATA/REPORTS/integration_report_Video_022_*.json` (2 файла) | 2 | Дублирующиеся интеграционные отчёты, структура стабильная |

### Проверка схем vs целевой базы (PHASE_0 → researches/videos/search_queue)
- `RESEARCHES_Master_List.csv` покрывает `research_id/title/department/status`, но нет полей `researcher_id`, `created_date`, `updated_date`, `metadata`. Нужно расширить перед загрузкой в таблицу `researches`.
- `Video_Queue_Master.csv` не содержит `channel_id`, `created_date`, `completed_date`; даты в формате `YYYY-MM-DD` + `MM:SS` для Duration — придётся нормализовать в `TIMESTAMP`/`INTERVAL`.
- `Search_Queue_Master.csv` имеет только шапку; формат колонок близок к целевому `search_queue`, но названия в `PascalCase` и отсутствует `query/results_path`.
- JSON инфлюенсеров расходится с ожидаемыми полями (`primary_platform` + вложенные метрики вместо плоских столбцов); при импорте в `influencers` потребуется маппинг и денормализация.

## Data Listing 2 — Markdown корпус

| Каталог (DATA/…) | Кол-во .md | Примечание |
| --- | --- | --- |
| 02_TRANSCRIPTIONS | 34 | Базовые стенограммы (Video_001…026) + трекеры; одна запись с битой кодировкой в имени `Video_024 (...)` |
| 03_ANALYSIS | 26 | Gap/Libray Mapping/Phase reports, execution plans |
| PROMPTS | 26 | Исходные research-промпты по отделам |
| REPORTS | 19 | Отчёты по очередям/процессингу/консолидации |
| ARCHIVE | 70 | Исторические логи, методологии, старые отчёты |
| 01_VIDEO_QUEUE | 5 | README/гайды очереди |
| 00_SEARCH_QUEUE | 1 | README |
| TAXONOMY | 2 | Черновики таксономии исследований |
| Прочее (корень DATA, DATA/DATA) | 8 | Обзорные материалы (`SYSTEM_OVERVIEW.md`, RSH-VID-001_AI_Video_Tools_Research.md, и др.) |

Всего Markdown: 191.

## Активные сущности (на основе источников)
- Исследования: 25/25 `Active` в `RESEARCHES_Master_List.csv`.
- Видеоочередь: 5 элементов (Pending 3, Selected 1, Parsed 1) в `Video_Queue_Master.csv`.
- Поисковая очередь: 0 записей (только шапка) в `Search_Queue_Master.csv`.
- ToDo backlog (archive): 4 файла, 26 задач со статусом `pending`.
- Инфлюенсеры/каналы: 6 + 6 записей, актуальность по `last_updated` 2025-11-13.

## Рекомендованный вариант действий
- Свести схемы к целевым именам Phase 0: унифицировать регистр/нейминг колонок в CSV и добавить недостающие поля (`created_date`, `researcher_id`, `query`, `results_path`).
- Очистить JSON перед импортом: нормализовать ключи в `tool_mapping.json` (lower-case + resolve дубли), задать явную схему для `discovered_tools.json` (tool_id, category, source, status).
- Зафиксировать Markdown-источники как неструктурированные: использовать ETL для извлечения метаданных (ID, department, статус) и связать с таблицами `researches`/`reports`.
- Для учёта активных сущностей: сделать две витрины (data listings) — (1) структурированные CSV/JSON с нормализованными статусами; (2) Markdown корпус с вычисляемыми полями (`entity_id`, `department`, `phase`, `last_modified`), обновляемые скриптом инвентаризации.
- Поддерживать актуальность: добавить скрипт-инвентарь (`scripts/`) с выводом counts/статусов + валидацией схем (header check, типы) и записывать результат в README Phase 0 перед каждым импортом.

---

## Как сделать (пошаговый план реализации)

### 1) Нормализация CSV (Phase 0 схемы)
- Целевая схема `researches`: добавить в `RESEARCHES_Master_List.csv` поля `created_date`, `updated_date`, `researcher_id`, `metadata` (JSON string), `output_path`; привести названия к snake_case. Временное решение: добавить пустые колонки, далее заполнить по файлам.
- Целевая схема `videos`: в `Video_Queue_Master.csv` добавить `created_date` (из `Added_Date`), `completed_date` (пусто/из Parsed_Date), `channel_id` (lookup позже), `transcript_path` (если есть), `phase`; привести статусы к enum (`queued`, `transcribing`, `analyzing`, `completed`, `failed`).
- Целевая схема `search_queue`: в `Search_Queue_Master.csv` добавить `query` (копия Search_Query), `results_path` (пусто), `priority` (int), `assigned_to`; переименовать шапку в snake_case.
- Инструмент: небольшой Python/PowerShell трансформер в `scripts/normalize_csv_phase0.py`:
  - Читает CSV → проверяет/добавляет колонки → переименовывает → сохраняет *_normalized.csv рядом.
  - Проверяет хедеры против эталона и пишет отчёт в `DEV/05_NEXT_DEVELOPMENT/ARCHITECTURE_PLAN/README.MD` (append).

### 2) Очистка JSON перед импортом
- `tool_mapping.json`: прочитать как dict, нормализовать ключи (lower-case/trim), если дубли по ключу — складывать в массив или брать первый и логировать конфликт. Сохранить в `tool_mapping_normalized.json` с явной схемой `{name, tool_id, category, file_path}`.
- `discovered_tools.json`: конвертировать массив строк → массив объектов со схемой `{tool_id: null, name: <строка>, category: null, source: "discovered_tools.json", status: "pending"}`; сохранить как `discovered_tools_structured.json`.
- Добавить в `scripts/normalize_json_phase0.py` две функции `normalize_tool_mapping()` и `structure_discovered_tools()`, плюс отчёт по конфликтам в `DEV/05_NEXT_DEVELOPMENT/ARCHITECTURE_PLAN/json_normalization_report.md`.

### 3) Markdown как неструктурированные источники
- Шаги ETL (скрипт `scripts/md_inventory.py`):
  1. Собрать все `.md` в `DATA/**`.
  2. Для каждого файла извлечь метаданные: `entity_id` (regex `RSH-|Video_|RSR-|TASK-|WRF-`), `department` (по пути или хедеру), `status` (по встречаемым тегам `Active/Archived/Draft`), `phase` (если есть в имени/папке), `last_modified` (mtime).
  3. Вывести CSV `DEV/05_NEXT_DEVELOPMENT/md_listing.csv` и JSON `md_listing.json`.
  4. Для связки с таблицами: создать поле `entity_type` (`research`, `video`, `report`, `prompt`, `analysis` по пути).

### 4) Две витрины данных
- `structured_listing` (CSV/JSON): объединить `RESEARCHES_Master_List_normalized.csv`, `Video_Queue_Master_normalized.csv`, `Search_Queue_Master_normalized.csv`, `Influencer_Database_normalized.json`, `YouTube_Channels_normalized.json`, `tool_mapping_normalized.json`, `discovered_tools_structured.json`. Добавить нормализованный статус (map в единый enum).
- `markdown_listing`: результаты `md_inventory.py` с вычисляемыми полями.
- Финальный вывод хранить в `DEV/05_NEXT_DEVELOPMENT/ARCHITECTURE_PLAN/data_listing_structured.json` и `data_listing_markdown.json`.

### 5) Инвентаризационный скрипт (поддержка актуальности)
- Скрипт `scripts/run_inventory.ps1` или `scripts/run_inventory.py`:
  - Запускает нормализацию CSV/JSON и `md_inventory`.
  - Делает header check (ожидаемые колонки) и типовой check (дата/enum).
  - Считает метрики: количества по статусам, по типам файлов, последние обновления.
  - Аппендит сводку в `DEV/05_NEXT_DEVELOPMENT/ARCHITECTURE_PLAN/README.MD` (раздел "Last inventory run: <timestamp>").
  - Файлы отчётов складывает в `DEV/05_NEXT_DEVELOPMENT/ARCHITECTURE_PLAN/reports/`.

### 6) Мини-сниппет для нормализации CSV (Python)
```python
import csv, pathlib

TARGETS = {
    "researches": ["research_id","title","department","status","created_date","updated_date","researcher_id","output_path","metadata"],
    "videos": ["queue_id","video_id","title","channel_name","channel_url","video_url","views","likes","comments","publish_date","duration","added_by","added_date","status","selected_by","selected_date","parsed_date","topic_category","research_source","priority_score","notes","channel_id","created_date","completed_date","transcript_path","phase"],
    "search_queue": ["search_id","employee","department","topic","query","status","videos_found","date_assigned","date_completed","results_path","priority","assigned_to","notes"]
}

def normalize_csv(src, target_cols):
    rows = list(csv.DictReader(open(src, newline='', encoding="utf-8")))
    for r in rows:
        for col in target_cols:
            r.setdefault(col, "")
    out = src.with_name(src.stem + "_normalized.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=target_cols)
        writer.writeheader()
        writer.writerows([{k: r.get(k, r.get(k.title(), r.get(k.upper(), ""))) for k in target_cols} for r in rows])
    return out
```

### 7) Мини-сниппет для нормализации `tool_mapping.json`
```python
import json, pathlib, collections

def normalize_tool_mapping(path: pathlib.Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    out = []
    seen = collections.defaultdict(list)
    for raw_key, payload in data.items():
        key = raw_key.strip().lower()
        seen[key].append(payload)
    conflicts = {k:v for k,v in seen.items() if len(v) > 1}
    for key, items in seen.items():
        first = items[0]
        out.append({
            "name": key,
            "tool_id": first.get("tool_id"),
            "category": first.get("category"),
            "file_path": first.get("file_path")
        })
    path.with_name(path.stem + "_normalized.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    (path.parent / "tool_mapping_conflicts.json").write_text(json.dumps(conflicts, indent=2), encoding="utf-8")
```

### 8) Интеграция в Phase 0 README
- Добавить раздел "Inventory pipeline" в `ARCHITECTURE_PLAN/README.MD` с командами:
  - `python scripts/normalize_csv_phase0.py`
  - `python scripts/normalize_json_phase0.py`
  - `python scripts/md_inventory.py`
  - `python scripts/run_inventory.py` (агрегатор)
- Каждый прогон обновляет timestamp + метрики (counts, статусы) и пути к свежим витринам.
