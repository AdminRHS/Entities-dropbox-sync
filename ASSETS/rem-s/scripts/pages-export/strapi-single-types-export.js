const axios = require('axios');
const fs = require('fs');
const path = require('path');

// Configuration
const STRAPI_URL = 'https://strapi.rem-s.com';
const LOCALES = ['en', 'uk', 'pl', 'ru']; // Всі локалі окрім slovak
const UPDATED_DIR = path.join(__dirname, '..', '..', 'updated', 'pages');
const EXPORT_DIR = path.join(__dirname, '..', '..', 'exported', 'pages');
const STATUS_TRACKER_PATH = path.join(__dirname, 'status-tracker.json');

// Single types для експорту
const SINGLE_TYPES = [
  { name: 'About', endpoint: 'about-us' },
  { name: 'Contact', endpoint: 'contact' },
  { name: 'Header', endpoint: 'header' },
  { name: 'Home', endpoint: 'home-page' },
  { name: 'NotFound', endpoint: 'not-found' },
  { name: 'ThankYou', endpoint: 'thank-you' },
  { name: 'VacancyPage', endpoint: 'vacancy-page' },
  { name: 'VacancyListData', endpoint: 'vacancy-list-data' },
  { name: 'VideoInterview', endpoint: 'videointerview' }
];

// Ensure directories exist
if (!fs.existsSync(UPDATED_DIR)) {
  fs.mkdirSync(UPDATED_DIR, { recursive: true });
}
if (!fs.existsSync(EXPORT_DIR)) {
  fs.mkdirSync(EXPORT_DIR, { recursive: true });
}

/**
 * Завантажити трекер статусів або створити новий
 * @returns {Object} Трекер статусів
 */
function loadStatusTracker() {
  if (fs.existsSync(STATUS_TRACKER_PATH)) {
    try {
      const content = fs.readFileSync(STATUS_TRACKER_PATH, 'utf8');
      return JSON.parse(content);
    } catch (error) {
      console.warn('⚠️  Помилка читання трекера, створюю новий');
    }
  }
  
  // Створюємо новий трекер
  const tracker = {};
  SINGLE_TYPES.forEach(type => {
    tracker[type.name] = {};
    LOCALES.forEach(locale => {
      tracker[type.name][locale] = 'pending';
    });
  });
  return tracker;
}

/**
 * Зберегти трекер статусів
 * @param {Object} tracker - Трекер статусів
 */
function saveStatusTracker(tracker) {
  fs.writeFileSync(STATUS_TRACKER_PATH, JSON.stringify(tracker, null, 2), 'utf8');
}

/**
 * Очистити дані від структури Strapi (data.attributes)
 * @param {Object} data - Дані з Strapi
 * @returns {Object} Плаский об'єкт з текстовими полями
 */
function cleanAttributes(data) {
  if (!data || !data.data || !data.data.attributes) {
    console.warn('⚠️  Неочікувана структура даних');
    return data;
  }
  
  // Повертаємо тільки attributes (плаский об'єкт)
  return data.data.attributes;
}

/**
 * Отримати дані single type з Strapi
 * @param {string} endpoint - API endpoint
 * @param {string} locale - Локаль
 * @param {string} token - API токен
 * @returns {Object} Дані з Strapi
 */
async function fetchSingleType(endpoint, locale, token) {
  try {
    const response = await axios.get(`${STRAPI_URL}/api/${endpoint}`, {
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      params: {
        'populate': '*',
        'locale': locale
      }
    });
    
    return response.data;
  } catch (error) {
    if (error.response) {
      console.error(`❌ API Error (${endpoint}, ${locale}):`, error.response.status, error.response.data?.error?.message || error.response.data);
    } else {
      console.error(`❌ Network Error (${endpoint}, ${locale}):`, error.message);
    }
    throw error;
  }
}

/**
 * Копіювати файли з updated/pages в exported/pages
 * @param {string} sourceDir - Вихідна директорія (updated/pages)
 * @param {string} targetDir - Цільова директорія (exported/pages)
 */
function copyFilesToExported(sourceDir, targetDir) {
  if (!fs.existsSync(sourceDir)) {
    console.warn(`⚠️  Вихідна директорія не існує: ${sourceDir}`);
    return;
  }
  
  // Створюємо цільову директорію якщо не існує
  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }
  
  // Проходимо по всіх сутностях
  SINGLE_TYPES.forEach(type => {
    const sourceTypeDir = path.join(sourceDir, type.name);
    const targetTypeDir = path.join(targetDir, type.name);
    
    if (!fs.existsSync(sourceTypeDir)) {
      return; // Пропускаємо якщо папка не існує
    }
    
    // Створюємо цільову папку для типу
    if (!fs.existsSync(targetTypeDir)) {
      fs.mkdirSync(targetTypeDir, { recursive: true });
    }
    
    // Копіюємо файли для кожної локалі
    LOCALES.forEach(locale => {
      const sourceFile = path.join(sourceTypeDir, `${locale}.json`);
      const targetFile = path.join(targetTypeDir, `${locale}.json`);
      
      if (fs.existsSync(sourceFile)) {
        try {
          fs.copyFileSync(sourceFile, targetFile);
          console.log(`   📋 Скопійовано: ${type.name}/${locale}.json`);
        } catch (error) {
          console.error(`   ❌ Помилка копіювання ${type.name}/${locale}.json: ${error.message}`);
        }
      }
    });
  });
}

/**
 * Експортувати single type для всіх локалей
 * @param {Object} type - Конфігурація типу
 * @param {string} token - API токен
 * @param {Object} tracker - Трекер статусів
 */
async function exportSingleType(type, token, tracker) {
  console.log(`\n📄 Експорт: ${type.name}`);
  console.log(`   Endpoint: ${type.endpoint}`);
  
  // Створюємо папку для типу в updated/pages
  const typeDir = path.join(UPDATED_DIR, type.name);
  if (!fs.existsSync(typeDir)) {
    fs.mkdirSync(typeDir, { recursive: true });
  }
  
  for (const locale of LOCALES) {
    try {
      console.log(`   [${locale}] Завантаження...`);
      
      // Отримуємо дані
      const data = await fetchSingleType(type.endpoint, locale, token);
      
      // Очищаємо від data.attributes
      const cleanData = cleanAttributes(data);
      
      // Зберігаємо JSON в updated/pages
      const jsonPath = path.join(typeDir, `${locale}.json`);
      fs.writeFileSync(jsonPath, JSON.stringify(cleanData, null, 2), 'utf8');
      
      // Оновлюємо трекер
      tracker[type.name][locale] = 'exported';
      
      console.log(`   [${locale}] ✅ Збережено: ${jsonPath}`);
      
      // Невелика затримка щоб не перевантажити API
      await new Promise(resolve => setTimeout(resolve, 200));
      
    } catch (error) {
      console.error(`   [${locale}] ❌ Помилка експорту`);
      tracker[type.name][locale] = 'error';
      
      // Продовжуємо з наступною локаллю
      continue;
    }
  }
}

/**
 * Головна функція експорту
 */
async function exportSingleTypes() {
  const isTest = process.argv.includes('--test') || process.argv.includes('-t');
  
  if (isTest) {
    console.log('🧪 Тестовий режим\n');
    console.log(`📍 Strapi URL: ${STRAPI_URL}`);
    console.log(`📁 Updated directory: ${UPDATED_DIR}`);
    console.log(`📁 Export directory: ${EXPORT_DIR}`);
    console.log(`📋 Status tracker: ${STATUS_TRACKER_PATH}`);
    console.log(`\n📦 Single types для експорту:`);
    SINGLE_TYPES.forEach(type => {
      console.log(`   - ${type.name} (${type.endpoint})`);
    });
    console.log(`\n🌍 Локалі: ${LOCALES.join(', ')}`);
    console.log(`\n📁 Перевірка директорій...`);
    console.log(`   Updated dir exists: ${fs.existsSync(UPDATED_DIR)}`);
    console.log(`   Export dir exists: ${fs.existsSync(EXPORT_DIR)}`);
    if (!fs.existsSync(UPDATED_DIR)) {
      console.log('   Створюю updated директорію...');
      fs.mkdirSync(UPDATED_DIR, { recursive: true });
      console.log('   ✅ Директорія створена');
    }
    if (!fs.existsSync(EXPORT_DIR)) {
      console.log('   Створюю exported директорію...');
      fs.mkdirSync(EXPORT_DIR, { recursive: true });
      console.log('   ✅ Директорія створена');
    }
    return;
  }

  console.log('🚀 Початок експорту single types з Strapi\n');
  console.log(`📍 Strapi URL: ${STRAPI_URL}`);
  console.log(`📁 Updated directory: ${UPDATED_DIR}`);
  console.log(`📁 Export directory: ${EXPORT_DIR}`);
  console.log(`🌍 Локалі: ${LOCALES.join(', ')}`);
  console.log(`📦 Single types: ${SINGLE_TYPES.length}\n`);

  // Отримуємо токен з environment або command line
  const token = process.env.STRAPI_TOKEN || process.argv[2];
  
  if (!token) {
    console.error('❌ Помилка: Потрібен Strapi API токен!');
    console.error('\nВикористання:');
    console.error('  node strapi-single-types-export.js <token>');
    console.error('  node strapi-single-types-export.js --test  (тестовий режим)');
    console.error('  або встановіть змінну STRAPI_TOKEN');
    console.error('\nПриклад:');
    console.error('  node strapi-single-types-export.js your_token_here');
    console.error('  STRAPI_TOKEN=your_token_here node strapi-single-types-export.js');
    process.exit(1);
  }

  // Завантажуємо трекер статусів
  const tracker = loadStatusTracker();
  console.log('📋 Трекер статусів завантажено\n');

  try {
    // Експортуємо кожен single type
    for (const type of SINGLE_TYPES) {
      await exportSingleType(type, token, tracker);
      
      // Зберігаємо трекер після кожного типу
      saveStatusTracker(tracker);
    }

    // Копіюємо файли з updated/pages в exported/pages
    console.log('\n📋 Копіювання файлів з updated/pages в exported/pages...\n');
    copyFilesToExported(UPDATED_DIR, EXPORT_DIR);
    
    // Підсумок
    console.log('\n✅ Експорт завершено!\n');
    console.log('📊 Підсумок:');
    
    let exportedCount = 0;
    let errorCount = 0;
    let pendingCount = 0;
    
    SINGLE_TYPES.forEach(type => {
      LOCALES.forEach(locale => {
        const status = tracker[type.name][locale];
        if (status === 'exported') exportedCount++;
        else if (status === 'error') errorCount++;
        else pendingCount++;
      });
    });
    
    console.log(`   Успішно експортовано: ${exportedCount}`);
    console.log(`   Помилки: ${errorCount}`);
    console.log(`   В очікуванні: ${pendingCount}`);
    console.log(`   Updated directory: ${UPDATED_DIR}`);
    console.log(`   Export directory: ${EXPORT_DIR}`);
    console.log(`   Status tracker: ${STATUS_TRACKER_PATH}\n`);

  } catch (error) {
    console.error('\n❌ Експорт не вдався:', error.message);
    if (error.response) {
      console.error('   Status:', error.response.status);
      console.error('   Data:', JSON.stringify(error.response.data, null, 2));
    }
    process.exit(1);
  }
}

// Запускаємо експорт
exportSingleTypes();

