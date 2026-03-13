# Research Frameworks

Reference document containing research methodologies and frameworks for comprehensive market analysis.

## Market Analysis Frameworks

### 1. TAM/SAM/SOM Model

**Purpose**: Quantify market opportunity at three levels

```
TAM (Total Addressable Market)
├── Total market demand for a product/service
├── Theoretical maximum revenue opportunity
└── Example: $100B global software market

SAM (Serviceable Addressable Market)
├── Segment of TAM targeted by your products
├── Within geographical reach
└── Example: $30B US software market

SOM (Serviceable Obtainable Market)
├── Portion of SAM you can realistically capture
├── Based on resources, competition, positioning
└── Example: $500M (1.7% of SAM)
```

**Calculation Methods**:
- Top-down: Industry reports → segment percentages
- Bottom-up: Customer count × average revenue
- Value theory: Customer value × number of customers

### 2. Porter's Five Forces

**Purpose**: Analyze competitive intensity and attractiveness

```
                    ┌─────────────────────┐
                    │  THREAT OF NEW      │
                    │  ENTRANTS           │
                    │  (Barriers to Entry)│
                    └─────────┬───────────┘
                              │
┌─────────────────┐          │          ┌─────────────────┐
│  SUPPLIER       │          │          │  BUYER          │
│  POWER          │◄─────────┼─────────►│  POWER          │
│  (Input costs)  │          │          │  (Price sensitivity)
└─────────────────┘          │          └─────────────────┘
                              │
                    ┌─────────▼───────────┐
                    │  COMPETITIVE        │
                    │  RIVALRY            │
                    │  (Industry dynamics)│
                    └─────────┬───────────┘
                              │
                    ┌─────────▼───────────┐
                    │  THREAT OF          │
                    │  SUBSTITUTES        │
                    │  (Alternative solutions)
                    └─────────────────────┘
```

**Analysis Questions**:
1. Threat of New Entrants: Capital requirements? Regulations? Brand loyalty?
2. Supplier Power: Few suppliers? Unique inputs? Switching costs?
3. Buyer Power: Many alternatives? Price sensitivity? Switching costs?
4. Threat of Substitutes: Alternative solutions? Price-performance ratio?
5. Competitive Rivalry: Number of competitors? Industry growth rate? Fixed costs?

### 3. PESTEL Analysis

**Purpose**: Analyze macro-environmental factors

| Factor | Analysis Focus | Example Questions |
|--------|---------------|-------------------|
| **P**olitical | Government policies | Tax policies? Trade restrictions? Political stability? |
| **E**conomic | Economic conditions | GDP growth? Inflation? Interest rates? Unemployment? |
| **S**ocial | Cultural trends | Demographics? Lifestyle changes? Cultural attitudes? |
| **T**echnological | Tech innovations | R&D activity? Automation? Disruptive technologies? |
| **E**nvironmental | Ecological factors | Climate regulations? Sustainability trends? |
| **L**egal | Regulatory framework | Employment law? Consumer protection? Industry regulations? |

### 4. SWOT Analysis

**Purpose**: Identify internal and external factors

```
                    INTERNAL              EXTERNAL
                    (Company)             (Market)
              ┌─────────────────┬─────────────────┐
   POSITIVE   │    STRENGTHS    │  OPPORTUNITIES  │
   (Helpful)  │  - Core competencies  │  - Market trends  │
              │  - Resources    │  - Gaps in market│
              │  - Advantages   │  - Partnerships  │
              ├─────────────────┼─────────────────┤
   NEGATIVE   │   WEAKNESSES    │    THREATS      │
   (Harmful)  │  - Limitations  │  - Competition  │
              │  - Gaps         │  - Market decline│
              │  - Vulnerabilities │  - Regulations  │
              └─────────────────┴─────────────────┘
```

## Competitor Analysis Frameworks

### 1. Competitive Positioning Matrix

**Purpose**: Map competitors on key dimensions

```
                    HIGH PRICE
                        │
                        │    PREMIUM
                        │    LEADERS
                        │
        ┌───────────────┼───────────────┐
        │               │               │
LOW     │   CHALLENGERS │   NICHE       │ HIGH
VALUE   │               │   PLAYERS     │ VALUE
        │               │               │
        └───────────────┼───────────────┘
                        │
                        │    VALUE
                        │    LEADERS
                        │
                    LOW PRICE
```

### 2. Feature Comparison Matrix

**Purpose**: Compare product features across competitors

| Feature | Your Product | Competitor A | Competitor B | Competitor C |
|---------|-------------|--------------|--------------|--------------|
| Feature 1 | ✓ | ✓ | ✗ | ✓ |
| Feature 2 | ✓ | ✗ | ✓ | Partial |
| Feature 3 | ✓ | ✓ | ✓ | ✓ |
| Pricing | $$$ | $$ | $$$$ | $$ |
| Target | Enterprise | SMB | Enterprise | Mid-market |

### 3. Competitor Profiling Template

```yaml
competitor_profile:
  basic_info:
    name: ""
    founded: ""
    headquarters: ""
    employees: ""
    funding: ""
    
  market_position:
    market_share: ""
    positioning: ""
    target_audience: ""
    geographic_focus: ""
    
  product_analysis:
    core_features: []
    unique_capabilities: []
    gaps: []
    pricing_model: ""
    price_range: ""
    
  strengths:
    - ""
    - ""
    
  weaknesses:
    - ""
    - ""
    
  strategy:
    growth_strategy: ""
    recent_initiatives: []
    partnerships: []
    
  threat_level: "high|medium|low"
```

## Customer Research Frameworks

### 1. Buyer Persona Template

```yaml
buyer_persona:
  name: "Persona Name"
  role: "Job Title"
  demographics:
    age_range: ""
    education: ""
    company_size: ""
    industry: ""
    
  goals:
    primary: ""
    secondary: []
    
  challenges:
    - ""
    - ""
    
  buying_behavior:
    research_sources: []
    decision_criteria: []
    typical_buying_cycle: ""
    budget_authority: ""
    
  objections:
    - ""
    - ""
    
  messaging_hooks:
    - ""
    - ""
```

### 2. Jobs to Be Done (JTBD)

**Purpose**: Understand customer motivations

```
When [situation], I want to [motivation], so I can [expected outcome].

Example:
"When I'm managing multiple projects, I want to see all deadlines 
in one place, so I can prioritize effectively and never miss a 
delivery date."
```

### 3. Customer Journey Mapping

```
AWARENESS → CONSIDERATION → DECISION → RETENTION → ADVOCACY
    │            │            │           │           │
    ▼            ▼            ▼           ▼           ▼
 Touchpoints  Touchpoints  Touchpoints Touchpoints Touchpoints
 Questions    Questions    Questions   Questions   Questions
 Emotions     Emotions     Emotions    Emotions    Emotions
 Pain Points  Pain Points  Pain Points Pain Points Pain Points
```

## Trend Analysis Frameworks

### 1. Trend Evaluation Matrix

| Trend | Impact (1-5) | Probability (1-5) | Timeline | Action Required |
|-------|-------------|-------------------|----------|-----------------|
| AI Integration | 5 | 5 | 1-2 years | Invest in R&D |
| Mobile-first | 4 | 5 | Now | Adapt products |
| Sustainability | 3 | 4 | 2-3 years | Monitor |

### 2. Hype Cycle Analysis

```
                    ┌─────────┐
                    │ PEAK OF │
                    │INFLATED │
         ┌──────────┤EXPECTATIONS├──────────┐
         │          └─────────┘          │
         │                               │
    ┌────▼────┐                    ┌─────▼─────┐
    │TECHNOLOGY│                    │  SLOPE OF │
    │ TRIGGER  │                    │ENLIGHTENMENT│
    └──────────┘                    └─────┬─────┘
                                          │
         ┌──────────┐                    │
         │  TROUGH  │◄───────────────────┘
         │   OF     │
         │DISILLUSIONMENT│
         └──────────┘
                    │
         ┌──────────▼──────────┐
         │  PLATEAU OF         │
         │  PRODUCTIVITY       │
         └─────────────────────┘
```

## Market Segmentation Frameworks

### 1. Segmentation Criteria

| Type | Variables | Example |
|------|-----------|---------|
| Demographic | Age, Gender, Income, Education | B2C segmentation |
| Firmographic | Company size, Industry, Revenue | B2B segmentation |
| Geographic | Location, Climate, Urban/Rural | Regional marketing |
| Psychographic | Values, Lifestyle, Personality | Brand positioning |
| Behavioral | Usage, Loyalty, Benefits sought | Product features |

### 2. Segment Attractiveness Matrix

```
              HIGH ATTRACTIVENESS
                    │
        ┌───────────┼───────────┐
        │  TARGET   │  TARGET   │
        │  SEGMENTS │  SEGMENTS │
        │           │           │
LOW     ├───────────┼───────────┤ HIGH
COMPET- │  AVOID    │  EVALUATE │ COMPET-
ITIVE   │           │           │ ITIVE
STRENGTH├───────────┼───────────┤ STRENGTH
        │  AVOID    │  DEFEND   │
        │           │           │
        └───────────┼───────────┘
                    │
              LOW ATTRACTIVENESS
```

## Research Quality Standards

### Source Hierarchy

1. **Primary Sources** (Highest confidence)
   - Company reports, SEC filings
   - Original research, surveys
   - Expert interviews

2. **Secondary Sources** (High confidence)
   - Industry analyst reports (Gartner, Forrester)
   - Market research firms (Statista, IBISWorld)
   - Academic research

3. **Tertiary Sources** (Medium confidence)
   - News articles, trade publications
   - Review sites (G2, Capterra)
   - Industry blogs

4. **User-Generated** (Requires verification)
   - Social media, forums
   - Customer reviews
   - Community discussions

### Data Validation Checklist

- [ ] Multiple sources confirm key statistics
- [ ] Sources are recent (within 2 years)
- [ ] Source credibility assessed
- [ ] Methodology understood
- [ ] Outliers investigated
- [ ] Data gaps identified

---

*Part of Multi-Agent Marketing Campaign System*