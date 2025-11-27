# Задачи по инвентаризации Markdown

- Держать актуальными `DEV/05_NEXT_DEVELOPMENT/md_listing.csv` и `md_listing.json`: запускать `py DEV/05_NEXT_DEVELOPMENT/scripts/md_inventory.py` после изменений в `DATA/**`.
- Проверить и при необходимости улучшить извлечение:
  - `entity_type` — уточнить правила для новых папок (например, если появятся другие отделы/вью).
  - `status` — добавить поиск статусов из front-matter, если появится.
  - `department` — при необходимости брать из хедера файла (сейчас — первый сегмент пути).
- Заполнить `reports/md_inventory_report.md` актуальным прогоном (если пустой).
- Использовать listing для сопоставления с таблицами `researches/reports/videos` и выявления файлов без `entity_id`.
