# PHASE 0 → таблицы (тестовый прогон)

Цель: прогнать полный цикл на тестовых данных и получить готовые таблицы/витрины в каталоге `DEV/05_NEXT_DEVELOPMENT/test`.

## Шаги

1) Обновить витрины (нормализация + инвентаризация)
- Запустить: `py DEV/05_NEXT_DEVELOPMENT/scripts/run_inventory.py`
- Проверить отчёт: `DEV/05_NEXT_DEVELOPMENT/ARCHITECTURE_PLAN/reports/inventory_run.md`
- Проверить, что обновились:
  - `_normalized/` (CSV/JSON)
  - `ARCHITECTURE_PLAN/data_listing_structured.json`
  - `ARCHITECTURE_PLAN/data_listing_markdown.json`

2) Сформировать вход для БД (выгрузка в тестовую папку)
- Скопировать (или ссылаться):
  - `ARCHITECTURE_PLAN/data_listing_structured.json`
  - `ARCHITECTURE_PLAN/data_listing_markdown.json`
- Сохранить копии в `DEV/05_NEXT_DEVELOPMENT/test/data_listing_structured.json` и `.../data_listing_markdown.json` (для изолированного теста).

3) Подготовить целевые таблицы (DDL — при необходимости)
- DDL в `DEV/05_NEXT_DEVELOPMENT/test/schema.sql` (PostgreSQL) покрывает все поля витрин:
  - `researches` — `research_id, name, description, department, status, created_date, updated_date, researcher_id, metadata, output_path`
  - `videos` — `video_id, queue_id, video_title, channel_name, channel_url, video_url, views, likes, comments, publish_date, duration, added_by, added_date, status, selected_by, selected_date, parsed_date, topic_category, research_source, priority_score, notes, created_date, completed_date, channel_id, transcript_path, phase`
  - `search_queue` — `search_id, employee, department, topic, query, status, videos_found, date_assigned, date_completed, results_path, priority, assigned_to, notes`
  - `tool_mapping` — `name, tool_id, category, file_path`
  - `discovered_tools` — `name, status, category, source, tool_id`
  - `markdown_files` — `path, entity_id, entity_type, department, status, phase, last_modified`

4) Загрузка тестовых данных
- Использовать `DEV/05_NEXT_DEVELOPMENT/test/load_to_db.py` (psycopg2, COPY):
  - Требуются переменные окружения: `PGHOST`, `PGPORT`, `PGUSER`, `PGPASSWORD`, `PGDATABASE`.
  - Запуск: `py DEV/05_NEXT_DEVELOPMENT/test/load_to_db.py`
  - Скрипт читает `test/data_listing_structured.json` и `test/data_listing_markdown.json` и грузит в таблицы `researches`, `videos`, `search_queue`, `tool_mapping`, `discovered_tools`, `markdown_files`.

5) Проверки (минимальные)
- Статусы в таблицах соответствуют enum из `DATA/id_and_status_rules.md`.
- Нет пропавших строк: сравнить counts с `inventory_run.md`.
- Проверить уникальность ключей (`research_id`, `video_id`, `search_id`).

6) Зафиксировать результат теста
- Создать отчёт `DEV/05_NEXT_DEVELOPMENT/test/PHASE0_TO_TABLES_REPORT.md`:
  - как загружали (команда/скрипт);
  - итоги по counts;
  - замеченные проблемы (например, пустые поля, некорректные статусы).

Готово: после прохождения этого чек-листа у тебя есть воспроизводимый путь «Phase 0 данные → таблицы» на тестовом наборе, что можно перенести в основную среду.***
