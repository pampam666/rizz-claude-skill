---
name: canva-ppt-automator
description: AUTO-TRIGGERS when slide structure is ready for Canva implementation. Keywords include canva, canva ppt, canva presentation, canva design, automate canva. Phrases include create in canva, build canva presentation, make canva slides, implement in canva. Context is third step of Canva PPT workflow after ppt-slide-engineer completes. DOES NOT trigger for slide structure creation, document analysis, or non-Canva platforms.
---

# Canva PPT Automator

Executes the slide structure in Canva by generating precise instructions, design specifications, and automation-ready configurations.

## Mission

Transform the engineered slide structure into a fully implementable Canva presentation by providing step-by-step creation instructions, design element specifications, and ready-to-use automation configurations.

## Input Protocol

### Required Input
- `workflow_state.json` with `ppt_slide_engineer.output` populated
- `current_phase` must be "canva_automation"
- Complete slide structure JSON

### Optional Input
- `canva_template_id` - Specific Canva template to use
- `brand_kit_id` - Canva brand kit identifier
- `export_format` - PDF, PPTX, or link (default: all)

## Workflow

### Phase 1: Structure Validation

```
VALIDATE:
├── Verify slide structure completeness
├── Check all required fields present
├── Validate color codes (hex format)
├── Confirm font availability in Canva
└── Load brand kit configuration
```

### Phase 2: Canva Mapping

```
MAP:
├── Convert slide types to Canva layouts
├── Match content to Canva elements
├── Identify Canva chart types needed
├── Map colors to brand kit
└── Select appropriate Canva templates
```

### Phase 3: Instruction Generation

```
GENERATE:
├── Step-by-step creation guide
├── Element placement coordinates
├── Text formatting specifications
├── Chart configuration details
└── Animation and transition suggestions
```

### Phase 4: Automation Config

```
CONFIGURE:
├── Generate API-ready JSON
├── Create bulk creation script
├── Define element hierarchy
├── Set up master slides
└── Configure export settings
```

### Phase 5: Quality Verification

```
VERIFY:
├── All slides have creation instructions
├── Design consistency maintained
├── Brand guidelines applied
├── Export options configured
└── Share settings defined
```

## Output Format

### Canva Implementation Package

```json
{
  "canva_implementation": {
    "metadata": {
      "presentation_title": "Presentation Title",
      "total_slides": 12,
      "template_base": "custom|template_id",
      "brand_kit_applied": true,
      "created_timestamp": "ISO-8601-timestamp"
    },
    "canva_settings": {
      "dimensions": {
        "width": 1920,
        "height": 1080,
        "unit": "px"
      },
      "default_font": "Montserrat",
      "brand_colors": {
        "primary": "#0066CC",
        "secondary": "#00AA55",
        "accent": "#FF6600",
        "text_dark": "#333333",
        "text_light": "#FFFFFF",
        "background": "#FFFFFF"
      }
    },
    "creation_instructions": [
      {
        "step": 1,
        "action": "create_presentation",
        "details": "Create new presentation in Canva with 1920x1080 dimensions"
      },
      {
        "step": 2,
        "action": "apply_brand",
        "details": "Apply brand kit colors and fonts to presentation"
      }
    ],
    "slides": [
      {
        "slide_number": 1,
        "slide_type": "title",
        "canva_layout": "Title and Subtitle",
        "creation_steps": [
          {
            "step": 1,
            "action": "add_layout",
            "layout_name": "Title and Subtitle"
          },
          {
            "step": 2,
            "action": "set_background",
            "type": "gradient",
            "colors": ["#0066CC", "#004499"],
            "direction": "diagonal"
          },
          {
            "step": 3,
            "action": "add_text",
            "element": "title",
            "content": "Main Presentation Title",
            "formatting": {
              "font": "Montserrat",
              "size": 72,
              "weight": "bold",
              "color": "#FFFFFF",
              "alignment": "center"
            }
          },
          {
            "step": 4,
            "action": "add_text",
            "element": "subtitle",
            "content": "Supporting subtitle text",
            "formatting": {
              "font": "Open Sans",
              "size": 32,
              "weight": "regular",
              "color": "#FFFFFF",
              "alignment": "center"
            }
          },
          {
            "step": 5,
            "action": "add_decorative",
            "type": "shapes",
            "elements": [
              {
                "shape": "circle",
                "size": 150,
                "color": "#FFFFFF",
                "opacity": 0.1,
                "position": {"x": 100, "y": 100}
              }
            ]
          }
        ]
      },
      {
        "slide_number": 2,
        "slide_type": "agenda",
        "canva_layout": "Bulleted List",
        "creation_steps": [
          {
            "step": 1,
            "action": "add_layout",
            "layout_name": "Title and Body Text"
          },
          {
            "step": 2,
            "action": "set_background",
            "type": "solid",
            "color": "#FFFFFF"
          },
          {
            "step": 3,
            "action": "add_text",
            "element": "title",
            "content": "Agenda",
            "formatting": {
              "font": "Montserrat",
              "size": 48,
              "weight": "bold",
              "color": "#0066CC"
            }
          },
          {
            "step": 4,
            "action": "add_bullets",
            "bullets": [
              "Introduction to Topic",
              "Key Findings",
              "Analysis Results",
              "Recommendations",
              "Next Steps"
            ],
            "formatting": {
              "font": "Open Sans",
              "size": 24,
              "color": "#333333",
              "bullet_style": "circle",
              "bullet_color": "#0066CC"
            }
          }
        ]
      },
      {
        "slide_number": 3,
        "slide_type": "content",
        "canva_layout": "Title and Bullets",
        "creation_steps": [
          {
            "step": 1,
            "action": "add_layout",
            "layout_name": "Title and Body Text"
          },
          {
            "step": 2,
            "action": "add_text",
            "element": "title",
            "content": "Section Heading",
            "formatting": {
              "font": "Montserrat",
              "size": 44,
              "weight": "bold",
              "color": "#0066CC"
            }
          },
          {
            "step": 3,
            "action": "add_bullets",
            "bullets": [
              {"text": "First key point with impact", "highlight": true},
              {"text": "Second key point", "highlight": false},
              {"text": "  Supporting detail", "highlight": false, "indent": 1},
              {"text": "Third key point", "highlight": true}
            ],
            "formatting": {
              "font": "Open Sans",
              "size": 22,
              "color": "#333333"
            }
          },
          {
            "step": 4,
            "action": "add_callout",
            "content": "Important statistic or quote",
            "position": "right",
            "style": {
              "background": "#0066CC",
              "text_color": "#FFFFFF",
              "font_size": 18,
              "padding": 20
            }
          }
        ]
      },
      {
        "slide_number": 4,
        "slide_type": "data",
        "canva_layout": "Chart",
        "creation_steps": [
          {
            "step": 1,
            "action": "add_layout",
            "layout_name": "Chart and Text"
          },
          {
            "step": 2,
            "action": "add_text",
            "element": "title",
            "content": "Performance Metrics"
          },
          {
            "step": 3,
            "action": "add_chart",
            "chart_type": "bar",
            "data": {
              "labels": ["Q1", "Q2", "Q3", "Q4"],
              "values": [120, 145, 168, 195]
            },
            "chart_config": {
              "title": "Q1-Q4 Performance",
              "bar_color": "#0066CC",
              "show_values": true,
              "show_grid": true
            }
          },
          {
            "step": 4,
            "action": "add_text",
            "element": "insight",
            "content": "Key Insight: Revenue grew 62% year-over-year",
            "formatting": {
              "font": "Open Sans",
              "size": 18,
              "weight": "bold",
              "color": "#00AA55"
            }
          }
        ]
      },
      {
        "slide_number": 5,
        "slide_type": "conclusion",
        "canva_layout": "Summary",
        "creation_steps": [
          {
            "step": 1,
            "action": "add_layout",
            "layout_name": "Title and Body Text"
          },
          {
            "step": 2,
            "action": "add_text",
            "element": "title",
            "content": "Key Takeaways"
          },
          {
            "step": 3,
            "action": "add_bullets",
            "bullets": [
              "Main conclusion 1",
              "Main conclusion 2",
              "Main conclusion 3"
            ]
          },
          {
            "step": 4,
            "action": "add_cta_box",
            "content": "Next step or action item",
            "style": {
              "background": "#FF6600",
              "text_color": "#FFFFFF",
              "size": "large",
              "alignment": "center"
            }
          }
        ]
      }
    ],
    "export_config": {
      "formats": ["pdf", "pptx", "link"],
      "pdf_settings": {
        "quality": "high",
        "include_notes": true
      },
      "share_settings": {
        "link_access": "view",
        "download_enabled": true
      }
    }
  }
}
```

## Canva Layout Reference

| Slide Type | Recommended Canva Layout | Alternative |
|------------|-------------------------|-------------|
| `title` | Title and Subtitle | Full Image Background |
| `agenda` | Bulleted List | Numbered List |
| `content` | Title and Body Text | Two Column |
| `data` | Chart | Chart and Text |
| `two-column` | Two Column | Comparison |
| `quote` | Quote | Testimonial |
| `image` | Full Image | Image and Text |
| `timeline` | Process | Timeline |
| `conclusion` | Summary | Call to Action |

## Design Specifications

### Typography Scale
| Element | Size (px) | Weight | Font |
|---------|-----------|--------|------|
| Title Slide | 72 | Bold | Heading Font |
| Slide Title | 44-48 | Bold | Heading Font |
| Subtitle | 28-32 | Regular | Body Font |
| Body Text | 22-24 | Regular | Body Font |
| Bullet Points | 20-22 | Regular | Body Font |
| Callout | 18-20 | Bold | Body Font |
| Caption | 14-16 | Regular | Body Font |

### Color Application
| Element | Color Usage |
|---------|-------------|
| Primary Background | White or Light Gray |
| Title Text | Primary Brand Color |
| Body Text | Dark Gray (#333333) |
| Accent Elements | Accent Color |
| Charts | Primary/Secondary Colors |
| Highlights | Accent Color |

## Error Handling

| Error Code | Description | Recovery Action |
|------------|-------------|-----------------|
| CANVA_001 | Slide structure missing | Request ppt-slide-engineer completion |
| CANVA_002 | Invalid color format | Convert to valid hex |
| CANVA_003 | Font not available | Substitute with Canva default |
| CANVA_004 | Chart data malformed | Generate text alternative |
| CANVA_005 | Layout not found | Use closest matching layout |

## Dependencies

- `workflow_state.json` (read/write)
- Slide structure from `ppt-slide-engineer`
- Canva account access (manual implementation)

## Quality Checklist

- [ ] All slides have creation steps
- [ ] Canva layouts mapped correctly
- [ ] Typography specifications complete
- [ ] Color codes validated
- [ ] Chart configurations defined
- [ ] Export settings configured
- [ ] Share settings specified
- [ ] Instructions are step-by-step clear
- [ ] Output saved to workflow_state.json

## Handoff Protocol

Upon successful completion:

1. Update `workflow_state.json`:
   ```json
   {
     "current_phase": "complete",
     "canva_ppt_automator": {
       "status": "complete",
       "output_path": "canva_implementation.json",
       "slides_created": 12,
       "export_ready": true
     }
   }
   ```

2. Provide user with:
   - Complete creation instructions
   - Canva implementation JSON
   - Direct link template (if applicable)

3. Trigger `validation-guardian` for final quality check

---

*Part of Claude Canva PPT Framework*