# Simple Lab Website Guide

This is your lab website. To update it, you only need to edit **3 YAML files**. That's it!

## 🎯 Quick Start

### 1. Add/Remove Lab Members
**Edit:** `_data/authors.yml`

```yaml
john_doe:                              # Unique ID (firstname_lastname)
  name: "John Doe, PhD"               # Full name with degree
  email: "john.doe@xjtlu.edu.cn"      # Email address
  bio: "AI; bioinformatics; proteins" # Keywords separated by semicolons
  bio_long: "Full biography here..."  # Longer description
  avatar: /assets/images/people/bio-doe.jpg  # Photo path
  title: "PhD Student"                # Position title
  type: member                        # Use "member" or "alumn"
  
  # Optional fields:
  github: johndoe                     # GitHub username
  linkedin: john-doe                  # LinkedIn username
  twitter: johndoe                    # Twitter handle (without @)
  google_scholar: ABC123              # Google Scholar ID
  orcid: 0000-0000-0000-0000         # ORCID ID
  ncbi_id: "Doe J"                   # For matching publications
  
  # For alumni only:
  current_position: "Scientist at Company"  # Current job (alumni only)
```

**Don't forget:** Add their photo to `/assets/images/people/bio-lastname.jpg` (400x400px)

### 2. Add/Remove Publications  
**Edit:** `_data/papers.csv`

```csv
id,title,journal,date,authors,link,doi,preprint_url,preprint_label,image
1,"Paper Title","Nature","2024 Mar","Chan KC, Doe J","https://doi.org/10.1038/xxx","10.1038/xxx","","","paper1.jpg"
```

**Don't forget:** Add paper thumbnail to `/assets/images/papers/paper1.jpg` (500x300px)

### 3. Change Website Menu
**Edit:** `_data/navigation.yml`

```yaml
main:
  - title: "Research"      # Menu text
    url: /research/        # Page URL
  - title: "Publications"
    url: /publications/
  - title: "People"
    url: /people/
  - title: "News"
    url: /news/
  - title: "Contact"
    url: /contact/
```

## 📝 Add News Posts

Create files in `_posts/` with format: `YYYY-MM-DD-title.md`

```markdown
---
layout: single
title: "Welcome New Lab Member"
categories: news
excerpt: "Brief summary for preview"
---

Your news content here in markdown.
```

## 🔧 Change Site Info

**Edit:** `_config.yml` (lines 16-20)

```yaml
title: "Your Lab Name"
subtitle: "Your Research Focus"  
description: "Lab description"
url: "https://yourusername.github.io"
```

## 📁 Essential Files Structure

```
skblnw.github.io/
├── _config.yml          # Site settings
├── _data/
│   ├── authors.yml      # Lab members (MAIN FILE)
│   ├── papers.csv       # Publications list
│   └── navigation.yml   # Website menu
├── _pages/              # Website content pages
├── _posts/              # News posts
├── assets/images/       # All images
└── ARCHIVE/            # Old complicated files (ignore)
```

## 🚀 Publish Changes

```bash
git add .
git commit -m "Update website"
git push
```

Website updates in 2-5 minutes at: https://skblnw.github.io

## 💡 Common Tasks

| Task | File to Edit | What to Do |
|------|-------------|------------|
| Add new member | `_data/authors.yml` | Add entry + photo |
| Remove member | `_data/authors.yml` | Change `type: member` to `type: alumn` |
| Add publication | `_data/papers.csv` | Add row + thumbnail |
| Change lab name | `_config.yml` | Edit `title` field |
| Add menu item | `_data/navigation.yml` | Add title/url pair |
| Post news | `_posts/` | Create new markdown file |

## 🆘 Need Help?

- **Images not showing?** Check file paths start with `/assets/images/`
- **Site not updating?** Wait 5 minutes, clear browser cache
- **YAML errors?** Check indentation (use 2 spaces, not tabs)

That's it! No complicated scripts, no confusing folders. Just edit the YAML files and your website updates automatically.