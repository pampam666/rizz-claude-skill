---
name: comparison-analyst
description: AUTO-TRIGGERS when comparison tables or metrics needed for prompt frameworks. Keywords include compare frameworks, pros cons table, benchmark metrics, ease of use, comparison matrix. Phrases include create comparison table, analyze framework differences, benchmark prompt frameworks, rate frameworks. Context is analysis phase of prompt research workflow. DOES NOT trigger for research gathering, report generation, or non-comparison tasks.
---

# Comparison Analyst

Specialist skill for transforming research artifacts into structured comparison tables with mandatory metrics.

## Mission

Build comprehensive comparison tables with standardized metrics for prompt engineering frameworks, enabling clear decision-making based on pros/cons, ease of use, LLM thinking process, and scalability.

## Activation Protocol

### Automatic Triggers
- Research phase completion detected
- Comparison table creation requested
- Metrics benchmarking needed

### Input Requirements

| Input | Source | Required |
|-------|--------|----------|
| `research_artifacts.framework_data` | workflow_state.json | Yes |
| `research_artifacts.sources` | workflow_state.json | Yes |
| `selected_toc` | workflow_state.json | Yes |

## Mandatory Metrics

All comparisons MUST include these metrics:

### 1. Pros and Cons Table

```json
{
  "pros_cons": {
    "framework_a": {
      "pros": [
        "Pro 1: description",
        "Pro 2: description",
        "Pro 3: description"
      ],
      "cons": [
        "Con 1: description",
        "Con 2: description",
        "Con 3: description"
      ]
    },
    "framework_b": {
      "pros": [...],
      "cons": [...]
    }
  }
}
```

### 2. Ease of Use Rating

| Score | Description |
|-------|-------------|
| 1-2 | Expert only, complex setup |
| 3-4 | Advanced knowledge required |
| 5-6 | Moderate learning curve |
| 7-8 | Beginner-friendly |
| 9-10 | No experience needed |

**Criteria for Rating:**
- Implementation complexity
- Documentation quality
- Community support
- Tool requirements
- Error handling difficulty

### 3. LLM Thinking Process Analysis

For each framework, document:

```json
{
  "thinking_process": {
    "framework_name": {
      "reasoning_type": "sequential|parallel|iterative|tree-based",
      "description": "How the LLM processes information",
      "steps": ["Step 1", "Step 2", "Step 3"],
      "transparency": "high|medium|low",
      "example": "Example of thinking output"
    }
  }
}
```

### 4. Scalability Assessment

| Level | Criteria |
|-------|----------|
| **High** | Production-ready, handles enterprise load, well-documented |
| **Medium** | Works at scale with caveats, some optimization needed |
| **Low** | Experimental, limited testing, performance concerns |

**Assessment Factors:**
- Token efficiency
- Latency impact
- Error rate at scale
- Production deployments known

### 5. Grok Compatibility

| Status | Criteria |
|--------|----------|
| **Yes** | Fully supported, documented examples, tested |
| **Partial** | Works with modifications, limited testing |
| **No** | Incompatible, no support, fundamental conflicts |

### 6. Claude Compatibility

| Status | Criteria |
|--------|----------|
| **Yes** | Native support, Anthropic documentation |
| **Partial** | Works with adaptation, community examples |
| **No** | Incompatible with Claude's architecture |

### 7. Benchmark Performance

```json
{
  "benchmarks": {
    "framework_name": {
      "accuracy": {
        "metric": "value",
        "source": "citation"
      },
      "speed": {
        "metric": "value",
        "source": "citation"
      },
      "token_efficiency": {
        "metric": "value",
        "source": "citation"
      }
    }
  }
}
```

## Comparison Matrix Template

Use `templates/comparison-matrix.json`:

```json
{
  "comparison_matrix": {
    "title": "Framework Comparison Matrix",
    "frameworks": ["Framework A", "Framework B"],
    "metrics": {
      "ease_of_use": {
        "framework_a": 8,
        "framework_b": 6,
        "notes": "Framework A has better documentation"
      },
      "scalability": {
        "framework_a": "High",
        "framework_b": "Medium",
        "notes": "Framework A has more production deployments"
      },
      "grok_compatibility": {
        "framework_a": "Yes",
        "framework_b": "Partial",
        "notes": "Framework B requires prompt modifications for Grok"
      },
      "claude_compatibility": {
        "framework_a": "Yes",
        "framework_b": "Yes",
        "notes": "Both work well with Claude"
      },
      "thinking_process": {
        "framework_a": "Sequential reasoning with explicit steps",
        "framework_b": "Iterative action-observation loops"
      },
      "token_overhead": {
        "framework_a": "Medium (+20-30%)",
        "framework_b": "High (+40-60%)"
      }
    }
  }
}
```

## Analysis Process

### Step 1: Extract Framework Data

From `research_artifacts.framework_data`, extract for each framework:
- Core mechanism description
- Implementation complexity indicators
- Compatibility information
- Source quality scores

### Step 2: Calculate Ease of Use

```
ease_of_use_score = (
  (10 - implementation_complexity) * 0.4 +
  documentation_quality * 0.3 +
  community_support * 0.2 +
  tool_availability * 0.1
)
```

### Step 3: Build Pros/Cons

For each framework:

**Pros identification:**
- Unique advantages from sources
- Performance benefits
- Ease of implementation
- Community strengths

**Cons identification:**
- Limitations from sources
- Performance drawbacks
- Implementation challenges
- Known issues

### Step 4: Assess Compatibility

Cross-reference with:
- Official documentation for native support
- Community examples for tested compatibility
- Technical analysis for architectural fit

### Step 5: Compile Benchmarks

Extract from academic sources:
- Accuracy metrics
- Speed/latency data
- Token efficiency measurements
- Comparative study results

## Output Schema

Update `workflow_state.json` with:

```json
{
  "analysis_artifacts": {
    "comparison_tables": {
      "pros_cons": { /* pros/cons data */ },
      "comparison_matrix": { /* matrix data */ },
      "thinking_process": { /* thinking analysis */ }
    },
    "metrics": {
      "ease_of_use": { /* scores */ },
      "scalability": { /* assessments */ },
      "compatibility": { /* grok/claude */ },
      "token_efficiency": { /* token data */ }
    },
    "benchmarks": {
      /* benchmark data from sources */
    },
    "analysis_metadata": {
      "frameworks_analyzed": 2,
      "metrics_calculated": 7,
      "sources_used": 8,
      "confidence_score": 0.85
    }
  }
}
```

## Quality Standards

| Metric | Target |
|--------|--------|
| Pros per framework | Minimum 3 |
| Cons per framework | Minimum 2 |
| Ease of use score | 1-10 scale |
| Compatibility check | All frameworks |
| Benchmark sources | Minimum 1 per metric |

## Error Handling

| Error | Code | Recovery |
|-------|------|----------|
| Missing framework data | E004 | Request additional research |
| Insufficient benchmarks | E005 | Mark as "data unavailable" |
| Conflicting sources | E006 | Use priority weighting |

## Quality Checklist

- [ ] All frameworks analyzed
- [ ] Pros/cons tables complete
- [ ] Ease of use scores calculated
- [ ] LLM thinking process documented
- [ ] Scalability assessed
- [ ] Grok compatibility checked
- [ ] Claude compatibility checked
- [ ] Benchmarks compiled
- [ ] Comparison matrix built
- [ ] workflow_state.json updated

## Example Execution

**Input:**
```json
{
  "framework_data": {
    "chain-of-thought": {
      "description": "Sequential reasoning with explicit steps",
      "implementation_complexity": 3,
      "compatibility": {"claude": "Yes", "grok": "Yes"}
    },
    "react": {
      "description": "Iterative action-observation loops",
      "implementation_complexity": 5,
      "compatibility": {"claude": "Yes", "grok": "Partial"}
    }
  }
}
```

**Output:**
```json
{
  "analysis_artifacts": {
    "comparison_tables": {
      "pros_cons": {
        "chain-of-thought": {
          "pros": ["Transparent reasoning", "Easy to implement", "Wide compatibility"],
          "cons": ["Token overhead", "Slower inference"]
        },
        "react": {
          "pros": ["Tool integration", "Dynamic adaptation", "Action-oriented"],
          "cons": ["Complex setup", "Error propagation risk"]
        }
      }
    },
    "metrics": {
      "ease_of_use": {"chain-of-thought": 8, "react": 6},
      "scalability": {"chain-of-thought": "High", "react": "Medium"},
      "compatibility": {
        "chain-of-thought": {"grok": "Yes", "claude": "Yes"},
        "react": {"grok": "Partial", "claude": "Yes"}
      }
    }
  }
}
```

---

*Part of Prompt Research Orchestrator Framework*