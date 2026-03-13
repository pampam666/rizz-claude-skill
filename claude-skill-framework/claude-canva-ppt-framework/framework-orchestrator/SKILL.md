---
name: framework-orchestrator
description: AUTO-TRIGGERS when user requests complete document-to-ppt conversion or mentions the full workflow. Keywords include full workflow, complete conversion, end to end, orchestrate, coordinate. Phrases include convert entire document to canva, run full ppt workflow, start complete conversion. Context is master controller for the entire claude-canva-ppt-framework. DOES NOT trigger for individual skill execution, partial workflows, or non-framework tasks.
---

# Framework Orchestrator

Master controller that orchestrates the complete document-to-Canva-PPT pipeline, managing skill handoffs, state transitions, and workflow progress.

## Mission

Coordinate all five skills in the claude-canva-ppt-framework to deliver seamless document-to-presentation conversion in under 10 minutes, ensuring proper sequencing, state management, and quality gates throughout the workflow.

## Input Protocol

### Required Input
- Document file (PDF, DOCX, TXT, or MD)
- User confirmation to proceed with full workflow

### Optional Input
- `target_slide_count` - Desired number of slides
- `brand_guidelines` - Brand configuration
- `presentation_style` - Corporate, creative, minimal
- `canva_template_id` - Specific Canva template
- `export_format` - PDF, PPTX, or link

## Workflow

### Phase 1: Workflow Initialization

```
INITIALIZE:
├── Create workflow_state.json
├── Set workflow_id (unique identifier)
├── Record input parameters
├── Set current_phase to "initialization"
├── Validate document format
└── Estimate total processing time
```

### Phase 2: Pipeline Execution

```
EXECUTE PIPELINE:
│
├── [STEP 1] Document Analysis
│   ├── Trigger document-analyzer
│   ├── Monitor completion
│   ├── Validate output
│   └── Proceed on success
│
├── [STEP 2] Quality Gate 1
│   ├── Trigger validation-guardian
│   ├── Check analysis quality
│   └── Proceed if score >= 0.80
│
├── [STEP 3] Slide Engineering
│   ├── Trigger ppt-slide-engineer
│   ├── Monitor completion
│   ├── Validate output
│   └── Proceed on success
│
├── [STEP 4] Quality Gate 2
│   ├── Trigger validation-guardian
│   ├── Check slide structure
│   └── Proceed if validated
│
├── [STEP 5] Canva Automation
│   ├── Trigger canva-ppt-automator
│   ├── Monitor completion
│   ├── Validate output
│   └── Proceed on success
│
└── [STEP 6] Final Quality Gate
    ├── Trigger validation-guardian
    ├── Complete validation
    └── Mark workflow complete
```

### Phase 3: State Management

```
MANAGE STATE:
├── Track current phase
├── Record skill completion status
├── Store output paths
├── Log errors and warnings
├── Update timestamps
└── Maintain rollback capability
```

### Phase 4: Error Recovery

```
ON ERROR:
├── Identify failed skill
├── Log error details
├── Attempt automatic recovery
├── Request user input if needed
├── Option to retry or rollback
└── Update state accordingly
```

### Phase 5: Completion

```
COMPLETE:
├── Generate final report
├── Compile all outputs
├── Provide download links
├── Archive workflow state
└── Request user feedback
```

## Output Format

### Workflow State Schema

```json
{
  "schema_version": "1.0",
  "workflow_id": "ppt-2024-01-15-001",
  "framework_name": "claude-canva-ppt-framework",
  "current_phase": "initialization|analysis|slide_engineering|canva_automation|complete|error",
  "status": "pending|in_progress|complete|error|cancelled",
  "started_at": "ISO-8601-timestamp",
  "updated_at": "ISO-8601-timestamp",
  "completed_at": "ISO-8601-timestamp or null",
  
  "input_parameters": {
    "source_document": "filename.pdf",
    "target_slide_count": 12,
    "presentation_style": "corporate",
    "brand_guidelines": {},
    "export_format": ["pdf", "pptx"]
  },
  
  "pipeline_progress": {
    "document_analyzer": {
      "status": "pending|in_progress|complete|error",
      "started_at": "ISO-8601-timestamp",
      "completed_at": "ISO-8601-timestamp",
      "output_path": "outputs/analysis_output.json",
      "confidence_score": 0.92
    },
    "ppt_slide_engineer": {
      "status": "pending|in_progress|complete|error",
      "started_at": "ISO-8601-timestamp",
      "completed_at": "ISO-8601-timestamp",
      "output_path": "outputs/slide_structure.json",
      "total_slides": 12
    },
    "canva_ppt_automator": {
      "status": "pending|in_progress|complete|error",
      "started_at": "ISO-8601-timestamp",
      "completed_at": "ISO-8601-timestamp",
      "output_path": "outputs/canva_implementation.json",
      "export_ready": true
    },
    "validation_guardian": {
      "checks_performed": 3,
      "all_passed": true,
      "details": []
    }
  },
  
  "outputs": {
    "analysis_output": "outputs/analysis_output.json",
    "slide_structure": "outputs/slide_structure.json",
    "canva_implementation": "outputs/canva_implementation.json",
    "final_presentation": "outputs/presentation_final.pdf"
  },
  
  "errors": [],
  
  "metadata": {
    "total_processing_time_seconds": 420,
    "document_word_count": 2500,
    "slides_generated": 12,
    "quality_score": 0.91
  }
}
```

### Final Report Format

```json
{
  "report": {
    "workflow_id": "ppt-2024-01-15-001",
    "status": "complete",
    "summary": {
      "source_document": "Quarterly Report Q4 2024.pdf",
      "slides_created": 12,
      "processing_time": "7 minutes",
      "quality_score": 0.91
    },
    "deliverables": {
      "analysis": {
        "path": "outputs/analysis_output.json",
        "key_findings": ["Finding 1", "Finding 2"]
      },
      "slide_structure": {
        "path": "outputs/slide_structure.json",
        "slide_types": ["title", "agenda", "content", "data", "conclusion"]
      },
      "canva_instructions": {
        "path": "outputs/canva_implementation.json",
        "ready_for_implementation": true
      }
    },
    "next_steps": [
      "Open Canva and create new presentation",
      "Follow step-by-step instructions in canva_implementation.json",
      "Apply brand kit if available",
      "Export in desired format"
    ],
    "quality_metrics": {
      "content_extraction": 0.95,
      "slide_structure": 0.90,
      "canva_readiness": 0.88,
      "overall": 0.91
    }
  }
}
```

## Skill Coordination Matrix

| Phase | Active Skill | Validation | Next Skill |
|-------|--------------|------------|------------|
| 1 | document-analyzer | validation-guardian | ppt-slide-engineer |
| 2 | ppt-slide-engineer | validation-guardian | canva-ppt-automator |
| 3 | canva-ppt-automator | validation-guardian | COMPLETE |

## Timing Estimates

| Phase | Estimated Time | Cumulative |
|-------|---------------|------------|
| Initialization | 30 seconds | 0:30 |
| Document Analysis | 2 minutes | 2:30 |
| Slide Engineering | 2 minutes | 4:30 |
| Canva Automation | 2 minutes | 6:30 |
| Validation & Report | 1 minute | 7:30 |
| **Total** | **~7-8 minutes** | - |

## Error Handling

| Error Code | Description | Recovery Action |
|------------|-------------|-----------------|
| ORCH_001 | Document format invalid | Request supported format |
| ORCH_002 | Skill execution timeout | Retry with extended timeout |
| ORCH_003 | Validation failed | Return to failed skill |
| ORCH_004 | State corruption | Rebuild from last checkpoint |
| ORCH_005 | Dependency missing | Install or configure dependency |

### Recovery Procedures

```
RECOVERY FLOW:
├── Identify failure point
├── Preserve current state
├── Option 1: Retry current skill
├── Option 2: Rollback to previous
├── Option 3: Skip and continue
└── Option 4: Cancel workflow
```

## Dependencies

- All framework skills (document-analyzer, ppt-slide-engineer, canva-ppt-automator, validation-guardian)
- `workflow_state.json` (read/write)
- File system access for outputs

## Quality Checklist

- [ ] Workflow initialized with unique ID
- [ ] Document format validated
- [ ] All skills executed in sequence
- [ ] Validation gates passed
- [ ] State updated at each phase
- [ ] Errors handled gracefully
- [ ] Final report generated
- [ ] All outputs accessible
- [ ] Processing time under 10 minutes
- [ ] Quality score >= 0.80

## Usage Example

**User Request:**
> "Convert this quarterly report to a Canva presentation"

**Orchestrator Response:**
1. Initialize workflow
2. Execute document-analyzer → Analysis complete (92% confidence)
3. Run validation → PASS
4. Execute ppt-slide-engineer → 12 slides created
5. Run validation → PASS
6. Execute canva-ppt-automator → Instructions ready
7. Run validation → PASS
8. Generate final report

**Output:**
- Complete Canva implementation guide
- Step-by-step creation instructions
- All intermediate files for reference

---

*Part of Claude Canva PPT Framework - Master Orchestrator*