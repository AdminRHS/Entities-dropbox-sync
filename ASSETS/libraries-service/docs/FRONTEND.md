# Frontend Architecture

Complete guide to the React frontend application.

## Overview

- **Framework**: React 19.1.0 with functional components and hooks
- **UI Library**: Material-UI 7.1.1 (MUI)
- **Build Tool**: Vite 6.3.5
- **Routing**: React Router 7.6.2
- **HTTP Client**: Axios 1.9.0
- **State Management**: Context API (Auth, Permissions, Theme)
- **Styling**: Emotion (CSS-in-JS with Material-UI)

## Application Structure

```
client/src/
├── main.jsx                 # Entry point with provider hierarchy
├── App.jsx                  # Main app component with routing
├── config/                  # Configuration files
├── pages/                   # 30+ page components
│   ├── Dashboard.jsx
│   ├── Professions.jsx
│   ├── Departments.jsx
│   ├── Login.jsx
│   └── ...
├── components/              # 57+ reusable components
│   ├── DataTable.jsx        # Universal table component
│   ├── CardView.jsx         # Grid card layout
│   ├── ProtectedRoute.jsx   # Auth route guard
│   ├── PermissionRoute.jsx  # Permission-based guard
│   ├── Sidebar.jsx          # Navigation sidebar
│   ├── Header.jsx           # Top navigation
│   └── [Entity]FormDialog.jsx  # 25+ CRUD dialogs
├── contexts/                # Global state providers
│   ├── AuthContext.jsx      # Authentication state
│   ├── PermissionContext.jsx # RBAC permissions
│   └── ThemeContext.jsx     # Light/dark theme
├── services/                # API integration
│   ├── api.js               # Axios client with interceptors
│   └── auth.js              # Auth service
├── themes/                  # Material-UI themes
│   └── themes.js            # Light/dark theme definitions
└── hooks/                   # Custom React hooks
```

## Entry Point and Provider Hierarchy

**File**: [client/src/main.jsx](../client/src/main.jsx)

```jsx
<Router>
  <ThemeProvider>
    <AuthProvider>
      <PermissionProvider>
        <App />
      </PermissionProvider>
    </AuthProvider>
  </ThemeProvider>
</Router>
```

**Provider Order** (outer to inner):
1. **Router** - React Router context
2. **ThemeProvider** - Material-UI theming + dark/light mode
3. **AuthProvider** - User authentication state
4. **PermissionProvider** - RBAC permissions (depends on user from AuthContext)
5. **App** - Main application component

## Routing Architecture

**File**: [client/src/App.jsx](../client/src/App.jsx:124-482)

### Route Types

**1. Public Routes** (no authentication required):
```jsx
<Route path="/" element={<WikiDashboard />} />
<Route path="/ai-tools" element={<Wiki />} />
<Route path="/login" element={<Login />} />
<Route path="/oauth-callback" element={<OAuthCallback />} />
```

**2. Protected Routes** (requires authentication):
```jsx
<Route element={<ProtectedRoute />}>
  <Route path="/dashboard" element={<Dashboard />} />
  {/* Nested routes with permission checks */}
</Route>
```

**3. Permission-Guarded Routes** (requires specific permission):
```jsx
<Route path="/professions" element={
  <PermissionRoute
    service="libraries-service"
    resource="profession"
    action="list"
  >
    <Professions />
  </PermissionRoute>
} />
```

### Route Guards

#### ProtectedRoute

**File**: [client/src/components/ProtectedRoute.jsx](../client/src/components/ProtectedRoute.jsx)

**Features**:
- Checks authentication via `useAuth()` hook
- Shows loading spinner during auth check
- Redirects to `/` if not authenticated
- Validates service-level access
- Displays access denied UI with "Go Back" and "Logout" buttons

#### PermissionRoute

**File**: [client/src/components/PermissionRoute.jsx](../client/src/components/PermissionRoute.jsx)

**Features**:
- Checks specific `service.resource.action` permission
- Supports multiple permissions with `requireAll` or `requireAny` logic
- Custom fallback component support
- Redirect on access denial
- Detailed error messages showing required permissions

**Usage**:
```jsx
// Single permission
<PermissionRoute
  service="libraries-service"
  resource="profession"
  action="create"
>
  <CreateButton />
</PermissionRoute>

// Multiple permissions (any)
<PermissionRoute
  permissions={[
    ['libraries-service', 'profession', 'create'],
    ['libraries-service', 'profession', 'update']
  ]}
  requireAll={false}
>
  <EditForm />
</PermissionRoute>
```

## Context Providers

### 1. AuthContext

**File**: [client/src/contexts/AuthContext.jsx](../client/src/contexts/AuthContext.jsx)

**State**:
- `user` - Current user object (null if not authenticated)
- `loading` - Authentication check in progress
- `error` - Login/auth errors
- `isAuthenticated` - Boolean computed from `!!user`

**Methods**:
- `login(email, password)` - Email/password login
- `loginWithGoogle()` - OAuth Google login
- `logout()` - Clear session and redirect
- `checkAuth()` - Validate token and refresh user data
- `setUser(user)` - Update user state

**Usage**:
```jsx
import { useAuth } from '../contexts/AuthContext';

function MyComponent() {
  const { user, isAuthenticated, login, logout } = useAuth();

  if (!isAuthenticated) {
    return <LoginForm onSubmit={login} />;
  }

  return <div>Welcome, {user.name}!</div>;
}
```

**Features**:
- Automatic token validation on mount
- Token refresh when expired
- Persists token in `localStorage`
- Fetches user profile from `/me` endpoint
- Redirects to home on auth failure

### 2. PermissionContext

**File**: [client/src/contexts/PermissionContext.jsx](../client/src/contexts/PermissionContext.jsx)

**State**:
- `userPermissions` - Array of user permissions from `user.permissions`
- `permissionsCache` - Map for fast permission lookups
- `isLoading` - Always false (permissions load with user)

**Methods**:
- `hasPermission(service, resource, action)` - Check specific permission
- `hasServiceAccess(service)` - Check any permission in service
- `hasResourceAccess(service, resource)` - Check any action for resource
- `hasAllPermissions(permissions[])` - All must be true
- `hasAnyPermission(permissions[])` - Any can be true
- `getServicePermissions(service)` - Get all permissions for service
- `getResourcePermissions(service, resource)` - Get all actions for resource

**Permission Format**:
```javascript
{
  service: 'libraries-service',
  resource: 'profession',
  action: 'create' // or '*' for wildcard
}
```

**Wildcard Support**:
- `*.*.*` - Global admin (all permissions)
- `service.*.*` - All resources in service
- `service.resource.*` - All actions for resource
- `service.*.action` - Same action across all resources

**Usage**:
```jsx
import { usePermissions, PermissionGuard } from '../contexts/PermissionContext';

function MyComponent() {
  const { hasPermission } = usePermissions();

  return (
    <div>
      {hasPermission('libraries-service', 'profession', 'create') && (
        <CreateButton />
      )}

      <PermissionGuard
        service="libraries-service"
        resource="profession"
        action="delete"
      >
        <DeleteButton />
      </PermissionGuard>
    </div>
  );
}
```

### 3. ThemeContext

**File**: [client/src/contexts/ThemeContext.jsx](../client/src/contexts/ThemeContext.jsx)

**State**:
- `mode` - Current theme mode ('light' | 'dark')

**Methods**:
- `toggleTheme()` - Switch between light and dark

**Features**:
- Persists theme preference in `localStorage`
- Wraps Material-UI `ThemeProvider`
- Includes `CssBaseline` for consistent baseline styles

**Usage**:
```jsx
import { useTheme } from '../contexts/ThemeContext';

function ThemeToggleButton() {
  const { mode, toggleTheme } = useTheme();

  return (
    <Button onClick={toggleTheme}>
      {mode === 'dark' ? <LightIcon /> : <DarkIcon />}
    </Button>
  );
}
```

## Core Reusable Components

### DataTable

**File**: [client/src/components/DataTable.jsx](../client/src/components/DataTable.jsx)

**Features**:
- Sortable columns with `TableSortLabel`
- Pagination with configurable rows per page
- Loading state with `CircularProgress`
- Error state with retry button
- Empty state with custom message
- Sticky header support
- Controlled or uncontrolled mode

**Props**:
```jsx
<DataTable
  data={[]}                    // Array of items
  columns={[                   // Column definitions
    { id: 'name', label: 'Name', sortable: true },
    { id: 'actions', label: 'Actions', align: 'right' }
  ]}
  totalItems={100}
  page={0}
  rowsPerPage={10}
  onPageChange={(e, page) => {}}
  onRowsPerPageChange={(e) => {}}
  loading={false}
  error={null}
  onRetry={() => {}}
  sortBy="name"
  sortOrder="asc"
  onSort={(column) => {}}
/>
```

### CardView

**File**: [client/src/components/CardView.jsx](../client/src/components/CardView.jsx)

**Features**:
- Grid layout with Material-UI `Grid`
- Pagination support
- Loading/error/empty states
- Customizable grid spacing
- Responsive breakpoints

**Props**:
```jsx
<CardView
  data={[]}
  renderCard={(item) => <Card>{item.name}</Card>}
  totalItems={100}
  page={0}
  itemsPerPage={12}
  onPageChange={(e, page) => {}}
  loading={false}
  error={null}
  gridProps={{ spacing: 2 }}
  itemProps={{ xs: 12, sm: 6, md: 4 }}
/>
```

### DataViewToggle

**File**: [client/src/components/DataViewToggle.jsx](../client/src/components/DataViewToggle.jsx)

**Features**:
- Switch between table and card views
- Icon buttons with tooltips
- Persists view preference

**Usage**:
```jsx
const [viewMode, setViewMode] = useState('table');

<DataViewToggle value={viewMode} onChange={setViewMode} />

{viewMode === 'table' ? <DataTable /> : <CardView />}
```

### Form Dialogs (25+ Components)

**Pattern** - All entity form dialogs follow consistent structure:

**Example**: [client/src/components/ProfessionFormDialog.jsx](../client/src/components/ProfessionFormDialog.jsx)

**Features**:
- Material-UI `Dialog` with responsive fullScreen on mobile
- Form validation
- Loading state during submission
- Error handling with `Alert`
- Create/Edit modes with conditional title
- Cancel/Save buttons

**Common Props**:
```jsx
<EntityFormDialog
  open={true}
  onClose={() => {}}
  onSubmit={(data) => {}}
  initialData={null}  // null for create, object for edit
/>
```

**Form Dialog Components**:
- ActionFormDialog
- CityFormDialog
- CountryFormDialog
- CurrencyFormDialog
- DepartmentFormDialog
- FormatFormDialog
- IndustryFormDialog
- LanguageFormDialog
- LevelFormDialog
- McpFormDialog
- ObjectFormDialog
- PositionFormDialog
- PriorityFormDialog
- ProfessionFormDialog
- RateFormDialog
- ResponsibilityFormDialog
- ServiceFormDialog
- ShiftFormDialog
- SkillFormDialog
- StatusFormDialog
- SubIndustryFormDialog
- TermTypeFormDialog
- ToolFormDialog
- ToolTypeFormDialog

### Other Reusable Components

**ConfirmDeleteDialog** - Confirmation dialog for delete operations
**DescriptionDialog** - View full descriptions
**ExpandableChips** - Collapsible chip lists
**Header** - Top navigation bar with menu toggle
**SearchInput** - Debounced search input
**Sidebar** - Navigation sidebar with 6 categories

## Page Components (30 Pages)

**Entity Management Pages** (standard CRUD pattern):

Each page includes:
- DataTable/CardView toggle
- Search/filter controls
- Create button (permission-guarded)
- Edit/Delete actions (permission-guarded)
- Pagination

**Pages**:
- Actions.jsx
- Cities.jsx
- Countries.jsx
- Currencies.jsx
- Dashboard.jsx
- Departments.jsx
- Formats.jsx
- Industries.jsx
- Languages.jsx
- Levels.jsx
- Mcps.jsx
- Objects.jsx
- Positions.jsx
- Priorities.jsx
- Professions.jsx
- Rates.jsx
- Responsibilities.jsx
- Services.jsx
- Shifts.jsx
- Skills.jsx
- Statuses.jsx
- SubIndustries.jsx
- TermTypes.jsx
- Terms.jsx
- Tools.jsx
- ToolTypes.jsx
- Wiki.jsx (public)
- WikiDashboard.jsx (public landing)
- Login.jsx
- NotFound.jsx

## API Integration

### Axios Client Configuration

**File**: [client/src/services/api.js](../client/src/services/api.js)

**Features**:
- Two axios instances: `api` (libraries-service) and `gatewayApi` (API Gateway)
- Base URL from environment variables
- JWT token auto-injection via request interceptor
- Token refresh on 401 errors via response interceptor
- Shared refresh queue to prevent multiple refresh requests
- Automatic redirect to login on refresh failure
- FormData support for file uploads

**Request Interceptor**:
```javascript
api.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  config.headers['X-Client-Domain'] = window.location.origin;
  return config;
});
```

**Response Interceptor** (Token Refresh):
```javascript
api.interceptors.response.use(
  response => response,
  async error => {
    if (error.response?.status === 401 && !originalRequest._retry) {
      // Refresh token logic
      const newToken = await authService.refreshToken();
      // Retry original request with new token
    }
  }
);
```

### API Services

**Pattern** - Each entity has dedicated API object:

```javascript
export const professionsAPI = {
  getAll: async (params = {}) => {
    const response = await api.get('/profession', { params });
    return response.data;
  },
  getById: async (id) => {
    const response = await api.get(`/profession/${id}`);
    return response.data;
  },
  create: async (data) => {
    const response = await api.post('/profession', data);
    return response.data;
  },
  update: async (id, data) => {
    const response = await api.put(`/profession/${id}`, data);
    return response.data;
  },
  delete: async (id) => {
    const response = await api.delete(`/profession/${id}`);
    return response.data;
  },
  getTerms: async (params = {}) => {
    const response = await api.get('/profession/terms', { params });
    return response.data;
  }
};
```

**Available API Services** (27 total):
- departmentsAPI
- professionsAPI
- statusesAPI
- prioritiesAPI
- servicesAPI
- languagesAPI
- statisticsAPI
- termTypesAPI
- toolTypesAPI
- formatsAPI
- toolsAPI
- termsAPI
- actionsAPI
- objectsAPI
- responsibilitiesAPI
- countriesAPI
- industriesAPI
- citiesAPI
- shiftsAPI
- currenciesAPI
- positionsAPI
- ratesAPI
- levelsAPI
- skillsAPI
- subIndustriesAPI
- mcpsAPI
- accountsAPI (via gatewayApi)

## Material-UI Theme Customization

**File**: [client/src/themes/themes.js](../client/src/themes/themes.js)

**Light Theme**:
```javascript
export const lightTheme = createTheme({
  palette: {
    mode: 'light',
    primary: { main: '#1976d2' },
    secondary: { main: '#dc004e' }
  }
});
```

**Dark Theme**:
```javascript
export const darkTheme = createTheme({
  palette: {
    mode: 'dark',
    primary: { main: '#90caf9' },
    secondary: { main: '#f48fb1' }
  }
});
```

**Component Overrides** (if needed):
```javascript
components: {
  MuiButton: {
    styleOverrides: {
      root: { borderRadius: 8 }
    }
  }
}
```

## Development Patterns

### 1. Dual View Pattern

All entity lists support table and card views:

```jsx
const [viewMode, setViewMode] = useState('table');

<DataViewToggle value={viewMode} onChange={setViewMode} />

{viewMode === 'table' ? (
  <DataTable data={items} columns={columns} />
) : (
  <CardView data={items} renderCard={(item) => <ItemCard item={item} />} />
)}
```

### 2. Permission-Based UI

Hide/show elements based on permissions:

```jsx
import { usePermissions } from '../contexts/PermissionContext';

const { hasPermission } = usePermissions();

{hasPermission('libraries-service', 'profession', 'create') && (
  <Button onClick={handleCreate}>Create</Button>
)}
```

### 3. Loading/Error States

Consistent handling across pages:

```jsx
const [loading, setLoading] = useState(false);
const [error, setError] = useState(null);

if (loading) return <CircularProgress />;
if (error) return <Alert severity="error">{error}</Alert>;
```

### 4. Responsive Layout

Mobile-first with Material-UI breakpoints:

```jsx
import { useMediaQuery, useTheme } from '@mui/material';

const theme = useTheme();
const isMobile = useMediaQuery(theme.breakpoints.down('md'));

{isMobile ? <MobileView /> : <DesktopView />}
```

## Environment Variables

**File**: [client/.env](../client/.env) (create from .env.example)

```bash
VITE_API_URL=http://localhost:3002/api
VITE_API_GATEWAY_URL=http://localhost:3003/api
```

**Usage in Code**:
```javascript
import { API_URL, API_GATEWAY_URL } from './config';
```

## Build and Development

### Start Development Server
```bash
cd client
npm run dev  # Runs on port 3000
```

### Build for Production
```bash
cd client
npm run build  # Output to client/dist
```

### Preview Production Build
```bash
cd client
npm run preview
```

### Linting
```bash
cd client
npm run lint
```

## Best Practices

1. **Use Functional Components** - All components use hooks, no class components
2. **Extract Reusable Logic** - Create custom hooks for shared logic
3. **Permission Checks** - Always guard create/update/delete actions
4. **Error Boundaries** - Use try-catch for async operations
5. **Loading States** - Always show loading indicators during async operations
6. **Responsive Design** - Test on mobile, tablet, desktop breakpoints
7. **Accessibility** - Use semantic HTML and ARIA labels
8. **Code Splitting** - Use React.lazy() for large components (if needed)

---

**See Also**:
- [API.md](API.md) - Backend API endpoints
- [AUTH.md](AUTH.md) - Authentication and permissions
- [DEVELOPMENT.md](DEVELOPMENT.md) - Development workflow

**Last Updated**: 2025-01-12
