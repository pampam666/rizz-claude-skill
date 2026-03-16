# Iteration Tracking

Defines how to track progress across evaluation iterations, replacing rigid phase-based state management.

## Overview

Instead of tracking phases (PLAN → ACT → VALIDATION → COMPLETE), we track iterations through the eval-refine loop. This reflects the actual workflow: multiple rounds of testing, feedback, and improvement.

---

## Tracking Philosophy

### From Phases to Iterations

**Old approach:** Linear phase transitions with complex state machine
```
PENDING → PLAN → ACT → VALIDATION → COMPLETE
                ↓
              ERROR → (retry or cancel)
```

**New approach:** Iteration-based tracking with flexible stages
```
iteration-1 → iteration-2 → iteration-3 → ... → done
     ↑              |
     └──────────────┘ (refine and repeat)
```

### What We Track

| Data | Purpose |
|------|---------|
| Current iteration | Which round of testing we're on |
| Current stage | What activity is happening now |
| Test cases | The evals being run |
| Benchmark results | Quantitative performance data |
| User feedback | Qualitative improvement guidance |
| Skill snapshots | Previous versions for comparison |

---

## State Schema

### Main State File

Location: `.clinerules/workflows/workflow_state.json`

```json
{
  "schema_version": "2.0",
  "skill_name": "skill-being-developed",
  "skill_path": "path/to/skill",
  "workspace_path": "path/to/skill-workspace",
  "current_iteration": 1,
  "current_stage": "intent|drafting|testing|reviewing|refining|optimizing|complete",
  "started_at": "ISO-8601-timestamp",
  "updated_at": "ISO-8601-timestamp",
  "iterations": [
    {
      "iteration_number": 1,
      "started_at": "ISO-8601-timestamp",
      "completed_at": "ISO-8601-timestamp",
      "evals": ["eval-0", "eval-1"],
      "benchmark_summary": {
        "with_skill_pass_rate": 0.75,
        "baseline_pass_rate": 0.50,
        "delta": 0.25
      },
      "user_feedback_status": "pending|incorporated|none",
      "status": "in_progress|complete|abandoned"
    }
  ],
  "test_cases": [
    {
      "id": 0,
      "name": "descriptive-eval-name",
      "prompt": "The test prompt",
      "has_assertions": true
    }
  ],
  "feedback_pending": false,
  "description_optimized": false
}
```

### Stage Definitions

| Stage | Description | Next |
|-------|-------------|------|
| `intent` | Capturing user requirements | `drafting` |
| `drafting` | Writing SKILL.md | `testing` |
| `testing` | Running parallel evaluations | `reviewing` |
| `reviewing` | User reviewing via eval-viewer | `refining` or `optimizing` |
| `refining` | Improving skill based on feedback | `testing` (new iteration) |
| `optimizing` | Optimizing description for triggering | `complete` |
| `complete` | Skill finished and packaged | — |

---

## Iteration Directory Structure

Each iteration creates a directory with full results:

```
skill-workspace/
├── iteration-1/
│   ├── eval-0/
│   │   ├── with_skill/
│   │   │   ├── outputs/
│   │   │   │   └── (generated files)
│   │   │   ├── grading.json
│   │   │   └── timing.json
│   │   ├── without_skill/
│   │   │   ├── outputs/
│   │   │   ├── grading.json
│   │   │   └── timing.json
│   │   └── eval_metadata.json
│   ├── eval-1/
│   │   └── ... (same structure)
│   ├── benchmark.json
│   └── benchmark.md
│
├── iteration-2/
│   └── ... (same structure)
│
├── skill-snapshot/
│   └── (copy of previous skill version for comparison)
│
└── feedback.json
```

---

## Supporting File Schemas

### eval_metadata.json

```json
{
  "eval_id": 0,
  "eval_name": "descriptive-name",
  "prompt": "The user's task prompt",
  "files": [],
  "assertions": [
    {
      "name": "assertion-name",
      "expected": "What should be true",
      "check_type": "contains|regex|exact|custom"
    }
  ]
}
```

### grading.json

```json
{
  "eval_id": 0,
  "run_type": "with_skill|without_skill|old_skill",
  "timestamp": "ISO-8601",
  "expectations": [
    {
      "text": "Assertion description",
      "passed": true,
      "evidence": "How it was verified"
    }
  ],
  "pass_count": 3,
  "fail_count": 0,
  "pass_rate": 1.0
}
```

### timing.json

```json
{
  "total_tokens": 84852,
  "duration_ms": 23332,
  "total_duration_seconds": 23.3
}
```

### benchmark.json

```json
{
  "skill_name": "example-skill",
  "iteration": 1,
  "timestamp": "ISO-8601",
  "configurations": [
    {
      "name": "with_skill",
      "pass_rate": 0.87,
      "pass_rate_std": 0.05,
      "mean_duration_ms": 23332,
      "mean_tokens": 84852
    },
    {
      "name": "without_skill",
      "pass_rate": 0.62,
      "pass_rate_std": 0.08,
      "mean_duration_ms": 28456,
      "mean_tokens": 92341
    }
  ],
  "delta": {
    "pass_rate_improvement": 0.25,
    "time_delta_ms": -5124,
    "token_delta": -7489
  },
  "per_eval_results": [...]
}
```

### feedback.json

```json
{
  "reviews": [
    {
      "run_id": "eval-0-with_skill",
      "feedback": "User's qualitative feedback",
      "timestamp": "ISO-8601"
    },
    {
      "run_id": "eval-1-with_skill",
      "feedback": "",
      "timestamp": "ISO-8601"
    }
  ],
  "status": "complete",
  "iteration": 1
}
```

---

## State Operations

### Initialize New Skill Development

```python
def initialize_skill_development(skill_name: str, skill_path: str) -> dict:
    return {
        "schema_version": "2.0",
        "skill_name": skill_name,
        "skill_path": skill_path,
        "workspace_path": f"{skill_path}-workspace",
        "current_iteration": 0,
        "current_stage": "intent",
        "started_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
        "iterations": [],
        "test_cases": [],
        "feedback_pending": False,
        "description_optimized": False
    }
```

### Start New Iteration

```python
def start_iteration(state: dict) -> dict:
    state["current_iteration"] += 1
    state["current_stage"] = "testing"
    state["iterations"].append({
        "iteration_number": state["current_iteration"],
        "started_at": datetime.now().isoformat(),
        "completed_at": None,
        "evals": [],
        "benchmark_summary": None,
        "user_feedback_status": "pending",
        "status": "in_progress"
    })
    state["updated_at"] = datetime.now().isoformat()
    return state
```

### Record Benchmark Results

```python
def record_benchmark(state: dict, benchmark: dict) -> dict:
    current = state["iterations"][-1]
    current["benchmark_summary"] = {
        "with_skill_pass_rate": benchmark["configurations"][0]["pass_rate"],
        "baseline_pass_rate": benchmark["configurations"][1]["pass_rate"],
        "delta": benchmark["delta"]["pass_rate_improvement"]
    }
    current["evals"] = [e["eval_id"] for e in benchmark.get("per_eval_results", [])]
    state["updated_at"] = datetime.now().isoformat()
    return state
```

### Complete Iteration

```python
def complete_iteration(state: dict, feedback_status: str = "incorporated") -> dict:
    current = state["iterations"][-1]
    current["completed_at"] = datetime.now().isoformat()
    current["user_feedback_status"] = feedback_status
    current["status"] = "complete"
    
    if feedback_status == "none" or feedback_status == "incorporated":
        state["current_stage"] = "optimizing"
    else:
        state["current_stage"] = "refining"
    
    state["updated_at"] = datetime.now().isoformat()
    return state
```

---

## Recovery and Resumption

### Check for In-Progress Work

```python
def find_in_progress(state: dict) -> Optional[dict]:
    """Find the last in-progress iteration, if any."""
    for iteration in reversed(state.get("iterations", [])):
        if iteration["status"] == "in_progress":
            return iteration
    return None
```

### Resume from State

```python
def resume_from_state(state: dict) -> str:
    """Determine what to do based on current state."""
    stage = state.get("current_stage", "intent")
    
    if stage == "testing":
        in_progress = find_in_progress(state)
        if in_progress:
            return f"Resume iteration {in_progress['iteration_number']} - check for running evals"
    
    if stage == "reviewing":
        return "Launch eval-viewer for user review"
    
    if stage == "refining":
        return "Read feedback.json and refine skill"
    
    return f"Continue from stage: {stage}"
```

---

## Migration from Old Schema

If you have state files using the old phase-based schema (v1.0), migrate as follows:

```python
def migrate_v1_to_v2(old_state: dict) -> dict:
    return {
        "schema_version": "2.0",
        "skill_name": old_state.get("blueprint_name", ""),
        "skill_path": "",
        "workspace_path": "",
        "current_iteration": 1 if old_state.get("current_phase") == "ACT" else 0,
        "current_stage": map_phase_to_stage(old_state.get("current_phase", "PENDING")),
        "started_at": old_state.get("metadata", {}).get("created_at", ""),
        "updated_at": old_state.get("metadata", {}).get("updated_at", ""),
        "iterations": [],
        "test_cases": [],
        "feedback_pending": False,
        "description_optimized": False
    }

def map_phase_to_stage(phase: str) -> str:
    mapping = {
        "PENDING": "intent",
        "PLAN": "intent",
        "ACT": "drafting",
        "VALIDATION": "testing",
        "COMPLETE": "complete",
        "ERROR": "refining",
        "CANCELLED": "complete"
    }
    return mapping.get(phase, "intent")
```

---

## Best Practices

1. **Persist after each significant operation** - Don't lose progress
2. **Keep iteration history** - Useful for analyzing improvement trajectory
3. **Snapshot skill before major changes** - Enables comparison
4. **Don't over-engineer** - The state exists to support the workflow, not complicate it
5. **Clean up old workspaces** - After skill is complete, archive or delete

---

## Integration

This tracking system integrates with:
- `skill-creation-workflow.md` — The workflow it supports
- `validation-rules.md` — Validation at each stage
- `skill-creator` skill — The primary consumer

---

*Aligned with skill-creator iterative methodology*