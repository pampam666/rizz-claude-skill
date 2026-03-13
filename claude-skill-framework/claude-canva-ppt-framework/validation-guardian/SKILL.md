---
name: validation-guardian
description: AUTO-TRIGGERS when any workflow phase completes and quality validation is needed. Keywords include validate, quality check, verify output, review quality. Phrases include validate the output, check quality, verify completion. Context is quality gatekeeper that runs after each skill completion in the framework. DOES NOT trigger for skill execution, content creation, or non-validation tasks.
---

# Validation Guardian

Validates outputs at each pipeline stage, ensuring quality thresholds are met before proceeding to the next skill.

## Mission

Serve as the quality gatekeeper for the claude-canva-ppt-framework by performing comprehensive validation checks at every stage transition, ensuring all outputs meet defined quality standards before allowing workflow progression.

## Input Protocol

### Required Input
- `workflow_state.json` with current phase status
- Output file from the skill that just completed
- Phase identifier (analysis, slide_engineering, canva_automation)

### Optional Input
- `quality_threshold` - Minimum acceptable score (default: 0.80)
- `strict_mode` - Enable additional validation checks (default: false)
- `skip_warnings` - Treat warnings as passed (default: false)

## Workflow

### Phase 1: Input Validation

```
VALIDATE INPUT:
├── Verify workflow state exists
├── Confirm phase is complete
├── Check output file exists
├── Validate file is readable
└── Parse JSON structure
```

### Phase 2: Phase-Specific Checks

```
RUN CHECKS BY PHASE:
│
├── [ANALYSIS PHASE]
│   ├── Document sections extracted
│   ├── Key points captured
│   ├── Slide mapping generated
│   ├── Confidence score >= 0.80
│   └── No placeholder content
│
├── [SLIDE ENGINEERING PHASE]
│   ├── All slides have titles
│   ├── Bullet counts within limits
│   ├── Speaker notes present
│   ├── Visual specs defined
│   └── Conclusion slide exists
│
└── [CANVA AUTOMATION PHASE]
    ├── Creation steps complete
    ├── Layouts mapped correctly
    ├── Colors validated (hex format)
    ├── Export settings configured
    └── Instructions are clear
```

### Phase 3: General Quality Checks

```
QUALITY VALIDATION:
├── No placeholder text ({{...}})
├── No TODO/FIXME comments
├── JSON structure valid
├── Required fields present
├── Data types correct
└── Values within expected ranges
```

### Phase 4: Score Calculation

```
CALCULATE SCORE:
├── Count passed checks
├── Count failed checks
├── Count warnings
├── Apply weights if configured
├── Calculate overall score
└── Determine pass/fail status
```

### Phase 5: Report Generation

```
GENERATE REPORT:
├── List all checks performed
├── Detail failures with reasons
├── Provide recommendations
├── Set proceed/block status
└── Update workflow state
```

## Output Format

### Validation Report Schema

```json
{
  "validation_report": {
    "validation_id": "val-2024-01-15-001",
    "workflow_id": "ppt-2024-01-15-001",
    "phase_validated": "analysis|slide_engineering|canva_automation",
    "validated_at": "ISO-8601-timestamp",
    
    "overall_status": "pass|fail|warning",
    "overall_score": 0.92,
    "threshold": 0.80,
    "proceed_to_next_phase": true,
    
    "summary": {
      "total_checks": 15,
      "passed": 13,
      "failed": 0,
      "warnings": 2,
      "skipped": 0
    },
    
    "checks": [
      {
        "category": "structure",
        "check_id": "STR_001",
        "check_name": "Output file exists",
        "status": "pass",
        "message": "File found: analysis_output.json",
        "severity": "critical"
      },
      {
        "category": "content",
        "check_id": "CON_001",
        "check_name": "No placeholder text",
        "status": "pass",
        "message": "No {{...}} patterns found",
        "severity": "critical"
      },
      {
        "category": "quality",
        "check_id": "QUA_001",
        "check_name": "Confidence score threshold",
        "status": "pass",
        "message": "Score 0.92 exceeds threshold 0.80",
        "severity": "critical"
      },
      {
        "category": "completeness",
        "check_id": "COM_001",
        "check_name": "All sections extracted",
        "status": "pass",
        "message": "5 sections extracted",
        "severity": "warning"
      },
      {
        "category": "completeness",
        "check_id": "COM_002",
        "check_name": "Visual recommendations provided",
        "status": "warning",
        "message": "Limited visual suggestions, consider adding more",
        "severity": "warning"
      }
    ],
    
    "failures": [],
    
    "warnings": [
      {
        "check_id": "COM_002",
        "message": "Limited visual suggestions",
        "recommendation": "Consider adding more chart and image recommendations"
      }
    ],
    
    "recommendations": [
      "Add more specific visual recommendations for slides 3-5",
      "Consider including icon suggestions for bullet points"
    ]
  }
}
```

## Validation Check Catalog

### Critical Checks (Must Pass)

| Check ID | Category | Check Name | Phase |
|----------|----------|------------|-------|
| STR_001 | structure | Output file exists | All |
| STR_002 | structure | Valid JSON format | All |
| STR_003 | structure | Required fields present | All |
| CON_001 | content | No placeholder text | All |
| CON_002 | content | No TODO/FIXME | All |
| QUA_001 | quality | Confidence score >= threshold | Analysis |
| QUA_002 | quality | All slides have titles | Slide Engineering |
| QUA_003 | quality | Creation steps complete | Canva Automation |

### Warning Checks (Should Pass)

| Check ID | Category | Check Name | Phase |
|----------|----------|------------|-------|
| COM_001 | completeness | Visual recommendations | Analysis |
| COM_002 | completeness | Speaker notes present | Slide Engineering |
| COM_003 | completeness | Chart configurations | Canva Automation |
| BST_001 | best_practice | Bullet count <= 6 | Slide Engineering |
| BST_002 | best_practice | Title length optimal | Slide Engineering |
| BST_003 | best_practice | Color format valid | Canva Automation |

## Phase-Specific Validation

### Analysis Phase Validation

```json
{
  "phase": "analysis",
  "required_checks": [
    "document_overview present",
    "content_structure.sections not empty",
    "slide_mapping.slides not empty",
    "confidence_score >= 0.80",
    "No {{placeholder}} text"
  ],
  "warning_checks": [
    "visual_recommendations present",
    "extraction_notes.content_gaps addressed",
    "At least 3 sections extracted"
  ]
}
```

### Slide Engineering Phase Validation

```json
{
  "phase": "slide_engineering",
  "required_checks": [
    "slide_deck.slides not empty",
    "Each slide has title",
    "Each slide has slide_type",
    "Title slide exists",
    "Conclusion slide exists"
  ],
  "warning_checks": [
    "Each slide has speaker_notes",
    "Bullet count <= 6 per slide",
    "Brand config applied",
    "Visual specs provided"
  ]
}
```

### Canva Automation Phase Validation

```json
{
  "phase": "canva_automation",
  "required_checks": [
    "canva_implementation present",
    "Each slide has creation_steps",
    "Colors in valid hex format",
    "Export config defined"
  ],
  "warning_checks": [
    "Canva layouts mapped",
    "Typography specs complete",
    "Share settings defined"
  ]
}
```

## Error Handling

| Error Code | Description | Recovery Action |
|------------|-------------|-----------------|
| VAL_001 | Output file not found | Request skill re-execution |
| VAL_002 | JSON parse error | Request output regeneration |
| VAL_003 | Critical check failed | Block progression, request fix |
| VAL_004 | Score below threshold | Review and improve output |
| VAL_005 | Missing required field | Request field completion |

### Failure Response Protocol

```
ON CRITICAL FAILURE:
├── Set status to "fail"
├── Block workflow progression
├── Generate detailed failure report
├── Provide specific remediation steps
├── Offer retry option
└── Update workflow_state.json
```

## Dependencies

- `workflow_state.json` (read/write)
- Access to skill output files
- JSON parsing capability

## Quality Checklist

- [ ] All critical checks performed
- [ ] All warning checks performed
- [ ] Score calculated correctly
- [ ] Report generated
- [ ] Proceed/block decision made
- [ ] workflow_state.json updated
- [ ] Recommendations provided
- [ ] Failures documented with remediation

## Integration Points

### With framework-orchestrator
- Receives validation requests
- Returns pass/fail status
- Provides detailed reports

### With All Skills
- Validates document-analyzer output
- Validates ppt-slide-engineer output
- Validates canva-ppt-automator output

## State Update Protocol

Upon validation completion:

```json
{
  "validation_guardian": {
    "last_validation": "ISO-8601-timestamp",
    "phase_validated": "analysis",
    "status": "pass|fail",
    "score": 0.92,
    "proceed": true,
    "report_path": "outputs/validation_report_analysis.json"
  }
}
```

---

*Part of Claude Canva PPT Framework - Quality Gatekeeper*