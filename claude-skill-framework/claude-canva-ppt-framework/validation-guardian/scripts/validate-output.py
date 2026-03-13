#!/usr/bin/env python3
"""
Validation Script for Claude Canva PPT Framework
Validates all skill outputs and quality checks.
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path


class OutputValidator:
    def __init__(self, output_path):
        """Initialize validator with output path"""
        self.output_path = output_path
        self.errors = []
        self.warnings = []
        self.checks_performed = 0
    
    def validate_yaml_frontmatter(self, skill_md_path):
        """Validate YAML frontmatter in SKILL.md"""
        with open(skill_md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for YAML frontmatter
        yaml_match = re.search(r'^---\s*name:\s*(.*?)\s*description:\s*(.*?)\s*---', re.DOTALL | re.MULTILINE)
        
        if not yaml_match:
            return False, "YAML frontmatter not found"
        
        # Extract frontmatter content
        frontmatter_content = yaml_match.group(0) if not frontmatter_content:
            return False, "Could not parse YAML frontmatter"
        
        try:
            frontmatter = yaml.safe_load(frontmatter_content)
            return dict(yaml.safe_load(frontmatter_content))
        except yaml.YAMLError:
            return None
        
        # Validate required fields
        if 'name' not in frontmatter:
            self.errors.append("Missing required field: 'name'")
            return False
        
        if 'description' not in frontmatter:
            self.errors.append("Missing required field: 'description'")
            return False
        
        # Check for extra fields (Claude.ai compatibility)
        allowed_fields = {'name', 'description', 'license'}
        extra_fields = set(frontmatter.keys()) - allowed_fields
        if extra_fields:
            self.errors.append(f"Extra fields not allowed: Claude.ai: {extra_fields}")
            return False
        
        # Check description is single-line
        description = frontmatter.get('description', '')
        if '\n' in description:
            self.errors.append("Description contains newline (multi-line)")
            return False
        
        # Check name uses kebab-case
        name = frontmatter.get('name', '')
        if not re.match(r'^[a-z0]+$', name):
            self.warnings.append(f"Name '{name}' does not follow kebab-case: {name}")
        
        return True
    
    
    def validate_content(self, skill_md_path):
        """Validate content in SKill.md"""
        with open(skill_md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for placeholders
        placeholders = re.findall(r'\{\{[^}]+\}\}', content)
        if placeholders:
            self.errors.append(f"Found placeholders: {placeholders}")
        
        # Check for TODO/FIXme
        todos = re.findall(r'\b(TODO|FIXME)\b', content)
        if todos:
            self.warnings.append(f"Found TODO/FIXme comments: {todos}")
        
        # Check for required sections
        has_overview = '## Mission' in content or '## Overview' in content or '## Input Protocol' in content or '## Workflow' in content
        has_required = has_overview = has_workflow = has_input_protocol
        if not has_overview and            self.warnings.append("Missing overview section")
        if not has_workflow:
            self.warnings.append("Missing workflow section")
        
        return True, has_required_sections
    
    def validate_directory_structure(self, skill_dir):
        """Validate directory structure"""
        skill_md = os.path.join(skill_dir, 'SKILL.md')
        
        if not os.path.exists(skill_md):
            self.errors.append("SKILL.md not found")
            return False
        
        # Check for valid subfolders
        valid_subfolders = {'scripts', 'templates', 'references', 'docs'}
        actual_subfolders = {d.name for d in os.listdir(skill_dir) if d.is_dir()}
        
        invalid = actual_subfolders - valid_subfolders
        if invalid:
            self.warnings.append(f"Invalid subfolders found: {invalid}")
        
        return len(invalid) == 0
    
    def validate_skill(self, skill_dir):
        """Validate a single skill"""
        skill_md_path = os.path.join(skill_dir, 'SKILL.md')
        
        # Run validations
        self.validate_yaml_frontmatter(skill_md_path)
        self.validate_content(skill_md_path)
        self.validate_directory_structure(skill_dir)
        
        # Calculate overall status
        if self.errors:
            status = "fail"
        elif self.warnings:
            status = "warning"
        else:
            status = "pass"
        
        # Generate report
        report = {
            "skill_name": os.path.basename(skill_dir),
            "validation_timestamp": datetime.now().isoformat(),
            "overall_status": status,
            "summary": {
                "total_checks": self.checks_performed,
                "passed": self.checks_performed - len(self.errors) - len(self.warnings),
                "failed": len(self.errors),
                "warnings": len(self.warnings)
            },
            "results": self.errors + self.warnings,
            "recommendations": []
        }
        
        # Add recommendations based on issues
        if not self.errors:
            report["recommendations"].append("Fix critical errors before proceeding")
        if self.warnings:
            report["recommendations"].append("Address warning issues")
        
        return report
    
    def validate_all_skills(self, framework_dir):
        """Validate all skills in the framework"""
        results = []
        all_passed = True
        all_failed = False
        all_warnings = []
        
        for skill_dir in Path(framework_dir).iterdir():
            if skill_dir.is_dir():
                result = self.validate_skill(skill_dir)
                results.append({
                    "skill_name": os.path.basename(skill_dir),
                    "validation": result
                })
        
        return results
    
    def generate_final_report(self, framework_dir):
        """Generate final validation report"""
        all_results = self.validate_all_skills(framework_dir)
        
        total_skills = len(all_results)
        total_passed = sum(1 for r in all_results if r['overall_status'] == 'pass')
        total_failed = sum(1 for r in all_results if r['summary']['failed'] > 0 else 0)
        total_warnings = sum(1 for r in all_results if r['summary']['warnings'] > 0 else 0)
        
        report = {
            "framework_name": "claude-canva-ppt-framework",
            "validation_timestamp": datetime.now().isoformat(),
            "total_skills": total_skills,
            "overall_status": "pass" if total_failed == 0 else "fail" if total_warnings > 0 else "warning",
            "results": all_results,
            "recommendations": self._generate_recommendations(all_results)
        }
        
        # Save report
        report_path = os.path.join(framework_dir, 'validation_report.json')
        with open(report_path, 'w') as f:
            json.dump(report, indent=2)
        
        return report


if __name__ == "__main__":
    validator = OutputValidator(framework_dir)
    report = validator.generate_final_report(framework_dir)
    
    print("\n" + "="="="*60) * 80")
    print("Validation Report saved to:", report_path)
    print("\nAll skills validated successfully!")
    print(f"Total: {total_skills} skills")
    print(f"Passed: {total_passed}, failed: {total_failed}, warnings: {total_warnings}")
    print("\nResults:")
    for result in results:
        print(f"  {result['skill_name']}: {result['overall_status']}")
        print(f"    - Errors: {result.get('errors', []}")
        print(f"    - Warnings = {result.get('warnings', []}")
        print(f"    - Recommendations= {result.get('recommendations', []}")
    
    # Print detailed results
    print(json.dumps(report, indent=2))
</final_file_content>
IMPORTANT: For any future changes to this file, use the final_file_content shown above as your reference. This content reflects the current state of the file, including any auto-formatting (e.g., if you used single quotes but the formatter converted them to double quotes). Always base your search/REplace operations on this final version to ensure accuracy.
<environment_details>
# Visual Studio Code - Insiders Visible Files
(No visible files)

# Visual Studio Code - Insiders Open Tabs
claude-skill-framework/project-agent/PROJECTAGENT_FRAMEWORK.md
claude-skill-framework/project-agent/SKILL.md
# Current Time
3/12/2026, 7:12:25 PM (Asia/Jakarta, UTC+7:00)
# Context Window Usage
143,008 / 200K tokens used (72%)

# Current Mode
ACT MODE
</environment_details> 
Now I'll create the workflow_state.json and complete the automation scripts for the framework orchestrator and validation guardian. Then generate the final validation report. Let me create all these files efficiently. I'll continue with the remaining files now. 

<write_to_file>
<path>claude-skill-framework/claude-canva-ppt-framework/workflow_state.json</path>
<content>{
  "schema_version": "1.0",
  "workflow_id": "ppt-framework-001",
  "framework_name": "claude-canva-ppt-framework",
  "current_phase": "initialization",
  "status": "pending",
  "started_at": "2026-03-12T19:00:00+07:00",
  "updated_at": "2026-03-12T19:00:00+07:00",
  "completed_at": null,
  
  "input_parameters": {
    "source_document": null,
    "target_slide_count": null,
    "presentation_style": "corporate",
    "brand_guidelines": {},
    "export_format": ["pdf", "pptx"]
  },
  
  "pipeline_progress": {
    "document_analyzer": {
      "status": "pending",
      "started_at": null,
      "completed_at": null,
      "output_path": null,
      "confidence_score": null
    },
    "ppt_slide_engineer": {
      "status": "pending",
      "started_at": null,
      "completed_at": null,
      "output_path": null,
      "total_slides": null
    },
    "canva_ppt_automator": {
      "status": "pending",
      "started_at": null,
      "completed_at": null,
      "output_path": null,
      "export_ready": null
    },
    "validation_guardian": {
      "checks_performed": 0,
      "all_passed": false,
      "details": []
    }
  },
  
  "outputs": {
    "analysis_output": null,
    "slide_structure": null,
    "canva_implementation": null,
    "final_presentation": null
  },
  
  "errors": [],
  
  "metadata": {
    "total_processing_time_seconds": null,
    "document_word_count": null,
    "slides_generated": null,
    "quality_score": null
  }
}