# Gantt Chart (Mermaid)

**Project Name:** [Project Name]
**Company:** [Company Name]
**Period:** [Start Date] to [End Date]
**Version:** 1.0

---

## Project Timeline Overview

This Gantt chart visualizes the complete project timeline using Mermaid syntax, compatible with Markdown editors, Notion, and documentation tools.

---

## Complete Project Gantt Chart

```mermaid
gantt
    title [Project Name] - Project Timeline
    dateFormat YYYY-MM-DD
    axisFormat %d/%m
    
    section Planning Phase
    Requirements Analysis     :a1, 2026-01-01, 3d
    Project Planning          :a2, after a1, 5d
    Resource Allocation       :a3, after a2, 2d
    Risk Assessment           :a4, after a2, 2d
    Stakeholder Alignment     :a5, after a3, 2d
    
    section Setup Phase
    Tool Setup                :b1, after a5, 3d
    Template Creation         :b2, after b1, 4d
    Team Onboarding           :b3, after b1, 2d
    Access & Permissions      :b4, after b1, 1d
    Test Run                  :b5, after b2 b3, 2d
    
    section Execution Phase
    Content Production        :c1, after b5, 30d
    Social Media Management   :c2, after b5, 30d
    Campaign Execution        :c3, after c1, 20d
    SEO Optimization          :c4, after c1, 15d
    Community Engagement      :c5, after c2, 30d
    
    section Monitoring & Closing
    Performance Monitoring    :d1, after c1, 14d
    Mid-Project Review        :d2, 2026-02-15, 2d
    Final Reporting           :d3, after c5, 3d
    Documentation             :d4, after d3, 3d
    Project Handover          :d5, after d4, 2d
```

---

## Phase 1: Planning Phase (Week 1-2)

```mermaid
gantt
    title Planning Phase Detail
    dateFormat YYYY-MM-DD
    axisFormat %d/%m
    
    section Analysis
    Stakeholder Interviews    :p1, 2026-01-01, 2d
    Document Review           :p2, after p1, 1d
    Requirements Gathering    :p3, after p1, 2d
    
    section Planning
    Project Charter           :p4, after p3, 2d
    WBS Development           :p5, after p4, 2d
    Schedule Development      :p6, after p5, 1d
    
    section Setup
    Resource Planning         :p7, after p6, 1d
    Budget Finalization       :p8, after p6, 1d
    Risk Register             :p9, after p7 p8, 1d
```

### Planning Phase Tasks

| Task | Start | End | Duration | Owner | Dependencies |
|------|-------|-----|----------|-------|--------------|
| Stakeholder Interviews | [Date] | [Date] | 2 days | PM | None |
| Document Review | [Date] | [Date] | 1 day | PM | Interviews |
| Requirements Gathering | [Date] | [Date] | 2 days | Team Lead | Interviews |
| Project Charter | [Date] | [Date] | 2 days | PM | Requirements |
| WBS Development | [Date] | [Date] | 2 days | PM | Charter |
| Schedule Development | [Date] | [Date] | 1 day | PM | WBS |
| Resource Planning | [Date] | [Date] | 1 day | PM | Schedule |
| Budget Finalization | [Date] | [Date] | 1 day | PM | Schedule |
| Risk Register | [Date] | [Date] | 1 day | PM | Resources, Budget |

---

## Phase 2: Setup Phase (Week 3-4)

```mermaid
gantt
    title Setup Phase Detail
    dateFormat YYYY-MM-DD
    axisFormat %d/%m
    
    section Tools
    Google Workspace Setup    :s1, 2026-01-15, 1d
    Notion Setup              :s2, after s1, 1d
    Analytics Tools           :s3, after s1, 1d
    Design Tools              :s4, after s1, 1d
    
    section Templates
    Content Templates         :s5, after s2, 2d
    Report Templates          :s6, after s2, 1d
    Social Media Templates    :s7, after s5, 1d
    
    section Team
    Access Granting           :s8, after s1 s2, 1d
    Training Session          :s9, after s8, 1d
    Pilot Test                :s10, after s5 s9, 2d
```

### Setup Phase Tasks

| Task | Start | End | Duration | Owner | Dependencies |
|------|-------|-----|----------|-------|--------------|
| Google Workspace Setup | [Date] | [Date] | 1 day | Tech Lead | Planning Complete |
| Notion Setup | [Date] | [Date] | 1 day | Tech Lead | Google Setup |
| Analytics Tools | [Date] | [Date] | 1 day | Analytics | Google Setup |
| Design Tools | [Date] | [Date] | 1 day | Designer | Google Setup |
| Content Templates | [Date] | [Date] | 2 days | Writer | Notion Setup |
| Report Templates | [Date] | [Date] | 1 day | PM | Notion Setup |
| Social Media Templates | [Date] | [Date] | 1 day | Social Media | Content Templates |
| Access Granting | [Date] | [Date] | 1 day | Tech Lead | All Tools |
| Training Session | [Date] | [Date] | 1 day | PM | Access |
| Pilot Test | [Date] | [Date] | 2 days | Team | Templates, Training |

---

## Phase 3: Execution Phase (Week 5-10)

```mermaid
gantt
    title Execution Phase Detail
    dateFormat YYYY-MM-DD
    axisFormat %W
    
    section Content
    Article 1-3               :e1, 2026-02-01, 10d
    Article 4-6               :e2, after e1, 10d
    Article 7-10              :e3, after e2, 10d
    
    section Social Media
    Instagram Campaign        :e4, 2026-02-01, 30d
    TikTok Content            :e5, 2026-02-01, 30d
    LinkedIn Posts            :e6, 2026-02-01, 30d
    
    section Marketing
    Paid Ads Campaign         :e7, after e1, 14d
    Influencer Outreach       :e8, after e2, 7d
    Email Marketing           :e9, 2026-02-15, 14d
    
    section SEO
    Keyword Implementation    :e10, after e1, 7d
    On-page Optimization      :e11, after e10, 7d
    Link Building             :e12, after e11, 7d
```

### Execution Phase Tasks

| Task | Start | End | Duration | Owner | Dependencies |
|------|-------|-----|----------|-------|--------------|
| Article 1-3 | [Date] | [Date] | 10 days | Writer | Setup Complete |
| Article 4-6 | [Date] | [Date] | 10 days | Writer | Article 1-3 |
| Article 7-10 | [Date] | [Date] | 10 days | Writer | Article 4-6 |
| Instagram Campaign | [Date] | [Date] | 30 days | Social Media | Setup Complete |
| TikTok Content | [Date] | [Date] | 30 days | Social Media | Setup Complete |
| LinkedIn Posts | [Date] | [Date] | 30 days | Social Media | Setup Complete |
| Paid Ads Campaign | [Date] | [Date] | 14 days | Marketing | Article 1-3 |
| Influencer Outreach | [Date] | [Date] | 7 days | Marketing | Article 4-6 |
| Email Marketing | [Date] | [Date] | 14 days | Marketing | Mid-phase |
| Keyword Implementation | [Date] | [Date] | 7 days | SEO | Article 1-3 |
| On-page Optimization | [Date] | [Date] | 7 days | SEO | Keywords |
| Link Building | [Date] | [Date] | 7 days | SEO | On-page |

---

## Phase 4: Monitoring & Closing (Week 11-12)

```mermaid
gantt
    title Monitoring & Closing Phase
    dateFormat YYYY-MM-DD
    axisFormat %d/%m
    
    section Monitoring
    Weekly Analytics Review   :m1, 2026-03-01, 14d
    KPI Dashboard Update      :m2, 2026-03-01, 14d
    Performance Report        :m3, 2026-03-07, 2d
    
    section Review
    Mid-Project Review        :m4, 2026-03-08, 1d
    Stakeholder Feedback      :m5, after m4, 2d
    Adjustments               :m6, after m5, 2d
    
    section Closing
    Final Report Writing      :m7, 2026-03-15, 3d
    Documentation Compile     :m8, after m7, 2d
    Presentation Prep         :m9, after m7, 2d
    Final Presentation        :m10, after m8 m9, 1d
    Handover                  :m11, after m10, 1d
```

### Closing Phase Tasks

| Task | Start | End | Duration | Owner | Dependencies |
|------|-------|-----|----------|-------|--------------|
| Weekly Analytics Review | [Date] | [Date] | 14 days | Analytics | Execution |
| KPI Dashboard Update | [Date] | [Date] | 14 days | PM | Execution |
| Performance Report | [Date] | [Date] | 2 days | PM | Week 1 Data |
| Mid-Project Review | [Date] | [Date] | 1 day | PM | Performance Report |
| Stakeholder Feedback | [Date] | [Date] | 2 days | PM | Review |
| Adjustments | [Date] | [Date] | 2 days | Team | Feedback |
| Final Report Writing | [Date] | [Date] | 3 days | PM | All Data |
| Documentation Compile | [Date] | [Date] | 2 days | Team | Final Report |
| Presentation Prep | [Date] | [Date] | 2 days | PM | Final Report |
| Final Presentation | [Date] | [Date] | 1 day | PM | Docs, Presentation |
| Handover | [Date] | [Date] | 1 day | PM | Presentation |

---

## Milestones Timeline

```mermaid
gantt
    title Project Milestones
    dateFormat YYYY-MM-DD
    axisFormat %d/%m
    
    section Milestones
    Project Kickoff           :milestone, mk1, 2026-01-01, 0d
    Planning Complete         :milestone, mk2, 2026-01-14, 0d
    Setup Complete            :milestone, mk3, 2026-01-28, 0d
    First Content Live        :milestone, mk4, 2026-02-07, 0d
    Mid-Project Review        :milestone, mk5, 2026-02-15, 0d
    Campaign Launch           :milestone, mk6, 2026-02-20, 0d
    All Content Complete      :milestone, mk7, 2026-03-07, 0d
    Final Presentation        :milestone, mk8, 2026-03-20, 0d
    Project Closure           :milestone, mk9, 2026-03-21, 0d
```

---

## Critical Path

```mermaid
flowchart LR
    A[Requirements] --> B[Project Plan]
    B --> C[Resource Allocation]
    C --> D[Tool Setup]
    D --> E[Template Creation]
    E --> F[Content Production]
    F --> G[Campaign Execution]
    G --> H[Performance Monitoring]
    H --> I[Final Report]
    I --> J[Handover]
    
    style A fill:#ff6b6b
    style B fill:#ff6b6b
    style D fill:#ff6b6b
    style F fill:#ff6b6b
    style G fill:#ff6b6b
    style I fill:#ff6b6b
    style J fill:#ff6b6b
```

### Critical Path Tasks

| Task | Duration | Float | Critical |
|------|----------|-------|----------|
| Requirements Analysis | 3 days | 0 | ✅ Yes |
| Project Planning | 5 days | 0 | ✅ Yes |
| Tool Setup | 3 days | 0 | ✅ Yes |
| Content Production | 30 days | 0 | ✅ Yes |
| Campaign Execution | 20 days | 0 | ✅ Yes |
| Final Reporting | 3 days | 0 | ✅ Yes |
| Handover | 1 day | 0 | ✅ Yes |

---

## Resource Loading

### Weekly Resource Allocation

```mermaid
xychart-beta
    title "Weekly Hours by Resource Type"
    x-axis [Week 1, Week 2, Week 3, Week 4, Week 5, Week 6, Week 7, Week 8, Week 9, Week 10, Week 11, Week 12]
    y-axis "Hours" 0 --> 50
    bar [40, 40, 30, 30, 20, 20, 20, 20, 20, 20, 30, 40]
    bar [20, 20, 30, 30, 40, 40, 40, 40, 40, 40, 30, 20]
    bar [10, 10, 20, 20, 30, 30, 30, 30, 30, 30, 20, 10]
```

---

## Usage Instructions

### How to Use This Gantt Chart

1. **Copy the Mermaid code** from any section above
2. **Paste into** any Mermaid-compatible editor:
   - Notion (with Mermaid block)
   - GitHub/GitLab Markdown
   - VS Code with Mermaid extension
   - Online editors: mermaid.live

3. **Customize dates** by modifying the `dateFormat` and date values
4. **Add tasks** using the syntax: `Task Name :id, start-date, duration`

### Mermaid Gantt Syntax Reference

```
gantt
    title Chart Title
    dateFormat YYYY-MM-DD
    
    section Section Name
    Task 1     :t1, 2026-01-01, 5d
    Task 2     :t2, after t1, 3d
    Milestone  :milestone, m1, 2026-01-15, 0d
```

---

## Gantt Chart Change Log

| Version | Date | Change Description | Author |
|---------|------|-------------------|--------|
| 1.0 | [Date] | Initial Gantt chart created | PM |

---

*Gantt Chart - [Project Name] - Version 1.0*