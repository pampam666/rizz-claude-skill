#!/usr/bin/env python3
"""
Run QA Checks Script

Performs quality assurance validation on all campaign deliverables.
Checks brand voice, SEO, content quality, and deliverable completeness.

Usage: python run_qa_checks.py <workflow_state.json>
"""

import json
import sys
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Tuple


def load_workflow_state(state_path: str) -> Dict[str, Any]:
    """Load workflow state from JSON file."""
    with open(state_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def check_brand_voice(article_path: str, brand_dna: Dict) -> Dict[str, Any]:
    """Check if article matches brand voice guidelines."""
    issues = []
    score = 1.0
    
    try:
        with open(article_path, 'r', encoding='utf-8') as f:
            content = f.read().lower()
    except FileNotFoundError:
        return {"status": "fail", "score": 0, "issues": ["File not found"]}
    
    voice = brand_dna.get('voice_and_tone', {})
    
    # Check don't keywords
    dont_keywords = voice.get('dont_keywords', [])
    for keyword in dont_keywords:
        if keyword.lower() in content:
            issues.append(f"Found 'don't' keyword: {keyword}")
            score -= 0.1
    
    # Check do keywords presence
    do_keywords = voice.get('do_keywords', [])
    found_do = sum(1 for kw in do_keywords if kw.lower() in content)
    if do_keywords and found_do < len(do_keywords) * 0.5:
        issues.append("Insufficient 'do' keywords found")
        score -= 0.1
    
    return {
        "status": "pass" if score >= 0.7 else "fail",
        "score": round(max(score, 0), 2),
        "issues": issues
    }


def check_seo(article_path: str) -> Dict[str, Any]:
    """Check SEO optimization of article."""
    issues = []
    score = 1.0
    
    try:
        with open(article_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return {"status": "fail", "score": 0, "issues": ["File not found"]}
    
    # Check frontmatter
    if not content.startswith('---'):
        issues.append("Missing frontmatter")
        score -= 0.2
    
    # Check meta description
    if 'description:' in content[:500]:
        desc_match = re.search(r'description:\s*["\'](.+?)["\']', content[:500])
        if desc_match:
            desc_len = len(desc_match.group(1))
            if desc_len < 150 or desc_len > 160:
                issues.append(f"Meta description length: {desc_len} (target: 150-160)")
                score -= 0.1
    else:
        issues.append("Missing meta description")
        score -= 0.15
    
    # Check title
    if 'title:' in content[:500]:
        title_match = re.search(r'title:\s*["\'](.+?)["\']', content[:500])
        if title_match:
            title_len = len(title_match.group(1))
            if title_len > 60:
                issues.append(f"Title too long: {title_len} chars")
                score -= 0.1
    else:
        issues.append("Missing title in frontmatter")
        score -= 0.15
    
    # Check H2 count
    h2_count = len(re.findall(r'^##\s+', content, re.MULTILINE))
    if h2_count < 3:
        issues.append(f"Insufficient H2 headings: {h2_count} (min: 3)")
        score -= 0.1
    
    # Check internal links
    internal_links = len(re.findall(r'\[.*?\]\(/.*?\)', content))
    if internal_links < 3:
        issues.append(f"Insufficient internal links: {internal_links} (min: 3)")
        score -= 0.1
    
    return {
        "status": "pass" if score >= 0.7 else "warning" if score >= 0.5 else "fail",
        "score": round(max(score, 0), 2),
        "issues": issues,
        "metrics": {
            "h2_count": h2_count,
            "internal_links": internal_links
        }
    }


def check_content_quality(article_path: str) -> Dict[str, Any]:
    """Check content quality metrics."""
    issues = []
    score = 1.0
    
    try:
        with open(article_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return {"status": "fail", "score": 0, "issues": ["File not found"]}
    
    # Remove frontmatter for word count
    body = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
    
    # Word count
    words = len(body.split())
    if words < 1200:
        issues.append(f"Word count low: {words} (min: 1200)")
        score -= 0.2
    elif words > 3000:
        issues.append(f"Word count high: {words} (max: 3000)")
        score -= 0.1
    
    # Check structure
    if not re.search(r'^##\s+.*introduction', body, re.IGNORECASE | re.MULTILINE):
        if 'introduction' not in body[:500].lower():
            issues.append("Missing clear introduction")
            score -= 0.1
    
    if not re.search(r'^##\s+.*conclusion', body, re.IGNORECASE | re.MULTILINE):
        if 'conclusion' not in body[-500:].lower():
            issues.append("Missing clear conclusion")
            score -= 0.1
    
    # Check for CTA
    cta_patterns = ['get started', 'learn more', 'contact us', 'sign up', 'try free']
    if not any(pattern in body.lower() for pattern in cta_patterns):
        issues.append("No clear CTA detected")
        score -= 0.1
    
    return {
        "status": "pass" if score >= 0.7 else "warning" if score >= 0.5 else "fail",
        "score": round(max(score, 0), 2),
        "issues": issues,
        "metrics": {
            "word_count": words
        }
    }


def check_deliverables(state: Dict) -> Dict[str, Any]:
    """Check all deliverables exist and are valid."""
    issues = []
    score = 1.0
    deliverables = state.get('deliverables', {})
    
    # Check research document
    research_path = deliverables.get('research_document_path', '')
    if research_path:
        if not Path(research_path).exists():
            issues.append(f"Research document not found: {research_path}")
            score -= 0.3
    else:
        issues.append("Research document path not set")
        score -= 0.2
    
    # Check campaign plan
    plan_path = deliverables.get('campaign_plan_path', '')
    if plan_path:
        if not Path(plan_path).exists():
            issues.append(f"Campaign plan not found: {plan_path}")
            score -= 0.3
    else:
        issues.append("Campaign plan path not set")
        score -= 0.2
    
    # Check articles
    article_paths = deliverables.get('article_paths', [])
    if article_paths:
        missing = [p for p in article_paths if not Path(p).exists()]
        if missing:
            issues.append(f"Missing articles: {len(missing)}")
            score -= 0.1 * len(missing)
    else:
        issues.append("No article paths set")
        score -= 0.3
    
    return {
        "status": "pass" if score >= 0.7 else "fail",
        "score": round(max(score, 0), 2),
        "issues": issues,
        "deliverables_checked": len(deliverables)
    }


def run_all_qa_checks(state_path: str) -> Dict[str, Any]:
    """Run all QA checks and return comprehensive report."""
    state = load_workflow_state(state_path)
    brand_dna = state.get('brand_dna', {})
    deliverables = state.get('deliverables', {})
    article_paths = deliverables.get('article_paths', [])
    
    results = {
        "qa_timestamp": datetime.now().isoformat(),
        "workflow_id": state.get('workflow_id', 'unknown'),
        "brand_voice": {"status": "skip", "score": 0, "issues": []},
        "seo_quality": {"status": "skip", "score": 0, "issues": [], "articles_checked": 0},
        "content_quality": {"status": "skip", "score": 0, "issues": [], "articles_checked": 0},
        "deliverable_validation": {"status": "skip", "score": 0, "issues": []},
        "overall": {"status": "pending", "score": 0, "ready_for_delivery": False}
    }
    
    scores = []
    
    # Brand voice checks
    if article_paths and brand_dna:
        voice_scores = []
        voice_issues = []
        for path in article_paths[:5]:  # Check first 5
            result = check_brand_voice(path, brand_dna)
            voice_scores.append(result['score'])
            voice_issues.extend(result.get('issues', []))
        
        if voice_scores:
            avg_score = sum(voice_scores) / len(voice_scores)
            results['brand_voice'] = {
                "status": "pass" if avg_score >= 0.7 else "fail",
                "score": round(avg_score, 2),
                "issues": voice_issues[:5]  # Limit issues
            }
            scores.append(avg_score)
    
    # SEO checks
    if article_paths:
        seo_scores = []
        seo_issues = []
        for path in article_paths:
            result = check_seo(path)
            seo_scores.append(result['score'])
            seo_issues.extend(result.get('issues', []))
        
        avg_score = sum(seo_scores) / len(seo_scores)
        results['seo_quality'] = {
            "status": "pass" if avg_score >= 0.7 else "warning" if avg_score >= 0.5 else "fail",
            "score": round(avg_score, 2),
            "issues": seo_issues[:5],
            "articles_checked": len(article_paths)
        }
        scores.append(avg_score)
    
    # Content quality checks
    if article_paths:
        content_scores = []
        content_issues = []
        total_words = 0
        
        for path in article_paths:
            result = check_content_quality(path)
            content_scores.append(result['score'])
            content_issues.extend(result.get('issues', []))
            total_words += result.get('metrics', {}).get('word_count', 0)
        
        avg_score = sum(content_scores) / len(content_scores)
        avg_words = total_words / len(article_paths) if article_paths else 0
        results['content_quality'] = {
            "status": "pass" if avg_score >= 0.7 else "warning" if avg_score >= 0.5 else "fail",
            "score": round(avg_score, 2),
            "issues": content_issues[:5],
            "articles_checked": len(article_paths),
            "average_word_count": round(avg_words)
        }
        scores.append(avg_score)
    
    # Deliverable validation
    deliv_result = check_deliverables(state)
    results['deliverable_validation'] = deliv_result
    scores.append(deliv_result['score'])
    
    # Overall score
    if scores:
        overall_score = sum(scores) / len(scores)
        results['overall'] = {
            "status": "pass" if overall_score >= 0.7 else "warning" if overall_score >= 0.5 else "fail",
            "score": round(overall_score, 2),
            "ready_for_delivery": overall_score >= 0.7
        }
    
    return results


def main():
    """CLI entry point."""
    if len(sys.argv) < 2:
        print("Usage: python run_qa_checks.py <workflow_state.json>")
        print("\nExample: python run_qa_checks.py workflow_state.json")
        sys.exit(1)
    
    state_path = sys.argv[1]
    results = run_all_qa_checks(state_path)
    
    print(json.dumps(results, indent=2))
    
    # Exit with appropriate code
    if results['overall']['status'] == 'pass':
        sys.exit(0)
    elif results['overall']['status'] == 'warning':
        sys.exit(1)
    else:
        sys.exit(2)


if __name__ == "__main__":
    main()