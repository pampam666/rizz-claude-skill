# Prompt Frameworks Encyclopedia

> Comprehensive reference guide to prompt engineering frameworks

---

## Table of Contents

1. [Chain-of-Thought (CoT)](#chain-of-thought-cot)
2. [ReAct](#react)
3. [xAI Prompting](#xai-prompting)
4. [Prompt Chaining](#prompt-chaining)
5. [Few-Shot Prompting](#few-shot-prompting)
6. [Self-Consistency](#self-consistency)
7. [Tree of Thoughts](#tree-of-thoughts)
8. [Chain-of-Verification](#chain-of-verification)
9. [Skeleton-of-Thought](#skeleton-of-thought)
10. [Claude Skills & Project Frameworks](#claude-skills--project-frameworks)

---

## Chain-of-Thought (CoT)

### Overview
Chain-of-Thought prompting is a technique that encourages language models to reason through a problem step-by-step before providing a final answer.

### Core Mechanism
The model generates intermediate reasoning steps, creating a "chain" of thoughts that lead to the conclusion.

### LLM Thinking Process
- **Type**: Sequential reasoning
- **Transparency**: High
- **Steps**:
  1. Problem decomposition
  2. Step-by-step reasoning
  3. Intermediate conclusions
  4. Final synthesis

### Typical Use Cases
- Mathematical reasoning
- Logical deduction problems
- Complex multi-step tasks
- Code debugging

### Implementation Complexity
**Low to Medium** - Simple to implement with phrase "Let's think step by step"

### Compatibility
| Platform | Support |
|----------|---------|
| Claude | Yes - Native support |
| GPT | Yes - Native support |
| Grok | Yes - Supported |

### Token Overhead
Medium (+20-30% additional tokens)

### Key Papers
- Wei et al. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
- Kojima et al. (2022). "Large Language Models are Zero-Shot Reasoners"

---

## ReAct

### Overview
ReAct (Reasoning + Acting) combines reasoning traces with external tool use, enabling models to interact with environments.

### Core Mechanism
The model alternates between thinking (reasoning traces) and acting (tool calls), creating an iterative loop.

### LLM Thinking Process
- **Type**: Iterative action-observation
- **Transparency**: High
- **Steps**:
  1. Thought about current state
  2. Action selection
  3. Action execution
  4. Observation of result
  5. Next thought

### Typical Use Cases
- Web browsing agents
- Question answering with search
- Tool-using agents
- Interactive problem solving

### Implementation Complexity
**Medium** - Requires tool integration and action space definition

### Compatibility
| Platform | Support |
|----------|---------|
| Claude | Yes - With tool definitions |
| GPT | Yes - With function calling |
| Grok | Partial - Limited tool support |

### Token Overhead
High (+40-60% additional tokens for multi-turn interactions)

### Key Papers
- Yao et al. (2022). "ReAct: Synergizing Reasoning and Acting in Language Models"
- Shinn et al. (2023). "Reflexion: Language Agents with Verbal Reinforcement Learning"

---

## xAI Prompting

### Overview
xAI prompting refers to techniques optimized for xAI's Grok model, emphasizing specific patterns that leverage Grok's unique capabilities.

### Core Mechanism
Grok-optimized prompts that leverage real-time information access and reasoning capabilities.

### LLM Thinking Process
- **Type**: Hybrid (sequential + real-time)
- **Transparency**: Medium
- **Steps**:
  1. Query understanding
  2. Real-time information retrieval
  3. Synthesis with training data
  4. Response generation

### Typical Use Cases
- Real-time information queries
- News and current events
- Factual verification
- Research with citations

### Implementation Complexity
**Low** - Natural language prompts work directly

### Compatibility
| Platform | Support |
|----------|---------|
| Claude | No - Platform-specific |
| GPT | No - Platform-specific |
| Grok | Yes - Native |

### Token Overhead
Low (native optimization)

### Key Resources
- xAI Documentation
- Grok Prompting Guide

---

## Prompt Chaining

### Overview
Prompt chaining breaks complex tasks into sequential sub-tasks, where each prompt's output feeds into the next prompt's input.

### Core Mechanism
A series of connected prompts where output from step N becomes context/input for step N+1.

### LLM Thinking Process
- **Type**: Sequential pipeline
- **Transparency**: Medium
- **Steps**:
  1. Task decomposition
  2. Sequential execution
  3. Output validation
  4. Chain progression
  5. Final aggregation

### Typical Use Cases
- Document summarization pipelines
- Multi-stage data processing
- Content generation workflows
- Complex analysis tasks

### Implementation Complexity
**Medium** - Requires pipeline design and output parsing

### Compatibility
| Platform | Support |
|----------|---------|
| Claude | Yes - Excellent for chaining |
| GPT | Yes - Well supported |
| Grok | Yes - Supported |

### Token Overhead
Medium to High (depends on chain length)

### Key Papers
- Wu et al. (2022). "AI Chains: Transparent and Controllable Human-AI Interaction"

---

## Few-Shot Prompting

### Overview
Few-shot prompting provides examples in the prompt to guide the model's output format and style without updating model weights.

### Core Mechanism
Include 2-5 example input-output pairs in the prompt before the actual task.

### LLM Thinking Process
- **Type**: Pattern matching
- **Transparency**: Medium
- **Steps**:
  1. Example pattern recognition
  2. Pattern abstraction
  3. Application to new input
  4. Output generation

### Typical Use Cases
- Format specification
- Style transfer
- Task demonstration
- Classification tasks

### Implementation Complexity
**Low** - Simple example inclusion in prompts

### Compatibility
| Platform | Support |
|----------|---------|
| Claude | Yes - Excellent few-shot learner |
| GPT | Yes - Native support |
| Grok | Yes - Supported |

### Token Overhead
Low to Medium (depends on example count)

### Key Papers
- Brown et al. (2020). "Language Models are Few-Shot Learers"
- Liu et al. (2022). "What Makes Good In-Context Examples for GPT-3?"

---

## Self-Consistency

### Overview
Self-consistency improves reasoning by sampling multiple reasoning paths and selecting the most consistent answer through majority voting.

### Core Mechanism
Generate multiple Chain-of-Thought responses, then aggregate through voting to find the most consistent answer.

### LLM Thinking Process
- **Type**: Parallel sampling + aggregation
- **Transparency**: High
- **Steps**:
  1. Generate multiple reasoning paths
  2. Extract final answers
  3. Majority voting
  4. Consistency verification
  5. Final answer selection

### Typical Use Cases
- Mathematical problems
- Logical reasoning
- High-stakes decisions
- Accuracy-critical tasks

### Implementation Complexity
**Medium** - Requires multiple generations and aggregation logic

### Compatibility
| Platform | Support |
|----------|---------|
| Claude | Yes - Supported |
| GPT | Yes - Supported |
| Grok | Yes - Supported |

### Token Overhead
High (multiple generations required)

### Key Papers
- Wang et al. (2022). "Self-Consistency Improves Chain of Thought Reasoning in Language Models"

---

## Tree of Thoughts

### Overview
Tree of Thoughts (ToT) extends CoT by exploring multiple reasoning paths in a tree structure, enabling backtracking and evaluation.

### Core Mechanism
Model generates multiple thought branches, evaluates them, and can backtrack from dead ends.

### LLM Thinking Process
- **Type**: Tree-based exploration
- **Transparency**: High
- **Steps**:
  1. Generate thought branches
  2. Evaluate each branch
  3. Select promising paths
  4. Backtrack from dead ends
  5. Synthesize solution

### Typical Use Cases
- Complex planning
- Creative writing
- Strategic decisions
- Multi-step reasoning with uncertainty

### Implementation Complexity
**High** - Requires tree management and evaluation logic

### Compatibility
| Platform | Support |
|----------|---------|
| Claude | Yes - With careful prompting |
| GPT | Yes - Supported |
| Grok | Partial - May need adaptation |

### Token Overhead
Very High (exponential with tree depth)

### Key Papers
- Yao et al. (2023). "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"

---

## Chain-of-Verification

### Overview
Chain-of-Verification (CoVe) generates verification questions to check the model's own answers, reducing hallucinations.

### Core Mechanism
After generating an initial response, the model generates verification questions and checks each claim.

### LLM Thinking Process
- **Type**: Self-verification loop
- **Transparency**: High
- **Steps**:
  1. Initial response generation
  2. Verification question generation
  3. Independent verification
  4. Inconsistency detection
  5. Corrected response

### Typical Use Cases
- Fact-checking
- Hallucination reduction
- Accuracy-critical applications
- Research verification

### Implementation Complexity
**Medium** - Requires two-phase prompting

### Compatibility
| Platform | Support |
|----------|---------|
| Claude | Yes - Supported |
| GPT | Yes - Supported |
| Grok | Yes - Supported |

### Token Overhead
High (verification pass required)

### Key Papers
- Dhuliawala et al. (2023). "Chain-of-Verification Reduces Hallucination in Large Language Models"

---

## Skeleton-of-Thought

### Overview
Skeleton-of-Thought generates a response skeleton first, then fills in details in parallel, reducing latency.

### Core Mechanism
Two-phase approach: (1) Generate skeleton/outline, (2) Fill in details potentially in parallel.

### LLM Thinking Process
- **Type**: Outline-then-fill
- **Transparency**: Medium
- **Steps**:
  1. Skeleton generation
  2. Point identification
  3. Parallel detail generation
  4. Integration
  5. Final response

### Typical Use Cases
- Long-form content generation
- Report writing
- Document generation
- Low-latency applications

### Implementation Complexity
**Medium** - Requires two-phase prompting

### Compatibility
| Platform | Support |
|----------|---------|
| Claude | Yes - Supported |
| GPT | Yes - Supported |
| Grok | Yes - Supported |

### Token Overhead
Medium (but reduced latency)

### Key Papers
- Naik et al. (2023). "Skeleton-of-Thought: Prompting LLMs for Efficient and Efficient Generation"

---

## Claude Skills & Project Frameworks

### Overview
Claude's native skills and project frameworks enable persistent context and reusable instruction sets for specialized tasks.

### Core Mechanism
Structured instruction files (SKILL.md) with YAML frontmatter that Claude loads as context when triggered.

### LLM Thinking Process
- **Type**: Context-augmented reasoning
- **Transparency**: High
- **Steps**:
  1. Skill trigger detection
  2. Context loading
  3. Instruction following
  4. Structured output generation

### Typical Use Cases
- Specialized workflows
- Repeated task patterns
- Domain-specific operations
- Multi-step processes

### Implementation Complexity
**Medium to High** - Requires SKILL.md authoring

### Compatibility
| Platform | Support |
|----------|---------|
| Claude | Yes - Native feature |
| GPT | No - Use GPTs/Custom Instructions |
| Grok | No - Not supported |

### Token Overhead
Low (pre-loaded context)

### Key Resources
- Anthropic Skills Documentation
- Claude.ai Skills Guide
- skill-creator Framework

---

## Quick Reference Matrix

| Framework | Ease of Use | Scalability | Claude | Grok | Token Overhead |
|-----------|-------------|-------------|--------|------|-----------------|
| CoT | 8/10 | High | Yes | Yes | Medium |
| ReAct | 6/10 | Medium | Yes | Partial | High |
| xAI Prompting | 9/10 | High | No | Yes | Low |
| Prompt Chaining | 6/10 | Medium | Yes | Yes | Medium-High |
| Few-Shot | 9/10 | High | Yes | Yes | Low-Medium |
| Self-Consistency | 5/10 | Low | Yes | Yes | High |
| Tree of Thoughts | 4/10 | Low | Yes | Partial | Very High |
| Chain-of-Verification | 6/10 | Medium | Yes | Yes | High |
| Skeleton-of-Thought | 6/10 | Medium | Yes | Yes | Medium |
| Claude Skills | 5/10 | High | Yes | No | Low |

---

*Part of Prompt Research Orchestrator Framework*