#!/usr/bin/env python3
"""
Data Validator for Market Research Intelligence Skill

This script validates input data format for the market-research-intelligence skill.
It Checks CSV, JSON, and mixed format inputs for required fields.

Usage:
    python data-validator.py <input_file>
    python data-validator.py --csv <input_file>
    python data-validator.py --json <input_file>
"""

import argparse
import json
import csv
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional


class DataValidator:
    """Validates competitor data input for market research analysis."""
    
    # Required fields by pillar
    SEO_FIELDS = [
        'domain_rating', 'domain_authority', 'dr', 'da',
        'organic_traffic', 'traffic',
        'referring_domains', 'backlinks',
        'keywords', 'top_keywords'
    ]
    
    CONTENT_FIELDS = [
        'instagram', 'facebook', 'youtube', 'tiktok', 'linkedin',
        'followers', 'engagement', 'posts',
        'social_media'
    ]
    
    TECH_FIELDS = [
        'cms', 'wordpress', 'elementor', 'webflow',
        'analytics', 'google_analytics', 'meta_pixel',
        'chatbot', 'tidio', 'intercom',
        'hosting', 'cdn',
        'tech_stack', 'automation'
    ]
    
    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.data: Dict = {}
        
    def validate(self) -> Tuple[bool, Dict]:
        """Main validation entry point."""
        suffix = self.filepath.suffix.lower()
        
        if suffix == '.csv':
            return self._validate_csv()
        elif suffix == '.json':
            return self._validate_json()
        elif suffix in ['.txt', '.md']:
            return self._validate_text()
        else:
            # Try to auto-detect format
            content = self.filepath.read_text(encoding='utf-8', errors='ignore')
            if content.strip().startswith('{'):
                return self._validate_json()
            elif ',' in content.split('\n')[0]:
                return self._validate_csv()
            else:
                return self._validate_text()
    
    def _validate_csv(self) -> Tuple[bool, Dict]:
        """Validate CSV format input."""
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                
            if not rows:
                self.errors.append("CSV file is empty")
                return False, self._get_results()
            
            # Check for required fields
            headers = [h.lower().strip() for h in rows[0].keys()]
            
            seo_found = any(h in headers for h in self.SEO_FIELDS)
            content_found = any(h in headers for h in self.CONTENT_FIELDS)
            tech_found = any(h in headers for h in self.TECH_FIELDS)
            
            if not seo_found and not content_found and not tech_found:
                self.errors.append(
                    "No recognizable data pillars found. "
                    f"Expected at least one of: {self.SEO_FIELDS + self.CONTENT_FIELDS + self.TECH_FIELDS}"
                )
            
            self.data = {
                'format': 'csv',
                'rows': len(rows),
                'headers': headers,
                'seo_detected': seo_found,
                'content_detected': content_found,
                'tech_detected': tech_found
            }
            
            return len(self.errors) == 00 self._get_results()
            
        except Exception as e:
            self.errors.append(f"CSV parsing error: {str(e)}")
            return False, self._get_results()
    
    def _validate_json(self) -> Tuple[bool, Dict]:
        """Validate JSON format input."""
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if not data:
                self.errors.append("JSON file is empty or invalid")
                return False, self._get_results()
            
            # Recursively check for pillar fields
            def check_nested(obj: Dict, fields: List[str]) -> bool:
                found = False
                for key, value in obj.items():
                    if key.lower() in [f.lower() for f in fields]:
                        found = True
                    if isinstance(value, dict):
                        if check_nested(value, fields):
                            found = True
                return found
            
            seo_found = check_nested(data, self.SEO_FIELDS)
            content_found = check_nested(data, self.CONTENT_FIELDS)
            tech_found = check_nested(data, self.TECH_FIELDS)
            
            if not seo_found and not content_found and not tech_found:
                self.warnings.append(
                    "Warning: Limited pillar data detected. "
                    "For comprehensive analysis, provide data for all 3 pillars."
                )
            
            self.data = {
                'format': 'json',
                'seo_detected': seo_found,
                'content_detected': content_found,
                'tech_detected': tech_found,
                'keys': list(data.keys())
            }
            
            return len(self.errors) == 0, self._get_results()
            
        except json.JSONDecodeError as e:
            self.errors.append(f"JSON parsing error: {str(e)}")
            return False, self._get_results()
    
    def _validate_text(self) -> Tuple[bool, Dict]:
        """Validate plain text/mixed format input."""
        try:
            content = self.filepath.read_text(encoding='utf-8')
            
            if not content.strip():
                self.errors.append("File is empty")
                return False, self._get_results()
            
            content_lower = content.lower()
            
            # Check for keywords indicating data types
            seo_keywords = ['domain rating', 'dr:', 'traffic', 'keyword', 'backlink', 'referring domain']
            content_keywords = ['instagram', 'facebook', 'youtube', 'tiktok', 'follower', 'engagement', 'social']
            tech_keywords = ['cms', 'wordpress', 'analytics', 'chatbot', 'hosting', 'cdn', 'automation']
            
            seo_found = any(kw in content_lower for kw in seo_keywords)
            content_found = any(kw in content_lower for kw in content_keywords)
            tech_found = any(kw in content_lower for kw in tech_keywords)
            
            if not seo_found and not content_found and not tech_found:
                self.warnings.append(
                    "Warning: No recognizable data pillars found. "
                    "Content may not be in expected format."
                )
            
            self.data = {
                'format': 'text',
                'seo_detected': seo_found,
                'content_detected': content_found,
                'tech_detected': tech_found,
                'length': len(content)
            }
            
            return len(self.errors) == 0, self._get_results()
            
        except Exception as e:
            self.errors.append(f"Text file reading error: {str(e)}")
            return False, self._get_results()
    
    def _get_results(self) -> Dict:
        """Compile validation results."""
        return {
            'valid': len(self.errors) == 00,
            'errors': self.errors,
            'warnings': self.warnings,
            'data': self.data
        }


def print_report(results: Dict) -> None:
    """Print validation report."""
    print("\n" + "="*60)
    print("DATA VALIDATION REPORT")
    print("="*60 + "\n")
    
    if results['valid']:
        print("✅ Status: VALID")
    else:
        print("❌ Status: INVALID")
    
    if results['errors']:
        print("\nErrors:")
        for error in results['errors']:
            print(f"  - {error}")
    
    if results['warnings']:
        print("\nWarnings:")
        for warning in results['warnings']:
            print(f"  ⚠ {warning}")
    
    print("\nDetected Data:")
    for key, value in results['data'].items():
        print(f"  {key}: {value}")
    
    print("\n" + "="*60)
    
    # Provide recommendations
    if results['data'].get('seo_detected') and not results['data'].get('content_detected'):
        print("💡 Recommendation: Add social media data for Content Ecosystem analysis")
    if results['data'].get('content_detected') and not results['data'].get('seo_detected'):
        print("💡 Recommendation: Add SEO metrics for SEO Authority analysis")
    if results['data'].get('tech_detected') and not results['data'].get('seo_detected'):
        print("💡 Recommendation: Add SEO data for complete analysis")
    
    print("\nReady to use market-research-intelligence skill for analysis.")


def main():
    parser = argparse.ArgumentParser(
        description='Validate competitor data input for market research analysis'
    )
    parser.add_argument(
        'input_file',
        help='Path to the input data file'
    )
    parser.add_argument(
        '--csv',
        action='store_true',
        help='Force CSV format validation'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Force JSON format validation'
    )
    
    args = parser.parse_args()
    
    if not Path(args.input_file).exists():
        print(f"Error: File not found: {args.input_file}")
        sys.exit(1)
    
    validator = DataValidator(args.input_file)
    results = validator.validate()
    print_report(results)


if __name__ == '__main__':
    main()