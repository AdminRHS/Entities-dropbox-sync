# Задачи по витринам данных (structured/markdown)

- При обновлении нормализованных CSV/JSON/MD запускать `py DEV/05_NEXT_DEVELOPMENT/scripts/aggregate_data_listings.py` для пересборки:
  - `ARCHITECTURE_PLAN/data_listing_structured.json`
  - `ARCHITECTURE_PLAN/data_listing_markdown.json`
- Проверить единый enum статусов: при появлении новых значений добавить маппинг в `aggregate_data_listings.py`.
- При необходимости включить дополнительные источники (новые нормализованные файлы) в агрегатор.
- Добавить запись прогона в `reports/md_inventory_report.md` и `reports/csv_normalization_report.md`/`json_normalization_report.md` перед сборкой (чтобы витрина ссылалась на свежие данные).
- Использовать `py DEV/05_NEXT_DEVELOPMENT/scripts/run_inventory.py` как единый запуск (нормализация CSV/JSON + md_inventory + агрегатор + отчёт `ARCHITECTURE_PLAN/reports/inventory_run.md` и блок в README).
