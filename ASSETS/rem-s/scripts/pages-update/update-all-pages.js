const { exec } = require('child_process');
const { promisify } = require('util');
const path = require('path');
const fs = require('fs');

const execAsync = promisify(exec);

// Всі скрипти оновлення сторінок
const UPDATE_SCRIPTS = [
  'strapi-about-update.js',
  'strapi-contact-update.js',
  'strapi-header-update.js',
  'strapi-home-update.js',
  'strapi-not-found-update.js',
  'strapi-thank-you-update.js',
  'strapi-vacancy-list-data-update.js',
  'strapi-vacancy-page-update.js',
  'strapi-video-interview-update.js'
];

// Кольори для консолі
const colors = {
  reset: '\x1b[0m',
  bright: '\x1b[1m',
  dim: '\x1b[2m',
  red: '\x1b[31m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  cyan: '\x1b[36m'
};

/**
 * Логування з кольорами
 */
function log(message, color = 'reset') {
  console.log(`${colors[color]}${message}${colors.reset}`);
}

/**
 * Запуск одного скрипта оновлення
 */
async function runUpdateScript(scriptName, args) {
  const scriptPath = path.join(__dirname, scriptName);
  const command = `node "${scriptPath}" ${args.join(' ')}`;
  
  log(`\n${'='.repeat(80)}`, 'cyan');
  log(`🚀 Запуск: ${scriptName}`, 'bright');
  log(`${'='.repeat(80)}`, 'cyan');
  
  try {
    const { stdout, stderr } = await execAsync(command, {
      cwd: __dirname,
      maxBuffer: 10 * 1024 * 1024 // 10MB
    });
    
    if (stdout) {
      console.log(stdout);
    }
    
    if (stderr && !stderr.includes('warning')) {
      log(`⚠️  Warnings: ${stderr}`, 'yellow');
    }
    
    return { success: true, script: scriptName };
  } catch (error) {
    log(`❌ Помилка при запуску ${scriptName}:`, 'red');
    if (error.stdout) {
      console.log(error.stdout);
    }
    if (error.stderr) {
      log(error.stderr, 'red');
    }
    log(`   ${error.message}`, 'red');
    return { success: false, script: scriptName, error: error.message };
  }
}

/**
 * Головна функція
 */
async function updateAllPages() {
  const args = process.argv.slice(2);
  
  // Перевірка аргументів
  const isDryRun = args.includes('--dry-run');
  const needsConfirm = args.includes('--confirm');
  const createBackup = args.includes('--backup');
  const exportAfter = args.includes('--export-after');
  const forceFlag = args.includes('--force');
  
  // Отримуємо токен
  const tokenIndex = args.findIndex(arg => !arg.startsWith('--'));
  const token = tokenIndex !== -1 ? args[tokenIndex] : process.env.STRAPI_TOKEN;
  
  // Формуємо аргументи для передачі скриптам
  const scriptArgs = [];
  if (isDryRun) {
    scriptArgs.push('--dry-run');
  }
  if (needsConfirm) {
    scriptArgs.push('--confirm');
  }
  if (createBackup) {
    scriptArgs.push('--backup');
  }
  if (exportAfter) {
    scriptArgs.push('--export-after');
  }
  if (forceFlag) {
    scriptArgs.push('--force');
  }
  if (token) {
    scriptArgs.push(token);
  }
  
  // Заголовок
  log('\n' + '='.repeat(80), 'bright');
  log('📦 МАСОВЕ ОНОВЛЕННЯ ВСІХ СТОРІНОК', 'bright');
  log('='.repeat(80), 'bright');
  log(`📋 Знайдено ${UPDATE_SCRIPTS.length} скриптів для запуску`, 'cyan');
  log(`🔧 Режим: ${isDryRun ? 'DRY-RUN' : needsConfirm ? 'CONFIRM' : 'DRY-RUN (за замовчуванням)'}`, 'cyan');
  
  if (createBackup) {
    log(`⚠️  УВАГА: Буде створено backup для кожного скрипта!`, 'yellow');
  }
  
  if (exportAfter) {
    log(`⚠️  УВАГА: Буде виконано експорт після кожного оновлення!`, 'yellow');
  }
  
  if (!token && !isDryRun) {
    log(`\n❌ Помилка: Потрібен Strapi API токен!`, 'red');
    log(`\nВикористання:`, 'cyan');
    log(`  node update-all-pages.js --dry-run`, 'info');
    log(`  node update-all-pages.js --confirm <token>`, 'info');
    log(`  node update-all-pages.js --confirm --backup --export-after <token>`, 'info');
    process.exit(1);
  }
  
  if (needsConfirm && !isDryRun) {
    log(`\n⚠️  УВАГА: Буде виконано реальне оновлення всіх сторінок в Strapi!`, 'yellow');
    log(`   Натисніть Ctrl+C для скасування або зачекайте 5 секунд...\n`, 'yellow');
    await new Promise(resolve => setTimeout(resolve, 5000));
  }
  
  // Статистика
  const results = {
    total: UPDATE_SCRIPTS.length,
    success: 0,
    failed: 0,
    errors: []
  };
  
  const startTime = Date.now();
  
  // Запускаємо всі скрипти послідовно
  for (let i = 0; i < UPDATE_SCRIPTS.length; i++) {
    const script = UPDATE_SCRIPTS[i];
    log(`\n[${i + 1}/${UPDATE_SCRIPTS.length}] Запуск ${script}...`, 'cyan');
    
    const result = await runUpdateScript(script, scriptArgs);
    
    if (result.success) {
      results.success++;
      log(`✅ ${script} - успішно`, 'green');
    } else {
      results.failed++;
      results.errors.push({
        script: script,
        error: result.error
      });
      log(`❌ ${script} - помилка`, 'red');
    }
    
    // Затримка між скриптами (щоб не перевантажити Strapi)
    if (i < UPDATE_SCRIPTS.length - 1) {
      await new Promise(resolve => setTimeout(resolve, 1000));
    }
  }
  
  // Підсумок
  const duration = ((Date.now() - startTime) / 1000).toFixed(2);
  
  log(`\n${'='.repeat(80)}`, 'bright');
  log('📊 ПІДСУМОК', 'bright');
  log('='.repeat(80), 'bright');
  log(`✅ Успішно: ${results.success}/${results.total}`, 'green');
  log(`❌ Помилки: ${results.failed}/${results.total}`, results.failed > 0 ? 'red' : 'reset');
  log(`⏱️  Час виконання: ${duration} секунд`, 'cyan');
  
  if (results.errors.length > 0) {
    log(`\n❌ Помилки:`, 'red');
    results.errors.forEach(err => {
      log(`   - ${err.script}: ${err.error}`, 'red');
    });
  }
  
  log(`\n${'='.repeat(80)}\n`, 'bright');
  
  // Повертаємо код виходу
  process.exit(results.failed > 0 ? 1 : 0);
}

// Запускаємо
updateAllPages().catch(error => {
  log(`\n❌ Критична помилка: ${error.message}`, 'red');
  console.error(error.stack);
  process.exit(1);
});

