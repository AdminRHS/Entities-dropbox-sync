const fs = require('fs').promises;
const path = require('path');
const os = require('os');
const readline = require('readline');

// Configuration
const REPORTS_DIR = path.join(__dirname, '..', 'reports');
const SESSIONS_FILE = path.join(REPORTS_DIR, 'active-sessions.json');
const USER_PROFILE_FILE = path.join(REPORTS_DIR, 'user-profiles.json');

/**
 * Create readline interface
 */
function createInterface() {
  return readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });
}

/**
 * Question helper
 */
function question(rl, query) {
  return new Promise(resolve => rl.question(query, resolve));
}

/**
 * Load active sessions
 */
async function loadSessions() {
  try {
    const data = await fs.readFile(SESSIONS_FILE, 'utf8');
    return JSON.parse(data);
  } catch {
    return { sessions: [] };
  }
}

/**
 * Load user profiles
 */
async function loadUserProfiles() {
  try {
    const data = await fs.readFile(USER_PROFILE_FILE, 'utf8');
    return JSON.parse(data);
  } catch {
    return { users: [] };
  }
}

/**
 * Save sessions
 */
async function saveSessions(sessions) {
  await fs.mkdir(REPORTS_DIR, { recursive: true });
  await fs.writeFile(SESSIONS_FILE, JSON.stringify(sessions, null, 2), 'utf8');
}

/**
 * Save user profiles
 */
async function saveUserProfiles(profiles) {
  await fs.mkdir(REPORTS_DIR, { recursive: true });
  await fs.writeFile(USER_PROFILE_FILE, JSON.stringify(profiles, null, 2), 'utf8');
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
 * Find existing user profile
 */
function findUserProfile(profiles, username, hostname) {
  return profiles.users.find(u => 
    u.username === username && u.hostname === hostname
  );
}

/**
 * Check if user has active session
 */
function hasActiveSession(sessions, username, hostname) {
  const now = Date.now();
  return sessions.sessions.some(s => 
    s.username === username && 
    s.hostname === hostname &&
    s.status === 'active' &&
    (now - new Date(s.startedAt).getTime()) < (s.duration || 4 * 60 * 60 * 1000) // 4 hours default
  );
}

/**
 * End old sessions
 */
function endOldSessions(sessions) {
  const now = Date.now();
  sessions.sessions = sessions.sessions.map(s => {
    if (s.status === 'active') {
      const sessionAge = now - new Date(s.startedAt).getTime();
      const maxDuration = s.duration || 4 * 60 * 60 * 1000; // 4 hours
      
      if (sessionAge > maxDuration) {
        return {
          ...s,
          status: 'ended',
          endedAt: new Date().toISOString()
        };
      }
    }
    return s;
  });
}

/**
 * Register new session
 */
async function registerSession(userData = null) {
  const rl = userData ? null : createInterface();
  
  try {
    const systemUser = getCurrentUser();
    const sessions = await loadSessions();
    const profiles = await loadUserProfiles();
    
    // End old sessions
    endOldSessions(sessions);
    await saveSessions(sessions);
    
    // Check if user already has active session
    if (hasActiveSession(sessions, systemUser.username, systemUser.hostname)) {
      console.log('\n✅ У вас вже є активна сесія!\n');
      if (rl) rl.close();
      return;
    }
    
    // Find or create user profile
    let userProfile = findUserProfile(profiles, systemUser.username, systemUser.hostname);
    
    let name, role, plannedWork, currentWork, estimatedDuration;
    
    if (userData) {
      // Use provided data
      name = userData.name;
      role = userData.role;
      plannedWork = userData.plannedWork;
      currentWork = userData.currentWork;
      estimatedDuration = userData.estimatedDuration || '4';
    } else {
      // Interactive mode
      if (!userProfile) {
        console.log('\n👋 Вітаємо! Це ваш перший раз тут.\n');
        console.log('Будь ласка, заповніть коротку форму:\n');
        
        name = await question(rl, 'Ваше ім\'я: ');
        role = await question(rl, 'Ваша посада/роль (наприклад: рекрутер, контент-менеджер): ');
        plannedWork = await question(rl, 'Чим ви плануєте займатись? (наприклад: оновлення вакансій, створення нових): ');
      }
      
      currentWork = await question(rl, 'Що ви плануєте робити зараз? (наприклад: оновити вакансію Front-end розробник): ');
      estimatedDuration = await question(rl, 'Орієнтовна тривалість роботи (години, за замовчуванням 4): ') || '4';
    }
    
    if (!userProfile) {
      userProfile = {
        username: systemUser.username,
        hostname: systemUser.hostname,
        name: name || systemUser.username,
        role: role || 'Користувач',
        plannedWork: plannedWork || 'Робота з колекціями',
        firstSeen: new Date().toISOString(),
        lastSeen: new Date().toISOString()
      };
      
      profiles.users.push(userProfile);
      await saveUserProfiles(profiles);
      
      if (!userData) {
        console.log('\n✅ Профіль створено!\n');
      }
    } else {
      // Update last seen
      userProfile.lastSeen = new Date().toISOString();
      await saveUserProfiles(profiles);
      
      if (!userData) {
        console.log(`\n👋 Вітаємо, ${userProfile.name}!\n`);
      }
    }
    
    // Create new session (duration defaults to 4 hours if not provided)
    const durationHours = estimatedDuration ? parseInt(estimatedDuration) : 4;
    // If currentWork not provided, use plannedWork
    const workDescription = currentWork || plannedWork || 'Робота з колекціями';
    const session = {
      id: `session-${Date.now()}`,
      username: systemUser.username,
      hostname: systemUser.hostname,
      name: userProfile.name,
      role: userProfile.role,
      currentWork: workDescription,
      startedAt: new Date().toISOString(),
      estimatedEnd: new Date(Date.now() + durationHours * 60 * 60 * 1000).toISOString(),
      duration: durationHours * 60 * 60 * 1000,
      status: 'active'
    };
    
    sessions.sessions.push(session);
    await saveSessions(sessions);
    
    if (!userData) {
      console.log('\n✅ Сесія зареєстрована!\n');
      console.log(`📋 Ваша поточна робота: ${session.currentWork}`);
      console.log(`⏰ Орієнтовне завершення: ${new Date(session.estimatedEnd).toLocaleString('uk-UA')}\n`);
      console.log('💡 Після завершення роботи запустіть: node scripts/register-session.js end\n');
    }
    
    return session;
    
  } finally {
    if (rl) rl.close();
  }
}

/**
 * End current session
 */
async function endSession() {
  const systemUser = getCurrentUser();
  const sessions = await loadSessions();
  
  const activeSession = sessions.sessions.find(s => 
    s.username === systemUser.username && 
    s.hostname === systemUser.hostname &&
    s.status === 'active'
  );
  
  if (!activeSession) {
    console.log('\n⚠️  Активна сесія не знайдена.\n');
    return;
  }
  
  activeSession.status = 'ended';
  activeSession.endedAt = new Date().toISOString();
  activeSession.actualDuration = Date.now() - new Date(activeSession.startedAt).getTime();
  
  await saveSessions(sessions);
  
  console.log('\n✅ Сесія завершена!\n');
  console.log(`📋 Робота: ${activeSession.currentWork}`);
  console.log(`⏱️  Тривалість: ${Math.round(activeSession.actualDuration / 60000)} хвилин\n`);
}

// Run based on command
if (require.main === module) {
  const command = process.argv[2];
  
  if (command === 'end') {
    endSession().catch(console.error);
  } else {
    registerSession().catch(console.error);
  }
}

module.exports = { registerSession, endSession, loadSessions, loadUserProfiles };

