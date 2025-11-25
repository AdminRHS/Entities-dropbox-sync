# Week 3 Day 21 - Project Plans

**Date:** 2025-01-21  
**Department:** AID (AI & Automation)  
**Source:** daily.md processing via MAIN_PROMPT_v6.md

---

## 1. Google Scraping Project (AID)

### Overview
Improve Google Maps scraping system with better filtering, search query optimization, and integration with existing CRM automation.

### Milestones

#### MLT-001: Research & Optimization Phase
- **Status:** In Progress
- **Focus:** Improve scraping quality and targeting
- **Key Areas:**
  - Filter last batch (June Entry Position targeting)
  - Research search query optimization
  - Develop Google Maps request formula/prompt architecture
  - Integrate with CRM automation

#### MLT-002: Search Query Development
- **Status:** Planning
- **Focus:** Create comprehensive search query system
- **Key Areas:**
  - Find existing LinkedIn search queries (Lead Generator file)
  - Convert LinkedIn queries to Google Maps format
  - Research Google Maps categories (place/club/spa/agency patterns)
  - Develop city-based formula for country-wide searches
  - Create prompt for Column H (search query generation)

#### MLT-003: YouTube Research Integration
- **Status:** Planning
- **Focus:** Build knowledge base through video tutorials
- **Key Areas:**
  - Research YouTube tutorials on Google Maps scraping
  - Parse 3-4 videos about Google Maps scraping
  - Establish daily video parsing routine (1 video/day minimum)
  - Import research methodology

#### MLT-004: Job Sites Entity Creation
- **Status:** Planning
- **Focus:** Structure job sites as separate entity
- **Key Areas:**
  - Create ENTITIES/Accounts/Job Sites folder
  - Follow taxonomy of other entities
  - Organize job site IDs and configurations
  - Integrate with existing automation

---

## 2. Reviews Scraping System

### Overview
Complete reviews collection and analysis system with semantic analysis, problem identification, and automated outreach recommendations.

### Milestones

#### MLT-005: System Completion & Documentation
- **Status:** In Progress
- **Focus:** Finalize system and document all stages
- **Key Areas:**
  - Document each stage of the process
  - Create research plan for each stage
  - Research best practices (3-5 AI tools parallel)
  - Build instruction set for Google Sheets/N8N setup
  - Add social media scraping capability
  - Mark data source (Google Maps vs other)

#### MLT-006: Review Collection Logic
- **Status:** Completed
- **Focus:** Collect reviews with filtering
- **Key Areas:**
  - Max 50 reviews per company
  - Filter: 4 stars and below, prioritize newest
  - Collect company name, review text, date
  - Extract website links

#### MLT-007: Semantic Analysis & Problem Identification
- **Status:** Completed
- **Focus:** Analyze reviews for problem patterns
- **Key Areas:**
  - Link problems to professions
  - Generate problem scores
  - Filter companies by problem score thresholds
  - Connect problems to specific job positions

#### MLT-008: Automated Outreach Generation
- **Status:** Completed
- **Focus:** Generate recommendation letters
- **Key Areas:**
  - Create outreach templates based on reviews
  - Generate personalized recommendations
  - Focus on companies with identified problems

---

## 3. Content Entity Creation

### Overview
Create structured entity system for storing and organizing tutorials, guides, and educational content.

### Milestones

#### MLT-009: Entity Structure Setup
- **Status:** Planning
- **Focus:** Establish content storage taxonomy
- **Key Areas:**
  - Create Content Entity structure
  - Define tutorial categories
  - Set up guide organization system
  - Integrate with existing ENTITIES structure

---

## 4. Employees Dashboard Project

### Overview
Complete HR dashboard for tracking employee attendance, Discord activity, CRM check-ins, and project status.

### Milestones

#### MLT-010: Dashboard Development
- **Status:** In Progress
- **Focus:** Build Next.js/Tailwind dashboard
- **Key Areas:**
  - Connect to Google Sheets data source
  - Display employee attendance data
  - Show Discord time tracking
  - Display CRM check-in status
  - Separate project vs non-project employees
  - Show hours, reports, time off

#### MLT-011: UI/UX Integration
- **Status:** In Progress
- **Focus:** Integrate UI kit and styling
- **Key Areas:**
  - Integrate UI kit (developed with Eleonora)
  - Apply consistent styling
  - Add avatar components
  - Improve visual design

#### MLT-012: Deployment & Access
- **Status:** Planning
- **Focus:** Deploy dashboard and set up access
- **Key Areas:**
  - Deploy to Vercel (Node.js backend)
  - Set up access control
  - Add Discord ID column to Google Sheets
  - Create deployment documentation
  - Test local setup for team members (Wilhelm example)

#### MLT-013: Feature Enhancements
- **Status:** Planning
- **Focus:** Add advanced features
- **Key Areas:**
  - Add calendar view
  - Include missing employees
  - Add leaderboard (top 5 best/worst)
  - Email integration
  - Status indicators and alerts

---

## 5. Work Environment & AI Tools Allocation

### Overview
Improve employee work environment by allocating local AI tools and modernizing development setup.

### Milestones

#### MLT-014: VS Code & AI Tools Setup
- **Status:** In Progress
- **Focus:** Modernize development environment
- **Key Areas:**
  - Set up VS Code for all employees
  - Install AI extensions (Claude Code, Cursor)
  - Configure accounts and access
  - Create onboarding documentation
  - Set up basic training program

#### MLT-015: Account Management System
- **Status:** Planning
- **Focus:** Manage AI tool accounts and limits
- **Key Areas:**
  - Track account limits (Google Sheets)
  - Allocate accounts to employees
  - Monitor usage
  - Set up separate accounts for onboarding
  - Create account rotation system

#### MLT-016: Training & Adoption
- **Status:** Planning
- **Focus:** Ensure team adoption of new tools
- **Key Areas:**
  - Create basic training materials
  - Document workflows
  - Set up support system
  - Track adoption rates
  - Create innovation badges/rewards system

---

## 6. YouTube Research & Content Processing

### Overview
Establish systematic approach to finding, processing, and integrating YouTube tutorials into knowledge base.

### Milestones

#### MLT-017: YouTube Channel Research
- **Status:** Planning
- **Focus:** Find relevant YouTube channels
- **Key Areas:**
  - Research Design department tutorials (last 1-2 months)
  - Find AI tools channels
  - Identify valuable tutorial sources
  - Create channel database

#### MLT-018: Video Processing Workflow
- **Status:** Planning
- **Focus:** Process and integrate video content
- **Key Areas:**
  - Parse videos from identified channels
  - Extract key information
  - Categorize content (redesign, design, etc.)
  - Store in Content Entity
  - Create searchable prompt library

---

## 7. Entity System Integration

### Overview
Integrate all projects with ENTITIES taxonomy system and improve cross-system connectivity.

### Milestones

#### MLT-019: Prompt Integration
- **Status:** Planning
- **Focus:** Integrate prompts into Antitrust/Composer ecosystem
- **Key Areas:**
  - Copy prompts to Composer
  - Create relative path references
  - Build prompt reuse system
  - Document prompt library

#### MLT-020: Report Generation System
- **Status:** In Progress
- **Focus:** Automate report creation and storage
- **Key Areas:**
  - Set up report storage in ENTITIES/Reports
  - Create report templates
  - Automate report generation
  - Organize reports by date/department

---

## Cross-Project Priorities

### Immediate Actions
1. Complete Google Scraping documentation and research
2. Finalize Reviews Scraping system documentation
3. Deploy Employees Dashboard to Vercel
4. Set up VS Code for team members

### Strategic Goals
- Build cumulative knowledge system (no starting from scratch)
- Integrate all systems with CRM automation
- Create reusable prompt library
- Establish daily research routines

---

**Next Steps:** See tasks.md for specific actionable items.

