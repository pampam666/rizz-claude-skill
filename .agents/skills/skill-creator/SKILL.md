---
name: skill-creator
description: Sub-skill that handles the actual generation of new Cline Skills. Activates when cline-skill-builder initiates skill creation process.
version: 1.0.0
author: Cline.Bot
parent: cline-skill-builder
tags: [sub-skill, skill-generation, scaffolding]
---

# Skill Creator

A sub-skill of Cline Skill Builder responsible for generating new Cline Skills with proper structure, validation, and content.

## Purpose

Skill Creator handles the technical aspects of skill generation:
- Directory structure creation
- SKILL.md file generation with valid YAML frontmatter
- Supporting file scaffolding (scripts, templates, docs)
- Content validation

## Activation

This sub-skill is activated by the parent `cline-skill-builder` skill when:
- User confirms a skill creation plan
- Blueprint execution phase begins
- Skill scaffolding is requested

## Process

### 1. Structure Generation
Creates the standard skill directory structure:
```
[skill-name]/
├── SKILL.md           # Main skill definition (required)
├── scripts/           # Helper scripts (optional)
├── templates/         # Reusable templates (optional)
└── docs/              # Documentation (optional)
```

### 2. SKILL.md Generation
Uses the `skill-skeleton.md` template to create properly formatted SKILL.md files with:
- Valid YAML frontmatter (name, description required)
- Skill overview and purpose
- Activation triggers
- Usage instructions
- Rules and constraints

### 3. Validation
Ensures generated skills comply with:
- Cline documentation standards
- Anthropic best practices
- Naming conventions (kebab-case)
- YAML frontmatter requirements

## Templates

Located in `templates/skill-skeleton.md`:
- Standard SKILL.md template
- Includes all required sections
- Placeholder system for customization

## Scripts

Located in `scripts/package-skill.py`:
- Packages skill directories into .skill files
- Creates shareable skill archives
- Generates installation manifests

## Output Rules

1. All skills output to `claude-skill-framework/[skill-name]/`
2. Never output directly to workspace root
3. Always validate before marking complete
4. Include installation instructions with each skill

## Quality Checklist

Before completing any skill generation:
- [ ] YAML frontmatter valid and complete
- [ ] Skill name uses kebab-case
- [ ] Description is precise and trigger-appropriate
- [ ] All sections properly filled
- [ ] No placeholder text remaining
- [ ] Installation instructions included

## Error Handling

If generation fails:
1. Report specific error to user
2. Do not leave partial files
3. Offer to retry or modify plan

## Dependencies

- Parent skill: `cline-skill-builder`
- Template: `templates/skill-skeleton.md`
- Script: `scripts/package-skill.py`