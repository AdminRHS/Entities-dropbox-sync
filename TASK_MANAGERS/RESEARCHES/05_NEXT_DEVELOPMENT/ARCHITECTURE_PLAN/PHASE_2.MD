# PHASE 2: GRAPH & VECTOR DATABASE ARCHITECTURE

**Phase ID:** RSH-ARCH-PHASE-2
**Status:** Planning
**Created:** 2025-11-26
**Dependencies:** PHASE 1 (PostgreSQL Infrastructure)

---

## 1. Overview

PHASE 2 extends the RESEARCHES infrastructure with advanced capabilities for relationship mapping and semantic search. This phase implements a graph database for complex entity relationships and a vector database for AI-powered semantic search across transcripts and research content.

**Key Objectives:**
- Deploy graph database (Neo4j) for entity relationships
- Implement vector database (Pinecone/Weaviate/Qdrant) for embeddings
- Generate embeddings for all transcript content
- Build semantic search capabilities
- Create relationship query APIs
- Enable AI-powered research discovery

---

## 2. Architecture Overview

### 2.1 Multi-Database Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    APPLICATION LAYER                         │
│           Dashboard / API / Search Interface                 │
└───────────────┬─────────────────┬──────────────┬────────────┘
                │                 │              │
                ▼                 ▼              ▼
┌──────────────────┐  ┌──────────────────┐  ┌──────────────┐
│   POSTGRESQL     │  │      NEO4J       │  │   VECTOR DB  │
│                  │  │   (Graph DB)     │  │  (Pinecone)  │
├──────────────────┤  ├──────────────────┤  ├──────────────┤
│ • Structured data│  │ • Relationships  │  │ • Embeddings │
│ • CSVs/JSONs     │  │ • Entity graphs  │  │ • Semantic   │
│ • Metadata       │  │ • Patterns       │  │   search     │
│ • Transactions   │  │ • Path queries   │  │ • Similarity │
└──────────────────┘  └──────────────────┘  └──────────────┘
        │                     │                     │
        └─────────────────────┴─────────────────────┘
                              │
                    ┌─────────▼──────────┐
                    │   SYNC SERVICE     │
                    │  (Data Connector)  │
                    └────────────────────┘
```

### 2.2 Database Selection Rationale

| Database | Use Case | Strengths | Limitations |
|----------|----------|-----------|-------------|
| **PostgreSQL** | Structured data, transactions | ACID compliance, mature, SQL | Limited graph traversal |
| **Neo4j** | Relationship mapping | Native graph queries, visualization | Not for large text storage |
| **Pinecone** | Vector embeddings | Managed, scalable, fast | Cost, vendor lock-in |
| **Weaviate** (Alternative) | Vector + hybrid search | Open-source, flexible | Self-hosted complexity |
| **Qdrant** (Alternative) | Vector search | Rust-based, fast, filters | Smaller ecosystem |

**Recommended:** PostgreSQL + Neo4j + Pinecone (or Weaviate for self-hosted)

---

## 3. Graph Database Design (Neo4j)

### 3.1 Node Types

#### A. Core Entity Nodes

```cypher
// Research Node
(:Research {
    research_id: "RSH-VID-001",
    title: "Video Tool Comparison",
    department: "VID",
    status: "completed",
    created_date: "2025-11-26"
})

// Video Node
(:Video {
    video_id: "Video_001",
    source_url: "https://youtube.com/watch?v=...",
    title: "AI Tools Overview",
    duration: 1200,
    status: "completed",
    phase: 7
})

// Channel Node
(:Channel {
    channel_id: "YT-CH-001",
    name: "AI Tools Daily",
    platform: "YouTube",
    subscriber_count: 150000
})

// Influencer Node
(:Influencer {
    influencer_id: "INF-001",
    name: "John Doe",
    platform: "YouTube",
    category: "AI Tools"
})

// Tool Node (extracted from analysis)
(:Tool {
    tool_id: "TOOL-001",
    name: "n8n",
    category: "Automation",
    url: "https://n8n.io"
})

// Department Node
(:Department {
    code: "VID",
    name: "Video Research",
    description: "Video processing and SMM research"
})

// Employee/Researcher Node
(:Employee {
    employee_id: "EMP-001",
    name: "Researcher Name",
    role: "Video Analyst"
})

// Concept/Topic Node
(:Topic {
    topic_id: "TOPIC-001",
    name: "AI Automation",
    category: "Technology"
})
```

#### B. Support Nodes

```cypher
// Report Node
(:Report {
    report_id: "RPT-VID-001",
    report_type: "Gap Analysis",
    file_path: "REPORTS/RSH-VID-001_Report.md"
})

// Transcript Segment
(:TranscriptSegment {
    segment_id: "Video_001_S01",
    video_id: "Video_001",
    start_time: 120,
    end_time: 180,
    text: "In this section, we discuss..."
})

// Prompt Node
(:Prompt {
    prompt_id: "PMT-044",
    title: "Sales Department Research",
    department: "SALES"
})
```

---

### 3.2 Relationship Types

#### A. Primary Relationships

```cypher
// Research to Video
(:Research)-[:ANALYZES]->(:Video)
(:Research)-[:REFERENCES]->(:Video)

// Video to Channel/Influencer
(:Video)-[:PUBLISHED_BY]->(:Channel)
(:Video)-[:CREATED_BY]->(:Influencer)
(:Channel)-[:MANAGED_BY]->(:Influencer)

// Research to Department
(:Research)-[:BELONGS_TO]->(:Department)
(:Video)-[:CATEGORIZED_IN]->(:Department)

// Research to Employee
(:Research)-[:ASSIGNED_TO]->(:Employee)
(:Research)-[:CREATED_BY]->(:Employee)

// Tool Relationships
(:Video)-[:MENTIONS {timestamp: 145, context: "demo"}]->(:Tool)
(:Research)-[:EVALUATES {rating: 4.5}]->(:Tool)
(:Tool)-[:COMPETES_WITH]->(:Tool)
(:Tool)-[:INTEGRATES_WITH]->(:Tool)

// Topic/Concept Relationships
(:Video)-[:COVERS {relevance: 0.85}]->(:Topic)
(:Research)-[:EXPLORES]->(:Topic)
(:Topic)-[:RELATED_TO {strength: 0.7}]->(:Topic)
```

#### B. Temporal & Sequential Relationships

```cypher
// Research workflow
(:Research)-[:PRECEDED_BY]->(:Research)
(:Research)-[:FOLLOWED_BY]->(:Research)

// Video processing phases
(:Video)-[:NEXT_PHASE]->(:Video)  // Same video, different phases

// Report generation
(:Research)-[:GENERATES]->(:Report)
(:Report)-[:DERIVED_FROM]->(:Research)
```

#### C. Similarity & Comparison Relationships

```cypher
// Content similarity (based on embeddings)
(:Video)-[:SIMILAR_TO {score: 0.92}]->(:Video)
(:Research)-[:SIMILAR_TO {score: 0.88}]->(:Research)

// Explicit comparisons
(:Tool)-[:COMPARED_IN]->(:Research)
(:Video)-[:COMPARED_WITH]->(:Video)
```

---

### 3.3 Graph Schema Implementation

**File:** `scripts/graph/neo4j_schema.cypher`

```cypher
// Create Constraints (Uniqueness)
CREATE CONSTRAINT research_id IF NOT EXISTS FOR (r:Research) REQUIRE r.research_id IS UNIQUE;
CREATE CONSTRAINT video_id IF NOT EXISTS FOR (v:Video) REQUIRE v.video_id IS UNIQUE;
CREATE CONSTRAINT channel_id IF NOT EXISTS FOR (c:Channel) REQUIRE c.channel_id IS UNIQUE;
CREATE CONSTRAINT influencer_id IF NOT EXISTS FOR (i:Influencer) REQUIRE i.influencer_id IS UNIQUE;
CREATE CONSTRAINT tool_id IF NOT EXISTS FOR (t:Tool) REQUIRE t.tool_id IS UNIQUE;
CREATE CONSTRAINT employee_id IF NOT EXISTS FOR (e:Employee) REQUIRE e.employee_id IS UNIQUE;

// Create Indexes (Performance)
CREATE INDEX research_department IF NOT EXISTS FOR (r:Research) ON (r.department);
CREATE INDEX research_status IF NOT EXISTS FOR (r:Research) ON (r.status);
CREATE INDEX video_status IF NOT EXISTS FOR (v:Video) ON (v.status);
CREATE INDEX video_phase IF NOT EXISTS FOR (v:Video) ON (v.phase);
CREATE INDEX tool_category IF NOT EXISTS FOR (t:Tool) ON (t.category);

// Full-Text Search Indexes
CALL db.index.fulltext.createNodeIndex(
    "videoTitles",
    ["Video"],
    ["title"]
);

CALL db.index.fulltext.createNodeIndex(
    "researchTitles",
    ["Research"],
    ["title"]
);

CALL db.index.fulltext.createNodeIndex(
    "toolNames",
    ["Tool"],
    ["name", "category"]
);
```

---

### 3.4 Graph Data Import

**File:** `scripts/graph/import_to_neo4j.py`

```python
"""
Import data from PostgreSQL to Neo4j
"""

from neo4j import GraphDatabase
import psycopg2

class Neo4jImporter:
    def __init__(self, neo4j_uri, neo4j_user, neo4j_password, pg_config):
        self.driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))
        self.pg_conn = psycopg2.connect(**pg_config)

    def import_researches(self):
        """Import researches as nodes"""
        cursor = self.pg_conn.cursor()
        cursor.execute("SELECT * FROM researches")

        with self.driver.session() as session:
            for row in cursor.fetchall():
                session.execute_write(self._create_research_node, row)

    def _create_research_node(self, tx, row):
        query = """
        MERGE (r:Research {research_id: $research_id})
        SET r.title = $title,
            r.department = $department,
            r.status = $status,
            r.created_date = $created_date
        """
        tx.run(query,
               research_id=row[1],
               title=row[2],
               department=row[3],
               status=row[4],
               created_date=str(row[5]))

    def import_relationships(self):
        """Import relationships from junction tables"""
        cursor = self.pg_conn.cursor()

        # Research-Video relationships
        cursor.execute("""
            SELECT r.research_id, v.video_id, rv.relevance_score
            FROM research_videos rv
            JOIN researches r ON rv.research_id = r.research_id
            JOIN videos v ON rv.video_id = v.video_id
        """)

        with self.driver.session() as session:
            for row in cursor.fetchall():
                session.execute_write(self._create_analyzes_relationship, row)

    def _create_analyzes_relationship(self, tx, row):
        query = """
        MATCH (r:Research {research_id: $research_id})
        MATCH (v:Video {video_id: $video_id})
        MERGE (r)-[rel:ANALYZES]->(v)
        SET rel.relevance_score = $relevance_score
        """
        tx.run(query,
               research_id=row[0],
               video_id=row[1],
               relevance_score=float(row[2]))
```

---

## 4. Vector Database Design

### 4.1 Vector Database Comparison

| Feature | Pinecone | Weaviate | Qdrant | Chroma |
|---------|----------|----------|--------|--------|
| **Deployment** | Cloud (managed) | Cloud/Self-hosted | Cloud/Self-hosted | Self-hosted |
| **Cost** | Pay-per-usage | Free tier + paid | Free tier + paid | Free (OSS) |
| **Performance** | Excellent | Very Good | Excellent | Good |
| **Filters** | Metadata filters | Class-based | Payload filters | Metadata filters |
| **Hybrid Search** | No | Yes | Yes | Limited |
| **Scalability** | Auto-scale | Manual/Auto | Manual/Auto | Limited |
| **Ecosystem** | Mature | Growing | Growing | Young |

**Recommendation:** Weaviate (best balance of features, cost, and flexibility)

---

### 4.2 Weaviate Schema Design

**File:** `scripts/vector/weaviate_schema.json`

```json
{
  "classes": [
    {
      "class": "VideoTranscript",
      "description": "Video transcript segments with embeddings",
      "vectorizer": "text2vec-openai",
      "moduleConfig": {
        "text2vec-openai": {
          "model": "text-embedding-3-small",
          "dimensions": 1536
        }
      },
      "properties": [
        {
          "name": "video_id",
          "dataType": ["string"],
          "description": "Video identifier"
        },
        {
          "name": "segment_id",
          "dataType": ["string"],
          "description": "Unique segment identifier"
        },
        {
          "name": "text",
          "dataType": ["text"],
          "description": "Transcript text content"
        },
        {
          "name": "start_time",
          "dataType": ["int"],
          "description": "Segment start time in seconds"
        },
        {
          "name": "end_time",
          "dataType": ["int"],
          "description": "Segment end time in seconds"
        },
        {
          "name": "department",
          "dataType": ["string"],
          "description": "Department category"
        },
        {
          "name": "created_date",
          "dataType": ["date"],
          "description": "Processing date"
        }
      ]
    },
    {
      "class": "ResearchDocument",
      "description": "Research reports and findings",
      "vectorizer": "text2vec-openai",
      "moduleConfig": {
        "text2vec-openai": {
          "model": "text-embedding-3-small",
          "dimensions": 1536
        }
      },
      "properties": [
        {
          "name": "research_id",
          "dataType": ["string"],
          "description": "Research identifier"
        },
        {
          "name": "title",
          "dataType": ["string"],
          "description": "Research title"
        },
        {
          "name": "content",
          "dataType": ["text"],
          "description": "Full research content"
        },
        {
          "name": "department",
          "dataType": ["string"],
          "description": "Department code"
        },
        {
          "name": "status",
          "dataType": ["string"],
          "description": "Research status"
        },
        {
          "name": "report_type",
          "dataType": ["string"],
          "description": "Type of report"
        },
        {
          "name": "created_date",
          "dataType": ["date"],
          "description": "Creation date"
        }
      ]
    },
    {
      "class": "ToolDescription",
      "description": "Extracted tool descriptions and features",
      "vectorizer": "text2vec-openai",
      "properties": [
        {
          "name": "tool_id",
          "dataType": ["string"]
        },
        {
          "name": "tool_name",
          "dataType": ["string"]
        },
        {
          "name": "description",
          "dataType": ["text"]
        },
        {
          "name": "category",
          "dataType": ["string"]
        },
        {
          "name": "features",
          "dataType": ["text[]"]
        },
        {
          "name": "use_cases",
          "dataType": ["text[]"]
        }
      ]
    }
  ]
}
```

---

### 4.3 Embedding Generation Pipeline

**File:** `scripts/vector/generate_embeddings.py`

```python
"""
Generate embeddings for transcripts and research documents
"""

import openai
from typing import List
import weaviate
from weaviate.util import generate_uuid5

class EmbeddingGenerator:
    def __init__(self, openai_api_key: str, weaviate_url: str):
        openai.api_key = openai_api_key
        self.client = weaviate.Client(weaviate_url)

    def generate_embedding(self, text: str, model: str = "text-embedding-3-small") -> List[float]:
        """Generate embedding for a single text"""
        response = openai.embeddings.create(
            input=text,
            model=model
        )
        return response.data[0].embedding

    def chunk_transcript(self, transcript: str, chunk_size: int = 500, overlap: int = 50) -> List[dict]:
        """Split transcript into overlapping chunks"""
        words = transcript.split()
        chunks = []

        for i in range(0, len(words), chunk_size - overlap):
            chunk_text = ' '.join(words[i:i + chunk_size])
            chunks.append({
                'text': chunk_text,
                'start_word': i,
                'end_word': min(i + chunk_size, len(words))
            })

        return chunks

    def import_video_transcript(self, video_id: str, transcript: str, metadata: dict):
        """Import video transcript with embeddings"""
        chunks = self.chunk_transcript(transcript)

        with self.client.batch as batch:
            for idx, chunk in enumerate(chunks):
                segment_id = f"{video_id}_S{idx:03d}"

                data_object = {
                    "video_id": video_id,
                    "segment_id": segment_id,
                    "text": chunk['text'],
                    "start_time": chunk.get('start_time', 0),
                    "end_time": chunk.get('end_time', 0),
                    "department": metadata.get('department', ''),
                    "created_date": metadata.get('created_date', '')
                }

                batch.add_data_object(
                    data_object=data_object,
                    class_name="VideoTranscript",
                    uuid=generate_uuid5(segment_id)
                )

    def import_research_document(self, research_id: str, content: str, metadata: dict):
        """Import research document with embeddings"""
        data_object = {
            "research_id": research_id,
            "title": metadata.get('title', ''),
            "content": content,
            "department": metadata.get('department', ''),
            "status": metadata.get('status', ''),
            "report_type": metadata.get('report_type', ''),
            "created_date": metadata.get('created_date', '')
        }

        self.client.data_object.create(
            data_object=data_object,
            class_name="ResearchDocument",
            uuid=generate_uuid5(research_id)
        )
```

---

### 4.4 Semantic Search Implementation

**File:** `scripts/vector/semantic_search.py`

```python
"""
Semantic search across transcripts and research documents
"""

import weaviate
from typing import List, Dict, Any

class SemanticSearch:
    def __init__(self, weaviate_url: str):
        self.client = weaviate.Client(weaviate_url)

    def search_transcripts(self, query: str, department: str = None, limit: int = 10) -> List[Dict]:
        """Search video transcripts by semantic similarity"""

        # Build query
        where_filter = None
        if department:
            where_filter = {
                "path": ["department"],
                "operator": "Equal",
                "valueString": department
            }

        result = (
            self.client.query
            .get("VideoTranscript", ["video_id", "segment_id", "text", "start_time", "department"])
            .with_near_text({"concepts": [query]})
            .with_limit(limit)
        )

        if where_filter:
            result = result.with_where(where_filter)

        response = result.do()

        return response['data']['Get']['VideoTranscript']

    def search_researches(self, query: str, filters: Dict = None, limit: int = 10) -> List[Dict]:
        """Search research documents by semantic similarity"""

        result = (
            self.client.query
            .get("ResearchDocument", ["research_id", "title", "content", "department", "report_type"])
            .with_near_text({"concepts": [query]})
            .with_limit(limit)
        )

        if filters:
            where_filter = self._build_where_filter(filters)
            result = result.with_where(where_filter)

        response = result.do()

        return response['data']['Get']['ResearchDocument']

    def find_similar_videos(self, video_id: str, limit: int = 5) -> List[Dict]:
        """Find videos similar to a given video"""

        # Get the first segment of the source video
        source = (
            self.client.query
            .get("VideoTranscript", ["video_id", "text"])
            .with_where({
                "path": ["video_id"],
                "operator": "Equal",
                "valueString": video_id
            })
            .with_limit(1)
            .do()
        )

        if not source['data']['Get']['VideoTranscript']:
            return []

        source_text = source['data']['Get']['VideoTranscript'][0]['text']

        # Find similar segments
        similar = (
            self.client.query
            .get("VideoTranscript", ["video_id", "segment_id", "text"])
            .with_near_text({"concepts": [source_text]})
            .with_limit(limit + 10)  # Get extra to filter out same video
            .do()
        )

        # Filter out same video
        results = [
            s for s in similar['data']['Get']['VideoTranscript']
            if s['video_id'] != video_id
        ]

        return results[:limit]

    def hybrid_search(self, query: str, department: str = None, date_range: tuple = None) -> List[Dict]:
        """Combine semantic search with filters"""

        where_conditions = []

        if department:
            where_conditions.append({
                "path": ["department"],
                "operator": "Equal",
                "valueString": department
            })

        if date_range:
            start_date, end_date = date_range
            where_conditions.append({
                "path": ["created_date"],
                "operator": "GreaterThanEqual",
                "valueDate": start_date
            })
            where_conditions.append({
                "path": ["created_date"],
                "operator": "LessThanEqual",
                "valueDate": end_date
            })

        where_filter = None
        if len(where_conditions) > 1:
            where_filter = {"operator": "And", "operands": where_conditions}
        elif len(where_conditions) == 1:
            where_filter = where_conditions[0]

        result = (
            self.client.query
            .get("VideoTranscript", ["video_id", "segment_id", "text", "department", "created_date"])
            .with_hybrid(query=query, alpha=0.7)  # 0.7 = more semantic, 0.3 = more keyword
            .with_limit(20)
        )

        if where_filter:
            result = result.with_where(where_filter)

        response = result.do()

        return response['data']['Get']['VideoTranscript']
```

---

## 5. Query Scenarios & Use Cases

### 5.1 Graph Query Examples

#### A. Find Research Path

```cypher
// Find all videos analyzed in a research
MATCH (r:Research {research_id: "RSH-VID-001"})-[:ANALYZES]->(v:Video)
RETURN r.title, v.video_id, v.title

// Find all tools mentioned in research-related videos
MATCH (r:Research {research_id: "RSH-VID-001"})-[:ANALYZES]->(v:Video)-[:MENTIONS]->(t:Tool)
RETURN DISTINCT t.name, t.category, COUNT(v) as mentions
ORDER BY mentions DESC

// Find similar researches based on shared videos
MATCH (r1:Research {research_id: "RSH-VID-001"})-[:ANALYZES]->(v:Video)<-[:ANALYZES]-(r2:Research)
WHERE r1 <> r2
RETURN r2.research_id, r2.title, COUNT(v) as shared_videos
ORDER BY shared_videos DESC
```

#### B. Influencer Network Analysis

```cypher
// Find influencers creating content on similar topics
MATCH (i1:Influencer)-[:CREATED]->(:Video)-[:COVERS]->(t:Topic)<-[:COVERS]-(:Video)<-[:CREATED]-(i2:Influencer)
WHERE i1 <> i2
RETURN i1.name, i2.name, COUNT(DISTINCT t) as shared_topics
ORDER BY shared_topics DESC

// Find channel collaboration potential
MATCH (c1:Channel)-[:PUBLISHED]->(:Video)-[:MENTIONS]->(tool:Tool)<-[:MENTIONS]-(:Video)<-[:PUBLISHED]-(c2:Channel)
WHERE c1 <> c2
RETURN c1.name, c2.name, COLLECT(DISTINCT tool.name) as shared_tools
```

#### C. Research Workflow Tracking

```cypher
// Find research dependencies
MATCH path = (r1:Research)-[:PRECEDED_BY*]->(r2:Research)
WHERE r1.research_id = "RSH-VID-010"
RETURN path

// Find all outputs from a research
MATCH (r:Research {research_id: "RSH-VID-001"})-[:GENERATES]->(report:Report)
RETURN report.report_type, report.file_path
```

---

### 5.2 Vector Search Examples

#### A. Semantic Content Discovery

```python
# Find transcripts discussing "AI automation workflows"
search = SemanticSearch(weaviate_url)

results = search.search_transcripts(
    query="AI automation workflows for small businesses",
    department="AI",
    limit=10
)

for result in results:
    print(f"Video: {result['video_id']}")
    print(f"Segment: {result['segment_id']}")
    print(f"Text: {result['text'][:200]}...")
    print("---")
```

#### B. Research Gap Analysis

```python
# Find researches similar to a topic not yet covered
existing_researches = search.search_researches(
    query="Video editing AI tools",
    filters={"department": "DESIGN"},
    limit=5
)

# If no results, it's a gap!
if not existing_researches:
    print("Gap identified: No research on video editing AI tools in DESIGN department")
```

#### C. Cross-Department Discovery

```python
# Find relevant content across all departments
results = search.hybrid_search(
    query="employee onboarding automation",
    date_range=("2025-01-01", "2025-12-31")
)

# Group by department
by_department = {}
for r in results:
    dept = r['department']
    if dept not in by_department:
        by_department[dept] = []
    by_department[dept].append(r)

print(f"Found content in {len(by_department)} departments")
```

---

### 5.3 Combined Graph + Vector Queries

**File:** `scripts/hybrid/combined_query.py`

```python
"""
Combined queries across graph and vector databases
"""

class HybridQueryEngine:
    def __init__(self, neo4j_driver, weaviate_client):
        self.neo4j = neo4j_driver
        self.weaviate = weaviate_client

    def find_expert_path(self, topic: str, target_employee_id: str):
        """
        Find learning path from topic to expert
        1. Semantic search for relevant videos
        2. Graph traversal to find expert connections
        """

        # Step 1: Find relevant videos with vector search
        semantic_results = SemanticSearch(self.weaviate).search_transcripts(
            query=topic,
            limit=20
        )

        video_ids = [r['video_id'] for r in semantic_results]

        # Step 2: Graph query to find path to expert
        with self.neo4j.session() as session:
            result = session.run("""
                MATCH path = shortestPath(
                    (v:Video)-[*]-(e:Employee {employee_id: $employee_id})
                )
                WHERE v.video_id IN $video_ids
                RETURN path, length(path) as path_length
                ORDER BY path_length ASC
                LIMIT 5
            """, video_ids=video_ids, employee_id=target_employee_id)

            return [record['path'] for record in result]

    def recommend_next_research(self, department: str):
        """
        Recommend next research based on:
        1. Existing research patterns (graph)
        2. Content gaps (vector)
        """

        # Analyze research patterns
        with self.neo4j.session() as session:
            patterns = session.run("""
                MATCH (r:Research {department: $department})-[:EXPLORES]->(t:Topic)
                RETURN t.name, COUNT(r) as research_count
                ORDER BY research_count DESC
            """, department=department)

            covered_topics = [record['t.name'] for record in patterns]

        # Find content that doesn't match existing patterns
        # This would indicate gap areas
        # Implementation depends on specific requirements

        return {
            'covered_topics': covered_topics,
            'recommended_gaps': []  # To be implemented
        }
```

---

## 6. Integration & Sync Architecture

### 6.1 Data Flow

```
┌──────────────┐
│  PostgreSQL  │  (Source of Truth)
└──────┬───────┘
       │
       ▼
┌──────────────────┐
│  Sync Service    │
│  - Change detect │
│  - Transform     │
│  - Route         │
└────┬────────┬────┘
     │        │
     ▼        ▼
┌─────────┐  ┌──────────┐
│  Neo4j  │  │ Weaviate │
└─────────┘  └──────────┘
```

### 6.2 Sync Service Implementation

**File:** `scripts/sync/database_sync.py`

```python
"""
Sync service to keep PostgreSQL, Neo4j, and Weaviate in sync
"""

import time
from typing import List
import psycopg2
from neo4j import GraphDatabase
import weaviate

class DatabaseSync:
    def __init__(self, pg_config, neo4j_config, weaviate_url):
        self.pg_conn = psycopg2.connect(**pg_config)
        self.neo4j_driver = GraphDatabase.driver(
            neo4j_config['uri'],
            auth=(neo4j_config['user'], neo4j_config['password'])
        )
        self.weaviate_client = weaviate.Client(weaviate_url)
        self.last_sync_timestamp = {}

    def detect_changes(self, table_name: str) -> List[dict]:
        """Detect changes since last sync"""
        cursor = self.pg_conn.cursor()

        last_sync = self.last_sync_timestamp.get(table_name, '1970-01-01')

        query = f"""
            SELECT * FROM {table_name}
            WHERE updated_date > %s OR created_date > %s
            ORDER BY COALESCE(updated_date, created_date) DESC
        """

        cursor.execute(query, (last_sync, last_sync))

        return cursor.fetchall()

    def sync_research_to_neo4j(self, research_data: dict):
        """Sync research record to Neo4j"""
        with self.neo4j_driver.session() as session:
            session.execute_write(self._upsert_research_node, research_data)

    def sync_transcript_to_weaviate(self, video_id: str, transcript: str, metadata: dict):
        """Sync transcript to Weaviate for semantic search"""
        embedder = EmbeddingGenerator(openai_key, weaviate_url)
        embedder.import_video_transcript(video_id, transcript, metadata)

    def run_continuous_sync(self, interval: int = 60):
        """Run continuous sync loop"""
        print(f"Starting continuous sync (interval: {interval}s)")

        while True:
            try:
                # Sync researches
                research_changes = self.detect_changes('researches')
                for change in research_changes:
                    self.sync_research_to_neo4j(change)

                # Sync videos
                video_changes = self.detect_changes('videos')
                for change in video_changes:
                    if change['transcript_content']:
                        self.sync_transcript_to_weaviate(
                            change['video_id'],
                            change['transcript_content'],
                            {'department': change['department']}
                        )

                # Update sync timestamps
                self.last_sync_timestamp['researches'] = time.time()
                self.last_sync_timestamp['videos'] = time.time()

                time.sleep(interval)

            except Exception as e:
                print(f"Sync error: {e}")
                time.sleep(interval)
```

---

## 7. API Extensions for Advanced Queries

### 7.1 Graph Query API

**File:** `api/graph_api.py`

```python
"""
GraphQL API for Neo4j queries
"""

from ariadne import QueryType, make_executable_schema
from neo4j import GraphDatabase

type_defs = """
    type Query {
        research(id: ID!): Research
        findSimilarResearches(id: ID!, limit: Int): [Research]
        researchNetwork(department: String!): ResearchNetwork
        toolMentions(toolName: String!): [VideoToolMention]
    }

    type Research {
        research_id: ID!
        title: String!
        department: String!
        videos: [Video]
        tools: [Tool]
    }

    type Video {
        video_id: ID!
        title: String
        channel: Channel
    }

    type Tool {
        tool_id: ID!
        name: String!
        category: String
    }

    type ResearchNetwork {
        nodes: [ResearchNode]
        edges: [ResearchEdge]
    }
"""

query = QueryType()

@query.field("research")
def resolve_research(_, info, id):
    driver = info.context["neo4j_driver"]

    with driver.session() as session:
        result = session.run("""
            MATCH (r:Research {research_id: $id})
            OPTIONAL MATCH (r)-[:ANALYZES]->(v:Video)
            RETURN r, COLLECT(v) as videos
        """, id=id)

        record = result.single()
        if not record:
            return None

        return {
            "research_id": record['r']['research_id'],
            "title": record['r']['title'],
            "department": record['r']['department'],
            "videos": record['videos']
        }

schema = make_executable_schema(type_defs, query)
```

### 7.2 Semantic Search API

**File:** `api/semantic_api.py`

```python
"""
Semantic search API endpoints
"""

from fastapi import APIRouter, Query
from typing import List, Optional

router = APIRouter(prefix="/api/v1/semantic")

@router.get("/search/transcripts")
async def search_transcripts(
    q: str = Query(..., description="Search query"),
    department: Optional[str] = None,
    limit: int = Query(10, le=50)
):
    """Semantic search across video transcripts"""
    search_engine = SemanticSearch(weaviate_url)

    results = search_engine.search_transcripts(
        query=q,
        department=department,
        limit=limit
    )

    return {
        "query": q,
        "filters": {"department": department},
        "count": len(results),
        "results": results
    }

@router.get("/similar/videos/{video_id}")
async def find_similar_videos(video_id: str, limit: int = 5):
    """Find videos similar to the given video"""
    search_engine = SemanticSearch(weaviate_url)

    results = search_engine.find_similar_videos(video_id, limit)

    return {
        "source_video_id": video_id,
        "similar_videos": results
    }

@router.post("/recommend/research")
async def recommend_research(department: str, topics: List[str]):
    """Recommend research areas based on topics"""
    # Combine semantic search with graph analysis
    hybrid_engine = HybridQueryEngine(neo4j_driver, weaviate_client)

    recommendations = hybrid_engine.recommend_next_research(department)

    return recommendations
```

---

## 8. Visualization & Dashboard Integration

### 8.1 Graph Visualization

**Tools:**
- **Neo4j Bloom** - Interactive graph exploration
- **D3.js** - Custom web visualizations
- **Gephi** - Network analysis and visualization

**Export for Visualization:**

```python
def export_graph_for_viz(research_id: str) -> dict:
    """Export graph data in D3-compatible format"""
    with driver.session() as session:
        result = session.run("""
            MATCH (r:Research {research_id: $id})-[rel]-(connected)
            RETURN r, rel, connected
        """, id=research_id)

        nodes = []
        links = []

        for record in result:
            nodes.append({
                "id": record['r']['research_id'],
                "label": record['r']['title'],
                "type": "research"
            })
            nodes.append({
                "id": record['connected']['id'],
                "label": record['connected'].get('name', record['connected'].get('title')),
                "type": record['connected'].labels[0].lower()
            })
            links.append({
                "source": record['r']['research_id'],
                "target": record['connected']['id'],
                "type": type(record['rel']).__name__
            })

        return {"nodes": nodes, "links": links}
```

### 8.2 Semantic Search UI

**React Component Example:**

```jsx
// components/SemanticSearch.jsx

import { useState } from 'react';

export default function SemanticSearch() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    setLoading(true);

    const response = await fetch(`/api/v1/semantic/search/transcripts?q=${encodeURIComponent(query)}`);
    const data = await response.json();

    setResults(data.results);
    setLoading(false);
  };

  return (
    <div className="semantic-search">
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search transcripts semantically..."
      />
      <button onClick={handleSearch} disabled={loading}>
        {loading ? 'Searching...' : 'Search'}
      </button>

      <div className="results">
        {results.map((result, idx) => (
          <div key={idx} className="result-card">
            <h3>{result.video_id}</h3>
            <p>{result.text}</p>
            <span>Department: {result.department}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
```

---

## 9. Performance & Scalability

### 9.1 Performance Targets

| Operation | Target | Notes |
|-----------|--------|-------|
| Graph query (single hop) | < 50ms | Indexed lookups |
| Graph query (3+ hops) | < 500ms | Path traversal |
| Vector search (top 10) | < 200ms | With filters |
| Vector search (top 100) | < 1s | Bulk retrieval |
| Embedding generation | < 2s per chunk | OpenAI API |
| Batch import (1000 nodes) | < 30s | Neo4j batch |

### 9.2 Optimization Strategies

**Neo4j:**
- Index frequently queried properties
- Use relationship direction for better performance
- Limit query depth with path length constraints
- Use query profiling: `EXPLAIN` and `PROFILE`

**Weaviate:**
- Use appropriate vector dimensions (balance quality vs speed)
- Implement metadata filters before vector search
- Use batch imports for large datasets
- Configure HNSW parameters for use case

### 9.3 Scalability Considerations

**Neo4j Scaling:**
- Single instance: up to ~10M nodes, ~50M relationships
- Clustering (Enterprise): horizontal scaling
- Read replicas for query distribution

**Weaviate Scaling:**
- Vertical: increase resources (RAM, CPU)
- Horizontal: sharding (coming in future versions)
- Cloud: managed scaling

---

## 10. Limitations & Trade-offs

### 10.1 Known Limitations

| Component | Limitation | Impact | Mitigation |
|-----------|------------|--------|------------|
| Neo4j | Memory-intensive for large graphs | Cost | Optimize query patterns, use indexes |
| Weaviate | No native sharding (yet) | Scale limits | Vertical scaling, filter optimization |
| Embeddings | API cost for large volumes | Budget | Cache embeddings, batch processing |
| Sync delay | Multi-DB sync latency | Data freshness | Acceptable delay (< 1 min) |
| Query complexity | Graph + vector queries slow | UX | Pre-compute common queries |

### 10.2 Design Trade-offs

| Decision | Choice | Trade-off |
|----------|--------|-----------|
| Managed vs Self-hosted | Weaviate self-hosted | Lower cost, more maintenance |
| Embedding model | text-embedding-3-small | Lower cost, slightly less quality |
| Sync frequency | 60 seconds | Balance freshness vs load |
| Graph depth | Limit to 5 hops | Performance vs completeness |
| Vector dimensions | 1536 | Good balance quality/speed |

---

## 11. Testing & Validation

### 11.1 Test Scenarios

```python
# test_graph_queries.py

def test_research_video_relationship():
    """Test research-video relationship creation"""
    with driver.session() as session:
        # Create test data
        session.run("""
            CREATE (r:Research {research_id: 'TEST-001', title: 'Test Research'})
            CREATE (v:Video {video_id: 'Video_TEST', title: 'Test Video'})
            CREATE (r)-[:ANALYZES {relevance: 0.9}]->(v)
        """)

        # Query
        result = session.run("""
            MATCH (r:Research {research_id: 'TEST-001'})-[rel:ANALYZES]->(v:Video)
            RETURN r, rel, v
        """)

        record = result.single()
        assert record['r']['research_id'] == 'TEST-001'
        assert record['rel']['relevance'] == 0.9

def test_semantic_search():
    """Test vector search functionality"""
    search = SemanticSearch(weaviate_test_url)

    results = search.search_transcripts(
        query="AI automation",
        limit=5
    )

    assert len(results) > 0
    assert 'video_id' in results[0]
    assert 'text' in results[0]
```

---

## 12. Deployment Plan

### 12.1 Deployment Phases

**Phase 2A: Neo4j Setup (Week 1-2)**
- [ ] Install Neo4j (Community/Enterprise)
- [ ] Create graph schema
- [ ] Import initial data from PostgreSQL
- [ ] Test basic queries
- [ ] Set up Neo4j Browser access

**Phase 2B: Weaviate Setup (Week 3-4)**
- [ ] Deploy Weaviate (Docker/Cloud)
- [ ] Configure schema and vectorizers
- [ ] Generate embeddings for existing transcripts
- [ ] Import embeddings
- [ ] Test semantic search

**Phase 2C: Integration (Week 5-6)**
- [ ] Implement sync service
- [ ] Build combined query APIs
- [ ] Create dashboard visualizations
- [ ] Performance testing
- [ ] Documentation

---

## 13. Success Criteria

### 13.1 Phase Completion Checklist

- [ ] Neo4j operational with complete schema
- [ ] All research-video relationships mapped
- [ ] Tool extraction and linking complete
- [ ] Weaviate operational with embeddings for all transcripts
- [ ] Semantic search API functional
- [ ] Graph query API functional
- [ ] Sync service running continuously
- [ ] Performance targets met
- [ ] Dashboard integration complete
- [ ] Documentation and runbooks complete

---

## 14. Risks & Mitigations

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Embedding API costs exceed budget | HIGH | MEDIUM | Batch processing, caching, cost monitoring |
| Graph queries too slow | HIGH | MEDIUM | Query optimization, indexes, caching |
| Data sync errors | CRITICAL | LOW | Robust error handling, retry logic, monitoring |
| Vector search quality issues | MEDIUM | MEDIUM | Tune embedding model, chunk size optimization |
| Neo4j licensing costs | MEDIUM | LOW | Start with Community, evaluate Enterprise needs |

---

## 15. Future Enhancements

### 15.1 Advanced Features (Phase 3+)

- **Graph ML:** Node classification, link prediction
- **Auto-tagging:** AI-powered topic extraction
- **Recommendation Engine:** Research suggestion system
- **Real-time updates:** WebSocket-based live sync
- **Multi-modal search:** Image + text search
- **Knowledge Graph Reasoning:** Inference rules
- **Temporal Graphs:** Time-based relationship analysis

---

## 16. Documentation & Resources

### 16.1 Required Documentation

- [ ] Neo4j schema documentation
- [ ] Weaviate schema documentation
- [ ] Query pattern cookbook
- [ ] API documentation (OpenAPI/Swagger)
- [ ] Sync service runbook
- [ ] Troubleshooting guide
- [ ] Performance tuning guide

### 16.2 Training Materials

- [ ] Graph query tutorial
- [ ] Semantic search guide
- [ ] Dashboard user guide
- [ ] Administrator handbook

---

**Document Status:** Draft
**Last Updated:** 2025-11-26
**Next Review:** After Phase 2 implementation
**Owner:** RESEARCHES Advanced Features Team
