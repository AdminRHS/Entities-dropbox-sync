# Supabase Database Schema - Research Management System

## Purpose
Complete PostgreSQL database schema for a Research Management System with 8 tables supporting a 7-phase video research workflow, multi-user collaboration, and AI-powered entity extraction.

## Context
This database will power 2 separate web applications:
1. **Queue Management App** - Manages search and video queues with priority scoring
2. **Video Processing App** - Multi-agent AI orchestration for extracting entities from video transcriptions

## Technology Stack
- **Database**: PostgreSQL 14+ (via Supabase)
- **Extensions**: pgvector (optional - for semantic search with embeddings)
- **Features Used**:
  - UUID primary keys
  - JSONB for flexible data
  - CHECK constraints for data integrity
  - Foreign key relationships
  - Indexes for performance
  - Row-Level Security (RLS)
  - Real-time subscriptions

## Database Tables (8 Total)

### Table 1: employees
**Purpose**: Store employee information for assignment tracking and authentication

```sql
CREATE TABLE employees (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  department TEXT NOT NULL CHECK (department IN ('VID', 'AID', 'HRM', 'FIN', 'MKT', 'ALL')),
  role TEXT NOT NULL CHECK (role IN ('Researcher', 'Analyst', 'Admin')),
  active BOOLEAN DEFAULT true,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Sample data
INSERT INTO employees (name, email, department, role) VALUES
  ('Alice Johnson', 'alice@example.com', 'VID', 'Researcher'),
  ('Bob Smith', 'bob@example.com', 'AID', 'Analyst'),
  ('Charlie Brown', 'charlie@example.com', 'HRM', 'Researcher'),
  ('Admin User', 'admin@example.com', 'ALL', 'Admin');
```

**Field Descriptions**:
- `id`: Unique identifier (UUID auto-generated)
- `name`: Employee full name
- `email`: Unique email (used for login)
- `department`: Department assignment
  - VID (Video Research)
  - AID (AI Development)
  - HRM (Human Resources)
  - FIN (Finance)
  - MKT (Marketing)
  - ALL (Cross-department/Admin)
- `role`: Permission level
  - Researcher (can create and edit own items)
  - Analyst (can view and analyze all items)
  - Admin (full access)
- `active`: Whether employee account is active
- `created_at`: Account creation timestamp

---

### Table 2: search_queue
**Purpose**: Track search task assignments for video discovery

```sql
CREATE TABLE search_queue (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  search_id TEXT UNIQUE NOT NULL, -- Format: SEARCH-001, SEARCH-002
  employee_id UUID REFERENCES employees(id) ON DELETE SET NULL,
  department TEXT NOT NULL,
  topic TEXT NOT NULL,
  search_query TEXT NOT NULL,
  status TEXT NOT NULL CHECK (status IN ('Assigned', 'In Progress', 'Completed')) DEFAULT 'Assigned',
  videos_found INTEGER DEFAULT 0 CHECK (videos_found >= 0),
  date_assigned DATE NOT NULL DEFAULT CURRENT_DATE,
  date_completed DATE,
  notes TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Trigger to auto-update updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_search_queue_updated_at BEFORE UPDATE ON search_queue
FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Sample data
INSERT INTO search_queue (search_id, employee_id, department, topic, search_query, status, videos_found, notes) VALUES
  ('SEARCH-001', (SELECT id FROM employees WHERE email = 'alice@example.com'), 'VID', 'AI Video Tools', 'ai video generation tools 2024', 'Completed', 5, 'Found several GLIF tutorials'),
  ('SEARCH-002', (SELECT id FROM employees WHERE email = 'bob@example.com'), 'AID', 'LLM Research', 'large language model training techniques', 'In Progress', 2, 'Still searching');
```

**Field Descriptions**:
- `search_id`: Human-readable ID (SEARCH-001, SEARCH-002, etc.)
- `employee_id`: FK to employees table (who is assigned)
- `department`: Department requesting the search
- `topic`: Research topic category
- `search_query`: Exact search query used
- `status`: Workflow status (Assigned → In Progress → Completed)
- `videos_found`: Count of videos discovered
- `date_assigned`: When search was assigned
- `date_completed`: When search was completed (NULL if in progress)
- `notes`: Additional context, findings, insights

---

### Table 3: video_queue
**Purpose**: Manage video processing queue with priority scoring and metadata

```sql
CREATE TABLE video_queue (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  queue_id TEXT UNIQUE NOT NULL, -- Format: VQ-001, VQ-002
  video_id TEXT NOT NULL, -- YouTube video ID (11 chars)
  video_title TEXT NOT NULL,
  channel_name TEXT NOT NULL,
  channel_url TEXT,
  video_url TEXT NOT NULL,
  views INTEGER DEFAULT 0 CHECK (views >= 0),
  likes INTEGER DEFAULT 0 CHECK (likes >= 0),
  comments INTEGER DEFAULT 0 CHECK (comments >= 0),
  publish_date DATE,
  duration TEXT, -- Format: HH:MM:SS or MM:SS
  added_by UUID REFERENCES employees(id) ON DELETE SET NULL,
  added_date DATE NOT NULL DEFAULT CURRENT_DATE,
  status TEXT NOT NULL CHECK (status IN ('Pending', 'Selected', 'Transcribing', 'Parsed', 'Completed', 'Skipped')) DEFAULT 'Pending',
  selected_by UUID REFERENCES employees(id) ON DELETE SET NULL,
  selected_date DATE,
  parsed_date DATE,
  topic_category TEXT,
  research_source TEXT, -- Perplexity, YouTube, Manual, Gemini, Claude
  priority_score INTEGER DEFAULT 0 CHECK (priority_score >= 0 AND priority_score <= 100),
  notes TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

CREATE TRIGGER update_video_queue_updated_at BEFORE UPDATE ON video_queue
FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Sample data
INSERT INTO video_queue (queue_id, video_id, video_title, channel_name, video_url, views, likes, comments, publish_date, duration, added_by, topic_category, research_source, priority_score) VALUES
  ('VQ-001', 'dQw4w9WgXcQ', 'How To Use AI Agents to 10x Your Creative AI Game', 'AI for Grownups', 'https://youtube.com/watch?v=dQw4w9WgXcQ', 150000, 5200, 340, '2024-11-10', '15:32', (SELECT id FROM employees WHERE email = 'alice@example.com'), 'AI Automation', 'Perplexity', 85),
  ('VQ-002', 'xXxXxXxXxXx', 'Complete Guide to Large Language Models', 'Tech Channel', 'https://youtube.com/watch?v=xXxXxXxXxXx', 75000, 2100, 180, '2024-11-15', '22:45', (SELECT id FROM employees WHERE email = 'bob@example.com'), 'LLM Research', 'YouTube', 72);
```

**Field Descriptions**:
- `queue_id`: Human-readable ID (VQ-001, VQ-002, etc.)
- `video_id`: YouTube video ID (11 characters)
- `video_title`: Full video title
- `channel_name`: YouTube channel name
- `channel_url`: Full channel URL
- `video_url`: Full video URL
- `views`: View count at time of addition
- `likes`: Like count at time of addition
- `comments`: Comment count at time of addition
- `publish_date`: Video publication date
- `duration`: Video length (HH:MM:SS format)
- `added_by`: FK to employee who added video
- `added_date`: Date added to queue
- `status`: Processing status
  - Pending: Not yet selected
  - Selected: Chosen for processing
  - Transcribing: Transcription in progress
  - Parsed: Transcription complete
  - Completed: All phases done
  - Skipped: Not processing this video
- `selected_by`: FK to employee who selected for processing
- `selected_date`: When selected
- `parsed_date`: When transcription completed
- `topic_category`: Content category
- `research_source`: Where video was found
- `priority_score`: Calculated score (0-100)
- `notes`: Additional metadata, tags, context

---

### Table 4: video_progress
**Purpose**: Track video processing through all 7 phases (Phase 0 → Complete)

```sql
CREATE TABLE video_progress (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  video_queue_id UUID REFERENCES video_queue(id) ON DELETE CASCADE,
  video_number INTEGER NOT NULL, -- 1, 2, 3, etc. (Video_001, Video_002)
  phase_0_search TEXT DEFAULT 'Not Started' CHECK (phase_0_search IN ('Not Started', 'In Progress', 'Complete')),
  phase_1_transcribed TEXT DEFAULT 'Not Started' CHECK (phase_1_transcribed IN ('Not Started', 'In Progress', 'Complete')),
  phase_2_extraction TEXT DEFAULT 'Not Started' CHECK (phase_2_extraction IN ('Not Started', 'In Progress', 'Complete')),
  phase_3_gap_analysis TEXT DEFAULT 'Not Started' CHECK (phase_3_gap_analysis IN ('Not Started', 'In Progress', 'Complete')),
  phase_4_integration TEXT DEFAULT 'Not Started' CHECK (phase_4_integration IN ('Not Started', 'In Progress', 'Complete')),
  phase_5_mapping TEXT DEFAULT 'Not Started' CHECK (phase_5_mapping IN ('Not Started', 'In Progress', 'Complete')),
  complete BOOLEAN DEFAULT false,
  transcription_text TEXT, -- Full markdown transcription (can also use Supabase Storage)
  extraction_data JSONB, -- Extracted entities as JSON
  gap_analysis_data JSONB, -- Gap analysis results as JSON
  mapping_report TEXT, -- Final library mapping report (markdown)
  last_updated TIMESTAMP WITH TIME ZONE DEFAULT now(),
  notes TEXT,
  UNIQUE(video_number) -- Ensure unique video numbers
);

-- Sample data
INSERT INTO video_progress (video_queue_id, video_number, phase_0_search, phase_1_transcribed, phase_2_extraction, transcription_text) VALUES
  ((SELECT id FROM video_queue WHERE queue_id = 'VQ-001'), 1, 'Complete', 'Complete', 'In Progress', '# Video Title\n\n## Transcription\nFull transcription here...');
```

**Field Descriptions**:
- `video_queue_id`: FK to video_queue (which video this tracks)
- `video_number`: Sequential number (1, 2, 3) - matches Video_001.md naming
- `phase_0_search`: Search/discovery phase status
- `phase_1_transcribed`: Transcription phase status
- `phase_2_extraction`: Entity extraction phase status
- `phase_3_gap_analysis`: Gap analysis phase status
- `phase_4_integration`: Integration phase status
- `phase_5_mapping`: Library mapping phase status
- `complete`: Boolean - true when all phases complete
- `transcription_text`: Full markdown transcription (TEXT column)
  - Alternative: Store file path if using Supabase Storage
- `extraction_data`: Extracted entities stored as JSONB
- `gap_analysis_data`: Gap analysis results stored as JSONB
- `mapping_report`: Final mapping report (markdown TEXT)
- `last_updated`: Auto-updated timestamp
- `notes`: Current status, blockers, next steps

---

### Table 5: extracted_entities
**Purpose**: Store individual entities extracted from video transcriptions

```sql
CREATE TABLE extracted_entities (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  video_progress_id UUID REFERENCES video_progress(id) ON DELETE CASCADE,
  entity_type TEXT NOT NULL CHECK (entity_type IN ('Tool', 'Workflow', 'Action', 'Object', 'Skill', 'Profession')),
  entity_name TEXT NOT NULL,
  entity_code TEXT, -- TOOL-AI-045, WRF-012, OBJ-015, etc.
  status TEXT NOT NULL CHECK (status IN ('NEW', 'EXISTS', 'NEEDS_UPDATE')),
  priority TEXT CHECK (priority IN ('CRITICAL', 'HIGH', 'MEDIUM', 'LOW')),
  category TEXT,
  description TEXT,
  evidence_from_video TEXT, -- Line numbers, timestamps, or quotes
  integration_status TEXT CHECK (integration_status IN ('Pending', 'Integrated', 'Skipped')) DEFAULT 'Pending',
  metadata JSONB, -- Additional flexible data (use cases, integrations, etc.)
  created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Sample data
INSERT INTO extracted_entities (video_progress_id, entity_type, entity_name, entity_code, status, priority, category, description, evidence_from_video) VALUES
  ((SELECT id FROM video_progress WHERE video_number = 1), 'Tool', 'GLIF', 'TOOL-AI-045', 'NEW', 'CRITICAL', 'AI Workflow Automation', 'AI-powered workflow automation platform', 'Lines 45-67, timestamp 02:15'),
  ((SELECT id FROM video_progress WHERE video_number = 1), 'Workflow', 'AI Thumbnail Generator', 'WRF-012', 'NEW', 'HIGH', 'Content Creation', 'Automated thumbnail creation workflow', 'Lines 120-145');
```

**Field Descriptions**:
- `video_progress_id`: FK to video_progress (source video)
- `entity_type`: Type of entity
  - Tool: Software, platform, library
  - Workflow: Process, procedure
  - Action: Verb, task, operation
  - Object: Deliverable, artifact, output
  - Skill: Competency, capability
  - Profession: Role, job title
- `entity_name`: Display name
- `entity_code`: Unique code (TOOL-AI-045, WRF-012, etc.)
- `status`:
  - NEW: Not in existing library
  - EXISTS: Already in library
  - NEEDS_UPDATE: Exists but needs enhancement
- `priority`: Integration priority
- `category`: Subcategory/classification
- `description`: What it is/does
- `evidence_from_video`: Where it was mentioned (line numbers, timestamps)
- `integration_status`: Whether it's been integrated
- `metadata`: JSONB for flexible data (use cases, integrations, URLs, etc.)

---

### Table 6: ai_api_usage
**Purpose**: Track AI API costs and usage per video processing

```sql
CREATE TABLE ai_api_usage (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  video_progress_id UUID REFERENCES video_progress(id) ON DELETE CASCADE,
  api_provider TEXT NOT NULL CHECK (api_provider IN ('OpenRouter', 'Claude', 'GPT', 'Gemini')),
  model TEXT NOT NULL, -- e.g., anthropic/claude-sonnet-3.5, openai/gpt-4-turbo
  phase TEXT NOT NULL CHECK (phase IN ('Phase_2', 'Phase_3', 'Phase_4', 'Phase_5')),
  prompt_tokens INTEGER DEFAULT 0 CHECK (prompt_tokens >= 0),
  completion_tokens INTEGER DEFAULT 0 CHECK (completion_tokens >= 0),
  total_tokens INTEGER DEFAULT 0 CHECK (total_tokens >= 0),
  cost_usd NUMERIC(10, 6) DEFAULT 0, -- Up to $9999.999999
  request_timestamp TIMESTAMP WITH TIME ZONE DEFAULT now(),
  response_time_seconds NUMERIC(10, 3), -- Up to 9999999.999 seconds
  success BOOLEAN DEFAULT true,
  error_message TEXT
);

-- Sample data
INSERT INTO ai_api_usage (video_progress_id, api_provider, model, phase, prompt_tokens, completion_tokens, total_tokens, cost_usd, response_time_seconds, success) VALUES
  ((SELECT id FROM video_progress WHERE video_number = 1), 'OpenRouter', 'anthropic/claude-sonnet-3.5', 'Phase_2', 15000, 8000, 23000, 0.115, 12.5, true),
  ((SELECT id FROM video_progress WHERE video_number = 1), 'Claude', 'claude-3-5-sonnet-20241022', 'Phase_3', 8000, 5000, 13000, 0.065, 8.2, true);
```

**Field Descriptions**:
- `video_progress_id`: FK to video being processed
- `api_provider`: Which API was used
- `model`: Specific model used
- `phase`: Which processing phase
- `prompt_tokens`: Input tokens
- `completion_tokens`: Output tokens
- `total_tokens`: Sum of input + output
- `cost_usd`: Cost in USD
- `request_timestamp`: When API was called
- `response_time_seconds`: How long request took
- `success`: Whether request succeeded
- `error_message`: Error details if failed

---

### Table 7: prompt_templates
**Purpose**: Store AI prompt templates for each processing phase

```sql
CREATE TABLE prompt_templates (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  template_id TEXT UNIQUE NOT NULL, -- PMT-004, PMT-007, PMT-009, etc.
  template_name TEXT NOT NULL,
  template_description TEXT,
  phase TEXT CHECK (phase IN ('Phase_1', 'Phase_2', 'Phase_3', 'Phase_4', 'Phase_5')),
  system_prompt TEXT NOT NULL,
  user_prompt_template TEXT NOT NULL, -- With {{variables}} for substitution
  recommended_model TEXT,
  temperature NUMERIC(3, 2) DEFAULT 0.7 CHECK (temperature >= 0 AND temperature <= 1),
  max_tokens INTEGER DEFAULT 4000 CHECK (max_tokens > 0),
  active BOOLEAN DEFAULT true,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

CREATE TRIGGER update_prompt_templates_updated_at BEFORE UPDATE ON prompt_templates
FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Sample data
INSERT INTO prompt_templates (template_id, template_name, template_description, phase, system_prompt, user_prompt_template, recommended_model, temperature) VALUES
  ('PMT-007', 'Entity Extraction', 'Extract entities from video transcription', 'Phase_2',
   'You are an expert at extracting structured entities from video transcriptions.',
   'Extract all Tools, Workflows, Actions, Objects, Skills, and Professions from this transcription:\n\n{{transcription}}',
   'anthropic/claude-sonnet-3.5', 0.3),
  ('PMT-009-P1', 'Gap Analysis', 'Compare extracted entities against existing library', 'Phase_3',
   'You are an expert at comparing extracted entities against existing libraries to identify gaps.',
   'Compare these extracted entities:\n{{entities}}\n\nAgainst existing library:\n{{library}}\n\nIdentify NEW, EXISTING, and NEEDS_UPDATE items.',
   'openai/gpt-4-turbo', 0.5);
```

**Field Descriptions**:
- `template_id`: Unique template ID (PMT-XXX)
- `template_name`: Display name
- `template_description`: What the template does
- `phase`: Which processing phase it's for
- `system_prompt`: AI system instructions
- `user_prompt_template`: User prompt with {{variable}} placeholders
- `recommended_model`: Suggested AI model
- `temperature`: Sampling temperature (0.0-1.0)
- `max_tokens`: Maximum response length
- `active`: Whether template is currently in use
- `created_at`, `updated_at`: Timestamps

---

### Table 8: ai_provider_config
**Purpose**: Store API keys and configuration for AI providers

```sql
CREATE TABLE ai_provider_config (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  provider_name TEXT UNIQUE NOT NULL CHECK (provider_name IN ('OpenRouter', 'Claude', 'GPT', 'Gemini')),
  api_key TEXT NOT NULL, -- Store encrypted (use Supabase Vault in production)
  base_url TEXT,
  enabled BOOLEAN DEFAULT true,
  priority INTEGER DEFAULT 1 CHECK (priority >= 1 AND priority <= 4),
  cost_per_million_tokens NUMERIC(10, 2),
  rate_limit_per_minute INTEGER,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

CREATE TRIGGER update_ai_provider_config_updated_at BEFORE UPDATE ON ai_provider_config
FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Sample data (use fake keys - replace with real ones in production)
INSERT INTO ai_provider_config (provider_name, api_key, base_url, enabled, priority, cost_per_million_tokens, rate_limit_per_minute) VALUES
  ('OpenRouter', 'sk-or-v1-xxx-FAKE-KEY', 'https://openrouter.ai/api/v1', true, 1, 5.00, 60),
  ('Claude', 'sk-ant-xxx-FAKE-KEY', 'https://api.anthropic.com', true, 2, 15.00, 50),
  ('GPT', 'sk-xxx-FAKE-KEY', 'https://api.openai.com/v1', true, 3, 10.00, 60),
  ('Gemini', 'AIza-xxx-FAKE-KEY', 'https://generativelanguage.googleapis.com', true, 4, 7.00, 60);
```

**Field Descriptions**:
- `provider_name`: API provider name
- `api_key`: API key (encrypt in production using Supabase Vault)
- `base_url`: API base URL
- `enabled`: Whether provider is active
- `priority`: Fallback order (1 = primary, 4 = last resort)
- `cost_per_million_tokens`: Estimated cost per 1M tokens
- `rate_limit_per_minute`: Max requests per minute

---

## Performance Indexes

```sql
-- Video queue indexes
CREATE INDEX idx_video_queue_status ON video_queue(status);
CREATE INDEX idx_video_queue_priority ON video_queue(priority_score DESC);
CREATE INDEX idx_video_queue_added_date ON video_queue(added_date DESC);

-- Search queue indexes
CREATE INDEX idx_search_queue_status ON search_queue(status);
CREATE INDEX idx_search_queue_employee ON search_queue(employee_id);

-- Extracted entities indexes
CREATE INDEX idx_extracted_entities_type ON extracted_entities(entity_type);
CREATE INDEX idx_extracted_entities_status ON extracted_entities(status);
CREATE INDEX idx_extracted_entities_priority ON extracted_entities(priority);

-- AI usage indexes
CREATE INDEX idx_ai_usage_provider ON ai_api_usage(api_provider);
CREATE INDEX idx_ai_usage_timestamp ON ai_api_usage(request_timestamp DESC);

-- Prompt templates index
CREATE INDEX idx_prompt_templates_phase ON prompt_templates(phase);
CREATE INDEX idx_prompt_templates_active ON prompt_templates(active);
```

---

## pgvector Extension (Optional - for Semantic Search)

```sql
-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Add embedding column to extracted_entities
ALTER TABLE extracted_entities ADD COLUMN embedding vector(1536); -- OpenAI ada-002 dimensions

-- Create index for vector similarity search
CREATE INDEX ON extracted_entities USING ivfflat (embedding vector_cosine_ops)
WITH (lists = 100);

-- Example: Find similar entities
-- SELECT entity_name, description,
--        1 - (embedding <=> '[your_query_embedding]') AS similarity
-- FROM extracted_entities
-- ORDER BY embedding <=> '[your_query_embedding]'
-- LIMIT 10;
```

**Use Cases for pgvector**:
- Find similar tools/workflows across videos
- Detect duplicate entities
- Semantic search through research content
- AI-powered recommendations
- Automated entity matching

---

## Row-Level Security (RLS) Policies

```sql
-- Enable RLS on all tables
ALTER TABLE employees ENABLE ROW LEVEL SECURITY;
ALTER TABLE search_queue ENABLE ROW LEVEL SECURITY;
ALTER TABLE video_queue ENABLE ROW LEVEL SECURITY;
ALTER TABLE video_progress ENABLE ROW LEVEL SECURITY;
ALTER TABLE extracted_entities ENABLE ROW LEVEL SECURITY;
ALTER TABLE ai_api_usage ENABLE ROW LEVEL SECURITY;
ALTER TABLE prompt_templates ENABLE ROW LEVEL SECURITY;
ALTER TABLE ai_provider_config ENABLE ROW LEVEL SECURITY;

-- Example policies (adjust based on your authentication setup)

-- Employees: Everyone can read, only admins can modify
CREATE POLICY "Public read access" ON employees FOR SELECT USING (true);
CREATE POLICY "Admins can insert" ON employees FOR INSERT
  WITH CHECK (auth.jwt() ->> 'role' = 'Admin');

-- Search queue: Users can see their own + their department
CREATE POLICY "Users see own department" ON search_queue FOR SELECT
  USING (
    department = (SELECT department FROM employees WHERE id = auth.uid())
    OR (SELECT role FROM employees WHERE id = auth.uid()) = 'Admin'
  );

-- Video queue: All authenticated users can read
CREATE POLICY "Authenticated read" ON video_queue FOR SELECT
  USING (auth.role() = 'authenticated');

-- Video progress: All authenticated users can read
CREATE POLICY "Authenticated read" ON video_progress FOR SELECT
  USING (auth.role() = 'authenticated');

-- Extracted entities: All authenticated users can read
CREATE POLICY "Authenticated read" ON extracted_entities FOR SELECT
  USING (auth.role() = 'authenticated');

-- AI usage: Admins only
CREATE POLICY "Admins only" ON ai_api_usage FOR SELECT
  USING ((SELECT role FROM employees WHERE id = auth.uid()) = 'Admin');

-- Prompt templates: All can read, admins can modify
CREATE POLICY "Public read" ON prompt_templates FOR SELECT USING (active = true);
CREATE POLICY "Admins modify" ON prompt_templates FOR ALL
  USING ((SELECT role FROM employees WHERE id = auth.uid()) = 'Admin');

-- Provider config: Admins only
CREATE POLICY "Admins only" ON ai_provider_config FOR ALL
  USING ((SELECT role FROM employees WHERE id = auth.uid()) = 'Admin');
```

---

## Real-Time Subscriptions Setup

```sql
-- Enable real-time for tables that need live updates
-- (This is configured in Supabase Dashboard → Database → Replication)

-- Tables to enable real-time on:
-- ✅ video_queue (for live queue updates)
-- ✅ search_queue (for live search status)
-- ✅ video_progress (for live phase tracking)
-- ❌ extracted_entities (too many updates, poll instead)
-- ❌ ai_api_usage (not needed real-time)
```

---

## Utility Functions

```sql
-- Function to auto-generate next Queue ID
CREATE OR REPLACE FUNCTION generate_queue_id()
RETURNS TEXT AS $$
DECLARE
  next_id INTEGER;
BEGIN
  SELECT COALESCE(MAX(CAST(SUBSTRING(queue_id FROM 4) AS INTEGER)), 0) + 1
  INTO next_id
  FROM video_queue;

  RETURN 'VQ-' || LPAD(next_id::TEXT, 3, '0');
END;
$$ LANGUAGE plpgsql;

-- Function to auto-generate next Search ID
CREATE OR REPLACE FUNCTION generate_search_id()
RETURNS TEXT AS $$
DECLARE
  next_id INTEGER;
BEGIN
  SELECT COALESCE(MAX(CAST(SUBSTRING(search_id FROM 8) AS INTEGER)), 0) + 1
  INTO next_id
  FROM search_queue;

  RETURN 'SEARCH-' || LPAD(next_id::TEXT, 3, '0');
END;
$$ LANGUAGE plpgsql;

-- Function to calculate priority score
CREATE OR REPLACE FUNCTION calculate_priority_score(
  p_views INTEGER,
  p_likes INTEGER,
  p_publish_date DATE,
  p_topic_relevance NUMERIC DEFAULT 0.5
)
RETURNS INTEGER AS $$
DECLARE
  view_score NUMERIC;
  engagement_score NUMERIC;
  recency_score NUMERIC;
  relevance_score NUMERIC;
  days_old INTEGER;
BEGIN
  -- View score (max 30 points)
  view_score := LEAST((p_views::NUMERIC / 1000000) * 30, 30);

  -- Engagement score (max 20 points)
  engagement_score := LEAST((p_likes::NUMERIC / 10000) * 20, 20);

  -- Recency score (max 25 points)
  days_old := CURRENT_DATE - p_publish_date;
  recency_score := CASE
    WHEN days_old <= 30 THEN 25
    WHEN days_old <= 90 THEN 20
    WHEN days_old <= 180 THEN 15
    ELSE 10
  END;

  -- Relevance score (max 25 points)
  relevance_score := p_topic_relevance * 25;

  RETURN ROUND(view_score + engagement_score + recency_score + relevance_score);
END;
$$ LANGUAGE plpgsql;

-- Usage example:
-- UPDATE video_queue
-- SET priority_score = calculate_priority_score(views, likes, publish_date, 0.8)
-- WHERE queue_id = 'VQ-001';
```

---

## Complete Setup SQL Script

Run this entire script in Supabase SQL Editor:

```sql
-- 1. Create all tables
-- (Copy all CREATE TABLE statements from above)

-- 2. Create triggers
-- (Copy all trigger statements from above)

-- 3. Insert sample data
-- (Copy all INSERT statements from above)

-- 4. Create indexes
-- (Copy all CREATE INDEX statements from above)

-- 5. Enable pgvector (optional)
-- (Copy pgvector statements from above)

-- 6. Set up RLS policies
-- (Copy all RLS statements from above)

-- 7. Create utility functions
-- (Copy all function statements from above)
```

---

## Supabase Configuration Checklist

After running the SQL:

### 1. Authentication Setup
- [ ] Go to Authentication → Settings
- [ ] Enable email authentication
- [ ] Configure email templates (optional)
- [ ] Set up redirect URLs for your app

### 2. API Keys
- [ ] Go to Project Settings → API
- [ ] Copy `anon` key (public key for client-side)
- [ ] Copy `service_role` key (secret key for server-side)
- [ ] Save both in your app's environment variables

### 3. Real-Time Configuration
- [ ] Go to Database → Replication
- [ ] Enable real-time for:
  - [x] video_queue
  - [x] search_queue
  - [x] video_progress

### 4. Storage (if storing files)
- [ ] Go to Storage
- [ ] Create bucket: `transcriptions`
- [ ] Create bucket: `reports`
- [ ] Set up bucket policies (public/private)

### 5. Security
- [ ] Review RLS policies
- [ ] Test authentication flow
- [ ] Verify API key security
- [ ] Enable database backups

---

## Testing the Schema

```sql
-- Test 1: Create employee
INSERT INTO employees (name, email, department, role) VALUES
  ('Test User', 'test@example.com', 'VID', 'Researcher')
RETURNING *;

-- Test 2: Create search
INSERT INTO search_queue (
  search_id,
  employee_id,
  department,
  topic,
  search_query
) VALUES (
  generate_search_id(),
  (SELECT id FROM employees WHERE email = 'test@example.com'),
  'VID',
  'Test Topic',
  'test query'
)
RETURNING *;

-- Test 3: Create video with priority
INSERT INTO video_queue (
  queue_id,
  video_id,
  video_title,
  channel_name,
  video_url,
  views,
  likes,
  publish_date,
  added_by,
  priority_score
) VALUES (
  generate_queue_id(),
  'testVIDEOid',
  'Test Video Title',
  'Test Channel',
  'https://youtube.com/watch?v=testVIDEOid',
  500000,
  25000,
  '2024-11-01',
  (SELECT id FROM employees WHERE email = 'test@example.com'),
  calculate_priority_score(500000, 25000, '2024-11-01', 0.9)
)
RETURNING *;

-- Test 4: Query with joins
SELECT
  vq.queue_id,
  vq.video_title,
  vq.priority_score,
  e.name AS added_by_name,
  vp.phase_2_extraction AS extraction_status
FROM video_queue vq
LEFT JOIN employees e ON vq.added_by = e.id
LEFT JOIN video_progress vp ON vq.id = vp.video_queue_id
ORDER BY vq.priority_score DESC;
```

---

## Next Steps

After setting up this schema:

1. **Configure Supabase** (see checklist above)
2. **Build App 1** - Queue Management (use Prompt 2)
3. **Build App 2** - Video Processing (use Prompt 3)
4. **Migrate Data** (optional) - Import existing CSV data

---

## Support & Resources

- **Supabase Docs**: https://supabase.com/docs
- **PostgreSQL Docs**: https://www.postgresql.org/docs/
- **pgvector Docs**: https://github.com/pgvector/pgvector
- **Supabase Discord**: https://discord.supabase.com

---

**Schema Version:** 1.0
**Last Updated:** 2025-11-27
**Compatibility:** PostgreSQL 14+, Supabase
