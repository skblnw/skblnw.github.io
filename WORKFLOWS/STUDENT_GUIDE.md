# 📚 Student Website Contribution Guide

## Welcome! This guide will help you contribute to the lab website safely and easily.

---

## 🎯 Quick Reference: What You Can Do

| Task | Difficulty | Location | Template |
|------|------------|----------|----------|
| Add News | ⭐ Easy | `STUDENT_ZONE/news_drafts/` | `news_template.md` |
| Update Your Profile | ⭐ Easy | `STUDENT_ZONE/my_profile/` | `profile_update.yml` |
| Share Event Photos | ⭐ Easy | `STUDENT_ZONE/photos/` | Just upload! |
| Announce Paper | ⭐⭐ Medium | `STUDENT_ZONE/news_drafts/` | `paper_news_template.md` |
| Suggest Publication | ⭐⭐ Medium | `STUDENT_ZONE/publication_drafts/` | `publication_template.txt` |

---

## 🚀 Step-by-Step Workflows

### Workflow 1: Adding Lab News (Most Common!)

#### What you need:
- News to share (award, event, achievement)
- 5 minutes

#### Steps:

1. **Navigate to templates:**
   ```
   STUDENT_ZONE/TEMPLATES/
   ```

2. **Copy the right template:**
   - General news → `news_template.md`
   - New paper → `paper_news_template.md`
   - Event/conference → `event_news_template.md`

3. **Create your news file:**
   ```
   STUDENT_ZONE/news_drafts/YYYY-MM-DD-short-title.md
   Example: 2024-03-15-best-poster-award.md
   ```

4. **Fill in the template:**
   - Replace ALL `[REPLACE: ...]` markers
   - Delete instruction comments
   - Add your content

5. **Submit via GitHub:**
   ```bash
   git add STUDENT_ZONE/news_drafts/your-file.md
   git commit -m "Add news: your title"
   git push
   ```

6. **Create Pull Request** on GitHub website

#### ✅ Example:

**Before (template):**
```markdown
title: "[REPLACE: Your News Title]"
date: [REPLACE: YYYY-MM-DD]
```

**After (filled):**
```markdown
title: "Jane Smith Wins Best Poster Award at ICML 2024"
date: 2024-03-15
```

---

### Workflow 2: Updating Your Profile

#### When to update:
- New publication
- Conference presentation
- Project milestone
- Skills update

#### Steps:

1. **Find your profile file:**
   ```
   STUDENT_ZONE/my_profile/firstname_lastname.yml
   ```
   
   If it doesn't exist, copy from:
   ```
   STUDENT_ZONE/TEMPLATES/profile_update.yml
   ```

2. **Edit ONLY these sections:**
   - ✅ `bio_long` - Your research description
   - ✅ `current_project` - What you're working on
   - ✅ `presentations` - Your talks/posters
   - ✅ `achievements` - Awards, publications
   - ✅ `skills` - Technical skills
   
   **NEVER edit:**
   - ❌ `name`
   - ❌ `email`
   - ❌ `title`
   - ❌ `type`

3. **Submit changes** (same Git process as news)

---

### Workflow 3: Adding Event Photos

#### Photo Requirements:
- Maximum 2MB per photo
- JPG or PNG format
- Good quality (not blurry)

#### Naming Convention:
```
YYYY-MM-DD-event-description.jpg

Examples:
2024-03-15-lab-retreat-group.jpg
2024-03-15-lab-retreat-poster-session.jpg
2024-03-15-lab-retreat-dinner.jpg
```

#### Steps:

1. **Resize photos if needed:**
   - Mac: Use Preview app
   - Windows: Use Photos app
   - Online: Use [compress.com](https://compress.com)

2. **Upload to:**
   ```
   STUDENT_ZONE/photos/
   ```

3. **Reference in news post:**
   ```markdown
   ![Lab retreat group photo](/STUDENT_ZONE/photos/2024-03-15-lab-retreat-group.jpg)
   ```

---

## 📝 Writing Tips

### Good News Title:
✅ "Jane Smith Wins Best Poster Award at ICML 2024"
❌ "Award" (too vague)

### Good Date Format:
✅ `2024-03-15`
❌ `March 15, 2024` or `15/03/2024`

### Good Tags:
✅ Specific: `conference`, `award`, `publication`
❌ Vague: `news`, `update`, `stuff`

---

## 🛠 Git Commands Cheat Sheet

```bash
# 1. See what you've changed
git status

# 2. Add your changes
git add STUDENT_ZONE/your-file.md

# 3. Commit with clear message
git commit -m "Add news: Best poster award at ICML"

# 4. Push to GitHub
git push

# 5. Go to GitHub website and create Pull Request
```

---

## ⚠️ Common Mistakes to Avoid

| Mistake | Why It's Bad | How to Fix |
|---------|--------------|------------|
| Editing outside STUDENT_ZONE | Could break website | Only work in STUDENT_ZONE |
| Forgetting date format | Page won't sort correctly | Use YYYY-MM-DD |
| Large images (>2MB) | Slow website | Compress images first |
| Missing [REPLACE] markers | Broken formatting | Check all markers replaced |
| Editing other's profiles | Privacy/accuracy | Only edit your own files |

---

## 🆘 Troubleshooting

### "Permission Denied" Error
- You're trying to edit PI_ONLY folder
- Solution: Stay in STUDENT_ZONE

### "Merge Conflict"
- Someone else edited same file
- Solution: Ask senior student or PI for help

### Images Not Showing
- Wrong file path
- Solution: Use full path from root: `/STUDENT_ZONE/photos/...`

### YAML Error
- Broken formatting in .yml file
- Solution: Check indentation (2 spaces, not tabs)

---

## 📋 Submission Checklist

Before submitting your Pull Request:

- [ ] All `[REPLACE]` markers are replaced
- [ ] Date format is YYYY-MM-DD
- [ ] Images are under 2MB
- [ ] Deleted instruction comments
- [ ] Spell-checked content
- [ ] Only edited files in STUDENT_ZONE
- [ ] Clear commit message
- [ ] Created Pull Request on GitHub

---

## 🎓 For New Students

### First Week Setup:
1. Get GitHub account
2. Get added to lab repository
3. Clone repository to your computer
4. Create your profile in `STUDENT_ZONE/my_profile/`
5. Submit first news post about joining the lab!

### Your First Contribution:
Start with a simple news post about joining the lab:
```markdown
---
title: "Welcome [Your Name] to CC Lab"
date: 2024-MM-DD
categories: news
tags:
  - welcome
  - team
---

We're excited to welcome [Your Name] who joins us as a [position]!

[Your Name] completed their [degree] at [University] and will be working on [research area].

Welcome to the team!
```

---

## 📞 Getting Help

1. **Check this guide first**
2. **Ask a senior student** - They've done this before!
3. **Check templates** - They have examples
4. **Email PI** - For urgent issues only

Remember: Everyone was new once. Don't be afraid to ask questions!