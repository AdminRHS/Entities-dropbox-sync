const { updateEntity } = require('./strapi-entity-update-base');
const path = require('path');

// Entity для оновлення
const ENTITY_TYPE = { name: 'Home', endpoint: 'home-page' };
const SCRIPT_NAME = path.basename(__filename);

// Запускаємо оновлення
updateEntity(ENTITY_TYPE, SCRIPT_NAME).catch(error => {
  console.error(`\n❌ Критична помилка: ${error.message}`);
  console.error(error.stack);
  process.exit(1);
});

