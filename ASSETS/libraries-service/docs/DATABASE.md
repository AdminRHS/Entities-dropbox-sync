# Database Architecture

Complete database schema documentation for libraries-service

## Overview
- **Total Models**: 35
- **Total Migrations**: 37
- **DBMS**: PostgreSQL 12+
- **ORM**: Sequelize 6.35.1

## Architecture Philosophy

### Terms System
All entities use **TermGroup → Terms → Languages** pattern for multilingual support.

**Benefits**:
- No schema changes when adding languages
- Centralized terminology management
- AI-friendly (single location for translations)
- Support for synonyms and similar terms

## Core Models Summary

### Terms System (5 models)
| Model | Purpose | Key Fields |
|-------|---------|------------|
| **TermGroup** | Container for related terms | id, name, main_term_id, icon |
| **Term** | Individual term/translation | id, value, language_id, term_type_id, ai_* fields |
| **TermGroupRelation** | M:N between TermGroup & Term | term_group_id, term_id, priority |
| **TermType** | Type classification | id, name (main/similar/translation) |
| **Language** | Language info | id, iso2, iso3, term_group_id |

### Organizational Entities (4 models)
| Model | Purpose | Key Associations |
|-------|---------|------------------|
| **Department** | Organizational departments | hasMany Profession, belongsTo TermGroup |
| **Profession** | Job professions | belongsTo Department, belongsToMany Tool |
| **Position** | Job positions | belongsTo TermGroup |
| **Level** | Experience levels | belongsTo TermGroup |

### Geographic Entities (4 models)
| Model | Purpose | Key Fields |
|-------|---------|------------|
| **Country** | Countries | iso2, iso3, currency_id, term_group_id |
| **City** | Cities | country_id, latitude, longitude, term_group_id |
| **Currency** | Currencies | code (ISO 4217), symbol, name |
| **Rate** | Exchange rates | from_currency_id, to_currency_id, rate |

### Business Entities
| Model | Purpose |
|-------|---------|
| **Industry** | Industry sectors |
| **SubIndustry** | Industry subcategories |
| **Action** | Action verbs for responsibilities |
| **Object** | Object nouns for responsibilities |
| **Responsibility** | Composite of Action + Object |
| **Tool** | Software tools/technologies |
| **ToolType** | Tool categories |
| **Skill** | Composite of Responsibility + Tool |
| **Format** | File/content formats |
| **Service** | Business services |
| **Shift** | Work shifts |

### Support Models
| Model | Purpose |
|-------|---------|
| **Status** | Global statuses |
| **Priority** | Priority levels |
| **Entity** | Entity categories |
| **EntityType** | Entity type classifications |
| **MCP** | Model Context Protocol services |

## Key Relationships

\
## Junction Tables (M:N)
1. **term_group_relations** - TermGroup ↔ Term
2. **profession_tools** - Profession ↔ Tool
3. **tool_tool_types** - Tool ↔ ToolType
4. **object_formats** - Object ↔ Format
5. **status_services** - Status ↔ Service

## Migration History (37 total)

Key migrations:
1. **20250609113843** - Initial tables
2. **20250707000001** - Terms system (TermType, Term, TermGroup, TermGroupRelation)
3. **20250707000002** - AI models (AIConfig, AIPrompt, AIGeneration, AIFeedback)
4. **20250707000010** - Tools and relationships
5. **20250715000013** - Drop libraries table (migrated to terms)
6. **20250721000020** - Move AI metadata to terms
7. **20250722000022-28** - Geographic/Business entities
8. **20250723000030** - Skills model
9. **20250723000032** - MCP services

## Common Query Patterns

### Fetch Entity with Terms
\
### Search Terms
\%\%\

## Indexes

**Key indexes for performance**:
- \ with pg_trgm for search
- All foreign keys indexed
- Composite indexes for common queries
- Unique constraints on junction tables

## Model Locations
- **Models**: - **Migrations**: - **Seeders**: 
---

**Last Updated**: 2025-01-12  
**See Also**: [TECH_STACK.md](TECH_STACK.md), [API.md](API.md)
