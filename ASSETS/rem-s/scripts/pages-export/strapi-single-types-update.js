const axios = require('axios');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');
const { promisify } = require('util');

const execAsync = promisify(exec);

// Configuration
const STRAPI_URL = 'https://strapi.rem-s.com';
const LOCALES = ['en', 'uk', 'pl', 'ru']; // Всі локалі окрім slovak
const UPDATED_DIR = path.join(__dirname, '..', '..', 'updated', 'pages');
const LOG_DIR = path.join(__dirname, 'logs');
const EXPORT_SCRIPT = path.join(__dirname, 'strapi-single-types-export.js');

// Single types для оновлення
const SINGLE_TYPES = [
  { name: 'About', endpoint: 'about-us' },
  { name: 'Contact', endpoint: 'contact' },
  { name: 'Footer', endpoint: 'footer' },
  { name: 'Header', endpoint: 'header' },
  { name: 'Home', endpoint: 'home-page' },
  { name: 'NotFound', endpoint: 'not-found' },
  { name: 'ThankYou', endpoint: 'thank-you' },
  { name: 'VacancyPage', endpoint: 'vacancy-page' },
  { name: 'VacancyListData', endpoint: 'vacancy-list-data' },
  { name: 'VideoInterview', endpoint: 'videointerview' }
];

// Ensure directories exist
if (!fs.existsSync(LOG_DIR)) {
  fs.mkdirSync(LOG_DIR, { recursive: true });
}

// Log file
const logFile = path.join(LOG_DIR, `update-${new Date().toISOString().replace(/[:.]/g, '-')}.log`);

/**
 * Логування дій
 * @param {string} message - Повідомлення
 * @param {string} level - Рівень (info, success, error, warning)
 */
function logAction(message, level = 'info') {
  const timestamp = new Date().toISOString();
  const logMessage = `[${timestamp}] ${message}\n`;
  
  // Запис у файл
  fs.appendFileSync(logFile, logMessage, 'utf8');
  
  // Вивід у консоль з кольорами
  const colors = {
    info: '\x1b[36m',    // Cyan
    success: '\x1b[32m', // Green
    error: '\x1b[31m',   // Red
    warning: '\x1b[33m',  // Yellow
    reset: '\x1b[0m'
  };
  
  const color = colors[level] || colors.info;
  console.log(`${color}${message}${colors.reset}`);
}

/**
 * Сканування папки updated/pages/ для знаходження файлів для оновлення
 * Читає всі JSON файли з updated/pages/{Entity}/{locale}.json
 * Зараз обробляє тільки About entity
 * @returns {Array} Масив об'єктів { entity, locale, filePath }
 */
function scanUpdatedFiles() {
  const filesToUpdate = [];
  
  if (!fs.existsSync(UPDATED_DIR)) {
    logAction(`⚠️  Папка ${UPDATED_DIR} не існує`, 'warning');
    return filesToUpdate;
  }
  
  // Фільтруємо тільки About entity
  const aboutType = SINGLE_TYPES.find(type => type.name === 'About');
  
  if (!aboutType) {
    logAction('⚠️  About entity не знайдено в конфігурації', 'warning');
    return filesToUpdate;
  }
  
  const entityDir = path.join(UPDATED_DIR, aboutType.name);
  
  if (!fs.existsSync(entityDir)) {
    logAction(`⚠️  Папка ${entityDir} не існує`, 'warning');
    return filesToUpdate;
  }
  
  // Перевіряємо файли для кожної локалі тільки для About
  LOCALES.forEach(locale => {
    const filePath = path.join(entityDir, `${locale}.json`);
    
    if (fs.existsSync(filePath)) {
      filesToUpdate.push({
        entity: aboutType.name,
        endpoint: aboutType.endpoint,
        locale: locale,
        filePath: filePath
      });
    }
  });
  
  return filesToUpdate;
}

/**
 * Очищення даних від системних полів, які не можна оновлювати
 * @param {Object} data - Дані з JSON файлу
 * @returns {Object} Очищені дані
 */
function cleanDataForUpdate(data) {
  const cleaned = { ...data };
  
  // Видаляємо системні поля Strapi, які не можна оновлювати
  delete cleaned.createdAt;
  delete cleaned.updatedAt;
  delete cleaned.publishedAt;
  delete cleaned.locale; // locale передається через query параметр
  delete cleaned.id;
  
  return cleaned;
}

/**
 * Валідація JSON файлу
 * @param {string} filePath - Шлях до файлу
 * @returns {Object} { valid: boolean, data: Object, error: string }
 */
function validateFile(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf8');
    const data = JSON.parse(content);
    
    // Базова перевірка - це об'єкт
    if (typeof data !== 'object' || data === null || Array.isArray(data)) {
      return {
        valid: false,
        data: null,
        error: 'Файл має містити JSON об\'єкт'
      };
    }
    
    // Перевірка наявності хоча б одного поля
    if (Object.keys(data).length === 0) {
      return {
        valid: false,
        data: null,
        error: 'Файл порожній'
      };
    }
    
    // Очищаємо дані від системних полів
    const cleanedData = cleanDataForUpdate(data);
    
    // Перевірка що після очищення залишилися дані
    if (Object.keys(cleanedData).length === 0) {
      return {
        valid: false,
        data: null,
        error: 'Після очищення системних полів файл порожній'
      };
    }
    
    return {
      valid: true,
      data: cleanedData,
      error: null
    };
  } catch (error) {
    return {
      valid: false,
      data: null,
      error: `Помилка парсингу JSON: ${error.message}`
    };
  }
}

/**
 * Створення backup поточного стану (експорт перед оновленням)
 * @param {string} token - API токен
 * @returns {Promise<boolean>}
 */
async function createBackup(token) {
  logAction('📦 Створення backup перед оновленням...', 'info');
  
  try {
    const { stdout, stderr } = await execAsync(`node "${EXPORT_SCRIPT}" "${token}"`);
    
    if (stderr && !stderr.includes('warning')) {
      logAction(`⚠️  Backup warning: ${stderr}`, 'warning');
    }
    
    logAction('✅ Backup створено успішно', 'success');
    return true;
  } catch (error) {
    logAction(`❌ Помилка створення backup: ${error.message}`, 'error');
    return false;
  }
}

/**
 * Оновлення single type через Strapi API
 * @param {string} endpoint - API endpoint
 * @param {string} locale - Локаль
 * @param {Object} data - Дані для оновлення
 * @param {string} token - API токен
 * @param {boolean} dryRun - Режим dry-run
 * @returns {Promise<Object>} { success: boolean, message: string }
 */
async function updateSingleType(endpoint, locale, data, token, dryRun = false) {
  if (dryRun) {
    logAction(`🔍 [DRY-RUN] Оновлення ${endpoint} (${locale})`, 'info');
    return { success: true, message: 'Dry-run mode - зміни не застосовано' };
  }
  
  // Спочатку отримуємо поточні дані, щоб перевірити структуру та можливо отримати ID
  let currentData = null;
  try {
    const getResponse = await axios.get(`${STRAPI_URL}/api/${endpoint}`, {
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      params: {
        'populate': '*',
        'locale': locale
      }
    });
    currentData = getResponse.data;
  } catch (getError) {
    // Якщо не вдалося отримати дані, продовжуємо без них
    if (getError.response && getError.response.status !== 404) {
      // Логуємо тільки якщо це не 404 (не знайдено)
    }
  }
  
  // Спробуємо різні формати URL для Strapi
  const urlFormats = [
    `${STRAPI_URL}/api/${endpoint}`,                    // Стандартний формат
    `${STRAPI_URL}/api/single-types/${endpoint}`       // Альтернативний формат для single types
  ];
  
  // Базовий конфіг
  const baseRequestConfig = {
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    params: {
      'locale': locale
    }
  };
  
  // Різні варіанти конфігів
  const requestConfigs = [
    baseRequestConfig,  // Базовий
    { ...baseRequestConfig, params: { ...baseRequestConfig.params, 'publicationState': 'live' } },
    { ...baseRequestConfig, params: { ...baseRequestConfig.params, 'publicationState': 'preview' } }
  ];
  
  // Спробуємо різні формати body (завжди з обгорткою data)
  const bodyFormats = [];
  
  // Стандартний формат
  bodyFormats.push({ data: data });
  
  // З published state (якщо потрібно опублікувати)
  bodyFormats.push({ 
    data: {
      ...data,
      publishedAt: new Date().toISOString() // Встановлюємо publishedAt
    }
  });
  
  // З поточними даними + нові (якщо є поточні дані)
  if (currentData && currentData.data) {
    bodyFormats.push({ 
      data: { 
        ...currentData.data, 
        ...data 
      } 
    });
  }
  
  // Спробуємо різні методи HTTP в порядку пріоритету
  const methods = [
    { method: 'PUT', name: 'PUT' },
    { method: 'PATCH', name: 'PATCH' },
    { method: 'POST', name: 'POST' }
  ];
  
  // Пробуємо кожну комбінацію URL + config + метод + body формат
  let lastError = null;
  
  for (let urlIndex = 0; urlIndex < urlFormats.length; urlIndex++) {
    const url = urlFormats[urlIndex];
    const isLastUrl = urlIndex === urlFormats.length - 1;
    
    for (let configIndex = 0; configIndex < requestConfigs.length; configIndex++) {
      const requestConfig = requestConfigs[configIndex];
      const isLastConfig = configIndex === requestConfigs.length - 1;
      
      for (let bodyIndex = 0; bodyIndex < bodyFormats.length; bodyIndex++) {
        const requestBody = bodyFormats[bodyIndex];
        const isLastBody = bodyIndex === bodyFormats.length - 1;
        
        for (let methodIndex = 0; methodIndex < methods.length; methodIndex++) {
          const { method, name } = methods[methodIndex];
          const isLastMethod = methodIndex === methods.length - 1;
          const isLastAttempt = isLastUrl && isLastConfig && isLastBody && isLastMethod;
          
          try {
            let response;
            
            if (method === 'PUT') {
              response = await axios.put(url, requestBody, requestConfig);
            } else if (method === 'PATCH') {
              response = await axios.patch(url, requestBody, requestConfig);
            } else if (method === 'POST') {
              response = await axios.post(url, requestBody, requestConfig);
            }
            
            return {
              success: true,
              message: `Оновлено успішно (через ${name}, URL: ${url.includes('single-types') ? 'single-types' : 'standard'})`,
              response: response.data
            };
          } catch (error) {
            lastError = error;
            
            if (error.response) {
              const status = error.response.status;
              
              // Якщо помилка 400, 405 або 500, пробуємо наступну комбінацію
              // 400 може означати неправильний формат body, тому пробуємо інші варіанти
              if (status === 400 || status === 405 || status === 500) {
                // Якщо це остання спроба, повертаємо помилку
                if (isLastAttempt) {
                  const errorData = error.response.data?.error || error.response.data;
                  
                  let errorMessage = `API Error (${status})`;
                  if (errorData) {
                    if (typeof errorData === 'object') {
                      errorMessage += `: ${JSON.stringify(errorData)}`;
                    } else {
                      errorMessage += `: ${errorData}`;
                    }
                  }
                  
                  if (status === 405) {
                    errorMessage += ` | Всі методи (PUT, PATCH, POST), формати URL та body не підтримуються для ${endpoint}. Можливо, цей single type не можна оновлювати через API або потрібні інші права доступу.`;
                  } else if (status === 500) {
                    errorMessage += ` | Можливі причини: неправильна структура даних, відсутні обов'язкові поля, або помилка на сервері Strapi`;
                  }
                  
                  return {
                    success: false,
                    message: errorMessage,
                    status: status,
                    errorDetails: errorData
                  };
                }
                // Інакше продовжуємо спробувати наступну комбінацію
                continue;
              }
              
              // Для інших помилок (не 405/500) повертаємо одразу
              const errorData = error.response.data?.error || error.response.data;
              
              let errorMessage = `API Error (${status})`;
              if (errorData) {
                if (typeof errorData === 'object') {
                  errorMessage += `: ${JSON.stringify(errorData)}`;
                } else {
                  errorMessage += `: ${errorData}`;
                }
              }
              
              return {
                success: false,
                message: errorMessage,
                status: status,
                errorDetails: errorData
              };
            } else {
              // Network error - пробуємо наступну спробу, якщо не остання
              if (isLastAttempt) {
                return {
                  success: false,
                  message: `Network Error: ${error.message}`
                };
              }
              continue;
            }
          }
        }
      }
    }
  }
  
  // Fallback (не повинно дійти сюди)
  return {
    success: false,
    message: 'Всі комбінації URL, config, body та методів HTTP не спрацювали'
  };
}

/**
 * Запуск експорту після оновлення
 * @param {string} token - API токен
 * @returns {Promise<boolean>}
 */
async function runExport(token) {
  logAction('📥 Запуск експорту після оновлення...', 'info');
  
  try {
    const { stdout, stderr } = await execAsync(`node "${EXPORT_SCRIPT}" "${token}"`);
    
    if (stderr && !stderr.includes('warning')) {
      logAction(`⚠️  Export warning: ${stderr}`, 'warning');
    }
    
    logAction('✅ Експорт завершено успішно', 'success');
    return true;
  } catch (error) {
    logAction(`❌ Помилка експорту: ${error.message}`, 'error');
    return false;
  }
}

/**
 * Головна функція оновлення
 */
async function updateSingleTypes() {
  const args = process.argv.slice(2);
  const isDryRun = args.includes('--dry-run');
  const needsConfirm = args.includes('--confirm');
  const createBackupFlag = args.includes('--backup');
  const exportAfter = args.includes('--export-after');
  
  // Отримуємо токен
  const tokenIndex = args.findIndex(arg => !arg.startsWith('--'));
  const token = tokenIndex !== -1 ? args[tokenIndex] : process.env.STRAPI_TOKEN;
  
  if (!token && !isDryRun) {
    logAction('❌ Помилка: Потрібен Strapi API токен!', 'error');
    logAction('\nВикористання:', 'info');
    logAction('  node strapi-single-types-update.js --dry-run', 'info');
    logAction('  node strapi-single-types-update.js --confirm <token>', 'info');
    logAction('  node strapi-single-types-update.js --confirm --backup --export-after <token>', 'info');
    process.exit(1);
  }
  
  logAction('🚀 Початок оновлення single types з Strapi\n', 'info');
  logAction(`📍 Strapi URL: ${STRAPI_URL}`, 'info');
  logAction(`📁 Source directory: ${UPDATED_DIR}`, 'info');
  logAction(`📋 Log file: ${logFile}`, 'info');
  
  if (isDryRun) {
    logAction('🔍 Режим DRY-RUN - зміни не будуть застосовані\n', 'warning');
  } else if (!needsConfirm) {
    logAction('⚠️  УВАГА: Режим оновлення вимкнено. Використайте --confirm для реальних змін\n', 'warning');
    logAction('🔍 Запускаю dry-run режим...\n', 'info');
  }
  
  // Скануємо файли для оновлення
  const filesToUpdate = scanUpdatedFiles();
  
  if (filesToUpdate.length === 0) {
    logAction('ℹ️  Файлів для оновлення не знайдено', 'info');
    logAction(`   Перевірте папку: ${UPDATED_DIR}`, 'info');
    return;
  }
  
  logAction(`\n📦 Знайдено ${filesToUpdate.length} файлів для оновлення:\n`, 'info');
  filesToUpdate.forEach((file, index) => {
    logAction(`   ${index + 1}. ${file.entity}/${file.locale}.json`, 'info');
  });
  logAction('');
  
  // Підтвердження для реальних змін
  if (!isDryRun && needsConfirm) {
    logAction('⚠️  УВАГА: Буде виконано реальне оновлення в Strapi!', 'warning');
    logAction('   Натисніть Ctrl+C для скасування або зачекайте 5 секунд...\n', 'warning');
    
    await new Promise(resolve => setTimeout(resolve, 5000));
  }
  
  // Створення backup перед оновленням
  if (createBackupFlag && !isDryRun && token) {
    const backupSuccess = await createBackup(token);
    if (!backupSuccess) {
      logAction('⚠️  Backup не створено, але продовжуємо оновлення...', 'warning');
    }
  }
  
  // Статистика
  let successCount = 0;
  let errorCount = 0;
  const errors = [];
  
  // Оновлюємо кожен файл
  logAction('\n📝 Початок оновлення файлів...\n', 'info');
  
  for (let i = 0; i < filesToUpdate.length; i++) {
    const file = filesToUpdate[i];
    
    logAction(`[${i + 1}/${filesToUpdate.length}] Оновлення ${file.entity}/${file.locale}.json...`, 'info');
    
    // Валідація файлу
    const validation = validateFile(file.filePath);
    
    if (!validation.valid) {
      logAction(`   ❌ Помилка валідації: ${validation.error}`, 'error');
      errorCount++;
      errors.push({
        file: `${file.entity}/${file.locale}.json`,
        error: validation.error
      });
      continue;
    }
    
    // Оновлення через API
    const result = await updateSingleType(
      file.endpoint,
      file.locale,
      validation.data,
      token,
      isDryRun || !needsConfirm
    );
    
    if (result.success) {
      logAction(`   ✅ ${result.message}`, 'success');
      successCount++;
    } else {
      logAction(`   ❌ ${result.message}`, 'error');
      errorCount++;
      errors.push({
        file: `${file.entity}/${file.locale}.json`,
        error: result.message
      });
    }
    
    // Rate limiting - затримка між запитами
    if (i < filesToUpdate.length - 1) {
      await new Promise(resolve => setTimeout(resolve, 500));
    }
  }
  
  // Підсумок
  logAction('\n✅ Оновлення завершено!\n', 'success');
  logAction('📊 Підсумок:', 'info');
  logAction(`   Успішно оновлено: ${successCount}`, 'success');
  logAction(`   Помилки: ${errorCount}`, errorCount > 0 ? 'error' : 'info');
  logAction(`   Log file: ${logFile}`, 'info');
  
  if (errors.length > 0) {
    logAction('\n❌ Помилки:', 'error');
    errors.forEach(err => {
      logAction(`   - ${err.file}: ${err.error}`, 'error');
    });
  }
  
  // Запуск експорту після оновлення
  if (exportAfter && !isDryRun && token && successCount > 0) {
    logAction('\n', 'info');
    await runExport(token);
  }
  
  logAction('\n', 'info');
}

// Запускаємо оновлення
updateSingleTypes().catch(error => {
  logAction(`\n❌ Критична помилка: ${error.message}`, 'error');
  logAction(error.stack, 'error');
  process.exit(1);
});