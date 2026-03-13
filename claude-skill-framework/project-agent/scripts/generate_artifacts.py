#!/usr/bin/env python3
"""
Generate Artifacts Engine
Core engine for creating all 13 project management artifacts.
"""

import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional
import re


class ArtifactGenerator:
    """Generates all 13 project management artifacts from analyzed data."""
    
    ARTIFACTS = [
        "project-management-plan",
        "work-breakdown-structure",
        "gantt-chart-mermaid",
        "content-production-calendar",
        "keyword-research-seo-strategy",
        "market-research-roadmap",
        "kpi-monitoring-dashboard",
        "weekly-activity-plan-report",
        "risk-issue-register",
        "communication-stakeholder-plan",
        "raci-matrix",
        "deliverables-tracking-sheet",
        "performance-evaluation-framework"
    ]
    
    def __init__(self, template_dir: str = None):
        self.template_dir = Path(template_dir) if template_dir else Path(__file__).parent.parent / "templates"
        self.output_dir = Path.cwd() / "output"
        
    def generate_all(self, analysis_data: Dict, output_dir: str = None) -> Dict:
        """
        Generate all 13 artifacts from analysis data.
        
        Args:
            analysis_data: Dict containing analyzed assignment data
            output_dir: Optional output directory path
            
        Returns:
            Dict with paths to generated artifacts
        """
        if output_dir:
            self.output_dir = Path(output_dir)
        
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        results = {
            "generated_at": datetime.now().isoformat(),
            "output_directory": str(self.output_dir),
            "artifacts": {}
        }
        
        context = self._build_context(analysis_data)
        
        for artifact in self.ARTIFACTS:
            try:
                output_path = self._generate_artifact(artifact, context)
                results["artifacts"][artifact] = str(output_path)
            except Exception as e:
                results["artifacts"][artifact] = f"Error: {str(e)}"
        
        return results
    
    def _build_context(self, analysis_data: Dict) -> Dict:
        """Build template context from analysis data."""
        company = analysis_data.get("company_info", {})
        period = analysis_data.get("internship_period", {})
        
        start_date = period.get("start_date") or datetime.now().strftime("%Y-%m-%d")
        end_date = period.get("end_date") or (datetime.now() + timedelta(weeks=12)).strftime("%Y-%m-%d")
        
        return {
            "project_name": f"{company.get('name', 'Project')} Internship Program",
            "company_name": company.get("name", "[Company Name]"),
            "industry": company.get("industry", "[Industry]"),
            "start_date": start_date,
            "end_date": end_date,
            "duration_weeks": period.get("duration_weeks", 12),
            "kpis": analysis_data.get("kpis", []),
            "deliverables": analysis_data.get("deliverables", []),
            "team_size": analysis_data.get("team_structure", {}).get("team_size", 1),
            "roles": analysis_data.get("team_structure", {}).get("roles", []),
            "current_date": datetime.now().strftime("%Y-%m-%d"),
            "version": "1.0"
        }
    
    def _generate_artifact(self, artifact_name: str, context: Dict) -> Path:
        """Generate a single artifact from template."""
        template_path = self.template_dir / f"{artifact_name}.md"
        
        if not template_path.exists():
            return self._generate_from_scratch(artifact_name, context)
        
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace placeholders
        content = self._replace_placeholders(content, context)
        
        output_path = self.output_dir / f"{artifact_name}.md"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return output_path
    
    def _replace_placeholders(self, content: str, context: Dict) -> str:
        """Replace template placeholders with context values."""
        # Simple replacements
        replacements = {
            "[Project Name]": context.get("project_name", ""),
            "[Company Name]": context.get("company_name", ""),
            "[Industry]": context.get("industry", ""),
            "[Start Date]": context.get("start_date", ""),
            "[End Date]": context.get("end_date", ""),
            "[Date]": context.get("current_date", ""),
            "[Duration]": str(context.get("duration_weeks", 12)),
        }
        
        for placeholder, value in replacements.items():
            content = content.replace(placeholder, value)
        
        return content
    
    def _generate_from_scratch(self, artifact_name: str, context: Dict) -> Path:
        """Generate artifact without template."""
        generators = {
            "project-management-plan": self._gen_project_plan,
            "work-breakdown-structure": self._gen_wbs,
            "gantt-chart-mermaid": self._gen_gantt,
        }
        
        generator = generators.get(artifact_name, self._gen_generic)
        content = generator(context)
        
        output_path = self.output_dir / f"{artifact_name}.md"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return output_path
    
    def _gen_project_plan(self, ctx: Dict) -> str:
        return f"""# Project Management Plan

**Project Name:** {ctx['project_name']}
**Company:** {ctx['company_name']}
**Period:** {ctx['start_date']} to {ctx['end_date']}
**Version:** {ctx['version']}

---

## Executive Summary

This project management plan outlines the approach for the internship program at {ctx['company_name']}.

## Project Objectives

1. Complete all assigned deliverables
2. Meet or exceed KPI targets
3. Develop professional skills

## Timeline

- **Duration:** {ctx['duration_weeks']} weeks
- **Start:** {ctx['start_date']}
- **End:** {ctx['end_date']}

---

*Generated by Project-Agent*
"""
    
    def _gen_wbs(self, ctx: Dict) -> str:
        return f"""# Work Breakdown Structure

**Project:** {ctx['project_name']}
**Version:** {ctx['version']}

---

## Phase 1: Planning (Week 1-2)
- 1.1 Project kickoff
- 1.2 Requirements gathering
- 1.3 Resource planning

## Phase 2: Execution (Week 3-{ctx['duration_weeks']-2})
- 2.1 Content creation
- 2.2 Campaign execution
- 2.3 Monitoring and reporting

## Phase 3: Closure (Week {ctx['duration_weeks']-1}-{ctx['duration_weeks']})
- 3.1 Final reporting
- 3.2 Documentation
- 3.3 Handover

---

*Generated by Project-Agent*
"""
    
    def _gen_gantt(self, ctx: Dict) -> str:
        return f"""# Gantt Chart

**Project:** {ctx['project_name']}

```mermaid
gantt
    title {ctx['project_name']}
    dateFormat  YYYY-MM-DD
    section Planning
    Kickoff           :a1, {ctx['start_date']}, 1w
    Requirements      :a2, after a1, 1w
    section Execution
    Content Creation  :b1, after a2, {ctx['duration_weeks']-4}w
    section Closure
    Final Report      :c1, after b1, 1w
    Handover          :c2, after c1, 1w
```

---

*Generated by Project-Agent*
"""
    
    def _gen_generic(self, ctx: Dict) -> str:
        return f"""# {ctx['project_name']}

**Company:** {ctx['company_name']}
**Period:** {ctx['start_date']} to {ctx['end_date']}
**Version:** {ctx['version']}

---

*Generated by Project-Agent*
"""


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate project artifacts')
    parser.add_argument('analysis_file', help='Path to analysis JSON file')
    parser.add_argument('--output', '-o', help='Output directory')
    parser.add_argument('--template-dir', '-t', help='Template directory')
    
    args = parser.parse_args()
    
    with open(args.analysis_file, 'r') as f:
        analysis_data = json.load(f)
    
    generator = ArtifactGenerator(template_dir=args.template_dir)
    results = generator.generate_all(analysis_data, output_dir=args.output)
    
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()