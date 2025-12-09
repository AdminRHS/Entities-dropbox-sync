// Load environment variables from .env file
require('dotenv').config({ path: require('path').join(__dirname, '..', '..', '.env') });

const axios = require('axios');
const fs = require('fs').promises;
const path = require('path');

const STRAPI_URL = 'https://strapi.rem-s.com';

/**
 * Clean data for API - remove components that cause errors
 */
function cleanDataForApi(data) {
  const cleaned = { ...data };
  
  // Remove components that cause 500 errors
  delete cleaned.responsibilities;
  delete cleaned.products;
  delete cleaned.tools;
  delete cleaned.seoData;
  delete cleaned.videoPreview;
  delete cleaned.localizations;
  
  // Ensure categories is a number, not array
  if (Array.isArray(cleaned.categories) && cleaned.categories.length > 0) {
    cleaned.categories = cleaned.categories[0];
  }
  
  return cleaned;
}

/**
 * Update single file
 */
async function updateSingleFile(filePath) {
  try {
    const token = process.env.STRAPI_TOKEN;
    
    if (!token) {
      throw new Error('STRAPI_TOKEN не знайдено в .env файлі');
    }
    
    // Read file
    const fileContent = await fs.readFile(filePath, 'utf8');
    const fileData = JSON.parse(fileContent);
    
    const id = fileData.id;
    const attributes = fileData.attributes || fileData;
    const locale = attributes.locale;
    
    if (!id) {
      throw new Error('ID не знайдено в файлі');
    }
    
    // Clean data
    const cleanedData = cleanDataForApi(attributes);
    
    // Determine collection name from path
    let collectionName = 'vacancies'; // default
    if (filePath.includes('vacancies')) collectionName = 'vacancies';
    else if (filePath.includes('categories')) collectionName = 'categories';
    else if (filePath.includes('keyword-tags')) collectionName = 'keyword-tags';
    else if (filePath.includes('skills')) collectionName = 'skills';
    else if (filePath.includes('form-users')) collectionName = 'form-users';
    
    const url = `${STRAPI_URL}/api/${collectionName}/${id}`;
    
    const config = {
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      }
    };
    
    // Add locale if needed
    if (locale && ['vacancies', 'categories', 'keyword-tags', 'skills', 'form-users'].includes(collectionName)) {
      config.params = { locale };
    }
    
    console.log(`🚀 Відправка файлу: ${path.basename(filePath)}`);
    console.log(`📍 URL: ${url}`);
    console.log(`🌐 Locale: ${locale || 'немає'}`);
    
    // Send request
    const response = await axios.put(url, { data: cleanedData }, config);
    
    console.log(`✅ Успішно оновлено!`);
    console.log(`📊 Статус: ${response.status}`);
    
    return { success: true, response: response.data };
    
  } catch (error) {
    if (error.response) {
      console.error(`❌ Помилка API: ${error.response.status}`);
      console.error(`📄 Деталі:`, JSON.stringify(error.response.data, null, 2));
    } else {
      console.error(`❌ Помилка:`, error.message);
    }
    throw error;
  }
}

// Main
const filePath = process.argv[2];

if (!filePath) {
  console.error('❌ Вкажіть шлях до файлу: node push-single-file.js <path-to-file>');
  process.exit(1);
}

updateSingleFile(filePath)
  .then(() => {
    console.log('\n✅ Готово!');
    process.exit(0);
  })
  .catch((error) => {
    console.error('\n❌ Помилка при відправці');
    process.exit(1);
  });









