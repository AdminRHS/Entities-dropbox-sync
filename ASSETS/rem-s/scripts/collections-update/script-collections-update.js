// Load environment variables from .env file if it exists
try {
  require('dotenv').config({ path: require('path').join(__dirname, '..', '..', '.env') });
} catch (e) {
  // dotenv not installed or .env file doesn't exist - continue without it
}

const axios = require('axios');
const fs = require('fs').promises;
const path = require('path');

// Configuration
const STRAPI_URL = 'https://strapi.rem-s.com';
const LOCALES = ['ru', 'en', 'uk', 'pl'];
const BASE_UPDATE_DIR = path.join(__dirname, '..', '..', 'updated', 'collections');
const BASE_EXPORT_DIR = path.join(__dirname, '..', '..', 'exported', 'collections');

// Rate limiting configuration (to prevent server overload)
const RATE_LIMIT_DELAY = 800; // milliseconds between requests
const BATCH_SIZE = 10; // process files in batches
const MAX_RETRIES = 3; // retry failed requests
const RETRY_DELAY = 2000; // milliseconds before retry

// Collections configuration (same as export script)
const LOCALIZED_COLLECTIONS = ['vacancies', 'categories', 'keyword-tags', 'skills', 'form-users'];

// Collection name mapping for API endpoints
const COLLECTION_ENDPOINTS = {
  'vacancies': 'vacancies',
  'categories': 'categories',
  'keyword-tags': 'keyword-tags',
  'skills': 'skills',
  'form-users': 'form-users',
  'users': 'users',
  'submissions': 'submissions',
  'recipients': 'recipients',
  'audiences': 'audiences'
};

/**
 * Sleep/delay function
 * @param {number} ms - Milliseconds to wait
 */
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

/**
 * Get collection name and locale from file path
 * @param {string} filePath - Full path to JSON file
 * @param {string} baseDir - Base directory for relative path calculation
 * @returns {Object} { collectionName, locale, id, isValid, relativePath }
 */
function parseFilePath(filePath, baseDir = BASE_UPDATE_DIR) {
  const relativePath = path.relative(baseDir, filePath);
  const parts = relativePath.split(path.sep);
  
  if (parts.length < 2) {
    return { collectionName: null, locale: null, id: null, isValid: false, relativePath };
  }
  
  const collectionName = parts[0];
  const isLocalized = LOCALIZED_COLLECTIONS.includes(collectionName);
  
  if (isLocalized) {
    if (parts.length < 5 || parts[1] !== 'languages') {
      return { collectionName: null, locale: null, id: null, isValid: false, relativePath };
    }
    
    const locale = parts[2];
    const fileName = parts[parts.length - 1];
    const idMatch = fileName.match(/^(\d+)_/);
    const id = idMatch ? idMatch[1] : null;
    
    return {
      collectionName,
      locale,
      id,
      relativePath,
      isValid: collectionName && locale && id && LOCALES.includes(locale)
    };
  } else {
    if (parts.length < 3) {
      return { collectionName: null, locale: null, id: null, isValid: false, relativePath };
    }
    
    const fileName = parts[parts.length - 1];
    const idMatch = fileName.match(/^(\d+)_/);
    const id = idMatch ? idMatch[1] : null;
    
    return {
      collectionName,
      locale: null,
      id,
      relativePath,
      isValid: collectionName && id
    };
  }
}

/**
 * Read and parse JSON file
 * @param {string} filePath - Path to JSON file
 * @returns {Promise<Object>} Parsed JSON data
 */
async function readJsonFile(filePath) {
  try {
    const content = await fs.readFile(filePath, 'utf-8');
    const data = JSON.parse(content);
    
    // Extract data.attributes if exists (Strapi format)
    if (data.data && data.data.attributes) {
      return data.data.attributes;
    }
    
    if (data.attributes) {
      return data.attributes;
    }
    
    return data;
  } catch (error) {
    throw new Error(`Помилка читання файлу ${filePath}: ${error.message}`);
  }
}

/**
 * Clean data for Strapi API - fix media fields and relations format
 * @param {Object} data - Data to clean
 * @returns {Object} Cleaned data
 */
function cleanDataForApi(data) {
  const cleaned = { ...data };
  
  // Fix CV/media field: convert { data: { id: ... } } to { id: ... } or null
  if (cleaned.CV) {
    if (cleaned.CV.data && cleaned.CV.data.id) {
      cleaned.CV = { id: cleaned.CV.data.id };
    } else if (cleaned.CV.data === null) {
      cleaned.CV = null;
    } else if (cleaned.CV.id) {
      // Already in correct format
      cleaned.CV = { id: cleaned.CV.id };
    } else {
      // Unknown format, set to null
      cleaned.CV = null;
    }
  }
  
  // Fix localizations: convert { data: [] } to [] or extract IDs
  if (cleaned.localizations) {
    if (cleaned.localizations.data && Array.isArray(cleaned.localizations.data)) {
      // Extract IDs from array of objects
      cleaned.localizations = cleaned.localizations.data
        .map(item => item.id || item)
        .filter(id => id !== null && id !== undefined);
    } else if (Array.isArray(cleaned.localizations)) {
      // Already an array, keep as is
      cleaned.localizations = cleaned.localizations;
    } else {
      // Unknown format, set to empty array
      cleaned.localizations = [];
    }
  }
  
  // Remove system fields that shouldn't be sent
  delete cleaned.createdAt;
  delete cleaned.updatedAt;
  delete cleaned.publishedAt;
  
  return cleaned;
}

/**
 * Get file hash for comparison
 * @param {string} filePath - Path to file
 * @returns {Promise<string>} File hash
 */
async function getFileHash(filePath) {
  try {
    const content = await fs.readFile(filePath, 'utf-8');
    const stats = await fs.stat(filePath);
    return `${stats.size}_${stats.mtimeMs}`;
  } catch {
    return null;
  }
}


/**
 * Update collection item via Strapi API with retry logic
 * @param {string} collectionName - Collection name
 * @param {string} id - Item ID
 * @param {string} locale - Locale (optional)
 * @param {Object} data - Data to update
 * @param {string} token - API token
 * @param {boolean} dryRun - Dry run mode
 * @returns {Promise<Object>} { success: boolean, message: string, method: string }
 */
async function updateCollectionItem(collectionName, id, locale, data, token, dryRun = false) {
  const endpoint = COLLECTION_ENDPOINTS[collectionName] || collectionName;
  const url = `${STRAPI_URL}/api/${endpoint}/${id}`;
  
  if (dryRun) {
    console.log(`   🔍 [DRY-RUN] Оновлення ${collectionName} #${id}${locale ? ` (${locale})` : ''}`);
    return { success: true, message: 'Dry-run mode - зміни не застосовано', method: 'PUT' };
  }
  
  const config = {
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    }
  };
  
  if (locale && LOCALIZED_COLLECTIONS.includes(collectionName)) {
    config.params = { locale };
  }
  
  // Clean data before sending
  const cleanedData = cleanDataForApi(data);
  
  // Retry logic
  let lastError = null;
  for (let attempt = 1; attempt <= MAX_RETRIES; attempt++) {
    try {
      // Try PUT first
      const response = await axios.put(url, { data: cleanedData }, config);
      return {
        success: true,
        message: 'Оновлено успішно',
        method: 'PUT',
        response: response.data
      };
    } catch (putError) {
      lastError = putError;
      
      // If 429 (Too Many Requests) or 500, wait and retry
      if (putError.response && (putError.response.status === 429 || putError.response.status >= 500)) {
        if (attempt < MAX_RETRIES) {
          const waitTime = RETRY_DELAY * attempt; // Exponential backoff
          console.log(`   ⏳ Затримка ${waitTime}ms перед повторною спробою (спроба ${attempt + 1}/${MAX_RETRIES})...`);
          await sleep(waitTime);
          continue;
        }
      }
      
      // If PUT fails with 400+, try PATCH
      if (putError.response && putError.response.status >= 400 && putError.response.status < 500) {
        try {
          const patchResponse = await axios.patch(url, { data: cleanedData }, config);
          return {
            success: true,
            message: 'Оновлено успішно (через PATCH)',
            method: 'PATCH',
            response: patchResponse.data
          };
        } catch (patchError) {
          lastError = patchError;
        }
      }
      
      // If last attempt, return error
      if (attempt === MAX_RETRIES) {
        break;
      }
    }
  }
  
  // All retries failed
  if (lastError && lastError.response) {
    return {
      success: false,
      message: `Помилка API: ${lastError.response.status} - ${JSON.stringify(lastError.response.data)}`,
      method: 'PUT'
    };
  }
  return {
    success: false,
    message: `Помилка мережі: ${lastError?.message || 'Невідома помилка'}`,
    method: 'PUT'
  };
}

/**
 * Create new collection item via Strapi API with retry logic
 * @param {string} collectionName - Collection name
 * @param {string} locale - Locale (optional)
 * @param {Object} data - Data to create
 * @param {string} token - API token
 * @param {boolean} dryRun - Dry run mode
 * @returns {Promise<Object>} { success: boolean, message: string, method: string }
 */
async function createCollectionItem(collectionName, locale, data, token, dryRun = false) {
  const endpoint = COLLECTION_ENDPOINTS[collectionName] || collectionName;
  const url = `${STRAPI_URL}/api/${endpoint}`;
  
  if (dryRun) {
    console.log(`   🔍 [DRY-RUN] Створення нового ${collectionName}${locale ? ` (${locale})` : ''}`);
    return { success: true, message: 'Dry-run mode - зміни не застосовано', method: 'POST' };
  }
  
  const config = {
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    }
  };
  
  if (locale && LOCALIZED_COLLECTIONS.includes(collectionName)) {
    config.params = { locale };
  }
  
  // Clean data before sending
  const cleanedData = cleanDataForApi(data);
  
  // Retry logic
  let lastError = null;
  for (let attempt = 1; attempt <= MAX_RETRIES; attempt++) {
    try {
      const response = await axios.post(url, { data: cleanedData }, config);
      return {
        success: true,
        message: 'Створено успішно',
        method: 'POST',
        response: response.data
      };
    } catch (error) {
      lastError = error;
      
      // If 429 (Too Many Requests) or 500, wait and retry
      if (error.response && (error.response.status === 429 || error.response.status >= 500)) {
        if (attempt < MAX_RETRIES) {
          const waitTime = RETRY_DELAY * attempt;
          console.log(`   ⏳ Затримка ${waitTime}ms перед повторною спробою (спроба ${attempt + 1}/${MAX_RETRIES})...`);
          await sleep(waitTime);
          continue;
        }
      }
      
      if (attempt === MAX_RETRIES) {
        break;
      }
    }
  }
  
  if (lastError && lastError.response) {
    return {
      success: false,
      message: `Помилка API: ${lastError.response.status} - ${JSON.stringify(lastError.response.data)}`,
      method: 'POST'
    };
  }
  return {
    success: false,
    message: `Помилка мережі: ${lastError?.message || 'Невідома помилка'}`,
    method: 'POST'
  };
}

/**
 * Delete collection item via Strapi API with retry logic
 * @param {string} collectionName - Collection name
 * @param {string} id - Item ID
 * @param {string} locale - Locale (optional)
 * @param {string} token - API token
 * @param {boolean} dryRun - Dry run mode
 * @returns {Promise<Object>} { success: boolean, message: string }
 */
async function deleteItem(collectionName, id, locale, token, dryRun = false) {
  const endpoint = COLLECTION_ENDPOINTS[collectionName] || collectionName;
  const url = `${STRAPI_URL}/api/${endpoint}/${id}`;
  
  if (dryRun) {
    console.log(`   🔍 [DRY-RUN] Видалення ${collectionName} #${id}${locale ? ` (${locale})` : ''}`);
    return { success: true, message: 'Dry-run mode - зміни не застосовано' };
  }
  
  const config = {
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    }
  };
  
  if (locale && LOCALIZED_COLLECTIONS.includes(collectionName)) {
    config.params = { locale };
  }
  
  // Retry logic
  let lastError = null;
  for (let attempt = 1; attempt <= MAX_RETRIES; attempt++) {
    try {
      const response = await axios.delete(url, config);
      return {
        success: true,
        message: 'Видалено успішно',
        response: response.data
      };
    } catch (error) {
      lastError = error;
      
      // If 429 (Too Many Requests) or 500, wait and retry
      if (error.response && (error.response.status === 429 || error.response.status >= 500)) {
        if (attempt < MAX_RETRIES) {
          const waitTime = RETRY_DELAY * attempt;
          console.log(`   ⏳ Затримка ${waitTime}ms перед повторною спробою (спроба ${attempt + 1}/${MAX_RETRIES})...`);
          await sleep(waitTime);
          continue;
        }
      }
      
      if (attempt === MAX_RETRIES) {
        break;
      }
    }
  }
  
  if (lastError && lastError.response) {
    return {
      success: false,
      message: `Помилка API: ${lastError.response.status} - ${JSON.stringify(lastError.response.data)}`
    };
  }
  return {
    success: false,
    message: `Помилка мережі: ${lastError?.message || 'Невідома помилка'}`
  };
}

/**
 * Find all JSON files in directory
 * @param {string} dir - Directory to scan
 * @returns {Promise<Array>} Array of file paths
 */
async function findJsonFiles(dir) {
  const files = [];
  
  async function scanDirectory(directory) {
    try {
      const entries = await fs.readdir(directory, { withFileTypes: true });
      
      for (const entry of entries) {
        const fullPath = path.join(directory, entry.name);
        
        if (entry.isDirectory()) {
          await scanDirectory(fullPath);
        } else if (entry.isFile() && entry.name.endsWith('.json') && !entry.name.includes('-list.json') && !entry.name.startsWith('.')) {
          files.push(fullPath);
        }
      }
    } catch (error) {
      // Ignore errors for non-existent directories
    }
  }
  
  await scanDirectory(dir);
  return files;
}

/**
 * Process batch of files with rate limiting
 * @param {Array} batch - Array of file info objects
 * @param {string} token - API token
 * @param {boolean} dryRun - Dry run mode
 * @returns {Promise<Object>} Results object
 */
async function processBatch(batch, token, dryRun) {
  const results = {
    created: { success: [], failed: [] },
    updated: { success: [], failed: [] },
    deleted: { success: [], failed: [] }
  };
  
  for (const item of batch) {
    try {
      if (item.action === 'delete') {
        // Delete item
        const result = await deleteItem(
          item.collection,
          item.id,
          item.locale,
          token,
          dryRun
        );
        
        if (result.success) {
          console.log(`   ✅ Видалено: ${item.collection} #${item.id}${item.locale ? ` (${item.locale})` : ''}`);
          results.deleted.success.push(item);
        } else {
          console.log(`   ❌ Помилка видалення: ${item.collection} #${item.id}${item.locale ? ` (${item.locale})` : ''} - ${result.message}`);
          results.deleted.failed.push({ ...item, error: result.message });
        }
      } else if (item.action === 'create') {
        // Create new item
        const data = await readJsonFile(item.filePath);
        const result = await createCollectionItem(
          item.collection,
          item.locale,
          data,
          token,
          dryRun
        );
        
        if (result.success) {
          console.log(`   ✅ Створено: ${item.collection}${item.id ? ` #${item.id}` : ''}${item.locale ? ` (${item.locale})` : ''} [${result.method}]`);
          results.created.success.push(item);
        } else {
          console.log(`   ❌ Помилка створення: ${item.collection}${item.id ? ` #${item.id}` : ''}${item.locale ? ` (${item.locale})` : ''} - ${result.message}`);
          results.created.failed.push({ ...item, error: result.message });
        }
      } else if (item.action === 'update') {
        // Update existing item
        const data = await readJsonFile(item.filePath);
        const result = await updateCollectionItem(
          item.collection,
          item.id,
          item.locale,
          data,
          token,
          dryRun
        );
        
        if (result.success) {
          console.log(`   ✅ Оновлено: ${item.collection} #${item.id}${item.locale ? ` (${item.locale})` : ''} [${result.method}]`);
          results.updated.success.push(item);
        } else {
          console.log(`   ❌ Помилка оновлення: ${item.collection} #${item.id}${item.locale ? ` (${item.locale})` : ''} - ${result.message}`);
          results.updated.failed.push({ ...item, error: result.message });
        }
      }
      
      // Rate limiting - delay between requests (except for dry-run)
      if (!dryRun) {
        await sleep(RATE_LIMIT_DELAY);
      }
    } catch (error) {
      console.log(`   ❌ Помилка обробки ${item.relativePath}: ${error.message}`);
      if (item.action === 'create') {
        results.created.failed.push({ ...item, error: error.message });
      } else if (item.action === 'update') {
        results.updated.failed.push({ ...item, error: error.message });
      }
    }
  }
  
  return results;
}

/**
 * Main update function
 */
async function updateCollections() {
  const isDryRun = process.argv.includes('--dry-run') || process.argv.includes('-d');
  const token = process.env.STRAPI_TOKEN || process.argv[2];
  
  // Check for collection filter (e.g., --only=vacancies)
  const onlyArg = process.argv.find(arg => arg.startsWith('--only='));
  const onlyCollection = onlyArg ? onlyArg.split('=')[1] : null;
  
  if (!token && !isDryRun) {
    console.error('❌ Помилка: API токен обов\'язковий!');
    console.error('\nВикористання:');
    console.error('  node script-collections-update.js <token>');
    console.error('  node script-collections-update.js <token> --dry-run  (перегляд без змін)');
    console.error('  node script-collections-update.js <token> --only=vacancies  (тільки вакансії)');
    console.error('  або встановіть змінну оточення STRAPI_TOKEN');
    process.exit(1);
  }
  
  if (onlyCollection) {
    console.log(`🎯 Фільтр: обробка тільки колекції "${onlyCollection}"\n`);
  }
  
  console.log('🚀 Аналіз та оновлення колекцій з Strapi\n');
  console.log(`📍 Strapi URL: ${STRAPI_URL}`);
  console.log(`📁 Папка з оновленими даними: ${BASE_UPDATE_DIR}`);
  console.log(`📁 Папка з оригінальними даними: ${BASE_EXPORT_DIR}`);
  console.log(`⏱️  Затримка між запитами: ${RATE_LIMIT_DELAY}ms`);
  console.log(`📦 Розмір батчу: ${BATCH_SIZE} файлів`);
  console.log(`🔄 Максимум повторів: ${MAX_RETRIES}\n`);
  
  if (isDryRun) {
    console.log('🔍 Режим DRY-RUN - зміни не будуть застосовані\n');
  } else {
    console.log('⚠️  Режим ОНОВЛЕННЯ - зміни будуть застосовані!\n');
  }
  
  try {
    // No snapshot needed - just scan files directly
    console.log('📂 Підготовка до оновлення файлів...\n');
    
    // Find all current files in updated directory
    console.log('📂 Сканування папки з оновленими даними...\n');
    const currentFiles = await findJsonFiles(BASE_UPDATE_DIR);
    
    if (currentFiles.length === 0) {
      console.log('⚠️  Файлів для оновлення не знайдено');
      console.log(`   Перевірте папку: ${BASE_UPDATE_DIR}\n`);
      return;
    }
    
    console.log(`   ✓ Знайдено ${currentFiles.length} файлів\n`);
    
    // Create current snapshot from updated files
    console.log('📸 Створення snapshot оновлених файлів...\n');
    const currentSnapshot = {};
    for (const filePath of currentFiles) {
      const parsed = parseFilePath(filePath);
      if (parsed.isValid) {
        const key = parsed.relativePath;
        const hash = await getFileHash(filePath);
        currentSnapshot[key] = {
          hash,
          collection: parsed.collectionName,
          id: parsed.id,
          locale: parsed.locale,
          filePath
        };
      }
    }
    
    // Find all files in exported directory for comparison
    console.log('📂 Сканування папки з оригінальними даними...\n');
    const exportedFiles = await findJsonFiles(BASE_EXPORT_DIR);
    
    console.log(`   ✓ Знайдено ${exportedFiles.length} оригінальних файлів\n`);
    
    // Create snapshot from exported files
    console.log('📸 Створення snapshot оригінальних файлів...\n');
    const exportedSnapshot = {};
    for (const filePath of exportedFiles) {
      const parsed = parseFilePath(filePath, BASE_EXPORT_DIR);
      if (parsed.isValid) {
        const key = parsed.relativePath;
        const hash = await getFileHash(filePath);
        exportedSnapshot[key] = {
          hash,
          collection: parsed.collectionName,
          id: parsed.id,
          locale: parsed.locale,
          filePath
        };
      }
    }
    
    // Compare and find changes
    console.log('🔍 Порівняння файлів для визначення змін...\n');
    
    const changes = {
      created: [],    // New files (POST) - в updated, немає в exported
      updated: [],    // Modified files (PUT/PATCH) - є в обох, але hash різний
      deleted: []     // Deleted files (DELETE) - НЕ ВИКОРИСТОВУЄТЬСЯ
    };
    
    // Find new and modified files (ONLY process files from updated folder)
    for (const [relativePath, info] of Object.entries(currentSnapshot)) {
      // Skip if collection filter is set and doesn't match
      if (onlyCollection && info.collection !== onlyCollection) {
        continue;
      }
      
      const exportedInfo = exportedSnapshot[relativePath];
      
      if (!exportedInfo) {
        // File doesn't exist in exported - treat as modified (not new)
        // We update existing records on server, not create new ones
        changes.updated.push({
          relativePath,
          collection: info.collection,
          id: info.id,
          locale: info.locale,
          filePath: info.filePath
        });
      } else if (exportedInfo.hash !== info.hash) {
        // File exists but hash is different - it's modified
        changes.updated.push({
          relativePath,
          collection: info.collection,
          id: info.id,
          locale: info.locale,
          filePath: info.filePath
        });
      }
      // If hash is the same - file is unchanged, skip it
    }
    
    // NOTE: We DON'T process deletions automatically
    // If file is missing from updated - user removed it locally
    // But we don't delete from server automatically - too dangerous
    // User should delete via Strapi admin if needed
    
    // Display changes summary
    console.log('📊 Знайдені зміни:\n');
    console.log(`   ➕ Створено: ${changes.created.length}`);
    console.log(`   ✏️  Оновлено: ${changes.updated.length}`);
    console.log(`   🗑️  Видалено: ${changes.deleted.length}`);
    console.log(`   📦 Всього змін: ${changes.created.length + changes.updated.length + changes.deleted.length}\n`);
    
    if (changes.created.length === 0 && changes.updated.length === 0 && changes.deleted.length === 0) {
      console.log('✅ Змін не знайдено. Всі файли актуальні.\n');
      return;
    }
    
    // Prepare all changes with actions
    const allChanges = [
      ...changes.deleted.map(item => ({ ...item, action: 'delete' })),
      ...changes.created.map(item => ({ ...item, action: 'create' })),
      ...changes.updated.map(item => ({ ...item, action: 'update' }))
    ];
    
    // Process in batches
    const results = {
      created: { success: [], failed: [] },
      updated: { success: [], failed: [] },
      deleted: { success: [], failed: [] }
    };
    
    const totalBatches = Math.ceil(allChanges.length / BATCH_SIZE);
    
    for (let i = 0; i < allChanges.length; i += BATCH_SIZE) {
      const batch = allChanges.slice(i, i + BATCH_SIZE);
      const batchNumber = Math.floor(i / BATCH_SIZE) + 1;
      
      console.log(`📦 Обробка батчу ${batchNumber}/${totalBatches} (${batch.length} файлів)...\n`);
      
      const batchResults = await processBatch(batch, token, isDryRun);
      
      // Merge results
      results.created.success.push(...batchResults.created.success);
      results.created.failed.push(...batchResults.created.failed);
      results.updated.success.push(...batchResults.updated.success);
      results.updated.failed.push(...batchResults.updated.failed);
      results.deleted.success.push(...batchResults.deleted.success);
      results.deleted.failed.push(...batchResults.deleted.failed);
      
      // Delay between batches (except for dry-run and last batch)
      if (!isDryRun && i + BATCH_SIZE < allChanges.length) {
        console.log(`\n   ⏸️  Пауза між батчами...\n`);
        await sleep(RATE_LIMIT_DELAY * 2);
      }
      
      console.log('');
    }
    
    // Summary
    console.log('='.repeat(60));
    console.log('📊 Підсумок:\n');
    console.log(`   ➕ Створено: ${results.created.success.length} успішно, ${results.created.failed.length} помилок`);
    console.log(`   ✏️  Оновлено: ${results.updated.success.length} успішно, ${results.updated.failed.length} помилок`);
    console.log(`   🗑️  Видалено: ${results.deleted.success.length} успішно, ${results.deleted.failed.length} помилок`);
    console.log(`   📦 Всього оброблено: ${results.created.success.length + results.updated.success.length + results.deleted.success.length}\n`);
    
    // Show errors if any
    const totalFailed = results.created.failed.length + results.updated.failed.length + results.deleted.failed.length;
    if (totalFailed > 0) {
      console.log('❌ Файли з помилками:\n');
      [...results.created.failed, ...results.updated.failed, ...results.deleted.failed].forEach(item => {
        console.log(`   - ${item.relativePath || item.collection}${item.error ? `: ${item.error}` : ''}`);
      });
      console.log('');
    }
    
    if (isDryRun) {
      console.log('💡 Для застосування змін запустіть без --dry-run\n');
    } else if (totalFailed === 0) {
      console.log('✅ Всі зміни успішно застосовано!\n');
    }
    
  } catch (error) {
    console.error('\n❌ Критична помилка:', error.message);
    if (error.stack) {
      console.error('\nStack trace:', error.stack);
    }
    process.exit(1);
  }
}

// Run update
updateCollections();
