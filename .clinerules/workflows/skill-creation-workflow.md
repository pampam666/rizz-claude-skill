# Skill Creation Workflow

The primary workflow for creating and improving skills, following the skill-creator's iterative, eval-driven methodology.

## Overview

This workflow replaces rigid phase-gated approaches with a flexible, evidence-based iteration loop. The goal is to create skills that actually perform well in practice, validated through real test cases and user feedback.

---

## Core Philosophy

### The Iterative Loop

```
Capture Intent → Draft → Test → Evaluate → Refine → Repeat
```

Key principles:
- **Flexibility first** - Adapt to user needs, don't force rigid steps
- **Evidence over assumption** - Validate through actual performance
- **Human in the loop** - User feedback drives improvements
- **Ship when ready** - Stop when satisfied, not when a checklist completes

---

## Workflow Stages

### Stage 1: Capture Intent

Understand what the user wants the skill to do.

**Activities:**
1. Listen to user's request
2. Extract from conversation history if skill is based on existing workflow
3. Ask clarifying questions:
   - What should this skill enable Claude to do?
   - When should this skill trigger?
   - What's the expected output format?
   - Should we set up test cases?

**Interview Questions:**
- Edge cases and how to handle them
- Input/output formats and examples
- Success criteria
- Dependencies and tools needed

**Output:** Clear understanding of skill purpose and scope

---

### Stage 2: Research (Optional)

If the skill involves unfamiliar domains or tools:

**Activities:**
1. Check available MCPs for research capabilities
2. Search documentation, find similar skills
3. Look up best practices
4. Come prepared with context

**Output:** Research notes, reference materials

---

### Stage 3: Draft SKILL.md

Write the initial skill draft based on captured intent.

**Structure:**
```
skill-name/
├── SKILL.md              # Required
│   ├── YAML frontmatter (name, description)
│   └── Markdown instructions
└── (optional) scripts/, templates/, references/, assets/
```

**YAML Frontmatter:**
```yaml
---
name: skill-name
description: Single line description. Keywords include X, Y. Phrases include "do X thing". Context is when to use. DOES NOT trigger for exclusion cases.
---
```

**Writing Guidelines:**
- Keep SKILL.md under 500 lines
- Explain WHY, not just WHAT
- Use imperative form
- Include examples for clarity
- Define output formats explicitly

**Output:** Draft SKILL.md in skill directory

---

### Stage 4: Create Test Prompts

Write 2-3 realistic test prompts that represent actual user requests.

**Good test prompts are:**
- Realistic - what a real user would actually say
- Varied - different phrasings, contexts
- Substantive - complex enough to benefit from a skill

**Store in evals/evals.json:**
```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "User's task prompt",
      "expected_output": "Description of expected result",
      "files": [],
      "assertions": []
    }
  ]
}
```

**Output:** Test cases ready for evaluation

---

### Stage 5: Run Parallel Evaluations

Execute test cases with both skill-enabled and baseline runs.

**Process:**

1. **Spawn all runs simultaneously:**
   - With-skill run: Claude has access to the skill
   - Baseline run: No skill (or old version for improvements)

2. **While runs execute, draft assertions:**
   - Objectively verifiable checks
   - Descriptively named
   - Non-redundant

3. **Capture timing data** from completion notifications:
   ```json
   {
     "total_tokens": 84852,
     "duration_ms": 23332
   }
   ```

4. **Grade outputs** against assertions

5. **Aggregate into benchmark:**
   ```bash
   python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>
   ```

**Output:** 
- `iteration-N/` directory with outputs, grading, timing
- `benchmark.json` and `benchmark.md`

---

### Stage 6: User Review via Eval-Viewer

Present results for qualitative human review.

**Launch the viewer:**
```bash
python <skill-creator-path>/eval-viewer/generate_review.py \
  <workspace>/iteration-N \
  --skill-name "my-skill" \
  --benchmark <workspace>/iteration-N/benchmark.json
```

**For headless environments:**
```bash
python generate_review.py ... --static <output_path>.html
```

**What the user sees:**
- **Outputs tab**: Each test case with prompt, output, feedback form
- **Benchmark tab**: Quantitative stats (pass rates, timing, tokens)

**User provides feedback** via the form, saved to `feedback.json`

---

### Stage 7: Refine Based on Feedback

Improve the skill using evaluation results and user feedback.

**How to approach improvements:**

1. **Generalize from feedback** - Don't overfit to specific test cases
2. **Keep lean** - Remove what isn't pulling its weight
3. **Explain the why** - Help the model understand reasoning
4. **Look for repeated patterns** - Bundle common operations as scripts

**After refining:**
- Increment iteration number
- Rerun all test cases
- Launch viewer with `--previous-workspace` for comparison
- Collect new feedback
- Repeat until satisfied

**Stop conditions:**
- User says they're happy
- Feedback is all empty (everything looks good)
- Not making meaningful progress

---

### Stage 8: Optimize Description (Optional)

After skill content is finalized, optimize the description for better triggering.

**Process:**

1. **Generate trigger eval queries** (20 total):
   - 8-10 should-trigger cases
   - 8-10 should-not-trigger cases (near-misses)

2. **Review with user** via HTML template

3. **Run optimization loop:**
   ```bash
   python -m scripts.run_loop \
     --eval-set trigger-eval.json \
     --skill-path /path/to/skill \
     --model <model-id> \
     --max-iterations 5
   ```

4. **Apply best_description** from results

**Output:** Optimized description that triggers accurately

---

### Stage 9: Package and Deliver

Package the final skill for installation.

**If present_files tool available:**
```bash
python -m scripts.package_skill <path/to/skill-folder>
```

**Output:** `.skill` file ready for installation

---

## Iteration Tracking

Track progress through iterations, not phases.

### Directory Structure
```
skill-workspace/
├── iteration-1/
│   ├── eval-0/
│   │   ├── with_skill/
│   │   ├── without_skill/
│   │   └── eval_metadata.json
│   ├── benchmark.json
│   └── benchmark.md
├── iteration-2/
│   └── ...
├── feedback.json
└── skill-snapshot/  (for improvement workflows)
```

### State Schema
See `iteration-tracking.md` for the state tracking schema.

---

## Flexibility Guidelines

The skill-creator emphasizes flexibility. Adapt to the user's needs:

- **"I don't need evaluations, just vibe with me"** → Skip testing, iterate conversationally
- **User already has a draft** → Jump straight to eval/iterate
- **Simple skill, obvious results** → Maybe one iteration is enough
- **Complex skill, subtle issues** → Run multiple iterations with detailed feedback

Don't force steps that aren't needed. The loop exists to ensure quality, not to create bureaucracy.

---

## Communication Tips

Users may have varying technical backgrounds:

- **Default**: "evaluation" and "benchmark" are OK
- **Explain if uncertain**: Brief definitions for "JSON", "assertion", etc.
- **Read context cues**: Adjust language based on user's familiarity

---

## Integration

This workflow integrates with:
- `validation-rules.md` — What "valid" means at each stage
- `iteration-tracking.md` — How to track state across iterations
- `skill-creator` skill — The actual execution engine

---

*Aligned with skill-creator iterative methodology*