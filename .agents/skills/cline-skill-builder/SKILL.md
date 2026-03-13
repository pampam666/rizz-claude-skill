---
name: cline-skill-builder
description: Auto-triggers when user requests to create, build, scaffold, or generate any Cline Skill, Claude Skill, blueprint, or skill framework. Also triggers for skill-related setup, initialization, or packaging tasks.
version: 1.0.0
author: Cline.Bot
tags: [skill-builder, claude-skill, cline-skill, blueprint, scaffolding]
---

# Cline Skill Builder

A production-grade Cline Skill for creating, validating, and packaging Claude Skills according to official Cline documentation and Anthropic best practices.

## Overview

Cline Skill Builder is a persistent skill that transforms your workspace into a skill creation powerhouse. It enforces strict **Plan → Confirm → Act** workflow to ensure quality and consistency in every skill created.

## Capabilities

### 1. Skill Creation
- Generate complete skill directory structures
- Create properly formatted SKILL.md files with valid YAML frontmatter
- Scaffold supporting files (scripts, templates, documentation)

### 2. Skill Validation
- Verify YAML frontmatter compliance
- Check naming conventions (kebab-case)
- Validate against Cline documentation standards
- Ensure Anthropic best practices adherence

### 3. Skill Packaging
- Package skills into shareable .skill files
- Generate installation instructions
- Create skill manifests

## Activation Triggers

This skill automatically activates when the user:
- Requests to create a new Cline Skill or Claude Skill
- Asks to build or scaffold a skill framework
- Mentions "blueprint" in the context of skill creation
- Requests skill-related setup or initialization
- Wants to package an existing skill

## Workflow

### Phase 0: Foundation Setup
Initial setup creates the skill builder infrastructure:
```
cline-skill-builder/
├── SKILL.md
├── .agents/skills/
├── .clinerules/
└── docs/
```

### Phase 1: Blueprint Execution
Creates actual skills in dedicated output folder:
```
claude-skill-framework/
└── [skill-name]/
    ├── SKILL.md
    ├── scripts/
    ├── templates/
    └── docs/
```

## Rules

1. **Never create without confirmation** — Always present a plan first
2. **Use kebab-case** — All folder and skill names must use kebab-case
3. **Include YAML frontmatter** — Every SKILL.md must have valid frontmatter with `name` and `description`
4. **Professional English** — All output in clear, professional English
5. **Validate before completion** — Check against Cline docs and Anthropic best practices

## Sub-Skills

- **skill-creator**: Located in `.agents/skills/skill-creator/` — Handles the actual skill generation process

## Related Files

- `.clinerules/workflows/blueprint-execution.md` — Master orchestration workflow
- `.clinerules/workflows/state-management.md` — State handling rules
- `.clinerules/validation-rules.md` — Validation standards
- `docs/anthropic-best-practices.md` — Anthropic standards reference

## Usage

To create a new skill:
1. Describe the skill you want to create
2. Review the generated plan
3. Confirm with "YES" to proceed
4. Receive complete skill structure with instructions

## References

- [Cline Skills Documentation](https://docs.cline.bot/customization/skills)
- [Anthropic Claude Best Practices](https://docs.anthropic.com/claude/docs)