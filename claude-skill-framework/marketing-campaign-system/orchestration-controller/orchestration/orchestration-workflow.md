# Orchestration Workflow

Master workflow for the Multi-Agent Marketing Campaign System.

## Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MARKETING CAMPAIGN WORKFLOW                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  PHASE 1          PHASE 2          PHASE 3          PHASE 4                 │
│  ┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐               │
│  │  Brand  │────▶│ Market  │────▶│Strategy │────▶│Research │               │
│  │   DNA   │     │Research │     │ Agent   │     │ Writer  │               │
│  └─────────┘     └─────────┘     └─────────┘     └─────────┘               │
│       │               │               │               │                     │
│       ▼               ▼               ▼               ▼                     │
│  [CHECKPOINT]    [CHECKPOINT]    [CHECKPOINT]    [CHECKPOINT]              │
│                                                                              │
│  PHASE 5          PHASE 6          PHASE 7                                   │
│  ┌─────────┐     ┌─────────┐     ┌─────────┐                               │
│  │Campaign │────▶│ Article │────▶│   QA    │──▶ DELIVERY                   │
│  │ Planning│     │ Content │     │  Agent  │                               │
│  └─────────┘     └─────────┘     └─────────┘                               │
│       │               │               │                                     │
│       ▼               ▼               ▼                                     │
│  [CHECKPOINT]    [CHECKPOINT]    [CHECKPOINT]                              │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Phase Definitions

### Phase 1: Brand DNA Extraction
**Agent**: `brand-dna-extractor`
**Input**: Company URL, marketing materials
**Output**: `brand_dna` object in workflow_state.json
**Checkpoint**: `brand_dna_complete`

**Validation Criteria**:
- [ ] Company info populated
- [ ] Voice and tone defined
- [ ] At least 3 core values
- [ ] Value proposition present

---

### Phase 2: Market Research
**Agent**: `market-research-agent`
**Input**: `brand_dna`, industry, target market
**Output**: `research_artifacts` object
**Checkpoint**: `research_complete`

**Validation Criteria**:
- [ ] Market overview complete
- [ ] At least 3 competitors analyzed
- [ ] Industry trends identified
- [ ] Sources documented

---

### Phase 3: Strategy Development
**Agent**: `campaign-strategy-agent`
**Input**: `brand_dna`, `research_artifacts`
**Output**: `strategy_artifacts` object
**Checkpoint**: `strategy_complete`

**Validation Criteria**:
- [ ] Positioning strategy defined
- [ ] Channel strategy complete
- [ ] Content themes established
- [ ] KPIs set

---

### Phase 4: Research Document
**Agent**: `research-writer-visualizer`
**Input**: All previous artifacts
**Output**: `Market_Research_Document.docx`
**Checkpoint**: `research_document_complete`

**Validation Criteria**:
- [ ] 25-40 pages generated
- [ ] 5+ visualizations included
- [ ] All sections complete
- [ ] Brand tone applied

---

### Phase 5: Campaign Planning
**Agent**: `campaign-planning-agent`
**Input**: Strategy artifacts
**Output**: `Campaign_Master_Plan.xlsx`
**Checkpoint**: `campaign_plan_complete`

**Validation Criteria**:
- [ ] All 8 sheets generated
- [ ] Timeline complete
- [ ] Budget allocated
- [ ] Content calendar populated

---

### Phase 6: Article Content
**Agent**: `article-content-executor`
**Input**: Campaign plan, content themes
**Output**: 10+ article markdown files
**Checkpoint**: `articles_complete`

**Validation Criteria**:
- [ ] 10+ articles generated
- [ ] All frontmatter complete
- [ ] SEO optimized
- [ ] Brand voice consistent

---

### Phase 7: Quality Assurance
**Agent**: `quality-assurance-agent`
**Input**: All deliverables
**Output**: QA report
**Checkpoint**: `qa_passed`

**Validation Criteria**:
- [ ] Brand voice validated
- [ ] SEO checks passed
- [ ] Content quality verified
- [ ] All deliverables present

---

## Checkpoint System

### Checkpoint Validation

Each phase must pass checkpoint validation before proceeding:

```python
def validate_checkpoint(checkpoint_name: str, state: dict) -> bool:
    checkpoint = CHECKPOINTS[checkpoint_name]
    
    for criterion in checkpoint['criteria']:
        if not evaluate_criterion(criterion, state):
            return False
    
    return True
```

### Checkpoint States

| State | Description |
|-------|-------------|
| `pending` | Not yet reached |
| `in_progress` | Currently validating |
| `passed` | Validation successful |
| `failed` | Validation failed, retry needed |

---

## Error Recovery

### Error Codes

| Code | Phase | Recovery Action |
|------|-------|-----------------|
| E001 | Brand DNA | Request additional materials |
| E002 | Research | Expand search parameters |
| E003 | Strategy | Re-run with adjusted inputs |
| E004 | Document | Regenerate failed sections |
| E005 | Planning | Adjust timeline/budget |
| E006 | Content | Rewrite failed articles |
| E007 | QA | Fix identified issues |

### Retry Logic

```
MAX_RETRIES = 3
RETRY_DELAY = 60  # seconds

on_error:
1. Log error to workflow_state.errors
2. Increment retry_count
3. If retry_count < MAX_RETRIES:
   - Wait RETRY_DELAY
   - Retry current phase
4. Else:
   - Mark workflow as failed
   - Request human intervention
```

---

## State Transitions

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│              │     │              │     │              │
│ initialization│────▶│  brand_dna   │────▶│  research    │
│              │     │              │     │              │
└──────────────┘     └──────────────┘     └──────────────┘
                                                │
                                                ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│              │     │              │     │              │
│   complete   │◀────│     qa       │◀────│  articles    │
│              │     │              │     │              │
└──────────────┘     └──────────────┘     └──────────────┘
                            ▲
                            │
┌──────────────┐     ┌──────────────┐
│              │     │              │
│   strategy   │────▶│   document   │
│              │     │              │
└──────────────┘     └──────────────┘
                            │
                            ▼
                     ┌──────────────┐
                     │              │
                     │   planning   │
                     │              │
                     └──────────────┘
```

---

## Deliverables Summary

| Phase | Deliverable | Format | Location |
|-------|-------------|--------|----------|
| 1 | Brand DNA Profile | JSON | workflow_state.json |
| 2 | Research Artifacts | JSON | workflow_state.json |
| 3 | Strategy Document | JSON | workflow_state.json |
| 4 | Research Document | DOCX | /deliverables/ |
| 5 | Campaign Plan | XLSX | /deliverables/ |
| 6 | Articles | MD | /deliverables/articles/ |
| 7 | QA Report | JSON | workflow_state.json |

---

## Usage

### Starting a New Campaign

```bash
# Initialize workflow
python scripts/phase_validator.py init --company "Acme Corp" --url "https://acme.com"

# Run full workflow
python scripts/phase_validator.py run-all

# Run specific phase
python scripts/phase_validator.py run --phase brand_dna
```

### Checking Status

```bash
# Get current status
python scripts/phase_validator.py status

# Validate checkpoint
python scripts/phase_validator.py validate --checkpoint brand_dna_complete
```

### Recovery

```bash
# Retry current phase
python scripts/phase_validator.py retry

# Rollback to checkpoint
python scripts/phase_validator.py rollback --checkpoint strategy_complete
```

---

*Part of Multi-Agent Marketing Campaign System*