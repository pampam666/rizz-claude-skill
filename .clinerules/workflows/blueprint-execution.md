# Blueprint Execution Workflow

Master orchestration workflow for executing skill blueprints in Cline Skill Builder.

## Overview

This workflow defines the standard process for creating and executing skill blueprints. It enforces the **Plan → Confirm → Act** pattern to ensure quality and user control.

## Workflow Phases

### Phase 1: PLAN MODE

**Purpose**: Gather requirements and create a detailed plan.

**Steps**:
1. Receive user request for skill creation
2. Analyze requirements and constraints
3. Explore existing codebase if needed
4. Create comprehensive plan including:
   - One-paragraph summary
   - Complete directory tree
   - File list with purposes
   - Validation checklist
   - Warnings (if any)
5. Present plan to user
6. Wait for explicit confirmation

**Output Format**:
```
**CLINE.BOT [PHASE NAME] — PLAN MODE**
[complete detailed plan + tree + file list + validation checklist]

Do you confirm this plan? Reply **YES** to proceed with creation or provide modifications.
```

**Exit Criteria**: User replies with "YES", "confirm", "proceed", "go ahead", "execute", or equivalent.

---

### Phase 2: ACT MODE

**Purpose**: Execute the confirmed plan.

**Steps**:
1. Switch to ACT MODE (user must toggle)
2. Create directory structure
3. Generate all files with complete content
4. Validate created files against plan
5. Provide completion summary

**Output Requirements**:
- Full directory tree of created structure
- Content of every critical file
- Installation/activation instructions
- Status confirmation

**Exit Criteria**: All files created and validated successfully.

---

### Phase 3: VALIDATION

**Purpose**: Ensure quality and compliance.

**Validation Checklist**:
- [ ] YAML frontmatter valid and complete
- [ ] `name` field present and uses kebab-case
- [ ] `description` field present and precise
- [ ] Directory names use kebab-case
- [ ] All planned files created
- [ ] No placeholder text remaining
- [ ] Professional English throughout

---

## State Management

Workflow state is tracked in `workflow_state.json`:

```json
{
  "current_phase": "PLAN|ACT|VALIDATION|COMPLETE",
  "blueprint_name": "skill-name",
  "created_files": [],
  "validation_results": [],
  "status": "pending|in_progress|complete|error"
}
```

See `state-management.md` for detailed state handling rules.

---

## Output Location Rules

### Foundation Files
Foundation infrastructure is placed in:
```
cline-skill-builder/
```

### Generated Skills
All blueprint-generated skills are placed in:
```
claude-skill-framework/
└── [skill-name]/
```

**Never** output generated skills directly to workspace root.

---

## Error Handling

### Plan Phase Errors
- If requirements unclear, ask clarifying questions
- If conflicts detected, warn user before proceeding

### Act Phase Errors
- Report specific error immediately
- Do not leave partial files
- Offer to retry or modify plan

### Validation Errors
- List all validation failures
- Offer to fix automatically if possible
- Request user guidance if needed

---

## Communication Protocol

### Progress Updates
Provide clear progress indicators:
```
✓ Created: cline-skill-builder/SKILL.md
✓ Created: .agents/skills/skill-creator/SKILL.md
...
```

### Completion Message
```
**STATUS:** [Foundation/Blueprint] complete.
[Additional instructions or next steps]
```

---

## Integration Points

This workflow integrates with:
- `state-management.md` — State tracking rules
- `validation-rules.md` — Validation standards
- `skill-creator` sub-skill — Actual file generation

---

*Part of Cline Skill Builder Workflow System*