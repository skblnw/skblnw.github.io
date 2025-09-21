#!/usr/bin/env python3
"""
Import publications from PubMed/NCBI or BibTeX files

This script can import publications from various sources and format them
for the Jekyll website.

Usage:
    python import_publications.py --pubmed "Doe J[Author]"
    python import_publications.py --bibtex publications.bib
    python import_publications.py --csv publications_new.csv
"""

import argparse
import csv
import json
import re
from pathlib import Path
from datetime import datetime

# You may need to install: pip install biopython
# from Bio import Entrez

PROJECT_ROOT = Path(__file__).parent.parent
PAPERS_CSV = PROJECT_ROOT / "_data" / "papers.csv"

def parse_bibtex(bibtex_file):
    """Parse BibTeX file and extract publication data"""
    publications = []
    
    with open(bibtex_file, 'r') as f:
        content = f.read()
    
    # Simple BibTeX parser (for basic cases)
    entries = re.findall(r'@\w+\{([^}]+)\}', content, re.DOTALL)
    
    for entry in entries:
        pub = {}
        
        # Extract fields
        title_match = re.search(r'title\s*=\s*["{]([^"}]+)["}]', entry)
        author_match = re.search(r'author\s*=\s*["{]([^"}]+)["}]', entry)
        journal_match = re.search(r'journal\s*=\s*["{]([^"}]+)["}]', entry)
        year_match = re.search(r'year\s*=\s*["{](\d{4})["}]', entry)
        doi_match = re.search(r'doi\s*=\s*["{]([^"}]+)["}]', entry)
        url_match = re.search(r'url\s*=\s*["{]([^"}]+)["}]', entry)
        
        if title_match:
            pub['title'] = title_match.group(1)
        if author_match:
            pub['authors'] = author_match.group(1).replace(' and ', ', ')
        if journal_match:
            pub['journal'] = journal_match.group(1)
        if year_match:
            pub['date'] = year_match.group(1)
        if doi_match:
            pub['doi'] = doi_match.group(1)
            pub['link'] = f"https://doi.org/{doi_match.group(1)}"
        elif url_match:
            pub['link'] = url_match.group(1)
        
        if pub:
            publications.append(pub)
    
    return publications

def fetch_pubmed(query, max_results=100):
    """Fetch publications from PubMed"""
    # Note: This requires Bio.Entrez from biopython
    # Uncomment and modify if you want to use this functionality
    
    publications = []
    
    # Example structure (implement actual PubMed fetching if needed)
    # Entrez.email = "your-email@university.edu"
    # handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    # record = Entrez.read(handle)
    # handle.close()
    # 
    # id_list = record["IdList"]
    # handle = Entrez.efetch(db="pubmed", id=id_list, rettype="medline", retmode="xml")
    # records = Entrez.read(handle)
    # handle.close()
    # 
    # for record in records['PubmedArticle']:
    #     # Extract publication data from record
    #     pass
    
    print(f"PubMed fetching not implemented. Query: {query}")
    return publications

def merge_csv(existing_csv, new_data):
    """Merge new publication data with existing CSV"""
    
    # Read existing data
    existing = []
    if existing_csv.exists():
        with open(existing_csv, 'r') as f:
            reader = csv.DictReader(f)
            existing = list(reader)
    
    # Find max ID
    max_id = 0
    for row in existing:
        try:
            max_id = max(max_id, int(row.get('id', 0)))
        except:
            pass
    
    # Add new data with incremented IDs
    for pub in new_data:
        max_id += 1
        pub['id'] = str(max_id)
        
        # Set defaults
        pub.setdefault('preprint_url', '')
        pub.setdefault('preprint_label', '')
        pub.setdefault('image', f'paper{max_id}.jpg')
        
        existing.append(pub)
    
    return existing

def write_csv(data, output_file):
    """Write publication data to CSV"""
    
    if not data:
        print("No data to write")
        return
    
    # Define column order
    fieldnames = ['id', 'title', 'journal', 'date', 'authors', 'link', 'doi', 
                  'preprint_url', 'preprint_label', 'image']
    
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in data:
            # Ensure all fields exist
            for field in fieldnames:
                row.setdefault(field, '')
            writer.writerow(row)
    
    print(f"Wrote {len(data)} publications to {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Import publications for Jekyll website')
    parser.add_argument('--bibtex', help='Import from BibTeX file')
    parser.add_argument('--pubmed', help='Search query for PubMed')
    parser.add_argument('--csv', help='Import from CSV file')
    parser.add_argument('--output', default=str(PAPERS_CSV), help='Output CSV file')
    parser.add_argument('--merge', action='store_true', help='Merge with existing data')
    
    args = parser.parse_args()
    
    new_publications = []
    
    # Import from specified source
    if args.bibtex:
        new_publications = parse_bibtex(args.bibtex)
        print(f"Imported {len(new_publications)} publications from BibTeX")
    
    elif args.pubmed:
        new_publications = fetch_pubmed(args.pubmed)
        print(f"Imported {len(new_publications)} publications from PubMed")
    
    elif args.csv:
        with open(args.csv, 'r') as f:
            reader = csv.DictReader(f)
            new_publications = list(reader)
        print(f"Imported {len(new_publications)} publications from CSV")
    
    else:
        print("Please specify a source: --bibtex, --pubmed, or --csv")
        return
    
    # Merge or replace
    if args.merge:
        all_publications = merge_csv(Path(args.output), new_publications)
    else:
        all_publications = new_publications
    
    # Write output
    write_csv(all_publications, args.output)

if __name__ == "__main__":
    main()