## Налаштування MCP сервісу онлайн-академії

Ця інструкція допоможе встановити та підключити MCP сервіс онлайн-академії з репозиторію `AdminRHS/oa-y-mcp-service`.

### 1. Передумови
- Node.js 22+ та npm (можна встановити за відео-інструкцією [https://youtu.be/kQabFyl9r9I?si=jd8oq2I-7NIHtr5A](https://youtu.be/kQabFyl9r9I?si=jd8oq2I-7NIHtr5A)); якщо у вас інша ОС чи версія, знайдіть відповідне відео самостійно

### 2. STDIO режим через npx (Cursor / Claude Desktop)
У налаштуваннях MCP клієнта просто вставте блок нижче. Він викликає сервіс напряму з GitHub через `npx`, без локальної збірки:
   ```json
   {
     "mcpServers": {
       "oa-y-mcp-service": {
         "command": "npx",
         "args": [
           "-y",
           "github:AdminRHS/oa-y-mcp-service"
         ],
         "env": {
           "APP_ENV": "prod",
           "API_TOKEN": "d383d4d1-5829-4aa1-80ce-0668d6869386",
           "API_TOKEN_LIBS": "sk_Jer9YBmelvx2d_EmyCyaYTxjEYxQs4WYnaeEpkh2D_k"
         }
       }
     }
   }
   ```
або якщо вже є встановленні інші мсп просто вставити:
   ```json
    "oa-y-mcp-service": {
        "command": "npx",
        "args": [
        "-y",
        "github:AdminRHS/oa-y-mcp-service"
        ],
        "env": {
        "APP_ENV": "prod",
        "API_TOKEN": "d383d4d1-5829-4aa1-80ce-0668d6869386",
        "API_TOKEN_LIBS": "sk_Jer9YBmelvx2d_EmyCyaYTxjEYxQs4WYnaeEpkh2D_k"
        }
    }
   ```