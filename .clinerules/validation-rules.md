# Validation Rules

Defines validation standards for skill development, aligned with the skill-creator's iterative, eval-driven methodology.

## Overview

Validation in this workspace follows the skill-creator paradigm: **test early, iterate often, let evidence guide refinement**. Static checks (YAML format, structure) are necessary but insufficient. Real validation comes from running test cases, comparing against baselines, and incorporating user feedback.

---

## Validation Philosophy

### The Iterative Validation Loop

```
Draft → Test → Evaluate → Refine → Repeat
```

Unlike rigid phase-gated validation, this approach:
- Validates through actual performance, not just structure
- Uses parallel comparisons (with-skill vs baseline)
- Incorporates human judgment via eval-viewer
- Iterates until quality targets are met

### When to Validate

| Stage | Validation Focus |
|-------|------------------|
| **After Drafting** | Static checks (YAML, structure, naming) |
| **After Test Runs** | Assertion pass rates, timing, token usage |
| **After User Review** | Qualitative feedback integration |
| **Before Completion** | Trigger accuracy via description optimization |

---

## Static Validation (Pre-Evaluation)

These checks run before test evaluations to catch structural issues early.

### 1. Structure Validation

| Check | Requirement | Level |
|-------|-------------|-------|
| `SKILL.md exists` | Skill directory must contain SKILL.md | CRITICAL |
| `Valid subfolders` | Only use: scripts/, templates/, references/, assets/, evals/ | WARNING |

**Valid structure:**
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

### 2. YAML Frontmatter Validation (CRITICAL)

Based on official Anthropic skills repository standards.

#### Required Fields

| Field | Requirement | Level |
|-------|-------------|-------|
| `name` | Must be present | CRITICAL |
| `description` | Must be present | CRITICAL |

#### Claude.ai Compatibility

| Requirement | Level | Message |
|-------------|-------|---------|
| Only `name` and `description` fields | CRITICAL | "Claude.ai only supports name and description fields" |
| `description` must be unquoted single-line | CRITICAL | "Description must be unquoted single-line text" |
| No `version`, `author`, or `tags` fields | CRITICAL | "Remove version, author, tags - not supported" |
| No literal block scalars (`\|`) | CRITICAL | "Do not use YAML literal block scalars (|)" |
| No folded block scalars (`>`) | CRITICAL | "Do not use YAML folded block scalars (>)" |
| No multi-line descriptions | CRITICAL | "Multi-line descriptions cause parsing errors" |

#### Valid Format
```yaml
---
name: skill-name
description: Single line description without quotes. Keywords include keyword1, keyword2. Phrases include phrase1, phrase2. Context is when to use this skill. DOES NOT trigger for exclusion cases.
---
```

#### Invalid Format (Causes Malformed YAML Error)
```yaml
---
name: skill-name
description: "Quoted description"
version: 1.0.0
author: AuthorName
tags: [tag1, tag2]
---
```

---

### 3. Naming Convention Validation

| Check | Requirement | Level |
|-------|-------------|-------|
| Directory lowercase | No uppercase letters | CRITICAL |
| No spaces | Use hyphens instead | CRITICAL |
| kebab-case | Hyphen-separated words | WARNING |
| Name matches directory | SKILL.md name = folder name | WARNING |

---

### 4. Content Validation

| Check | Requirement | Level |
|-------|-------------|-------|
| No `{{placeholder}}` text | Remove all placeholders | CRITICAL |
| No `TODO` comments | Resolve before completion | WARNING |
| No `FIXME` comments | Resolve before completion | WARNING |
| Has clear instructions | Skill body provides actionable guidance | WARNING |

---

## Evaluation-Based Validation

The skill-creator approach validates through actual performance.

### 1. Test Case Structure

Test cases are stored in `evals/evals.json`:

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "Realistic user task prompt",
      "expected_output": "Description of expected result",
      "files": [],
      "assertions": [
        {
          "name": "descriptive-assertion-name",
          "expected": "What should be true",
          "check_type": "contains|regex|exact|custom"
        }
      ]
    }
  ]
}
```

### 2. Assertion Design Principles

Good assertions are:
- **Objectively verifiable** - Can be checked programmatically
- **Descriptively named** - Clear in benchmark viewer
- **Non-redundant** - Each tests something different
- **Discriminating** - Distinguish good from bad outputs

Avoid assertions for:
- Subjective qualities (writing style, design aesthetics)
- Vague criteria that require human judgment

### 3. Parallel Evaluation Requirements

For valid comparison:
- **With-skill run**: Claude has access to the skill
- **Baseline run**: Claude works without the skill (or with old version)
- **Same prompt**: Both runs receive identical task
- **Simultaneous spawn**: Launch in same turn to finish together

### 4. Benchmark Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| `pass_rate` | Percentage of assertions passed | Higher is better |
| `total_tokens` | Token consumption | Lower is better (ceteris paribus) |
| `duration_ms` | Execution time | Lower is better |
| `delta` | Improvement over baseline | Positive = skill helps |

### 5. Iteration Tracking

Results organized by iteration:
```
skill-workspace/
├── iteration-1/
│   ├── eval-0/
│   │   ├── with_skill/
│   │   │   ├── outputs/
│   │   │   ├── grading.json
│   │   │   └── timing.json
│   │   ├── without_skill/
│   │   │   ├── outputs/
│   │   │   ├── grading.json
│   │   │   └── timing.json
│   │   └── eval_metadata.json
│   ├── benchmark.json
│   └── benchmark.md
├── iteration-2/
│   └── ...
└── feedback.json
```

---

## User Feedback Validation

The eval-viewer enables human-in-the-loop validation.

### Feedback Collection

After each iteration:
1. Run `eval-viewer/generate_review.py` to launch viewer
2. User reviews outputs qualitatively
3. User provides feedback per test case
4. Feedback saved to `feedback.json`

### Feedback Schema
```json
{
  "reviews": [
    {
      "run_id": "eval-0-with_skill",
      "feedback": "User's qualitative feedback",
      "timestamp": "ISO-8601"
    }
  ],
  "status": "complete"
}
```

### Validation from Feedback

- Empty feedback = user satisfied
- Specific complaints = focus areas for refinement
- Pattern across cases = systemic issue to address

---

## Trigger Accuracy Validation

After skill content is finalized, validate description triggers correctly.

### Description Optimization Process

1. **Generate trigger eval queries** (20 total):
   - 8-10 should-trigger cases (varied phrasings, edge cases)
   - 8-10 should-not-trigger cases (near-misses, adjacent domains)

2. **Review with user** via HTML template

3. **Run optimization loop**:
   ```bash
   python -m scripts.run_loop \
     --eval-set trigger-eval.json \
     --skill-path /path/to/skill \
     --model <model-id> \
     --max-iterations 5
   ```

4. **Apply best_description** from results

### Description Quality Checks

| Check | Requirement |
|-------|-------------|
| Includes keywords | Specific trigger words present |
| Includes phrases | Multi-word expressions that should trigger |
| Includes context | When skill should activate |
| Includes exclusions | "DOES NOT trigger for..." cases |
| Single-line | No newlines or block scalars |
| Unquoted | No surrounding quotes |

---

## Validation Report Format

```json
{
  "skill_name": "example-skill",
  "validation_timestamp": "ISO-8601-timestamp",
  "iteration": 3,
  "static_checks": {
    "yaml_valid": true,
    "structure_valid": true,
    "naming_valid": true,
    "no_placeholders": true
  },
  "benchmark_summary": {
    "with_skill_pass_rate": 0.87,
    "baseline_pass_rate": 0.62,
    "delta": 0.25,
    "total_evals": 5
  },
  "user_feedback_status": "incorporated",
  "trigger_accuracy": {
    "tested": true,
    "train_score": 0.92,
    "test_score": 0.88
  },
  "overall_status": "pass",
  "recommendations": []
}
```

---

## Validation Levels

### Critical (Must Pass)
- SKILL.md exists
- Valid YAML frontmatter (name + description only)
- No placeholder text
- Directory naming correct

### Performance-Based (Should Meet Targets)
- Pass rate improves over baseline
- User feedback addressed
- Trigger accuracy > 85%

### Warning (Nice to Have)
- SKILL.md under 500 lines
- Clear section organization
- Bundled scripts for repeated patterns

---

## Integration with skill-creator

This validation system is designed to work seamlessly with the skill-creator skill:

1. **Static validation** runs after initial draft
2. **Evaluation validation** runs during test phase
3. **Feedback validation** runs after user review
4. **Trigger validation** runs before final packaging

The skill-creator skill itself handles the orchestration - these rules define what "valid" means at each stage.

---

*Aligned with skill-creator iterative methodology*