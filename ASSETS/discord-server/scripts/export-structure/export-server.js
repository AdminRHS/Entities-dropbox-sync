/**
 * Discord Server Structure Export Script
 *
 * Exports complete Discord server structure including:
 * - Categories
 * - Channels (text and voice)
 * - Roles
 * - Permissions
 *
 * Prerequisites:
 * 1. Create a Discord bot at https://discord.com/developers/applications
 * 2. Enable necessary intents (Guilds)
 * 3. Invite bot to your server with appropriate permissions
 * 4. Add DISCORD_TOKEN and DISCORD_GUILD_ID to .env file
 */

require('dotenv').config({ path: '../../.env' });
const { Client, GatewayIntentBits } = require('discord.js');
const fs = require('fs');
const path = require('path');

// Configuration
const TOKEN = process.env.DISCORD_TOKEN;
const GUILD_ID = process.env.DISCORD_GUILD_ID;
const OUTPUT_DIR = path.join(__dirname, '../../exported/current-structure');

// Validate environment variables
if (!TOKEN || !GUILD_ID) {
  console.error('❌ Error: DISCORD_TOKEN and DISCORD_GUILD_ID must be set in .env file');
  process.exit(1);
}

// Create Discord client
const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
  ]
});

/**
 * Export server structure to JSON files
 */
async function exportServerStructure(guild) {
  console.log(`\n📊 Exporting structure for: ${guild.name}`);
  console.log(`Server ID: ${guild.id}`);
  console.log(`Member count: ${guild.memberCount}\n`);

  // Fetch all channels
  const channels = await guild.channels.fetch();

  // Organize channels by category
  const categories = [];
  const channelsList = [];

  channels.forEach(channel => {
    if (channel.type === 4) { // Category
      categories.push({
        id: channel.id,
        name: channel.name,
        position: channel.position,
        channels: {
          text: 0,
          voice: 0
        }
      });
    }
  });

  // Count channels per category and build channel list
  channels.forEach(channel => {
    if (channel.type === 4) return; // Skip categories

    const categoryData = categories.find(cat => cat.id === channel.parentId);

    const channelInfo = {
      id: channel.id,
      name: channel.name,
      type: channel.type === 0 ? 'text' : channel.type === 2 ? 'voice' : 'other',
      categoryId: channel.parentId,
      categoryName: categoryData ? categoryData.name : 'No Category',
      position: channel.position
    };

    channelsList.push(channelInfo);

    // Update category counts
    if (categoryData) {
      if (channel.type === 0) categoryData.channels.text++;
      else if (channel.type === 2) categoryData.channels.voice++;
    }
  });

  // Fetch roles
  const roles = await guild.roles.fetch();
  const rolesList = roles.map(role => ({
    id: role.id,
    name: role.name,
    color: role.color,
    position: role.position,
    permissions: role.permissions.toArray()
  }));

  // Sort by position
  categories.sort((a, b) => a.position - b.position);
  channelsList.sort((a, b) => a.position - b.position);

  // Prepare export data
  const exportData = {
    serverName: guild.name,
    serverId: guild.id,
    exportDate: new Date().toISOString().split('T')[0],
    memberCount: guild.memberCount,
    categories: categories,
    channels: channelsList,
    roles: rolesList.sort((a, b) => b.position - a.position),
    summary: {
      totalCategories: categories.length,
      totalTextChannels: channelsList.filter(ch => ch.type === 'text').length,
      totalVoiceChannels: channelsList.filter(ch => ch.type === 'voice').length,
      totalChannels: channelsList.length,
      totalRoles: rolesList.length
    }
  };

  // Ensure output directory exists
  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }

  // Write files
  const categoriesFile = path.join(OUTPUT_DIR, 'categories.json');
  const channelsFile = path.join(OUTPUT_DIR, 'channels.json');
  const rolesFile = path.join(OUTPUT_DIR, 'roles.json');
  const fullExportFile = path.join(OUTPUT_DIR, 'full-export.json');

  fs.writeFileSync(categoriesFile, JSON.stringify({
    serverName: guild.name,
    exportDate: exportData.exportDate,
    categories: exportData.categories,
    summary: {
      totalCategories: exportData.summary.totalCategories
    }
  }, null, 2));

  fs.writeFileSync(channelsFile, JSON.stringify({
    serverName: guild.name,
    exportDate: exportData.exportDate,
    channels: exportData.channels,
    summary: {
      totalChannels: exportData.summary.totalChannels,
      textChannels: exportData.summary.totalTextChannels,
      voiceChannels: exportData.summary.totalVoiceChannels
    }
  }, null, 2));

  fs.writeFileSync(rolesFile, JSON.stringify({
    serverName: guild.name,
    exportDate: exportData.exportDate,
    roles: exportData.roles,
    summary: {
      totalRoles: exportData.summary.totalRoles
    }
  }, null, 2));

  fs.writeFileSync(fullExportFile, JSON.stringify(exportData, null, 2));

  console.log('✅ Export complete!\n');
  console.log('📁 Files created:');
  console.log(`   - ${path.relative(process.cwd(), categoriesFile)}`);
  console.log(`   - ${path.relative(process.cwd(), channelsFile)}`);
  console.log(`   - ${path.relative(process.cwd(), rolesFile)}`);
  console.log(`   - ${path.relative(process.cwd(), fullExportFile)}`);
  console.log('\n📊 Summary:');
  console.log(`   Categories: ${exportData.summary.totalCategories}`);
  console.log(`   Text Channels: ${exportData.summary.totalTextChannels}`);
  console.log(`   Voice Channels: ${exportData.summary.totalVoiceChannels}`);
  console.log(`   Total Channels: ${exportData.summary.totalChannels}`);
  console.log(`   Roles: ${exportData.summary.totalRoles}\n`);
}

// Bot ready event
client.once('ready', async () => {
  console.log(`\n🤖 Bot logged in as ${client.user.tag}`);

  try {
    const guild = await client.guilds.fetch(GUILD_ID);
    await exportServerStructure(guild);
  } catch (error) {
    console.error('❌ Error:', error.message);
  } finally {
    client.destroy();
    process.exit(0);
  }
});

// Error handling
client.on('error', error => {
  console.error('❌ Discord client error:', error);
  process.exit(1);
});

// Login
console.log('🔄 Connecting to Discord...');
client.login(TOKEN).catch(error => {
  console.error('❌ Failed to login:', error.message);
  console.error('\n💡 Check that:');
  console.error('   1. DISCORD_TOKEN is valid');
  console.error('   2. Bot has been invited to the server');
  console.error('   3. Bot has necessary permissions\n');
  process.exit(1);
});
