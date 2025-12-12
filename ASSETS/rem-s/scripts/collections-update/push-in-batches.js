// Load environment variables from .env file
require('dotenv').config({ path: require('path').join(__dirname, '..', '..', '.env') });

const axios = require('axios');
const fs = require('fs').promises;
const path = require('path');

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function findAllVacancies(dir) {
  let files = [];
  const items = await fs.readdir(dir, { withFileTypes: true });
  
  for (const item of items) {
    const fullPath = path.join(dir, item.name);
    if (item.isDirectory()) {
      const subFiles = await findAllVacancies(fullPath);
      files = files.concat(subFiles);
    } else if (item.name.endsWith('.json') && !item.name.includes('list')) {
      files.push(fullPath);
    }
  }
  
  return files;
}

async function pushBatch(files, batchNum, totalBatches) {
  console.log(`\n📦 Батч ${batchNum}/${totalBatches} (${files.length} файлів)...\n`);
  
  const token = process.env.STRAPI_TOKEN;
  if (!token) {
    console.error('❌ Помилка: STRAPI_TOKEN не знайдено в .env файлі');
    process.exit(1);
  }
  
  let success = 0;
  let failed = 0;
  
  for (const file of files) {
    try {
      const content = await fs.readFile(file, 'utf8');
      const data = JSON.parse(content);
      const fileName = path.basename(file);
      
      // ⚠️ КРИТИЧНО: Видаляємо компоненти, які викликають помилки
      const cleanData = { ...data.attributes };
      delete cleanData.responsibilities;
      delete cleanData.products;
      delete cleanData.tools;
      delete cleanData.seoData;
      delete cleanData.videoPreview;
      delete cleanData.localizations;
      
      // Перевірка формату categories (має бути число, не масив)
      if (Array.isArray(cleanData.categories) && cleanData.categories.length > 0) {
        cleanData.categories = cleanData.categories[0];
      }
      
      await axios.put(
        `https://strapi.rem-s.com/api/vacancies/${data.id}`,
        { data: cleanData },
        {
          headers: { 'Authorization': `Bearer ${token}` },
          params: { locale: data.attributes.locale }
        }
      );
      
      console.log(`  ✅ ${fileName}`);
      success++;
      await sleep(300); // Пауза між запитами
    } catch (e) {
      console.log(`  ❌ ${path.basename(file)} - ${e.response?.status || e.message}`);
      if (e.response?.data) {
        console.log(`     Деталі: ${JSON.stringify(e.response.data).substring(0, 100)}`);
      }
      failed++;
    }
  }
  
  console.log(`\n   ✅ Успішно: ${success}`);
  if (failed > 0) console.log(`   ❌ Помилок: ${failed}`);
  
  return { success, failed };
}

async function main() {
  const vacanciesDir = path.join(__dirname, '..', '..', 'updated', 'collections', 'vacancies', 'languages');
  
  console.log('🔍 Шукаю вакансії...');
  const allFiles = await findAllVacancies(vacanciesDir);
  
  console.log(`🚀 Знайдено ${allFiles.length} вакансій для відправки\n`);
  
  if (allFiles.length === 0) {
    console.log('⚠️  Файлів не знайдено. Перевірте шлях до папки.');
    return;
  }
  
  const BATCH_SIZE = 10; // 10 файлів за раз
  const batches = [];
  
  for (let i = 0; i < allFiles.length; i += BATCH_SIZE) {
    batches.push(allFiles.slice(i, i + BATCH_SIZE));
  }
  
  console.log(`📊 Розділено на ${batches.length} батчів по ${BATCH_SIZE} файлів\n`);
  
  let totalSuccess = 0;
  let totalFailed = 0;
  
  for (let i = 0; i < batches.length; i++) {
    const result = await pushBatch(batches[i], i + 1, batches.length);
    totalSuccess += result.success;
    totalFailed += result.failed;
    
    if (i < batches.length - 1) {
      console.log('\n⏳ Пауза 2 секунди перед наступним батчем...');
      await sleep(2000); // Пауза між батчами
    }
  }
  
  console.log('\n' + '='.repeat(50));
  console.log(`✅ Всього успішно: ${totalSuccess}`);
  if (totalFailed > 0) console.log(`❌ Всього помилок: ${totalFailed}`);
  console.log('='.repeat(50));
}

main().catch(e => {
  console.error('❌ Помилка:', e.message);
  process.exit(1);
});













