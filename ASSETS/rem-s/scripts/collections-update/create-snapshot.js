// Load environment variables from .env file if it exists
try {
  require('dotenv').config({ path: require('path').join(__dirname, '..', '..', '.env') });
} catch (e) {
  // dotenv not installed or .env file doesn't exist - continue without it
}

const fs = require('fs').promises;
const path = require('path');

// Configuration
const BASE_EXPORT_DIR = path.join(__dirname, '..', '..', 'exported', 'collections');
const SNAPSHOT_FILE = path.join(BASE_EXPORT_DIR, '.snapshot.json');
const LOCALIZED_COLLECTIONS = ['vacancies', 'categories', 'keyword-tags', 'skills', 'form-users'];

/**
 * Get file hash for comparison
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
 * Find all JSON files recursively
 */
async function findJsonFiles(dir, baseDir = dir) {
  const files = [];
  try {
    const entries = await fs.readdir(dir, { withFileTypes: true });
    
    for (const entry of entries) {
      const fullPath = path.join(dir, entry.name);
      const relativePath = path.relative(baseDir, fullPath);
      
      if (entry.isDirectory()) {
        const subFiles = await findJsonFiles(fullPath, baseDir);
        files.push(...subFiles);
      } else if (entry.isFile() && entry.name.endsWith('.json') && !entry.name.includes('-list.json')) {
        files.push(relativePath);
      }
    }
  } catch (error) {
    // Ignore errors for directories that don't exist
  }
  
  return files;
}

/**
 * Parse file path to get collection info
 */
function parseFilePath(filePath, baseDir = BASE_EXPORT_DIR) {
  const relativePath = filePath;
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
      isValid: collectionName && locale && id
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
 * Create snapshot from exported files
 */
async function createSnapshot() {
  console.log('📸 Створення snapshot з експортованих файлів...\n');
  
  try {
    // Find all JSON files
    console.log('📂 Сканування експортованих файлів...\n');
    const files = await findJsonFiles(BASE_EXPORT_DIR);
    
    console.log(`   ✓ Знайдено ${files.length} файлів\n`);
    
    // Create snapshot
    const snapshot = {};
    let processed = 0;
    
    for (const filePath of files) {
      const parsed = parseFilePath(filePath);
      if (parsed.isValid) {
        const fullPath = path.join(BASE_EXPORT_DIR, filePath);
        const hash = await getFileHash(fullPath);
        
        if (hash) {
          snapshot[parsed.relativePath] = {
            hash,
            collection: parsed.collectionName,
            id: parsed.id,
            locale: parsed.locale
          };
        }
      }
      
      processed++;
      if (processed % 100 === 0) {
        console.log(`   ⏳ Оброблено ${processed}/${files.length} файлів...`);
      }
    }
    
    // Save snapshot
    await fs.writeFile(SNAPSHOT_FILE, JSON.stringify(snapshot, null, 2), 'utf-8');
    
    console.log(`\n✅ Snapshot створено успішно!\n`);
    console.log(`   📁 Файл: ${SNAPSHOT_FILE}`);
    console.log(`   📊 Записано ${Object.keys(snapshot).length} файлів\n`);
    
  } catch (error) {
    console.error('\n❌ Помилка створення snapshot:', error.message);
    if (error.stack) {
      console.error('\nStack trace:', error.stack);
    }
    process.exit(1);
  }
}

// Run
createSnapshot();






