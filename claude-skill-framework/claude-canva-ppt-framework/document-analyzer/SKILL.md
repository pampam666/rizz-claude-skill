---
name: document-analyzer
description: AUTO-TRIGGERS when user uploads ANY document for PPT conversion. Keywords include analyze document, extract content, document structure, parse file. Phrases include turn this into slides, convert this document, make a presentation from. Context is first step of Canva PPT workflow after document upload. DOES NOT trigger for image-only files, audio files, or non-document formats.
---

# Document Analyzer

Extracts and structures all meaningful content from uploaded documents into a standardized analysis format ready for slide engineering.

## Mission

Transform any uploaded document (PDF, DOCX, TXT, MD) into a comprehensive, structured analysis that captures key themes, main points, supporting details, hierarchical structure, and visual recommendations for slide creation.

## Input Protocol

### Required Input
- Uploaded document file (PDF, DOCX, TXT, or MD format)
- Document content accessible for text extraction

### Optional Input
- `target_slide_count` - Desired number of slides (default: auto-detect)
- `focus_areas` - Specific topics or sections to prioritize
- `brand_guidelines` - Brand voice and tone reference

## Workflow

### Phase 1: Document Intake

```
PROCESS:
├── Identify document format
├── Extract raw text content
├── Detect document language
└── Calculate approximate word count
```

### Phase 2: Structure Analysis

```
ANALYZE:
├── Document hierarchy (headings, sections, subsections)
├── Content organization patterns
├── List structures and bullet points
├── Table data and statistics
└── Image/chart references
```

### Phase 3: Content Extraction

```
EXTRACT:
├── Main title and subtitle
├── Section headings (H1, H2, H3)
├── Key points per section
├── Supporting data and statistics
├── Quotes and callouts
└── Action items or conclusions
```

### Phase 4: Theme Identification

```
IDENTIFY:
├── Primary themes (3-5 main topics)
├── Secondary themes (supporting topics)
├── Narrative flow and progression
├── Target audience signals
└── Presentation purpose indicators
```

### Phase 5: Slide Mapping

```
MAP:
├── Group content into logical slide units
├── Assign slide types (title, content, data, conclusion)
├── Identify visual opportunities
├── Calculate optimal slide count
└── Generate content distribution plan
```

## Output Format

### Standard Analysis Output

```json
{
  "analysis_metadata": {
    "source_document": "filename.pdf",
    "document_type": "pdf",
    "word_count": 2500,
    "analysis_timestamp": "ISO-8601-timestamp",
    "confidence_score": 0.92
  },
  "document_overview": {
    "title": "Extracted or Inferred Title",
    "subtitle": "Subtitle if present",
    "primary_theme": "Main topic",
    "purpose": "inform|persuade|train|report",
    "target_audience": "Identified audience"
  },
  "content_structure": {
    "sections": [
      {
        "section_id": 1,
        "heading": "Section Title",
        "level": 1,
        "key_points": [
          "Main point 1",
          "Main point 2"
        ],
        "supporting_details": [
          "Detail 1",
          "Detail 2"
        ],
        "data_references": [
          {
            "type": "statistic",
            "value": "75%",
            "context": "Context for the statistic"
          }
        ],
        "recommended_slide_type": "content|data|quote|image"
      }
    ]
  },
  "slide_mapping": {
    "recommended_slide_count": 12,
    "slides": [
      {
        "slide_number": 1,
        "slide_type": "title",
        "title": "Presentation Title",
        "subtitle": "Subtitle text",
        "source_section": "document_overview"
      },
      {
        "slide_number": 2,
        "slide_type": "agenda",
        "title": "Agenda",
        "bullet_points": ["Topic 1", "Topic 2", "Topic 3"],
        "source_section": "section_1"
      }
    ]
  },
  "visual_recommendations": {
    "charts_needed": [
      {
        "slide_number": 5,
        "chart_type": "bar|pie|line",
        "data_source": "Section 3 statistics"
      }
    ],
    "images_suggested": [
      {
        "slide_number": 3,
        "image_type": "diagram|photo|icon",
        "description": "Suggested visual"
      }
    ]
  },
  "extraction_notes": {
    "content_gaps": ["Areas needing clarification"],
    "assumptions_made": ["List of assumptions"],
    "quality_indicators": {
      "structure_clarity": 0.85,
      "content_completeness": 0.90,
      "slide_readiness": 0.88
    }
  }
}
```

## Error Handling

| Error Code | Description | Recovery Action |
|------------|-------------|-----------------|
| DOC_001 | File format not supported | Request supported format (PDF, DOCX, TXT, MD) |
| DOC_002 | Text extraction failed | Try alternative extraction method or request text paste |
| DOC_003 | Insufficient content | Request additional source material |
| DOC_004 | Structure unclear | Request document outline or key points |
| DOC_005 | Language not supported | Notify user and request translation |

### Recovery Workflow

```
ON ERROR:
├── Log error with context
├── Attempt fallback extraction
├── If recoverable: continue with partial data
├── If unrecoverable: request user input
└── Update workflow_state.json with error status
```

## Dependencies

- Text extraction capability
- `workflow_state.json` (read/write)
- File system access for document reading

## Quality Checklist

- [ ] Document format identified and validated
- [ ] All sections extracted with headings
- [ ] Key points captured per section
- [ ] Statistics and data points preserved
- [ ] Slide mapping generated
- [ ] Visual recommendations provided
- [ ] Confidence score >= 0.80
- [ ] Output saved to workflow_state.json

## Handoff Protocol

Upon successful completion:

1. Update `workflow_state.json`:
   ```json
   {
     "current_phase": "slide_engineering",
     "document_analyzer": {
       "status": "complete",
       "output_path": "analysis_output.json",
       "confidence_score": 0.92
     }
   }
   ```

2. Trigger `ppt-slide-engineer` skill automatically

3. Pass analysis output to next skill

---

*Part of Claude Canva PPT Framework*