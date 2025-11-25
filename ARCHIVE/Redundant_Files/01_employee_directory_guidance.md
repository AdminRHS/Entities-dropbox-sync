# Employee Directory Guidance

## Overview
This document provides guidance on automatic participant identification in call transcripts using the Remote Helpers Employee Directory.

## Employee Directory (32 Employees)

### HR (2 employees)
1. **Rekonvald Viktoriia** (ID: 83953) - Recruiter, Lead generator | Austria | @kkktouse | viktoriiarekonvald@gmail.com
2. **Nealova Evgeniya** (ID: 72889) - Recruiter | Ukraine | @ievgeniia_nealova | zp4058203@gmail.com

### AI (3 employees)
3. **Zasiadko Matvii** (ID: 86981) - Prompt engineer | Ukraine | @matviy04 | matvey.z.2004@icloud.com
4. **Artemchuk Nikolay** (ID: 37226) - Project manager, Lead generator | Ukraine | @twinklelilsta | artemchuknn@gmail.com
5. **Perederii Vladislav** (ID: 86246) - Prompt engineer | Ukraine | @WeAllWillDie | vladyslav.perederii@nure.ua

### Video (3 employees)
6. **Panchenko Diana** (ID: 39273) - Video Editor | Ukraine | @diblackprod | panchenko.di@yahoo.com
7. **Podolskyi Sviatoslav** (ID: 299) - Video Editor, Graphic Designer | Ukraine | neozoy.x@gmail.com
8. **Azanova Darya** (ID: 80190) - Video Editor | Ukraine | @daria_azanova | azanova1997@gmail.com

### Sales (1 employee)
9. **Kovalska Anastasiya** (ID: 45405) - Sales Manager, SMM Manager, Personal Assistant | Ukraine | @anastasia_kovalska | avkovalska23@gmail.com

### Design (9 employees)
10. **Shelep Olha** (ID: 86641) - UI/UX designer | Ukraine | @olyashelep | shelep.olya@gmail.com
11. **Bogun Polina** (ID: 87537) - UI/UX designer | Austria | @polinabogun | pollybogun@gmail.com
12. **Kucherenko Iuliia** (ID: 228) - Graphic Designer, Web Designer | Ukraine | viligosh17@gmail.com
13. **Chobotar Yuliia** (ID: 87826) - UI/UX designer, Graphic Designer | Ukraine | @Lulu_ly | chobotar.ly@gmail.com
14. **Vereteno Marta** (ID: 626) - Graphic designer | Moldova | sd.designsmart@gmail.com
15. **Safonova Elleonora** (ID: 87995) - UI/UX designer | Germany/Ukraine | @eleonora_lee | ellesafonova@gmail.com
16. **Skrypkar Vilhelm** (ID: 333) - Illustrator, Graphic Designer | Ukraine | @bull_will | ntwilson666@gmail.com
17. **Hlushko Mariia** (ID: 88626) - Illustrator, Graphic Designer, Project manager | Ukraine | @white_book_wizard | mariiahlushko9@gmail.com
18. **Shymkevych Iryna** (ID: 88357) - UI/UX designer | Ukraine | @lamperry | shymkevychiryna@gmail.com

### Dev (3 employees)
19. **Klimenko Yaroslav** (ID: 86478) - Frontend Developer | Ukraine | @nosebl33d | klimyarik13@gmail.com
20. **Kizilova Olha** (ID: 178) - Backend Developer | Ukraine | @OlgaKizilova | olgascorpions26@gmail.com
21. **Danylenko Liliia** (ID: 72754) - Frontend/Full-Stack Developer | Ukraine | @Liliia_Danylenko | liliia.danylenko.dev@gmail.com

### LG (11 employees)
22. **Hanan Zaheur** (ID: 87984) - Lead generator, Personal Assistant | China | @hananZ2003 | hanane.zaheur@gmail.com
23. **Rybak Nataliia** (ID: 88054) - Lead generator, Content manager | Ukraine | @NataliaRybak91 | rybaknatalia91@gmail.com
24. **Shkinder Kseniia** (ID: 87157) - Lead generator, Translator, Personal Assistant | Ukraine | @shkinderksenia | k49209700@gmail.com
25. **Archibong Isaac** (ID: 86453) - Lead generator, Prompt engineer | Nigeria | @Archibong222 | archibong222@gmail.com
26. **Iskandarova Anush** (ID: 85829) - Sales Manager, Personal Assistant | Kazakhstan/Ukraine | @lskandarova | nushnushok@icloud.com
27. **Davlatmamadova Firuza** (ID: 84059) - Lead generator, Chat operator | Azerbaijan/Kazakhstan | davlatmamadova.firuza@bk.ru
28. **Peneva Plamena** (ID: 86297) - Lead generator | Bulgaria | @pvpeneva | plamenapeneva1206@gmail.com
29. **Burda Anna** (ID: 84138) - Lead generator, Translator, Sales Manager | Ukraine | @burdaanna8 | burdaanna8@gmail.com
30. **Pasichna Anastasiia** (ID: 88105) - Personal Assistant, Financial manager | Ukraine | @aabeeille | anastasiya.pasichnaya@gmail.com
31. **Alakbarova Ulviyya** (ID: 88270) - Lead generator | Azerbaijan | @sura_alakbarova | ulviyyelekberova@gmail.com
32. **Bindiak Dana** (ID: 87396) - Lead generator, Translator | Ukraine | @Dana_Bindiak | bindyak.dv09@gmail.com

---

## Participant Identification Strategies

### 1. Direct Name Match
Match first name, last name, or full name to directory
- Handle name variations: Nikolay/Nikolai/Mykola, Viktoriia/Victoria/Vika
- Case-insensitive matching
- Common diminutives: Olya/Olha, Zhenya/Evgeniya

### 2. Contextual Clues
- **Department context**: If discussing design work, likely from Design department
- **Project context**: If discussing specific project, match to known stakeholders
- **Role context**: "Our frontend developer" → Check Dev department
- **Location mentions**: "Our person in Austria" → Rekonvald Viktoriia or Bogun Polina
- **Profession mentions**: "Our recruiter in Austria" → Rekonvald Viktoriia

### 3. Communication Handles
- Match Telegram handles: @twinklelilsta → Artemchuk Nikolay
- Match email addresses: artemchuknn@gmail.com → Artemchuk Nikolay

### 4. Voice/Speech Patterns
- **Language spoken**: Chinese speaker → likely Hanan Zaheur (LG, China)
- **Accent/location**: Nigerian accent → Archibong Isaac (LG, Nigeria)
- **Professional terminology**: Discussing React/TypeScript → likely Dev department

### 5. Multi-lingual Name Matching
- Russian/Ukrainian variations: Дарья/Darya, Євгенія/Evgeniya, Михайло/Matvii
- Handle Cyrillic transliterations
- Recognize common Russian diminutives: Женя (Zhenya) = Evgeniya

---

## Confidence Levels

### High Confidence
- Direct name match + context alignment
- Exact ID or email match
- Name + department + role all match

### Medium Confidence
- Partial name match with strong context
- Role-based identification with project context
- Telegram handle match

### Low Confidence
- Weak contextual clues only
- Generic role mention without specifics
- Requires manual verification

---

## Output Format

When identifying participants, use this format:

```
**Artemchuk Nikolay** (ID: 37226) - Project manager, Lead generator | AI | Confidence: High
**Shelep Olha** (ID: 86641) - UI/UX designer | Design | Confidence: Medium - [Reason: Discussing Figma work]
**Unknown Participant** - Unknown | Possibly LG Department | Confidence: Low - *Requires manual verification*
```

---

## Integration into Daily Report Prompts

### Purpose Section
Add employee directory reference:
- "This prompt uses the Remote Helpers Employee Directory (32 employees) to automatically identify participants"

### Department Context Section
Include employee list for the specific department:
```markdown
### {Department} Employees
- Employee 1 (ID: xxxxx) - Role
- Employee 2 (ID: xxxxx) - Role
```

### Department Instructions Section
Add participant identification step:
```markdown
**Step 1.1: Identify Participants**
- Match all mentioned names to Employee Directory
- Assign confidence levels (High/Medium/Low)
- Flag unmatched participants for manual verification
- Include employee ID, department, and role for all matches
```

### Quality Standards Section
Add employee identification quality criteria:
- All participants must be matched against Employee Directory
- Include confidence levels for all matches
- Flag unidentified participants with contextual clues
- Use full names with IDs in all reports

---

## Department Distribution
- **HR**: 2 employees (6.25%)
- **AI**: 3 employees (9.4%)
- **Video**: 3 employees (9.4%)
- **Sales**: 1 employee (3.1%)
- **Design**: 9 employees (28.1%)
- **Dev**: 3 employees (9.4%)
- **LG**: 11 employees (34.4%)

Use this distribution to inform probability when context is ambiguous.

---

*Last Updated: November 7, 2025*
