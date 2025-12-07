# PAGE 1: CORE CONCEPT - What We're Building

**Start Here: The Simplest Possible Version**

---

## THE BIG IDEA

Build a system that moves items through stages, tracks progress, and prevents mistakes.

**Real-World Example from RESEARCH 2**:
- Videos move through 7 stages: Queued → Transcribed → Extracted → Analyzed → Integrated → Mapped → Complete
- Each stage must be completed before moving to next
- System tracks which stage each video is in
- System prevents skipping stages

---

## YOUR SIMPLEST VERSION

Build a **3-stage item tracker**:

```
Stage 1: NEW
   ↓
Stage 2: IN PROGRESS
   ↓
Stage 3: DONE
```

**That's it. Start here.**

---

## WHAT IT DOES (Minimum)

### 1. Add Items
```
You: "Add item: Write report"
System: Creates item with ID #1, sets stage to NEW
```

### 2. Move Items Forward
```
You: "Move #1 to IN PROGRESS"
System: Changes stage from NEW → IN PROGRESS
```

```
You: "Move #1 to DONE"
System: Changes stage from IN PROGRESS → DONE
```

### 3. List All Items
```
You: "List all"
System: Shows:
  #1 - Write report - DONE
  #2 - Review code - IN PROGRESS
  #3 - Send email - NEW
```

---

## CORE RULES (Business Logic)

### Rule 1: Sequential Stages Only
**Cannot skip stages**

```
✗ WRONG: NEW → DONE (skipped IN PROGRESS)
✓ RIGHT: NEW → IN PROGRESS → DONE
```

**Why**: Ensures every item gets processed properly, no shortcuts

### Rule 2: Auto-Generated IDs
**System creates IDs, not you**

```
First item: #1
Second item: #2
Third item: #3
```

**Why**: No duplicate IDs, always unique

### Rule 3: Items Start at Stage 1
**All new items begin at NEW**

```
Add item → Automatically set to NEW
```

**Why**: Clear starting point, consistent

---

## DATA YOU NEED TO STORE

For each item, remember:
1. **ID** - Unique number (#1, #2, #3)
2. **Name** - What the item is ("Write report")
3. **Stage** - Where it is (NEW, IN PROGRESS, or DONE)

**That's all you need for the simplest version.**

---

## EXAMPLE WALKTHROUGH

### Start: Empty system

### Step 1: Add first item
```
Action: Add "Write report"
Result:
  #1 - Write report - NEW
```

### Step 2: Add second item
```
Action: Add "Review code"
Result:
  #1 - Write report - NEW
  #2 - Review code - NEW
```

### Step 3: Start working on #1
```
Action: Move #1 to IN PROGRESS
Result:
  #1 - Write report - IN PROGRESS
  #2 - Review code - NEW
```

### Step 4: Try to skip a stage (SHOULD FAIL)
```
Action: Move #2 to DONE
Result: ERROR - Cannot skip from NEW to DONE
Status: No change
  #1 - Write report - IN PROGRESS
  #2 - Review code - NEW
```

### Step 5: Do it correctly
```
Action: Move #2 to IN PROGRESS
Result:
  #1 - Write report - IN PROGRESS
  #2 - Review code - IN PROGRESS
```

### Step 6: Complete #1
```
Action: Move #1 to DONE
Result:
  #1 - Write report - DONE
  #2 - Review code - IN PROGRESS
```

---

## WHAT YOU DON'T NEED (Yet)

**Skip these for now** (we'll add later):

- ❌ Dates/timestamps
- ❌ Priority scores
- ❌ Descriptions
- ❌ Categories
- ❌ Multiple users
- ❌ Backups
- ❌ Reports
- ❌ Search/filters

**Just focus on: Add item, Move item, List items**

---

## SUCCESS CRITERIA

You've built the simplest version when:

✅ Can add items (auto-assigns ID, sets to NEW)
✅ Can move items forward one stage at a time
✅ Cannot skip stages (validation works)
✅ Can list all items with current stage
✅ Each item has unique ID

**Once this works, go to Page 2.**

---

## PSEUDOCODE (Not Real Code)

```
ITEMS = empty list

FUNCTION add_item(name):
    new_id = count of items + 1
    create item with:
        id = new_id
        name = name
        stage = "NEW"
    add item to ITEMS
    show "Created #new_id"

FUNCTION move_item(id, new_stage):
    find item with this id
    current_stage = item's current stage

    if current_stage is "NEW" and new_stage is "DONE":
        show "ERROR: Cannot skip stages"
        stop

    if current_stage is "DONE":
        show "ERROR: Already done"
        stop

    item's stage = new_stage
    show "Moved #id to new_stage"

FUNCTION list_items():
    for each item in ITEMS:
        show "item.id - item.name - item.stage"
```

---

## NEXT STEP

**Go to Page 2: Add More Stages**

Once you can add/move/list items through 3 stages, we'll expand to more stages (like the RESEARCH 2 7-phase system).
