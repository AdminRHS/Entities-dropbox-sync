-- Phase 0 test schema (PostgreSQL) for loading data_listing_structured.json / data_listing_markdown.json

CREATE TABLE IF NOT EXISTS researches (
    id              SERIAL PRIMARY KEY,
    research_id     VARCHAR(50) UNIQUE NOT NULL,
    name            TEXT,
    description     TEXT,
    department      VARCHAR(20),
    status          VARCHAR(20),
    created_date    TIMESTAMP,
    updated_date    TIMESTAMP,
    researcher_id   VARCHAR(50),
    metadata        JSONB,
    output_path     TEXT
);

CREATE TABLE IF NOT EXISTS videos (
    id              SERIAL PRIMARY KEY,
    video_id        VARCHAR(50) UNIQUE NOT NULL,
    queue_id        VARCHAR(50),
    video_title     TEXT,
    channel_name    TEXT,
    channel_url     TEXT,
    video_url       TEXT,
    views           INTEGER,
    likes           INTEGER,
    comments        INTEGER,
    publish_date    TIMESTAMP,
    duration        TEXT,
    added_by        TEXT,
    added_date      TIMESTAMP,
    status          VARCHAR(20),
    selected_by     TEXT,
    selected_date   TIMESTAMP,
    parsed_date     TIMESTAMP,
    topic_category  TEXT,
    research_source TEXT,
    priority_score  NUMERIC,
    notes           TEXT,
    created_date    TIMESTAMP,
    completed_date  TIMESTAMP,
    channel_id      TEXT,
    transcript_path TEXT,
    phase           TEXT
);

CREATE TABLE IF NOT EXISTS search_queue (
    id              SERIAL PRIMARY KEY,
    search_id       VARCHAR(50) UNIQUE NOT NULL,
    employee        TEXT,
    department      VARCHAR(20),
    topic           TEXT,
    query           TEXT,
    status          VARCHAR(20),
    videos_found    INTEGER,
    date_assigned   TIMESTAMP,
    date_completed  TIMESTAMP,
    results_path    TEXT,
    priority        INTEGER,
    assigned_to     TEXT,
    notes           TEXT
);

CREATE TABLE IF NOT EXISTS tool_mapping (
    id          SERIAL PRIMARY KEY,
    name        TEXT,
    tool_id     TEXT,
    category    TEXT,
    file_path   TEXT
);

CREATE TABLE IF NOT EXISTS discovered_tools (
    id          SERIAL PRIMARY KEY,
    name        TEXT,
    status      TEXT,
    category    TEXT,
    source      TEXT,
    tool_id     TEXT
);

CREATE TABLE IF NOT EXISTS markdown_files (
    id              SERIAL PRIMARY KEY,
    path            TEXT UNIQUE NOT NULL,
    entity_id       TEXT,
    entity_type     TEXT,
    department      TEXT,
    status          TEXT,
    phase           TEXT,
    last_modified   TIMESTAMP
);
