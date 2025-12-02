const fs = require('fs').promises;
const path = require('path');
const os = require('os');

// Configuration
const BASE_EXPORT_DIR = path.join(__dirname, '..', 'exported', 'collections');
const BASE_UPDATE_DIR = path.join(__dirname, '..', 'updated', 'collections');
const REPORTS_DIR = path.join(__dirname, '..', 'reports');
const TRACKER_FILE = path.join(REPORTS_DIR, 'changes-tracker.json');
const STATUS_FILE = path.join(REPORTS_DIR, 'current-status.json');
const SESSIONS_FILE = path.join(REPORTS_DIR, 'active-sessions.json');
const USER_PROFILE_FILE = path.join(REPORTS_DIR, 'user-profiles.json');

/**
 * Get file hash (size + mtime)
 */
async function getFileHash(filePath) {
  try {
    const stats = await fs.stat(filePath);
    return {
      size: stats.size,
      mtime: stats.mtime.toISOString(),
      mtimeMs: stats.mtimeMs
    };
  } catch {
    return null;
  }
}

/**
 * Get current user info
 */
function getCurrentUser() {
  return {
    username: os.userInfo().username,
    hostname: os.hostname(),
    platform: os.platform()
  };
}

/**
 * Normalize JSON for comparison
 */
function normalizeJson(obj) {
  return JSON.stringify(obj, Object.keys(obj).sort(), 2);
}

/**
 * Compare two JSON objects
 */
function compareJson(obj1, obj2) {
  const normalized1 = normalizeJson(obj1);
  const normalized2 = normalizeJson(obj2);
  return normalized1 === normalized2;
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
      
      // Skip hidden files, templates, list files
      if (entry.name.startsWith('.') || 
          entry.name.includes('template') ||
          entry.name.endsWith('list.json') ||
          entry.name.includes('-list.json')) {
        continue;
      }
      
      if (entry.isDirectory()) {
        const subFiles = await findJsonFiles(fullPath, baseDir);
        files.push(...subFiles);
      } else if (entry.isFile() && entry.name.endsWith('.json')) {
        // Only include files with ID prefix
        if (/^\d+_/.test(entry.name)) {
          files.push(fullPath);
        }
      }
    }
  } catch (error) {
    // Directory doesn't exist or can't be read
  }
  
  return files;
}

/**
 * Load existing tracker
 */
async function loadTracker() {
  try {
    const data = await fs.readFile(TRACKER_FILE, 'utf8');
    return JSON.parse(data);
  } catch {
    return {
      changes: [],
      lastUpdate: null
    };
  }
}

/**
 * Save tracker
 */
async function saveTracker(tracker) {
  await fs.mkdir(REPORTS_DIR, { recursive: true });
  tracker.lastUpdate = new Date().toISOString();
  await fs.writeFile(TRACKER_FILE, JSON.stringify(tracker, null, 2), 'utf8');
}

/**
 * Read JSON file
 */
async function readJsonFile(filePath) {
  try {
    const content = await fs.readFile(filePath, 'utf8');
    return JSON.parse(content);
  } catch {
    return null;
  }
}

/**
 * Get what changed between two objects
 */
function getChanges(oldObj, newObj, path = '') {
  const changes = [];
  
  if (!oldObj && newObj) {
    changes.push({
      path: path || 'root',
      action: 'added',
      oldValue: null,
      newValue: typeof newObj === 'object' ? '[object]' : newObj
    });
    return changes;
  }
  
  if (oldObj && !newObj) {
    changes.push({
      path: path || 'root',
      action: 'removed',
      oldValue: typeof oldObj === 'object' ? '[object]' : oldObj,
      newValue: null
    });
    return changes;
  }
  
  if (typeof oldObj !== 'object' || typeof newObj !== 'object' || 
      oldObj === null || newObj === null) {
    if (oldObj !== newObj) {
      changes.push({
        path: path || 'root',
        action: 'modified',
        oldValue: oldObj,
        newValue: newObj
      });
    }
    return changes;
  }
  
  const allKeys = new Set([...Object.keys(oldObj), ...Object.keys(newObj)]);
  
  for (const key of allKeys) {
    const newPath = path ? `${path}.${key}` : key;
    const oldVal = oldObj[key];
    const newVal = newObj[key];
    
    if (!(key in oldObj)) {
      changes.push({
        path: newPath,
        action: 'added',
        oldValue: null,
        newValue: typeof newVal === 'object' ? '[object]' : newVal
      });
    } else if (!(key in newObj)) {
      changes.push({
        path: newPath,
        action: 'removed',
        oldValue: typeof oldVal === 'object' ? '[object]' : oldVal,
        newValue: null
      });
    } else {
      changes.push(...getChanges(oldVal, newVal, newPath));
    }
  }
  
  return changes;
}

/**
 * Main tracking function
 */
async function trackChanges() {
  console.log('🔍 Аналіз змін у файлах...\n');
  
  const user = getCurrentUser();
  const timestamp = new Date().toISOString();
  
  // Load existing tracker
  const tracker = await loadTracker();
  
  // Find all files in exported (original)
  console.log('📂 Сканування оригінальних файлів...');
  const exportedFiles = await findJsonFiles(BASE_EXPORT_DIR, BASE_EXPORT_DIR);
  console.log(`   ✓ Знайдено ${exportedFiles.length} оригінальних файлів\n`);
  
  // Find all files in updated
  console.log('📂 Сканування оновлених файлів...');
  const updatedFiles = await findJsonFiles(BASE_UPDATE_DIR, BASE_UPDATE_DIR);
  console.log(`   ✓ Знайдено ${updatedFiles.length} оновлених файлів\n`);
  
  // Create maps for quick lookup
  const exportedMap = new Map();
  for (const file of exportedFiles) {
    const relativePath = path.relative(BASE_EXPORT_DIR, file);
    exportedMap.set(relativePath, file);
  }
  
  const updatedMap = new Map();
  for (const file of updatedFiles) {
    const relativePath = path.relative(BASE_UPDATE_DIR, file);
    updatedMap.set(relativePath, file);
  }
  
  // Track changes
  const currentStatus = {
    files: [],
    summary: {
      total: 0,
      modified: 0,
      created: 0,
      deleted: 0,
      unchanged: 0
    },
    lastUpdate: timestamp
  };
  
  console.log('🔍 Порівняння файлів...\n');
  
  // Check all updated files
  for (const [relativePath, updatedFile] of updatedMap.entries()) {
    const exportedFile = exportedMap.get(relativePath);
    const updatedHash = await getFileHash(updatedFile);
    const updatedData = await readJsonFile(updatedFile);
    
    let status = 'created';
    let changes = [];
    let lastModified = updatedHash?.mtime;
    
    if (exportedFile) {
      const exportedHash = await getFileHash(exportedFile);
      const exportedData = await readJsonFile(exportedFile);
      
      if (exportedHash && updatedHash) {
        if (exportedHash.mtimeMs === updatedHash.mtimeMs) {
          status = 'unchanged';
        } else {
          status = 'modified';
          // Compare content
          if (exportedData && updatedData) {
            changes = getChanges(exportedData, updatedData);
            // Filter out only meaningful changes (not just metadata)
            changes = changes.filter(c => 
              !c.path.includes('createdAt') && 
              !c.path.includes('updatedAt') &&
              !c.path.includes('publishedAt')
            );
          }
        }
        lastModified = updatedHash.mtime;
      }
    }
    
    // Extract collection info from path
    const pathParts = relativePath.split(path.sep);
    const collectionName = pathParts[0];
    const locale = pathParts.includes('languages') ? pathParts[2] : null;
    const fileName = pathParts[pathParts.length - 1];
    const idMatch = fileName.match(/^(\d+)_/);
    const id = idMatch ? idMatch[1] : null;
    
    const fileInfo = {
      path: relativePath,
      collection: collectionName,
      locale: locale,
      id: id,
      fileName: fileName,
      status: status,
      lastModified: lastModified,
      changesCount: changes.length,
      changes: changes.slice(0, 5), // Limit to first 5 changes for summary
      editor: status === 'modified' || status === 'created' ? user.username : null
    };
    
    currentStatus.files.push(fileInfo);
    
    // Add to tracker if modified or created
    if (status === 'modified' || status === 'created') {
      tracker.changes.push({
        timestamp: timestamp,
        user: user.username,
        hostname: user.hostname,
        path: relativePath,
        collection: collectionName,
        locale: locale,
        id: id,
        action: status,
        changes: changes.slice(0, 10) // Limit changes in tracker
      });
    }
    
    // Update summary
    currentStatus.summary.total++;
    if (status === 'modified') currentStatus.summary.modified++;
    else if (status === 'created') currentStatus.summary.created++;
    else currentStatus.summary.unchanged++;
  }
  
  // Check for deleted files
  for (const [relativePath, exportedFile] of exportedMap.entries()) {
    if (!updatedMap.has(relativePath)) {
      const pathParts = relativePath.split(path.sep);
      const collectionName = pathParts[0];
      const locale = pathParts.includes('languages') ? pathParts[2] : null;
      const fileName = pathParts[pathParts.length - 1];
      const idMatch = fileName.match(/^(\d+)_/);
      const id = idMatch ? idMatch[1] : null;
      
      const exportedHash = await getFileHash(exportedFile);
      
      const fileInfo = {
        path: relativePath,
        collection: collectionName,
        locale: locale,
        id: id,
        fileName: fileName,
        status: 'deleted',
        lastModified: exportedHash?.mtime,
        changesCount: 0,
        changes: [],
        editor: user.username
      };
      
      currentStatus.files.push(fileInfo);
      currentStatus.summary.total++;
      currentStatus.summary.deleted = (currentStatus.summary.deleted || 0) + 1;
      
      tracker.changes.push({
        timestamp: timestamp,
        user: user.username,
        hostname: user.hostname,
        path: relativePath,
        collection: collectionName,
        locale: locale,
        id: id,
        action: 'deleted',
        changes: []
      });
    }
  }
  
  // Calculate statistics by collection
    const collectionStats = {};
    for (const file of currentStatus.files) {
      if (!collectionStats[file.collection]) {
        collectionStats[file.collection] = {
          total: 0,
          modified: 0,
          created: 0,
          deleted: 0,
          unchanged: 0
        };
      }
      collectionStats[file.collection].total++;
      if (file.status === 'modified') collectionStats[file.collection].modified++;
      else if (file.status === 'created') collectionStats[file.collection].created++;
      else if (file.status === 'deleted') collectionStats[file.collection].deleted++;
      else collectionStats[file.collection].unchanged++;
    }
  
  // Add collection stats to status
  currentStatus.collectionStats = collectionStats;
  
  // Filter only changed files for display (modified, created, or deleted)
  currentStatus.changedFiles = currentStatus.files.filter(f => 
    f.status === 'modified' || f.status === 'created' || f.status === 'deleted'
  );
  
  // Save files
  await saveTracker(tracker);
  await fs.writeFile(STATUS_FILE, JSON.stringify(currentStatus, null, 2), 'utf8');
  
  // Generate HTML report
  await generateHtmlReport(currentStatus, tracker);
  
  console.log('✅ Відстеження змін завершено!\n');
  console.log('📊 Підсумок:');
  console.log(`   Всього файлів: ${currentStatus.summary.total}`);
  console.log(`   Змінено: ${currentStatus.summary.modified}`);
  console.log(`   Створено: ${currentStatus.summary.created}`);
  if (currentStatus.summary.deleted > 0) {
    console.log(`   Видалено: ${currentStatus.summary.deleted}`);
  }
  console.log(`   Без змін: ${currentStatus.summary.unchanged}\n`);
  console.log(`📁 Звіти збережено в: ${REPORTS_DIR}`);
  console.log(`   - changes-tracker.json - повна історія змін`);
  console.log(`   - current-status.json - поточний стан`);
  console.log(`   - changes-report.html - таблиця для перегляду\n`);
}

/**
 * Load active sessions
 */
async function loadActiveSessions() {
  try {
    const data = await fs.readFile(SESSIONS_FILE, 'utf8');
    const sessions = JSON.parse(data);
    // Filter only active sessions
    const now = Date.now();
    return sessions.sessions.filter(s => {
      if (s.status !== 'active') return false;
      const sessionAge = now - new Date(s.startedAt).getTime();
      const maxDuration = s.duration || 4 * 60 * 60 * 1000; // 4 hours
      return sessionAge < maxDuration;
    });
  } catch {
    return [];
  }
}

/**
 * Generate HTML report
 */
async function generateHtmlReport(status, tracker) {
  // Load active sessions
  const activeSessions = await loadActiveSessions();
  const html = `<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Звіт про зміни в колекціях</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: #f5f5f5;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            padding: 30px;
        }
        h1 {
            color: #2c3e50;
            margin-bottom: 10px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-weight: 600;
            font-size: 28px;
        }
        h2 {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-weight: 600;
            font-size: 22px;
        }
        .subtitle {
            color: #7f8c8d;
            margin-bottom: 30px;
        }
        .summary {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .summary-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }
        .summary-card h3 {
            font-size: 32px;
            margin-bottom: 5px;
        }
        .summary-card p {
            opacity: 0.9;
            font-size: 14px;
        }
        .summary-card.modified {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        }
        .summary-card.created {
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        }
        .summary-card.unchanged {
            background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
        }
        .collection-card {
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .collection-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }
        .collection-card.has-changes {
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.9; }
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #e0e0e0;
        }
        th {
            background: #f8f9fa;
            font-weight: 600;
            color: #2c3e50;
            position: sticky;
            top: 0;
        }
        tr:hover {
            background: #f8f9fa;
        }
        .status-badge {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 600;
            text-transform: uppercase;
        }
        .status-modified {
            background: #fff3cd;
            color: #856404;
        }
        .status-created {
            background: #d1ecf1;
            color: #0c5460;
        }
        .status-unchanged {
            background: #d4edda;
            color: #155724;
        }
        .status-deleted {
            background: #f8d7da;
            color: #721c24;
        }
        .changes-list {
            font-size: 12px;
            color: #666;
            max-width: 300px;
        }
        .changes-list li {
            margin: 4px 0;
            padding-left: 10px;
        }
        .filter-bar {
            margin-bottom: 20px;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            align-items: center;
        }
        .filter-btn {
            padding: 8px 16px;
            border: 1px solid #ddd;
            background: white;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.2s;
        }
        .filter-btn:hover {
            background: #f8f9fa;
        }
        .filter-btn.active {
            background: #667eea;
            color: white;
            border-color: #667eea;
        }
        .search-box {
            flex: 1;
            min-width: 250px;
            padding: 10px 15px;
            border: 2px solid #e0e0e0;
            border-radius: 6px;
            font-size: 14px;
            transition: border-color 0.2s;
        }
        .search-box:focus {
            outline: none;
            border-color: #667eea;
        }
        .search-box::placeholder {
            color: #999;
        }
        .last-update {
            text-align: right;
            color: #7f8c8d;
            font-size: 12px;
            margin-top: 20px;
        }
        .active-sessions {
            background: #fff3cd;
            border: 2px solid #ffc107;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 30px;
        }
        .active-sessions h2 {
            color: #856404;
            margin-bottom: 15px;
            font-size: 18px;
        }
        .session-item {
            background: white;
            padding: 15px;
            border-radius: 6px;
            margin-bottom: 10px;
            border-left: 4px solid #ffc107;
        }
        .session-item:last-child {
            margin-bottom: 0;
        }
        .session-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        }
        .session-name {
            font-weight: 600;
            color: #856404;
        }
        .session-time {
            font-size: 12px;
            color: #666;
        }
        .session-work {
            color: #333;
            font-size: 14px;
        }
        .no-sessions {
            color: #666;
            font-style: italic;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Звіт про зміни в колекціях</h1>
        <p class="subtitle">Відстеження редагувань файлів вакансій та інших колекцій</p>
        
        ${activeSessions.length > 0 ? `
        <div class="active-sessions">
            <h2>🟢 Активні сесії (${activeSessions.length} ${activeSessions.length === 1 ? 'користувач працює' : 'користувачів працюють'})</h2>
            ${activeSessions.map(session => {
              const startTime = new Date(session.startedAt);
              const endTime = new Date(session.estimatedEnd);
              return `
                <div class="session-item">
                    <div class="session-header">
                        <span class="session-name">${session.name || session.username} (${session.role || 'Користувач'})</span>
                        <span class="session-time">${startTime.toLocaleString('uk-UA')} - ${endTime.toLocaleString('uk-UA')}</span>
                    </div>
                    <div class="session-work">${session.currentWork || 'Робота з колекціями'}</div>
                </div>
              `;
            }).join('')}
        </div>
        ` : `
        <div class="active-sessions">
            <h2>Активні сесії</h2>
            <div class="no-sessions">Наразі ніхто не працює</div>
        </div>
        `}
        
        <h2 style="margin-top: 20px; margin-bottom: 20px; color: #2c3e50;">Колекції</h2>
        <div class="summary" id="collectionsSummary">
            ${(() => {
              // Color palette for different collections - clear, vibrant colors
              const collectionColors = {
                'vacancies': 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
                'categories': 'linear-gradient(135deg, #ec4899 0%, #f43f5e 100%)',
                'keyword-tags': 'linear-gradient(135deg, #0ea5e9 0%, #06b6d4 100%)',
                'skills': 'linear-gradient(135deg, #10b981 0%, #059669 100%)',
                'form-users': 'linear-gradient(135deg, #f59e0b 0%, #d97706 100%)'
              };
              
              // Default color for unknown collections
              const defaultColor = 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)';
              
              return Object.entries(status.collectionStats || {}).map(([collection, stats]) => {
                const hasChanges = stats.modified > 0 || stats.created > 0 || stats.deleted > 0;
                const bgColor = collectionColors[collection] || defaultColor;
                const changesCount = stats.modified + stats.created + (stats.deleted || 0);
                return `
                  <div class="summary-card collection-card ${hasChanges ? 'has-changes' : ''}" 
                       onclick="filterByCollection('${collection}')" 
                       style="cursor: pointer; background: ${bgColor}; ${hasChanges ? 'border: 3px solid #ffc107;' : ''}">
                      <h3>${changesCount}</h3>
                      <p>${collection}</p>
                  </div>
                `;
              }).join('');
            })()}
        </div>
        
        <div class="filter-bar" style="margin-top: 30px;">
            <input type="text" 
                   id="searchInput" 
                   class="search-box" 
                   placeholder="🔍 Пошук за датою, назвою, мовою, ID..." 
                   onkeyup="performSearch()">
            <button class="filter-btn active" onclick="filterTable('all')">Всі</button>
            <button class="filter-btn" onclick="filterTable('modified')">Змінено</button>
            <button class="filter-btn" onclick="filterTable('created')">Створено</button>
            <button class="filter-btn" onclick="filterTable('deleted')">Видалено</button>
        </div>
        
        <div id="tableContainer">
            ${status.changedFiles && status.changedFiles.length > 0 ? `
            <table id="changesTable">
                <thead>
                    <tr>
                        <th>Статус</th>
                        <th>Колекція</th>
                        <th>Мова</th>
                        <th>ID</th>
                        <th>Файл</th>
                        <th>Хто редагував</th>
                        <th>Коли</th>
                        <th>Що змінилося</th>
                    </tr>
                </thead>
                <tbody>
                    ${status.changedFiles.map(file => {
                      const dateStr = file.lastModified ? new Date(file.lastModified).toLocaleString('uk-UA') : '-';
                      return `
                    <tr data-status="${file.status}" 
                        data-collection="${file.collection}"
                        data-locale="${file.locale || ''}"
                        data-id="${file.id || ''}"
                        data-filename="${file.fileName}"
                        data-date="${dateStr}"
                        data-editor="${file.editor || ''}">
                        <td>
                            <span class="status-badge status-${file.status}">
                                ${file.status === 'modified' ? 'Змінено' : 
                                  file.status === 'created' ? 'Створено' : 
                                  file.status === 'deleted' ? 'Видалено' :
                                  'Без змін'}
                            </span>
                        </td>
                        <td>${file.collection}</td>
                        <td>${file.locale || '-'}</td>
                        <td>${file.id || '-'}</td>
                        <td>${file.fileName}</td>
                        <td>${file.editor || '-'}</td>
                        <td>${dateStr}</td>
                        <td>
                            ${file.changesCount > 0 ? `
                                <ul class="changes-list">
                                    ${file.changes.slice(0, 3).map(c => `
                                        <li>${c.path}: ${c.action === 'modified' ? 'змінено' : c.action === 'added' ? 'додано' : 'видалено'}</li>
                                    `).join('')}
                                    ${file.changesCount > 3 ? `<li>... і ще ${file.changesCount - 3}</li>` : ''}
                                </ul>
                            ` : '-'}
                        </td>
                    </tr>
                    `;
                    }).join('')}
                </tbody>
            </table>
            ` : `
            <div style="text-align: center; padding: 60px 20px; color: #7f8c8d;">
                <h3 style="font-size: 24px; margin-bottom: 10px;">✨ Поки що немає змін</h3>
                <p style="font-size: 16px;">Коли хтось відредагує або створить файли, вони з'являться тут</p>
            </div>
            `}
        </div>
        
        <div class="last-update">
            Оновлено: ${new Date(status.lastUpdate).toLocaleString('uk-UA')}
        </div>
    </div>
    
    <script>
        let currentCollection = null;
        
        function filterTable(status) {
            const rows = document.querySelectorAll('#changesTable tbody tr');
            const buttons = document.querySelectorAll('.filter-btn');
            const searchInput = document.getElementById('searchInput');
            const searchTerm = searchInput ? searchInput.value.toLowerCase().trim() : '';
            
            buttons.forEach(btn => btn.classList.remove('active'));
            if (event && event.target) {
                event.target.classList.add('active');
            }
            
            rows.forEach(row => {
                let show = false;
                
                if (status === 'all') {
                    // Show all files, respecting collection filter if active
                    show = !currentCollection || row.dataset.collection === currentCollection;
                } else {
                    // Show files with specific status, respecting collection filter if active
                    show = row.dataset.status === status && (!currentCollection || row.dataset.collection === currentCollection);
                }
                
                // Apply search filter if search term exists
                if (show && searchTerm) {
                    const collection = (row.dataset.collection || '').toLowerCase();
                    const locale = (row.dataset.locale || '').toLowerCase();
                    const id = (row.dataset.id || '').toLowerCase();
                    const filename = (row.dataset.filename || '').toLowerCase();
                    const date = (row.dataset.date || '').toLowerCase();
                    const editor = (row.dataset.editor || '').toLowerCase();
                    
                    const matches = 
                        collection.includes(searchTerm) ||
                        locale.includes(searchTerm) ||
                        id.includes(searchTerm) ||
                        filename.includes(searchTerm) ||
                        date.includes(searchTerm) ||
                        editor.includes(searchTerm);
                    
                    show = matches;
                }
                
                row.style.display = show ? '' : 'none';
            });
        }
        
        function filterByCollection(collection) {
            const rows = document.querySelectorAll('#changesTable tbody tr');
            const cards = document.querySelectorAll('.collection-card');
            
            if (currentCollection === collection) {
                // Deselect
                currentCollection = null;
                cards.forEach(card => {
                    const cardText = card.querySelector('p').textContent.trim();
                    if (cardText === collection) {
                        // Restore original border if has changes
                        const hasChanges = card.classList.contains('has-changes');
                        card.style.border = hasChanges ? '3px solid #ffc107' : '';
                    }
                });
            } else {
                // Select
                currentCollection = collection;
                cards.forEach(card => {
                    const cardText = card.querySelector('p').textContent.trim();
                    if (cardText === collection) {
                        card.style.border = '3px solid #667eea';
                    } else {
                        // Restore original border if has changes
                        const hasChanges = card.classList.contains('has-changes');
                        card.style.border = hasChanges ? '3px solid #ffc107' : '';
                    }
                });
            }
            
            // Apply current filter
            const activeBtn = document.querySelector('.filter-btn.active');
            if (activeBtn) {
                const btnText = activeBtn.textContent.trim().toLowerCase();
                filterTable(btnText === 'всі' ? 'all' : btnText);
            } else {
                filterTable('all');
            }
        }
        
        function performSearch() {
            const searchInput = document.getElementById('searchInput');
            const searchTerm = searchInput.value.toLowerCase().trim();
            const rows = document.querySelectorAll('#changesTable tbody tr');
            
            if (!searchTerm) {
                // If search is empty, apply current filter
                const activeBtn = document.querySelector('.filter-btn.active');
                if (activeBtn) {
                    const btnText = activeBtn.textContent.trim().toLowerCase();
                    filterTable(btnText === 'всі' ? 'all' : btnText);
                }
                return;
            }
            
            rows.forEach(row => {
                const collection = (row.dataset.collection || '').toLowerCase();
                const locale = (row.dataset.locale || '').toLowerCase();
                const id = (row.dataset.id || '').toLowerCase();
                const filename = (row.dataset.filename || '').toLowerCase();
                const date = (row.dataset.date || '').toLowerCase();
                const editor = (row.dataset.editor || '').toLowerCase();
                
                // Check if search term matches any field
                const matches = 
                    collection.includes(searchTerm) ||
                    locale.includes(searchTerm) ||
                    id.includes(searchTerm) ||
                    filename.includes(searchTerm) ||
                    date.includes(searchTerm) ||
                    editor.includes(searchTerm);
                
                // Also respect collection filter if active
                const collectionMatch = !currentCollection || row.dataset.collection === currentCollection;
                
                row.style.display = (matches && collectionMatch) ? '' : 'none';
            });
        }
        
        // Initialize - show all files by default
        window.addEventListener('DOMContentLoaded', () => {
            // All files are shown by default (active button is "Всі")
        });
    </script>
</body>
</html>`;
  
  await fs.writeFile(path.join(REPORTS_DIR, 'changes-report.html'), html, 'utf8');
}

// Run if called directly
if (require.main === module) {
  trackChanges().catch(console.error);
}

module.exports = { trackChanges, generateHtmlReport, loadActiveSessions };

