# Authentication & Authorization

Complete guide to authentication and authorization in libraries-service.

## Overview

- **Authentication**: External JWT via auth-users-service
- **Authorization**: Permission-based (service.resource.action)
- **API Keys**: Supported for service-to-service communication
- **OAuth**: Google OAuth 2.0 supported

## Authentication Methods

### 1. JWT Token (Primary)

**How it Works**:
1. User logs in via auth-service
2. Receives JWT access token + refresh token (cookie)
3. Includes token in Authorization header
4. libraries-service validates via auth-service
5. User data cached in Redis (10 min TTL)

**Request Header**:
```
Authorization: Bearer <jwt-token>
```

**Validation Flow**:
```
Client → libraries-service → auth-service (validate) → libraries-service → Client
                 ↓
              Redis Cache (10 min)
```

**Middleware**: `src/middleware/authMiddleware.js`

### 2. API Key (Alternative)

**Headers**:
```
X-API-Key: <api-key>
# or
X-API-Token: <api-key>
# or
Authorization: Bearer <api-key>
```

**Validation Flow**:
```
Client → libraries-service → API Gateway (validate) → libraries-service → Client
                 ↓
              Redis Cache (10 min)
```

**Middleware**: `src/middleware/apiKeyAuth.js`

### 3. OAuth (Google)

**Flow**:
1. User clicks "Sign in with Google"
2. Redirect to `/api/auth/google`
3. Google authentication
4. Callback to `/oauth-callback?accessToken=...`
5. Exchange token for refresh cookie
6. Redirect to `/dashboard`

**Frontend Component**: `client/src/pages/OAuthCallback.jsx`

## Authorization

### Permission Format

`service.resource.action`

Examples:
- `libraries-service.profession.create`
- `libraries-service.department.list`
- `libraries-service.*.read` (wildcard)
- `*.*.*` (super admin)

### Permission Check Middleware

**Location**: `src/middleware/permissionCheck.js`

**Methods**:

1. **requirePermission(service, resource, action)**
```javascript
router.post(
  '/profession',
  authMiddleware,
  requirePermission('libraries-service', 'profession', 'create'),
  professionController.create
);
```

2. **requireAnyPermission([permissions])**
```javascript
requireAnyPermission([
  { service: 'libraries-service', resource: 'profession', action: 'create' },
  { service: 'libraries-service', resource: 'profession', action: 'update' }
])
```

3. **requireAllPermissions([permissions])**
```javascript
requireAllPermissions([
  { service: 'libraries-service', resource: 'profession', action: 'read' },
  { service: 'libraries-service', resource: 'department', action: 'read' }
])
```

4. **requireServiceAccess(service)**
```javascript
requireServiceAccess('libraries-service')
```

### Frontend Permission Checks

**PermissionContext**: `client/src/contexts/PermissionContext.jsx`

**Hooks**:
```javascript
const { hasPermission, hasServiceAccess } = usePermission();

if (hasPermission('libraries-service', 'profession', 'create')) {
  // Show create button
}
```

**Components**:
```jsx
<PermissionRoute
  service="libraries-service"
  resource="profession"
  action="list"
>
  <ProfessionsPage />
</PermissionRoute>
```

## Token Management

### Access Token
- **Type**: JWT
- **Storage**: localStorage (frontend)
- **Lifetime**: 15 minutes (configurable)
- **Header**: `Authorization: Bearer <token>`

### Refresh Token
- **Type**: HTTP-only cookie
- **Lifetime**: 7 days (configurable)
- **Auto-refresh**: When access token expires

### Token Refresh Flow

```
1. API request fails with 401
2. Frontend calls /auth/refresh
3. New access token received
4. Retry original request
5. If refresh fails → redirect to login
```

**Frontend**: `client/src/services/api.js` (axios interceptor)

## User Context

### Backend (req.user)
```javascript
{
  id: "user-uuid",
  email: "user@example.com",
  roles: ["admin", "user"],
  permissions: [
    { service: "libraries-service", resource: "profession", action: "create" }
  ]
}
```

### Frontend (AuthContext)
```javascript
{
  user: {
    id, email, roles, permissions
  },
  isAuthenticated: true,
  loading: false,
  error: null
}
```

## Security Features

### CORS
- **Allowed Origins**: Configured via `ALLOWED_ORIGINS` env var
- **Credentials**: Supported
- **Methods**: GET, POST, PUT, DELETE, OPTIONS
- **Headers**: Content-Type, Authorization, X-API-Key

### Rate Limiting
- **General**: 100 requests / 15 minutes
- **Search**: 50 requests / 1 minute
- **By IP**: Per client IP address

### Headers Security (Helmet)
- Content Security Policy
- X-Frame-Options: DENY
- X-Content-Type-Options: nosniff
- Strict-Transport-Security

## File Locations

- **Auth Middleware**: `src/middleware/authMiddleware.js`
- **Permission Middleware**: `src/middleware/permissionCheck.js`
- **API Key Middleware**: `src/middleware/apiKeyAuth.js`
- **Auth Context**: `client/src/contexts/AuthContext.jsx`
- **Permission Context**: `client/src/contexts/PermissionContext.jsx`

---

**See Also**: [API.md](API.md), [BACKEND.md](BACKEND.md)
