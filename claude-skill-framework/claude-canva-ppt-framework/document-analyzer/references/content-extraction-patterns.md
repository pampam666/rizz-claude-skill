# Content Extraction Patterns

This document outlines the patterns and best practices for extracting content from various document formats.
## Supported Formats
| Format | Extension | Extraction Method | Notes |
|--------|-----------|-------------------|-------|
| PDF | .pdf | Text extraction | May require OCR for scanned documents |
| Word | .docx | XML parsing | Best structure preservation |
| Text | .txt | Plain text read | Simple, no formatting |
| Markdown | .md | Markdown parsing | Preserves structure |
## Extraction Patterns
### Section Detection
```
PATTERN: Heading Detection
├── H1: Single # followed by text
├── H2: Single # followed by text
├── H3: Single # followed by text
├── H4-H6: Single # followed by text
```
### List Detection
```
PATTERN: List Items
├── Bulleted: Line starts with - or *
├── Numbered: Line starts with number + period
├── Lettered: Line starts with letter + period
├── Nested: Indented items under parent
```
### Data Extraction
```
PATTERN: Data Points
├── Percentages: \d+%\b|%\b| or \b[0-9]\b%
├── Currency: \$\d+\b|,\d]+\b|.\d+
├── Dates: Various date formats
├── Numbers: Integers, decimals, ranges
```
## Content Organization
### Hierarchy Mapping
```
DOCUMENT STRUCTURE → SLIDE STRUCTURE
├── Document Title → Title Slide
├── H1 Sections → Section Slides
├── H2 Subsections → Content Slides or Sub-slides
├── H3 Details → Bullet Points
├── Lists → Individual Slides or Slide Content
```
### Content Grouping Rules
1. **Title Slide**: Document title + subtitle + author/date
2. **Agenda Slide**: H1 sections as agenda items
3. **Content Slides**: Each H2 section becomes a slide
4. **Detail Slides**: H3 content grouped under parent H2
5. **Data Slides**: Statistics and data visualizations
6. **Conclusion Slide**: Summary + call to action
## Extraction Priority
### Must Extract
- Main title and subtitle
- Section headings (all levels)
- Key statistics and numbers
- Important quotes
- Action items and conclusions
### Should Extract
- Supporting details
- Examples and anecdotes
- Visual descriptions
- Secondary data
### Optional to Extract
- Metadata (author, date, version)
- References and citations
- Footnotes and endnotes
- Appendices
## Quality Indicators
### High Confidence (0.9-1.0)
- Clear document structure
- Explicit section headings
- Well-organized content
- Readable text
- Standard formatting
### Medium Confidence (0.7-0.8)
- Some structure present
- Mixed heading styles
- Moderate organization
- Some formatting inconsistencies
### Low Confidence (below 0.7)
- No clear structure
- Unorganized content
- Heavy text blocks
- Inconsistent formatting
- Scanned or image-based PDF
## Error Handling
### Common Issues
| Issue | Detection | Resolution |
|-------|-----------|----------|
| No readable text | Empty extraction result | Request different document |
| Mixed formats | Inconsistent patterns | Normalize and retry |
| Encoding issues | Garbled characters | Try UTF-8 detection |
| Missing sections | No headings found | Use paragraph breaks |
### Recovery Strategies
1. **Fallback**: Use paragraph-based extraction
2. **Manual Request**: Ask user for key points
3. **Best Effort**: Extract what's available, note gaps
4. **Retry**: Attempt alternative extraction method
---
*Part of Claude Canva PPT Framework - Reference Documentation*