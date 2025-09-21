#!/usr/bin/env python3
"""
Generate Jekyll collection files for people from _data/authors.yml

This script reads the authors.yml file and generates individual markdown files
for each person in the collections/_people directory.

Usage:
    python generate_people.py
"""

import os
import yaml
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
AUTHORS_FILE = PROJECT_ROOT / "_data" / "authors.yml"
PEOPLE_DIR = PROJECT_ROOT / "collections" / "_people"

# Template for individual person page
PERSON_TEMPLATE = """---
title: {name}
author: {author_id}
layout: single
jobtitle: {jobtitle}
bio: {bio}
type: {type}
excerpt: "{excerpt}"
header:
  teaser: {avatar}
---

## Biography

{bio_long}

## Contact

Email: [{email}](mailto:{email})

"""

def load_authors():
    """Load authors from YAML file"""
    with open(AUTHORS_FILE, 'r') as f:
        return yaml.safe_load(f)

def generate_person_file(person_id, person_data):
    """Generate markdown file for a single person"""
    
    # Prepare data with defaults
    name = person_data.get('name', 'Unknown')
    jobtitle = person_data.get('title', '')
    bio = person_data.get('bio', '')
    bio_long = person_data.get('bio_long', '')
    person_type = person_data.get('type', 'member')
    avatar = person_data.get('avatar', '/assets/images/people/default.jpg')
    email = person_data.get('email', '')
    
    # Create excerpt (first 160 chars of bio_long)
    excerpt = bio_long[:160] if bio_long else bio[:160] if bio else ""
    # Remove HTML tags from excerpt
    import re
    excerpt = re.sub('<.*?>', '', excerpt)
    
    # Generate content
    content = PERSON_TEMPLATE.format(
        name=name,
        author_id=person_id,
        jobtitle=jobtitle,
        bio=bio,
        type=person_type,
        excerpt=excerpt,
        avatar=avatar,
        bio_long=bio_long,
        email=email
    )
    
    # Add additional sections if data is available
    if person_data.get('github'):
        content += f"\n[GitHub](https://github.com/{person_data['github']})"
    if person_data.get('linkedin'):
        content += f"\n[LinkedIn](https://linkedin.com/in/{person_data['linkedin']})"
    if person_data.get('twitter'):
        content += f"\n[Twitter](https://twitter.com/{person_data['twitter']})"
    if person_data.get('google_scholar'):
        content += f"\n[Google Scholar](https://scholar.google.com/citations?user={person_data['google_scholar']})"
    if person_data.get('orcid'):
        content += f"\n[ORCID](https://orcid.org/{person_data['orcid']})"
    
    # Write file
    output_file = PEOPLE_DIR / f"{person_id}.md"
    with open(output_file, 'w') as f:
        f.write(content)
    
    print(f"Generated: {output_file}")

def main():
    """Main function"""
    
    # Create output directory if it doesn't exist
    PEOPLE_DIR.mkdir(parents=True, exist_ok=True)
    
    # Load authors data
    authors = load_authors()
    
    if not authors:
        print("No authors found in authors.yml")
        return
    
    # Generate files for each person
    for person_id, person_data in authors.items():
        if person_id.startswith('#'):  # Skip comments
            continue
        generate_person_file(person_id, person_data)
    
    print(f"\nGenerated {len(authors)} person files in {PEOPLE_DIR}")

if __name__ == "__main__":
    main()