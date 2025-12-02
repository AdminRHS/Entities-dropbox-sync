const fs = require('fs').promises;
const path = require('path');

// Load the generateHtmlReport function
const trackChangesPath = path.join(__dirname, 'track-changes.js');
delete require.cache[require.resolve(trackChangesPath)];
const trackChangesModule = require(trackChangesPath);

// Create empty status and tracker
const emptyStatus = {
  files: [],
  summary: {
    total: 0,
    modified: 0,
    created: 0,
    deleted: 0,
    unchanged: 0
  },
  collectionStats: {},
  changedFiles: [],
  lastUpdate: new Date().toISOString()
};

const emptyTracker = {
  changes: [],
  lastUpdate: new Date().toISOString()
};

// Generate HTML report
(async () => {
  try {
    await trackChangesModule.generateHtmlReport(emptyStatus, emptyTracker);
    console.log('✅ Порожній звіт згенеровано!');
  } catch (error) {
    console.error('❌ Помилка:', error.message);
    process.exit(1);
  }
})();


