const fs = require('fs').promises;
const path = require('path');

// Configuration
const EXPORTED_DIR = path.join(__dirname, '..', 'exported');
const UPDATED_DIR = path.join(__dirname, '..', 'updated');

/**
 * Copy directory structure (without files)
 */
async function copyDirectoryStructure(sourceDir, targetDir) {
  try {
    // Create target directory if it doesn't exist
    await fs.mkdir(targetDir, { recursive: true });
    
    // Read source directory
    const entries = await fs.readdir(sourceDir, { withFileTypes: true });
    
    for (const entry of entries) {
      const sourcePath = path.join(sourceDir, entry.name);
      const targetPath = path.join(targetDir, entry.name);
      
      if (entry.isDirectory()) {
        // Recursively copy directory structure
        await copyDirectoryStructure(sourcePath, targetPath);
        console.log(`   ✓ Створено: ${path.relative(UPDATED_DIR, targetPath)}`);
      }
      // Skip files - we only copy structure
    }
  } catch (error) {
    if (error.code !== 'ENOENT') {
      throw error;
    }
  }
}

/**
 * Main function
 */
async function setupUpdatedStructure() {
  console.log('🚀 Створення структури папок для updated...\n');
  console.log(`📁 Джерело: ${EXPORTED_DIR}`);
  console.log(`📁 Призначення: ${UPDATED_DIR}\n`);
  
  try {
    // Copy collections structure
    const exportedCollections = path.join(EXPORTED_DIR, 'collections');
    const updatedCollections = path.join(UPDATED_DIR, 'collections');
    
    console.log('📂 Копіювання структури collections...\n');
    await copyDirectoryStructure(exportedCollections, updatedCollections);
    
    // Copy pages structure if exists
    const exportedPages = path.join(EXPORTED_DIR, 'pages');
    const updatedPages = path.join(UPDATED_DIR, 'pages');
    
    try {
      await fs.access(exportedPages);
      console.log('\n📂 Копіювання структури pages...\n');
      await copyDirectoryStructure(exportedPages, updatedPages);
    } catch {
      // Pages directory doesn't exist, skip
    }
    
    console.log('\n✅ Структура папок створена успішно!\n');
    console.log(`📁 Перевірте папку: ${UPDATED_DIR}\n`);
    
  } catch (error) {
    console.error('\n❌ Помилка:', error.message);
    process.exit(1);
  }
}

// Run setup
setupUpdatedStructure();

