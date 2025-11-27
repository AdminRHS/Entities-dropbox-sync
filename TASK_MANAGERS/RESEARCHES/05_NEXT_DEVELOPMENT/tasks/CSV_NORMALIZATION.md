# Задачи по нормализации CSV (Phase 0)

- При каждом изменении исходных CSV запускать `python DEV/05_NEXT_DEVELOPMENT/scripts/normalize_csv_phase0.py` для обновления `_normalized` и `reports/csv_normalization_report.md`.
- Заполнить пустые поля в нормализованных файлах:
  - `RESEARCHES_Master_List_normalized.csv`: `created_date`, `updated_date`, `researcher_id`, `metadata`, `output_path`.
  - `Video_Queue_Master_normalized.csv`: `channel_id`, `transcript_path`, `phase` (и при появлении статусов вне enum — дополнить маппинг).
  - `Search_Queue_Master_normalized.csv`: `priority`, `assigned_to`, `results_path` (если появятся исходные значения).
- Зафиксировать стратегию маппинга статусов видео: сейчас `pending→queued`, `selected→analyzing`, `parsed→completed`; при появлении новых статусов добавить в словарь.
- При необходимости расширить скрипт проверкой типов и валидацией дат перед импортом.
