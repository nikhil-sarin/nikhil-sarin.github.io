#!/usr/bin/env python3
"""
Script to find new papers by Nikhil Sarin on arXiv and add them to Recent News
in the exact style used in the about page.
"""

import re
import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import argparse

def search_arxiv_papers(max_results=100):
    """Search for papers by Nikhil Sarin on arXiv."""
    search_queries = [
        "au:Sarin+AND+au:Nikhil",
        "au:\"Nikhil+Sarin\"", 
        "au:Sarin,+Nikhil"
    ]
    
    all_papers = []
    seen_ids = set()
    
    for query in search_queries:
        url = f"http://export.arxiv.org/api/query?search_query={query}&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            
            root = ET.fromstring(response.content)
            ns = {'atom': 'http://www.w3.org/2005/Atom'}
            
            for entry in root.findall('atom:entry', ns):
                arxiv_id = entry.find('atom:id', ns).text.split('/')[-1]
                
                if arxiv_id in seen_ids:
                    continue
                seen_ids.add(arxiv_id)
                
                title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
                
                authors = []
                for author in entry.findall('atom:author', ns):
                    name = author.find('atom:name', ns).text
                    authors.append(name)
                
                published = entry.find('atom:published', ns).text
                published_date = datetime.strptime(published[:10], '%Y-%m-%d').date()
                
                # Only include papers where Nikhil Sarin is actually an author
                if any('sarin' in author.lower() and ('nikhil' in author.lower() or 'n.' in author.lower()) 
                       for author in authors):
                    
                    # Skip LIGO collaboration papers
                    authors_str = ' '.join(authors).lower()
                    title_lower = title.lower()
                    
                    # Skip papers that are clearly LIGO collaboration papers
                    if any(keyword in title_lower or keyword in authors_str 
                           for keyword in ['ligo scientific collaboration', 'ligo-virgo', 'ligo/virgo', 
                                          'virgo collaboration', 'ligo-virgo-kagra', 'kagra collaboration',
                                          'gwtc-', 'gravitational-wave transient catalog']):
                        continue
                    
                    all_papers.append({
                        'arxiv_id': arxiv_id,
                        'title': title,
                        'authors': authors,
                        'published_date': published_date,
                        'arxiv_url': f"https://arxiv.org/abs/{arxiv_id}"
                    })
        except Exception as e:
            print(f"Error with query {query}: {e}")
            continue
    
    # Sort by publication date (most recent first)
    all_papers.sort(key=lambda x: x['published_date'], reverse=True)
    return all_papers

def extract_existing_arxiv_ids(about_content):
    """Extract all arXiv IDs already mentioned in the about page."""
    # Look for patterns like arxiv.org/abs/1234.5678 or arXiv](https://arxiv.org/abs/1234.5678)
    arxiv_pattern = r'arxiv\.org/abs/(\d{4}\.\d{4,5})'
    existing_ids = set(re.findall(arxiv_pattern, about_content, re.IGNORECASE))
    return existing_ids

def format_paper_news(paper):
    """Format paper in the exact style used in the about page."""
    # Determine the first author for the news format
    first_author = paper['authors'][0] if paper['authors'] else "Unknown"
    
    # Check if Nikhil Sarin is first author
    if 'sarin' in first_author.lower() and ('nikhil' in first_author.lower() or 'n.' in first_author.lower()):
        # First author format: "Sarin et al. YYYY"
        author_str = "Sarin et al."
    else:
        # Co-author format: "FirstAuthor et al. YYYY" 
        last_name = first_author.split()[-1]
        author_str = f"{last_name} et al."
    
    # Format date as "Day Month YYYY" (e.g., "4th June 2025")
    day = paper['published_date'].day
    if day in [1, 21, 31]:
        day_suffix = "st"
    elif day in [2, 22]:
        day_suffix = "nd" 
    elif day in [3, 23]:
        day_suffix = "rd"
    else:
        day_suffix = "th"
    
    date_str = f"{day}{day_suffix} {paper['published_date'].strftime('%B %Y')}"
    
    # Format the news entry in your exact style
    title = paper['title']
    year = paper['published_date'].year
    arxiv_url = paper['arxiv_url']
    
    # Note: Your format typically shows "submitted" for new papers, 
    # but we can't determine the venue from arXiv alone
    news_entry = f"* {date_str}: {author_str} {year} - _{title}_ submitted. Check it out on [arXiv]({arxiv_url})."
    
    return news_entry

def update_about_page(about_path, new_papers, dry_run=False):
    """Update the about page with new papers."""
    with open(about_path, 'r') as f:
        content = f.read()
    
    # Extract existing arXiv IDs
    existing_ids = extract_existing_arxiv_ids(content)
    
    # Filter out papers that are already mentioned
    truly_new_papers = []
    for paper in new_papers:
        arxiv_id = paper['arxiv_id'].split('v')[0]  # Remove version number
        if arxiv_id not in existing_ids:
            truly_new_papers.append(paper)
    
    if not truly_new_papers:
        print("No new papers found that aren't already in the about page.")
        return False
    
    print(f"Found {len(truly_new_papers)} new papers:")
    for paper in truly_new_papers:
        print(f"  - {paper['title']} ({paper['published_date']})")
    
    if dry_run:
        print("\nDry run - would add these entries:")
        for paper in truly_new_papers:
            print(format_paper_news(paper))
        return False
    
    # Find the Recent News section
    news_pattern = r'(# Recent News\s*\n)(.*?)(\n# |\n## |\Z)'
    news_match = re.search(news_pattern, content, re.DOTALL)
    
    if not news_match:
        print("Could not find '# Recent News' section in about page.")
        return False
    
    # Format new entries
    new_entries = []
    for paper in truly_new_papers:
        new_entries.append(format_paper_news(paper))
    
    # Add new entries at the top of the news section
    existing_news = news_match.group(2).strip()
    if existing_news:
        updated_news = "\n".join(new_entries) + "\n" + existing_news
    else:
        updated_news = "\n".join(new_entries)
    
    # Replace the news section
    new_content = content.replace(
        news_match.group(0),
        news_match.group(1) + updated_news + news_match.group(3)
    )
    
    # Write updated content
    with open(about_path, 'w') as f:
        f.write(new_content)
    
    print(f"Added {len(new_entries)} new papers to the about page.")
    return True

def main():
    parser = argparse.ArgumentParser(description='Update Recent News with new papers from arXiv')
    parser.add_argument('--about-path', type=str,
                       default='/Users/nikhil/Documents/postdoc/nikhil-sarin.github.io/_pages/about.md',
                       help='Path to about page markdown file')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be added without making changes')
    parser.add_argument('--max-results', type=int, default=100,
                       help='Maximum number of papers to fetch from arXiv')
    
    args = parser.parse_args()
    
    print("Searching arXiv for papers by Nikhil Sarin...")
    papers = search_arxiv_papers(args.max_results)
    print(f"Found {len(papers)} total papers")
    
    # Only consider recent papers (last 2 years to avoid clutter)
    recent_papers = [p for p in papers if p['published_date'].year >= 2023]
    print(f"Found {len(recent_papers)} papers from 2023 onwards")
    
    if not recent_papers:
        print("No recent papers found.")
        return
    
    # Update about page
    updated = update_about_page(args.about_path, recent_papers, args.dry_run)
    
    if updated and not args.dry_run:
        print(f"Successfully updated {args.about_path}")

if __name__ == "__main__":
    main()