# State Management Rules

Defines state handling rules for the Cline Skill Builder workflow system.

## Overview

State management ensures consistent tracking of workflow progress, enabling resumption, validation, and error recovery across multi-step operations.

## State File Location

State is maintained in:
```
cline-skill-builder/.clinerules/workflows/workflow_state.json
```

## State Schema

```json
{
  "schema_version": "1.0",
  "workflow_id": "unique-workflow-identifier",
  "blueprint_name": "skill-being-created",
  "current_phase": "PLAN|ACT|VALIDATION|COMPLETE",
  "status": "pending|in_progress|complete|error|cancelled",
  "created_files": [
    {
      "path": "relative/path/to/file",
      "status": "created|skipped|error",
      "timestamp": "ISO-8601-timestamp"
    }
  ],
  "validation_results": [
    {
      "check": "validation-check-name",
      "status": "pass|fail|warning",
      "message": "Details about the result"
    }
  ],
  "errors": [
    {
      "phase": "phase-where-error-occurred",
      "message": "Error description",
      "timestamp": "ISO-8601-timestamp",
      "recoverable": true|false
    }
  ],
  "metadata": {
    "created_at": "ISO-8601-timestamp",
    "updated_at": "ISO-8601-timestamp",
    "author": "user-or-system",
    "parent_workflow": "parent-workflow-id-if-any"
  }
}
```

## Phase States

### PLAN State
```json
{
  "current_phase": "PLAN",
  "status": "in_progress",
  "plan_details": {
    "summary": "Plan summary text",
    "directory_tree": "...",
    "file_list": [...],
    "user_confirmed": false
  }
}
```

### ACT State
```json
{
  "current_phase": "ACT",
  "status": "in_progress",
  "act_details": {
    "files_total": 10,
    "files_created": 5,
    "files_remaining": 5,
    "current_file": "path/to/current/file"
  }
}
```

### VALIDATION State
```json
{
  "current_phase": "VALIDATION",
  "status": "in_progress",
  "validation_details": {
    "checks_total": 7,
    "checks_passed": 5,
    "checks_failed": 0,
    "checks_warning": 2
  }
}
```

### COMPLETE State
```json
{
  "current_phase": "COMPLETE",
  "status": "complete",
  "completion_details": {
    "files_created": 10,
    "validation_passed": true,
    "output_location": "claude-skill-framework/skill-name/"
  }
}
```

## State Transitions

```
PENDING → PLAN → ACT → VALIDATION → COMPLETE
    ↓        ↓       ↓         ↓
    ← ← ← ERROR ← ← ← ←
              ↓
         CANCELLED
```

### Valid Transitions
| From | To | Trigger |
|------|-----|---------|
| PENDING | PLAN | Workflow initialized |
| PLAN | ACT | User confirms plan |
| PLAN | CANCELLED | User rejects plan |
| ACT | VALIDATION | All files created |
| ACT | ERROR | File creation fails |
| VALIDATION | COMPLETE | All checks pass |
| VALIDATION | ERROR | Critical check fails |
| ERROR | ACT | Retry requested |
| ERROR | CANCELLED | User cancels |

## State Operations

### Initialize State
```python
def initialize_state(blueprint_name: str) -> dict:
    return {
        "schema_version": "1.0",
        "workflow_id": generate_uuid(),
        "blueprint_name": blueprint_name,
        "current_phase": "PLAN",
        "status": "pending",
        "created_files": [],
        "validation_results": [],
        "errors": [],
        "metadata": {
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "author": "cline-skill-builder"
        }
    }
```

### Update State
```python
def update_state(state: dict, updates: dict) -> dict:
    state.update(updates)
    state["metadata"]["updated_at"] = datetime.now().isoformat()
    return state
```

### Record File Creation
```python
def record_file_creation(state: dict, file_path: str, status: str = "created") -> dict:
    state["created_files"].append({
        "path": file_path,
        "status": status,
        "timestamp": datetime.now().isoformat()
    })
    return update_state(state, {})
```

### Record Validation Result
```python
def record_validation(state: dict, check: str, status: str, message: str) -> dict:
    state["validation_results"].append({
        "check": check,
        "status": status,
        "message": message
    })
    return update_state(state, {})
```

### Record Error
```python
def record_error(state: dict, message: str, recoverable: bool = True) -> dict:
    state["errors"].append({
        "phase": state["current_phase"],
        "message": message,
        "timestamp": datetime.now().isoformat(),
        "recoverable": recoverable
    })
    state["status"] = "error"
    return update_state(state, {})
```

## Recovery Procedures

### Recoverable Errors
1. Load state from `workflow_state.json`
2. Identify last successful operation
3. Resume from that point
4. Continue workflow

### Non-Recoverable Errors
1. Load state from `workflow_state.json`
2. Identify all created files
3. Offer to rollback (delete created files)
4. Reset state to PENDING

### Manual Recovery
User can manually edit `workflow_state.json` to:
- Force a specific phase
- Mark files as created/skipped
- Clear errors

## Best Practices

1. **Always persist state** after each significant operation
2. **Validate state** before transitions
3. **Log state changes** for debugging
4. **Handle corruption** gracefully (reset to clean state)
5. **Never delete state** without user confirmation

## Integration

State management integrates with:
- `blueprint-execution.md` — Workflow orchestration
- `validation-rules.md` — Validation check definitions
- `skill-creator` sub-skill — File creation tracking

---

*Part of Cline Skill Builder Workflow System*