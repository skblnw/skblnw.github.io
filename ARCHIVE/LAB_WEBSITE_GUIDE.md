# Lab Website Management Guide

This guide explains how to manage and update your CC Lab website built with Jekyll and the Minimal Mistakes theme.

## Table of Contents
1. [Quick Start](#quick-start)
2. [File Structure](#file-structure)
3. [How to Update Content](#how-to-update-content)
4. [Adding Lab Members](#adding-lab-members)
5. [Managing Publications](#managing-publications)
6. [Creating News Posts](#creating-news-posts)
7. [Updating Research Projects](#updating-research-projects)
8. [Adding Images](#adding-images)
9. [Troubleshooting](#troubleshooting)

---

## Quick Start

### Local Development
```bash
# Install dependencies
bundle install

# Run local server
bundle exec jekyll serve

# View at http://localhost:4000
```

### Deploy to GitHub Pages
```bash
git add .
git commit -m "Update website"
git push origin gh-pages
```

Your site will be live at: https://skblnw.github.io

---

## File Structure

```
├── _config.yml           # Main configuration (site name, URL, etc.)
├── _data/               
│   ├── navigation.yml   # Navigation menu items
│   ├── authors.yml      # ALL lab member data (MAIN SOURCE)
│   └── papers.csv       # Publications list
├── _pages/              
│   ├── home.md         # Homepage content
│   ├── research.md     # Research descriptions
│   ├── people.md       # People page (auto-generated from authors.yml)
│   ├── publications.md # Publications (reads from papers.csv)
│   ├── contact.md      # Contact information
│   ├── news.md         # News archive
│   └── resources.md    # Software/data resources
├── collections/         
│   ├── _people/        # Individual person pages (auto-generated)
│   └── _posts/         # News posts (YYYY-MM-DD-title.md format)
├── assets/images/       
│   ├── people/         # Member photos (bio-lastname.jpg)
│   ├── papers/         # Paper thumbnails
│   ├── bar-network.png # Homepage banner
│   └── lab-photo.jpg   # Group photo
└── utils/              
    ├── generate_people.py    # Script to generate people pages
    └── import_publications.py # Script to import papers
```

---

## How to Update Content

### 1. Update Site Name/Info
Edit `_config.yml`:
```yaml
title: "CC Lab @ xjtlu"  # Your lab name
description: "Research laboratory focused on structural bioinformatics"
email: "Chun.Chan@xjtlu.edu.cn"
```

### 2. Update Navigation Menu
Edit `_data/navigation.yml`:
```yaml
main:
  - title: "Research"
    url: /research/
  - title: "New Section"  # Add new menu item
    url: /new-section/
```

---

## Adding Lab Members

### Step 1: Edit the Main Data File
Edit `_data/authors.yml` and add a new person:

```yaml
firstname_lastname:  # Unique ID (use underscores)
  name: "First Last, PhD"  # Full name with degree
  email: "email@xjtlu.edu.cn"
  bio: "keyword1; keyword2; keyword3"  # Short keywords
  bio_long: >
    Full biography paragraph. Can include HTML tags like <p></p>.
    Describe research interests, background, current projects.
  avatar: /assets/images/people/bio-lastname.jpg  # Photo path
  title: "Position Title"  # e.g., "PhD Student", "Postdoc"
  type: member  # Use "member" for current, "alumn" for alumni
  
  # Optional fields:
  github: githubusername
  linkedin: linkedin-username
  twitter: twitterhandle
  google_scholar: ScholarID
  orcid: 0000-0000-0000-0000
  ncbi_id: "Last F"  # For auto-matching publications
```

### Step 2: Add Their Photo
1. Name the photo: `bio-lastname.jpg`
2. Resize to 400x400px square
3. Save to: `/assets/images/people/`

### Step 3: Generate Their Page
Run the Python script:
```bash
cd /Users/ukevi/github/skblnw.github.io
python utils/generate_people.py
```

This creates a page in `collections/_people/firstname_lastname.md`

### Example: Adding a New PhD Student
```yaml
# In _data/authors.yml:
john_smith:
  name: "John Smith"
  email: "john.smith@xjtlu.edu.cn"
  bio: "molecular dynamics; protein folding; machine learning"
  bio_long: >
    John is a PhD student who joined in 2024. He works on 
    developing ML models for protein structure prediction.
  avatar: /assets/images/people/bio-smith.jpg
  title: "PhD Student"
  type: member
  github: johnsmith
  ncbi_id: "Smith J"
```

---

## Managing Publications

### Method 1: Edit CSV Directly
Edit `_data/papers.csv`:

```csv
id,title,journal,date,authors,link,doi,preprint_url,preprint_label,image
6,"Your Paper Title","Nature","2024 Mar","Chan KC, Smith J","https://doi.org/10.1038/xxx","10.1038/xxx","https://arxiv.org/xxx","arXiv","paper6.jpg"
```

Fields explained:
- **id**: Sequential number
- **title**: Full paper title
- **journal**: Journal name
- **date**: "YYYY Mon" format (e.g., "2024 Mar")
- **authors**: Author list (use your ncbi_id format)
- **link**: DOI link
- **doi**: DOI number
- **preprint_url**: ArXiv/bioRxiv link (optional)
- **preprint_label**: "arXiv" or "bioRxiv" (optional)
- **image**: Thumbnail filename in `/assets/images/papers/`

### Method 2: Import from BibTeX
```bash
python utils/import_publications.py --bibtex my_papers.bib --merge
```

### Adding Paper Thumbnails
1. Create a 500x300px image
2. Name it: `paperX.jpg` (match the ID)
3. Save to: `/assets/images/papers/`

---

## Creating News Posts

### Step 1: Create News File
Create a new file in `collections/_posts/` with format:
```
YYYY-MM-DD-short-title.md
```

Example: `2024-03-15-new-grant.md`

### Step 2: Add Content
```markdown
---
layout: single
title: "Full News Title Here"
categories: news
excerpt: "Brief 1-2 sentence summary for the preview"
tags:
  - grant
  - research
---

Your news content here. You can use **markdown** formatting.

Add images: ![description](/assets/images/posts/image.jpg)

Add links: [Link text](https://example.com)
```

### Common News Types

**New Publication:**
```markdown
---
layout: single
title: "New Paper Published in Nature"
categories: news
excerpt: "Our latest work on protein folding is now published."
tags:
  - publication
---

Our paper "Title" has been published in Nature! 

Led by John Smith, this work presents...

Read it here: [DOI link](https://doi.org/...)
```

**New Member:**
```markdown
---
layout: single
title: "Welcome John Smith to the Lab"
categories: news
excerpt: "John joins us as a new PhD student."
tags:
  - team
---

We're excited to welcome John Smith who joins us as a PhD student!

John completed his BSc at... and will be working on...
```

---

## Updating Research Projects

Edit `_pages/research.md` directly:

```markdown
## Research Directions

### Project Name
*Research question or focus*

Description of the project...

Key areas:
- Bullet point 1
- Bullet point 2

### Another Project
Content...
```

---

## Adding Images

### Homepage Images (REQUIRED)
1. **bar-network.png** (1920x400px)
   - Network/molecular visualization banner
   - Save to: `/assets/images/`

2. **lab-photo.jpg** (800x600px)
   - Group photo
   - Save to: `/assets/images/`

### Member Photos
- Size: 400x400px square
- Format: JPG
- Naming: `bio-lastname.jpg`
- Location: `/assets/images/people/`

### Paper Thumbnails
- Size: 500x300px
- Format: JPG
- Naming: `paper1.jpg`, `paper2.jpg`, etc.
- Location: `/assets/images/papers/`

### Image Optimization
```bash
# Resize with ImageMagick
convert input.jpg -resize 400x400^ -gravity center -crop 400x400+0+0 bio-lastname.jpg

# Compress
convert input.jpg -quality 85% output.jpg
```

---

## Common Tasks Step-by-Step

### Task: Add a New Lab Member
1. Edit `_data/authors.yml` - add their entry
2. Add photo to `/assets/images/people/bio-lastname.jpg`
3. Run `python utils/generate_people.py`
4. Commit and push changes

### Task: Add a Publication
1. Edit `_data/papers.csv` - add new row
2. Add thumbnail to `/assets/images/papers/paperX.jpg`
3. Commit and push changes

### Task: Post News
1. Create `/collections/_posts/2024-MM-DD-title.md`
2. Write content with front matter
3. Commit and push changes

### Task: Update Contact Info
1. Edit `_pages/contact.md`
2. Update email, phone, address
3. Commit and push changes

---

## Troubleshooting

### Site Not Updating
- Wait 5-10 minutes for GitHub Pages to rebuild
- Check GitHub Actions tab for build errors
- Clear browser cache (Cmd+Shift+R or Ctrl+F5)

### Images Not Showing
- Check file path starts with `/`
- Verify image exists in correct folder
- Check filename case (Linux is case-sensitive)

### People Pages Not Generating
```bash
# Make sure you're in the right directory
cd /Users/ukevi/github/skblnw.github.io

# Run the script
python utils/generate_people.py

# Check for new files in collections/_people/
ls collections/_people/
```

### Build Errors
Test locally first:
```bash
bundle exec jekyll build --verbose
bundle exec jekyll serve
```

### YAML Syntax Errors
- Use a YAML validator: https://www.yamllint.com/
- Common issues:
  - Missing quotes around URLs with special characters
  - Incorrect indentation (use 2 spaces, not tabs)
  - Missing colons or dashes

---

## Quick Reference

### Markdown Formatting
```markdown
# Heading 1
## Heading 2
**bold text**
*italic text*
[link text](https://url.com)
![image alt](image-path.jpg)

- Bullet list
1. Numbered list

> Blockquote
```

### Front Matter Template
```yaml
---
layout: single  # or splash, archive
title: "Page Title"
permalink: /custom-url/
excerpt: "Brief description"
header:
  overlay_image: /assets/images/banner.jpg
---
```

### Git Commands
```bash
# Check status
git status

# Add all changes
git add .

# Commit with message
git commit -m "Update description"

# Push to GitHub
git push origin gh-pages

# Pull latest changes
git pull origin gh-pages
```

---

## Regular Maintenance Schedule

### Weekly
- Add news posts for achievements
- Update member profiles if needed

### Monthly  
- Add new publications
- Update project descriptions
- Review and update member list

### Annually
- Update group photo
- Archive old news
- Review all content for accuracy
- Update alumni section

---

## Getting Help

- [Minimal Mistakes Documentation](https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/)
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Markdown Guide](https://www.markdownguide.org/)
- [GitHub Pages Help](https://docs.github.com/en/pages)

## Contact for Technical Issues

If you encounter problems with the website structure or scripts, check:
1. This guide first
2. Error messages in terminal
3. GitHub Actions build logs
4. Jekyll build output with `--verbose` flag

Remember: Always test changes locally before pushing to GitHub!