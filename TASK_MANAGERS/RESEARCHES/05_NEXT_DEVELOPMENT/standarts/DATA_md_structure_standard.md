# DATA: стандарты каталогов и Markdown

## Цель
Установить единый способ категоризации Markdown-файлов в `./DATA`, стандартизировать дерево каталогов и шаблоны имен/контента, чтобы все файлы однозначно относились к своей категории по имени каталога.

## Быстрый инвентарь (на 2025-11-26)
| Каталог               | MD | Комментарий                                    |
|-----------------------|----|-----------------------------------------------|
| ./ (корень DATA)      | 5  | README, SYSTEM_OVERVIEW, DASHBOARD_PROMPT и др. |
| 00_SEARCH_QUEUE       | 1  | Очередь поиска                                 |
| 01_VIDEO_QUEUE        | 5  | Очередь видео и инструкции                     |
| 02_TRANSCRIPTIONS     | 34 | Транскрипты и связанные сводки                 |
| 03_ANALYSIS           | 26 | Подкаталоги Gap_Analysis, Extractions и др.    |
| 04_INTEGRATION        | 0  | Пусто                                          |
| ARCHIVE               | 70 | Исторические материалы                         |
| DATA                  | 2  | Дублирующие/старые исследования                |
| PROMPTS               | 26 | Промпты                                        |
| REPORTS               | 19 | Отчеты                                         |
| scripts               | 1  | README                                         |
| TAXONOMY              | 2  | Таксономия                                     |
| templates             | 0  | Пусто                                          |
| _backups              | 0  | Пусто                                          |

## Базовое правило категоризации
- Категория файла = имя каталога верхнего уровня `DATA/<Каталог>`, в котором лежит файл.  
- Подкаталог уточняет подкатегорию, но основная категория не меняется.  
- Файлы в корне `DATA` получают категорию `ROOT`.  
- Архивные материалы получают категорию `ARCHIVE/<подкаталог>` и не смешиваются с активными.

## Целевая структура каталогов
```
DATA/
  00_SEARCH_QUEUE/
    README.md
    SQ-<id>_<topic>.md               # задачи/результаты поиска

  01_VIDEO_QUEUE/
    README.md
    VQ-<id>_<topic>.md               # описание очереди
    VQ-<id>_Processing_Summary.md    # сводка обработки

  02_TRANSCRIPTIONS/
    README.md
    VID-<id>_<title>_Transcript.md
    VID-<id>_Processing_Summary.md
    VIDEOS_INDEX.md                  # индекс по всем видео

  03_ANALYSIS/
    README.md
    Gap_Analysis/VID-<id>_Gap_Analysis.md
    Extractions/VID-<id>_Extraction.md
    Integration/VID-<id>_Integration.md
    Library_Mapping/VID-<id>_Library_Mapping.md
    Phase_Reports/Phase_<n>_Report.md
    Validation/VID-<id>_Validation.md

  04_REPORTS/                        # переименовать REPORTS
    README.md
    RPT-YYYYMMDD_<scope>.md          # сводные отчеты, статусы

  05_PROMPTS/                        # переименовать PROMPTS
    README.md
    PMT-<num>_<Topic>.md

  06_TAXONOMY/                       # переименовать TAXONOMY
    README.md
    TAX-<topic>.md

  07_SCRIPTS/                        # переименовать scripts
    README.md

  templates/
    TEMPLATE_<type>.md               # готовые шаблоны под типы ниже

  ARCHIVE/
    YYYY/                            # архив по годам или проектам
      <scope>/...

  legacy/                            # перенести DATA/DATA, _backups, прочие дублеты
    ...
```

## Стандарт именования файлов
- Префикс = идентификатор сущности, далее ключевой контекст через `_`, слова в `Pascal_Snake_Case`.
- Базовые префиксы:
  - `SQ-<id>` — задачи/лог поиска.
  - `VQ-<id>` — очередь видео.
  - `VID-<id>` — конкретное видео (транскрипт, анализ, интеграция, лог).
  - `RPT-<YYYYMMDD>` — отчеты/сводки.
  - `PMT-<num>` — промпты (сохранить текущий формат).
  - `TAX-<topic>` — таксономия.
- Обязательные суффиксы для типов:
  - `_Transcript`, `_Processing_Summary`, `_Execution_Flow`, `_Gap_Analysis`, `_Library_Mapping`, `_Integration`, `_Validation`, `_Work_Log`, `_Index`.
- README в каждом каталоге: `README.md` с описанием назначения каталога и ссылкой на индекс.

## Минимальный шаблон Markdown
```
---
category: 02_TRANSCRIPTIONS           # имя каталога
subcategory: Gap_Analysis             # имя подкаталога или тип
type: transcript|analysis|report|prompt|taxonomy|log
source_id: VID-024
title: <краткое название>
date: 2025-11-24
status: draft|final
owner: <ник/отдел>
related: [VID-024, RPT-20251124]
links:
  - <url или относительный путь>
---

# <Человекочитаемый заголовок>

## Summary
- Ключевые выводы в 3–5 пунктах.

## Details
- Основная информация по теме файла (транскрипт/анализ/шаги).

## Actions / Next Steps
- Что нужно сделать, дедлайны, ответственные.
```

## Правила для ключевых каталогов
- `00_SEARCH_QUEUE`: каждое задание поиска — отдельный `SQ-<id>_<topic>.md`; в README хранить список активных и архивных задач.
- `01_VIDEO_QUEUE`: единый `README` с процессом; по каждому видео — `VQ-<id>_<topic>.md` + при наличии `_Processing_Summary`.
- `02_TRANSCRIPTIONS`: одна запись на видео; общий индекс `VIDEOS_INDEX.md` с статусами; транскрипты и их сводки держать рядом.
- `03_ANALYSIS`: разбивать только по подкаталогам типов анализа (Gap_Analysis, Extractions и т.д.); имя файла всегда начинается с `VID-<id>`.
- `04_REPORTS`: все сводные отчеты, статусы, пайплайн-обзоры; дата в имени, без привязки к конкретному видео.
- `05_PROMPTS`: текущий формат `PMT-<num>_<Topic>` оставить, добавить README с описанием полей и версионности.
- `06_TAXONOMY`: любые версии таксономий и интеграционных сводок; версия или дата в имени (`TAX-<topic>_v1`, `TAX-<topic>_20251124`).
- `ARCHIVE`: переносить устаревшие документы без изменения имени, но упаковывать по годам/проектам.
- `templates`: хранить готовые шаблоны для каждого типа (`TEMPLATE_transcript.md`, `TEMPLATE_analysis.md`, `TEMPLATE_report.md`, `TEMPLATE_prompt.md`).

## План действий по выравниванию
1) Переименовать каталоги в целевую схему (`REPORTS`→`04_REPORTS`, `PROMPTS`→`05_PROMPTS`, `TAXONOMY`→`06_TAXONOMY`, `scripts`→`07_SCRIPTS`), создать `legacy/` и перенести `DATA/DATA`, `_backups`, пустые `templates` заполнить шаблонами.  
2) Добавить `README.md` в каждый каталог с назначением, ссылкой на индекс и списком владельцев.  
3) Применить единый шаблон фронт-маттер + секции ко всем новым/обновляемым MD.  
4) Обновить имена файлов под префиксы/суффиксы (в частности, все `Video_XXX` → `VID-XXX_*`).  
5) Создать/обновить индексы: `VIDEOS_INDEX.md` в транскрипциях, `INDEX.md`/`README` в каждом подкаталоге анализа и отчетов.  
6) Переместить исторические файлы в `ARCHIVE/` по годам/проектам, оставив в активных каталогах только актуальные версии.  
7) Поддерживать CSV/JSON-индекс (`md_listing.*`) в `DEV/05_NEXT_DEVELOPMENT` синхронно с новыми именами, чтобы автоматизировать поиск.
