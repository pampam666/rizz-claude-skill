---
name: framework-researcher
description: AUTO-TRIGGERS when framework research or web search needed for prompt engineering. Keywords include web search, framework analysis, prompt documentation, prompting guide, anthropic docs. Phrases include search prompting frameworks, research prompt techniques, analyze framework documentation, gather sources. Context is research phase of prompt research workflow. DOES NOT trigger for general web searches, non-prompt topics, or comparison table creation.
---

# Framework Researcher

Specialist skill for conducting rigorous multi-source research on prompt engineering frameworks.

## Mission

Conduct scientist-level research on prompt engineering frameworks using web search, GDrive link processing, and authoritative documentation with source prioritization.

## Activation Protocol

### Automatic Triggers
- TOC confirmation received
- Research phase initiated by mother-orchestrator
- User provides GDrive links for analysis

### Input Requirements

| Input | Source | Required |
|-------|--------|----------|
| `frameworks_to_compare` | workflow_state.json | Yes |
| `gdrive_links` | workflow_state.json | Optional |
| `special_requirements` | workflow_state.json | Optional |

## Research Methodology

### Phase 1: Source Prioritization

Follow strict source hierarchy:

| Priority | Source Type | Examples | Weight |
|----------|-------------|----------|--------|
| 1 | Official Documentation | Anthropic docs, OpenAI docs | 10 |
| 2 | Academic Papers | arXiv, peer-reviewed journals | 9 |
| 3 | Authoritative Guides | PromptingGuide.ai, Learn Prompting | 8 |
| 4 | Technical Blogs | Official company blogs | 6 |
| 5 | Community Resources | GitHub, forums | 4 |

### Phase 2: Web Search Protocol

**Primary Sources (search first):**

1. **PromptingGuide.ai**
   - Search query: `site:promptingguide.ai [framework name]`
   - Extract: descriptions, examples, references

2. **Anthropic Documentation**
   - Search query: `site:docs.anthropic.com [framework name]`
   - Extract: best practices, implementation guides

3. **Academic Sources**
   - Search query: `site:arxiv.org [framework name] prompting`
   - Extract: methodology, benchmarks, citations

**Search Execution:**
```
For each framework:
1. Search PromptingGuide.ai
2. Search Anthropic docs
3. Search arXiv for papers
4. Search official framework papers
5. Compile sources with metadata
```

### Phase 3: Framework Data Extraction

For each framework, extract:

```json
{
  "framework_name": {
    "description": "2-3 sentence overview",
    "core_mechanism": "How it works",
    "thinking_process": "LLM reasoning pattern",
    "typical_use_cases": ["use case 1", "use case 2"],
    "implementation_complexity": "Low|Medium|High",
    "token_overhead": "Description of token usage",
    "compatibility": {
      "claude": "Yes|Partial|No",
      "grok": "Yes|Partial|No",
      "gpt": "Yes|Partial|No"
    },
    "sources": [
      {
        "title": "Source title",
        "url": "source url",
        "priority": 1-5,
        "accessed": "ISO-8601 date"
      }
    ]
  }
}
```

### Phase 4: GDrive Link Processing

When GDrive links provided:

1. **Extract document content**
   - Download/access document
   - Parse text content
   - Extract framework mentions

2. **Process multiple links**
   - Handle up to 5 GDrive links
   - Aggregate content
   - Cross-reference with web research

3. **Document processing output:**
```json
{
  "gdrive_content": {
    "link_1": {
      "title": "Document title",
      "frameworks_mentioned": ["framework 1", "framework 2"],
      "key_insights": ["insight 1", "insight 2"],
      "relevant_excerpts": ["excerpt 1", "excerpt 2"]
    }
  }
}
```

## Framework Encyclopedia Reference

Consult `references/prompt-frameworks-encyclopedia.md` for pre-existing knowledge on:

- Chain-of-Thought (CoT)
- ReAct
- xAI Prompting
- Prompt Chaining
- Few-Shot Prompting
- Self-Consistency
- Tree of Thoughts
- Chain-of-Verification
- Skeleton-of-Thought
- Claude Skills & Project Frameworks

## Research Output Schema

Update `workflow_state.json` with:

```json
{
  "research_artifacts": {
    "sources": [
      {
        "id": "src_001",
        "type": "official_docs|academic|guide|blog|community",
        "title": "Source title",
        "url": "source url",
        "framework": "framework name",
        "priority": 1-5,
        "accessed": "ISO-8601",
        "key_findings": ["finding 1", "finding 2"]
      }
    ],
    "framework_data": {
      "framework_1": { /* framework schema */ },
      "framework_2": { /* framework schema */ }
    },
    "gdrive_content": {
      /* processed gdrive content */
    },
    "research_metadata": {
      "total_sources": 0,
      "sources_per_framework": {},
      "research_duration_seconds": 0,
      "confidence_score": 0.0
    }
  }
}
```

## Quality Standards

### Minimum Research Requirements

| Requirement | Threshold |
|-------------|-----------|
| Sources per framework | Minimum 3 |
| Priority 1-2 sources | At least 1 per framework |
| GDrive links processed | All valid links |
| Framework data complete | All required fields |

### Confidence Scoring

Calculate research confidence:

```
confidence_score = (
  (priority_1_sources * 1.0) +
  (priority_2_sources * 0.8) +
  (priority_3_sources * 0.6) +
  (priority_4_sources * 0.4) +
  (priority_5_sources * 0.2)
) / total_sources
```

Target: confidence_score >= 0.7

## Citation Preparation

Prepare citations in APA format for each source:

```
Author, A. A. (Year). Title of work. Source.
URL: [link] Accessed: [date]
```

Store in `research_artifacts.sources` for later use by report-generator.

## Error Handling

| Error | Code | Recovery |
|-------|------|----------|
| Source unavailable | E002 | Use alternative sources, log warning |
| GDrive link invalid | E003 | Skip and continue, notify in output |
| Insufficient sources | E004 | Expand search, lower priority threshold |

## Quality Checklist

- [ ] All frameworks researched
- [ ] Minimum 3 sources per framework
- [ ] PromptingGuide.ai searched
- [ ] Anthropic docs searched
- [ ] Academic papers searched
- [ ] GDrive links processed
- [ ] Framework data complete
- [ ] Citations prepared
- [ ] workflow_state.json updated
- [ ] Confidence score >= 0.7

## Example Execution

**Input:**
- Frameworks: ["Chain-of-Thought", "ReAct"]
- GDrive links: ["https://drive.google.com/file/d/xxx", "https://drive.google.com/file/d/yyy"]

**Process:**
1. Search PromptingGuide.ai for CoT and ReAct
2. Search Anthropic docs for CoT and ReAct
3. Search arXiv for CoT and ReAct papers
4. Process GDrive link 1
5. Process GDrive link 2
6. Compile framework data
7. Calculate confidence score
8. Update workflow_state.json

**Output:**
```json
{
  "research_artifacts": {
    "sources": [ /* 6-10 sources */ ],
    "framework_data": {
      "chain-of-thought": { /* complete schema */ },
      "react": { /* complete schema */ }
    },
    "gdrive_content": { /* processed content */ },
    "research_metadata": {
      "total_sources": 8,
      "confidence_score": 0.82
    }
  }
}
```

---

*Part of Prompt Research Orchestrator Framework*