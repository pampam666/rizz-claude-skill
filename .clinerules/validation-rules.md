# Validation Rules

Defines validation standards for Cline Skill Builder to ensure all created skills comply with Cline documentation and Anthropic best practices.

## Overview

All skills created by Cline Skill Builder must pass validation checks before being considered complete. This document defines those checks and their requirements.

## Validation Categories

### 1. Structure Validation

#### 1.1 Directory Structure
**Check**: `directory_structure`

| Requirement | Status | Message |
|-------------|--------|---------|
| Skill directory exists | PASS/FAIL | "Skill directory must exist" |
| SKILL.md file present | PASS/FAIL | "SKILL.md is required" |
| Optional subfolders valid | PASS/WARN | "Subfolders should be: scripts/, templates/, docs/" |

**Implementation**:
```python
def validate_directory_structure(skill_path: str) -> ValidationResult:
    checks = []
    
    # Required: SKILL.md
    skill_md = Path(skill_path) / "SKILL.md"
    checks.append(("SKILL.md exists", skill_md.exists()))
    
    # Optional: subfolders
    valid_subfolders = {"scripts", "templates", "docs"}
    actual_subfolders = {d.name for d in Path(skill_path).iterdir() if d.is_dir()}
    invalid = actual_subfolders - valid_subfolders
    if invalid:
        checks.append(("Valid subfolders", False, f"Invalid subfolders: {invalid}"))
    
    return checks
```

---

### 2. YAML Frontmatter Validation

#### 2.1 Required Fields
**Check**: `yaml_frontmatter_required`

| Field | Requirement | Status | Message |
|-------|-------------|--------|---------|
| `name` | Must be present | PASS/FAIL | "YAML frontmatter must include 'name' field" |
| `description` | Must be present | PASS/FAIL | "YAML frontmatter must include 'description' field" |

#### 2.2 Field Format
**Check**: `yaml_field_format`

| Field | Requirement | Status | Message |
|-------|-------------|--------|---------|
| `name` | kebab-case, no spaces | PASS/WARN | "Skill name should use kebab-case" |
| `description` | Non-empty, descriptive | PASS/WARN | "Description should be descriptive" |
| `version` | SemVer format | PASS/WARN | "Version should follow semver (e.g., 1.0.0)" |

#### 2.3 Claude.ai Compatibility (CRITICAL)
**Check**: `claude_ai_yaml_compatibility`

Based on official Anthropic skills repository (https://github.com/anthropics/skills):

| Requirement | Status | Message |
|-------------|--------|---------|
| Only `name` and `description` fields | PASS/FAIL | "Claude.ai only supports name and description fields" |
| `description` must be unquoted single-line | PASS/FAIL | "Description must be unquoted single-line text" |
| No `version`, `author`, or `tags` fields | PASS/FAIL | "Remove version, author, tags - not supported by Claude.ai" |
| No literal block scalars (`\|`) | PASS/FAIL | "Do not use YAML literal block scalars (|)" |
| No folded block scalars (`>`) | PASS/FAIL | "Do not use YAML folded block scalars (>)" |
| No multi-line descriptions | PASS/FAIL | "Multi-line descriptions cause parsing errors" |

**Official Format** (from anthropics/skills repository):
```yaml
---
name: skill-name
description: Single line description without quotes. Keywords include keyword1, keyword2. Phrases include phrase1, phrase2. Context is when to use this skill. DOES NOT trigger for exclusion cases.
---
```

**Rejected Format** (causes "malformed YAML frontmatter" error):
```yaml
---
name: skill-name
description: "Quoted description"
version: 1.0.0
author: AuthorName
tags: [tag1, tag2]
---
```

**Implementation**:
```python
def validate_claude_ai_compatibility(frontmatter: dict) -> ValidationResult:
    checks = []
    
    # Only allowed fields
    allowed_fields = {"name", "description", "license"}
    extra_fields = set(frontmatter.keys()) - allowed_fields
    checks.append(("Only allowed fields", len(extra_fields) == 0, f"Remove: {extra_fields}"))
    
    # Check description format
    desc = frontmatter.get("description", "")
    checks.append(("description is string", isinstance(desc, str)))
    
    # Must not contain newlines (single-line)
    if isinstance(desc, str):
        checks.append(("description is single-line", "\n" not in desc))
    
    return checks
```

#### 2.3 Optional Fields
**Check**: `yaml_frontmatter_optional`

| Field | Requirement | Status | Message |
|-------|-------------|--------|---------|
| `author` | If present, non-empty | PASS/WARN | "Author should not be empty" |
| `tags` | If present, must be array | PASS/WARN | "Tags should be an array" |

**Implementation**:
```python
def validate_yaml_frontmatter(skill_md_path: str) -> ValidationResult:
    frontmatter = parse_yaml_frontmatter(skill_md_path)
    checks = []
    
    # Required fields
    checks.append(("name field present", "name" in frontmatter))
    checks.append(("description field present", "description" in frontmatter))
    
    # Format checks
    if "name" in frontmatter:
        name = frontmatter["name"]
        is_kebab = name.islower() and " " not in name and "_" not in name
        checks.append(("name uses kebab-case", is_kebab))
    
    if "description" in frontmatter:
        desc = frontmatter["description"]
        checks.append(("description is descriptive", len(desc) > 10))
    
    return checks
```

---

### 3. Naming Convention Validation

#### 3.1 Directory Names
**Check**: `directory_naming`

| Requirement | Status | Message |
|-------------|--------|---------|
| Lowercase only | PASS/FAIL | "Directory names must be lowercase" |
| No spaces | PASS/FAIL | "Directory names must not contain spaces" |
| Hyphens for separation | PASS/WARN | "Use hyphens (-) to separate words" |

#### 3.2 Skill Names
**Check**: `skill_naming`

| Requirement | Status | Message |
|-------------|--------|---------|
| Matches directory name | PASS/WARN | "Skill name should match directory name" |
| kebab-case format | PASS/FAIL | "Skill name must use kebab-case" |

---

### 4. Content Validation

#### 4.1 Required Sections
**Check**: `content_sections`

| Section | Requirement | Status | Message |
|---------|-------------|--------|---------|
| Overview/Description | Must be present | PASS/WARN | "Skill should have an overview section" |
| Usage/Instructions | Must be present | PASS/WARN | "Skill should include usage instructions" |

#### 4.2 Placeholder Check
**Check**: `placeholder_content`

| Requirement | Status | Message |
|-------------|--------|---------|
| No `{{placeholder}}` text | PASS/FAIL | "Remove all placeholder text before completion" |
| No `TODO` comments | PASS/WARN | "Resolve all TODO comments" |
| No `FIXME` comments | PASS/WARN | "Resolve all FIXME comments" |

**Implementation**:
```python
def validate_content(skill_md_path: str) -> ValidationResult:
    content = Path(skill_md_path).read_text()
    checks = []
    
    # Placeholder check
    has_placeholders = "{{" in content and "}}" in content
    checks.append(("No placeholders remaining", not has_placeholders))
    
    # TODO/FIXME check
    has_todo = "TODO" in content or "FIXME" in content
    checks.append(("No TODO/FIXME remaining", not has_todo))
    
    # Section checks
    checks.append(("Has overview section", "## Overview" in content or "# " in content))
    checks.append(("Has usage section", "## Usage" in content or "## How to Use" in content))
    
    return checks
```

---

### 5. Best Practices Validation

#### 5.1 Cline Documentation Compliance
**Check**: `cline_docs_compliance`

| Requirement | Status | Message |
|-------------|--------|---------|
| SKILL.md in root of skill directory | PASS/FAIL | "SKILL.md must be in skill directory root" |
| Valid YAML syntax | PASS/FAIL | "YAML frontmatter must be valid" |
| Clear trigger description | PASS/WARN | "Description should clearly define activation triggers" |

#### 5.2 Anthropic Best Practices
**Check**: `anthropic_best_practices`

| Requirement | Status | Message |
|-------------|--------|---------|
| Clear instructions | PASS/WARN | "Skill should have clear, actionable instructions" |
| Defined scope | PASS/WARN | "Skill should define its scope and limitations" |
| Error handling guidance | PASS/WARN | "Consider adding error handling guidance" |

---

## Validation Levels

### Critical (Must Pass)
These checks MUST pass for skill to be valid:
- SKILL.md exists
- Valid YAML frontmatter
- `name` field present
- `description` field present
- No placeholder text remaining

### Warning (Should Pass)
These checks SHOULD pass but skill can function without:
- kebab-case naming
- Optional YAML fields
- Section completeness
- Best practices adherence

---

## Validation Report Format

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
    },
    {
      "category": "content",
      "check": "no_placeholders",
      "status": "fail",
      "message": "Found 3 placeholder(s): {{NAME}}, {{DESCRIPTION}}, {{VERSION}}"
    }
  ],
  "recommendations": [
    "Replace placeholder {{NAME}} with actual skill name",
    "Consider adding an 'Error Handling' section"
  ]
}
```

---

## Integration

This validation system integrates with:
- `blueprint-execution.md` — Validation phase
- `state-management.md` — Recording validation results
- `skill-creator` sub-skill — Pre-completion validation

---

*Part of Cline Skill Builder Validation System*