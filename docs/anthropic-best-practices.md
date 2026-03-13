# Anthropic Claude Skill Best Practices

A comprehensive summary of Anthropic Claude Skill best practices for building effective, reliable, and maintainable AI skills.

## Overview

This document compiles best practices from Anthropic's official documentation for creating Claude Skills that are effective, safe, and maintainable. These practices should be followed when creating any new skill.

---

## Core Principles

### 1. Clarity and Precision

**Be explicit and specific in instructions:**
- Use clear, unambiguous language
- Define exact formats and structures
- Specify what should happen in edge cases
- Avoid vague terms like "appropriately" or "as needed"

**Example:**
```markdown
# Bad
Handle errors appropriately.

# Good
When an API call fails:
1. Retry up to 3 times with exponential backoff
2. Log the error with timestamp and request ID
3. Return a structured error object with code and message
4. Notify the user if all retries fail
```

### 2. Scope Definition

**Clearly define what the skill does and does not do:**
- List specific capabilities
- Define boundaries and limitations
- Specify when the skill should NOT activate
- Document dependencies and prerequisites

**Template:**
```markdown
## Scope

### This skill WILL:
- Generate markdown documentation
- Create API reference guides
- Format code blocks with syntax highlighting

### This skill will NOT:
- Execute code
- Access external APIs
- Modify files outside the docs/ directory
```

### 3. Structured Output

**Define output formats explicitly:**
- Use templates for consistent output
- Specify file naming conventions
- Define required sections and their order
- Include examples of expected output

---

## Skill Structure Best Practices

### YAML Frontmatter

Every skill MUST include valid YAML frontmatter:

```yaml
---
name: skill-name
description: Precise description that controls when this skill activates
version: 1.0.0
author: Author Name
tags: [relevant, tags, here]
---
```

**Critical Fields:**

| Field | Required | Purpose |
|-------|----------|---------|
| `name` | Yes | Unique identifier for the skill (kebab-case) |
| `description` | Yes | Controls auto-activation; be precise about triggers |
| `version` | Recommended | Track skill versions using semver |
| `author` | Optional | Attribution and contact |
| `tags` | Optional | Categorization and searchability |

### Description Writing

The `description` field is critical for auto-activation. Write descriptions that:

1. **Define clear trigger conditions**
   ```yaml
   # Good
   description: Auto-triggers when user requests to create, build, or scaffold a new REST API endpoint with Express.js framework.
   
   # Bad
   description: Helps with API stuff.
   ```

2. **Be specific about contexts**
   ```yaml
   # Good
   description: Activates when working with TypeScript files that contain React component definitions.
   
   # Bad  
   description: For React components.
   ```

3. **Include action keywords**
   - Use verbs: create, generate, build, scaffold, analyze, transform
   - Include synonyms users might use

---

## Instruction Design

### Step-by-Step Instructions

Break complex tasks into clear, numbered steps:

```markdown
## Workflow

1. **Analyze** the input requirements
2. **Generate** a plan with file list
3. **Wait** for user confirmation
4. **Execute** the approved plan
5. **Validate** all created files
6. **Report** completion status
```

### Conditional Logic

Use clear conditional statements:

```markdown
## Error Handling

If validation fails:
  - Display specific error messages
  - Offer to fix automatically if possible
  - Request user guidance if uncertain

If file already exists:
  - Prompt user before overwriting
  - Offer to create backup
  - Suggest alternative names
```

### Examples and Templates

Always provide concrete examples:

```markdown
## Output Format

Generate files in this structure:

```
feature-name/
├── index.ts
├── types.ts
└── utils.ts
```

Example `index.ts`:
```typescript
export { Feature } from './types';
export { createFeature } from './utils';
```
```

---

## Safety and Reliability

### Input Validation

Always validate inputs before processing:

```markdown
## Prerequisites

Before executing:
1. Verify all required parameters are provided
2. Check file/directory permissions
3. Validate input formats match expectations
4. Confirm no conflicts with existing files
```

### Error Handling

Provide comprehensive error handling guidance:

```markdown
## Error Handling

### Recoverable Errors
- Missing optional parameters: Use defaults, log warning
- Minor validation failures: Prompt user for correction

### Critical Errors  
- Missing required parameters: Stop, request input
- Permission denied: Stop, inform user
- Dependency missing: Stop, provide installation instructions
```

### Idempotency

Design skills to be safely re-runnable:

```markdown
## Re-execution Safety

This skill is idempotent:
- Re-running will not duplicate content
- Existing files are detected and skipped or updated
- State is tracked to allow resumption
```

---

## Documentation Best Practices

### Self-Documenting Skills

Include documentation within the skill:

```markdown
## Usage

To use this skill, provide:
1. **Project name** - The name of your project (required)
2. **Output directory** - Where to create files (default: ./output)
3. **Template** - Which template to use (options: basic, advanced)

Example prompt:
"Create a new API project called 'user-service' in the ./projects folder using the advanced template"
```

### Changelog

Track changes within the skill file:

```markdown
## Changelog

### v1.2.0 (2024-01-15)
- Added support for custom templates
- Improved error messages
- Fixed validation bug

### v1.1.0 (2024-01-10)
- Initial release
```

---

## Performance Considerations

### Efficiency

Design for efficiency:

```markdown
## Performance

- Process files in batches when possible
- Cache results of expensive operations
- Use lazy loading for large datasets
- Provide progress indicators for long operations
```

### Resource Management

Be mindful of resources:

```markdown
## Resource Limits

- Maximum files per operation: 100
- Maximum file size: 10MB
- Timeout for external operations: 30 seconds
```

---

## Testing and Validation

### Self-Validation

Include validation checklists:

```markdown
## Validation Checklist

Before completing:
- [ ] All required files created
- [ ] No placeholder text remaining
- [ ] File permissions correct
- [ ] Dependencies satisfied
- [ ] Output matches expected format
```

### Quality Metrics

Define quality expectations:

```markdown
## Quality Standards

- Code must pass linting
- Documentation must be complete
- No TODO or FIXME comments
- All examples must be functional
```

---

## Integration with Cline

### Cline-Specific Features

Leverage Cline capabilities:

```markdown
## Cline Integration

This skill integrates with Cline features:
- File system operations via Cline tools
- Command execution for builds/tests
- Git operations for version control
- MCP servers for extended capabilities
```

### Workflow Integration

Define how the skill fits into larger workflows:

```markdown
## Workflow Position

This skill is typically used:
1. After: Project initialization
2. Before: Testing and deployment
3. Can be chained with: lint-setup, ci-config
```

---

## References

- [Anthropic Claude Documentation](https://docs.anthropic.com/claude/docs)
- [Cline Skills Documentation](https://docs.cline.bot/customization/skills)
- [Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/prompt-engineering)

---

*Part of Cline Skill Builder Documentation*