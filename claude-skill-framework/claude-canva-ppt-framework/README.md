# Claude Canva PPT Framework

> Transform any document into a professional Canva presentation in under 10 minutes.

## Quick Start

1. **Upload your document** (PDF, DOCX, TXT, or MD)
2. **Say**: "Convert this document to a Canva presentation"
3. **Follow the guided workflow** through all 5 skills
4. **Get your Canva implementation guide** in minutes!

## Skills Overview

| Skill | Purpose | Trigger |
|------|---------|--------|
| `document-analyzer` | Extract content from documents | Document upload |
| `ppt-slide-engineer` | Create slide structure | Analysis complete |
| `canva-ppt-automator` | Generate Canva instructions | Slides ready |
| `framework-orchestrator` | Coordinate entire workflow | Full workflow request |
| `validation-guardian` | Quality checks at each phase | Phase completion |

## Folder Structure

```
claude-canva-ppt-framework/
├── README.md                          ← You file
├── CLINE-PPT-CANVA-FRAMEWORK.md  ← Full documentation
├── workflow_state.json              ← Workflow state
│
├── document-analyzer/
│   ├── SKILL.md
│   ├── templates/document-analysis-schema.json
│   └── references/content-extraction-patterns.md
│
├── ppt-slide-engineer/
│   ├── SKILL.md
│   ├── templates/slide-structure-template.json
│   └── references/slide-design-principles.md
│
├── canva-ppt-automator/
│   ├── SKILL.md
│   ├── scripts/canva-automation-helper.js
│   └── templates/canva-brand-config.json
│
├── framework-orchestrator/
│   ├── SKILL.md
│   └── scripts/workflow-coordinator.py
│
├── validation-guardian/
│   ├── SKILL.md
│   └── scripts/validate-output.py
│
└── Validations/
    └── framework-validation-report.md
```

## How to Use

### Full Workflow
```
"Convert this document [filename.pdf] to a Canva presentation"
```

### Individual Skills
```
"Analyze this document for slide creation"
"Create slide structure from this analysis"
"Generate Canva instructions for these slides"
"Validate the output quality"
```

## Documentation

- **Full Guide**: See `CLINE-PPT-CANVA-FRAMEWORK.md` for comprehensive documentation
- **Validation Report**: See `Validations/framework-validation-report.md`

## Status

✅ **Framework Complete** - All 5 skills validated and ready for use.