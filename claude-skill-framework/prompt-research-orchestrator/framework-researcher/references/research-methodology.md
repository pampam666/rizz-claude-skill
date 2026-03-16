# Research Methodology

> Scientific method guide for conducting prompt engineering research

---

## Table of Contents

1. [Research Philosophy](#research-philosophy)
2. [Source Evaluation Framework](#source-evaluation-framework)
3. [Data Collection Protocol](#data-collection-protocol)
4. [Quality Assurance Standards](#quality-assurance-standards)
5. [Citation Requirements](#citation-requirements)

---

## Research Philosophy

### Core Principles

1. **Rigor over Speed**: Prioritize accuracy and completeness
2. **Multi-Source Verification**: Cross-reference claims across sources
3. **Transparency**: Document all sources and methodology
4. **Reproducibility**: Enable others to replicate findings

### Scientific Approach

```
Hypothesis → Literature Review → Data Collection → Analysis → Synthesis → Conclusion
```

### Research Questions Template

When researching frameworks, answer:

1. What is the core mechanism?
2. How does it affect LLM thinking process?
3. What are the implementation requirements?
4. What does the evidence say about effectiveness?
5. What are the limitations and trade-offs?

---

## Source Evaluation Framework

### Source Hierarchy

| Tier | Source Type | Weight | Examples |
|------|-------------|--------|----------|
| **1** | Official Documentation | 1.0 | Anthropic docs, OpenAI docs, xAI docs |
| **2** | Peer-Reviewed Papers | 0.9 | arXiv (cs.CL, cs.AI), ACL, NeurIPS |
| **3** | Authoritative Guides | 0.8 | PromptingGuide.ai, Learn Prompting |
| **4** | Technical Blogs | 0.6 | Official company blogs, researcher blogs |
| **5** | Community Resources | 0.4 | GitHub, Stack Overflow, forums |

### Source Quality Checklist

- [ ] Author credentials verified
- [ ] Publication date within 2 years (for fast-moving field)
- [ ] Claims supported by evidence
- [ ] Methodology clearly described
- [ ] Reproducible results

### Red Flags (Avoid or Downgrade)

- No author attribution
- No citations or references
- Claims without evidence
- Outdated information (>2 years for LLM topics)
- Promotional content

---

## Data Collection Protocol

### Phase 1: Primary Source Search

**PromptingGuide.ai Search:**
```
1. Navigate to promptingguide.ai
2. Search for framework name
3. Extract: description, examples, references
4. Note: related frameworks mentioned
```

**Anthropic Documentation Search:**
```
1. Navigate to docs.anthropic.com
2. Search for framework/technique
3. Extract: best practices, examples, limitations
4. Note: Claude-specific guidance
```

**Academic Search:**
```
1. Search arXiv cs.CL and cs.AI
2. Use query: "[framework name] prompting" OR "[framework name] language model"
3. Extract: methodology, benchmarks, conclusions
4. Note: citation count, publication venue
```

### Phase 2: Framework Data Extraction

For each framework, collect:

```json
{
  "framework_name": {
    "primary_source": {
      "title": "",
      "url": "",
      "authors": [],
      "date": "",
      "tier": 1-5
    },
    "description": "2-3 sentence overview",
    "core_mechanism": "Technical explanation",
    "invented_by": "Authors/organization",
    "year_introduced": 2022,
    "key_paper": {
      "title": "",
      "url": "",
      "citation": "APA format"
    },
    "evidence_quality": "strong|moderate|weak",
    "benchmark_results": [
      {
        "task": "task name",
        "metric": "accuracy/f1/etc",
        "result": "value",
        "baseline": "value",
        "improvement": "+X%"
      }
    ],
    "implementation": {
      "complexity": "low|medium|high",
      "requirements": ["req1", "req2"],
      "example_prompt": "Example prompt text"
    },
    "compatibility": {
      "claude": "yes|partial|no",
      "gpt": "yes|partial|no",
      "grok": "yes|partial|no"
    },
    "limitations": ["limitation1", "limitation2"],
    "best_for": ["use case1", "use case2"],
    "avoid_for": ["use case1", "use case2"]
  }
}
```

### Phase 3: Cross-Reference Verification

For key claims, verify across sources:

```
Claim: "CoT improves math reasoning by X%"
Sources needed: Minimum 2
- Source 1: Original paper
- Source 2: Independent replication
Status: Verified | Partially Verified | Unverified
```

---

## Quality Assurance Standards

### Minimum Research Requirements

| Requirement | Threshold |
|-------------|-----------|
| Sources per framework | Minimum 3 |
| Tier 1-2 sources | At least 1 per framework |
| Cross-referenced claims | All major claims |
| Recent sources | 80% within 2 years |
| Confidence score | ≥ 0.7 |

### Confidence Scoring Formula

```
confidence_score = (
  (tier_1_count * 1.0) +
  (tier_2_count * 0.9) +
  (tier_3_count * 0.8) +
  (tier_4_count * 0.6) +
  (tier_5_count * 0.4)
) / total_sources * cross_reference_factor

where cross_reference_factor = 1.0 if claims verified, 0.8 if partially verified, 0.6 if unverified
```

### Research Completeness Checklist

- [ ] All frameworks have minimum 3 sources
- [ ] At least 1 Tier 1-2 source per framework
- [ ] All claims cross-referenced
- [ ] Benchmark data extracted (if available)
- [ ] Limitations documented
- [ ] Compatibility assessed
- [ ] Implementation complexity evaluated

---

## Citation Requirements

### APA Format (Required)

**Journal Article:**
```
Author, A. A., & Author, B. B. (Year). Title of article. Journal Name, Volume(Issue), pages. DOI or URL
```

**arXiv Preprint:**
```
Author, A. A., Author, B. B., & Author, C. C. (Year). Title of paper. arXiv preprint arXiv:XXXX.XXXXX.
URL: https://arxiv.org/abs/XXXX.XXXXX
```

**Online Documentation:**
```
Organization. (Year, Month Day). Title of page. Site Name.
URL: [full URL] Accessed: [date]
```

**Example Citations:**

```
Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., & Zhou, D. (2022). Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. arXiv preprint arXiv:2201.11903.
URL: https://arxiv.org/abs/2201.11903 Accessed: 2024-01-15

Anthropic. (2024). Prompt Engineering Guide. Anthropic Documentation.
URL: https://docs.anthropic.com/claude/docs/prompt-engineering Accessed: 2024-01-15
```

### In-Text Citation Format

Use author-date format:
- Single author: (Author, Year)
- Two authors: (Author & Author, Year)
- Three+ authors: (Author et al., Year)

### Citation Quality Standards

| Element | Requirement |
|---------|-------------|
| Authors | All authors listed (use et al. for 4+) |
| Year | Publication year required |
| Title | Full title, sentence case |
| Source | Journal name or repository |
| URL | Direct link to source |
| Access Date | Required for online sources |

---

## GDrive Document Processing

### Processing Protocol

1. **Access Document**
   - Follow GDrive link
   - Verify access permissions
   - Note document title and author

2. **Extract Content**
   - Identify framework mentions
   - Extract relevant sections
   - Note any proprietary information

3. **Process Multiple Links**
   - Handle up to 5 GDrive links
   - Aggregate findings
   - Cross-reference with web research

4. **Document Output**
```json
{
  "gdrive_source": {
    "title": "Document Title",
    "link": "https://drive.google.com/...",
    "author": "Author Name (if available)",
    "frameworks_mentioned": ["CoT", "ReAct"],
    "key_insights": [
      "Insight 1 from document",
      "Insight 2 from document"
    ],
    "relevant_excerpts": [
      "Direct quote 1",
      "Direct quote 2"
    ],
    "credibility_notes": "Internal document / Published / Unknown"
  }
}
```

---

## Error Handling

### Common Research Issues

| Issue | Code | Resolution |
|-------|------|------------|
| Source paywalled | R001 | Use abstract, cite as "abstract only" |
| Conflicting information | R002 | Document conflict, use higher-tier source |
| Outdated source | R003 | Note date, seek newer source |
| Non-reproducible claims | R004 | Mark as "unverified", seek corroboration |
| GDrive access denied | R005 | Log error, request alternative |

### Research Recovery Protocol

```
1. Log error with code
2. Attempt alternative source
3. Document limitation in output
4. Adjust confidence score accordingly
```

---

## Research Output Template

Final research output structure:

```json
{
  "research_artifacts": {
    "sources": [/* all sources with metadata */],
    "framework_data": {/* extracted framework data */},
    "gdrive_content": {/* processed GDrive content */},
    "research_metadata": {
      "total_sources": 8,
      "sources_per_framework": {"CoT": 4, "ReAct": 4},
      "tier_distribution": {"tier_1": 2, "tier_2": 3, "tier_3": 2, "tier_4": 1},
      "research_duration_seconds": 120,
      "confidence_score": 0.82,
      "verification_status": "all_major_claims_verified"
    }
  }
}
```

---

*Part of Prompt Research Orchestrator Framework*