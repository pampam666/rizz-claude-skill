---
name: mother-orchestrator
description: AUTO-TRIGGERS for prompt engineering research requests. Keywords include prompt research, framework comparison, prompt analysis, LLM prompting study, prompt engineering comparison. Phrases include compare prompting frameworks, analyze prompt techniques, research prompt engineering, create comparison report. Context is entry point for all prompt research workflows. DOES NOT trigger for general coding tasks, file operations, or non-research requests.
---

# Mother Orchestrator

Central coordination skill that serves as the single user interface for all prompt engineering research requests.

## Mission

Orchestrate the complete prompt research workflow by receiving requests, generating TOC proposals, coordinating specialist skills, and delivering final reports.

## Activation Protocol

### Automatic Triggers
- User requests prompt framework comparison
- User mentions "prompt research" or "framework analysis"
- User provides GDrive links with prompt documentation
- User asks for "pros/cons" analysis of prompting techniques

### Manual Activation
Use this skill when you need to conduct research on prompt engineering frameworks.

## Workflow Phases

| Phase | Skill | Trigger Condition |
|-------|-------|-------------------|
| 1. TOC Proposal | mother-orchestrator | Request received |
| 2. Research | framework-researcher | TOC confirmed |
| 3. Analysis | comparison-analyst | Research complete |
| 4. Report | report-generator | Analysis complete |
| 5. Delivery | mother-orchestrator | Report complete |

## Input Protocol

### Required Input
- User request (natural language)
- Optional: GDrive links to prompt documentation

### Request Parsing

Extract from user request:
1. **Frameworks to compare** (e.g., "CoT vs ReAct")
2. **Specific metrics requested** (e.g., "ease of use", "thinking process")
3. **GDrive links** (if provided)
4. **Special requirements** (e.g., "include benchmarks", "APA citations")

## Phase 1: TOC Proposal Generation

### TOC Generation Rules

Always generate 3-5 TOC options with different structures:

**Option A: Comprehensive Academic**
- Executive Summary
- Literature Review
- Framework Descriptions
- Methodology
- Comparison Tables
- Benchmark Analysis
- Conclusions
- References

**Option B: Practitioner-Focused**
- Quick Reference
- Framework Overview
- Pros/Cons Tables
- Ease of Use Ratings
- Implementation Guide
- Recommendations

**Option C: Technical Deep-Dive**
- Technical Specifications
- LLM Thinking Process Analysis
- Token Efficiency
- Scalability Assessment
- Grok/Claude Compatibility
- Performance Benchmarks

**Option D: Executive Summary**
- Key Findings
- Comparison Matrix
- Recommendations
- Implementation Roadmap

**Option E: Research Paper Format**
- Abstract
- Introduction
- Background
- Methods
- Results
- Discussion
- Conclusion
- Bibliography

### TOC Presentation Format

```
I've generated 5 Table of Contents options for your research report.

**Option A: Comprehensive Academic** (15-20 pages)
Best for: Academic research, literature reviews
Structure: Executive Summary → Literature Review → Framework Descriptions → Methodology → Comparison Tables → Benchmark Analysis → Conclusions → References

**Option B: Practitioner-Focused** (8-12 pages)
Best for: Implementation decisions, team guides
Structure: Quick Reference → Framework Overview → Pros/Cons Tables → Ease of Use Ratings → Implementation Guide → Recommendations

**Option C: Technical Deep-Dive** (12-15 pages)
Best for: Engineering teams, performance optimization
Structure: Technical Specifications → LLM Thinking Process Analysis → Token Efficiency → Scalability Assessment → Grok/Claude Compatibility → Performance Benchmarks

**Option D: Executive Summary** (5-8 pages)
Best for: Decision makers, quick overviews
Structure: Key Findings → Comparison Matrix → Recommendations → Implementation Roadmap

**Option E: Research Paper Format** (20-25 pages)
Best for: Publications, academic submissions
Structure: Abstract → Introduction → Background → Methods → Results → Discussion → Conclusion → Bibliography

Please select an option (A, B, C, D, or E) or request modifications.
```

## Phase 2: Research Coordination

After TOC confirmation, delegate to `framework-researcher`:

```
<delegate to="framework-researcher">
<task>
Conduct research on the following frameworks: [list frameworks]
GDrive links to process: [list links or "none"]
Required sources: PromptingGuide.ai, Anthropic docs, academic papers
Output: research_artifacts in workflow_state.json
</task>
<context>
workflow_state.json path: [path to workflow_state.json]
Selected TOC: [option letter]
</context>
</delegate>
```

## Phase 3: Analysis Coordination

After research completion, delegate to `comparison-analyst`:

```
<delegate to="comparison-analyst">
<task>
Build comparison tables for: [list frameworks]
Required metrics: pros/cons, ease of use, LLM thinking process, scalability, Grok/Claude compatibility, Claude compatibility
Output: analysis_artifacts in workflow_state.json
</task>
<context>
workflow_state.json path: [path to workflow_state.json]
Research artifacts: [summary of available data]
</context>
</delegate>
```

## Phase 4: Report Coordination

After analysis completion, delegate to `report-generator`:

```
<delegate to="report-generator">
<task>
Generate DOCX report following TOC: [option letter]
Citation style: APA
Output: deliverables.report_path in workflow_state.json
</task>
<context>
workflow_state.json path: [path to workflow_state.json]
Selected TOC: [option structure]
Analysis artifacts: [summary of comparison data]
</context>
</delegate>
```

## Phase 5: Delivery

After report generation:

1. Validate report exists at `deliverables.report_path`
2. Present to user with summary:
   ```
   ## Research Report Complete
   
   **Report**: [filename].docx
   **Pages**: [count]
   **Frameworks Compared**: [list]
   **Sources Cited**: [count]
   
   **Key Findings**:
   - [Finding 1]
   - [Finding 2]
   - [Finding 3]
   
   Report saved to: [full path]
   ```

## State Management

### Initialize Workflow State

```json
{
  "workflow_id": "research-${timestamp}",
  "created_at": "${ISO-8601}",
  "status": {
    "current_phase": "toc_proposal",
    "overall_status": "in_progress",
    "completion_percentage": 0
  },
  "request": {
    "original_query": "${user query}",
    "frameworks_to_compare": ["${extracted frameworks}"],
    "gdrive_links": ["${extracted links}"],
    "special_requirements": ["${extracted requirements}"]
  }
}
```

### Update State After Each Phase

```json
{
  "status": {
    "current_phase": "${phase_name}",
    "completion_percentage": ${percentage}
  },
  "checkpoints": {
    "${checkpoint_name}": true
  }
}
```

## Error Handling

### Common Errors

| Error | Recovery |
|-------|----------|
| No frameworks identified | Ask user to specify frameworks |
| GDrive link invalid | Request alternative link or skip |
| Research insufficient | Expand search parameters |
| Report generation fails | Retry with minimal template |

### Error Logging

```json
{
  "errors": [
    {
      "code": "E001",
      "phase": "research",
      "message": "Source unavailable: PromptingGuide.ai",
      "timestamp": "${ISO-8601}",
      "recovery": "Used cached content"
    }
  ]
}
```

## Quality Checklist

- [ ] User request parsed correctly
- [ ] 3-5 TOC options generated
- [ ] User confirmation received
- [ ] framework-researcher delegated
- [ ] comparison-analyst delegated
- [ ] report-generator delegated
- [ ] Final report validated
- [ ] Delivery summary provided

## Example Usage

**Input:**
"Please analyse and create a comparison report of prompt engineering between Prompt A and B in pros/cons in table, ease of use, LLM Thinking process." (plus two GDrive links)

**Execution:**
1. Parse request: Frameworks=[Prompt A, Prompt B], Metrics=[pros/cons, ease of use, thinking process], GDrive=[link1, link2]
2. Generate 5 TOC options
3. Wait for user selection
4. Delegate to framework-researcher with GDrive links
5. Delegate to comparison-analyst with metrics
6. Delegate to report-generator with TOC
7. Deliver final .docx

---

*Part of Prompt Research Orchestrator Framework*