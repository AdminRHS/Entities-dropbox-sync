const axios = require('axios');

/**
 * Нормалізація медіа полів для Strapi API
 * Перетворює формат { data: [{ id: X, attributes: {...} }] } на [X, Y, Z] для масивів
 * Перетворює формат { data: { id: X, attributes: {...} } } на X для одиночних полів
 * @param {any} value - Значення поля
 * @returns {any} Нормалізоване значення
 */
function normalizeMediaField(value) {
  // Якщо це об'єкт з data масивом (формат з експорту Strapi для масивів медіа)
  if (value && typeof value === 'object' && value.data && Array.isArray(value.data)) {
    // Витягуємо ID з кожного елемента
    const ids = value.data
      .map(item => {
        if (typeof item === 'object' && item !== null) {
          return item.id;
        }
        return item;
      })
      .filter(id => id != null);
    return ids.length > 0 ? ids : null;
  }
  
  // Якщо це об'єкт з data об'єктом (формат з експорту Strapi для одиночних медіа полів)
  if (value && typeof value === 'object' && value.data && typeof value.data === 'object' && value.data.id) {
    return value.data.id;
  }
  
  // Якщо це вже масив ID - залишаємо як є
  if (Array.isArray(value)) {
    return value;
  }
  
  // Якщо це об'єкт з одним id (без data обгортки)
  if (value && typeof value === 'object' && value.id && !value.data) {
    return value.id;
  }
  
  // Якщо це connect формат
  if (value && typeof value === 'object' && value.connect && Array.isArray(value.connect)) {
    const ids = value.connect
      .map(item => item.id || item)
      .filter(id => id != null);
    return ids.length > 0 ? ids : null;
  }
  
  return value;
}

/**
 * Нормалізація даних для порівняння (видаляє системні поля)
 * @param {any} data - Дані для нормалізації
 * @returns {any} Нормалізовані дані
 */
function normalizeForComparison(data) {
  if (Array.isArray(data)) {
    return data.map(item => normalizeForComparison(item));
  }
  
  if (typeof data === 'object' && data !== null) {
    const normalized = {};
    for (const key in data) {
      // Виключаємо системні поля Strapi
      if (key === 'id' || key === 'createdAt' || key === 'updatedAt' || 
          key === '__component' || key === '__v' || key === 'documentId') {
        continue;
      }
      normalized[key] = normalizeForComparison(data[key]);
    }
    return normalized;
  }
  
  return data;
}

/**
 * Логування спроби оновлення
 * @param {Function} logAction - Функція логування
 * @param {number} attemptNumber - Номер спроби
 * @param {string} method - HTTP метод
 * @param {string} url - URL
 * @param {string} endpoint - Endpoint
 */
function logAttempt(logAction, attemptNumber, method, url, endpoint) {
  const urlType = url.includes('single-types') ? 'single-types' : 'standard';
  logAction(`   🔄 Спроба ${attemptNumber}: ${method} ${urlType}`, 'info');
}

/**
 * Оновлення single type через Strapi API з множинними спробами
 * Винесена логіка спроб різних комбінацій методів, URL та body форматів
 * 
 * @param {string} endpoint - API endpoint
 * @param {string} locale - Локаль
 * @param {Object} data - Дані для оновлення
 * @param {string} token - API токен
 * @param {string} strapiUrl - Strapi URL
 * @param {Object} currentData - Поточні дані з GET запиту (опціонально)
 * @param {Function} logAction - Функція логування
 * @param {number} maxAttempts - Максимальна кількість спроб (за замовчуванням 12)
 * @returns {Promise<Object>} { success: boolean, message: string, response?: Object, status?: number, errorDetails?: any }
 */
async function updateSingleTypeWithRetry(
  endpoint,
  locale,
  data,
  token,
  strapiUrl,
  currentData = null,
  logAction,
  maxAttempts = 12
) {
  // Спробуємо різні формати URL для Strapi
  // Стандартний API працював раніше, тому використовуємо його першим
  // Content Manager API повертає 405, тому не використовуємо його
  const urlFormats = [
    `${strapiUrl}/api/${endpoint}`,                    // Стандартний формат (працював раніше)
    `${strapiUrl}/api/single-types/${endpoint}`       // Альтернативний формат для single types
  ];
  
  // Базовий конфіг
  const baseRequestConfig = {
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    params: {
      'locale': locale,
      'populate': '*' // Додаємо populate для правильної обробки даних
    }
  };
  
  // Різні варіанти конфігів (спрощено до найбільш ймовірних)
  // Для Content Manager API може знадобитися інший формат параметрів
  const requestConfigs = [
    baseRequestConfig,  // Базовий з populate
    { ...baseRequestConfig, params: { ...baseRequestConfig.params, 'publicationState': 'live' } },
    { ...baseRequestConfig, params: { ...baseRequestConfig.params, 'populate': 'deep' } }, // Глибокий populate
    { ...baseRequestConfig, params: { locale: locale, 'publicationState': 'live', 'populate': '*' } }, // Комбінація
    // Для Content Manager API з i18n плагіном
    { ...baseRequestConfig, params: { 'plugins[i18n][locale]': locale, 'populate': '*' } }
  ];
  
  // Спробуємо різні формати body (завжди з обгорткою data)
  const bodyFormats = [];
  
  // ВИКОРИСТОВУЄМО ТІЛЬКИ ДАНІ З ФАЙЛУ - це гарантує, що всі поля з файлу будуть відправлені
  // Починаємо з даних з файлу, а не з даних Strapi
  const dataToSend = { ...data };
  
  // Нормалізуємо медіа поля (перетворюємо { data: [{ id: X }] } на [X, Y, Z] або { data: { id: X } } на X)
  // Це потрібно для полів типу partnersSlider, mainCat, vacancyCat, videoCat тощо
  for (const key in dataToSend) {
    const value = dataToSend[key];
    // Перевіряємо чи це медіа поле (має структуру { data: [...] } або { data: { id: X } })
    if (value && typeof value === 'object' && value.data) {
      const normalized = normalizeMediaField(value);
      if (normalized !== null && normalized !== value) {
        dataToSend[key] = normalized;
        const displayValue = Array.isArray(normalized) 
          ? `${normalized.length} елементів` 
          : `ID: ${normalized}`;
        logAction(`   🖼️  Нормалізовано медіа поле ${key}: ${displayValue}`, 'info');
      }
    }
  }
  
  // Логуємо кількість полів, які відправляються
  const fieldsCount = Object.keys(dataToSend).length;
  logAction(`   📤 Підготовлено ${fieldsCount} полів для відправки`, 'info');
  
  // Обробка publishedAt для публікації
  // Якщо publishedAt є в файлі АБО дані вже опубліковані в Strapi, 
  // ЗАВЖДИ оновлюємо publishedAt на поточний час
  // Це потрібно для того, щоб Strapi розпізнав оновлення як нову публікацію
  // і фронтенд отримав оновлені дані
  // ВАЖЛИВО: Навіть якщо publishedAt є в файлі, ми його перезаписуємо новим часом
  // для опублікованих даних, щоб гарантувати оновлення на сайті
  const isPublishedInStrapi = currentData && currentData.data && currentData.data.publishedAt;
  const hasPublishedAtInFile = dataToSend.publishedAt;
  
  if (isPublishedInStrapi || hasPublishedAtInFile) {
    // Дані вже опубліковані (в Strapi або в файлі) - ЗАВЖДИ оновлюємо publishedAt на поточний час
    // Це гарантує, що Strapi розпізнає це як нову публікацію
    const newPublishedAt = new Date().toISOString();
    dataToSend.publishedAt = newPublishedAt;
    logAction(`   📅 Оновлено publishedAt для нової публікації: ${newPublishedAt}`, 'info');
  } else {
    // Дані не опубліковані і publishedAt немає в файлі - не додаємо його
    // (буде опубліковано пізніше через автоматичну публікацію)
  }
  
  // Strapi v4 ВИМАГАЄ формат { data: { attributes: {...} } } для оновлення
  // Але для title працює краще формат БЕЗ attributes обгортки
  // Тому спробуємо спочатку формат без attributes, потім з attributes
  
  // Формат 1: дані БЕЗ обгортки attributes (працює для title!)
  bodyFormats.push({
    data: dataToSend
  });
  
  // Формат 2: дані з attributes обгорткою (обов'язковий для Strapi v4)
  bodyFormats.push({
    data: {
      attributes: dataToSend
    }
  });
  
  // Формат 3: дані з attributes + publishedAt (якщо потрібно для публікації)
  if (currentData && currentData.data && currentData.data.publishedAt && !data.publishedAt) {
    bodyFormats.push({
      data: {
        attributes: {
          ...dataToSend,
          publishedAt: currentData.data.publishedAt
        }
      }
    });
  }
  
  // Формат 4: дані з attributes + новий publishedAt (для публікації)
  // Додаємо новий publishedAt якщо його немає - це опублікує дані
  if (!dataToSend.publishedAt) {
    bodyFormats.push({
      data: {
        attributes: {
          ...dataToSend,
          publishedAt: new Date().toISOString()
        }
      }
    });
  }
  
  // Формат 5: дані з attributes + id (можливо потрібен id для оновлення)
  if (currentData && currentData.data && currentData.data.id) {
    bodyFormats.push({
      data: {
        id: currentData.data.id,
        attributes: dataToSend
      }
    });
  }
  
  // Спробуємо різні методи HTTP в порядку пріоритету
  // Для single types можливо потрібен POST замість PUT
  const methods = [
    { method: 'PUT', name: 'PUT' },
    { method: 'POST', name: 'POST' },
    { method: 'PATCH', name: 'PATCH' }
  ];
  
  // Пробуємо кожну комбінацію URL + config + метод + body формат
  let attemptNumber = 0;
  let lastError = null;
  
  for (let urlIndex = 0; urlIndex < urlFormats.length && attemptNumber < maxAttempts; urlIndex++) {
    const url = urlFormats[urlIndex];
    const isLastUrl = urlIndex === urlFormats.length - 1;
    
    for (let configIndex = 0; configIndex < requestConfigs.length && attemptNumber < maxAttempts; configIndex++) {
      const requestConfig = requestConfigs[configIndex];
      const isLastConfig = configIndex === requestConfigs.length - 1;
      
      for (let bodyIndex = 0; bodyIndex < bodyFormats.length && attemptNumber < maxAttempts; bodyIndex++) {
        const requestBody = bodyFormats[bodyIndex];
        const isLastBody = bodyIndex === bodyFormats.length - 1;
        
        for (let methodIndex = 0; methodIndex < methods.length && attemptNumber < maxAttempts; methodIndex++) {
          const { method, name } = methods[methodIndex];
          const isLastMethod = methodIndex === methods.length - 1;
          const isLastAttempt = isLastUrl && isLastConfig && isLastBody && isLastMethod;
          
          attemptNumber++;
          
          // Використовуємо стандартний формат (Content Manager API не працює)
          let finalRequestBody = requestBody;
          
          try {
            let response;
            
            if (method === 'PUT') {
              response = await axios.put(url, finalRequestBody, requestConfig);
            } else if (method === 'PATCH') {
              response = await axios.patch(url, finalRequestBody, requestConfig);
            } else if (method === 'POST') {
              response = await axios.post(url, finalRequestBody, requestConfig);
            }
            
            logAction(`   ✅ Успіх на спробі ${attemptNumber} (${name}, ${url.includes('single-types') ? 'single-types' : 'standard'})`, 'success');
            
            // Перевіряємо title в відповіді (тільки якщо є проблема)
            if (response.data && response.data.data && response.data.data.attributes && response.data.data.attributes.title) {
              if (dataToSend.title && response.data.data.attributes.title !== dataToSend.title) {
                logAction(`   ⚠️  title не зберігся, спроба окремого оновлення...`, 'warning');
                await new Promise(resolve => setTimeout(resolve, 500));
                
                try {
                  // Спробуємо різні формати для title
                  const titleFormats = [
                    { data: { attributes: { title: dataToSend.title } } },
                    { data: { title: dataToSend.title } },
                    { title: dataToSend.title }
                  ];
                  
                  let titleUpdated = false;
                  for (let titleFormatIndex = 0; titleFormatIndex < titleFormats.length && !titleUpdated; titleFormatIndex++) {
                    const titleBody = titleFormats[titleFormatIndex];
                    
                    try {
                      const titleResponse = await axios.put(url, titleBody, requestConfig);
                      if (titleResponse.data && titleResponse.data.data && titleResponse.data.data.attributes) {
                        const newTitle = titleResponse.data.data.attributes.title;
                        
                        if (newTitle === dataToSend.title) {
                          logAction(`   ✅ title оновлено успішно`, 'success');
                          titleUpdated = true;
                          // Тепер оновлюємо всі інші поля
                          const otherFields = { ...dataToSend };
                          delete otherFields.title;
                          if (Object.keys(otherFields).length > 0) {
                            const otherFieldsBody = {
                              data: {
                                attributes: otherFields
                              }
                            };
                            await axios.put(url, otherFieldsBody, requestConfig);
                          }
                          // Оновлюємо response для подальшої обробки
                          response = titleResponse;
                        }
                      }
                    } catch (titleFormatError) {
                      // Ігноруємо помилки окремих форматів
                    }
                  }
                  
                  if (!titleUpdated) {
                    logAction(`   ❌ Не вдалося оновити title`, 'error');
                  }
                } catch (titleError) {
                  logAction(`   ⚠️  Помилка оновлення title: ${titleError.message}`, 'warning');
                }
              }
            }
            
            // Перевіряємо чи дані дійсно збереглися - робимо GET запит
            // Додаємо невелику затримку щоб Strapi встиг зберегти дані
            await new Promise(resolve => setTimeout(resolve, 500));
            
            try {
              // Перевіряємо published дані (publicationState: 'live')
              const verifyResponse = await axios.get(url, {
                headers: {
                  'Authorization': `Bearer ${token}`,
                  'Content-Type': 'application/json'
                },
                params: {
                  'locale': locale,
                  'populate': '*',
                  'publicationState': 'live' // Перевіряємо тільки published дані
                }
              });
              
              // Також перевіряємо draft дані для порівняння
              let draftResponse = null;
              try {
                draftResponse = await axios.get(url, {
                  headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                  },
                  params: {
                    'locale': locale,
                    'populate': '*',
                    'publicationState': 'preview' // Отримуємо draft дані
                  }
                });
              } catch (draftError) {
                // Ігноруємо помилки при отриманні draft даних
              }
              
              if (verifyResponse.data && verifyResponse.data.data) {
                // Дані в Strapi зберігаються в attributes
                const verifiedData = verifyResponse.data.data.attributes || verifyResponse.data.data;
                const verifiedFields = Object.keys(verifiedData).length;
                
                // Перевіряємо чи дані опубліковані
                const isPublished = verifiedData.publishedAt !== null && verifiedData.publishedAt !== undefined;
                const publicationStatus = isPublished ? 'опубліковано' : 'draft';
                logAction(`   ✅ Перевірка: в Strapi збережено ${verifiedFields} полів (статус: ${publicationStatus})`, 'success');
                
                // Якщо є draft дані - порівнюємо
                if (draftResponse && draftResponse.data && draftResponse.data.data) {
                  const draftData = draftResponse.data.data.attributes || draftResponse.data.data;
                  const draftIsPublished = draftData.publishedAt !== null && draftData.publishedAt !== undefined;
                  if (!draftIsPublished && isPublished) {
                    logAction(`   ⚠️  УВАГА: Published дані відрізняються від draft!`, 'warning');
                  }
                }
                
                // Отримуємо дані які були відправлені (може бути в data або data.attributes)
                let sentData = requestBody.data || {};
                if (sentData.attributes) {
                  sentData = sentData.attributes;
                }
                
                
                // Перевіряємо ВСІ поля які були відправлені
                const sentFields = Object.keys(sentData).filter(key => 
                  key !== 'publishedAt' && 
                  key !== 'localizations'
                );
                
                const mismatchedFields = [];
                const missingFields = [];
                
                sentFields.forEach(field => {
                  const sentValue = sentData[field];
                  const verifiedValue = verifiedData[field];
                  
                  // Перевіряємо чи поле взагалі існує
                  if (verifiedValue === undefined && sentValue !== undefined && sentValue !== null) {
                    missingFields.push(field);
                    return;
                  }
                  
                  // Для масивів та об'єктів нормалізуємо та порівнюємо JSON
                  if (Array.isArray(sentValue) || (typeof sentValue === 'object' && sentValue !== null)) {
                    // Нормалізуємо дані (видаляємо системні поля Strapi)
                    const normalizedSent = normalizeForComparison(sentValue);
                    const normalizedVerified = normalizeForComparison(verifiedValue || null);
                    
                    const sentJson = JSON.stringify(normalizedSent);
                    const verifiedJson = JSON.stringify(normalizedVerified);
                    if (sentJson !== verifiedJson) {
                      mismatchedFields.push(field);
                    }
                  } else if (String(sentValue) !== String(verifiedValue)) {
                    mismatchedFields.push(field);
                  }
                });
                
                if (mismatchedFields.length > 0) {
                  // Для компонентів (як languagesList) це може бути нормально, якщо Strapi додав системні поля
                  const componentFields = mismatchedFields.filter(f => 
                    Array.isArray(sentData[f]) || (typeof sentData[f] === 'object' && sentData[f] !== null)
                  );
                  if (componentFields.length > 0) {
                    logAction(`   ⚠️  Поля-компоненти мають відмінності (можливо, системні поля Strapi): ${componentFields.join(', ')}`, 'warning');
                    logAction(`   ℹ️  Якщо основні дані відображаються правильно на сайті, це нормально`, 'info');
                  }
                  const otherFields = mismatchedFields.filter(f => !componentFields.includes(f));
                  if (otherFields.length > 0) {
                    logAction(`   ❌ Поля не збереглися правильно: ${otherFields.join(', ')}`, 'error');
                  }
                } else if (missingFields.length > 0) {
                  logAction(`   ⚠️  Поля відсутні в Strapi: ${missingFields.join(', ')}`, 'warning');
                } else {
                  logAction(`   ✅ Всі поля збережені успішно`, 'success');
                }
                
                // Якщо дані не опубліковані - спробуємо опублікувати
                if (!isPublished) {
                  logAction(`   ⚠️  Дані збережені в draft стані. Спроба публікації...`, 'warning');
                  try {
                    // Спробуємо опублікувати через PUT з publishedAt
                    const publishBody = {
                      data: {
                        attributes: {
                          ...sentData,
                          publishedAt: new Date().toISOString()
                        }
                      }
                    };
                    await axios.put(url, publishBody, {
                      ...requestConfig,
                      params: {
                        ...requestConfig.params,
                        'publicationState': 'live'
                      }
                    });
                    logAction(`   ✅ Дані опубліковано`, 'success');
                  } catch (publishError) {
                    logAction(`   ⚠️  Не вдалося опублікувати: ${publishError.message}`, 'warning');
                  }
                }
              }
            } catch (verifyError) {
              logAction(`   ⚠️  Не вдалося перевірити збережені дані: ${verifyError.message}`, 'warning');
            }
            
            return {
              success: true,
              message: `Оновлено успішно (через ${name}, URL: ${url.includes('single-types') ? 'single-types' : 'standard'})`,
              response: response.data
            };
          } catch (error) {
            lastError = error;
            
            if (error.response) {
              const status = error.response.status;
              const errorData = error.response.data?.error || error.response.data;
              
              // Логуємо кожну невдалу спробу
              let errorMsg = `HTTP ${status}`;
              if (errorData) {
                if (typeof errorData === 'object') {
                  errorMsg += `: ${JSON.stringify(errorData).substring(0, 100)}`;
                } else {
                  errorMsg += `: ${errorData.substring(0, 100)}`;
                }
              }
              logAction(`   ❌ Спроба ${attemptNumber} не вдалася: ${errorMsg}`, 'warning');
              
              // Якщо помилка 400, 405 або 500, пробуємо наступну комбінацію
              if (status === 400 || status === 405 || status === 500) {
                // Якщо це остання спроба або досягнуто максимум, повертаємо помилку
                if (isLastAttempt || attemptNumber >= maxAttempts) {
                  let errorMessage = `API Error (${status})`;
                  if (errorData) {
                    if (typeof errorData === 'object') {
                      errorMessage += `: ${JSON.stringify(errorData)}`;
                    } else {
                      errorMessage += `: ${errorData}`;
                    }
                  }
                  
                  if (status === 405) {
                    errorMessage += ` | Всі методи (PUT, PATCH), формати URL та body не підтримуються для ${endpoint}. Можливо, цей single type не можна оновлювати через API або потрібні інші права доступу.`;
                  } else if (status === 500) {
                    errorMessage += ` | Можливі причини: неправильна структура даних, відсутні обов'язкові поля, або помилка на сервері Strapi`;
                  }
                  
                  return {
                    success: false,
                    message: errorMessage,
                    status: status,
                    errorDetails: errorData
                  };
                }
                // Інакше продовжуємо спробувати наступну комбінацію
                continue;
              }
              
              // Для інших помилок (не 400/405/500) повертаємо одразу
              let errorMessage = `API Error (${status})`;
              if (errorData) {
                if (typeof errorData === 'object') {
                  errorMessage += `: ${JSON.stringify(errorData)}`;
                } else {
                  errorMessage += `: ${errorData}`;
                }
              }
              
              return {
                success: false,
                message: errorMessage,
                status: status,
                errorDetails: errorData
              };
            } else {
              // Network error - пробуємо наступну спробу, якщо не остання
              logAction(`   ⚠️  Спроба ${attemptNumber} не вдалася: Network Error: ${error.message}`, 'warning');
              
              if (isLastAttempt || attemptNumber >= maxAttempts) {
                return {
                  success: false,
                  message: `Network Error: ${error.message}`
                };
              }
              continue;
            }
          }
        }
      }
    }
  }
  
  // Fallback (не повинно дійти сюди, але на всяк випадок)
  const finalError = lastError 
    ? `Остання помилка: ${lastError.message}` 
    : 'Невідома помилка';
  
  return {
    success: false,
    message: `Всі комбінації URL, config, body та методів HTTP не спрацювали. ${finalError}`
  };
}

module.exports = {
  updateSingleTypeWithRetry
};

