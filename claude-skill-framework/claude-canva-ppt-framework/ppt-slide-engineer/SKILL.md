---
name: ppt-slide-engineer
description: AUTO-TRIGGERS when document analysis is complete and slide creation is needed. Keywords include slide structure, slide outline, presentation flow, slide content. Phrases include create slides from analysis, build presentation structure, design slide deck. Context is second step of Canva PPT workflow after document-analyzer completes. DOES NOT trigger for raw document analysis, final Canva output, or non-slide tasks.
---

# PPT Slide Engineer

Transforms analyzed document content into a professional slide structure with titles, bullet points, speaker notes, and visual recommendations.

## Mission

Convert structured document analysis into a complete, presentation-ready slide deck blueprint with optimized content distribution, visual hierarchy, and professional formatting suitable for Canva implementation.

## Input Protocol

### Required Input
- `workflow_state.json` with `document_analyzer.output` populated
- `current_phase` must be "slide_engineering"
- Document analysis JSON with slide mapping

### Optional Input
- `brand_guidelines` - Color palette, fonts, logo specifications
- `presentation_style` - Corporate, creative, minimal, or custom
- `slide_preferences` - Max bullets per slide, preferred layouts

## Workflow

### Phase 1: Analysis Intake

```
VALIDATE:
├── Verify document analysis completeness
├── Check confidence score >= 0.80
├── Review slide mapping suggestions
└── Load brand guidelines if provided
```

### Phase 2: Slide Architecture

```
DESIGN:
├── Create title slide with main theme
├── Build agenda/overview slide
├── Structure content slides (3-5 bullets each)
├── Design data visualization slides
├── Create summary/conclusion slides
└── Add appendix if needed
```

### Phase 3: Content Optimization

```
OPTIMIZE:
├── Trim verbose content to bullet points
├── Apply 6x6 rule (max 6 lines, 6 words each)
├── Create hierarchical bullet structures
├── Extract key statistics for emphasis
└── Generate compelling headlines
```

### Phase 4: Visual Planning

```
PLAN:
├── Assign layout templates per slide type
├── Identify chart/graph requirements
├── Recommend image placements
├── Specify icon needs
└── Define color coding for themes
```

### Phase 5: Speaker Notes Generation

```
GENERATE:
├── Create talking points per slide
├── Add context for data points
├── Include transition suggestions
├── Note timing recommendations
└── Add engagement prompts
```

## Output Format

### Slide Structure Output

```json
{
  "slide_deck": {
    "metadata": {
      "title": "Presentation Title",
      "subtitle": "Subtitle",
      "total_slides": 12,
      "estimated_duration_minutes": 20,
      "style_preset": "corporate|creative|minimal",
      "created_timestamp": "ISO-8601-timestamp"
    },
    "brand_config": {
      "primary_color": "#0066CC",
      "secondary_color": "#00AA55",
      "accent_color": "#FF6600",
      "heading_font": "Montserrat",
      "body_font": "Open Sans",
      "logo_placement": "bottom-right"
    },
    "slides": [
      {
        "slide_number": 1,
        "slide_type": "title",
        "layout": "title-center",
        "content": {
          "title": "Main Presentation Title",
          "subtitle": "Supporting subtitle text",
          "background_recommendation": "gradient|image|solid"
        },
        "visual_spec": {
          "background_type": "gradient",
          "background_colors": ["#0066CC", "#004499"],
          "decorative_elements": ["geometric shapes", "subtle pattern"]
        }
      },
      {
        "slide_number": 2,
        "slide_type": "agenda",
        "layout": "bullets-left",
        "content": {
          "title": "Agenda",
          "bullets": [
            {"text": "Introduction to Topic", "level": 0},
            {"text": "Key Findings", "level": 0},
            {"text": "Analysis Results", "level": 0},
            {"text": "Recommendations", "level": 0},
            {"text": "Next Steps", "level": 0}
          ]
        },
        "speaker_notes": "Welcome everyone. Today we will cover five main areas starting with an introduction and ending with actionable next steps."
      },
      {
        "slide_number": 3,
        "slide_type": "content",
        "layout": "title-and-bullets",
        "content": {
          "title": "Section Heading",
          "bullets": [
            {"text": "First key point with impact", "level": 0},
            {"text": "Second key point", "level": 0},
            {"text": "Supporting detail", "level": 1},
            {"text": "Third key point", "level": 0}
          ],
          "callout": {
            "text": "Important statistic or quote",
            "position": "right"
          }
        },
        "visual_spec": {
          "icon_suggestions": ["checkmark", "arrow", "star"],
          "highlight_bullets": [0, 2]
        },
        "speaker_notes": "This section covers three main points. The first point is particularly important because..."
      },
      {
        "slide_number": 4,
        "slide_type": "data",
        "layout": "chart-focus",
        "content": {
          "title": "Performance Metrics",
          "chart_spec": {
            "chart_type": "bar",
            "title": "Q1-Q4 Performance",
            "data": {
              "labels": ["Q1", "Q2", "Q3", "Q4"],
              "datasets": [
                {
                  "label": "Revenue",
                  "values": [120, 145, 168, 195]
                }
              ]
            },
            "colors": ["#0066CC"]
          },
          "key_insight": "Revenue grew 62% year-over-year"
        },
        "speaker_notes": "Looking at our performance data, we see consistent growth across all quarters. The key insight here is our 62% growth."
      },
      {
        "slide_number": 5,
        "slide_type": "two-column",
        "layout": "split-content",
        "content": {
          "title": "Comparison View",
          "left_column": {
            "heading": "Before",
            "bullets": ["State 1", "State 2", "State 3"]
          },
          "right_column": {
            "heading": "After",
            "bullets": ["Improved State 1", "Improved State 2", "Improved State 3"]
          }
        },
        "speaker_notes": "Comparing the before and after states clearly shows the improvement in all three areas."
      },
      {
        "slide_number": 6,
        "slide_type": "conclusion",
        "layout": "summary",
        "content": {
          "title": "Key Takeaways",
          "bullets": [
            "Main conclusion 1",
            "Main conclusion 2",
            "Main conclusion 3"
          ],
          "call_to_action": "Next step or action item"
        },
        "speaker_notes": "To summarize, we have three key takeaways. The most important action item is..."
      }
    ]
  }
}
```

## Slide Type Reference

| Slide Type | Purpose | Recommended Layout |
|------------|---------|-------------------|
| `title` | Opening slide | Full-screen title with subtitle |
| `agenda` | Overview of topics | Vertical bullet list |
| `content` | Main information | Title with 3-5 bullets |
| `data` | Charts and statistics | Chart-focused with insight |
| `two-column` | Comparisons | Split view |
| `quote` | Testimonial/emphasis | Large quote with attribution |
| `image` | Visual showcase | Full or partial image |
| `timeline` | Sequential info | Horizontal or vertical timeline |
| `conclusion` | Summary | Key takeaways with CTA |
| `appendix` | Supporting material | Dense content acceptable |

## Content Rules

### Bullet Point Guidelines
- Maximum 6 bullets per slide
- Maximum 6 words per bullet (6x6 rule)
- Use parallel structure
- Start with action verbs when appropriate
- Avoid complete sentences

### Title Guidelines
- Clear and descriptive
- 3-8 words optimal
- Title case formatting
- Consistent style throughout

### Speaker Notes Guidelines
- 2-4 sentences per slide
- Include transition phrases
- Add timing cues
- Note emphasis points

## Error Handling

| Error Code | Description | Recovery Action |
|------------|-------------|-----------------|
| SLIDE_001 | Analysis input missing | Request document-analyzer completion |
| SLIDE_002 | Low confidence analysis | Request manual review of source |
| SLIDE_003 | Content overflow | Auto-split into multiple slides |
| SLIDE_004 | Brand config invalid | Use default styling |
| SLIDE_005 | Chart data incomplete | Generate text alternative |

## Dependencies

- `workflow_state.json` (read/write)
- Document analysis output from `document-analyzer`
- Brand guidelines (optional)

## Quality Checklist

- [ ] All analysis content mapped to slides
- [ ] Title slide created with main theme
- [ ] Agenda slide generated
- [ ] Each content slide has 3-5 bullets max
- [ ] Speaker notes added to all slides
- [ ] Visual specifications provided
- [ ] Chart requirements defined
- [ ] Conclusion slide with CTA included
- [ ] Total slide count appropriate
- [ ] Output saved to workflow_state.json

## Handoff Protocol

Upon successful completion:

1. Update `workflow_state.json`:
   ```json
   {
     "current_phase": "canva_automation",
     "ppt_slide_engineer": {
       "status": "complete",
       "output_path": "slide_structure.json",
       "total_slides": 12
     }
   }
   ```

2. Trigger `canva-ppt-automator` skill automatically

3. Pass slide structure to next skill

---

*Part of Claude Canva PPT Framework*