# Cline Foundation Documentation

Comprehensive documentation for the Cline Foundation setup in this workspace.

---

## Table of Contents

1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Cline Skills](#cline-skills)
4. [Workflow Rules](#workflow-rules)
5. [Validation Standards](#validation-standards)
6. [Best Practices](#best-practices)
7. [Getting Started](#getting-started)

---

## Overview

### What is Cline Foundation?

Cline Foundation is a structured workspace configuration that enables AI-assisted development through Cline (an AI coding assistant). This foundation provides:

- **Standardized Workflows**: Plan → Confirm → Act pattern for all operations
- **Validation System**: Ensures quality and compliance for generated skills
- **State Management**: Tracks progress across multi-step operations
- **Best Practices**: Guidelines based on Anthropic's recommendations

### Purpose

This workspace is designed to:

1. Create and manage Cline Skills efficiently
2. Enforce quality through validation rules
3. Provide reproducible workflows
4. Maintain state across complex operations

---

## Project Structure

```
d:\CLAUDE-SKILL\Campaign\
│
├── .clinerules/                          # Cline configuration & rules
│   ├── validation-rules.md               # Skill validation standards
│   └── workflows/                        # Workflow definitions
│       ├── blueprint-execution.md        # Plan → Confirm → Act workflow
│       ├── state-management.md           # State tracking rules
│       └── workflow_state.json           # Current workflow state
│
├── docs/                                 # Additional documentation
│   └── anthropic-best-practices.md       # Anthropic Claude best practices
│
├── mcp-servers/                          # MCP server configurations
│   ├── context7-mcp/                     # Context7 MCP server
│   └── filesystem-mcp/                   # Filesystem MCP server
│
└── CLINE_FOUNDATION.md                   # This documentation
```

### Directory Descriptions

| Directory | Purpose |
|-----------|---------|
| `.clinerules/` | Contains all Cline-specific configuration, validation rules, and workflow definitions |
| `docs/` | Additional documentation and reference materials |
| `mcp-servers/` | Model Context Protocol server configurations |

---

## Cline Skills

### What are Cline Skills?

Cline Skills are reusable instruction sets that extend Cline's capabilities. Each skill is defined in a `SKILL.md` file with YAML frontmatter that controls when the skill auto-activates.

### Skill Architecture

```mermaid
flowchart TD
    subgraph SkillStructure["Skill Structure"]
        A[SKILL.md] --> B[YAML Frontmatter]
        A --> C[Markdown Content]
        B --> D[name]
        B --> E[description]
        C --> F[Mission]
        C --> G[Input Protocol]
        C --> H[Workflow]
        C --> I[Output Format]
        C --> J[Error Handling]
    end
    
    subgraph Optional["Optional Components"]
        K[scripts/]
        L[templates/]
        M[references/]
    end
    
    SkillStructure --> Optional
```

### Skill Directory Structure

```
skill-name/
├── SKILL.md              # Required: Main skill definition
├── scripts/              # Optional: Automation scripts
│   ├── script.py
│   └── script.js
├── templates/            # Optional: File templates
│   └── template.md
└── references/           # Optional: Reference documentation
    └── frameworks.md
```

### Skill Activation Mechanism

```mermaid
sequenceDiagram
    participant U as User
    participant C as Cline
    participant S as Skill System
    participant SK as Skill
    
    U->>C: Send message
    C->>S: Check for matching skills
    S->>S: Parse description keywords
    S->>S: Match against user input
    
    alt Match Found
        S->>SK: Activate skill
        SK->>C: Provide instructions
        C->>U: Execute with skill context
    else No Match
        C->>U: Process normally
    end
```

### Description-Based Activation

Skills auto-activate based on their `description` field:

| Component | Purpose | Example |
|-----------|---------|---------|
| **Keywords** | Single words that trigger | `brand dna`, `marketing`, `campaign` |
| **Phrases** | Multi-word expressions | `analyze this website`, `create campaign` |
| **Context** | When to activate | `first phase of marketing campaign` |
| **Exclusion** | When NOT to activate | `DOES NOT trigger for general web scraping` |

### Skill Types

```mermaid
mindmap
  root((Skill Types))
    Agent Skills
      Autonomous execution
      Multi-step workflows
      State management
    Utility Skills
      Single purpose
      Quick actions
      Format conversion
    Orchestrator Skills
      Coordinate agents
      Manage workflows
      Handle handoffs
    Validator Skills
      Quality checks
      Compliance verification
      Report generation
```

### Creating Skills

To create a new skill in this workspace:

1. **Define Purpose**: Clearly identify what the skill should do
2. **Choose Name**: Use kebab-case (e.g., `my-skill-name`)
3. **Write Description**: Include keywords, phrases, context, and exclusions
4. **Structure Content**: Follow the skill template
5. **Add Components**: Include scripts, templates, or references as needed
6. **Validate**: Ensure all validation checks pass

### Skill Communication Pattern

```mermaid
flowchart LR
    subgraph Input["Input Protocol"]
        A[Required Input]
        B[Optional Input]
    end
    
    subgraph Processing["Skill Processing"]
        C[Validate Input]
        D[Execute Workflow]
        E[Generate Output]
    end
    
    subgraph Output["Output Protocol"]
        F[Files Created]
        G[State Updated]
        H[Report Generated]
    end
    
    Input --> Processing --> Output
```

### Best Practices for Skills

| Practice | Description |
|----------|-------------|
| **Single Responsibility** | Each skill should do one thing well |
| **Clear Triggers** | Description should precisely define activation conditions |
| **Explicit Inputs** | Document all required and optional inputs |
| **Structured Outputs** | Define exact output formats |
| **Error Handling** | Include recovery procedures |
| **Idempotency** | Skills should be safely re-runnable |

---

## Workflow Rules

### Core Pattern: Plan → Confirm → Act

All operations in this workspace follow the **Plan → Confirm → Act** pattern to ensure quality and user control.

```mermaid
flowchart LR
    subgraph PLAN["PLAN MODE"]
        A[User Request] --> B[Analyze Requirements]
        B --> C[Create Plan]
        C --> D[Present Plan]
    end
    
    subgraph DECISION{"Decision"}
        D --> E{User Confirms?}
    end
    
    subgraph ACT["ACT MODE"]
        E -->|YES| F[Execute Plan]
        F --> G[Create Files]
        G --> H[Validate Output]
    end
    
    subgraph COMPLETE["Complete"]
        H --> I[Report Results]
    end
    
    E -->|NO/Modify| B
```

### Workflow Phases

The workflow operates in distinct phases with clear transitions:

```mermaid
stateDiagram-v2
    [*] --> PENDING: Initialize
    PENDING --> PLAN: Start Workflow
    
    state PLAN {
        [*] --> Analyze
        Analyze --> CreatePlan
        CreatePlan --> WaitForConfirm
    }
    
    PLAN --> ACT: User Confirms
    PLAN --> CANCELLED: User Rejects
    
    state ACT {
        [*] --> CreateStructure
        CreateStructure --> GenerateFiles
        GenerateFiles --> [*]
    }
    
    ACT --> VALIDATION: Files Created
    ACT --> ERROR: Creation Failed
    
    state VALIDATION {
        [*] --> CheckYAML
        CheckYAML --> CheckContent
        CheckContent --> CheckNaming
        CheckNaming --> [*]
    }
    
    VALIDATION --> COMPLETE: All Checks Pass
    VALIDATION --> ERROR: Critical Failure
    
    ERROR --> ACT: Retry
    ERROR --> CANCELLED: User Cancels
    
    COMPLETE --> [*]: Success
    CANCELLED --> [*]: Cancelled
```

### State Transitions

```mermaid
flowchart TD
    subgraph States
        PENDING[(PENDING)]
        PLAN[(PLAN)]
        ACT[(ACT)]
        VALIDATION[(VALIDATION)]
        COMPLETE[(COMPLETE)]
        ERROR[(ERROR)]
        CANCELLED[(CANCELLED)]
    end
    
    PENDING -->|"Workflow initialized"| PLAN
    PLAN -->|"User confirms plan"| ACT
    PLAN -->|"User rejects plan"| CANCELLED
    ACT -->|"All files created"| VALIDATION
    ACT -->|"File creation fails"| ERROR
    VALIDATION -->|"All checks pass"| COMPLETE
    VALIDATION -->|"Critical check fails"| ERROR
    ERROR -->|"Retry requested"| ACT
    ERROR -->|"User cancels"| CANCELLED
    
    style COMPLETE fill:#90EE90
    style ERROR fill:#FFB6C1
    style CANCELLED fill:#D3D3D3
```

### State Management

Workflow state is tracked in `workflow_state.json`:

```mermaid
classDiagram
    class WorkflowState {
        +string schema_version
        +string workflow_id
        +string blueprint_name
        +string current_phase
        +string status
        +FileEntry[] created_files
        +ValidationResult[] validation_results
        +Error[] errors
        +Metadata metadata
    }
    
    class FileEntry {
        +string path
        +string status
        +string timestamp
    }
    
    class ValidationResult {
        +string check
        +string status
        +string message
    }
    
    class Error {
        +string phase
        +string message
        +string timestamp
        +bool recoverable
    }
    
    class Metadata {
        +string created_at
        +string updated_at
        +string author
        +string parent_workflow
    }
    
    WorkflowState "1" *-- "many" FileEntry
    WorkflowState "1" *-- "many" ValidationResult
    WorkflowState "1" *-- "many" Error
    WorkflowState "1" *-- "1" Metadata
```

### State Schema

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
      "recoverable": true
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

---

## Validation Standards

All skills created in this workspace must pass validation checks before being considered complete.

### Validation Categories

```mermaid
mindmap
  root((Validation))
    Structure
      Directory exists
      SKILL.md present
      Valid subfolders
    YAML Frontmatter
      name field
      description field
      Claude.ai compatibility
    Naming Convention
      Lowercase directories
      kebab-case names
      No spaces
    Content
      No placeholders
      No TODO/FIXME
      Required sections
    Best Practices
      Clear instructions
      Defined scope
      Error handling
```

### YAML Frontmatter Requirements

#### Required Fields

| Field | Requirement | Example |
|-------|-------------|---------|
| `name` | Must be present, kebab-case | `skill-name` |
| `description` | Must be present, single-line | `Auto-triggers when...` |

#### Claude.ai Compatibility (Critical)

```mermaid
flowchart TD
    subgraph Valid["✓ Valid Format"]
        A1["name: skill-name"]
        A2["description: Single line text"]
    end
    
    subgraph Invalid["✗ Invalid Format"]
        B1["version: 1.0.0"]
        B2["author: Name"]
        B3["tags: [tag1, tag2]"]
        B4["Multi-line descriptions"]
        B5["Quoted descriptions"]
    end
    
    Valid --> |"Accepted"| C[(Claude.ai)]
    Invalid -->|"Rejected"| D["Malformed YAML Error"]
```

**Official Format:**
```yaml
---
name: skill-name
description: Single line description without quotes. Keywords include keyword1, keyword2. Phrases include phrase1, phrase2. Context is when to use this skill. DOES NOT trigger for exclusion cases.
---
```

**Rejected Format:**
```yaml
---
name: skill-name
description: "Quoted description"
version: 1.0.0
author: AuthorName
tags: [tag1, tag2]
---
```

### Validation Levels

```mermaid
pie title Validation Check Priority
    "Critical (Must Pass)" : 5
    "Warning (Should Pass)" : 10
```

| Level | Checks | Behavior |
|-------|--------|----------|
| **Critical** | SKILL.md exists, Valid YAML, name present, description present, No placeholders | Must pass for skill to be valid |
| **Warning** | kebab-case naming, Optional YAML fields, Section completeness, Best practices | Should pass but skill can function |

### Validation Report Format

```json
{
  "skill_name": "example-skill",
  "validation_timestamp": "ISO-8601-timestamp",
  "overall_status": "pass|fail|warning",
  "summary": {
    "total_checks": 15,
    "passed": 12,
    "failed": 1,
    "warnings": 2
  },
  "results": [
    {
      "category": "yaml_frontmatter",
      "check": "name_field_present",
      "status": "pass",
      "message": "name field found: 'example-skill'"
    }
  ],
  "recommendations": [
    "Consider adding an 'Error Handling' section"
  ]
}
```

---

## Best Practices

### Core Principles

```mermaid
mindmap
  root((Best Practices))
    Clarity
      Explicit instructions
      Define exact formats
      Specify edge cases
    Scope
      List capabilities
      Define boundaries
      Document limitations
    Output
      Use templates
      Specify file naming
      Define required sections
    Safety
      Validate inputs
      Handle errors
      Design for idempotency
```

### Skill Structure Template

```markdown
---
name: skill-name
description: Precise description that controls when this skill activates
---

# Skill Title

Brief description of what this skill does.

## Mission

Clear statement of the skill's purpose.

## Input Protocol

### Required Input
- Item 1
- Item 2

### Optional Input
- Item 3

## Workflow

1. Step 1
2. Step 2
3. Step 3

## Output Format

Description of expected output.

## Error Handling

How errors are handled.

## Quality Checklist

- [ ] Checklist item 1
- [ ] Checklist item 2
```

### Description Writing Guidelines

The `description` field controls auto-activation:

```mermaid
flowchart LR
    subgraph Good["✓ Good Description"]
        A1["Specific trigger conditions"]
        A2["Clear context"]
        A3["Action keywords"]
        A4["Exclusion cases"]
    end
    
    subgraph Bad["✗ Bad Description"]
        B1["Vague terms"]
        B2["Unclear context"]
        B3["Missing triggers"]
    end
    
    Good --> C["Proper Activation"]
    Bad --> D["Unpredictable Behavior"]
```

**Example:**
```yaml
# Good
description: AUTO-TRIGGERS when user provides ANY company URL for marketing analysis. Keywords include brand dna, brand voice. Phrases include analyze this website. Context is first phase of marketing campaign. DOES NOT trigger for general web scraping.

# Bad
description: Helps with brand stuff.
```

### Error Handling Pattern

```mermaid
flowchart TD
    A[Operation] --> B{Success?}
    B -->|Yes| C[Continue]
    B -->|No| D{Recoverable?}
    D -->|Yes| E[Log Warning]
    E --> F[Use Default]
    F --> C
    D -->|No| G[Stop]
    G --> H[Request User Input]
```

---

## Getting Started

### How to Use This Foundation

```mermaid
flowchart TD
    A[Start] --> B[Open Workspace in VS Code]
    B --> C[Ensure Cline Extension Installed]
    C --> D[Review .clinerules/ Configuration]
    D --> E[Understand Workflow Patterns]
    E --> F[Begin Development]
```

### Creating a New Skill

1. **Initiate Request**: Describe the skill you want to create
2. **Review Plan**: Cline will present a detailed plan in PLAN MODE
3. **Confirm**: Reply "YES" to approve the plan
4. **Toggle to ACT MODE**: Switch modes to execute
5. **Validate**: Review validation results
6. **Iterate**: Make adjustments if needed

### Workflow Commands

```mermaid
sequenceDiagram
    participant U as User
    participant C as Cline
    participant S as State File
    participant V as Validator
    
    U->>C: Request skill creation
    C->>S: Initialize state (PENDING)
    C->>U: Present plan (PLAN MODE)
    U->>C: Confirm plan
    C->>S: Update state (ACT)
    C->>C: Create files
    C->>S: Record created files
    C->>S: Update state (VALIDATION)
    C->>V: Run validation checks
    V->>S: Record results
    alt All checks pass
        S->>C: Update state (COMPLETE)
        C->>U: Report success
    else Checks fail
        S->>C: Update state (ERROR)
        C->>U: Report failures
    end
```

### File Location Rules

| Type | Location |
|------|----------|
| Configuration | `.clinerules/` |
| Documentation | `docs/` |
| MCP Servers | `mcp-servers/` |
| Workflow State | `.clinerules/workflows/workflow_state.json` |

---

## Quick Reference

### Workflow Phases

| Phase | Purpose | User Action Required |
|-------|---------|---------------------|
| PENDING | Initialized | None |
| PLAN | Requirements gathering | Review & confirm |
| ACT | Execute plan | None (auto) |
| VALIDATION | Quality checks | None (auto) |
| COMPLETE | Finished | None |
| ERROR | Failed | Retry or cancel |

### Status Codes

| Status | Description |
|--------|-------------|
| `pending` | Waiting to start |
| `in_progress` | Currently executing |
| `complete` | Successfully finished |
| `error` | Failed with errors |
| `cancelled` | User cancelled |

### Validation Checklist

- [ ] SKILL.md exists
- [ ] Valid YAML frontmatter
- [ ] `name` field present (kebab-case)
- [ ] `description` field present (single-line)
- [ ] No placeholder text (`{{...}}`)
- [ ] No TODO/FIXME comments
- [ ] Directory names use kebab-case

---

## References

- [Anthropic Claude Documentation](https://docs.anthropic.com/claude/docs)
- [Cline Skills Documentation](https://docs.cline.bot/customization/skills)
- [Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [Mermaid Documentation](https://mermaid.js.org/)

---

*Part of Cline Foundation Documentation*