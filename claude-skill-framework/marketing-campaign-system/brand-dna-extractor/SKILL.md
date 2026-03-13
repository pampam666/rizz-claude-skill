---
name: brand-dna-extractor
description: AUTO-TRIGGERS when user provides ANY company URL for marketing analysis. Keywords include brand dna, brand voice, brand identity, tone analysis, company positioning. Phrases include analyze this website, extract brand from, understand this company brand. Context is first phase of ANY marketing campaign workflow after initialization. DOES NOT trigger for general web scraping, competitor analysis (use market-research-agent), or non-brand tasks.
---

# Brand DNA Extractor

Extracts comprehensive brand identity, voice, tone, and positioning from any company website URL.

## Mission

Transform a company website URL into a comprehensive Brand DNA profile that captures brand voice, tone characteristics, positioning, target audience signals, and competitive differentiators.

## Input Protocol

### Required Input
- `workflow_state.json` with `company_url` populated
- `current_phase` must be "brand_extraction" or "initialization"

## Extraction Process

### Step 1: Multi-Page Deep Fetch

| Page Type | URL Variations | What to Extract |
|-----------|---------------|-----------------|
| Homepage | `/`, `/home` | Hero messaging, value propositions |
| About | `/about`, `/about-us` | Brand story, mission, vision, values |
| Products | `/products`, `/services` | Offerings, categories, pricing |
| Blog | `/blog`, `/resources` | Content topics, writing samples |

### Step 2: Tone Pattern Recognition

```
ANALYZE:
├── Sentence length and complexity
├── Formality indicators
├── Emotional temperature
├── Voice characteristics
└── Keyword patterns
```

### Step 3: Positioning Analysis

```
EXTRACT:
├── Value proposition
├── Unique differentiators
├── Competitive advantages
└── Target audience signals
```

## Output Schema

```json
{
  "brand_dna": {
    "company_info": {
      "name": "Company Name",
      "tagline": "Company tagline",
      "industry": "Industry"
    },
    "voice_and_tone": {
      "primary_tone": "professional",
      "formality_level": 0.7,
      "do_keywords": [],
      "dont_keywords": []
    },
    "positioning": {
      "value_proposition": "",
      "unique_differentiators": [],
      "competitive_advantages": []
    },
    "target_audience": {
      "primary_audience": {},
      "pain_points": [],
      "goals": []
    }
  }
}
```

## Error Handling

| Code | Description | Recovery |
|------|-------------|----------|
| BRAND_001 | URL fetch failed | Try alternative URLs |
| BRAND_002 | Insufficient content | Request brand guidelines |
| BRAND_003 | Low confidence score | Request additional context |

## Dependencies

- Web fetch capability
- workflow_state.json (read/write)

## Quality Checklist

- [ ] At least 5 pages analyzed
- [ ] Primary tone identified
- [ ] Value proposition extracted
- [ ] Target audience defined
- [ ] Confidence score >= 0.7

---

*Part of Multi-Agent Marketing Campaign System*