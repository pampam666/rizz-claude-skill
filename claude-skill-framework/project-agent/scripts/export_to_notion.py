#!/usr/bin/env python3
"""
Export to Notion
Creates Notion database templates and exports content to Notion.
"""

import json
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime


class NotionExporter:
    """Exports artifacts to Notion using free-tier integration."""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        
    def generate_database_schema(self, db_type: str) -> Dict:
        """Generate Notion database schema for different artifact types."""
        schemas = {
            "kpi_dashboard": {
                "name": "KPI Dashboard",
                "properties": {
                    "KPI Name": {"title": {}},
                    "Target": {"number": {"format": "number"}},
                    "Current": {"number": {"format": "number"}},
                    "Progress": {"formula": {"expression": "prop(\"Current\") / prop(\"Target\") * 100"}},
                    "Status": {"select": {"options": [
                        {"name": "On Track", "color": "green"},
                        {"name": "At Risk", "color": "yellow"},
                        {"name": "Behind", "color": "red"}
                    ]}},
                    "Owner": {"people": {}},
                    "Due Date": {"date": {}}
                }
            },
            "content_calendar": {
                "name": "Content Calendar",
                "properties": {
                    "Title": {"title": {}},
                    "Type": {"select": {"options": [
                        {"name": "Article", "color": "blue"},
                        {"name": "Social Media", "color": "purple"},
                        {"name": "Video", "color": "red"},
                        {"name": "Infographic", "color": "green"}
                    ]}},
                    "Status": {"status": {}},
                    "Publish Date": {"date": {}},
                    "Author": {"people": {}},
                    "Keywords": {"rich_text": {}},
                    "Platform": {"multi_select": {"options": [
                        {"name": "Website", "color": "gray"},
                        {"name": "Instagram", "color": "pink"},
                        {"name": "LinkedIn", "color": "blue"},
                        {"name": "TikTok", "color": "default"}
                    ]}}
                }
            },
            "risk_register": {
                "name": "Risk Register",
                "properties": {
                    "Risk": {"title": {}},
                    "Probability": {"select": {"options": [
                        {"name": "Low", "color": "green"},
                        {"name": "Medium", "color": "yellow"},
                        {"name": "High", "color": "red"}
                    ]}},
                    "Impact": {"select": {"options": [
                        {"name": "Low", "color": "green"},
                        {"name": "Medium", "color": "yellow"},
                        {"name": "High", "color": "red"}
                    ]}},
                    "Mitigation": {"rich_text": {}},
                    "Owner": {"people": {}},
                    "Status": {"status": {}}
                }
            }
        }
        return schemas.get(db_type, {})
    
    def convert_markdown_to_blocks(self, content: str) -> List[Dict]:
        """Convert markdown content to Notion block format."""
        blocks = []
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            if line.startswith('# '):
                blocks.append({
                    "object": "block",
                    "type": "heading_1",
                    "heading_1": {"rich_text": [{"type": "text", "text": {"content": line[2:]}}]}
                })
            elif line.startswith('## '):
                blocks.append({
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {"rich_text": [{"type": "text", "text": {"content": line[3:]}}]}
                })
            elif line.startswith('### '):
                blocks.append({
                    "object": "block",
                    "type": "heading_3",
                    "heading_3": {"rich_text": [{"type": "text", "text": {"content": line[4:]}}]}
                })
            elif line.startswith('- ') or line.startswith('* '):
                blocks.append({
                    "object": "block",
                    "type": "bulleted_list_item",
                    "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": line[2:]}}]}
                })
            else:
                blocks.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {"rich_text": [{"type": "text", "text": {"content": line[:2000]}}]}
                })
        
        return blocks
    
    def export_artifact(self, artifact_path: str, page_id: str = None) -> Dict:
        """Export a single artifact to Notion."""
        with open(artifact_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        blocks = self.convert_markdown_to_blocks(content)
        
        return {
            "artifact": artifact_path,
            "blocks_generated": len(blocks),
            "status": "ready_for_export",
            "note": "Use Notion API with blocks to create page content"
        }


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Export artifacts to Notion')
    parser.add_argument('--schema', '-s', choices=['kpi_dashboard', 'content_calendar', 'risk_register'],
                       help='Generate Notion database schema')
    parser.add_argument('--artifact', '-a', help='Path to artifact file to convert')
    parser.add_argument('--output', '-o', help='Output file path')
    
    args = parser.parse_args()
    
    exporter = NotionExporter()
    
    if args.schema:
        schema = exporter.generate_database_schema(args.schema)
        output = json.dumps(schema, indent=2)
        if args.output:
            with open(args.output, 'w') as f:
                f.write(output)
        print(output)
    
    if args.artifact:
        result = exporter.export_artifact(args.artifact)
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()