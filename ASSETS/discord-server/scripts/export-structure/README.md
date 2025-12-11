# Discord Server Structure Export

This script exports your Discord server structure to JSON files for backup and analysis.

## 🚀 Quick Start

### 1. Prerequisites

- Node.js 16+ installed
- Discord bot token
- Bot invited to your server

### 2. Setup

```bash
# Install dependencies
npm install

# Configure environment
# Edit ../../.env and add:
# DISCORD_TOKEN=your_bot_token_here
# DISCORD_GUILD_ID=your_server_id_here
```

### 3. Run Export

```bash
npm run export
```

## 🤖 Creating a Discord Bot

1. Go to https://discord.com/developers/applications
2. Click "New Application"
3. Give it a name (e.g., "Server Export Bot")
4. Go to "Bot" section
5. Click "Add Bot"
6. Copy the token (save to .env)
7. Enable "Server Members Intent" (optional)
8. Go to "OAuth2" → "URL Generator"
9. Select scopes: `bot`
10. Select permissions: `Read Messages/View Channels`
11. Copy the URL and invite bot to your server

## 📁 Output Files

The script creates these files in `exported/current-structure/`:

- `categories.json` - All server categories
- `channels.json` - All channels with metadata
- `roles.json` - All server roles
- `full-export.json` - Complete server structure

## 🔧 Troubleshooting

### "Invalid token"
- Check that DISCORD_TOKEN in .env is correct
- Regenerate token if needed

### "Unknown Guild"
- Verify DISCORD_GUILD_ID is correct
- Ensure bot has been invited to the server

### "Missing Access"
- Bot needs "View Channels" permission
- Check bot role position in server settings

## 📊 Example Output

```json
{
  "serverName": "REMS! - Remote Employees ;)",
  "exportDate": "2025-12-10",
  "categories": [...],
  "channels": [...],
  "summary": {
    "totalCategories": 16,
    "totalChannels": 103
  }
}
```

## 🔒 Security

- Never commit .env file
- Keep bot token secret
- Use minimal permissions
- Revoke token when done

## 📚 Dependencies

- `discord.js` - Discord API library
- `dotenv` - Environment variable management

---

**Version:** 1.0.0
**Updated:** 2025-12-10
