# Architecture Decision: Dropbox API vs Database Storage

**Document ID:** DOC-RES-018
**Version:** 1.0
**Date:** 2025-12-09
**Status:** Decision Analysis
**Purpose:** Compare two architectural approaches and provide clear recommendation

---

## Executive Summary

There are **two versions** of the complete application generation prompt:

| Version | File | Storage Approach | Lines | Status |
|---------|------|------------------|-------|--------|
| **v2.0** | `COMPLETE-APP-GENERATION-PROMPT.md` | PostgreSQL + Prisma | 2,842 | ⚠️ Traditional DB |
| **v3.1** | `COMPLETE-APP-GENERATION-PROMPT_1.md` | Dropbox API (No DB) | 3,073 | ✅ **RECOMMENDED** |

**Recommendation:** **Use Version 3.1 (Dropbox API)** - Aligns with current system architecture

---

## Table of Contents

1. [Current System Analysis](#1-current-system-analysis)
2. [Version Comparison](#2-version-comparison)
3. [Architecture Differences](#3-architecture-differences)
4. [Pros and Cons Analysis](#4-pros-and-cons-analysis)
5. [Performance Comparison](#5-performance-comparison)
6. [Implementation Complexity](#6-implementation-complexity)
7. [Cost Analysis](#7-cost-analysis)
8. [Migration Path](#8-migration-path)
9. [Final Recommendation](#9-final-recommendation)
10. [Action Items](#10-action-items)

---

## 1. Current System Analysis

### 1.1 How the System Currently Works

The RESEARCHES system **already operates successfully** using file-based storage:

```
Current Data Storage:
├── CSV Files (Tabular data)
│   ├── Search_Queue_Master.csv
│   ├── Video_Queue_Master.csv
│   └── VIDEO_PROGRESS_TRACKER.csv
├── JSON Files (Structured entities)
│   ├── LIBRARIES/TOOLS/TOL-*.json
│   ├── LIBRARIES/WORKFLOWS/WRF-*.json
│   └── LIBRARIES/OBJECTS/OBJ-*.json
└── Markdown Files (Documentation)
    ├── 02_TRANSCRIPTIONS/Video_*.md
    └── 03_ANALYSIS/*/Video_*_*.md
```

**Key Facts:**
- ✅ 28 videos successfully processed
- ✅ 500+ entities created and managed
- ✅ Zero database infrastructure
- ✅ All files stored in Dropbox
- ✅ Human-readable and version-controllable
- ✅ No performance issues at current scale

### 1.2 Current Scale Metrics

| Metric | Current | Projected (1 Year) | Scalability Status |
|--------|---------|-------------------|-------------------|
| Videos Processed | 28 | 100-200 | ✅ File-based adequate |
| Entities Created | 500+ | 2,000-4,000 | ✅ File-based adequate |
| Queue Entries | 5 active | 50-100 active | ✅ File-based adequate |
| Search Tasks | ~20 | 200-400 | ✅ File-based adequate |
| Total Files | ~170 | 1,000-2,000 | ✅ File-based adequate |
| Query Performance | < 1s | < 1s (with indexes) | ✅ No DB needed |

**Conclusion:** File-based storage is working and will continue to work for foreseeable future.

---

## 2. Version Comparison

### 2.1 Technology Stack Comparison

#### Version 2.0 (PostgreSQL + Prisma)

```json
{
  "backend": {
    "runtime": "Node.js 20+",
    "framework": "Express.js 4.18+",
    "database": "PostgreSQL 15+ (Supabase/Neon)",
    "orm": "Prisma ORM",
    "validation": "Zod",
    "cors": "CORS middleware",
    "auth": "JWT (jsonwebtoken)",
    "apiDocs": "Swagger/OpenAPI"
  }
}
```

**Pros:**
- ✅ SQL queries (powerful)
- ✅ ACID transactions
- ✅ Built-in relationships
- ✅ Optimized for scale

**Cons:**
- ❌ Requires database hosting (Supabase/Neon)
- ❌ Monthly cost ($10-50/month)
- ❌ More complex setup
- ❌ Doesn't align with current system
- ❌ Migration required from CSV/JSON
- ❌ Additional dependency (PostgreSQL)

#### Version 3.1 (Dropbox API)

```json
{
  "backend": {
    "runtime": "Node.js 20+",
    "framework": "Express.js 4.18+",
    "dataStorage": "Dropbox API (no database)",
    "validation": "Zod",
    "cors": "CORS middleware",
    "auth": "JWT (jsonwebtoken)",
    "apiDocs": "Swagger/OpenAPI"
  }
}
```

**Pros:**
- ✅ No database infrastructure needed
- ✅ Zero monthly cost (Dropbox already exists)
- ✅ Aligns with current system
- ✅ Human-readable files (CSV/JSON)
- ✅ Version control friendly
- ✅ Easy backup (copy files)
- ✅ Simple deployment
- ✅ Direct access to existing data

**Cons:**
- ⚠️ No SQL queries (use file operations)
- ⚠️ Manual index management
- ⚠️ Concurrent access requires care

---

## 3. Architecture Differences

### 3.1 Data Flow Comparison

#### Version 2.0 (Database)

```
┌────────────────────────────────────────────┐
│         React Frontend (Port 3000)         │
│  ┌──────────────────────────────────────┐  │
│  │   Search Queue UI   Video Queue UI   │  │
│  └───────────────┬──────────────────────┘  │
└────────────────────┼──────────────────────┘
                     │ REST API
┌────────────────────▼──────────────────────┐
│       Express.js Backend (Port 5000)       │
│  ┌──────────────────────────────────────┐  │
│  │  Controllers → Services → Prisma     │  │
│  └───────────────┬──────────────────────┘  │
└────────────────────┼──────────────────────┘
                     │ SQL Queries
┌────────────────────▼──────────────────────┐
│         PostgreSQL Database                │
│  ┌──────────────────────────────────────┐  │
│  │  search_queue, video_queue,          │  │
│  │  videos, entities tables             │  │
│  └──────────────────────────────────────┘  │
└────────────────────────────────────────────┘
```

#### Version 3.1 (Dropbox API)

```
┌────────────────────────────────────────────┐
│         React Frontend (Port 3000)         │
│  ┌──────────────────────────────────────┐  │
│  │   Search Queue UI   Video Queue UI   │  │
│  └───────────────┬──────────────────────┘  │
└────────────────────┼──────────────────────┘
                     │ REST API
┌────────────────────▼──────────────────────┐
│       Express.js Backend (Port 5000)       │
│  ┌──────────────────────────────────────┐  │
│  │  Controllers → Dropbox Service       │  │
│  └───────────────┬──────────────────────┘  │
└────────────────────┼──────────────────────┘
                     │ Dropbox API
┌────────────────────▼──────────────────────┐
│              Dropbox Storage               │
│  ┌──────────────────────────────────────┐  │
│  │  Search_Queue_Master.csv             │  │
│  │  Video_Queue_Master.csv              │  │
│  │  LIBRARIES/*/TOL-*.json              │  │
│  └──────────────────────────────────────┘  │
└────────────────────────────────────────────┘
```

### 3.2 File Structure Comparison

#### Version 2.0 (Database)

```bash
research-management/
├── frontend/
│   ├── src/
│   ├── package.json
│   └── vite.config.ts
└── backend/
    ├── src/
    ├── prisma/
    │   ├── schema.prisma    # Database schema
    │   └── migrations/      # DB migrations
    ├── package.json
    └── .env                 # DATABASE_URL required
```

**Required Dependencies:**
- `@prisma/client`
- `prisma` (dev)
- PostgreSQL hosting (Supabase/Neon)

#### Version 3.1 (Dropbox)

```bash
research-management/
├── frontend/
│   ├── src/
│   ├── package.json
│   └── vite.config.ts
└── backend/
    ├── src/
    │   ├── services/
    │   │   └── dropboxService.ts    # Dropbox API wrapper
    │   └── utils/
    │       ├── csvUtils.ts          # CSV operations
    │       └── jsonUtils.ts         # JSON operations
    ├── package.json
    └── .env                         # DROPBOX_ACCESS_TOKEN required
```

**Required Dependencies:**
- `dropbox` (Dropbox SDK)
- `csv-parser` and `csv-writer`

---

## 4. Pros and Cons Analysis

### 4.1 Database Approach (Version 2.0)

#### Advantages ✅

1. **Powerful Queries**
   - SQL provides complex filtering, joins, aggregations
   - Example: `SELECT * FROM videos WHERE priority > 70 AND status = 'Pending' ORDER BY priority DESC`

2. **Data Integrity**
   - ACID transactions guarantee consistency
   - Foreign key constraints enforce relationships
   - No risk of orphaned records

3. **Performance at Scale**
   - Optimized for millions of records
   - Built-in indexing
   - Query optimization

4. **Mature Ecosystem**
   - Well-tested solutions
   - Prisma provides excellent TypeScript integration
   - Many hosting options

#### Disadvantages ❌

1. **Infrastructure Complexity**
   - Requires database hosting (Supabase/Neon/Railway)
   - Connection pooling setup
   - Migration management
   - Backup/restore procedures

2. **Cost**
   - Monthly hosting: $10-50/month
   - Scales with usage
   - Free tiers have limitations

3. **Development Complexity**
   - Prisma schema maintenance
   - Migration creation/management
   - Local dev database setup
   - Testing requires test database

4. **Deployment Complexity**
   - Database must be deployed first
   - Connection string management
   - Environment-specific configs
   - SSL certificate setup

5. **Doesn't Match Current System**
   - Requires full migration from CSV/JSON
   - Loses human-readable files
   - Loses version control benefits
   - Breaks existing scripts/workflows

### 4.2 Dropbox API Approach (Version 3.1)

#### Advantages ✅

1. **Zero Infrastructure**
   - No database hosting needed
   - No connection strings
   - No migrations
   - Uses existing Dropbox account

2. **Zero Cost**
   - Dropbox already exists
   - No additional monthly fees
   - Free tier sufficient for years

3. **Matches Current System**
   - Directly accesses existing CSV/JSON files
   - No migration needed
   - Scripts continue to work
   - Seamless integration

4. **Human-Readable Files**
   - CSV files open in Excel/Google Sheets
   - JSON files easy to inspect/edit
   - Markdown files for documentation
   - Version control friendly

5. **Simple Deployment**
   - Deploy backend to Vercel/Railway
   - Set `DROPBOX_ACCESS_TOKEN` env var
   - No database setup
   - Deploy frontend to Vercel/Netlify

6. **Easy Backup**
   - Dropbox handles backups automatically
   - Copy folder for instant backup
   - No export/dump needed
   - Sync across devices

7. **Collaborative**
   - Team members can access files
   - Manual edits possible when needed
   - Shared folder access
   - Real-time sync

#### Disadvantages ⚠️

1. **Query Limitations**
   - No SQL (must implement filters in code)
   - Complex queries require custom logic
   - No built-in aggregations
   - Full file read for queries

2. **Performance at Scale**
   - Adequate for 1,000-10,000 records
   - Requires indexing for larger scale
   - File-based operations slower than DB
   - Network latency for API calls

3. **Concurrent Access**
   - No built-in locking
   - Must implement conflict resolution
   - Race conditions possible
   - Requires careful state management

4. **Index Management**
   - Must manually maintain indexes
   - Index can become stale
   - No automatic optimization
   - Requires rebuild logic

---

## 5. Performance Comparison

### 5.1 Read Operations

| Operation | PostgreSQL | Dropbox API (No Index) | Dropbox API (With Index) |
|-----------|------------|------------------------|--------------------------|
| Get single record | 1-5ms | 50-200ms (read file + parse) | 50-200ms (cached) |
| Filter 100 records | 5-20ms | 50-200ms (read + filter) | 50-200ms (cached) |
| Join 2 tables | 10-50ms | 100-400ms (2 files) | 100-400ms |
| Aggregate 1000 records | 20-100ms | 200-500ms | 200-500ms |

**Verdict:** Database is faster, but Dropbox is adequate for < 10,000 records

### 5.2 Write Operations

| Operation | PostgreSQL | Dropbox API |
|-----------|------------|-------------|
| Insert 1 record | 5-20ms | 100-300ms (read + append + write) |
| Update 1 record | 5-20ms | 100-300ms (read + modify + write) |
| Delete 1 record | 5-20ms | 100-300ms (read + filter + write) |
| Batch insert 100 | 50-200ms | 500-1000ms |

**Verdict:** Database is 10-20x faster for writes, but Dropbox is acceptable

### 5.3 Real-World Performance

**Current System (28 videos, 500+ entities):**
- ✅ All operations < 1 second
- ✅ No performance complaints
- ✅ Adequate for daily use

**Projected (200 videos, 2,000+ entities):**
- ✅ Dropbox with indexes: < 1 second
- ✅ Still adequate

**Threshold for Database:**
- ⚠️ Consider database if > 10,000 videos
- ⚠️ Consider database if > 100,000 entities
- ⚠️ Consider database if > 1,000 concurrent users

**Conclusion:** Current scale doesn't require database

---

## 6. Implementation Complexity

### 6.1 Setup Complexity

#### Version 2.0 (Database)

**Backend Setup Steps:**
1. Create Supabase/Neon account
2. Create PostgreSQL database
3. Get connection string
4. Install Prisma dependencies
5. Create Prisma schema
6. Run initial migration
7. Generate Prisma client
8. Configure environment variables
9. Implement controllers/services
10. Test database connection

**Estimated Setup Time:** 4-6 hours

**Frontend Setup Steps:**
1. Install dependencies
2. Configure API base URL
3. Implement Zustand stores
4. Create API service layer
5. Test API integration

**Estimated Setup Time:** 2-3 hours

**Total:** 6-9 hours

#### Version 3.1 (Dropbox)

**Backend Setup Steps:**
1. Get Dropbox access token (from existing account)
2. Install Dropbox SDK
3. Create `dropboxService.ts`
4. Implement CSV/JSON utils
5. Configure environment variables
6. Test Dropbox connection

**Estimated Setup Time:** 2-3 hours

**Frontend Setup Steps:**
1. Install dependencies
2. Configure API base URL
3. Implement Zustand stores
4. Create API service layer
5. Test API integration

**Estimated Setup Time:** 2-3 hours

**Total:** 4-6 hours

**Conclusion:** Dropbox approach is 2-3 hours faster to set up

### 6.2 Development Complexity

#### Version 2.0 (Database)

**Complexity Score:** 7/10

**Challenges:**
- Prisma schema design and maintenance
- Migration management (dev → staging → prod)
- Database seeding for development
- Testing requires test database
- Connection pool management
- Transaction handling

**Example Code Complexity:**

```typescript
// Create video (Database)
async createVideo(data: CreateVideoInput) {
  return await prisma.$transaction(async (tx) => {
    const video = await tx.video.create({ data });
    await tx.videoQueue.create({
      data: {
        videoId: video.id,
        priority: calculatePriority(video),
        status: 'Pending'
      }
    });
    return video;
  });
}
```

#### Version 3.1 (Dropbox)

**Complexity Score:** 5/10

**Challenges:**
- CSV/JSON parsing and writing
- Index management
- Concurrent access handling
- File path management
- Error handling for API calls

**Example Code Complexity:**

```typescript
// Create video (Dropbox)
async createVideo(data: CreateVideoInput) {
  const queue = await readCSV('Video_Queue_Master.csv');
  const newVideo = {
    Queue_ID: generateId(queue),
    ...data,
    Priority: calculatePriority(data),
    Status: 'Pending'
  };
  queue.push(newVideo);
  await writeCSV('Video_Queue_Master.csv', queue);
  return newVideo;
}
```

**Conclusion:** Dropbox approach is simpler (2 points less complex)

---

## 7. Cost Analysis

### 7.1 Infrastructure Costs (Monthly)

#### Version 2.0 (Database)

| Service | Tier | Cost | Notes |
|---------|------|------|-------|
| **PostgreSQL Hosting** | | | |
| Supabase Free | Free | $0 | 500MB, 2 concurrent connections |
| Supabase Pro | Pro | $25 | 8GB, 120 concurrent connections |
| Neon Free | Free | $0 | 0.5GB, 3 compute units |
| Neon Scale | Scale | $19 | 10GB, autoscaling |
| Railway Hobby | Hobby | $5 | Shared resources |
| Railway Pro | Pro | $20 | Dedicated resources |
| **Backend Hosting** | | | |
| Vercel Free | Free | $0 | Serverless functions |
| Railway Free | Free | $0 | 500 hours |
| **Frontend Hosting** | | | |
| Vercel Free | Free | $0 | Unlimited bandwidth |
| Netlify Free | Free | $0 | 100GB bandwidth |

**Total Monthly Cost:**
- Minimum: $0 (free tiers, limited)
- Typical: $25-45 (Supabase Pro + hosting)
- Annual: $300-540

#### Version 3.1 (Dropbox)

| Service | Tier | Cost | Notes |
|---------|------|------|-------|
| **Dropbox** | Existing | $0 | Already have account |
| **Backend Hosting** | | | |
| Vercel Free | Free | $0 | Serverless functions |
| Railway Free | Free | $0 | 500 hours |
| **Frontend Hosting** | | | |
| Vercel Free | Free | $0 | Unlimited bandwidth |
| Netlify Free | Free | $0 | 100GB bandwidth |

**Total Monthly Cost:**
- Minimum: $0 (all free tiers)
- Typical: $0 (Dropbox already exists)
- Annual: $0

**Savings:** $300-540/year

### 7.2 Development Cost

**Time to Implement (Full Application):**

| Phase | Database Version | Dropbox Version | Time Saved |
|-------|------------------|-----------------|------------|
| Setup | 6-9 hours | 4-6 hours | 2-3 hours |
| Backend Development | 40-50 hours | 30-40 hours | 10 hours |
| Frontend Development | 30-40 hours | 30-40 hours | 0 hours |
| Testing | 20-30 hours | 15-25 hours | 5 hours |
| Deployment | 4-6 hours | 2-4 hours | 2 hours |
| **Total** | **100-135 hours** | **81-115 hours** | **19-20 hours** |

**Cost Savings (at $50/hour):** $950-1,000

---

## 8. Migration Path

### 8.1 Current State → Database Version

**Required Steps:**

1. **Export Data from CSV/JSON**
   ```python
   # Export Search Queue
   search_queue = pd.read_csv('Search_Queue_Master.csv')
   search_queue.to_sql('search_queue', engine, if_exists='replace')

   # Export Video Queue
   video_queue = pd.read_csv('Video_Queue_Master.csv')
   video_queue.to_sql('video_queue', engine, if_exists='replace')

   # Export Entities
   for json_file in glob('LIBRARIES/**/*.json'):
       entity = json.load(open(json_file))
       # Insert into entities table
   ```

2. **Update All Scripts**
   - Replace CSV operations with Prisma queries
   - Update all file paths to database calls
   - Test thoroughly

3. **Maintain Dual System**
   - Keep CSV files for backup
   - Export database to CSV regularly
   - Run parallel for 1-2 months

**Estimated Effort:** 40-60 hours
**Risk Level:** High (data integrity, script breakage)

### 8.2 Current State → Dropbox Version

**Required Steps:**

1. **Get Dropbox Access Token**
   - Log into Dropbox
   - Create app
   - Generate token
   - Set environment variable

2. **Create Dropbox Service**
   ```typescript
   // dropboxService.ts
   import { Dropbox } from 'dropbox';
   const dbx = new Dropbox({ accessToken: process.env.DROPBOX_ACCESS_TOKEN });
   ```

3. **Implement File Operations**
   - Read CSV → Dropbox API
   - Write CSV → Dropbox API
   - Read JSON → Dropbox API
   - Write JSON → Dropbox API

**Estimated Effort:** 8-12 hours
**Risk Level:** Low (uses existing files as-is)

**Conclusion:** Dropbox migration is 5x easier

---

## 9. Final Recommendation

### 9.1 Decision Matrix

| Criteria | Weight | Database (v2.0) | Dropbox (v3.1) | Winner |
|----------|--------|----------------|----------------|--------|
| **Aligns with Current System** | 25% | 2/10 (requires migration) | 10/10 (uses existing files) | 🏆 Dropbox |
| **Development Cost** | 20% | 5/10 (100-135 hours) | 8/10 (81-115 hours) | 🏆 Dropbox |
| **Infrastructure Cost** | 15% | 4/10 ($300-540/year) | 10/10 ($0/year) | 🏆 Dropbox |
| **Performance** | 15% | 9/10 (faster) | 7/10 (adequate) | Database |
| **Scalability** | 10% | 10/10 (millions of records) | 7/10 (thousands of records) | Database |
| **Ease of Use** | 10% | 6/10 (SQL knowledge) | 9/10 (CSV/JSON) | 🏆 Dropbox |
| **Deployment Simplicity** | 5% | 5/10 (complex) | 9/10 (simple) | 🏆 Dropbox |

**Weighted Scores:**
- **Database (v2.0):** 5.55/10
- **Dropbox (v3.1):** 8.65/10

**Winner:** 🏆 **Dropbox API (Version 3.1)**

### 9.2 Recommendation

**✅ USE VERSION 3.1 (COMPLETE-APP-GENERATION-PROMPT_1.md)**

**Reasons:**

1. **Aligns with Current System** - Uses existing CSV/JSON files, no migration needed
2. **Zero Cost** - No database hosting fees
3. **Faster Development** - 20 hours less development time
4. **Simpler Deployment** - No database setup required
5. **Human-Readable** - CSV/JSON files easy to inspect and edit
6. **Adequate Performance** - Current system proves file-based approach works
7. **Team Familiarity** - Team already uses CSV/JSON workflow

**When to Reconsider:**
- If scale exceeds 10,000 videos
- If complex queries become critical
- If concurrent users > 100
- If performance becomes issue (not expected for years)

---

## 10. Action Items

### 10.1 Immediate Actions

- [x] ✅ **Use COMPLETE-APP-GENERATION-PROMPT_1.md as primary prompt**
- [x] ✅ **Archive COMPLETE-APP-GENERATION-PROMPT.md (database version)**
- [ ] 🔄 **Update all documentation to reference v3.1**
- [ ] 🔄 **Create Dropbox Service implementation**
- [ ] 🔄 **Begin frontend/backend development using v3.1**

### 10.2 Documentation Updates

**Files to Update:**

1. **README.md** - Point to v3.1 as primary
2. **ARCHITECTURE-OVERVIEW.md** - Update to show Dropbox API
3. **HOW-TO-BUILD-APP.md** - Reference v3.1
4. **FUNCTIONAL.md** - Ensure Dropbox examples
5. **deployment guides** - Remove database setup steps

### 10.3 Development Roadmap

**Phase 1: Backend (Dropbox API) - 2 weeks**
- Set up Express.js server
- Implement Dropbox Service
- Create CSV/JSON utils
- Implement Search Queue routes
- Implement Video Queue routes
- Add priority calculation
- Test all endpoints

**Phase 2: Frontend (React) - 2 weeks**
- Set up Vite + React
- Implement design system
- Create Search Queue module
- Create Video Queue module
- Add Zustand state management
- Integrate with backend API
- Test all features

**Phase 3: Deployment - 1 week**
- Deploy backend to Vercel/Railway
- Deploy frontend to Vercel
- Configure Dropbox access token
- Test production environment
- Set up monitoring

**Total Timeline:** 5 weeks

---

## Appendix A: Code Examples

### A.1 Dropbox Service Implementation

```typescript
// backend/src/services/dropboxService.ts
import { Dropbox } from 'dropbox';
import csv from 'csv-parser';
import { Readable } from 'stream';

export class DropboxService {
  private dbx: Dropbox;

  constructor() {
    this.dbx = new Dropbox({
      accessToken: process.env.DROPBOX_ACCESS_TOKEN
    });
  }

  async readCSV(filePath: string): Promise<any[]> {
    try {
      // Download file from Dropbox
      const response = await this.dbx.filesDownload({ path: filePath });
      const buffer = (response.result as any).fileBinary;

      // Parse CSV
      return new Promise((resolve, reject) => {
        const results: any[] = [];
        const readable = Readable.from(buffer.toString());

        readable
          .pipe(csv())
          .on('data', (data) => results.push(data))
          .on('end', () => resolve(results))
          .on('error', reject);
      });
    } catch (error) {
      console.error('Error reading CSV:', error);
      throw error;
    }
  }

  async writeCSV(filePath: string, data: any[]): Promise<void> {
    try {
      // Convert to CSV string
      const csvString = this.arrayToCSV(data);

      // Upload to Dropbox
      await this.dbx.filesUpload({
        path: filePath,
        contents: csvString,
        mode: { '.tag': 'overwrite' }
      });
    } catch (error) {
      console.error('Error writing CSV:', error);
      throw error;
    }
  }

  async readJSON(filePath: string): Promise<any> {
    try {
      const response = await this.dbx.filesDownload({ path: filePath });
      const buffer = (response.result as any).fileBinary;
      return JSON.parse(buffer.toString());
    } catch (error) {
      console.error('Error reading JSON:', error);
      throw error;
    }
  }

  async writeJSON(filePath: string, data: any): Promise<void> {
    try {
      const jsonString = JSON.stringify(data, null, 2);
      await this.dbx.filesUpload({
        path: filePath,
        contents: jsonString,
        mode: { '.tag': 'overwrite' }
      });
    } catch (error) {
      console.error('Error writing JSON:', error);
      throw error;
    }
  }

  private arrayToCSV(data: any[]): string {
    if (data.length === 0) return '';

    const headers = Object.keys(data[0]);
    const rows = data.map(row =>
      headers.map(header => JSON.stringify(row[header] || '')).join(',')
    );

    return [headers.join(','), ...rows].join('\n');
  }
}

export default new DropboxService();
```

### A.2 Video Queue Controller (Dropbox)

```typescript
// backend/src/controllers/videoQueueController.ts
import { Request, Response } from 'express';
import dropboxService from '../services/dropboxService';
import { calculatePriority } from '../utils/priorityCalculator';

const VIDEO_QUEUE_CSV = '/RESEARCHES/Video_Queue_Master.csv';

export const videoQueueController = {
  // Get all videos
  async getAllVideos(req: Request, res: Response) {
    try {
      const videos = await dropboxService.readCSV(VIDEO_QUEUE_CSV);
      res.json(videos);
    } catch (error) {
      res.status(500).json({ error: 'Failed to fetch videos' });
    }
  },

  // Add new video
  async addVideo(req: Request, res: Response) {
    try {
      const videos = await dropboxService.readCSV(VIDEO_QUEUE_CSV);

      const newVideo = {
        Queue_ID: `VQ-${String(videos.length + 1).padStart(3, '0')}`,
        ...req.body,
        Priority: calculatePriority(req.body),
        Status: 'Pending',
        Date_Added: new Date().toISOString()
      };

      videos.push(newVideo);
      await dropboxService.writeCSV(VIDEO_QUEUE_CSV, videos);

      res.status(201).json(newVideo);
    } catch (error) {
      res.status(500).json({ error: 'Failed to add video' });
    }
  },

  // Update video
  async updateVideo(req: Request, res: Response) {
    try {
      const { id } = req.params;
      const videos = await dropboxService.readCSV(VIDEO_QUEUE_CSV);

      const index = videos.findIndex(v => v.Queue_ID === id);
      if (index === -1) {
        return res.status(404).json({ error: 'Video not found' });
      }

      videos[index] = { ...videos[index], ...req.body };
      await dropboxService.writeCSV(VIDEO_QUEUE_CSV, videos);

      res.json(videos[index]);
    } catch (error) {
      res.status(500).json({ error: 'Failed to update video' });
    }
  },

  // Delete video
  async deleteVideo(req: Request, res: Response) {
    try {
      const { id } = req.params;
      const videos = await dropboxService.readCSV(VIDEO_QUEUE_CSV);

      const filtered = videos.filter(v => v.Queue_ID !== id);
      if (filtered.length === videos.length) {
        return res.status(404).json({ error: 'Video not found' });
      }

      await dropboxService.writeCSV(VIDEO_QUEUE_CSV, filtered);
      res.json({ message: 'Video deleted' });
    } catch (error) {
      res.status(500).json({ error: 'Failed to delete video' });
    }
  }
};
```

---

## Conclusion

**Use Version 3.1 (COMPLETE-APP-GENERATION-PROMPT_1.md)** with Dropbox API as the primary architecture for the RESEARCHES 2 application.

This decision is based on:
- ✅ Alignment with current system
- ✅ Zero infrastructure cost
- ✅ Faster development time
- ✅ Adequate performance
- ✅ Simpler deployment
- ✅ Human-readable files

The database approach (v2.0) should only be considered if scale exceeds 10,000 videos or if complex SQL queries become critical requirements.

---

**Document Status:** Complete
**Next Steps:** Begin implementation using v3.1
**Estimated Timeline:** 5 weeks to production
**Priority:** High

---

*Generated: 2025-12-09*
*Version: 1.0*
