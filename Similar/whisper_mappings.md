# Whisper Transcription Mappings

**Entity:** SIM
**Purpose:** Normalize voice transcription variations to canonical terms
**Last Updated:** 2025-12-07

---

## How to Use

1. Automation agent reads this file on startup
2. When processing transcriptions, applies mappings
3. Variations on left → canonical term on right
4. Case-insensitive matching, output preserves target case

---

## Reserved Action Words

### RESEARCH
```
research = investigate = look into = study = explore = analyze → RESEARCH
```

### BUILD
```
build = construct = develop = make = create system = implement → BUILD
```

### CREATE
```
create = make = generate = produce = write new → CREATE
```

### PROCESS
```
process = handle = work on = go through = transform → PROCESS
```

### SHARE
```
share = send = distribute = communicate = pass along → SHARE
```

### EXECUTE
```
execute = run = perform = carry out = do = implement → EXECUTE
```

### UPGRADE
```
upgrade = improve = enhance = update = refine = optimize → UPGRADE
```

### TEACH
```
teach = train = educate = show = explain = instruct → TEACH
```

### REVIEW
```
review = check = examine = analyze = evaluate = assess → REVIEW
```

### MARK
```
mark = flag = highlight = note = tag = designate → MARK
```

---

## File Operations

### Create
```
create file = make file = new file = add file = generate file → create_file
create folder = make directory = new folder = add directory → create_folder
```

### Read
```
read file = open file = view file = check file = look at → read_file
read folder = list directory = check folder → list_directory
```

### Update
```
update file = edit file = modify file = change file → edit_file
move file = transfer file = relocate file → move_file
rename file = change name → rename_file
```

### Delete
```
delete file = remove file = erase file = get rid of → delete_file
delete folder = remove directory = delete directory → delete_folder
```

---

## Cloud & Infrastructure

### General
```
cloud = cloud platform = cloud service = cloud provider → cloud_platform
server = cloud server = virtual machine = VM = instance → server
storage = cloud storage = file storage = data storage → storage
```

### Specific Platforms
```
aws = amazon = amazon web services → AWS
gcp = google cloud = google cloud platform → GCP
azure = microsoft azure = microsoft cloud → Azure
dropbox = drop box → Dropbox
drive = google drive = gdrive → Google_Drive
```

---

## Entities

### LBS (Libraries)
```
library = libraries = books = reading = research materials → LBS
book = ebook = electronic book = e-book → book
article = paper = research paper = publication → article
```

### SCR (Scraping)
```
scraping = web scraping = data extraction = scrape → SCR
scraper = scraping tool = extraction tool → scraper
```

### VID (Video)
```
video = videos = video content = footage → VID
shooting = video shooting = filming = recording → video_shooting
editing = video editing = post production → video_editing
```

### HR (Human Resources)
```
hr = human resources = people = employees → HR
hiring = recruiting = recruitment → hiring
onboarding = employee onboarding = new hire → onboarding
```

---

## Time & Organization

### Time Periods
```
day = daily = today = this day → day
week = weekly = this week → week
month = monthly = this month → month
```

### Organization
```
folder = directory = dir = location → folder
file = document = doc → file
task = todo = to do = action item → task
project = prt = initiative → project
template = sprg = sprint → template
```

---

## Development & Technical

### Programming
```
code = programming = coding = development → code
script = automation script = program → script
function = method = procedure → function
```

### Architecture
```
agent = ai agent = autonomous agent = bot → agent
microservice = micro service = service → microservice
api = interface = endpoint → API
```

### Data
```
database = db = data store = datastore → database
table = data table = db table → table
json = jason = JSON file → JSON
yaml = yml = YAML file → YAML
```

---

## Personal vs Work

### Personal
```
personal = private = my own = mine → personal
calendar = schedule = agenda = appointments → calendar
brand = personal brand = identity → personal_brand
relax warsaw = relaxwarsaw = relax → Relax_Warsaw
```

### Work
```
work = business = company = professional → work
employee = worker = staff = team member → employee
client = customer = user → client
```

---

## Task Manager Terms

### Hierarchy
```
project = prt = proj → PRT
template = sprg = sprint = iteration → SPRG
tag = label = category = classification → tag
```

### Actions
```
assign = give to = delegate to → assign
prioritize = set priority = mark important → prioritize
complete = finish = done = mark done → complete
```

---

## Common Phrases

### Requests
```
i want to = i need to = i would like to = let me → action_request
can you = could you = would you = please → polite_request
make sure = ensure = verify = confirm → verification_request
```

### Questions
```
what is = what's = whats = what are → what_query
how do i = how to = how can i → how_query
where is = wheres = where can i find → where_query
```

---

## Normalization Rules

### Apply mappings in this order:
1. Exact phrase match (longest first)
2. Word-level match
3. Stem match (if no exact match)
4. Keep original if no mapping found

### Examples:
```
Input: "I want to research cloud options"
  → "I want to" → action_request
  → "research" → RESEARCH
  → "cloud" → cloud_platform
Output: "action_request RESEARCH cloud_platform options"

Input: "Create new folder for videos"
  → "create" → CREATE
  → "folder" → folder
  → "videos" → VID
Output: "CREATE new folder for VID"
```

---

## Adding New Mappings

### Process:
1. Identify variation in transcription
2. Determine canonical term
3. Add to appropriate section above
4. Test with automation-agent
5. Verify normalization works

### Format:
```
variation1 = variation2 = variation3 → canonical_term
```

---

**Mapping Count:** 100+ variations mapped
**Coverage:** Core operations, entities, reserved words
**Status:** Active - continuously expanding
