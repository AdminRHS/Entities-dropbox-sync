# AI PROMPT: Stand-Alone Web Application Builder (No Authentication)

**Version**: 1.0
**Last Updated**: 2025-12-05
**Purpose**: Ready-to-use prompt for AI assistants to generate complete stand-alone web applications

---

## HOW TO USE THIS PROMPT

1. Copy the **MAIN PROMPT** section below
2. Replace `[APP_TYPE]` with your desired application (see USE CASE EXAMPLES)
3. Paste into ChatGPT, Claude, or any AI coding assistant
4. Review and customize the generated code as needed

---

# MAIN PROMPT

```
Build a complete, production-ready [APP_TYPE] web application with the following specifications:

## PROJECT REQUIREMENTS

### Core Specifications
- **No Authentication**: Application must work without any login or user accounts
- **Client-Side Only**: Entirely browser-based, no backend server required
- **Immediate Functionality**: Works by simply opening index.html in a browser
- **Modern JavaScript**: Use ES6+ syntax (async/await, arrow functions, template literals)
- **Responsive Design**: Mobile-first approach, works on all screen sizes
- **Public API Integration**: Use free, no-auth-required APIs where applicable

### Technology Stack
- **HTML5**: Semantic markup, minimal boilerplate
- **CSS3**: Modern CSS with Flexbox/Grid, CSS variables for theming
- **Vanilla JavaScript**: No frameworks or libraries required
- **Fetch API**: For all HTTP requests with proper error handling

## TECHNICAL IMPLEMENTATION

### File Structure
Create three main files:
1. `index.html` - Semantic HTML5 structure
2. `styles.css` - Modern, responsive styling
3. `script.js` - ES6+ JavaScript with proper organization
4. `README.md` - Complete documentation

### JavaScript Architecture
Use this proven pattern:

```javascript
// Phase 1: DOM Selection
const element1 = document.getElementById('element1');
const element2 = document.getElementById('element2');
// ... select all interactive elements

// Phase 2: Function Definitions
async function fetchData() {
  try {
    const response = await fetch('API_URL');
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error:', error);
    displayError('Failed to fetch data. Please try again.');
    return null;
  }
}

function createDOMElement(data) {
  const element = document.createElement('div');
  element.innerHTML = `
    <h3>${data.title}</h3>
    <p>${data.description}</p>
  `;
  return element;
}

function displayError(message) {
  // Show user-friendly error message
}

// Phase 3: Event Listeners
button.addEventListener('click', async () => {
  const data = await fetchData();
  if (data) updateUI(data);
});

// Use event delegation for dynamic elements
container.addEventListener('click', (e) => {
  if (e.target.matches('.delete-btn')) {
    handleDelete(e.target);
  }
});

// Phase 4: Initialization
document.addEventListener('DOMContentLoaded', () => {
  // Initialize app
});
```

### Required Features
1. **Core Functionality**
   - Primary user actions (add, delete, search, etc.)
   - Data display with proper formatting
   - Interactive elements with visual feedback

2. **API Integration**
   - Async/await for all API calls
   - Comprehensive error handling
   - Loading states during requests
   - Timeout handling for slow connections

3. **User Experience**
   - Loading indicators during async operations
   - Success/error message displays
   - Empty state messages
   - Clear visual feedback for all actions
   - Input validation with helpful error messages

4. **Error Handling**
   - Try/catch blocks for all async operations
   - User-friendly error messages (not technical jargon)
   - Graceful degradation if API is unavailable
   - Console logging for debugging

5. **Code Quality**
   - Clear, descriptive variable and function names
   - Comments explaining complex logic
   - DRY principle (no repetitive code)
   - Proper indentation and formatting
   - Consistent naming conventions (camelCase for JS)

## STYLING REQUIREMENTS

### CSS Structure
```css
/* 1. CSS Variables */
:root {
  --primary-color: #007bff;
  --secondary-color: #6c757d;
  --success-color: #28a745;
  --error-color: #dc3545;
  --background-color: #f8f9fa;
  --text-color: #333;
  --border-radius: 8px;
  --spacing-unit: 8px;
}

/* 2. Reset & Base Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  line-height: 1.6;
  color: var(--text-color);
  background-color: var(--background-color);
}

/* 3. Layout (Flexbox/Grid) */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: calc(var(--spacing-unit) * 2);
}

/* 4. Components */
.btn {
  padding: calc(var(--spacing-unit) * 1.5) calc(var(--spacing-unit) * 3);
  border: none;
  border-radius: var(--border-radius);
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

/* 5. Responsive Design */
@media (max-width: 768px) {
  .container {
    padding: var(--spacing-unit);
  }
}
```

### Design Principles
- Modern, clean aesthetic
- Adequate whitespace
- Clear visual hierarchy
- Smooth transitions and animations
- Accessible color contrast (WCAG AA compliant)

## DOCUMENTATION REQUIREMENTS

### README.md Structure
```markdown
# [Application Name]

Brief description of what the application does.

## Features
- Feature 1
- Feature 2
- Feature 3

## Technologies Used
- HTML5
- CSS3
- Vanilla JavaScript (ES6+)
- [API Name] API

## Installation & Usage
1. Clone or download this repository
2. Open `index.html` in a modern web browser
3. No additional setup required!

## API Information
- **API Used**: [API Name]
- **Endpoint**: https://api.example.com
- **Rate Limits**: [if applicable]
- **Documentation**: [API docs link]

## Browser Compatibility
Works on all modern browsers:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Future Enhancements
- [ ] Add local storage persistence
- [ ] Implement dark mode
- [ ] Add filtering/sorting options

## License
MIT License

## Author
[Your Name]
```

## QUALITY CHECKLIST

Before providing the final code, ensure:
- [ ] All code uses ES6+ syntax
- [ ] All async operations have error handling
- [ ] User receives feedback for all actions
- [ ] Code is well-commented
- [ ] Variable/function names are descriptive
- [ ] No console errors when running
- [ ] Responsive on mobile and desktop
- [ ] HTML is semantic and accessible
- [ ] README is complete and accurate

## DELIVERABLES

Provide complete, ready-to-use code for:
1. **index.html** - Full HTML structure
2. **styles.css** - Complete styling
3. **script.js** - All JavaScript logic
4. **README.md** - Full documentation

Include brief explanations of:
- How the code is organized
- Key functions and their purposes
- How to extend or modify the application
- Any API limitations or considerations

## ADDITIONAL NOTES
- Prioritize code readability over cleverness
- Use descriptive comments for complex logic
- Ensure the app is immediately usable without configuration
- Make the code beginner-friendly but professional quality
```

---

# USE CASE EXAMPLES

Copy the MAIN PROMPT above and replace `[APP_TYPE]` with one of these:

## 1. Task/Todo Manager (Beginner)
**Replace with**: "task management / todo list"

**Suggested API**: JSONPlaceholder (`https://jsonplaceholder.typicode.com/todos`)

**Key Features**:
- Add new tasks
- Delete tasks
- Mark tasks as complete/incomplete
- Fetch sample tasks from API
- Optional: Local storage persistence

---

## 2. Weather Dashboard (Beginner-Intermediate)
**Replace with**: "weather dashboard"

**Suggested API**: OpenWeatherMap (free tier)

**Key Features**:
- Search weather by city name
- Display current temperature, conditions, humidity
- 5-day forecast
- Geolocation to get user's weather
- Weather icons and visual indicators

**Additional Setup**:
```
You'll need a free API key from OpenWeatherMap:
1. Sign up at https://openweathermap.org/api
2. Get your free API key
3. Add to the code: const API_KEY = 'your_key_here';
```

---

## 3. Recipe Finder (Intermediate)
**Replace with**: "recipe finder and meal planner"

**Suggested API**: TheMealDB (`https://www.themealdb.com/api.php`)

**Key Features**:
- Search recipes by ingredient
- Filter by cuisine type
- Display recipe details (ingredients, instructions)
- Random recipe generator
- Recipe image gallery

---

## 4. Movie/TV Show Search (Intermediate)
**Replace with**: "movie and TV show search engine"

**Suggested API**: OMDb API (requires free API key)

**Key Features**:
- Search by title
- Display poster, rating, plot, cast
- Pagination for multiple results
- Filter by year or type (movie/series)
- Detailed view modal

---

## 5. Quote Generator (Beginner)
**Replace with**: "inspirational quote generator"

**Suggested API**: Quotable (`https://api.quotable.io`)

**Key Features**:
- Display random quotes
- Filter by tag/category
- Show author information
- Share quote functionality
- Copy to clipboard

---

## 6. Currency Converter (Beginner-Intermediate)
**Replace with**: "currency converter"

**Suggested API**: ExchangeRate-API or FreeCurrencyAPI

**Key Features**:
- Convert between currencies
- Real-time exchange rates
- Swap currencies
- Popular currency shortcuts
- Historical rate charts (optional)

---

## 7. News Reader (Intermediate)
**Replace with**: "news reader/aggregator"

**Suggested API**: NewsAPI (free tier available)

**Key Features**:
- Fetch latest headlines
- Filter by category (tech, sports, business)
- Search news by keyword
- Display article previews
- Link to full articles

---

## 8. Random User Generator (Beginner)
**Replace with**: "random user profile generator"

**Suggested API**: RandomUser API (`https://randomuser.me/api/`)

**Key Features**:
- Generate random user profiles
- Display profile picture, name, contact info
- Generate multiple users
- Copy profile data
- Filter by gender/nationality

---

## 9. GitHub Profile Viewer (Intermediate)
**Replace with**: "GitHub profile and repository viewer"

**Suggested API**: GitHub API (public endpoints, no auth needed)

**Key Features**:
- Search GitHub users
- Display profile info and stats
- Show repositories
- Repository details (stars, forks, language)
- Link to actual GitHub profiles

---

## 10. Pokedex App (Beginner-Intermediate)
**Replace with**: "Pokemon Pokedex"

**Suggested API**: PokeAPI (`https://pokeapi.co/api/v2/`)

**Key Features**:
- Browse Pokemon list
- Search by name or ID
- Display Pokemon details (stats, types, abilities)
- Evolution chain
- Type effectiveness chart

---

# CUSTOMIZATION OPTIONS

## Add These Modifiers to the Prompt for Enhanced Features:

### For Local Storage Persistence
Add this to the prompt:
```
Include local storage functionality to persist data between sessions.
Save user data to localStorage when modified and load it on page load.
```

### For Dark Mode
Add this to the prompt:
```
Implement a dark mode toggle that switches between light and dark themes.
Use CSS variables for colors and save the user's preference to localStorage.
```

### For Advanced Filtering/Sorting
Add this to the prompt:
```
Include advanced filtering and sorting options for the displayed data.
Allow users to filter by multiple criteria and sort ascending/descending.
```

### For Data Export
Add this to the prompt:
```
Add functionality to export data as JSON or CSV files.
Include a download button that generates and downloads the file.
```

### For Offline Support
Add this to the prompt:
```
Implement basic service worker functionality for offline access.
Cache essential assets and provide offline fallback messages.
```

---

# PUBLIC APIs REFERENCE

## No Authentication Required

### General Purpose
- **JSONPlaceholder** - `https://jsonplaceholder.typicode.com`
  - Posts, comments, albums, photos, todos, users
  - Perfect for learning and testing

### Specific Domains

**Weather**
- OpenWeatherMap - `https://openweathermap.org/api` (free tier)
- WeatherAPI - `https://www.weatherapi.com` (free tier)

**Food & Recipes**
- TheMealDB - `https://www.themealdb.com/api.php`
- Spoonacular - `https://spoonacular.com/food-api` (free tier)

**Movies & TV**
- OMDb API - `http://www.omdbapi.com` (free tier)
- TVMaze - `https://www.tvmaze.com/api`

**Quotes & Text**
- Quotable - `https://api.quotable.io`
- Advice Slip - `https://api.adviceslip.com`

**Data & Information**
- REST Countries - `https://restcountries.com`
- Wikipedia API - `https://www.mediawiki.org/wiki/API`

**Fun & Entertainment**
- Dog API - `https://dog.ceo/dog-api/`
- Cat Facts - `https://catfact.ninja`
- Pokemon API - `https://pokeapi.co`
- Rick and Morty API - `https://rickandmortyapi.com`

**Development**
- GitHub API - `https://api.github.com` (public endpoints)
- Random User - `https://randomuser.me`

**News**
- NewsAPI - `https://newsapi.org` (free tier)
- Hacker News - `https://github.com/HackerNews/API`

**Finance**
- ExchangeRate API - `https://www.exchangerate-api.com` (free tier)
- CoinGecko - `https://www.coingecko.com/en/api` (crypto prices)

---

# ADVANCED PROMPT VARIATIONS

## For More Experienced Developers

Replace the JavaScript architecture section with:

```javascript
// Use modern module pattern
const App = {
  // State management
  state: {
    data: [],
    loading: false,
    error: null
  },

  // API methods
  api: {
    async fetch(endpoint) {
      this.setState({ loading: true, error: null });
      try {
        const response = await fetch(endpoint);
        if (!response.ok) throw new Error('API Error');
        const data = await response.json();
        this.setState({ data, loading: false });
        return data;
      } catch (error) {
        this.setState({ error: error.message, loading: false });
        return null;
      }
    }
  },

  // State management
  setState(updates) {
    Object.assign(this.state, updates);
    this.render();
  },

  // Render method
  render() {
    // Update UI based on current state
  },

  // Initialize
  init() {
    this.bindEvents();
    this.render();
  }
};

// Initialize app
document.addEventListener('DOMContentLoaded', () => App.init());
```

---

# TROUBLESHOOTING GUIDE

## Common Issues When Using This Prompt

### Issue: CORS Errors
**Symptom**: Console shows "CORS policy" errors
**Solution**:
- Ensure the API supports CORS
- Use APIs from the recommended list above
- Consider using a CORS proxy for development only

### Issue: API Rate Limiting
**Symptom**: API stops responding after several requests
**Solution**:
- Implement request debouncing
- Cache API responses
- Display rate limit warnings to users

### Issue: Code Doesn't Run
**Symptom**: Nothing happens when opening HTML file
**Solution**:
- Check browser console for errors
- Ensure JavaScript file is properly linked
- Verify all DOM elements exist before selecting them
- Use `DOMContentLoaded` event

### Issue: Styling Issues on Mobile
**Symptom**: Layout broken on small screens
**Solution**:
- Add viewport meta tag: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- Test responsive breakpoints
- Use mobile-first approach

---

# EXAMPLES OF SUCCESSFUL OUTPUTS

## What Good Generated Code Looks Like

### HTML Example
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Todo List App</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="container">
    <header>
      <h1>My Todo List</h1>
    </header>

    <main>
      <div class="input-section">
        <input type="text" id="taskInput" placeholder="Enter a new task..." aria-label="Task input">
        <button id="addTask" class="btn btn-primary">Add Task</button>
        <button id="fetchTasks" class="btn btn-secondary">Load Sample Tasks</button>
      </div>

      <div id="loading" class="loading hidden">Loading...</div>
      <div id="error" class="error hidden"></div>

      <ul id="taskList" class="task-list"></ul>
    </main>
  </div>

  <script src="script.js"></script>
</body>
</html>
```

### JavaScript Example (Key Functions)
```javascript
// DOM Elements
const taskInput = document.getElementById('taskInput');
const addTaskBtn = document.getElementById('addTask');
const fetchTasksBtn = document.getElementById('fetchTasks');
const taskList = document.getElementById('taskList');
const loadingEl = document.getElementById('loading');
const errorEl = document.getElementById('error');

// Add task function
function addTask() {
  const taskText = taskInput.value.trim();

  if (!taskText) {
    showError('Please enter a task');
    return;
  }

  const taskItem = createTaskElement(taskText, false);
  taskList.appendChild(taskItem);

  taskInput.value = '';
  taskInput.focus();
}

// Create task element
function createTaskElement(text, completed) {
  const li = document.createElement('li');
  li.className = `task-item ${completed ? 'completed' : ''}`;
  li.innerHTML = `
    <span class="task-text">${text}</span>
    <button class="delete-btn" aria-label="Delete task">×</button>
  `;
  return li;
}

// Fetch tasks from API
async function fetchTasks() {
  showLoading(true);
  hideError();

  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/todos?_limit=5');

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const tasks = await response.json();

    taskList.innerHTML = '';
    tasks.forEach(task => {
      const taskItem = createTaskElement(task.title, task.completed);
      taskList.appendChild(taskItem);
    });

  } catch (error) {
    console.error('Fetch error:', error);
    showError('Failed to load tasks. Please check your connection and try again.');
  } finally {
    showLoading(false);
  }
}

// Event delegation for delete buttons
taskList.addEventListener('click', (e) => {
  if (e.target.matches('.delete-btn')) {
    e.target.closest('.task-item').remove();
  }
});

// Event listeners
addTaskBtn.addEventListener('click', addTask);
fetchTasksBtn.addEventListener('click', fetchTasks);
taskInput.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') addTask();
});

// Utility functions
function showLoading(show) {
  loadingEl.classList.toggle('hidden', !show);
}

function showError(message) {
  errorEl.textContent = message;
  errorEl.classList.remove('hidden');
}

function hideError() {
  errorEl.classList.add('hidden');
}
```

---

# VERSION HISTORY

**v1.0** (2025-12-05)
- Initial release
- Based on proven To-Do List tutorial architecture
- Includes 10 use case examples
- Comprehensive API reference
- Quality checklist and troubleshooting guide

---

# TIPS FOR BEST RESULTS

1. **Be Specific**: The more specific you are about features, the better the output
2. **Start Simple**: Begin with basic functionality, then ask for enhancements
3. **Test Incrementally**: Test each feature as it's added
4. **Iterate**: Ask the AI to refine or improve specific parts
5. **Combine Ideas**: Mix multiple use cases for unique applications

---

# FEEDBACK & IMPROVEMENTS

This prompt is designed to evolve. If you discover better patterns or have suggestions:
- Document what works well
- Note any common issues
- Suggest improvements to the prompt structure
- Share successful variations

---

**End of Prompt Template**

**Ready to use!** Copy the MAIN PROMPT section, customize `[APP_TYPE]`, and start building.
