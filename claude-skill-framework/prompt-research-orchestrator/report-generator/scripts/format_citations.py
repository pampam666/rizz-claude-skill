#!/usr/bin/env python3
"""
Citation Formatter for Prompt Research Orchestrator

Formats sources into APA citations for research reports.

Usage:
    python format_citations.py --sources <path> --output <path>
"""

import json
import argparse
from datetime import datetime
from typing import List, Dict, Optional


def load_sources(path: str) -> List[Dict]:
    """Load sources from JSON file."""
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        if isinstance(data, list):
            return data
        elif isinstance(data, dict):
            return data.get('sources', [])
        return []


def format_authors(authors: List[str]) -> str:
    """Format author list for APA citation."""
    if not authors:
        return "Unknown"
    
    if len(authors) == 1:
        return authors[0]
    elif len(authors) == 2:
        return f"{authors[0]} & {authors[1]}"
    elif len(authors) <= 20:
        return ", ".join(authors[:-1]) + ", & " + authors[-1]
    else:
        return ", ".join(authors[:19]) + ", ... " + authors[-1]


def format_apa_citation(source: Dict) -> Dict:
    """
    Format a source into APA citation format.
    
    Args:
        source: Source dictionary with metadata
    
    Returns:
        Dictionary with formatted citation
    """
    source_type = source.get('type', 'online')
    authors = source.get('authors', [])
    year = source.get('year', source.get('date', 'n.d.'))
    title = source.get('title', 'Untitled')
    url = source.get('url', '')
    accessed = source.get('accessed', datetime.now().strftime('%Y-%m-%d'))
    
    # Format authors
    author_str = format_authors(authors)
    
    # Format year
    if isinstance(year, str) and len(year) > 4:
        year = year[:4]
    year_str = f"({year})"
    
    # Build citation based on type
    if source_type == 'journal':
        journal = source.get('journal', '')
        volume = source.get('volume', '')
        issue = source.get('issue', '')
        pages = source.get('pages', '')
        doi = source.get('doi', '')
        
        citation = f"{author_str} {year_str}. {title}. {journal}"
        if volume:
            citation += f", {volume}"
            if issue:
                citation += f"({issue})"
        if pages:
            citation += f", {pages}"
        citation += "."
        if doi:
            citation += f" https://doi.org/{doi}"
        elif url:
            citation += f" {url}"
    
    elif source_type == 'arxiv':
        arxiv_id = source.get('arxiv_id', '')
        citation = f"{author_str} {year_str}. {title}. arXiv preprint arXiv:{arxiv_id}."
        if url:
            citation += f"\nURL: {url}"
    
    elif source_type == 'conference':
        conference = source.get('conference', '')
        pages = source.get('pages', '')
        publisher = source.get('publisher', '')
        
        citation = f"{author_str} {year_str}. {title}. In Proceedings of {conference}"
        if pages:
            citation += f" (pp. {pages})"
        if publisher:
            citation += f". {publisher}"
        citation += "."
        if url:
            citation += f" {url}"
    
    elif source_type == 'blog':
        blog_name = source.get('blog_name', '')
        
        citation = f"{author_str} {year_str}. {title} [Blog post]"
        if blog_name:
            citation += f". {blog_name}"
        citation += "."
        if url:
            citation += f"\nURL: {url}"
    
    elif source_type == 'documentation':
        organization = source.get('organization', '')
        site_name = source.get('site_name', '')
        
        citation = f"{organization} {year_str}. {title}."
        if site_name:
            citation += f" {site_name}"
        citation += "."
        if url:
            citation += f"\nURL: {url}"
    
    else:  # online or default
        site_name = source.get('site_name', '')
        
        citation = f"{author_str} {year_str}. {title}."
        if site_name:
            citation += f" {site_name}"
        citation += "."
        if url:
            citation += f"\nURL: {url}"
    
    # Add accessed date for online sources
    if url and accessed:
        citation += f" Accessed: {accessed}"
    
    # Generate in-text citation
    if authors:
        first_author = authors[0].split(',')[-1].strip() if ',' in authors[0] else authors[0].split()[-1]
        if len(authors) == 1:
            in_text = f"({first_author}, {year})"
        elif len(authors) == 2:
            second_author = authors[1].split(',')[-1].strip() if ',' in authors[1] else authors[1].split()[-1]
            in_text = f"({first_author} & {second_author}, {year})"
        else:
            in_text = f"({first_author} et al., {year})"
    else:
        in_text = f"({title[:20]}..., {year})"
    
    return {
        'id': source.get('id', ''),
        'apa_format': citation,
        'in_text': in_text,
        'source_url': url,
        'type': source_type
    }


def format_all_citations(sources: List[Dict]) -> List[Dict]:
    """
    Format all sources into citations.
    
    Args:
        sources: List of source dictionaries
    
    Returns:
        List of formatted citation dictionaries
    """
    citations = []
    for source in sources:
        citation = format_apa_citation(source)
        citations.append(citation)
    
    # Sort alphabetically by first author
    citations.sort(key=lambda x: x['apa_format'].split()[0] if x['apa_format'] else '')
    
    return citations


def save_citations(citations: List[Dict], output_path: str):
    """Save formatted citations to JSON file."""
    output = {
        'citations': citations,
        'count': len(citations),
        'generated_at': datetime.now().isoformat()
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser(description='Format sources into APA citations')
    parser.add_argument('--sources', required=True, help='Path to sources JSON file')
    parser.add_argument('--output', required=True, help='Path for output citations JSON file')
    
    args = parser.parse_args()
    
    # Load sources
    sources = load_sources(args.sources)
    
    # Format citations
    citations = format_all_citations(sources)
    
    # Save citations
    save_citations(citations, args.output)
    
    print(f"Formatted {len(citations)} citations")
    print(f"Output saved to: {args.output}")


if __name__ == '__main__':
    main()