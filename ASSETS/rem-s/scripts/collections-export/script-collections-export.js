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
const BASE_EXPORT_DIR = path.join(__dirname, '..', '..', 'exported', 'collections');

// Collections configuration
// Collections with localization (i18n enabled)
// Based on Strapi admin URLs with plugins[i18n][locale] parameter
// Collections that have locale parameter in admin URL are localized
// Use plural names to match API endpoints
const LOCALIZED_COLLECTIONS = ['vacancies', 'categories', 'keyword-tags', 'skills', 'form-users'];

// Collection name mapping: Admin URL -> API endpoint
// Based on actual Strapi admin URLs from https://strapi.rem-s.com/admin:
// - api::category.category -> /api/category (with locale)
// - api::skill.skill -> /api/skill
// - api::form-user.form-user -> /api/form-user (with locale)
// - api::keyword-tag.keyword-tag -> /api/keyword-tag
// - plugin::ezforms.submission -> /api/submissions (ezforms plugin, plural)
// - plugin::ezforms.recipient -> /api/recipients (ezforms plugin, plural)
// - plugin::users-permissions.user -> /api/users (users-permissions plugin, plural)
// - plugin::navigation.audience -> /api/audiences (navigation plugin, plural)
// Collections that are confirmed working (have data in exported folders)
// Based on actual exported data structure
const COLLECTIONS = [
  'vacancies',            // ✅ Confirmed working - has data
  'categories',           // ✅ Confirmed working - has data
  'form-users',           // ✅ Confirmed working - has data in ru locale
  'keyword-tags',         // ✅ Confirmed working - has data
  'skills',               // ✅ Confirmed working - has data
  'submissions',          // plugin::ezforms.submission -> /api/submissions
  'recipients',           // plugin::ezforms.recipient -> /api/recipients
  'users',                // plugin::users-permissions.user -> /api/users
  'audiences'             // plugin::navigation.audience -> /api/audiences
];

// Alternative names to try if main name fails
// Based on Strapi admin URLs, try different variations
const COLLECTION_ALTERNATIVES = {
  'categories': ['category'],
  'form-users': ['form-user', 'form-users'],
  'keyword-tags': ['keyword-tag', 'keyword-tags'],
  'skills': ['skill'],
  'submissions': ['submission', 'ezforms/submissions', 'form-submissions', 'form-submission'],
  'recipients': ['recipient', 'ezforms/recipients', 'notification-recipients', 'notification-recipient'],
  'users': ['user'],
  'audiences': ['audience', 'navigation/audiences']
};

/**
 * Get export paths for a collection
 * @param {string} collectionName - Collection name
 * @param {string} locale - Locale code (optional)
 * @returns {Object} Paths object
 */
function getCollectionPaths(collectionName, locale = null) {
  const isLocalized = LOCALIZED_COLLECTIONS.includes(collectionName);
  
  if (isLocalized && locale) {
    // Localized collection structure: collections/{name}/languages/{locale}/
    const localeDir = path.join(BASE_EXPORT_DIR, collectionName, 'languages', locale);
    const itemsDir = path.join(localeDir, collectionName);
    return {
      baseDir: path.join(BASE_EXPORT_DIR, collectionName),
      localeDir,
      itemsDir,
      listFile: path.join(localeDir, `${collectionName}-list.json`)
    };
  } else {
    // Non-localized collection structure: collections/{name}/
    const itemsDir = path.join(BASE_EXPORT_DIR, collectionName, collectionName);
    return {
      baseDir: path.join(BASE_EXPORT_DIR, collectionName),
      itemsDir,
      listFile: path.join(BASE_EXPORT_DIR, collectionName, `${collectionName}-list.json`)
    };
  }
}

/**
 * Ensure export directories exist
 * @param {string} collectionName - Collection name
 * @param {string} locale - Locale code (optional)
 */
async function ensureDirectories(collectionName, locale = null) {
  const paths = getCollectionPaths(collectionName, locale);
  await fs.mkdir(paths.itemsDir, { recursive: true });
}

/**
 * Try to find correct endpoint name by testing alternatives
 * @param {string} token - Strapi API token
 * @param {string} collectionName - Collection name to try
 * @param {string} locale - Locale code (optional)
 * @returns {string|null} Correct endpoint name or null if not found
 */
async function findCorrectEndpoint(token, collectionName, locale = null) {
  const alternatives = COLLECTION_ALTERNATIVES[collectionName] || [];
  const namesToTry = [collectionName, ...alternatives];
  
  for (const name of namesToTry) {
    try {
      const params = {
        'pagination[page]': 1,
        'pagination[pageSize]': 1,
        'populate': '*'
      };
      
      if (locale && LOCALIZED_COLLECTIONS.includes(collectionName)) {
        params.locale = locale;
      }
      
      const response = await axios.get(`${STRAPI_URL}/api/${name}`, {
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        params,
        validateStatus: (status) => status < 500 // Don't throw on 404, only on server errors
      });
      
      if (response.status === 200 && response.data?.data) {
        console.log(`   ✓ Found correct endpoint: ${name} (was trying ${collectionName})`);
        return name;
      }
    } catch (error) {
      // Continue to next alternative
      continue;
    }
  }
  
  return null;
}

/**
 * Fetch all items from Strapi with pagination
 * @param {string} token - Strapi API token
 * @param {string} collectionName - Collection name
 * @param {string} locale - Locale code (optional)
 * @returns {Array} Array of items
 */
async function fetchAllItems(token, collectionName, locale = null) {
  // First, try to find correct endpoint name (only if not vacancies which we know works)
  let actualEndpointName = collectionName;
  if (collectionName !== 'vacancies') {
    actualEndpointName = await findCorrectEndpoint(token, collectionName, locale);
    if (!actualEndpointName) {
      // If not found, use original name and let it fail with proper error
      actualEndpointName = collectionName;
      console.log(`   ⚠️  Could not find correct endpoint for ${collectionName}, trying original name`);
    }
  }
  
  let allItems = [];
  let page = 1;
  let hasMore = true;

  while (hasMore) {
    try {
      // Build params - locale goes first in URL, then other params
      // Based on code example: `/categories?locale=${lang}` with additional params
      const params = {
        'pagination[page]': page,
        'pagination[pageSize]': 100,
        'populate': '*'
      };

      // Add locale to params if collection is localized
      // Strapi API accepts locale both in URL and params, but URL is more common
      if (locale && LOCALIZED_COLLECTIONS.includes(collectionName)) {
        params.locale = locale;
      }

      const response = await axios.get(`${STRAPI_URL}/api/${actualEndpointName}`, {
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        params
      });

      const { data, meta } = response.data;
      
      if (!data || !Array.isArray(data)) {
        console.warn(`⚠️  Unexpected response structure for ${actualEndpointName}${locale ? ` (${locale})` : ''}, page ${page}`);
        break;
      }

      allItems.push(...data);
      
      const pageCount = meta?.pagination?.pageCount || 1;
      const total = meta?.pagination?.total || data.length;
      
      const localeLabel = locale ? ` ${locale.toUpperCase()}` : '';
      console.log(`   ${actualEndpointName}${localeLabel}: Page ${page}/${pageCount}: ${data.length} items (Total: ${allItems.length}/${total})`);

      hasMore = page < pageCount;
      page++;
      
      // Safety limit
      if (page > 1000) {
        console.warn('⚠️  Safety limit reached (1000 pages)');
        break;
      }
    } catch (error) {
      if (error.response) {
        const status = error.response.status;
        const errorMsg = error.response.data?.error?.message || JSON.stringify(error.response.data);
        
        // Don't throw for 404 - collection might not exist or have different name
        if (status === 404) {
          console.warn(`⚠️  Collection "${actualEndpointName}" not found (404). Tried: ${collectionName}`);
          if (COLLECTION_ALTERNATIVES[collectionName]) {
            console.warn(`   💡 Alternatives to try: ${COLLECTION_ALTERNATIVES[collectionName].join(', ')}`);
          }
          return [];
        }
        
        // Don't throw for 403 - might be permission issue
        if (status === 403) {
          console.warn(`⚠️  No permission to access "${actualEndpointName}" (403). Check token permissions.`);
          return [];
        }
        
        // Don't throw for 401 - authentication issue
        if (status === 401) {
          console.error(`❌ Authentication failed for "${actualEndpointName}" (401). Check token.`);
          throw error;
        }
        
        console.error(`❌ API Error (${actualEndpointName}${locale ? `, ${locale}` : ''}, Page ${page}):`, status, errorMsg);
      } else {
        console.error(`❌ Network Error (${actualEndpointName}${locale ? `, ${locale}` : ''}, Page ${page}):`, error.message);
      }
      throw error;
    }
  }

  return allItems;
}

/**
 * Generate safe filename from item data
 * @param {Object} item - Item object
 * @param {string} collectionName - Collection name
 * @returns {string} Safe filename
 */
function generateFilename(item, collectionName) {
  const id = item.id || 'unknown';
  
  // Try to get title/name from attributes
  const title = item.attributes?.title || 
                item.attributes?.name || 
                item.attributes?.email ||
                item.attributes?.username ||
                collectionName;
  
  // Clean title for filename
  const cleanTitle = title.toString()
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, '')
    .replace(/\s+/g, '-')
    .substring(0, 50)
    .replace(/^-+|-+$/g, '') || collectionName;
  
  return `${id}_${cleanTitle}`;
}

/**
 * Clean ALL old files from export directory before new export
 * @param {string} collectionName - Collection name
 * @param {string} locale - Locale code (optional)
 */
async function cleanAllOldFiles(collectionName, locale) {
  try {
    const paths = getCollectionPaths(collectionName, locale);
    
    // Check if directory exists
    try {
      await fs.access(paths.itemsDir);
    } catch {
      // Directory doesn't exist, nothing to clean
      return 0;
    }
    
    const files = await fs.readdir(paths.itemsDir);
    const jsonFiles = files.filter(file => file.endsWith('.json'));
    
    if (jsonFiles.length > 0) {
      await Promise.all(
        jsonFiles.map(file => 
          fs.unlink(path.join(paths.itemsDir, file))
        )
      );
      return jsonFiles.length;
    }
    return 0;
  } catch (error) {
    console.warn(`⚠️  Could not clean old files for ${collectionName}${locale ? ` (${locale})` : ''}:`, error.message);
    return 0;
  }
}

/**
 * Clean old list file
 * @param {string} collectionName - Collection name
 * @param {string} locale - Locale code (optional)
 */
async function cleanOldListFile(collectionName, locale) {
  try {
    const paths = getCollectionPaths(collectionName, locale);
    try {
      await fs.unlink(paths.listFile);
      return 1;
    } catch {
      // File doesn't exist, nothing to clean
      return 0;
    }
  } catch (error) {
    return 0;
  }
}

/**
 * Remove empty directories recursively
 * @param {string} dirPath - Directory path to check
 */
async function removeEmptyDirectories(dirPath) {
  try {
    const files = await fs.readdir(dirPath);
    
    // If directory is empty, try to remove it
    if (files.length === 0) {
      try {
        await fs.rmdir(dirPath);
        return true;
      } catch {
        // Directory might not be removable, skip
        return false;
      }
    }
    
    // Recursively check subdirectories
    for (const file of files) {
      const filePath = path.join(dirPath, file);
      try {
        const stat = await fs.stat(filePath);
        if (stat.isDirectory()) {
          const wasRemoved = await removeEmptyDirectories(filePath);
          if (wasRemoved) {
            // Try to remove parent if it became empty
            await removeEmptyDirectories(dirPath);
          }
        }
      } catch {
        // Skip errors
      }
    }
    
    return false;
  } catch {
    // Directory doesn't exist or can't be accessed
    return false;
  }
}

/**
 * Export single item to JSON
 * @param {Object} item - Item object
 * @param {string} collectionName - Collection name
 * @param {string} locale - Locale code (optional)
 * @returns {Promise<{filename: string}>}
 */
async function exportItem(item, collectionName, locale = null) {
  const filename = generateFilename(item, collectionName);
  const paths = getCollectionPaths(collectionName, locale);
  const jsonPath = path.join(paths.itemsDir, `${filename}.json`);
  const content = JSON.stringify(item, null, 2);
  await fs.writeFile(jsonPath, content, 'utf8');
  return { filename: `${filename}.json` };
}

/**
 * Create list file for a collection
 * @param {Array} items - Array of all items
 * @param {string} collectionName - Collection name
 * @param {string} locale - Locale code (optional)
 */
async function createListFile(items, collectionName, locale = null) {
  const paths = getCollectionPaths(collectionName, locale);
  
  const list = {
    exportDate: new Date().toISOString(),
    collection: collectionName,
    locale: locale || null,
    total: items.length,
    items: items.map(item => {
      const filename = generateFilename(item, collectionName);
      return {
        id: item.id,
        title: item.attributes?.title || 
               item.attributes?.name || 
               item.attributes?.email ||
               item.attributes?.username ||
               'Untitled',
        filename: filename,
        slug: item.attributes?.slug || 
              item.attributes?.vacancySlug || 
              item.attributes?.categorySlug || null,
        createdAt: item.attributes?.createdAt,
        updatedAt: item.attributes?.updatedAt,
        publishedAt: item.attributes?.publishedAt
      };
    })
  };

  await fs.writeFile(paths.listFile, JSON.stringify(list, null, 2), 'utf8');
  return paths.listFile;
}

/**
 * Export collection for a single locale (or non-localized)
 * @param {string} token - Strapi API token
 * @param {string} collectionName - Collection name
 * @param {string} locale - Locale code (optional)
 * @param {boolean} keepOld - Keep old files
 */
async function exportCollectionLocale(token, collectionName, locale, keepOld) {
  const localeLabel = locale ? ` ${locale.toUpperCase()}` : '';
  console.log(`\n📦 Exporting ${collectionName}${localeLabel}...\n`);
  
  // Fetch all items FIRST (before creating directories)
  let items;
  try {
    items = await fetchAllItems(token, collectionName, locale);
  } catch (error) {
    // If fetchAllItems returned empty array for 404/403, it's already handled
    // Re-throw other errors
    console.error(`   ❌ Error fetching ${collectionName}${localeLabel}:`, error.message);
    throw error;
  }
  
  // If no items found, don't create any directories or files
  if (!items || items.length === 0) {
    console.log(`   ⚠️  No ${collectionName}${localeLabel} items found - skipping (no files created)\n`);
    return { collectionName, locale, count: 0, exported: 0 };
  }
  
  // Only create directories if we have items to export (don't create empty folders)
  const paths = getCollectionPaths(collectionName, locale);
  await ensureDirectories(collectionName, locale);
  console.log(`   📁 Export directory: ${paths.itemsDir}`);
  console.log(`   📄 List file: ${paths.listFile}\n`);

  console.log(`\n   📦 Found ${items.length} ${collectionName}${localeLabel} items\n`);

  // Note: Old files are already cleaned at the start of exportAllCollections
  // This is just for logging if keepOld is set
  if (keepOld) {
    console.log(`   ℹ️  Keeping old files (--keep-old flag set)\n`);
  }

  // Export all items in parallel
  const startTime = Date.now();
  
  const exportPromises = items.map(item => exportItem(item, collectionName, locale));
  const exported = await Promise.all(exportPromises);
  
  const exportTime = ((Date.now() - startTime) / 1000).toFixed(2);
  console.log(`   💾 Exported ${exported.length} items (${exportTime}s)`);
  
  // Verify files were created
  try {
    const files = await fs.readdir(paths.itemsDir);
    const jsonFiles = files.filter(f => f.endsWith('.json'));
    console.log(`   ✓ Verified: ${jsonFiles.length} JSON files in ${paths.itemsDir}\n`);
  } catch (error) {
    console.warn(`   ⚠️  Could not verify files: ${error.message}\n`);
  }

  // Create list file
  const listPath = await createListFile(items, collectionName, locale);
  console.log(`   📋 Created list: ${path.basename(listPath)}`);
  
  // Verify list file exists
  try {
    const listExists = await fs.access(listPath).then(() => true).catch(() => false);
    if (listExists) {
      console.log(`   ✓ Verified: List file exists at ${listPath}\n`);
    }
  } catch (error) {
    console.warn(`   ⚠️  Could not verify list file: ${error.message}\n`);
  }

  return { 
    collectionName,
    locale, 
    count: items.length, 
    exported: exported.length,
    time: exportTime
  };
}

/**
 * Export a collection (with all locales if localized)
 * @param {string} token - Strapi API token
 * @param {string} collectionName - Collection name
 * @param {boolean} keepOld - Keep old files
 */
async function exportCollection(token, collectionName, keepOld) {
  const isLocalized = LOCALIZED_COLLECTIONS.includes(collectionName);
  const results = [];
  let hasAnyData = false;

  if (isLocalized) {
    // Export for each locale
    for (const locale of LOCALES) {
      try {
        const result = await exportCollectionLocale(token, collectionName, locale, keepOld);
        results.push(result);
        if (result.count > 0) {
          hasAnyData = true;
        }
      } catch (error) {
        console.error(`\n❌ Failed to export ${collectionName} (${locale}):`, error.message);
        results.push({ collectionName, locale, count: 0, exported: 0, error: error.message });
      }
    }
  } else {
    // Export without locale
    try {
      const result = await exportCollectionLocale(token, collectionName, null, keepOld);
      results.push(result);
      if (result.count > 0) {
        hasAnyData = true;
      }
    } catch (error) {
      console.error(`\n❌ Failed to export ${collectionName}:`, error.message);
      results.push({ collectionName, locale: null, count: 0, exported: 0, error: error.message });
    }
  }

  // If no data was exported for any locale, clean up empty directories
  if (!hasAnyData && !keepOld) {
    try {
      const paths = getCollectionPaths(collectionName, null);
      // Remove empty directories recursively
      await removeEmptyDirectories(paths.baseDir);
    } catch (error) {
      // Ignore errors when cleaning up
    }
  }

  return results;
}

/**
 * Test all endpoints to find correct names
 */
async function testAllEndpoints(token) {
  console.log('🧪 Testing all endpoints to find correct names...\n');
  
  if (!token) {
    console.log('⚠️  No token provided, testing without authentication\n');
  }
  
  const results = {};
  
  for (const collection of COLLECTIONS) {
    const alternatives = [collection, ...(COLLECTION_ALTERNATIVES[collection] || [])];
    console.log(`\n🔍 Testing ${collection}:`);
    
    for (const name of alternatives) {
      try {
        const params = {
          'pagination[page]': 1,
          'pagination[pageSize]': 1,
          'populate': '*'
        };
        
        if (LOCALIZED_COLLECTIONS.includes(collection)) {
          params.locale = 'ru';
        }
        
        const response = await axios.get(`${STRAPI_URL}/api/${name}`, {
          headers: token ? {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          } : {},
          params,
          validateStatus: () => true
        });
        
        if (response.status === 200 && response.data?.data) {
          console.log(`   ✅ ${name} - Status: ${response.status}, Items: ${response.data.data.length}`);
          results[collection] = name;
          break;
        } else if (response.status === 401) {
          console.log(`   ⚠️  ${name} - Status: ${response.status} (Auth required, endpoint exists)`);
          results[collection] = name;
          break;
        } else if (response.status === 403) {
          console.log(`   ⚠️  ${name} - Status: ${response.status} (No permission, endpoint exists)`);
          results[collection] = name;
          break;
        } else {
          console.log(`   ❌ ${name} - Status: ${response.status}`);
        }
      } catch (error) {
        console.log(`   ❌ ${name} - Error: ${error.message}`);
      }
    }
    
    if (!results[collection]) {
      console.log(`   ⚠️  No working endpoint found for ${collection}`);
    }
  }
  
  console.log('\n📊 Results:');
  console.log(JSON.stringify(results, null, 2));
  
  return results;
}

/**
 * Test endpoint connection (without token)
 */
async function testEndpoint() {
  console.log('🧪 Testing Strapi endpoint...\n');
  console.log(`📍 URL: ${STRAPI_URL}/api/\n`);
  
  const token = process.env.STRAPI_TOKEN || process.argv[2];
  
  // Test all endpoints if token provided
  if (token) {
    await testAllEndpoints(token);
  } else {
    try {
      const response = await axios.get(`${STRAPI_URL}/api/vacancies`, {
        params: {
          'pagination[page]': 1,
          'pagination[pageSize]': 1,
          'locale': 'ru'
        },
        validateStatus: () => true
      });
      
      console.log('📡 Response Status:', response.status);
      
      if (response.status === 200 || response.status === 401) {
        console.log('✅ Endpoint is accessible');
        if (response.status === 401) {
          console.log('⚠️  Authentication required (expected)');
        }
      }
    } catch (error) {
      if (error.response) {
        console.log('📡 Response Status:', error.response.status);
        console.log('✅ Endpoint is accessible (error response received)');
      } else {
        console.error('❌ Network error:', error.message);
        throw error;
      }
    }
  }
  
  // Test directory structure
  console.log(`\n📁 Base export directory: ${BASE_EXPORT_DIR}`);
  for (const collection of COLLECTIONS) {
    const isLocalized = LOCALIZED_COLLECTIONS.includes(collection);
    if (isLocalized) {
      for (const locale of LOCALES) {
        const paths = getCollectionPaths(collection, locale);
        await ensureDirectories(collection, locale);
        console.log(`   ✓ ${collection}/${locale.toUpperCase()}: ${paths.localeDir}`);
      }
    } else {
      const paths = getCollectionPaths(collection);
      await ensureDirectories(collection);
      console.log(`   ✓ ${collection}: ${paths.baseDir}`);
    }
  }
}

/**
 * Main export function
 */
async function exportAllCollections() {
  const isTest = process.argv.includes('--test') || process.argv.includes('-t');
  
  if (isTest) {
    await testEndpoint();
    return;
  }

  console.log('🚀 Starting collections export from Strapi\n');
  console.log(`📍 Strapi URL: ${STRAPI_URL}`);
  console.log(`📁 Export directory: ${BASE_EXPORT_DIR}`);
  console.log(`📦 Collections: ${COLLECTIONS.join(', ')}`);
  console.log(`🌐 Localized collections: ${LOCALIZED_COLLECTIONS.join(', ')}\n`);

  // Get token from environment or command line
  const token = process.env.STRAPI_TOKEN || process.argv[2];
  
  if (!token) {
    console.error('❌ Error: Strapi API token required!');
    console.error('\nUsage:');
    console.error('  node script-collections.js <token>');
    console.error('  node script-collections.js <token> --keep-old  (keep old files)');
    console.error('  node script-collections.js --test  (test endpoint without token)');
    console.error('  or set STRAPI_TOKEN environment variable');
    console.error('\nExample:');
    console.error('  node script-collections.js your_token_here');
    console.error('  node script-collections.js your_token_here --keep-old');
    console.error('  STRAPI_TOKEN=your_token_here node script-collections.js');
    process.exit(1);
  }

  try {
    // Check if keep old files option
    const keepOld = process.argv.includes('--keep-old') || process.argv.includes('-k');
    
    if (!keepOld) {
      console.log('🧹 Cleaning all old data before export...\n');
      // Clean all old files for all collections
      for (const collection of COLLECTIONS) {
        const isLocalized = LOCALIZED_COLLECTIONS.includes(collection);
        if (isLocalized) {
          for (const locale of LOCALES) {
            await cleanAllOldFiles(collection, locale);
            await cleanOldListFile(collection, locale);
          }
        } else {
          await cleanAllOldFiles(collection, null);
          await cleanOldListFile(collection, null);
        }
      }
      console.log('   ✓ All old data cleaned\n');
    }
    
    // Export all collections
    console.log('📥 Fetching collections from Strapi...\n');
    
    const allResults = [];
    const totalStartTime = Date.now();
    
    for (const collection of COLLECTIONS) {
      try {
        const results = await exportCollection(token, collection, keepOld);
        allResults.push(...results);
      } catch (error) {
        console.error(`\n❌ Failed to export ${collection}:`, error.message);
        allResults.push({ collectionName: collection, locale: null, count: 0, exported: 0, error: error.message });
      }
    }
    
    const totalTime = ((Date.now() - totalStartTime) / 1000).toFixed(2);

    // Summary
    console.log('✅ Export completed!\n');
    console.log('📊 Summary:\n');
    
    // Group by collection
    const byCollection = {};
    for (const result of allResults) {
      if (!byCollection[result.collectionName]) {
        byCollection[result.collectionName] = [];
      }
      byCollection[result.collectionName].push(result);
    }
    
    let totalItems = 0;
    let totalFiles = 0;
    
    for (const [collectionName, results] of Object.entries(byCollection)) {
      const isLocalized = LOCALIZED_COLLECTIONS.includes(collectionName);
      const collectionTotal = results.reduce((sum, r) => sum + (r.count || 0), 0);
      const collectionFiles = results.reduce((sum, r) => sum + (r.exported || 0), 0);
      
      totalItems += collectionTotal;
      totalFiles += collectionFiles;
      
      if (isLocalized) {
        console.log(`   ${collectionName.toUpperCase()}:`);
        for (const result of results) {
          const locale = result.locale ? result.locale.toUpperCase() : 'ALL';
          if (result.error) {
            console.log(`      ${locale}: ❌ ERROR - ${result.error}`);
          } else {
            console.log(`      ${locale}: ${result.count || 0} items, ${result.exported || 0} files`);
          }
        }
        if (collectionTotal > 0) {
          console.log(`      TOTAL: ${collectionTotal} items, ${collectionFiles} files\n`);
        } else {
          console.log(`      ⚠️  No items exported (check collection name and permissions)\n`);
        }
      } else {
        const hasError = results.some(r => r.error);
        if (hasError) {
          const error = results.find(r => r.error)?.error || 'Unknown error';
          console.log(`   ${collectionName.toUpperCase()}: ❌ ERROR - ${error}\n`);
        } else {
          console.log(`   ${collectionName.toUpperCase()}: ${collectionTotal} items, ${collectionFiles} files\n`);
        }
      }
    }
    
    console.log(`   ⏱️  Total time: ${totalTime}s`);
    console.log(`   📦 Total items: ${totalItems}`);
    console.log(`   📄 Total files: ${totalFiles}`);
    console.log(`   📁 Export directory: ${BASE_EXPORT_DIR}\n`);
    
    // Clean up any empty directories that might have been created
    if (!keepOld) {
      console.log('🧹 Cleaning up empty directories...\n');
      for (const collection of COLLECTIONS) {
        try {
          const paths = getCollectionPaths(collection, null);
          await removeEmptyDirectories(paths.baseDir);
        } catch {
          // Ignore errors
        }
      }
      console.log('   ✓ Cleanup completed\n');
    }

  } catch (error) {
    console.error('\n❌ Export failed:', error.message);
    if (error.response) {
      console.error('   Status:', error.response.status);
      console.error('   Data:', JSON.stringify(error.response.data, null, 2));
    }
    process.exit(1);
  }
}

// Run export
exportAllCollections();

