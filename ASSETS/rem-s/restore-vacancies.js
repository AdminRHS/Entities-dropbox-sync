const fs = require('fs').promises;
const path = require('path');

const exportedDir = path.join(__dirname, 'exported', 'collections', 'vacancies');
const updatedDir = path.join(__dirname, 'updated', 'collections', 'vacancies');

async function copyRecursive(src, dest) {
  const entries = await fs.readdir(src, { withFileTypes: true });
  
  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    
    if (entry.isDirectory()) {
      await fs.mkdir(destPath, { recursive: true });
      await copyRecursive(srcPath, destPath);
    } else {
      await fs.copyFile(srcPath, destPath);
      console.log(`✓ Скопійовано: ${path.relative(updatedDir, destPath)}`);
    }
  }
}

async function restore() {
  try {
    console.log('🔄 Відновлення вакансій з папки exported...\n');
    console.log(`📂 З: ${exportedDir}`);
    console.log(`📂 В: ${updatedDir}\n`);
    
    await copyRecursive(exportedDir, updatedDir);
    
    console.log('\n✅ Всі файли успішно відновлено!');
  } catch (error) {
    console.error('❌ Помилка:', error.message);
    process.exit(1);
  }
}

restore();






