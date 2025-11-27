# Job Sites Deep Research Prompt

**Purpose**: Systematically discover and document job posting platforms and CV sourcing channels across traditional sites, bulletin boards, Telegram groups, and Facebook communities
**Version**: 1.0.0
**Date**: 2025-11-14
**Status**: Active
**Related Prompts**: CV_Parser_v1.md, Communication_Templates_Prompt.md, CRM_Data_Entry_Prompt.md

---

## 🎯 Research Objective

**MISSION**: Conduct comprehensive research to identify job posting platforms and candidate CV sourcing channels across four platform types: traditional job sites, online bulletin boards, Telegram groups, and Facebook communities.

**KEY GOALS**:
1. Discover traditional job boards not yet in our 23-site library
2. Identify bulletin boards with active job posting sections
3. Map active Telegram job channels by country, profession, and industry
4. Document Facebook job groups with posting capabilities
5. Classify all platforms by profession, department, geography, and features
6. Integrate findings with LIBRARIES (Professions) and TASK_MANAGERS frameworks
7. Enable strategic candidate sourcing and multi-platform job posting

---

## 📊 Current Baseline

**Existing Job Sites Library**: 23 platforms documented
- **File Location 1**: `C:\Users\anast\Dropbox\HR Nov25\LIBRARIES\job sites.md`
- **File Location 2**: `C:\Users\anast\Dropbox\AI Nov25\Perederii Vladislav\job_sites.json`

**Current Geographic Coverage**:
- Eastern Europe: Ukraine, Poland, Lithuania, Moldova, Azerbaijan, Kazakhstan
- Western Europe: Germany, Sweden, UK, Switzerland, Spain, France, Ireland, Belgium, Austria, Norway, Italy
- North America: USA, Canada
- Other: Netherlands

**Platform Types Currently Documented**:
- Traditional job sites only (Work.ua, LinkedIn, Indeed, etc.)
- ⚠️ **Missing**: Bulletin boards, Telegram channels, Facebook groups

**Current Languages Supported**:
- English, Ukrainian, Polish, Russian, Lithuanian, German, Swedish, French, Spanish, Italian, Azerbaijani, Kazakh, Romanian

---

## 🔍 Platform Types to Research

### 1. Traditional Job Sites ⭐⭐⭐⭐⭐
**Definition**: Dedicated platforms built specifically for job postings and candidate sourcing

**Characteristics**:
- Professional interface with job posting forms
- Resume/CV database or candidate profiles
- Search and filter capabilities
- Employer accounts and dashboards
- Often paid services with tiered pricing

**Examples**:
- Work.ua, LinkedIn, Indeed, Djinni, Pracuj.pl, StepStone, Reed.co.uk

**Research Focus**:
- Find gaps in current 23-site coverage
- Discover niche/industry-specific boards
- Identify emerging platforms (launched 2023-2025)

---

### 2. Bulletin Boards (Classifieds) ⭐⭐⭐⭐
**Definition**: Online classified advertisement platforms with job posting sections

**Characteristics**:
- General marketplace with job category
- Often free or low-cost posting
- Local/regional focus common
- Less structured than dedicated job sites
- High volume, mixed quality

**Examples to Research**:
- OLX (multiple countries)
- Craigslist equivalents per country
- Local classified sites (e.g., Gumtree UK, Kijiji Canada, Leboncoin France)
- Mobile marketplace apps with job sections

**Research Queries**:
```
"[Country] classified ads jobs"
"[Country] free job posting classifieds"
"[City] bulletin board jobs"
"OLX jobs [country]"
"online classifieds [country]"
```

**Validation Steps**:
1. Confirm job posting section exists and is active
2. Check if job postings allowed (some sites restrict to services only)
3. Verify recent activity (posts within last 7 days)
4. Document posting requirements (registration, fees, verification)

---

### 3. Telegram Groups & Channels ⭐⭐⭐⭐⭐
**Definition**: Telegram communities and broadcast channels dedicated to job postings and hiring

**Characteristics**:
- Real-time job alerts
- Community-driven moderation
- Free access (no platform fees)
- Direct employer-candidate communication
- High engagement in active channels
- Language and region-specific

**Types of Telegram Job Communities**:

**A. Job Posting Channels** (Broadcast)
- Admins post job openings
- Members can view but not post
- High volume of postings
- Often curated or moderated

**B. Job Exchange Groups** (Discussion)
- Members can post job offers and CVs
- Community interaction and recommendations
- Less structured, higher noise

**C. Industry/Profession-Specific**
- IT jobs, designer jobs, sales jobs, etc.
- Niche communities with targeted audiences
- Better candidate quality

**D. Regional/Country-Specific**
- Ukraine IT jobs, Poland remote work, etc.
- Language-specific (Polish, Ukrainian, Russian, etc.)

**Research Queries**:
```
"Telegram job channel [country]"
"[Profession] jobs Telegram"
"IT jobs Telegram [country]"
"Remote work Telegram group"
"[City] job vacancies Telegram"
"Telegram job groups list [country]"
```

**Telegram Discovery Resources**:
- TGStat.com (Telegram analytics and directory)
- Telemetr.io (Telegram channel statistics)
- TelegramChannels.me (Channel directory)
- Google: "site:t.me [country] jobs"
- Ask in existing Telegram communities for recommendations

**Information to Document**:
- Channel/group name and username (@handle)
- Link (t.me/channelname)
- Member count
- Language(s)
- Posting frequency (posts per day/week)
- Type (broadcast channel vs discussion group)
- Professions/industries covered
- Geographic focus
- Posting rules (can employers post freely? approval required?)
- Quality assessment (spam level, moderation quality)

**Access Requirements**:
- Telegram account needed
- Some groups require approval to join
- May need to answer screening questions
- Phone number verification for Telegram account

---

### 4. Facebook (Meta) Groups ⭐⭐⭐⭐
**Definition**: Facebook community groups where job postings and CV sharing are allowed

**Characteristics**:
- Community-driven with admins/moderators
- Public or private groups
- Free to join and post (usually)
- High reach in certain demographics
- Mixed quality, requires moderation
- Strong in local/regional markets

**Types of Facebook Job Groups**:

**A. General Job Groups**
- "[Country/City] Jobs" or "Jobs in [Location]"
- All industries and professions
- High volume, broad audience

**B. Industry-Specific Groups**
- "IT Jobs [Country]", "AI Jobs [City]"
- "Remote Developer Jobs", "Graphic Designers Worldwide"
- Better targeting, relevant audience

**C. Profession-Specific Groups**
- "Frontend Developers Group"
- "HR Professionals Network"
- "Freelance Designers"

**D. Company/Network Groups**
- Alumni groups (university, bootcamp)
- Expat communities (e.g., "Ukrainians in Poland")
- Professional associations

**E. Remote Work Groups**
- "Remote Work Opportunities"
- "Digital Nomad Jobs"
- Global reach, remote-first jobs

**Research Queries** (within Facebook search):
```
"Jobs [country]"
"[Profession] jobs"
"[City] job vacancies"
"[Industry] hiring"
"Remote [profession] jobs"
"Freelance [profession]"
"[Country] praca" (Polish for work)
"[Country] работа" (Russian for work)
```

**Facebook Discovery Methods**:
1. **Direct Facebook Search**: Use Facebook's group search with job-related keywords
2. **Google Search**: `site:facebook.com/groups "[country] jobs"`
3. **Community Recommendations**: Ask in existing groups for related job groups
4. **Cross-Platform**: Check if job sites or Telegram channels mention Facebook groups
5. **Join Related Groups**: Admins often manage multiple related groups

**Information to Document**:
- Group name
- Facebook URL (facebook.com/groups/[groupid])
- Member count
- Public or Private
- Approval required to join (Yes/No)
- Posting rules (Do they allow job postings? How many per week? Format requirements?)
- Activity level (posts per day/week)
- Language(s)
- Geographic focus
- Professions/industries covered
- AI responsiveness
- Quality assessment (spam management, post quality)

**Access Requirements**:
- Facebook account required
- Profile may need to be somewhat complete (not brand new account)
- Private groups require approval (may take 1-3 days)
- Some groups ask screening questions before approval
- AI may check your profile before approving

---

## 🗺️ Geographic Research Framework

### Research by Region

For each platform type, systematically cover:

**Eastern Europe** (Priority: High)
- Ukraine, Poland, Lithuania, Moldova, Belarus, Romania, Bulgaria, Czech Republic, Slovakia, Hungary

**Western Europe** (Priority: High)
- Germany, UK, France, Netherlands, Switzerland, Austria, Belgium, Sweden, Norway, Denmark, Finland, Ireland, Spain, Portugal, Italy

**North America** (Priority: Medium)
- USA, Canada

**Other Regions** (Priority: Low - Optional)
- Latin America: Mexico, Brazil, Argentina
- Asia-Pacific: India, Philippines, Vietnam, Thailand
- MENA: UAE, Saudi Arabia, Israel, Egypt

### Multi-Country Platforms

Prioritize platforms with coverage in 3+ countries:
- Indeed (global)
- LinkedIn (global)
- Jooble (multiple countries)
- Glassdoor (multiple countries)
- Europa.eu EURES (EU-wide)

---

## 📐 Advanced Classification System

Classify every platform across **10 dimensions**:

### Dimension 1: Platform Type
**Options**:
- `Job Site` - Dedicated job board
- `Bulletin Board` - Classified ads platform
- `Telegram` - Telegram channel or group
- `Facebook` - Facebook group
- `Hybrid` - Multiple platform types (e.g., site + Telegram channel)

**Tag Format**: `platform_type: "Job Site"`

---

### Dimension 2: Purpose
**Options**:
- `Job Postings Only` - Employers post jobs, candidates browse
- `CV Database Only` - Candidate profiles/CVs, employers search
- `Both` - Job postings + CV database
- `Talent Marketplace` - Matching platform with bidding/proposals

**Tag Format**: `purpose: "Both"`

**Examples**:
- Work.ua → Both (post jobs + search CVs)
- Djinni → Both (job board + developer profiles)
- Telegram job channel → Job Postings Only (one-way broadcast)
- Facebook job group → Both (jobs posted + people share CVs)

---

### Dimension 3: Professions Supported

Map to **LIBRARIES/Professions** entity structure:

**Professions List** (from `C:\Users\anast\Dropbox\Entities\LIBRARIES\Professions`):

**Managers Department**:
- hr manager
- lead generator
- project manager
- sales manager
- seo manager
- seo manager tech

**Developers Department**:
- front end developer
- back end developer
- full stack developer

**Designers Department**:
- graphic designer
- ui/ux designer
- motion designer
- 3d designer

**Marketers Department**:
- smm (Social Media Manager)
- content manager
- seo manager

**Videographers Department**:
- video editor
- animator

**Other Professions**:
- recruiter
- personal assistant
- ai engineer

**Tag Format**: Array of professions
```json
"professions_supported": [
  "front end developer",
  "back end developer",
  "full stack developer",
  "ui/ux designer"
]
```

**Classification Rules**:
- **General platforms** (Indeed, LinkedIn): Tag with `"All Professions"`
- **Tech-focused platforms** (Djinni, DOU.ua): List specific tech professions
- **Industry-specific platforms**: List only relevant professions
- **Telegram/Facebook groups**: List professions explicitly mentioned in group description or observed in posts

---

### Dimension 4: Departments

Map to department structure from Professions entity:

**Departments**:
- Managers
- Developers
- Designers
- Marketers
- Videographers
- Other

**Tag Format**: Array of departments
```json
"departments": ["Developers", "Designers"]
```

**Examples**:
- Behance → `["Designers"]`
- GitHub Jobs → `["Developers"]`
- LinkedIn → `["Managers", "Developers", "Designers", "Marketers", "Videographers", "Other"]`

---

### Dimension 5: Geography

**Tag Format**:
```json
"geography": {
  "countries": ["Poland", "Ukraine"],
  "regions": ["Eastern Europe"],
  "cities": ["Warsaw", "Krakow"],
  "scope": "Regional" // or "Country", "Multi-Country", "Global"
}
```

**Scope Definitions**:
- `Local/City` - Single city focus (e.g., "Kyiv IT Jobs" Telegram)
- `Country` - Single country (e.g., Work.ua → Ukraine)
- `Regional` - Multiple countries in one region (e.g., Baltic job board)
- `Multi-Country` - Select countries across regions
- `Global` - Worldwide reach (LinkedIn, Remote.co)

---

### Dimension 6: Languages Supported

**Tag Format**: Array of ISO language codes
```json
"languages": ["EN", "PL", "UA", "RU"]
```

**Common Languages**:
- EN (English)
- UA (Ukrainian)
- PL (Polish)
- RU (Russian)
- DE (German)
- FR (French)
- ES (Spanish)
- IT (Italian)
- SV (Swedish)
- NL (Dutch)
- LT (Lithuanian)
- RO (Romanian)
- AZ (Azerbaijani)
- KK (Kazakh)

**Classification**:
- Check platform interface language options
- Note language of job postings (may differ from interface)
- For Telegram/Facebook: language(s) used in community

---

### Dimension 7: Access & Pricing

**Access Level**:
- `Free` - No cost to post or browse
- `Freemium` - Free basic, paid premium features
- `Paid` - Requires payment to post or access CV database
- `Enterprise` - Enterprise contracts only

**Pricing Details** (if available):
```json
"pricing": {
  "access_level": "Freemium",
  "free_features": ["Browse jobs", "Apply"],
  "paid_features": ["Post unlimited jobs", "CV database access", "Featured listings"],
  "typical_cost": "50-200 EUR per month",
  "notes": "Free trial available"
}
```

**For Telegram/Facebook**:
```json
"pricing": {
  "access_level": "Free",
  "platform_fee": "None",
  "notes": "Community-managed, no platform fees"
}
```

---

### Dimension 8: Features Available

**Feature Checklist**:
- ✅ Bulk posting capability (post to multiple positions at once)
- ✅ Resume/CV database search
- ✅ AI-powered matching or filtering
- ✅ ATS (Applicant Tracking System) integration
- ✅ Employer branding (company pages, reviews)
- ✅ Job alerts (for candidates)
- ✅ Application tracking
- ✅ Interview scheduling
- ✅ Multi-language interface
- ✅ Mobile app availability
- ✅ Analytics and reporting
- ✅ Featured/promoted listings

**Tag Format**:
```json
"features": {
  "bulk_posting": true,
  "cv_database": true,
  "ai_matching": false,
  "ats_integration": false,
  "employer_branding": true,
  "job_alerts": true,
  "application_tracking": true,
  "mobile_app": true,
  "analytics": true,
  "promoted_listings": true
}
```

**Note**: For Telegram/Facebook groups, most features will be `false` or `N/A` except:
```json
"features": {
  "bulk_posting": "N/A",
  "cv_database": "Informal (people post CVs)",
  "direct_messaging": true,
  "community_discussion": true,
  "real_time_updates": true
}
```

---

### Dimension 9: Target Audience

**Options** (can select multiple):
- `Employers` - Companies posting jobs
- `Candidates` - Job seekers browsing and applying
- `Recruiters` - Third-party recruiters sourcing talent
- `Freelancers` - Independent contractors
- `Agencies` - Recruitment agencies

**Tag Format**:
```json
"target_audience": ["Employers", "Candidates", "Recruiters"]
```

**Examples**:
- LinkedIn → All audiences
- Djinni → Employers + Candidates (tech)
- Telegram job channel → Candidates (passive, receive alerts)
- Facebook job group → Employers + Candidates (both post)

---

### Dimension 10: Job Types Supported

**Job Type Options**:
- Full-time
- Part-time
- Contract
- Freelance / Project-based
- Internship
- Remote
- Hybrid (remote + office)
- On-site

**Tag Format**:
```json
"job_types": ["Full-time", "Remote", "Contract", "Freelance"]
```

**Examples**:
- General job board → All types
- "Remote Work" Telegram → Remote, Freelance
- Freelancer-focused platform → Freelance, Project-based

---

## 🎯 Advanced Sorting Methods

Use these **7 sorting strategies** to organize and prioritize platforms:

### Sorting Method 1: Multi-Criteria Matrix

**Purpose**: Filter platforms by multiple dimensions simultaneously

**Use Cases**:
- "Show me Telegram groups for Developers in Poland"
- "Find free job boards with CV database in Ukraine"
- "Which platforms support Designers in Western Europe?"

**Implementation**:
```
Platform Type: Telegram
Department: Developers
Geography: Poland
Access Level: Free
→ Results: IT Jobs Poland Telegram, Polish Developers Group, etc.
```

**Matrix Dimensions** (combine any 2-4):
- Platform Type × Profession × Geography
- Purpose × Department × Access Level
- Platform Type × Geography × Languages

**Output Format**: Filterable table or spreadsheet

---

### Sorting Method 2: Purpose-Based Segmentation

**Purpose**: Separate platforms by primary use case

**Segments**:

**A. Job Posting Focused**
- Platforms best for posting jobs and receiving applications
- Metrics: Application volume, time-to-first-application
- Use for: Bulk hiring, ongoing recruitment

**B. CV Database Focused**
- Platforms best for proactive candidate sourcing
- Metrics: Database size, search filters, contact options
- Use for: Headhunting, niche roles, passive candidates

**C. Dual-Purpose (Both)**
- Platforms offering both job posting and CV search
- Metrics: Balance of features, overall traffic
- Use for: Comprehensive recruitment strategy

**D. Community-Driven (Telegram/Facebook)**
- Engagement-focused, direct communication
- Metrics: Member count, daily activity, response rates
- Use for: Hard-to-fill roles, niche professions, local markets

**Sorting Rule**: Within each segment, rank by monthly traffic or member count

---

### Sorting Method 3: Feature-Rich Scoring System

**Purpose**: Rank platforms by capability and sophistication

**Scoring Formula**:
```
Feature Score = Sum of:
- Bulk posting: +2 points
- CV database: +3 points
- AI matching: +2 points
- ATS integration: +1 point
- Employer branding: +1 point
- Analytics: +1 point
- Mobile app: +1 point
- Multi-language: +1 point
```

**Tiers**:
- **Tier 1** (10+ points): Full-featured platforms (LinkedIn, Indeed)
- **Tier 2** (6-9 points): Solid regional platforms (Work.ua, Pracuj.pl)
- **Tier 3** (3-5 points): Basic job boards
- **Tier 4** (0-2 points): Simple platforms (Telegram, bulletin boards)

**Use Case**: Prioritize platforms for enterprise clients or high-volume hiring

**Note**: Tier 4 platforms (Telegram, Facebook) may have **low feature scores** but **high engagement and reach** - do not dismiss them!

---

### Sorting Method 4: Geographic Penetration Score

**Purpose**: Assess platform reach within target markets

**Scoring**:
```
Penetration Score per Country =
  (Estimated Monthly Active Users in Country) / (Country's Online Workforce)

OR use qualitative assessment:
- Dominant (>50% market share): 5 points
- Strong (20-50%): 4 points
- Moderate (10-20%): 3 points
- Emerging (5-10%): 2 points
- Niche (<5%): 1 point
```

**Examples**:
- Work.ua in Ukraine → Dominant (5 points)
- LinkedIn in USA → Dominant (5 points)
- Djinni in Ukraine → Strong for IT (4 points)
- New Telegram channel → Emerging (2 points)

**Multi-Country Platforms**: Calculate average score across all countries covered

**Use Case**: Identify which platforms dominate in your target hiring regions

---

### Sorting Method 5: Profession Specialization Index

**Purpose**: Distinguish niche platforms from generalist platforms

**Specialization Score**:
```
Score = (# of professions supported) / (Total professions in taxonomy)

Result:
- 1.0 (or "All Professions") → Generalist
- 0.5-0.9 → Semi-specialized (e.g., all tech roles)
- 0.2-0.4 → Niche (e.g., only designers)
- <0.2 → Hyper-niche (e.g., only 3D designers)
```

**Taxonomy Reference**: 22 total professions in LIBRARIES/Professions

**Sorting Strategy**:

**For General Hiring**: Prioritize generalist platforms (score 0.8-1.0)
- LinkedIn, Indeed, Work.ua

**For Specific Roles**: Prioritize niche platforms (score 0.2-0.5)
- Hiring Frontend Developer → Djinni (tech-focused)
- Hiring Graphic Designer → Behance, Dribbble
- Hiring Video Editor → Videographer-specific Telegram groups

**Niche Platform Benefits**:
- Higher quality candidates (self-selected)
- Less competition from other employers
- Better targeting and relevance
- Community credibility

**Output**: Tag platforms as `Generalist`, `Tech-Focused`, `Creative-Focused`, `Sales-Focused`, etc.

---

### Sorting Method 6: Platform Activity & Engagement Level

**Purpose**: Prioritize platforms with active users and high engagement

**Metrics to Collect**:

**For Traditional Job Sites**:
- Monthly active job postings (rough estimate)
- Application rate (applications per job posting)
- Time-to-first-application
- Employer reviews or ratings

**For Telegram Channels/Groups**:
- Member count
- Posts per day/week
- Message engagement (replies, reactions)
- Member growth rate (if available via TGStat)

**For Facebook Groups**:
- Member count
- Posts per day
- Comments per post
- AI responsiveness

**Activity Score Tiers**:

**Job Sites**:
- High: 1000+ new job postings per month
- Medium: 100-1000 per month
- Low: <100 per month

**Telegram/Facebook**:
- High: 5+ posts per day, 10+ engagement per post
- Medium: 1-5 posts per day, 3-10 engagement
- Low: <1 post per day, <3 engagement

**Sorting Rule**: Within each platform type, rank by activity score (High → Medium → Low)

**Red Flags** (Deprioritize or Exclude):
- No posts in last 30 days
- AI inactive (no moderation visible)
- High spam ratio (>50% of posts are spam)
- Group locked or restricted

---

### Sorting Method 7: Department-Specific Optimization

**Purpose**: Recommend best platforms per department's unique needs

**Department Profiles**:

#### **Managers Department** (HR Manager, Project Manager, Sales Manager, Lead Generator)

**Best Platform Types**:
- Traditional job sites (high professionalism)
- LinkedIn (strong for managerial roles)
- Industry-specific job boards

**Prioritize**:
- CV database access (proactive sourcing)
- Senior-level candidate filters
- Platforms with professional networking

**Recommended Platforms** (examples):
- LinkedIn, Indeed, Executive job boards, Management Telegram groups

---

#### **Developers Department** (Frontend, Backend, Full Stack)

**Best Platform Types**:
- Tech-focused job boards (Djinni, DOU.ua, Stack Overflow Jobs)
- Telegram developer communities (highly active)
- GitHub Jobs, AngelList (startup focus)

**Prioritize**:
- Platforms with tech skill filters
- Developer communities (Telegram, Discord)
- Portfolio/GitHub profile integration

**Recommended Platforms** (examples):
- Djinni, DOU.ua, IT Jobs Telegram channels, GitHub, Stack Overflow, HackerRank

---

#### **Designers Department** (Graphic, UI/UX, Motion, 3D)

**Best Platform Types**:
- Portfolio platforms (Behance, Dribbble)
- Creative industry job boards
- Design Telegram/Facebook communities

**Prioritize**:
- Visual portfolio showcases
- Creative community engagement
- Freelance and project-based opportunities

**Recommended Platforms** (examples):
- Behance, Dribbble, Coroflot, Creative Telegram groups, Design Facebook groups

---

#### **Marketers Department** (SMM, Content Manager, SEO Manager)

**Best Platform Types**:
- General job boards (high volume)
- AI-specific job boards
- Facebook marketing groups

**Prioritize**:
- Platforms with marketing role filters
- Communities with case study sharing
- Freelance marketplaces

**Recommended Platforms** (examples):
- LinkedIn, Indeed, AI Hire, MarketingJobs.com, Facebook marketing groups

---

#### **Videographers Department** (Video Editor, Animator)

**Best Platform Types**:
- Creative job boards
- Freelance platforms (Upwork, Fiverr)
- Video production Telegram/Facebook groups

**Prioritize**:
- Portfolio/reel showcases
- Freelance and contract opportunities
- Creative community platforms

**Recommended Platforms** (examples):
- Behance, Mandy.com, ProductionHub, Videographer Telegram groups, Vimeo Jobs

---

**Department-Specific Sorting Output**:

Create department-specific platform recommendation lists:

```markdown
## Developers Department - Recommended Platforms

### Tier 1: Essential Platforms
1. Djinni (Ukraine) - Tech-focused, strong developer community
2. LinkedIn - Global reach, professional networking
3. IT Jobs Poland Telegram - High engagement, real-time postings

### Tier 2: Supplementary Platforms
4. DOU.ua - Ukrainian tech community
5. Stack Overflow Jobs - Developer-focused
6. GitHub Jobs - Open source community

### Tier 3: Niche Platforms
7. Frontend Developers Facebook Group
8. Remote Frontend Jobs Telegram
```

Repeat for all departments.

---

## 📝 Documentation Templates

### Template 1: Traditional Job Site Profile

```markdown
### [Platform Name]

**🔖 Basic Information**
- **Platform Type:** Job Site
- **URL:** [https://...]
- **Established:** [Year, if known]
- **Headquarters:** [Country]

**🌍 Geographic Coverage**
- **Countries:** [List]
- **Regions:** [Eastern Europe, Western Europe, etc.]
- **Scope:** Country / Regional / Multi-Country / Global

**💼 Purpose**
- **Job Postings:** Yes / No
- **CV Database:** Yes / No
- **Purpose Classification:** Job Postings Only | CV Database Only | Both | Talent Marketplace

**👥 Professions & Departments**
- **Professions Supported:** [List, or "All Professions"]
- **Departments:** [Managers, Developers, Designers, Marketers, Videographers, Other]
- **Specialization:** Generalist / Tech-Focused / Creative-Focused / [Other]

**🌐 Languages**
- **Interface Languages:** [EN, PL, UA, etc.]
- **Job Posting Languages:** [EN, PL, UA, etc.]

**💰 Pricing & Access**
- **Access Level:** Free / Freemium / Paid / Enterprise
- **Job Posting Cost:** [Free, €X per post, €X per month, etc.]
- **CV Database Access Cost:** [Free, €X per month, etc.]
- **Free Trial:** Yes / No
- **Notes:** [Any pricing details]

**✨ Features**
- ✅/❌ Bulk posting capability
- ✅/❌ Resume/CV database search
- ✅/❌ AI-powered matching or filtering
- ✅/❌ ATS integration available
- ✅/❌ Employer branding (company pages)
- ✅/❌ Job alerts for candidates
- ✅/❌ Application tracking
- ✅/❌ Interview scheduling tools
- ✅/❌ Mobile app available
- ✅/❌ Analytics and reporting
- ✅/❌ Featured/promoted listings

**📊 Activity & Reach**
- **Monthly Active Users:** [Estimate, if available]
- **Monthly Job Postings:** [Estimate]
- **Time-to-First-Application:** [Fast / Medium / Slow, or estimate]
- **Geographic Penetration:** Dominant / Strong / Moderate / Emerging / Niche
- **Activity Score:** High / Medium / Low

**🎯 Best For**
- [Use case description: e.g., "High-volume hiring in Poland"]
- [Target audience: e.g., "Tech companies hiring developers"]
- [Job types: e.g., "Full-time, remote, and hybrid roles"]

**🔗 TASK_MANAGERS Integration**
- **Related Task Templates:**
  - TASK-HR-001: Post Job Opening on [Platform]
  - TASK-HR-005: Search CV Database for [Profession]
  - TASK-HR-010: Respond to Candidate Applications
- **Related Workflows:**
  - Job Posting Creation Workflow
  - Candidate Sourcing Workflow

**📌 Notes**
- [Any additional observations, tips, or considerations]
- [Registration requirements]
- [Verification needed (email, company, etc.)]
- [Best practices for this platform]

---
```

---

### Template 2: Bulletin Board Profile

```markdown
### [Platform Name]

**🔖 Basic Information**
- **Platform Type:** Bulletin Board
- **URL:** [https://...]
- **Parent Company:** [If part of larger classifieds network]

**🌍 Geographic Coverage**
- **Countries:** [List]
- **Regions:** [List]
- **Scope:** Local / Country / Regional / Multi-Country

**💼 Job Section Details**
- **Job Section Available:** Yes / No
- **Job Posting Allowed:** Yes / No (some sites restrict to services)
- **Categories:** [Employment, Part-time, Freelance, etc.]
- **Purpose Classification:** Job Postings Only | Both (jobs + people post CVs)

**👥 Professions & Departments**
- **Professions Supported:** [List, or "All Professions"]
- **Departments:** [All / Specific]
- **Specialization:** Generalist (mixed industries)

**🌐 Languages**
- **Primary Language:** [EN, PL, UA, etc.]
- **Multi-language Support:** Yes / No

**💰 Pricing & Access**
- **Access Level:** Free / Low-cost
- **Job Posting Cost:** [Free, €X per post, etc.]
- **Registration Required:** Yes / No
- **Verification Required:** [Email, phone, none]

**✨ Features**
- ✅/❌ Free job posting
- ✅/❌ Location-based filtering
- ✅/❌ Contact info visible (email/phone)
- ✅/❌ Direct messaging between users
- ✅/❌ Photo/document upload (for CVs)
- ✅/❌ Mobile app

**📊 Activity & Reach**
- **Job Section Activity:** High / Medium / Low
- **Posts per Day:** [Estimate]
- **Response Rate:** [If known or estimated: Fast / Medium / Slow]
- **Quality Assessment:** [Professional / Mixed / Low quality]

**🎯 Best For**
- [Use case: e.g., "Local hiring in small cities"]
- [Job types: e.g., "Part-time, temporary, blue-collar roles"]
- [Advantages: e.g., "Free, high visibility in local market"]

**🔗 TASK_MANAGERS Integration**
- **Related Task Templates:**
  - TASK-HR-020: Post Job on Free Classifieds
  - TASK-HR-021: Monitor Bulletin Board Responses
- **Related Workflows:**
  - Low-Budget Job Posting Workflow

**⚠️ Considerations**
- **Moderation Quality:** [High / Medium / Low]
- **Spam Level:** [Low / Medium / High]
- **Professional Appearance:** [Yes / No / Mixed]
- **Candidate Quality:** [Professional / Mixed / Entry-level]

**📌 Notes**
- [Tips for using this platform effectively]
- [Posting best practices]
- [How to filter serious candidates]

---
```

---

### Template 3: Telegram Channel/Group Profile

```markdown
### [Channel/Group Name]

**🔖 Basic Information**
- **Platform Type:** Telegram
- **Type:** Broadcast Channel / Discussion Group
- **Username:** @[handle]
- **Link:** https://t.me/[channelname]
- **Member Count:** [Number] (as of [Date])

**🌍 Geographic Coverage**
- **Country/Region Focus:** [Poland, Ukraine, Europe, Global, etc.]
- **Scope:** Local / Country / Regional / Global

**💼 Purpose & Content**
- **Job Postings:** Yes / No
- **CV Sharing:** Yes / No (in discussion groups)
- **Purpose Classification:** Job Postings Only | Both
- **Content Type:** [Job ads, career advice, industry news, etc.]

**👥 Professions & Departments**
- **Professions Covered:** [List specific professions, or "All Professions"]
- **Departments:** [Developers, Designers, Managers, etc.]
- **Specialization:** [Tech-focused, Creative-focused, Generalist, etc.]

**🌐 Languages**
- **Primary Language(s):** [EN, PL, UA, RU, etc.]
- **Multi-language Posts:** Yes / No

**💰 Access**
- **Access Level:** Free
- **Platform Fee:** None
- **Join Approval Required:** Yes / No
- **Screening Questions:** Yes / No (describe if yes)

**✨ Community Features**
- ✅/❌ Public channel (anyone can join)
- ✅/❌ Broadcast channel (no member discussion)
- ✅/❌ Discussion group (members can post and comment)
- ✅/❌ AI-curated job postings only
- ✅/❌ Direct messaging allowed
- ✅/❌ Pinned important posts
- ✅/❌ Related resources (docs, links)

**📊 Activity & Engagement**
- **Posting Frequency:** [X posts per day / per week]
- **Engagement Level:** High / Medium / Low
- **Average Reactions per Post:** [Estimate]
- **Member Growth:** Growing / Stable / Declining
- **Last Active:** [Date of most recent post]

**🎯 Best For**
- [Use case: e.g., "Finding Frontend Developers in Poland"]
- [Advantages: e.g., "Real-time job alerts, direct communication"]
- [Job types: e.g., "Remote, freelance, full-time"]

**📋 Posting Rules**
- **Employers Can Post:** Yes / No / Requires approval
- **Posting Format:** [Free-form / Template required]
- **Posting Frequency Limit:** [X posts per week / No limit]
- **Prohibited Content:** [List if specified]

**🔗 TASK_MANAGERS Integration**
- **Related Task Templates:**
  - TASK-HR-030: Post Job to Telegram Channel
  - TASK-HR-031: Monitor Telegram Responses
  - TASK-HR-032: Engage with Candidates in Telegram Group
- **Related Workflows:**
  - Telegram Job Posting Workflow
  - Real-Time Candidate Engagement Workflow

**⚙️ Quality Assessment**
- **Moderation Quality:** High / Medium / Low / None
- **Spam Level:** Low / Medium / High
- **Post Quality:** Professional / Mixed / Low
- **AI Responsiveness:** Fast / Medium / Slow

**📌 Notes**
- [Tips for engaging in this community]
- [Best times to post]
- [How to contact admin if needed]
- [Related channels or groups]

---
```

---

### Template 4: Facebook Group Profile

```markdown
### [Group Name]

**🔖 Basic Information**
- **Platform Type:** Facebook Group
- **Group Name:** [Full name]
- **URL:** https://facebook.com/groups/[groupid]
- **Member Count:** [Number] (as of [Date])
- **Group Type:** Public / Private

**🌍 Geographic Coverage**
- **Country/Region Focus:** [Poland, Ukraine, Global, etc.]
- **Scope:** Local / Country / Regional / Global

**💼 Purpose & Content**
- **Job Postings Allowed:** Yes / No
- **CV Sharing Allowed:** Yes / No
- **Purpose Classification:** Job Postings Only | Both
- **Content Type:** [Job ads, networking, career advice, etc.]

**👥 Professions & Departments**
- **Professions Covered:** [List specific professions, or "All Professions"]
- **Departments:** [All, or specific departments]
- **Specialization:** [Tech, Creative, Sales, Generalist, etc.]

**🌐 Languages**
- **Primary Language(s):** [EN, PL, UA, etc.]
- **Multi-language Posts:** Yes / No

**💰 Access**
- **Access Level:** Free
- **Platform Fee:** None (Facebook group)
- **Join Approval Required:** Yes / No
- **Approval Time:** [Instant / 1-3 days / 1 week]
- **Screening Questions:** Yes / No (describe if yes)
- **Profile Requirements:** [Active profile, minimum friends, etc.]

**✨ Community Features**
- ✅/❌ Public group (visible to all)
- ✅/❌ Members can post freely
- ✅/❌ AI approval required per post
- ✅/❌ Direct messaging allowed between members
- ✅/❌ Files and documents can be uploaded
- ✅/❌ Events and meetups organized
- ✅/❌ Pinned post with group rules

**📊 Activity & Engagement**
- **Posting Frequency:** [X posts per day]
- **Engagement Level:** High / Medium / Low
- **Average Comments per Post:** [Estimate]
- **Average Reactions per Post:** [Estimate]
- **Member Growth:** Growing / Stable / Declining
- **Last Active:** [Date of most recent post]

**🎯 Best For**
- [Use case: e.g., "Finding local designers in Warsaw"]
- [Advantages: e.g., "High engagement, community trust"]
- [Job types: e.g., "Freelance, part-time, contract"]

**📋 Posting Rules**
- **Employers Can Post:** Yes / No
- **Posting Format:** [Free-form / Template required]
- **Posting Frequency Limit:** [X posts per week / per day]
- **Prohibited Content:** [Spam, duplicates, etc.]
- **Penalties:** [Post removal, member removal, ban]

**🔗 TASK_MANAGERS Integration**
- **Related Task Templates:**
  - TASK-HR-040: Post Job to Facebook Group
  - TASK-HR-041: Monitor Facebook Group Responses
  - TASK-HR-042: Engage with Candidates in Facebook Group
- **Related Workflows:**
  - Facebook Job Posting Workflow
  - Community Engagement Workflow

**⚙️ Quality Assessment**
- **Moderation Quality:** High / Medium / Low
- **Spam Level:** Low / Medium / High
- **Post Quality:** Professional / Mixed / Low
- **AI Responsiveness:** Fast / Medium / Slow / Absent
- **Community Vibe:** Professional / Casual / Mixed

**📌 Notes**
- [Tips for getting accepted to the group]
- [Best practices for posting]
- [How to engage authentically without spamming]
- [Related groups managed by same admins]
- [Observations about member demographics]

---
```

---

### Template 5: Comparison Matrix

Use this template to compare multiple platforms side-by-side:

```markdown
## Platform Comparison: [Category or Region]

| Platform Name | Type | Geography | Professions | Purpose | Access | Activity | Best For |
|--------------|------|-----------|------------|---------|--------|----------|----------|
| Work.ua | Job Site | Ukraine | All | Both | Freemium | High | General hiring in Ukraine |
| Djinni | Job Site | Ukraine, EU | Developers, Designers | Both | Free/Paid | High | Tech hiring |
| IT Jobs PL Telegram | Telegram | Poland | Developers | Job Postings | Free | High | Real-time dev jobs Poland |
| Warsaw Jobs Facebook | Facebook | Poland (Warsaw) | All | Both | Free | Medium | Local hiring in Warsaw |
| OLX.ua Jobs | Bulletin Board | Ukraine | All | Both | Free | Medium | Part-time, local jobs |

### Feature Comparison

| Platform | Bulk Post | CV Database | AI Match | Mobile App | Multi-language |
|----------|-----------|-------------|----------|------------|----------------|
| Work.ua | ✅ | ✅ | ❌ | ✅ | ✅ EN, UA |
| Djinni | ❌ | ✅ | ✅ | ✅ | ✅ EN, UA |
| IT Jobs PL Telegram | N/A | ❌ | ❌ | ✅ (Telegram) | ✅ PL, EN |
| Warsaw Jobs Facebook | N/A | ❌ | ❌ | ✅ (Facebook) | ✅ PL, EN |
| OLX.ua Jobs | ❌ | ❌ | ❌ | ✅ | ✅ UA, RU |

### Pricing Comparison

| Platform | Job Posting Cost | CV Database Cost | Notes |
|----------|------------------|------------------|-------|
| Work.ua | Free + Paid promotion | €50-150/month | Freemium model |
| Djinni | Free for employers | Free basic, €X for advanced | Candidates pay for premium |
| IT Jobs PL Telegram | Free | N/A | Community-managed |
| Warsaw Jobs Facebook | Free | N/A | No platform fees |
| OLX.ua Jobs | Free basic, paid featured | N/A | Low-cost promotions available |
```

---

## 🔗 Integration with Taxonomy Frameworks

### Integration 1: LIBRARIES/Professions Mapping

**Objective**: Tag every platform with relevant professions from the Professions entity

**Professions Entity Location**: `C:\Users\anast\Dropbox\Entities\LIBRARIES\Professions`

**Mapping Process**:

1. **Review platform scope**:
   - Read platform description, check job categories
   - For Telegram/Facebook: scan recent posts for job titles

2. **Match to professions**:
   - If platform covers all industries → Tag: `"All Professions"`
   - If tech-focused → Tag: `["front end developer", "back end developer", "full stack developer"]`
   - If creative-focused → Tag: `["graphic designer", "ui/ux designer", "motion designer", "3d designer"]`

3. **Document in platform profile**:
```json
"professions_supported": [
  "front end developer",
  "back end developer",
  "ui/ux designer"
]
```

4. **Create reverse index**:
```markdown
### Frontend Developer - Platform Recommendations

**Best Platforms for Hiring Frontend Developers**:
1. Djinni (Ukraine) - Tech-focused, 5000+ FE developers
2. LinkedIn (Global) - Professional network, global reach
3. IT Jobs Poland Telegram - Real-time postings, Polish market
4. Frontend Developers Facebook Group - Community engagement
```

Repeat for all 22 professions.

**Deliverable**: Profession-to-Platform mapping document

---

### Integration 2: TASK_MANAGERS Task Templates

**Objective**: Connect platforms to actionable Task Templates in TASK_MANAGERS framework

**TASK_MANAGERS Entity Location**: `C:\Users\anast\Dropbox\Entities\TASK_MANAGERS`

**Task Template Structure**: `ACTION + OBJECT + CONTEXT`

**Task Templates to Create/Link**:

#### Job Posting Tasks

**TASK-HR-001: Post Job Opening on [Platform]**
- **Action**: Post
- **Object**: Job Opening
- **Context**: on [Platform Name]
- **Tools Required**: Platform account, job description, company branding
- **Steps**:
  1. Log in to [Platform]
  2. Select "Post Job" or equivalent
  3. Fill job details (title, description, requirements, salary)
  4. Add company information
  5. Set job location and type (remote/on-site)
  6. Preview and publish
  7. Monitor for applications
- **Estimated Duration**: 20-30 minutes
- **Department**: HR
- **Profession**: hr manager, recruiter

**TASK-HR-002: Post Job Opening on Telegram Channel**
- **Action**: Post
- **Object**: Job Opening
- **Context**: on Telegram Channel
- **Tools Required**: Telegram account, channel access, job description
- **Steps**:
  1. Format job post according to channel template (if any)
  2. Include: Job title, Company, Location/Remote, Requirements, Contact info
  3. Post to Telegram channel
  4. Monitor for direct messages or comments
- **Estimated Duration**: 10-15 minutes
- **Department**: HR
- **Profession**: hr manager, recruiter

**TASK-HR-003: Post Job Opening on Facebook Group**
- **Action**: Post
- **Object**: Job Opening
- **Context**: on Facebook Group
- **Tools Required**: Facebook account, group membership, job description
- **Steps**:
  1. Ensure group membership approved
  2. Review group posting rules
  3. Format job post (engaging, clear, concise)
  4. Post to Facebook group
  5. Monitor comments and direct messages
  6. Engage with interested candidates
- **Estimated Duration**: 15-20 minutes
- **Department**: HR
- **Profession**: hr manager, recruiter

**TASK-HR-004: Bulk Post Job Opening to Multiple Platforms**
- **Action**: Post
- **Object**: Job Opening
- **Context**: to Multiple Platforms (Multi-Channel)
- **Tools Required**: Platform accounts, job description, tracking spreadsheet
- **Steps**:
  1. Prepare standardized job description
  2. Customize for each platform (format, length, tone)
  3. Post to Platform 1 (LinkedIn)
  4. Post to Platform 2 (Work.ua)
  5. Post to Platform 3 (IT Jobs Telegram)
  6. Post to Platform 4 (Facebook group)
  7. Log all postings in tracking sheet
  8. Set reminders to monitor each platform
- **Estimated Duration**: 1-1.5 hours
- **Department**: HR
- **Profession**: hr manager, recruiter

---

#### Candidate Sourcing Tasks

**TASK-HR-005: Search CV Database for [Profession]**
- **Action**: Search
- **Object**: CV Database
- **Context**: for [Profession] (e.g., Frontend Developer)
- **Tools Required**: Platform account with CV database access, search criteria
- **Steps**:
  1. Log in to platform
  2. Navigate to CV database / Candidate search
  3. Set filters (profession, skills, location, experience level)
  4. Review candidate profiles
  5. Shortlist promising candidates
  6. Initiate contact (message or connection request)
  7. Track outreach in CRM
- **Estimated Duration**: 1-2 hours
- **Department**: HR
- **Profession**: hr manager, recruiter

**TASK-HR-006: Monitor Telegram Channel for Candidate CVs**
- **Action**: Monitor
- **Object**: Telegram Channel
- **Context**: for Candidate CVs
- **Tools Required**: Telegram account, channel membership
- **Steps**:
  1. Join relevant Telegram channels
  2. Set notifications for new messages
  3. Scan daily for CV posts or candidate profiles
  4. Reach out to promising candidates via direct message
  5. Log candidates in CRM
- **Estimated Duration**: 20-30 minutes per day
- **Department**: HR
- **Profession**: hr manager, recruiter

---

#### Application Management Tasks

**TASK-HR-010: Respond to Candidate Applications from [Platform]**
- **Action**: Respond
- **Object**: Candidate Applications
- **Context**: from [Platform]
- **Tools Required**: Platform account, email templates, ATS or CRM
- **Steps**:
  1. Log in to platform
  2. Check new applications
  3. Review candidate profiles and resumes
  4. Send initial response (acknowledgment or next steps)
  5. Log candidates in ATS/CRM
  6. Schedule screening calls if qualified
- **Estimated Duration**: 30-60 minutes
- **Department**: HR
- **Profession**: hr manager, recruiter

---

**Deliverable**: Create 10-15 HR Task Templates linked to platform usage, add to TASK_MANAGERS

---

### Integration 3: Workflow Mapping

**Objective**: Map platforms into end-to-end hiring workflows

**Workflow Example 1: Multi-Platform Job Posting Workflow**

```yaml
Workflow Name: Multi-Platform Job Posting
Department: HR
Owner: hr manager
Trigger: New job requisition approved

Steps:
  1. Prepare Job Description
     - Action: Create
     - Object: Job Description
     - Tool: Google Docs, Notion
     - Duration: 1 hour

  2. Post to Primary Platforms
     - Action: Post
     - Object: Job Opening
     - Tools: LinkedIn, Work.ua, Djinni
     - Task Templates: TASK-HR-001 (repeated for each platform)
     - Duration: 1 hour

  3. Post to Community Platforms
     - Action: Post
     - Object: Job Opening
     - Tools: Telegram IT Jobs Channel, Facebook Developers Group
     - Task Templates: TASK-HR-002, TASK-HR-003
     - Duration: 30 minutes

  4. Monitor Applications
     - Action: Monitor
     - Object: Applications
     - Tools: All platforms
     - Task Templates: TASK-HR-010
     - Frequency: Daily
     - Duration: 1 hour per day

  5. Engage with Candidates
     - Action: Respond
     - Object: Candidate Messages
     - Tools: Platform messaging, Email
     - Task Templates: TASK-HR-010
     - Duration: 2 hours per week

Success Criteria:
  - Job posted on 5+ platforms
  - 20+ applications received within 2 weeks
  - 3+ qualified candidates moved to interview stage
```

**Workflow Example 2: Proactive Candidate Sourcing Workflow**

```yaml
Workflow Name: Proactive Candidate Sourcing
Department: HR
Owner: recruiter
Trigger: Hard-to-fill role or passive candidate search needed

Steps:
  1. Define Target Candidate Profile
     - Action: Define
     - Object: Candidate Profile
     - Tool: Notion, Google Docs
     - Duration: 30 minutes

  2. Search CV Databases
     - Action: Search
     - Object: CV Database
     - Tools: LinkedIn, Djinni, Work.ua
     - Task Templates: TASK-HR-005
     - Duration: 2 hours

  3. Monitor Community Platforms
     - Action: Monitor
     - Object: Telegram Channels, Facebook Groups
     - Tools: Telegram, Facebook
     - Task Templates: TASK-HR-006
     - Duration: 30 minutes per day

  4. Engage with Passive Candidates
     - Action: Send
     - Object: Outreach Message
     - Tools: LinkedIn, Email, Telegram
     - Task Templates: TASK-HR-007 (Personalized Outreach)
     - Duration: 3 hours per week

  5. Nurture Candidate Relationships
     - Action: Follow Up
     - Object: Candidate Communication
     - Tools: Email, CRM
     - Frequency: Weekly
     - Duration: 2 hours per week

Success Criteria:
  - 50+ candidates identified
  - 20+ outreach messages sent
  - 5+ interested candidates
  - 2+ candidates moved to interview stage
```

---

### Integration 4: Actions + Objects Taxonomy

**Actions Used in Job Site Research**:
- **Post** (job opening)
- **Search** (CV database, candidate profiles)
- **Monitor** (applications, channels, groups)
- **Respond** (to applications, messages)
- **Engage** (with candidates, communities)
- **Join** (Telegram channels, Facebook groups)
- **Message** (direct outreach to candidates)
- **Track** (applications, outreach, platform performance)

**Objects Used in Job Site Research**:
- **Job Opening** / Job Posting
- **CV** / Resume
- **Candidate Profile**
- **Application**
- **Telegram Channel** / Telegram Group
- **Facebook Group**
- **CV Database**
- **Outreach Message**
- **Platform Account**

**Cross-Reference**: Map these actions and objects to existing LIBRARIES/Actions and LIBRARIES/Objects entities

---

## 📋 Research Workflow

Execute research in **6 phases**:

### Phase 1: Traditional Job Sites Discovery (30 minutes)

**Objective**: Find job boards not yet in the 23-site library

**Search Queries**:
```
"[Country] job boards"
"best job sites [country] 2025"
"[country] employment websites"
"job posting sites [country]"
"[industry] job boards [country]"
"niche job boards [profession]"
```

**Sources**:
- Google search
- "Best job boards in [country]" articles
- Competitor analysis (check where competitors post jobs)
- Industry forums and discussions

**Validation**:
- ✅ Site is active (jobs posted in last 30 days)
- ✅ Job posting or CV database available
- ✅ Clear pricing and access requirements
- ✅ Professional appearance and functionality

**Documentation**:
- Use **Template 1: Traditional Job Site Profile**
- Fill all sections
- Add to platform inventory

---

### Phase 2: Bulletin Boards Discovery (20 minutes)

**Objective**: Identify classified ad platforms with job sections

**Search Queries**:
```
"[Country] classified ads"
"OLX [country] jobs"
"[Country] free classifieds"
"Craigslist [country] equivalent"
"[City] online bulletin board"
```

**Target Platforms**:
- OLX (Ukraine, Poland, etc.)
- Country-specific classified sites
- City/regional marketplaces
- Mobile app marketplaces (e.g., OfferUp, Letgo equivalents)

**Validation**:
- ✅ Job posting section exists
- ✅ Job postings are allowed (not just services)
- ✅ Activity: 5+ job posts in last 7 days
- ✅ Accessible without subscription

**Documentation**:
- Use **Template 2: Bulletin Board Profile**
- Note pros and cons
- Assess candidate quality

---

### Phase 3: Telegram Channels/Groups Discovery (45 minutes)

**Objective**: Find active Telegram communities for job postings and candidate sourcing

**Discovery Methods**:

**Method 1: Telegram Directory Sites**
- Visit: TGStat.com, Telemetr.io, TelegramChannels.me
- Search: "[Country] jobs", "[Profession] jobs", "IT jobs [country]"
- Filter by member count and activity

**Method 2: Google Search**
```
site:t.me "[country] jobs"
site:t.me "[profession] vacancies"
site:t.me "IT jobs Poland"
site:t.me "remote work [country]"
```

**Method 3: Telegram Internal Search**
- Open Telegram app
- Use search bar: "jobs [country]", "[profession] [country]"
- Browse results, join promising channels

**Method 4: Community Recommendations**
- Join 1-2 general job channels
- Ask admins or members for related channels
- Check pinned messages for channel lists

**Validation**:
- ✅ Member count: 500+ (minimum threshold)
- ✅ Activity: At least 1 post per day
- ✅ Last post: Within last 7 days
- ✅ Language: Relevant to your hiring regions
- ✅ Content: Job postings (not spam or unrelated content)
- ✅ Moderation: Evidence of admin activity

**Red Flags** (Skip):
- ❌ Last post >30 days ago
- ❌ High spam ratio (>50%)
- ❌ No admin activity
- ❌ Channel deleted or restricted

**Documentation**:
- Use **Template 3: Telegram Channel/Group Profile**
- Record member count and date
- Note posting rules
- Assess quality and relevance

**Goal**: Find 10-20 active Telegram channels per country/profession

---

### Phase 4: Facebook Groups Discovery (45 minutes)

**Objective**: Identify Facebook groups where job postings are allowed and active

**Discovery Methods**:

**Method 1: Facebook Internal Search**
- Log in to Facebook
- Navigate to Groups (left sidebar or facebook.com/groups)
- Search: "[Country] jobs", "[City] jobs", "[Profession] jobs", "Remote [profession]"
- Filter: Groups, by relevance or member count

**Method 2: Google Search**
```
site:facebook.com/groups "[country] jobs"
site:facebook.com/groups "[profession] [city]"
site:facebook.com/groups "remote jobs"
```

**Method 3: Explore Related Groups**
- Join 1-2 relevant groups
- Check "Suggested Groups" sidebar
- Look at group members' other group memberships (if visible)

**Method 4: Ask for Recommendations**
- Post in existing groups: "Can anyone recommend other job groups for [profession]?"
- Check group descriptions for links to related groups

**Validation**:
- ✅ Member count: 1,000+ (minimum threshold)
- ✅ Activity: At least 3-5 posts per day
- ✅ Job postings allowed: Check group rules or pinned post
- ✅ Last post: Within last 3 days
- ✅ Moderation: Evidence of admin oversight (spam removed, rules enforced)
- ✅ Post quality: Mix of job postings and candidate CVs

**Red Flags** (Skip):
- ❌ Group inactive (no posts in 7+ days)
- ❌ Group rules prohibit job postings
- ❌ AI approval required per post AND slow approval times
- ❌ High spam ratio (unrelated content)
- ❌ Irrelevant content (not job-focused)

**Access Considerations**:
- **Public Groups**: Can view content immediately, join instantly
- **Private Groups**: Must request to join, wait for approval (1-3 days)
  - Strategy: Request to join multiple groups simultaneously
  - Fill out screening questions if required
  - Wait for approval before documenting

**Documentation**:
- Use **Template 4: Facebook Group Profile**
- Note if approval required and estimated wait time
- Record posting rules and restrictions
- Assess community vibe and professionalism

**Goal**: Find 10-20 active Facebook groups per country/profession

---

### Phase 5: Validation & Classification (30 minutes)

**Objective**: Verify platform access and classify across all 10 dimensions

**Validation Steps**:

1. **Access Verification**
   - Can you register/join?
   - Are there restrictions (company email required, verification needed)?
   - Is the platform still operational?

2. **Feature Testing**
   - Try to post a test job (if allowed) or view posting interface
   - Check if CV database is accessible
   - Test search and filter functions

3. **Activity Check**
   - Confirm recent posts (within target timeframe)
   - Verify member/user engagement
   - Assess quality of content

4. **Classification**
   - Apply all 10 classification dimensions
   - Tag with professions, departments, geography
   - Document features, pricing, access level

**Deliverable**: Fully classified platform profiles ready for documentation

---

### Phase 6: Documentation & Reporting (30 minutes)

**Objective**: Create structured documentation for all discovered platforms

**Output Files**:

**1. Enhanced Markdown Documentation** (update existing job sites.md)
```markdown
# Job Sites Library - Comprehensive Platform Directory

Last Updated: [Date]
Total Platforms: [Number]

## Table of Contents
1. Traditional Job Sites
2. Bulletin Boards
3. Telegram Channels & Groups
4. Facebook Groups
5. Platform Comparison Matrices
6. Department-Specific Recommendations

---

## 1. Traditional Job Sites

### By Country

#### Ukraine
[Platform profiles using Template 1...]

#### Poland
[Platform profiles using Template 1...]

[Continue for all countries...]

---

## 2. Bulletin Boards

### By Country
[Platform profiles using Template 2...]

---

## 3. Telegram Channels & Groups

### By Country & Profession

#### Ukraine - Developers
[Platform profiles using Template 3...]

#### Poland - All Professions
[Platform profiles using Template 3...]

---

## 4. Facebook Groups

### By Country & Profession
[Platform profiles using Template 4...]

---

## 5. Platform Comparison Matrices

### Comparison by Country: Poland
[Use Template 5: Comparison Matrix...]

---

## 6. Department-Specific Recommendations

### Developers Department
**Best Platforms for Hiring Developers:**
1. [Platform] - [Why best]
2. [Platform] - [Why best]
...

[Repeat for all departments...]
```

**2. Structured JSON Data** (update existing job_sites.json)
```json
{
  "metadata": {
    "last_updated": "2025-11-14",
    "total_platforms": 100,
    "countries_covered": 25,
    "platform_types": ["Job Site", "Bulletin Board", "Telegram", "Facebook"]
  },
  "platforms": [
    {
      "id": "PLATFORM-001",
      "name": "Work.ua",
      "platform_type": "Job Site",
      "url": "https://www.work.ua",
      "countries": ["Ukraine"],
      "regions": ["Eastern Europe"],
      "scope": "Country",
      "languages": ["EN", "UA"],
      "purpose": "Both",
      "professions_supported": "All Professions",
      "departments": ["Managers", "Developers", "Designers", "Marketers", "Videographers", "Other"],
      "specialization": "Generalist",
      "pricing": {
        "access_level": "Freemium",
        "job_posting_cost": "Free basic, paid promotion",
        "cv_database_cost": "Paid subscription"
      },
      "features": {
        "bulk_posting": true,
        "cv_database": true,
        "ai_matching": false,
        "ats_integration": false,
        "employer_branding": true,
        "mobile_app": true
      },
      "activity": {
        "penetration_score": "Dominant",
        "activity_level": "High"
      },
      "task_templates": ["TASK-HR-001", "TASK-HR-005"],
      "notes": "Leading job board in Ukraine"
    },
    {
      "id": "PLATFORM-025",
      "name": "IT Jobs Poland",
      "platform_type": "Telegram",
      "username": "@itjobspoland",
      "url": "https://t.me/itjobspoland",
      "type": "Broadcast Channel",
      "member_count": 15000,
      "countries": ["Poland"],
      "regions": ["Eastern Europe"],
      "scope": "Country",
      "languages": ["PL", "EN"],
      "purpose": "Job Postings Only",
      "professions_supported": [
        "front end developer",
        "back end developer",
        "full stack developer"
      ],
      "departments": ["Developers"],
      "specialization": "Tech-focused",
      "pricing": {
        "access_level": "Free",
        "platform_fee": "None"
      },
      "features": {
        "real_time_alerts": true,
        "direct_messaging": true
      },
      "activity": {
        "posts_per_day": 10,
        "engagement_level": "High",
        "last_post": "2025-11-14"
      },
      "posting_rules": {
        "employers_can_post": true,
        "format": "Free-form"
      },
      "quality": {
        "moderation": "High",
        "spam_level": "Low"
      },
      "task_templates": ["TASK-HR-002"],
      "notes": "Very active channel, high-quality job postings"
    }
  ]
}
```

**3. Profession-to-Platform Mapping Report**
```markdown
# Profession-to-Platform Mapping

## Frontend Developer

### Best Platforms for Hiring Frontend Developers

#### Tier 1: Essential Platforms
1. **Djinni** (Ukraine, EU)
   - Specialization: Tech-focused
   - Database: 5,000+ FE developers
   - Cost: Free for employers

2. **LinkedIn** (Global)
   - Specialization: Generalist
   - Reach: Global, professional network
   - Cost: Freemium

3. **IT Jobs Poland Telegram** (Poland)
   - Specialization: Tech-focused
   - Engagement: 10 posts/day, 15K members
   - Cost: Free

#### Tier 2: Supplementary Platforms
[Continue...]

[Repeat for all 22 professions...]
```

**4. Department Sourcing Strategies**
```markdown
# Department-Specific Sourcing Strategies

## Developers Department

### Platform Mix Recommendation
- **Primary (70%)**: Tech-focused job sites (Djinni, DOU.ua, Stack Overflow)
- **Secondary (20%)**: General job boards (LinkedIn, Indeed)
- **Tertiary (10%)**: Community platforms (Telegram dev channels, GitHub)

### Workflow
1. Post to tech job boards (Day 1)
2. Share in Telegram channels (Day 1-2)
3. Proactive CV database search on LinkedIn (Day 3-7)
4. Engage in developer communities (Ongoing)

[Repeat for all departments...]
```

---

### Total Research Time per Session

- **Phase 1** (Traditional Job Sites): 30 min
- **Phase 2** (Bulletin Boards): 20 min
- **Phase 3** (Telegram): 45 min
- **Phase 4** (Facebook): 45 min
- **Phase 5** (Validation): 30 min
- **Phase 6** (Documentation): 30 min

**Total Time**: 3 hours

**Recommended Frequency**: Monthly (for ongoing discovery)

---

## ✅ Quality Criteria & Validation Checklist

Use this checklist to validate each platform before adding to the library:

### General Criteria (All Platform Types)

- [ ] **Active Platform**: Posts or activity within last 30 days
- [ ] **Accessible**: Registration or join process is functional
- [ ] **Geographic Relevance**: Covers target hiring regions
- [ ] **Language Support**: Supports relevant languages for your hiring needs
- [ ] **Clear Purpose**: Job postings, CV database, or both is clearly defined
- [ ] **Professional Quality**: Platform appears credible and trustworthy

### Traditional Job Sites

- [ ] **Functional Posting Interface**: Job posting form is accessible and functional
- [ ] **Pricing Transparency**: Costs are clearly stated or discoverable
- [ ] **Recent Job Postings**: 10+ jobs posted in last 7 days (or reasonable activity for niche sites)
- [ ] **Application Process**: Clear path for candidates to apply
- [ ] **Company Profiles**: Employer branding or company pages available (if applicable)
- [ ] **Search Filters**: Candidate search has useful filters (profession, location, experience)

### Bulletin Boards

- [ ] **Job Section Exists**: Dedicated job or employment category
- [ ] **Posting Allowed**: Job postings are permitted (not restricted to services only)
- [ ] **Free or Low-Cost**: Accessible for small businesses or individuals
- [ ] **Local Activity**: Relevant for local/regional hiring
- [ ] **Contact Options**: Direct contact info (email/phone) visible

### Telegram Channels/Groups

- [ ] **Member Count**: 500+ members (minimum threshold for viability)
- [ ] **Recent Activity**: At least 1 post in last 7 days
- [ ] **Language Relevance**: Uses language(s) relevant to your hiring regions
- [ ] **Content Quality**: Majority of posts are job-related (not spam or off-topic)
- [ ] **Moderation Evidence**: AI activity visible (spam removed, rules enforced)
- [ ] **Posting Clarity**: Clear how employers can post (if allowed)
- [ ] **Engagement**: Posts receive reactions or replies (shows active audience)

### Facebook Groups

- [ ] **Member Count**: 1,000+ members (minimum threshold for viability)
- [ ] **Recent Activity**: 3-5+ posts per day
- [ ] **Job Postings Allowed**: Group rules explicitly allow job postings
- [ ] **Join Process**: Public or reasonable approval process (<3 days)
- [ ] **Moderation Quality**: Evidence of admin oversight and spam management
- [ ] **Content Quality**: Mix of job postings and professional discussion
- [ ] **Community Engagement**: Posts receive comments and reactions

### Classification Completeness

- [ ] **Platform Type** classified
- [ ] **Purpose** classified (Job Postings / CV Database / Both)
- [ ] **Professions Supported** tagged
- [ ] **Departments** mapped
- [ ] **Geography** documented (countries, regions, scope)
- [ ] **Languages** listed
- [ ] **Pricing & Access** documented
- [ ] **Features** assessed (relevant features checked)
- [ ] **Target Audience** identified
- [ ] **Job Types Supported** listed

### Integration Readiness

- [ ] **Professions Mapped**: Tagged with relevant professions from LIBRARIES/Professions
- [ ] **Task Templates Linked**: Related TASK_MANAGERS Task Templates identified
- [ ] **Use Case Defined**: Clear description of "Best For" use cases
- [ ] **Department Recommendation**: Identified which departments benefit most

### Documentation Completeness

- [ ] **Template Used**: Appropriate profile template filled out completely
- [ ] **Notes Added**: Observations, tips, and considerations documented
- [ ] **Comparison Ready**: Platform can be compared with others in its category
- [ ] **Searchable**: Enough detail for future reference and search

---

## 🚫 Exclusion Criteria

**Do NOT document platforms that meet any of these criteria**:

❌ **Inactive Platform**
- No posts or activity in last 60 days
- Platform domain expired or unreachable
- Official announcement of shutdown

❌ **Scam or Fraudulent**
- Reports of scams or fraudulent activity
- Requests payment upfront with no service delivery
- Fake job postings prevalent

❌ **Severe Quality Issues**
- 80%+ spam content
- No moderation (Telegram/Facebook)
- Extremely low engagement despite high member count

❌ **Access Restricted or Prohibited**
- Platform prohibits job postings after registration
- Requires impossible verification (e.g., local business license for international companies)
- Banned in target hiring regions

❌ **Irrelevant**
- No overlap with target geographies or professions
- Language barriers with no English option for global roles

---

## 📚 Research Resources & Tools

### Telegram Discovery Resources
- **TGStat.com** - Telegram channel analytics and directory
- **Telemetr.io** - Telegram statistics and channel search
- **TelegramChannels.me** - Telegram channel directory
- **Combot.org** - Telegram group analytics

### Facebook Group Discovery
- **Facebook's internal search** - Primary discovery method
- **Google search**: `site:facebook.com/groups "[keyword]"`
- **Social media group directories** - Some blogs and sites list Facebook groups by topic

### Job Board Directories
- **Adzuna** - Aggregates job boards by country
- **Indeed Company Pages** - Check where competitors post jobs
- **Google**: "best job boards [country] 2025"
- **Reddit**: r/forhire, r/recruiting - Community recommendations

### Country-Specific Resources
- **Eastern Europe**: DOU.ua forums, Habr Career, local tech communities
- **Western Europe**: Europa.eu EURES, country-specific employment agencies
- **Global**: LinkedIn groups, international recruiter communities

### Validation Tools
- **SimilarWeb** - Estimate website traffic
- **Alexa** (if still available) - Website ranking
- **Google Trends** - Platform popularity over time
- **TGStat / Social Blade** - Telegram/social media analytics

---

## 🔄 Maintenance & Updates

### Quarterly Platform Review

**Frequency**: Every 3 months

**Tasks**:
1. **Verify Activity**: Check if all documented platforms are still active
   - Remove platforms with no activity in 60+ days
   - Update member counts for Telegram/Facebook

2. **Update Information**: Refresh platform details
   - Pricing changes
   - Feature updates
   - Member count changes
   - New platform policies

3. **Discover New Platforms**: Allocate 1-2 hours to discover new platforms launched in the quarter
   - New job boards
   - New Telegram channels
   - New Facebook groups

4. **Quality Audit**: Sample 10-20 platforms and validate quality criteria still met

5. **User Feedback Integration**: Incorporate feedback from team members using the platforms
   - Which platforms delivered best candidates?
   - Which platforms had poor ROI?
   - Which platforms should be prioritized or deprioritized?

---

### Continuous Monitoring

**Daily (5-10 minutes)**:
- Scan 2-3 active Telegram channels for job posting trends
- Check 1-2 Facebook groups for new activity

**Weekly (30 minutes)**:
- Review application rates from different platforms
- Identify which platforms delivered qualified candidates
- Adjust posting strategy based on performance

**Monthly (1 hour)**:
- Update platform activity scores
- Add newly discovered platforms
- Remove inactive platforms

---

### Platform Performance Tracking

**Metrics to Track**:
1. **Applications per Platform**: How many applications from each platform?
2. **Quality Score**: % of qualified candidates from each platform
3. **Time-to-Hire**: How fast candidates move through pipeline from each platform
4. **Cost-per-Hire**: If platform charges, calculate ROI
5. **Candidate Source**: Track which platforms hired candidates came from

**Create a Tracking Sheet**:
```markdown
| Platform | Jobs Posted | Applications Received | Qualified Candidates | Interviews | Hires | Cost | Notes |
|----------|-------------|----------------------|---------------------|-----------|-------|------|-------|
| LinkedIn | 5 | 50 | 10 (20%) | 5 | 1 | €200 | Good quality |
| Work.ua | 5 | 80 | 15 (19%) | 6 | 2 | €100 | High volume |
| IT Jobs PL Telegram | 5 | 30 | 12 (40%) | 5 | 1 | €0 | Best quality/cost |
```

Use this data to refine platform prioritization and recommendations.

---

## 🎓 Best Practices

### DO:
✅ **Start with existing library** - Build on the 23 platforms already documented
✅ **Focus on activity** - Prioritize platforms with recent, frequent postings
✅ **Test before documenting** - Join/register to verify platform functionality
✅ **Document thoroughly** - Complete all template sections for future reference
✅ **Map to taxonomy** - Always connect to Professions and TASK_MANAGERS
✅ **Track performance** - Monitor which platforms deliver best candidates
✅ **Respect community rules** - Follow Telegram/Facebook group guidelines
✅ **Engage authentically** - Build relationships in community platforms (Telegram/Facebook)
✅ **Update regularly** - Platforms change; keep documentation current

### DON'T:
❌ **Don't spam communities** - Respect posting limits in Telegram/Facebook groups
❌ **Don't ignore quality** - High member count ≠ high quality
❌ **Don't skip validation** - Always verify platform is active and functional
❌ **Don't overlook niche platforms** - Specialized platforms often have better candidate quality
❌ **Don't rely on one platform type** - Use a mix of job sites, Telegram, Facebook for best reach
❌ **Don't neglect Telegram/Facebook** - Community platforms can outperform traditional job sites
❌ **Don't forget professions** - Always tag platforms with relevant professions
❌ **Don't ignore language barriers** - Ensure platform supports languages your candidates speak

---

## 📊 Success Metrics

Track the effectiveness of this research:

### Quantitative Metrics
- **Total platforms documented**: [Target: 100+ within 3 months]
- **Platform types covered**: [Target: All 4 types]
- **Countries covered**: [Target: 25+ countries]
- **Professions mapped**: [Target: All 22 professions]
- **Applications generated**: [Track per platform]
- **Cost savings**: [By using free platforms like Telegram/Facebook]

### Qualitative Metrics
- **Candidate quality improvement**: Higher % of qualified candidates
- **Time-to-fill reduction**: Faster hiring through multi-platform approach
- **Recruiter satisfaction**: Ease of finding platforms for specific roles
- **Department feedback**: Do departments find platforms useful?

### Monthly Review Questions
1. Which platforms delivered the most qualified candidates this month?
2. Which platform types (job sites, Telegram, Facebook) performed best?
3. Are there professions we're still struggling to source? What platforms are missing?
4. Which countries/regions need more platform coverage?
5. How can we improve platform documentation or classification?

---

## 🔧 Troubleshooting

### Common Issues

**Issue**: Telegram channel has high member count but no recent activity
- **Solution**: Mark as "Inactive" and deprioritize. Look for alternative active channels.

**Issue**: Facebook group requires approval and admin hasn't responded in 7+ days
- **Solution**: Try contacting admin directly via Facebook message. If no response in 14 days, move to "Low Priority" and continue with other groups.

**Issue**: Job site has paywall and unclear pricing
- **Solution**: Contact sales team for pricing quote. Document as "Pricing: Contact Sales" and note difficulty of obtaining pricing info.

**Issue**: Platform claims to cover a country but all jobs are in a different language
- **Solution**: Re-classify language support accurately. Note in "Notes" section that despite country tag, jobs are primarily in [Language].

**Issue**: Bulletin board has job section but 80% spam
- **Solution**: Tag with "Quality: Low, High spam". Use only as last resort for hard-to-fill roles.

**Issue**: Telegram channel admin prohibits employer job postings
- **Solution**: Re-classify as "Candidate-focused" and note "Posting not allowed, monitoring only" in purpose field.

---

## 📞 Questions or Feedback?

If you have suggestions for improving this research process, discovered new platform types, or need specific profession/country coverage, update this prompt or communicate with the HR and Taxonomy teams.

**Prompt Owner**: HR Operations Team
**Research Team**: Recruiters, HR Managers
**Taxonomy Integration**: Taxonomy Team

---

## 📖 Version History

**v1.0.0** (2025-11-14):
- Initial creation - Comprehensive job sites deep research prompt
- Added 4 platform types: Job Sites, Bulletin Boards, Telegram, Facebook
- 10-dimensional classification system
- 7 advanced sorting methods
- Integration with LIBRARIES/Professions and TASK_MANAGERS
- 6-phase research workflow
- 4 documentation templates
- Quality criteria and validation checklists
- Best practices and troubleshooting guide

---

**Last Research Date**: [To be filled]
**Total Platforms Documented**: [To be filled]
**Most Recent Additions**: [To be filled]
**Top 5 Recommended Platforms**: [To be filled]

---

## 📂 Related Files

**Job Sites Libraries**:
- `C:\Users\anast\Dropbox\HR Nov25\LIBRARIES\job sites.md` - Current 23-site library (markdown)
- `C:\Users\anast\Dropbox\AI Nov25\Perederii Vladislav\job_sites.json` - Current library (JSON format)

**Taxonomy Integration**:
- `C:\Users\anast\Dropbox\Entities\LIBRARIES\Professions\` - Professions entity for profession mapping
- `C:\Users\anast\Dropbox\Entities\TASK_MANAGERS\` - Task Templates and workflows

**Related HR Prompts**:
- `CV_Parser_v1.md` - CV parsing and candidate data extraction
- `Communication_Templates_Prompt.md` - Candidate communication templates
- `CRM_Data_Entry_Prompt.md` - Candidate and platform data entry

---

**End of Prompt**
