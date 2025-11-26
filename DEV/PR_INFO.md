# ENTITIES (корень)
- Рабочее пространство ENTITIES: справочники, промпты, задачи, настройки и аналитика для миграций и автоматизаций.

## Файлы в корне
- `analysis_report.md` – итог скрипта анализа сущностей и ссылок.
- `analyze_entities.py` – прогоняет валидацию JSON/ID и пишет `analysis_report.md`.
- `update_prompts_references.py`, `update_library_paths.py` – вспомогательные апдейтеры ссылок/путей после миграций.
- `ARCHITECTURE_UPDATE_PLAN.md` – план обновления архитектуры ENTITIES.
- `create_entities_master_list.py` – генерация сводного списка сущностей.
- `ENTITIES_MASTER_LIST.csv`, `ENTITIES_MASTER_LIST_SUMMARY.md` – итоговые реестры сущностей.
- `FINAL_MIGRATION_SUMMARY_2025-11-17.md`, `MIGRATION_COMPLETED_2025-11-17.md`, `MIGRATION_PLAN_Actions_Objects.md` – отчёты о миграциях и план объединения action/object.

# ARCHIVE
- Архив старых миграций, промптов, избыточных файлов и вспомогательных скриптов; используется только для истории.

## ANALYTICS
- Отчёты и скрипты по аналитике (например, посещаемость удалённых хелперов), журналы задач/шагов/проектов, очистка дублей милстоунов.

## Migration_History
- Полный след миграций: `Scripts/` (бат/ps1 для миграции и референс-сканов), `Documentation/`, `Reports/`, `Step_Templates/` с готовыми шаблонами шагов.

## Prompts_Archive
- Архивные промпты по миграциям и объявлениям.

## Scripts
- Исторические утилиты: `Migration/`, `Generation/`, `Processing/`, `Extraction/`.
- `Extraction/LIBRARIES/extract_processes_results.ps1` – вытаскивает процессы/результаты из `actions.json`, группирует по категориям и сохраняет библиотеки.
- `Extraction/LIBRARIES/Responsibilities/extract_action_object_pairs.py` – собирает пары action+object из шаблонов задач для слияния в Responsibilities.

## Redundant_Files
- Сборник файлов, признанных избыточными при миграциях, с отчётом `Redundancy_Report.md`.

## TSM-008_RESEARCHES_Deprecated_2025-11-20
- Замороженные материалы по ресёрчам Task Managers (до миграции в актуальные каталоги).

## Дополнительные архивы
- `ANALYTICS/reports`, `Steps`, `Milestones`, `Projects`, `tests` – исторические данные и вспомогательные скрипты.
- В корне: `TAXONOMY_GUIDELINES.md`, `README.md`, `Redundancy_Report.md` – описание архива и итоговые отчёты.

# ASSETS
- Каталог активов проекта oa-y (обучающие материалы, тесты, курсы).

## oa-y
- Управляющие файлы экспорта (`EXPORT_PROGRESS.md`, `OAY_Asset_Registry.json`, `FILE_MAP.md`, `Prompt.md`, статусные markdown).
- Подкаталоги `Courses/`, `Lessons/`, `Modules/`, `TASKS/`, `Tests/` с детализированными единицами контента для онбординга и тестирования.

# DAILIES
- Ежедневные файлы сотрудников, отчёты, планы и импорты; используется для обработки дэйли-логов и последующей экстракции сущностей.

## Daily_Processing
- Регламент и структура папок для ежедневной обработки (`README.md`), примеры коллекций с собранными файлами, извлечёнными задачами и логами.

## IMPORTS
- Импортные кампании (Week_3) с пайплайнами по фазам: очистка, мэппинг полей, обогащение, генерация JSON, валидация и статистика. Присутствуют отчёты (`FINAL_IMPORT_SUMMARY.md`, `validation_report.md`) и архивы данных (Prospects/Clients/Ex_Clients).

## LOG
- Журналы рабочих сессий (создание промптов, проектирование БД, генерация ежедневных отчётов).

## PLANS
- Планирование для недельного цикла (Week_3, System_Rebuild) и интеграций департаментов: дорожные карты фаз, планы багфиксов, спецификации импорта бизнесов.

## REPORTS
- Сводные отчёты по дэйли-процессингу (например, 2025-11-19) с логами и срезами по департаментам.

## Week3
- Поддаты `18/`, `19/`, `20/`, `21/` с десятками персональных файлов: `daily`, `plans`, `task(s)`, `todo`, `report` и т.п. по каждому сотруднику/департаменту; отдельные анализы (gap, verb forms) и мастер-выгрузки (`MASTER_OUTPUT.*`).

# DEV
- Рабочая зона для вспомогательной документации; сюда сохранён `PR_INFO.md`.

# JOBS
- `README.md` и `POPULATE_JOBS_PROMPT.md` – описание сущности JOBS и промпты для автонаполнения вакансий.

# LIBRARIES
- Центральный справочник знаний: действия, объекты, департаменты, профессии, инструменты, соцмедиа, таксономии и экосистема Responsibilities.

## Archive
- Старые действия/объекты и миграционные артефакты: `Backups/` (мастера действий/процессов/результатов, архивированные процессы), `_old_LBS_001_Actions/`, `Legacy_Root_Files/`.
- Отчёты и логи миграций (`migration_report.*`, `integration_update_log.json`, `INTEGRATION_REPORT_2025-11-22.md`, `SKILLS_INTEGRATION_COMPLETE_2025-11-22.md`) и справки по структурам ID/папок.

## LBS_003_Tools
- Библиотека инструментов/платформ по категориям (AI, Dev, Data, Security, Publishing, Freelance и др.) с JSON-файлами по каждому сервису.
- Скрипты миграции (`run_complete_migration.py`, `migrate_tools_to_tol.py`, фазовые апдейтеры) и `MIGRATION_README.md`.

## LBS_005_Professions
- Справочник профессий: `Master/` агрегирует полный список, `Individual/` содержит файлы по отдельным профессиям; README описывает атрибуты и коды.

## LBS_006_Departments
- Описание департаментов, их коды, цвета и функции (`departments.json`, `README.md`); есть общие ресурсы (`README_SHARED_RESOURCES.md`) и вложенный SMM-блок.
### SMM
- Материалы для соцсетей: планы интеграции, отчёты по документам, дорожка по влиянию (Influencer_Tracking/YouTube_Channels.json, базы инфлюенсеров).

## Responsibilities
- Единая экосистема обязанностей: `Core/` (master, индексы вариантов действий/объектов), `Objects/` (категории объектов/доставляемых результатов), `Integration/` (phrase_combinations, parameter mapping), `Parameters/` (по профессиям/департаментам), `By_Department/` и `_ARCHIVE/` (устаревшие выгрузки).
- Валидаторы и миграционные скрипты (`migrate_*`, `validate_ecosystem.py`, `ecosystem_validation_report.json`), отчёты интеграции и покрытие шагов.

## SMM (корень LIBRARIES)
- Аналитика и интеграционные отчёты по стратегиям в соцсетях, таксономия контента и сценарии общения (Instagram DMs и т.д.).

## Taxonomy
- Таксономические артефакты LIBRARIES: master-листы, реестры ISO-кодов, деревья и распределения по департаментам; скрипт `generate_master_list.py`.

## Плановые и объектные файлы
- `PLANNING.md`, `OBJECTS_README.md`, `LBS_FOLDER_MASTER.*` – сводные планы, справка по объектам и карта путей всех LBS-папок.

# PROMPTS
- Каталог рабочих промптов PMT-### и связанных инструкций.

## _INDEX
- Индексы и реестры промптов (иерархия, ISO-коды, миграционные логи, master CSV/JSON).

## _ARCHIVE
- Старые версии промптов (MAIN_PROMPT v2/v3, Call Organizer v2/v3, устаревшие инструкции).

## Automation/Core/CREATIVES/DATA_FIELDS/DEPARTMENTS/SYSTEM/UTILITIES
- Тематические подборки промптов: ядро системы (main prompts v4/v6), автоматизация, креативные задачи, шаблоны данных, департаментные промпты, системная архитектура и утилиты коммуникаций/дайджестов.

## WORKFLOWS
- Готовые операционные сценарии (аккаунт-менеджмент, обработка библиотек, документирование проектов, call organizer v4, daily report processing) плюс видео-обработки (PMT-004..012, 071).

## Корневые промпты
- Отдельные файлы PMT-004..012, 071, AutoGenerate_Weekly_Plans, BUSINESSES_IMPORT_PROMPT, TAXONOMY_AUDIT_REPORT и др. для быстрого запуска без навигации в подпапки.

# RESEARCHES
- Исследования по видео: транскрипции (`02_TRANSCRIPTIONS/`), анализы и gap-отчёты (`03_ANALYSIS/Gap_Analysis/`), текущие материалы в `VIDEO_RESEARCHES/`.

# SETTINGS
- Централизованные конфиги и справочные данные (страны, валюты, статусы, сервисы авторизации, talentdb).

## Countries / Currencies / Statuses
- JSON-реестры стран, валют (ISO-коды), статусов; используются для нормализации данных.

## Auth User Service
- Markdown с требованиями/описанием службы авторизации.

## talentdb.md
- Спецификация БД талантов и связанных сущностей.

# TALENTS
- Управление талантами: навыки, кандидаты, сотрудники, аналитика посещаемости и шаблоны коммуникации.

## Skills
- Полный каталог навыков (`Master/`), срезы по департаменту/профессии/сложности/инструменту, маппинги, шаблоны оценок и планов развития; README с миграционной справкой.

## Employees
- Структура полей сотрудника (`units/*.json`, схемы профиля), профили (Work/HR), инструкции по очистке и интеграции посещаемости.
- Логи посещаемости (`Voice Log Discord/*.json`, `crm_export_attendance/*.json`), аналитика (`attendance_analyzer/` с скриптами и конфигом), задачи по очистке данных.

## Candidates_JSON_Clusters
- Структура данных кандидатов (`Candidate Info/*.json`), архивные/тестовые кластеры, шаблоны полей.

## Templates
- Коммуникационные шаблоны (`Templates/Communication_Templates.json`) и другие вспомогательные файлы для работы с кандидатами/талантами.

## ANALYTICS файлов
- Отчёты/CSV по посещаемости в корне TALENTS (`ANALYTICS_Employees_Attendance_Remote_Helpers_*`).

# TASK_MANAGERS
- Шаблоны проектов/милстоунов/тасков/шагов, воркфлоу и гайды для управления задачами.

## TSM-001..006
- Каталоги Project/Milestone/Task/Step Templates и Checklists/Workflows с CSV/JSON и описаниями (см. `INDEX.md`, `PROJECTS_LISTING.md`, `Task_Templates_Listing*.md`).

## TSM-007_GUIDES
- Пакет гайдов (GDS-001..012), реестры ISO/иерархий, база инструментов, базы версий; база данных предпросмотров таблиц и методички по интеграции. README объясняет назначение и статус, есть SAMPLE-примеры мульти-форматных гайдов.

## RESEARCHES
- Материалы исследований для Task Managers, интеграции с другими сущностями.

## Прочие файлы
- `ARCHITECTURE_LOG.md`, `All_Migrations_Index.md`, `BUSINESSES_Import_TaskManager.md`, `Skills_Task_Linkage.md`, `FILES.md`, `TASK.md` – история миграций, архитектура и связи навыков/тасков.

# TAXONOMY
- Узел документации по ID и кодам; зеркала таксономий из других сущностей.

## TAX-001_Libraries
- Master-листы и деревья для LIBRARIES (кодовые реестры, распределение по департаментам, карты миграций).

## TAX-002_Task_Managers
- Таксономия Task Managers: master-листы, ISO-реестры, деревья и распределение департаментов для TSM.

## TAX-003_Video_Processing
- Специализированные материалы по интеграции видео-таксономии (например, PMT-009 Taxonomy Integration).

## TAX-004_Entity_Integration
- Документация и материалы по сквозной интеграции сущностей через таксономии (mirrors/артефакты).

## _ARCHIVE
- Архивные версии таксономий.

