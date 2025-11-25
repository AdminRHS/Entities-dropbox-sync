# Employee Attendance Analyzer

Комплексная система анализа посещаемости сотрудников на основе данных Discord Voice Log с продвинутой аналитикой, детекцией аномалий и визуализацией.

## Возможности

### Продвинутая аналитика:
- ✅ Расчет рабочих часов с учетом перерывов
- ✅ Выявление аномалий (слишком короткий/длинный день)
- ✅ Анализ паттернов по времени прихода/ухода
- ✅ Категоризация сотрудников по риску
- ✅ Статистический анализ (среднее, медиана, отклонение)

### Визуализация:
- ✅ Тепловая карта активности по часам
- ✅ Гистограмма распределения рабочих часов
- ✅ Временная шкала присутствия (Gantt)
- ✅ Scatter-график время прихода vs ухода
- ✅ Box plot для выявления выбросов
- ✅ Комплексный дашборд со всеми метриками

### Отчеты:
- ✅ Excel с множественными листами (Full Data, Active, Anomalies, Statistics)
- ✅ CSV экспорт
- ✅ Текстовые summary отчеты

## Установка

### 1. Установка Python зависимостей

```bash
cd scripts
pip install -r requirements.txt
```

Или с использованием виртуального окружения:

```bash
python3 -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Проверка структуры

Убедитесь, что структура папок выглядит так:

```
attendance_analyzer/
├── scripts/
│   ├── employee_analytics.py
│   ├── visualizations.py
│   └── requirements.txt
├── output/
│   ├── reports/       (создастся автоматически)
│   ├── charts/        (создастся автоматически)
│   └── summaries/     (создастся автоматически)
├── config/
│   └── analysis_config.json
└── README.md
```

## Использование

### Быстрый старт

#### 1. Запуск полного анализа

```bash
cd scripts
python employee_analytics.py
```

Этот скрипт:
- Загрузит данные из `../Voice Log Discord/crm_export_2025-11-18.json`
- Выполнит полный анализ с детекцией аномалий
- Сгенерирует Excel и CSV отчеты
- Создаст текстовый summary

#### 2. Генерация визуализаций

```bash
python visualizations.py
```

Этот скрипт создаст:
- 8 различных графиков в папке `output/charts/`
- Комплексный дашборд со всеми метриками

### Использование в коде

#### Пример 1: Базовый анализ

```python
from employee_analytics import EmployeeAnalytics

# Инициализация
analyzer = EmployeeAnalytics()

# Запуск полного анализа
df, stats = analyzer.run_full_analysis()

# Доступ к данным
print(f"Всего сотрудников: {stats['total_employees']}")
print(f"Активных: {stats['active_employees']}")
print(f"Средние рабочие часы: {stats['avg_working_hours']:.2f}h")
```

#### Пример 2: Пошаговый анализ

```python
from employee_analytics import EmployeeAnalytics

analyzer = EmployeeAnalytics()

# Загрузка данных
analyzer.load_data()

# Детекция аномалий
analyzer.detect_anomalies()

# Анализ паттернов
analyzer.analyze_patterns()

# Статистика
stats = analyzer.calculate_statistics()

# Экспорт
analyzer.export_to_excel()
```

#### Пример 3: Использование с визуализацией

```python
from employee_analytics import EmployeeAnalytics
from visualizations import AttendanceVisualizer

# Анализ
analyzer = EmployeeAnalytics()
df, stats = analyzer.run_full_analysis()

# Визуализация
visualizer = AttendanceVisualizer()
visualizer.generate_all_visualizations(dataframe=df)
```

#### Пример 4: Выборочные визуализации

```python
from visualizations import AttendanceVisualizer

visualizer = AttendanceVisualizer()
visualizer.load_data()

# Генерация отдельных графиков
visualizer.plot_working_hours_distribution()
visualizer.plot_heatmap_activity()
visualizer.plot_gantt_timeline(max_employees=50)
```

## Конфигурация

Настройки находятся в `config/analysis_config.json`:

### Основные параметры:

```json
{
  "working_hours": {
    "standard_work_day_hours": 8,
    "lunch_break_minutes": 60
  },
  "anomaly_thresholds": {
    "min_work_hours": 4,      // Минимум для нормального дня
    "max_work_hours": 12,     // Максимум для нормального дня
    "late_arrival_time": "10:00"
  }
}
```

### Настройка порогов аномалий:

- `min_work_hours`: Минимальная продолжительность рабочего дня (по умолчанию 4ч)
- `max_work_hours`: Максимальная продолжительность без переработки (по умолчанию 12ч)
- `late_arrival_time`: Время, после которого приход считается опозданием

## Интерпретация результатов

### Категории риска:

- **Normal**: Нет аномалий, стандартная посещаемость
- **Medium Risk**: 1-2 аномалии (например, одно опоздание)
- **High Risk**: 3+ аномалий (требует внимания)
- **Inactive**: Нет записей активности

### Типы аномалий:

1. **Short Day** (<4 часов): Слишком короткий рабочий день
2. **Long Day** (>12 часов): Переработка
3. **Late Arrival**: Приход после 10:00
4. **Early Departure**: Уход до 15:00
5. **Late Departure**: Уход после 20:00
6. **Missing Checkout**: Есть вход, но нет выхода

### Категории времени прихода:

- **Very Early Bird** (до 7:00)
- **Early Bird** (7:00-9:00)
- **On Time** (9:00-10:00)
- **Late Arrival** (после 10:00)

## Выходные файлы

### Excel отчет (в `output/reports/`)

Содержит листы:
1. **Full Data**: Все данные с вычисленными колонками
2. **Active Employees**: Только активные сотрудники
3. **Anomalies**: Сотрудники с аномалиями
4. **Statistics**: Сводная статистика
5. **Inactive Employees**: Неактивные сотрудники
6. **Patterns Summary**: Распределение по паттернам

### Визуализации (в `output/charts/`)

1. `working_hours_distribution_*.png` - Распределение рабочих часов
2. `activity_heatmap_*.png` - Тепловая карта по часам
3. `timeline_gantt_*.png` - Временная шкала присутствия
4. `arrival_departure_scatter_*.png` - Scatter график прихода/ухода
5. `status_distribution_*.png` - Pie charts статусов
6. `anomalies_summary_*.png` - Сводка аномалий
7. `records_analysis_*.png` - Анализ количества записей
8. `comprehensive_dashboard_*.png` - Полный дашборд

### Текстовый отчет (в `output/summaries/`)

Содержит:
- Обзор (общее количество, активные/неактивные)
- Статистика рабочих часов
- Паттерны прихода/ухода
- Выявленные аномалии
- Оценка рисков
- Топ-10 сотрудников с аномалиями

## Расширенные возможности

### Анализ конкретного файла

```python
analyzer = EmployeeAnalytics()
analyzer.run_full_analysis(json_file='/path/to/custom_file.json')
```

### Изменение настроек программно

```python
analyzer = EmployeeAnalytics()
analyzer.config['anomaly_thresholds']['min_work_hours'] = 3
analyzer.run_full_analysis()
```

### Фильтрация данных

```python
# Только сотрудники с аномалиями
anomalies_df = analyzer.df[analyzer.df['Total_Anomalies'] > 0]

# Высокий риск
high_risk = analyzer.df[analyzer.df['Risk_Category'] == 'High Risk']

# Переработки
overtime = analyzer.df[analyzer.df['Working_Hours'] > 10]
```

## Troubleshooting

### Проблема: ModuleNotFoundError

```bash
pip install -r requirements.txt
```

### Проблема: FileNotFoundError для JSON

Убедитесь, что путь к JSON файлу правильный в `config/analysis_config.json`:

```json
"data_source": {
  "json_file": "../Voice Log Discord/crm_export_2025-11-18.json"
}
```

### Проблема: Графики не сохраняются

Проверьте права на запись в папку `output/charts/`:

```bash
chmod -R 755 output/
```

## Примеры использования

### 1. Еженедельный отчет

```python
from employee_analytics import EmployeeAnalytics
from visualizations import AttendanceVisualizer
from datetime import datetime

# Анализ
analyzer = EmployeeAnalytics()
df, stats = analyzer.run_full_analysis()

# Визуализация
visualizer = AttendanceVisualizer()
visualizer.generate_all_visualizations(dataframe=df)

print(f"Отчет за {datetime.now().strftime('%Y-%m-%d')} готов!")
```

### 2. Поиск проблемных сотрудников

```python
analyzer = EmployeeAnalytics()
df, stats = analyzer.run_full_analysis()

# Высокий риск
high_risk = df[df['Risk_Category'] == 'High Risk']
print(f"Сотрудники высокого риска: {len(high_risk)}")
print(high_risk[['Employee ID', 'Total_Anomalies', 'Working_Hours']])
```

### 3. Анализ переработок

```python
analyzer = EmployeeAnalytics()
df, stats = analyzer.run_full_analysis()

overtime = df[df['Working_Hours'] > 10]
print(f"Переработки: {len(overtime)} сотрудников")
print(f"Средняя переработка: {overtime['Working_Hours'].mean():.2f}h")
```

## Дополнительная информация

- Все времена обрабатываются с учетом перерывов (по умолчанию 30 минут)
- Стандартный рабочий день: 8 часов
- Графики сохраняются в высоком разрешении (300 DPI)
- Excel файлы поддерживают кириллицу

## Лицензия

Internal use only

## Автор

Created with Claude Code (Anthropic)
