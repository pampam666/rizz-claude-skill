#!/usr/bin/env python3
"""
Google Docs Generator
Creates Google Docs templates from markdown content.
"""

import json
import re
from typing import Dict, List, Optional
from pathlib import Path
from datetime import datetime


class DocsGenerator:
    """Generates Google Docs templates from markdown."""
    
    def __init__(self):
        self.template_vars = {}
    
    def convert_markdown_to_docs(self, markdown_path: str, context: Dict = None) -> Dict:
        """
        Convert markdown file to Google Docs structure.
        
        Args:
            markdown_path: Path to markdown file
            context: Optional context for placeholder replacement
            
        Returns:
            Dict with document structure
        """
        with open(markdown_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if context:
            content = self._replace_placeholders(content, context)
        
        return {
            "title": self._extract_title(content),
            "body": self._parse_content(content),
            "generated_at": datetime.now().isoformat()
        }
    
    def _extract_title(self, content: str) -> str:
        """Extract title from markdown content."""
        match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        return match.group(1) if match else "Untitled Document"
    
    def _replace_placeholders(self, content: str, context: Dict) -> str:
        """Replace placeholders with context values."""
        for key, value in context.items():
            placeholder = f"[{key}]"
            content = content.replace(placeholder, str(value))
        return content
    
    def _parse_content(self, content: str) -> List[Dict]:
        """Parse markdown content into document elements."""
        elements = []
        lines = content.split('\n')
        current_paragraph = []
        
        for line in lines:
            # Heading 1
            if line.startswith('# '):
                if current_paragraph:
                    elements.append(self._create_paragraph(current_paragraph))
                    current_paragraph = []
                elements.append({
                    "type": "heading",
                    "level": 1,
                    "text": line[2:].strip()
                })
            # Heading 2
            elif line.startswith('## '):
                if current_paragraph:
                    elements.append(self._create_paragraph(current_paragraph))
                    current_paragraph = []
                elements.append({
                    "type": "heading",
                    "level": 2,
                    "text": line[3:].strip()
                })
            # Heading 3
            elif line.startswith('### '):
                if current_paragraph:
                    elements.append(self._create_paragraph(current_paragraph))
                    current_paragraph = []
                elements.append({
                    "type": "heading",
                    "level": 3,
                    "text": line[4:].strip()
                })
            # Horizontal rule
            elif line.strip() == '---':
                if current_paragraph:
                    elements.append(self._create_paragraph(current_paragraph))
                    current_paragraph = []
                elements.append({"type": "horizontal_rule"})
            # List item
            elif line.strip().startswith('- ') or line.strip().startswith('* '):
                if current_paragraph:
                    elements.append(self._create_paragraph(current_paragraph))
                    current_paragraph = []
                elements.append({
                    "type": "list_item",
                    "text": line.strip()[2:]
                })
            # Numbered list
            elif re.match(r'^\d+\.\s', line.strip()):
                if current_paragraph:
                    elements.append(self._create_paragraph(current_paragraph))
                    current_paragraph = []
                elements.append({
                    "type": "numbered_item",
                    "text": re.sub(r'^\d+\.\s', '', line.strip())
                })
            # Empty line
            elif not line.strip():
                if current_paragraph:
                    elements.append(self._create_paragraph(current_paragraph))
                    current_paragraph = []
            # Regular text
            else:
                current_paragraph.append(line)
        
        if current_paragraph:
            elements.append(self._create_paragraph(current_paragraph))
        
        return elements
    
    def _create_paragraph(self, lines: List[str]) -> Dict:
        """Create paragraph element from lines."""
        text = ' '.join(lines)
        return {
            "type": "paragraph",
            "text": text,
            "formatting": self._detect_formatting(text)
        }
    
    def _detect_formatting(self, text: str) -> List[Dict]:
        """Detect text formatting (bold, italic, links)."""
        formatting = []
        
        # Bold
        bold_matches = re.finditer(r'\*\*(.+?)\*\*', text)
        for match in bold_matches:
            formatting.append({
                "type": "bold",
                "start": match.start(),
                "end": match.end() - 2
            })
        
        # Italic
        italic_matches = re.finditer(r'\*(.+?)\*', text)
        for match in italic_matches:
            formatting.append({
                "type": "italic",
                "start": match.start(),
                "end": match.end() - 1
            })
        
        # Links
        link_matches = re.finditer(r'\[(.+?)\]\((.+?)\)', text)
        for match in link_matches:
            formatting.append({
                "type": "link",
                "text": match.group(1),
                "url": match.group(2),
                "start": match.start(),
                "end": match.end()
            })
        
        return formatting
    
    def generate_project_plan_doc(self, context: Dict) -> Dict:
        """Generate Project Management Plan document structure."""
        return {
            "title": f"{context.get('project_name', 'Project')} - Project Management Plan",
            "document_type": "project_management_plan",
            "sections": [
                {
                    "heading": "Executive Summary",
                    "content": "This document outlines the project management approach..."
                },
                {
                    "heading": "Project Objectives",
                    "content": "The primary objectives of this project are..."
                },
                {
                    "heading": "Scope",
                    "content": "The project scope includes..."
                },
                {
                    "heading": "Timeline",
                    "content": f"Project duration: {context.get('duration_weeks', 12)} weeks"
                },
                {
                    "heading": "Resources",
                    "content": "Team composition and resources..."
                },
                {
                    "heading": "Risk Management",
                    "content": "Key risks and mitigation strategies..."
                }
            ],
            "metadata": {
                "created": datetime.now().isoformat(),
                "version": "1.0",
                "author": "Project-Agent"
            }
        }
    
    def generate_weekly_report_doc(self, week_num: int, context: Dict) -> Dict:
        """Generate Weekly Activity Report document structure."""
        return {
            "title": f"Week {week_num} Activity Report",
            "document_type": "weekly_report",
            "sections": [
                {
                    "heading": "Summary",
                    "content": "Weekly summary of activities and progress..."
                },
                {
                    "heading": "Tasks Completed",
                    "content": "List of completed tasks this week..."
                },
                {
                    "heading": "Tasks In Progress",
                    "content": "Current work in progress..."
                },
                {
                    "heading": "Challenges",
                    "content": "Issues and challenges encountered..."
                },
                {
                    "heading": "Next Week Plan",
                    "content": "Planned activities for next week..."
                },
                {
                    "heading": "KPI Progress",
                    "content": "Current KPI status and metrics..."
                }
            ],
            "metadata": {
                "week_number": week_num,
                "created": datetime.now().isoformat(),
                "project": context.get('project_name', '')
            }
        }
    
    def export_to_json(self, doc_structure: Dict, output_path: str = None) -> str:
        """Export document structure to JSON."""
        json_output = json.dumps(doc_structure, indent=2)
        
        if output_path:
            with open(output_path, 'w') as f:
                f.write(json_output)
        
        return json_output


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate Google Docs templates')
    parser.add_argument('--markdown', '-m', help='Path to markdown file to convert')
    parser.add_argument('--template', '-t', 
                       choices=['project_plan', 'weekly_report'],
                       help='Template type to generate')
    parser.add_argument('--week', '-w', type=int, help='Week number for weekly report')
    parser.add_argument('--output', '-o', help='Output JSON file path')
    parser.add_argument('--context', '-c', help='JSON file with context variables')
    
    args = parser.parse_args()
    
    generator = DocsGenerator()
    context = {}
    
    if args.context:
        with open(args.context, 'r') as f:
            context = json.load(f)
    
    if args.markdown:
        result = generator.convert_markdown_to_docs(args.markdown, context)
    elif args.template == 'project_plan':
        result = generator.generate_project_plan_doc(context)
    elif args.template == 'weekly_report':
        result = generator.generate_weekly_report_doc(args.week or 1, context)
    else:
        print("Please specify --markdown or --template")
        return
    
    output = generator.export_to_json(result, args.output)
    print(output)


if __name__ == '__main__':
    main()