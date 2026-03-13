#!/usr/bin/env python3
"""
Google Sheets Generator
Creates Google Sheets templates with formulas and charts for KPI tracking.
"""

import json
from typing import Dict, List, Optional
from pathlib import Path


class SheetsGenerator:
    """Generates Google Sheets templates with formulas and formatting."""
    
    def __init__(self):
        self.templates = {}
    
    def generate_kpi_dashboard(self, kpis: List[Dict] = None) -> Dict:
        """Generate KPI Dashboard sheet structure with formulas."""
        return {
            "sheet_name": "KPI Dashboard",
            "sheets": [
                {
                    "name": "Dashboard",
                    "data": {
                        "headers": ["KPI Name", "Category", "Target", "Current", "Progress %", "Status", "Owner", "Due Date"],
                        "rows": kpis or [
                            ["Social Media Followers", "Social Media", 10000, 0, "", "", "", ""],
                            ["Content Articles", "Content", 20, 0, "", "", "", ""],
                            ["Engagement Rate", "Social Media", 5.0, 0, "", "", "", ""],
                            ["Website Traffic", "Traffic", 5000, 0, "", "", "", ""]
                        ],
                        "formulas": {
                            "E2": "=IF(C2>0,ROUND(D2/C2*100,1),0)",
                            "F2": '=IF(E2>=100,"Complete",IF(E2>=75,"On Track",IF(E2>=50,"At Risk","Behind")))'
                        },
                        "formatting": {
                            "header_row": {"bold": True, "background": "#4285f4", "font_color": "#ffffff"},
                            "progress_column": {"format": "percentage"},
                            "conditional_formatting": [
                                {"range": "F:F", "rules": {"Complete": "green", "On Track": "yellow", "At Risk": "orange", "Behind": "red"}}
                            ]
                        }
                    }
                },
                {
                    "name": "Weekly Tracking",
                    "data": {
                        "headers": ["Week", "Date", "KPI", "Value", "Notes"],
                        "rows": []
                    }
                },
                {
                    "name": "Summary",
                    "data": {
                        "headers": ["Metric", "Value"],
                        "rows": [
                            ["Total KPIs", "=COUNTA(Dashboard!A:A)-1"],
                            ["Completed", '=COUNTIF(Dashboard!F:F,"Complete")'],
                            ["On Track", '=COUNTIF(Dashboard!F:F,"On Track")'],
                            ["At Risk", '=COUNTIF(Dashboard!F:F,"At Risk")'],
                            ["Behind", '=COUNTIF(Dashboard!F:F,"Behind")'],
                            ["Overall Progress %", "=AVERAGE(Dashboard!E:E)"]
                        ]
                    }
                }
            ],
            "charts": [
                {
                    "type": "pie",
                    "title": "KPI Status Distribution",
                    "range": "Summary!A1:B5",
                    "position": {"row": 1, "col": 3}
                },
                {
                    "type": "bar",
                    "title": "Progress by KPI",
                    "range": "Dashboard!A:A,E:E",
                    "position": {"row": 10, "col": 1}
                }
            ]
        }
    
    def generate_content_tracker(self) -> Dict:
        """Generate Content Production Tracker sheet."""
        return {
            "sheet_name": "Content Tracker",
            "sheets": [
                {
                    "name": "Content Calendar",
                    "data": {
                        "headers": ["ID", "Title", "Type", "Status", "Author", "Due Date", "Publish Date", "Platform", "Keywords", "Notes"],
                        "rows": [],
                        "data_validation": {
                            "C:C": {"options": ["Article", "Social Media", "Video", "Infographic", "Report"]},
                            "D:D": {"options": ["Planned", "In Progress", "Review", "Published", "Cancelled"]}
                        }
                    }
                },
                {
                    "name": "Monthly Summary",
                    "data": {
                        "headers": ["Month", "Planned", "Published", "Completion Rate"],
                        "formulas": {
                            "D2": "=IF(B2>0,C2/B2*100,0)"
                        }
                    }
                }
            ]
        }
    
    def generate_risk_register(self) -> Dict:
        """Generate Risk Register sheet."""
        return {
            "sheet_name": "Risk Register",
            "sheets": [
                {
                    "name": "Risks",
                    "data": {
                        "headers": ["Risk ID", "Description", "Category", "Probability", "Impact", "Risk Score", "Mitigation", "Owner", "Status", "Date Identified"],
                        "formulas": {
                            "F2": '=SWITCH(D2,"High",3,"Medium",2,"Low",1)*SWITCH(E2,"High",3,"Medium",2,"Low",1)'
                        },
                        "data_validation": {
                            "D:D": {"options": ["High", "Medium", "Low"]},
                            "E:E": {"options": ["High", "Medium", "Low"]},
                            "I:I": {"options": ["Open", "Mitigating", "Closed", "Accepted"]}
                        },
                        "conditional_formatting": [
                            {"range": "F:F", "rules": {"high": ">6", "medium": "3-6", "low": "<3"}}
                        ]
                    }
                }
            ]
        }
    
    def generate_deliverables_tracker(self) -> Dict:
        """Generate Deliverables Tracking sheet."""
        return {
            "sheet_name": "Deliverables",
            "sheets": [
                {
                    "name": "All Deliverables",
                    "data": {
                        "headers": ["ID", "Deliverable", "Description", "Priority", "Status", "Progress %", "Start Date", "Due Date", "Owner", "Dependencies"],
                        "rows": []
                    }
                },
                {
                    "name": "Summary",
                    "data": {
                        "headers": ["Status", "Count", "Percentage"],
                        "rows": [
                            ["Not Started", '=COUNTIF(\'All Deliverables\'!E:E,"Not Started")', ""],
                            ["In Progress", '=COUNTIF(\'All Deliverables\'!E:E,"In Progress")', ""],
                            ["Completed", '=COUNTIF(\'All Deliverables\'!E:E,"Completed")', ""],
                            ["Total", "=SUM(B2:B4)", "100%"]
                        ],
                        "formulas": {
                            "C2": "=IF($B$5>0,B2/$B$5,0)",
                            "C3": "=IF($B$5>0,B3/$B$5,0)",
                            "C4": "=IF($B$5>0,B4/$B$5,0)"
                        }
                    }
                }
            ]
        }
    
    def export_to_json(self, template_type: str, output_path: str = None) -> str:
        """Export template to JSON file."""
        generators = {
            "kpi_dashboard": self.generate_kpi_dashboard,
            "content_tracker": self.generate_content_tracker,
            "risk_register": self.generate_risk_register,
            "deliverables": self.generate_deliverables_tracker
        }
        
        generator = generators.get(template_type)
        if not generator:
            raise ValueError(f"Unknown template type: {template_type}")
        
        template = generator()
        json_output = json.dumps(template, indent=2)
        
        if output_path:
            with open(output_path, 'w') as f:
                f.write(json_output)
        
        return json_output
    
    def generate_csv(self, template_type: str) -> str:
        """Generate CSV format for simple import."""
        generators = {
            "kpi_dashboard": self.generate_kpi_dashboard,
            "content_tracker": self.generate_content_tracker,
            "risk_register": self.generate_risk_register,
            "deliverables": self.generate_deliverables_tracker
        }
        
        generator = generators.get(template_type)
        if not generator:
            raise ValueError(f"Unknown template type: {template_type}")
        
        template = generator()
        first_sheet = template["sheets"][0]
        
        lines = [",".join(first_sheet["data"]["headers"])]
        for row in first_sheet["data"]["rows"]:
            lines.append(",".join(str(cell) for cell in row))
        
        return "\n".join(lines)


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate Google Sheets templates')
    parser.add_argument('--type', '-t', 
                       choices=['kpi_dashboard', 'content_tracker', 'risk_register', 'deliverables'],
                       required=True, help='Template type to generate')
    parser.add_argument('--format', '-f', choices=['json', 'csv'], default='json',
                       help='Output format')
    parser.add_argument('--output', '-o', help='Output file path')
    
    args = parser.parse_args()
    
    generator = SheetsGenerator()
    
    if args.format == 'json':
        output = generator.export_to_json(args.type, args.output)
    else:
        output = generator.generate_csv(args.type)
        if args.output:
            with open(args.output, 'w') as f:
                f.write(output)
    
    print(output)


if __name__ == '__main__':
    main()