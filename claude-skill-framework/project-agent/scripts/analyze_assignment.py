#!/usr/bin/env python3
"""
Analyze Internship Assignment Letter
Extracts KPIs, deliverables, and project structure from assignment documents.
"""

import re
import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from pathlib import Path


class AssignmentAnalyzer:
    """Analyzes internship assignment letters and extracts key information."""
    
    def __init__(self):
        self.kpi_patterns = [
            r'(\d+(?:\.\d+)?)\s*%?\s*(?:increase|growth|target|goal)',
            r'(?:target|goal|objective)[:\s]+(\d+(?:\.\d+)?)',
            r'(\d+)\s*(?:articles?|posts?|content|pieces)',
            r'(\d+)\s*(?:followers?|engagement|likes?|views?)',
        ]
        
    def analyze(self, document_path: str) -> Dict:
        """
        Analyze an internship assignment document.
        
        Args:
            document_path: Path to the assignment document (txt, md, or pdf)
            
        Returns:
            Dict containing extracted information
        """
        content = self._read_document(document_path)
        
        result = {
            "document_path": document_path,
            "analyzed_at": datetime.now().isoformat(),
            "company_info": self._extract_company_info(content),
            "internship_period": self._extract_period(content),
            "kpis": self._extract_kpis(content),
            "deliverables": self._extract_deliverables(content),
            "team_structure": self._extract_team_structure(content),
            "raw_text_length": len(content)
        }
        
        return result
    
    def _read_document(self, path: str) -> str:
        """Read document content from file."""
        file_path = Path(path)
        
        if not file_path.exists():
            raise FileNotFoundError(f"Document not found: {path}")
        
        if file_path.suffix.lower() == '.pdf':
            try:
                import PyPDF2
                with open(file_path, 'rb') as f:
                    reader = PyPDF2.PdfReader(f)
                    return '\n'.join(page.extract_text() for page in reader.pages)
            except ImportError:
                raise ImportError("PyPDF2 required for PDF parsing. Install with: pip install PyPDF2")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def _extract_company_info(self, content: str) -> Dict:
        """Extract company name and basic information."""
        info = {
            "name": None,
            "industry": None,
            "department": None
        }
        
        # Common patterns for company names
        company_patterns = [
            r'(?:PT|CV|Company|Perusahaan)\s+([A-Za-z\s]+)',
            r'at\s+([A-Z][A-Za-z\s]+)',
            r'([A-Z][A-Za-z\s]+)\s+(?:Internship|Magang)'
        ]
        
        for pattern in company_patterns:
            match = re.search(pattern, content)
            if match:
                info["name"] = match.group(1).strip()
                break
        
        return info
    
    def _extract_period(self, content: str) -> Dict:
        """Extract internship start and end dates."""
        period = {
            "start_date": None,
            "end_date": None,
            "duration_weeks": None
        }
        
        # Date patterns
        date_patterns = [
            r'(\d{1,2}[/\-]\d{1,2}[/\-]\d{2,4})',
            r'(\d{4}[/\-]\d{1,2}[/\-]\d{1,2})',
            r'((?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4})'
        ]
        
        dates = []
        for pattern in date_patterns:
            dates.extend(re.findall(pattern, content, re.IGNORECASE))
        
        if len(dates) >= 2:
            period["start_date"] = dates[0]
            period["end_date"] = dates[1]
            
            # Try to calculate duration
            try:
                start = self._parse_date(dates[0])
                end = self._parse_date(dates[1])
                if start and end:
                    delta = end - start
                    period["duration_weeks"] = delta.days // 7
            except:
                pass
        
        # Duration patterns if dates not found
        duration_match = re.search(r'(\d+)\s*(?:weeks?|months?|bulan|minggu)', content, re.IGNORECASE)
        if duration_match and not period["duration_weeks"]:
            period["duration_weeks"] = int(duration_match.group(1))
            if re.search(r'month|bulan', content, re.IGNORECASE):
                period["duration_weeks"] *= 4
        
        return period
    
    def _parse_date(self, date_str: str) -> Optional[datetime]:
        """Parse date string to datetime object."""
        formats = [
            '%d/%m/%Y', '%d-%m-%Y', '%Y/%m/%d', '%Y-%m-%d',
            '%d/%m/%y', '%d-%m-%y', '%B %d, %Y', '%B %d %Y'
        ]
        
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        return None
    
    def _extract_kpis(self, content: str) -> List[Dict]:
        """Extract KPIs and targets from the document."""
        kpis = []
        
        # Look for numerical targets
        for pattern in self.kpi_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                context_start = max(0, match.start() - 50)
                context_end = min(len(content), match.end() + 50)
                context = content[context_start:context_end]
                
                kpi = {
                    "value": float(match.group(1)) if '.' in match.group(1) else int(match.group(1)),
                    "context": context.strip(),
                    "type": self._classify_kpi(context)
                }
                
                if kpi not in kpis:
                    kpis.append(kpi)
        
        return kpis
    
    def _classify_kpi(self, context: str) -> str:
        """Classify the type of KPI based on context."""
        context_lower = context.lower()
        
        if any(word in context_lower for word in ['follower', 'engagement', 'like', 'share']):
            return "social_media"
        elif any(word in context_lower for word in ['article', 'content', 'post', 'blog']):
            return "content"
        elif any(word in context_lower for word in ['traffic', 'visitor', 'view']):
            return "traffic"
        elif any(word in context_lower for word in ['seo', 'keyword', 'ranking']):
            return "seo"
        elif any(word in context_lower for word in ['conversion', 'lead', 'sale']):
            return "conversion"
        else:
            return "general"
    
    def _extract_deliverables(self, content: str) -> List[Dict]:
        """Extract expected deliverables from the document."""
        deliverables = []
        
        # Look for deliverable patterns
        deliverable_patterns = [
            r'(?:deliverable|output|hasil|tugas)[:\s]+([^\n.]+)',
            r'(?:create|write|produce|make)\s+(\d+\s+[^\n.]+)',
            r'[-•]\s+([A-Z][^\n]+)'
        ]
        
        for pattern in deliverable_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                deliverable = {
                    "description": match.strip(),
                    "category": self._categorize_deliverable(match)
                }
                if deliverable not in deliverables:
                    deliverables.append(deliverable)
        
        return deliverables
    
    def _categorize_deliverable(self, description: str) -> str:
        """Categorize a deliverable based on its description."""
        desc_lower = description.lower()
        
        if any(word in desc_lower for word in ['article', 'blog', 'writing', 'content']):
            return "content"
        elif any(word in desc_lower for word in ['social', 'instagram', 'linkedin', 'tiktok']):
            return "social_media"
        elif any(word in desc_lower for word in ['report', 'analysis', 'research']):
            return "research"
        elif any(word in desc_lower for word in ['video', 'design', 'creative']):
            return "creative"
        elif any(word in desc_lower for word in ['presentation', 'meeting']):
            return "presentation"
        else:
            return "other"
    
    def _extract_team_structure(self, content: str) -> Dict:
        """Extract team structure information."""
        structure = {
            "team_size": None,
            "roles": []
        }
        
        # Look for team size
        size_match = re.search(r'(\d+)\s*(?:people|person|members?|orang)', content, re.IGNORECASE)
        if size_match:
            structure["team_size"] = int(size_match.group(1))
        
        # Look for role mentions
        role_patterns = [
            r'(?:supervisor|manager|mentor|supervisor)\s*[:\-]?\s*([A-Za-z\s]+)',
            r'([A-Za-z\s]+)\s*[-–]\s*(?:supervisor|manager|mentor|lead)'
        ]
        
        for pattern in role_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                role = match.strip()
                if role and len(role) > 2 and role not in structure["roles"]:
                    structure["roles"].append(role)
        
        return structure


def main():
    """Main entry point for command-line usage."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Analyze internship assignment letter')
    parser.add_argument('document', help='Path to assignment document')
    parser.add_argument('--output', '-o', help='Output JSON file path')
    parser.add_argument('--pretty', '-p', action='store_true', help='Pretty print output')
    
    args = parser.parse_args()
    
    analyzer = AssignmentAnalyzer()
    result = analyzer.analyze(args.document)
    
    output_json = json.dumps(result, indent=2) if args.pretty else json.dumps(result)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output_json)
        print(f"Analysis saved to {args.output}")
    else:
        print(output_json)


if __name__ == '__main__':
    main()