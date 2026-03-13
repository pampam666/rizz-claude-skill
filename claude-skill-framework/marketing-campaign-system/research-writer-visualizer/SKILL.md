---
name: research-writer-visualizer
description: AUTO-TRIGGERS when campaign strategy is complete and research document is needed. Keywords include research document, market research report, create document, visualizations, data presentation. Phrases include write research document, create market report, generate visualizations, build research report. Context is fourth phase of marketing campaign workflow after strategy development. DOES NOT trigger for strategy development, content creation, or article writing.
---

# Research Writer and Visualizer

Creates professional 25-40 page research documents with 5+ data visualizations, written in brand-matched tone.

## Mission

Transform research artifacts and strategy into a comprehensive, professionally formatted research document with charts, graphs, and visual data representations suitable for stakeholder presentation.

## Input Protocol

### Required Input
- `workflow_state.json` with:
  - `brand_dna` populated
  - `research_artifacts` populated
  - `strategy_artifacts` populated
  - `current_phase` = "research_writing"

## Document Structure

### Page Count: 25-40 pages

| Section | Pages | Content |
|---------|-------|---------|
| Cover Page | 1 | Title, branding |
| Executive Summary | 2-3 | Key findings |
| Market Overview | 4-6 | Size, segmentation |
| Competitive Analysis | 5-7 | Competitor profiles |
| Industry Trends | 3-5 | Emerging patterns |
| Target Audience | 4-6 | Personas, journey |
| Recommendations | 3-5 | Strategic advice |
| Appendix | 2-4 | Sources, methodology |

## Visualization Requirements

Minimum 5 visualizations required:
1. Market Size Chart (TAM/SAM/SOM)
2. Competitor Positioning Matrix
3. Trend Timeline
4. Audience Demographics
5. Channel Mix Pie Chart

## Output Schema

```json
{
  "deliverables": {
    "research_document_path": "/path/to/Market_Research_Document.docx",
    "document_metadata": {
      "page_count": 32,
      "word_count": 8500,
      "visualizations": 6,
      "sections": 9
    }
  }
}
```

## Dependencies

- `brand-dna-extractor`
- `market-research-agent`
- `campaign-strategy-agent`
- `scripts/create_visualizations.js`
- workflow_state.json (read/write)

## Quality Checklist

- [ ] 25-40 pages generated
- [ ] All sections complete
- [ ] 5+ visualizations included
- [ ] Brand tone applied
- [ ] Data sources cited
- [ ] workflow_state.json updated

---

*Part of Multi-Agent Marketing Campaign System*