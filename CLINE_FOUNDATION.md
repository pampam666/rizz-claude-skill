# Cline Foundation Documentation

This workspace is configured for skill development using the **skill-creator** methodology — an iterative, eval-driven approach to creating high-quality Claude skills.

---

## Table of Contents

1. [Overview](#overview)
2. [The skill-creator Paradigm](#the-skill-creator-paradigm)
3. [Workspace Structure](#workspace-structure)
4. [Skill Development Workflow](#skill-development-workflow)
5. [Validation Standards](#validation-standards)
6. [Iteration Tracking](#iteration-tracking)
7. [Quick Reference](#quick-reference)

---

## Overview

### What is This Workspace?

This workspace provides a structured environment for creating Claude skills using the official **skill-creator** approach. Instead of rigid phase-gated workflows, we use an iterative loop:

```
Draft → Test → Evaluate → Refine → Repeat
```

### Core Philosophy

1. **Test early, iterate often** — Validate through actual performance
2. **Evidence over assumption** — Use parallel evals with baselines
3. **Human in the loop** — User feedback drives improvements
4. **Flexibility first** — Adapt to user needs, don't force rigid steps
5. **Ship when ready** — Stop when satisfied, not when a checklist completes

---

## The skill-creator Paradigm

### How Skills Are Created

The skill-creator skill (located in `.agents/skills/skill-creator/`) is the primary tool for creating new skills. It follows this workflow:

1. **Capture Intent** — Understand what the skill should do through interview
2. **Research** (optional) — Gather context, check MCPs, find best practices
3. **Draft SKILL.md** — Write initial skill with YAML frontmatter
4. **Create Test Prompts** — Write 2-3 realistic user prompts
5. **Run Parallel Evaluations** — Execute with-skill and baseline runs simultaneously
6. **User Review** — Present results via eval-viewer for qualitative feedback
7. **Refine** — Improve based on feedback and benchmark data
8. **Repeat** — Continue until satisfied
9. **Optimize Description** — Ensure skill triggers correctly
10. **Package** — Deliver the final `.skill` file

### Key Differences from Old Approach

| Aspect | Old Way | skill-creator Way |
|--------|---------|-------------------|
| Workflow | Plan → Confirm → Act | Draft → Test → Refine → Repeat |
| Validation | Structure checklists | Parallel evals + benchmarks |
| State | Phase-based (PLAN/ACT/VALIDATION) | Iteration-based (iteration-1, 2, 3...) |
| Quality | Checklist completion | User satisfaction + performance data |
| Flexibility | Rigid gates | Adaptable to user needs |

---

## Workspace Structure

```
d:\CLAUDE-SKILL\rizz-claude-skill\
│
├── .clinerules/                          # Configuration & rules
│   ├── validation-rules.md               # Validation standards
│   └── workflows/
│       ├── skill-creation-workflow.md    # Primary workflow
│       ├── iteration-tracking.md         # State tracking schema
│       └── workflow_state.json           # Current state
│
├── .agents/skills/                       # Installed skills
│   └── skill-creator/                    # The official skill-creator
│       ├── SKILL.md
│       ├── scripts/
│       ├── references/
│       └── eval-viewer/
│
├── claude-skill-framework/               # Generated skills go here
│   └── [skill-name]/
│
├── docs/                                 # Additional documentation
│   └── anthropic-best-practices.md
│
├── mcp-servers/                          # MCP server configurations
│
└── CLINE_FOUNDATION.md                   # This file
```

---

## Skill Development Workflow

### Starting a New Skill

1. **Invoke skill-creator** — Just describe what skill you want to create
2. **Answer interview questions** — Help clarify intent, triggers, outputs
3. **Review the draft** — Check the initial SKILL.md
4. **Approve test cases** — Confirm the test prompts look realistic

### The Evaluation Cycle

When running evaluations:

1. **Parallel execution** — Both with-skill and baseline runs launch together
2. **Draft assertions** — While runs execute, define what "good" looks like
3. **Review in eval-viewer** — See outputs side-by-side, leave feedback
4. **Check benchmarks** — Review pass rates, timing, token usage

### Iterating

After each evaluation cycle:

1. **Read feedback.json** — Understand what needs improvement
2. **Refine the skill** — Make targeted improvements, don't overfit
3. **Rerun evaluations** — Create a new iteration directory
4. **Compare** — Use eval-viewer with `--previous-workspace` to see progress

### When to Stop

Stop iterating when:
- User says they're happy
- All feedback is empty (everything looks good)
- Not making meaningful progress between iterations

### Description Optimization

After the skill content is finalized:

1. Generate trigger eval queries (should-trigger and should-not-trigger cases)
2. Review with user via HTML template
3. Run optimization loop: `python -m scripts.run_loop`
4. Apply the `best_description` from results

---

## Validation Standards

### Static Validation (Pre-Evaluation)

Before running tests, verify:

| Check | Requirement | Level |
|-------|-------------|-------|
| SKILL.md exists | Required file | CRITICAL |
| Valid YAML frontmatter | name + description only | CRITICAL |
| Directory naming | lowercase, kebab-case | CRITICAL |
| No placeholders | Remove all `{{...}}` | CRITICAL |

### YAML Frontmatter Format

**Valid:**
```yaml
---
name: skill-name
description: Single line description. Keywords include X, Y. Phrases include "do X". Context is when to use. DOES NOT trigger for exclusions.
---
```

**Invalid (causes errors):**
```yaml
---
name: skill-name
description: "Quoted text"
version: 1.0.0
author: Name
tags: [tag1, tag2]
---
```

### Performance Validation

Through evaluation:

| Metric | What It Means |
|--------|---------------|
| Pass rate | Percentage of assertions that passed |
| Delta | Improvement over baseline |
| Token usage | Efficiency measure |
| Duration | Time to complete |

### User Feedback Validation

Via eval-viewer:
- Empty feedback = satisfied
- Specific complaints = focus areas
- Patterns across cases = systemic issues

---

## Iteration Tracking

### State Schema

Track progress in `workflow_state.json`:

```json
{
  "schema_version": "2.0",
  "skill_name": "my-skill",
  "current_iteration": 2,
  "current_stage": "reviewing",
  "iterations": [
    {
      "iteration_number": 1,
      "benchmark_summary": {
        "with_skill_pass_rate": 0.75,
        "baseline_pass_rate": 0.50,
        "delta": 0.25
      },
      "user_feedback_status": "incorporated"
    }
  ]
}
```

### Stages

| Stage | Description |
|-------|-------------|
| `intent` | Capturing requirements |
| `drafting` | Writing SKILL.md |
| `testing` | Running evaluations |
| `reviewing` | User reviewing results |
| `refining` | Improving based on feedback |
| `optimizing` | Optimizing description |
| `complete` | Done |

### Iteration Directory Structure

```
skill-workspace/
├── iteration-1/
│   ├── eval-0/
│   │   ├── with_skill/
│   │   │   ├── outputs/
│   │   │   ├── grading.json
│   │   │   └── timing.json
│   │   ├── without_skill/
│   │   └── eval_metadata.json
│   ├── benchmark.json
│   └── benchmark.md
├── iteration-2/
│   └── ...
└── feedback.json
```

---

## Quick Reference

### Using skill-creator

Just describe what you want:

> "Create a skill that helps me write commit messages following conventional commits format"

The skill-creator will guide you through the process.

### Key Commands

**Aggregate benchmark:**
```bash
python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>
```

**Launch eval-viewer:**
```bash
python eval-viewer/generate_review.py <workspace>/iteration-N --skill-name "my-skill" --benchmark benchmark.json
```

**Headless environments:**
```bash
python eval-viewer/generate_review.py ... --static output.html
```

**Optimize description:**
```bash
python -m scripts.run_loop --eval-set trigger-eval.json --skill-path /path/to/skill --model <model-id>
```

**Package skill:**
```bash
python -m scripts.package_skill /path/to/skill-folder
```

### File Locations

| Item | Location |
|------|----------|
| Configuration | `.clinerules/` |
| skill-creator skill | `.agents/skills/skill-creator/` |
| Generated skills | `claude-skill-framework/` |
| Iteration workspaces | `[skill-name]-workspace/` |

### Skill Structure

```
skill-name/
├── SKILL.md              # Required
├── scripts/              # Optional: executable helpers
├── templates/            # Optional: output templates
├── references/           # Optional: loaded as needed
├── assets/               # Optional: static files
└── evals/                # Optional: test cases
    └── evals.json
```

---

## Further Reading

- `.clinerules/validation-rules.md` — Detailed validation standards
- `.clinerules/workflows/skill-creation-workflow.md` — Full workflow documentation
- `.clinerules/workflows/iteration-tracking.md` — State tracking details
- `.agents/skills/skill-creator/SKILL.md` — The skill-creator itself

---

*This workspace follows the skill-creator iterative methodology.*