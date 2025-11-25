# Social Media Graphics Creation with UI Kit and Design Guidelines

**Purpose**: Create social media graphics using mascot prompts, UI kit, and design guidelines for non-designers following a comprehensive workflow.

**Version**: 1.0  
**Date**: 2025-11-21  
**Status**: Active  
**Related Prompts**: CREATIVES/Mascot_Prompting_Documents_Index.md

---

## Overview

This comprehensive workflow enables non-designers to create social media graphics by providing mascot prompts, UI kit, design guidelines, and reference images to AI. The process involves multiple iterations to refine prompts and create user-friendly instructions.

**Primary Use Case**: Enabling non-designers to create branded social media graphics  
**Target Platform**: ChatGPT (with image generation)  
**Department**: DGN (Design) - but used by all departments

---

## Prompt Instructions

### Step 1: Mascot Prompt Creation

```
Hello chat! i'm a graphic designer. I need the prompt for recreating this mascot in generative AI
[Attach mascot image]
```

### Step 2: Mascot Prompt Refinement

```
this prompt has to be used during creation of bigger graphics, so avoid using phrasing like "Create a cute..." or "The mascot should look...". Use this example of the prompt. And i want the generated images to be versatile so avoid including objects that the mascot holds as they will be generated over and over again
```

### Step 3: UI Kit and Design Guidelines

```
Now please analyze these social media graphics and create a universal UI kit and design guidelines for this brand so I can create new graphics of the same stylistics by giving AI them and those reference graphics
[Attach reference graphics]
```

### Step 4: Color and Typography Refinement

```
move Light Peach / Light Beige (#F5C6A5) to secondary colors the main titles font is Sofia Sans Condensed separate UI kit and the design guides
```

### Step 5: Master Prompt Creation

```
Great! And now give me the prompt, so I will provide an AI with the prompt, the UI kit and the design guidelines, the reference pictures, then I will give it the new post theme, title or other details - and AI will generate the graphics like those examples
```

### Step 6: Placeholder Refinement

```
in the prompt: - leave placeholders for the main titles and the rest of design elements that the graphics has to have - accentuate the "full-time/part-time, language, location, etc" are only for example and don't have to be on the image unless directly specified - give directions to create more picturesque background, like on these references
```

### Step 7: Placeholder Behavior Clarification

```
look at the generated image. another chat put texts from placeholders on it. accentuate in this updated prompt that it puts stuff from placeholders only if user explicitly fills them, otherwise it doesn't
```

### Step 8: User Instructions Creation

```
Good. I want to turn it into a comprehensive instruction for employees who are not designers and will have to generate that graphics having only topic (or some extra requirements) of the post and access to the folder containing the mascot references, posts references, prompt, ui kit, and design guidelines. Please write to them what to upload to the AI (chatgpt), which prompt to use, how to add extra requirements (if they have any), and how to prompt the AI in the continuation of the dialog if they want to add some elements or change something on the graphics
```

### Step 9: Mascot File Addition

```
add that they have to add the mascot prompt file too
```

---

## Usage Workflow for Non-Designers

### Step 1: Gather Materials
1. Access folder with:
   - Mascot references
   - Post references (example graphics)
   - Mascot prompt file
   - UI kit file
   - Design guidelines file
   - Master prompt

### Step 2: Prepare ChatGPT Session
1. Open ChatGPT
2. Upload all required files:
   - Mascot references
   - Post references
   - Mascot prompt
   - UI kit
   - Design guidelines

### Step 3: Execute Master Prompt
1. Paste master prompt
2. Provide post theme/title/details
3. Specify any extra requirements
4. Generate graphics

### Step 4: Refine (if needed)
1. Request specific changes
2. Add or remove elements
3. Adjust colors/layout
4. Finalize design

---

## Required Files Structure

### Folder Contents
```
Graphics_Creation_Folder/
├── mascot_references/
│   └── [mascot images]
├── post_references/
│   └── [example graphics]
├── mascot_prompt.md
├── ui_kit.md
├── design_guidelines.md
└── master_prompt.md
```

---

## Master Prompt Structure

The master prompt should include:
- **Mascot Description**: From mascot prompt file
- **UI Kit Reference**: Colors, fonts, elements
- **Design Guidelines**: Style rules, composition
- **Placeholders**: For titles and dynamic content
- **Background Guidelines**: Pictorial style requirements
- **Placeholder Behavior**: Only fill if explicitly provided

---

## Examples

### Example Input
**Post Theme**: "New Job Opening - Frontend Developer"  
**Extra Requirements**: Include salary range, remote work option

### Example Output
Social media graphic matching brand style with:
- Mascot integrated
- Brand colors and fonts
- Post title in placeholder
- Pictorial background
- Required elements included

---

## Best Practices

- ✅ Always include mascot prompt file
- ✅ Upload all reference materials
- ✅ Use placeholders for dynamic content
- ✅ Follow design guidelines strictly
- ✅ Only fill placeholders when explicitly requested
- ❌ Don't skip mascot prompt file
- ❌ Don't fill placeholders automatically
- ❌ Don't deviate from UI kit colors/fonts

---

## Version History

- v1.0 (2025-11-21): Initial integration from personal prompts collection

