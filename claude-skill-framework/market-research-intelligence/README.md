# Market Research Intelligence

A Claude Skill that transforms raw competitor data into structured strategic intelligence reports using the 3-Pillar Analysis Framework.

## Overview

This skill automates competitive intelligence analysis for the renewable energy market in Indonesia. It processes data from SEO tools (Semrush, Ahrefs), social media analytics, and web technology reports to generate actionable insights with team-specific recommendations.

### Target Users

Internal market research team with 3 specializations:
- **Sani** - Web & SEO Specialist
- **Aziz** - Content & Social Media Strategist
- **Pramono** - AI & Automation Engineer

## Installation

### Method 1: Manual Installation

1. Clone or download this repository
2. Copy the `market-research-intelligence` folder to your Claude skills directory:
   ```bash
   # For Claude Code
   cp -r market-research-intelligence ~/.claude/skills/
   
   # For Claude.ai (if applicable)
   # Upload the skill folder through the interface
   ```
3. Restart Claude or reload skills

### Method 2: Direct Path

Place the skill folder at:
```
~/.claude/skills/market-research-intelligence/
```

## Usage

### Basic Usage

Simply paste competitor data and request analysis:

```
Use market-research-intelligence skill to analyze this competitor data:

[Paste your CSV/JSON/text data here]
```

### Trigger Phrases

The skill automatically triggers when you use phrases like:
- "analyze this competitor"
- "generate market research report"
- "SEO gap analysis for..."
- "competitor intelligence report"
- "3-pillar analysis"
- "analyze tech stack"

### Supported Input Formats

| Format | Description | Example Sources |
|--------|-------------|-----------------|
| **CSV** | Tabular data with headers | Semrush, Ahrefs exports |
| **JSON** | Structured data objects | Meta Ads Library, APIs |
| **Plain Text** | Unstructured descriptions | Manual research notes |
| **Mixed** | Combination of formats | Compiled research |

### Required Data Fields

For comprehensive analysis, provide data from all three pillars:

**SEO & Web Metrics:**
- Domain Authority (DA) / Domain Rating (DR)
- Monthly organic traffic
- Referring domains / backlinks
- Top ranking keywords with volumes

**Content & Social Media:**
- Active platforms with follower counts
- Engagement rates (likes, comments, shares)
- Posting frequency
- Content themes

**Technology Stack:**
- CMS platform
- Analytics tools
- Marketing automation
- Chatbot/AI implementations

## Output Structure

The skill generates a structured Markdown report with 4 sections:

1. **Ringkasan Eksekutif (TL;DR)** - 3-5 key strategic insights
2. **Analisis Mendalam** - Table with strengths/weaknesses per pillar
3. **Analisis Lompang** - Gap analysis paragraph
4. **Rekomendasi Tindakan** - Team-specific actionable recommendations

### Output Language

All reports are generated in **professional Indonesian/Malay (Bahasa Indonesia)** for local market relevance.

## Examples

See the `examples/` directory for sample inputs and outputs:

- `sample-input-csv.txt` - SEO data from Ahrefs/Semrush
- `sample-input-json.txt` - Social media analytics JSON
- `sample-input-mixed.txt` - Combined format example
- `sample-output.md` - Complete analysis report

## Reference Documentation

The `references/` directory contains detailed documentation:

- `3-pillar-framework.md` - Complete framework explanation
- `keyword-gap-methodology.md` - SEO gap analysis methodology
- `ai-maturity-levels.md` - Tech stack maturity assessment

## Data Validation

Use the optional validation script to check input data format:

```bash
python scripts/data-validator.py your_data_file.csv
```

## Constraints & Quality Assurance

This skill follows strict quality rules:

- **Zero Hallucination**: Only uses facts from provided data
- **Objectivity**: States competitor superiority when evident
- **Specificity**: All recommendations include concrete numbers
- **Word Limit**: Maximum 800 words per report
- **Actionability**: Recommendations are sprint-task ready

## Industry Context

**Target Market:** Renewable Energy (Solar, Wind, Biogas) in Indonesia

**Competitive Landscape:**
- 50+ active solar installers
- Fragmented market with varying digital maturity
- Top 5 players control ~40% market share

**Key SEO Keywords:**
- "panel surya" (5,400/month)
- "harga panel surya" (2,900/month)
- "biaya instalasi panel surya" (3,500/month)

## Version

- **Version:** 1.0.0
- **Status:** Production Ready
- **Last Updated:** April 2026

## License

Part of the Claude Skill Framework for PT Daya Berkah Sentosa Nusantara.

---

*For questions or improvements, contact the Market Research Team.*