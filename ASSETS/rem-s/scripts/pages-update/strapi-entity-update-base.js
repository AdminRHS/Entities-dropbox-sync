const axios = require('axios');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');
const { promisify } = require('util');
const { updateSingleTypeWithRetry } = require('./strapi-api-retry');

const execAsync = promisify(exec);

// Configuration
const STRAPI_URL = 'https://strapi.rem-s.com';
const LOCALES = ['en', 'uk', 'pl', 'ru']; // Всі локалі окрім slovak
const UPDATED_DIR = path.join(__dirname, '..', '..', 'updated', 'pages');
const LOG_DIR = path.join(__dirname, 'logs');
const EXPORT_SCRIPT = path.join(__dirname, '..', 'pages-export', 'strapi-single-types-export.js');

// Ensure directories exist
if (!fs.existsSync(LOG_DIR)) {
  fs.mkdirSync(LOG_DIR, { recursive: true });
}

/**
 * Логування дій
 * @param {string} logFile - Шлях до файлу логів
 * @param {string} message - Повідомлення
 * @param {string} level - Рівень (info, success, error, warning)
 */
function logAction(logFile, message, level = 'info') {
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
 * Валідація токена через Strapi API
 * Перевіряє токен через спробу зробити GET запит до single type endpoint
 * (API токени не мають доступу до /api/users/me, тому використовуємо альтернативний спосіб)
 * @param {string} token - API токен
 * @param {string} logFile - Шлях до файлу логів
 * @returns {Promise<boolean>} true якщо токен валідний
 */
async function validateToken(token, logFile) {
  try {
    // Спробуємо зробити GET запит до about-us endpoint для перевірки токена
    const response = await axios.get(`${STRAPI_URL}/api/about-us`, {
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      params: {
        'locale': 'en'
      },
      // Не викидаємо помилку на 404 - це нормально, якщо запис не існує
      validateStatus: function (status) {
        return status < 500; // Приймаємо всі статуси окрім 5xx
      }
    });
    
    // Якщо отримали 401 - токен невалідний
    if (response.status === 401) {
      logAction(logFile, `❌ Токен невалідний: 401 Unauthorized`, 'error');
      return false;
    }
    
    // Якщо отримали 403 - токен не має прав доступу
    if (response.status === 403) {
      logAction(logFile, `⚠️  Токен не має прав доступу: 403 Forbidden`, 'warning');
      logAction(logFile, `   Продовжуємо, але можуть виникнути помилки при оновленні`, 'warning');
      return true; // Все одно продовжуємо, можливо права достатні для оновлення
    }
    
    // Якщо отримали 200, 404 або інший успішний статус - токен валідний
    logAction(logFile, `✅ Токен валідний (статус: ${response.status})`, 'success');
    return true;
  } catch (error) {
    if (error.response) {
      const status = error.response.status;
      if (status === 401) {
        logAction(logFile, `❌ Токен невалідний: 401 Unauthorized`, 'error');
      } else if (status === 403) {
        logAction(logFile, `⚠️  Токен не має прав доступу: 403 Forbidden`, 'warning');
        logAction(logFile, `   Продовжуємо, але можуть виникнути помилки при оновленні`, 'warning');
        return true; // Все одно продовжуємо
      } else {
        logAction(logFile, `⚠️  Помилка перевірки токена: ${status} ${error.response.statusText}`, 'warning');
        logAction(logFile, `   Продовжуємо виконання...`, 'warning');
        return true; // Продовжуємо, можливо це тимчасова помилка
      }
    } else {
      logAction(logFile, `⚠️  Network помилка при перевірці токена: ${error.message}`, 'warning');
      logAction(logFile, `   Продовжуємо виконання...`, 'warning');
      return true; // Продовжуємо, можливо це тимчасова мережева помилка
    }
    return false;
  }
}

/**
 * Сканування папки updated/pages/ для знаходження файлів для оновлення
 * @param {Object} entityType - { name: string, endpoint: string }
 * @param {string} logFile - Шлях до файлу логів
 * @returns {Array} Масив об'єктів { entity, locale, filePath }
 */
function scanUpdatedFiles(entityType, logFile) {
  const filesToUpdate = [];
  
  if (!fs.existsSync(UPDATED_DIR)) {
    logAction(logFile, `⚠️  Папка ${UPDATED_DIR} не існує`, 'warning');
    return filesToUpdate;
  }
  
  const entityDir = path.join(UPDATED_DIR, entityType.name);
  
  if (!fs.existsSync(entityDir)) {
    logAction(logFile, `⚠️  Папка ${entityDir} не існує`, 'warning');
    return filesToUpdate;
  }
  
  // Перевіряємо файли для кожної локалі
  LOCALES.forEach(locale => {
    const filePath = path.join(entityDir, `${locale}.json`);
    
    if (fs.existsSync(filePath)) {
      filesToUpdate.push({
        entity: entityType.name,
        endpoint: entityType.endpoint,
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
  // publishedAt не видаляємо - він може бути потрібен для публікації
  delete cleaned.locale; // locale передається через query параметр
  delete cleaned.id;
  
  // Видаляємо relation поля, які не можна оновлювати через API
  // localizations - це relation поле, яке автоматично синхронізується Strapi
  delete cleaned.localizations;
  
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
 * @param {string} logFile - Шлях до файлу логів
 * @returns {Promise<boolean>}
 */
async function createBackup(token, logFile) {
  logAction(logFile, '📦 Створення backup перед оновленням...', 'info');
  
  try {
    const { stdout, stderr } = await execAsync(`node "${EXPORT_SCRIPT}" "${token}"`);
    
    if (stderr && !stderr.includes('warning')) {
      logAction(logFile, `⚠️  Backup warning: ${stderr}`, 'warning');
    }
    
    logAction(logFile, '✅ Backup створено успішно', 'success');
    return true;
  } catch (error) {
    logAction(logFile, `❌ Помилка створення backup: ${error.message}`, 'error');
    return false;
  }
}

/**
 * Оновлення single type через Strapi API
 * @param {string} endpoint - API endpoint
 * @param {string} locale - Локаль
 * @param {Object} data - Дані для оновлення
 * @param {string} token - API токен
 * @param {string} logFile - Шлях до файлу логів
 * @param {boolean} dryRun - Режим dry-run
 * @returns {Promise<Object>} { success: boolean, message: string }
 */
async function updateSingleType(endpoint, locale, data, token, logFile, dryRun = false) {
  if (dryRun) {
    logAction(logFile, `🔍 [DRY-RUN] Оновлення ${endpoint} (${locale})`, 'info');
    return { success: true, message: 'Dry-run mode - зміни не застосовано' };
  }
  
  // Спочатку отримуємо поточні дані, щоб перевірити структуру та можливо отримати ID
  // Використовуємо publicationState: 'preview' щоб отримати і draft і published дані
  let currentData = null;
  try {
    const getResponse = await axios.get(`${STRAPI_URL}/api/${endpoint}`, {
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      params: {
        'populate': '*',
        'locale': locale,
        'publicationState': 'preview' // Отримуємо і draft і published дані
      }
    });
    currentData = getResponse.data;
  } catch (getError) {
    // Логуємо помилки GET (окрім 404 - це нормально, якщо запис не існує)
    if (getError.response) {
      const status = getError.response.status;
      if (status !== 404) {
        const errorData = getError.response.data?.error || getError.response.data;
        logAction(logFile, `⚠️  Помилка отримання поточних даних (${status}): ${errorData ? JSON.stringify(errorData).substring(0, 100) : 'Unknown error'}`, 'warning');
      }
    } else {
      logAction(logFile, `⚠️  Network помилка при отриманні поточних даних: ${getError.message}`, 'warning');
    }
    // Продовжуємо без поточних даних
  }
  
  // Створюємо обгортку для logAction, яка відповідає очікуваному формату
  const logActionWrapper = (message, level = 'info') => {
    logAction(logFile, message, level);
  };
  
  // Використовуємо винесену логіку спроб
  return await updateSingleTypeWithRetry(
    endpoint,
    locale,
    data,
    token,
    STRAPI_URL,
    currentData,
    logActionWrapper,
    12 // Максимум 12 спроб (2 URL × 2 config × 2 body × 2 methods = 8, але з запасом)
  );
}

/**
 * Запуск експорту після оновлення
 * @param {string} token - API токен
 * @param {string} logFile - Шлях до файлу логів
 * @returns {Promise<boolean>}
 */
async function runExport(token, logFile) {
  logAction(logFile, '📥 Запуск експорту після оновлення...', 'info');
  
  try {
    const { stdout, stderr } = await execAsync(`node "${EXPORT_SCRIPT}" "${token}"`);
    
    if (stderr && !stderr.includes('warning')) {
      logAction(logFile, `⚠️  Export warning: ${stderr}`, 'warning');
    }
    
    logAction(logFile, '✅ Експорт завершено успішно', 'success');
    return true;
  } catch (error) {
    logAction(logFile, `❌ Помилка експорту: ${error.message}`, 'error');
    return false;
  }
}

/**
 * Головна функція оновлення
 * @param {Object} entityType - { name: string, endpoint: string }
 * @param {string} scriptName - Назва скрипта для повідомлень
 */
async function updateEntity(entityType, scriptName) {
  const args = process.argv.slice(2);
  const isDryRun = args.includes('--dry-run');
  const needsConfirm = args.includes('--confirm');
  const createBackupFlag = args.includes('--backup');
  const exportAfter = args.includes('--export-after');
  const forceFlag = args.includes('--force');
  
  // Отримуємо токен
  const tokenIndex = args.findIndex(arg => !arg.startsWith('--'));
  const token = tokenIndex !== -1 ? args[tokenIndex] : process.env.STRAPI_TOKEN;
  
  // Log file
  const logFile = path.join(LOG_DIR, `update-${new Date().toISOString().replace(/[:.]/g, '-')}.log`);
  
  if (!token && !isDryRun) {
    logAction(logFile, '❌ Помилка: Потрібен Strapi API токен!', 'error');
    logAction(logFile, '\nВикористання:', 'info');
    logAction(logFile, `  node ${scriptName} --dry-run`, 'info');
    logAction(logFile, `  node ${scriptName} --confirm <token>`, 'info');
    logAction(logFile, `  node ${scriptName} --confirm --backup --export-after <token>`, 'info');
    logAction(logFile, `  node ${scriptName} --confirm --backup --force <token>`, 'info');
    process.exit(1);
  }
  
  logAction(logFile, `🚀 Початок оновлення ${entityType.name} з Strapi\n`, 'info');
  logAction(logFile, `📍 Strapi URL: ${STRAPI_URL}`, 'info');
  logAction(logFile, `📁 Source directory: ${UPDATED_DIR}`, 'info');
  logAction(logFile, `📋 Log file: ${logFile}`, 'info');
  
  if (isDryRun) {
    logAction(logFile, '🔍 Режим DRY-RUN - зміни не будуть застосовані\n', 'warning');
  } else if (!needsConfirm) {
    logAction(logFile, '⚠️  УВАГА: Режим оновлення вимкнено. Використайте --confirm для реальних змін\n', 'warning');
    logAction(logFile, '🔍 Запускаю dry-run режим...\n', 'info');
  }
  
  // Валідація токена (якщо не dry-run)
  if (!isDryRun && token) {
    logAction(logFile, '🔐 Перевірка токена...', 'info');
    const isValidToken = await validateToken(token, logFile);
    if (!isValidToken) {
      logAction(logFile, '❌ Токен невалідний. Перевірте токен та спробуйте знову.', 'error');
      process.exit(1);
    }
  }
  
  // Скануємо файли для оновлення
  const filesToUpdate = scanUpdatedFiles(entityType, logFile);
  
  if (filesToUpdate.length === 0) {
    logAction(logFile, 'ℹ️  Файлів для оновлення не знайдено', 'info');
    logAction(logFile, `   Перевірте папку: ${UPDATED_DIR}`, 'info');
    return;
  }
  
  logAction(logFile, `\n📦 Знайдено ${filesToUpdate.length} файлів для оновлення:\n`, 'info');
  filesToUpdate.forEach((file, index) => {
    logAction(logFile, `   ${index + 1}. ${file.entity}/${file.locale}.json`, 'info');
  });
  logAction(logFile, '', 'info');
  
  // Підтвердження для реальних змін
  if (!isDryRun && needsConfirm) {
    logAction(logFile, '⚠️  УВАГА: Буде виконано реальне оновлення в Strapi!', 'warning');
    logAction(logFile, '   Натисніть Ctrl+C для скасування або зачекайте 5 секунд...\n', 'warning');
    
    await new Promise(resolve => setTimeout(resolve, 5000));
  }
  
  // Створення backup перед оновленням
  // ⚠️  УВАГА: Backup експортує дані з Strapi і перезаписує файли!
  // Тому ваші локальні зміни можуть бути втрачені
  if (createBackupFlag && !isDryRun && token) {
    logAction(logFile, '⚠️  УВАГА: Backup експортує дані з Strapi і може перезаписати ваші локальні зміни!', 'warning');
    logAction(logFile, '   Переконайтеся, що ви зберегли всі зміни перед створенням backup', 'warning');
    const backupSuccess = await createBackup(token, logFile);
    if (!backupSuccess) {
      if (forceFlag) {
        logAction(logFile, '⚠️  Backup не створено, але продовжуємо з --force...', 'warning');
      } else {
        logAction(logFile, '❌ Backup не створено. Використайте --force для продовження без backup.', 'error');
        logAction(logFile, '   Це може призвести до втрати даних!', 'error');
        process.exit(1);
      }
    } else {
      logAction(logFile, '⚠️  ПЕРЕВІРТЕ: Файли могли бути перезаписані даними з Strapi!', 'warning');
      logAction(logFile, '   Переконайтеся, що ваші зміни все ще присутні в файлах', 'warning');
    }
  }
  
  // Статистика
  let successCount = 0;
  let errorCount = 0;
  const errors = [];
  
  // Оновлюємо кожен файл
  logAction(logFile, '\n📝 Початок оновлення файлів...\n', 'info');
  
  for (let i = 0; i < filesToUpdate.length; i++) {
    const file = filesToUpdate[i];
    
    logAction(logFile, `[${i + 1}/${filesToUpdate.length}] Оновлення ${file.entity}/${file.locale}.json...`, 'info');
    
    // Перевіряємо час модифікації файлу - якщо файл недавно змінений, попереджаємо
    try {
      const stats = fs.statSync(file.filePath);
      const now = new Date();
      const fileTime = new Date(stats.mtime);
      const diffMinutes = (now - fileTime) / (1000 * 60);
      
      if (diffMinutes < 1) {
        logAction(logFile, `   ⚠️  УВАГА: Файл був змінений менше ніж 1 хвилину тому!`, 'warning');
        logAction(logFile, `   ⚠️  Переконайтеся, що ви ЗБЕРЕГЛИ файл перед запуском скрипта!`, 'warning');
      }
    } catch (statError) {
      // Ігноруємо помилки статистики
    }
    
    // Валідація файлу
    const validation = validateFile(file.filePath);
    
    if (!validation.valid) {
      logAction(logFile, `   ❌ Помилка валідації: ${validation.error}`, 'error');
      errorCount++;
      errors.push({
        file: `${file.entity}/${file.locale}.json`,
        error: validation.error
      });
      continue;
    }
    
    // Логуємо що буде відправлено
    const fieldsToSend = Object.keys(validation.data).length;
    logAction(logFile, `   📤 Підготовлено ${fieldsToSend} полів для відправки`, 'info');
    logAction(logFile, `   📋 Поля: ${Object.keys(validation.data).join(', ')}`, 'info');
    
    // Логуємо конкретні значення з файлу (перші 3 поля для діагностики)
    const sampleFields = Object.keys(validation.data).slice(0, 3);
    sampleFields.forEach(field => {
      const value = validation.data[field];
      const preview = typeof value === 'string' ? value.substring(0, 60) : JSON.stringify(value).substring(0, 60);
      logAction(logFile, `   📄 З файлу ${field}: "${preview}${typeof value === 'string' && value.length > 60 ? '...' : ''}"`, 'info');
    });
    
    // Додаткова перевірка: читаємо файл напряму для порівняння
    try {
      const fileContent = fs.readFileSync(file.filePath, 'utf8');
      const fileData = JSON.parse(fileContent);
      
      
    } catch (checkError) {
      logAction(logFile, `   ⚠️  Помилка перевірки файлу: ${checkError.message}`, 'warning');
    }
    
    // Оновлення через API
    const result = await updateSingleType(
      file.endpoint,
      file.locale,
      validation.data,
      token,
      logFile,
      isDryRun || !needsConfirm
    );
    
    if (result.success) {
      logAction(logFile, `   ✅ ${result.message}`, 'success');
      successCount++;
    } else {
      logAction(logFile, `   ❌ ${result.message}`, 'error');
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
  logAction(logFile, '\n✅ Оновлення завершено!\n', 'success');
  logAction(logFile, '📊 Підсумок:', 'info');
  logAction(logFile, `   Успішно оновлено: ${successCount}`, 'success');
  logAction(logFile, `   Помилки: ${errorCount}`, errorCount > 0 ? 'error' : 'info');
  logAction(logFile, `   Log file: ${logFile}`, 'info');
  
  if (errors.length > 0) {
    logAction(logFile, '\n❌ Помилки:', 'error');
    errors.forEach(err => {
      logAction(logFile, `   - ${err.file}: ${err.error}`, 'error');
    });
  }
  
  // Запуск експорту після оновлення
  if (exportAfter && !isDryRun && token && successCount > 0) {
    logAction(logFile, '\n', 'info');
    logAction(logFile, '⚠️  УВАГА: Запускається експорт після оновлення!', 'warning');
    logAction(logFile, '⚠️  Це ПЕРЕЗАПИШЕ всі JSON файли даними з Strapi!', 'warning');
    logAction(logFile, '⚠️  Якщо ви редагували файли вручну, вони будуть перезаписані!', 'warning');
    await runExport(token, logFile);
    logAction(logFile, '⚠️  Експорт завершено - перевірте файли, чи не були вони перезаписані!', 'warning');
  }
  
  logAction(logFile, '\n', 'info');
}

module.exports = {
  updateEntity
};

