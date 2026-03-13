---
name: orchestration-controller
description: AUTO-TRIGGERS when multi-agent campaign workflow needs coordination. Keywords include orchestration, workflow control, agent coordination, phase management, workflow controller. Phrases include coordinate workflow, manage campaign phases, orchestrate agents, control workflow state. Context is central controller for entire marketing campaign system. DOES NOT trigger for individual agent tasks, research, or content creation.
---

# Orchestration Controller

Central coordination agent that manages workflow state, phase transitions, and agent handoffs across the marketing campaign system.

## Mission

Orchestrate the entire marketing campaign workflow by managing state, validating phase transitions, coordinating agent execution, and ensuring deliverable quality across all phases.

## Input Protocol

### Required Input
- `workflow_state.json` with:
  - `company_url` populated
  - `current_phase` set

## Workflow Phases

| Phase | Agent | Trigger Condition |
|-------|-------|-------------------|
| 1. Initialization | orchestration-controller | User provides company URL |
| 2. Brand Extraction | brand-dna-extractor | Phase 1 complete |
| 3. Market Research | market-research-agent | Phase 2 complete |
| 4. Strategy Development | campaign-strategy-agent | Phase 3 complete |
| 5. Campaign Planning | campaign-planning-agent | Phase 4 complete |
| 6. Research Writing | research-writer-visualizer | Phase 4 complete |
| 7. Article Execution | article-content-executor | Phase 5 complete |
| 8. Quality Assurance | quality-assurance-agent | Phase 7 complete |

## State Management

```json
{
  "workflow_state": {
    "company_url": "",
    "current_phase": "",
    "phases_completed": [],
    "brand_dna": {},
    "research_artifacts": {},
    "strategy_artifacts": {},
    "deliverables": {},
    "errors": []
  }
}
```

## Dependencies

- All campaign agents
- `scripts/phase_validator.py`
- workflow_state.json (read/write)

## Quality Checklist

- [ ] Workflow state initialized
- [ ] Phase transitions validated
- [ ] Agent handoffs coordinated
- [ ] Error handling active
- [ ] Progress tracked

---

*Part of Multi-Agent Marketing Campaign System*