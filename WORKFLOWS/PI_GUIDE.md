# 🔑 PI Website Management Guide

## Overview
This guide covers advanced website management tasks that only the PI should perform, including critical content updates, student permission management, and emergency procedures.

---

## 📊 Content Management Hierarchy

```
Critical (PI Only)          →  PI_ONLY/
├── Site Configuration      →  _config.yml
├── Navigation              →  PI_ONLY/_data/navigation.yml
├── Homepage                →  PI_ONLY/_pages/home.md
├── Research Directions     →  PI_ONLY/_pages/research.md
├── Contact Info            →  PI_ONLY/_pages/contact.md
└── Member Database         →  PI_ONLY/_data/authors_master.yml

Supervised (PI Reviews)     →  Student PRs from STUDENT_ZONE/
├── News Posts              →  Review → collections/_posts/
├── Profile Updates         →  Review → Merge to authors_master.yml
└── Publications            →  Review → _data/papers.csv

Automated (Safe)            →  STUDENT_ZONE/
├── Draft Content           →  Auto-validated
├── Photos                  →  Size-limited
└── Templates               →  Read-only
```

---

## 🎯 Critical Tasks (PI Only)

### 1. Adding/Removing Lab Members

#### Adding a New Member:
```yaml
# Edit: PI_ONLY/_data/authors_master.yml

new_member:
  name: "Full Name, Degree"
  email: "email@xjtlu.edu.cn"
  bio: "keywords; separated; by semicolons"
  bio_long: >
    Full biography with background and research interests.
  avatar: /assets/images/people/bio-lastname.jpg
  title: "Position Title"
  type: member  # or "alumn"
  
  # Set permissions
  can_edit_news: true
  can_edit_profile: true
  github_username: their_github
  joined_date: "2024-03-15"
```

#### Moving to Alumni:
```yaml
# Change type from "member" to "alumn"
type: alumn
left_date: "2024-03-15"
current_position: "Postdoc at Harvard"
```

### 2. Homepage Updates

```markdown
# Edit: PI_ONLY/_pages/home.md

# Update welcome message
title: "Welcome to the CC Lab @ XJTLU"
excerpt: "New lab description..."

# Update affiliations
We're part of [Department](url)...
```

### 3. Research Directions

```markdown
# Edit: PI_ONLY/_pages/research.md

## New Research Direction
Content about new research area...

# Archive old projects
<!-- Archived 2024-03-15
Old project content...
-->
```

---

## 👥 Student Permission Management

### GitHub Branch Protection Setup

1. **Go to Repository Settings → Branches**
2. **Add rule for `gh-pages`:**
   - ✅ Require pull request reviews
   - ✅ Dismiss stale reviews
   - ✅ Require review from CODEOWNERS
   - ✅ Include administrators
   - ❌ Allow force pushes

3. **Create `.github/CODEOWNERS`:**
```
# Critical files - PI only
/PI_ONLY/ @skblnw
/_config.yml @skblnw
/_data/navigation.yml @skblnw

# Student areas - anyone can propose
/STUDENT_ZONE/ @skblnw

# Auto-approve student photos
/STUDENT_ZONE/photos/ 
```

### Student Access Levels

| Level | Can Do | Cannot Do | Good For |
|-------|--------|-----------|----------|
| **Reader** | View repository | Make changes | New students (first month) |
| **Writer** | Create branches, PRs | Merge to main | Active students |
| **Maintainer** | Merge PRs | Edit protected files | Senior students, postdocs |
| **Admin** | Everything | N/A | PI only |

---

## 📝 Review Workflow for Student PRs

### Quick Review Checklist:
```markdown
- [ ] Changes only in STUDENT_ZONE?
- [ ] No sensitive information?
- [ ] Dates formatted correctly?
- [ ] Images under 2MB?
- [ ] Content appropriate?
- [ ] No broken links?
```

### Approving Student News:

1. **Review PR on GitHub**
2. **Check preview:**
   ```bash
   git checkout student-branch
   bundle exec jekyll serve
   # Preview at localhost:4000
   ```

3. **If good, approve and merge:**
   ```bash
   # Move news to production
   mv STUDENT_ZONE/news_drafts/post.md collections/_posts/
   git add .
   git commit -m "Publish: student news post title"
   git push
   ```

4. **If needs revision:**
   - Comment on PR with specific changes needed
   - Student revises and updates PR

---

## 🔧 Maintenance Tasks

### Weekly (5 minutes):
- Review pending student PRs
- Check for broken links
- Verify recent deployments

### Monthly (30 minutes):
- Update publication list
- Archive old news (>1 year)
- Review and update member list
- Check image storage usage

### Annually:
- Update group photo
- Archive graduated students
- Review all research descriptions
- Clean up unused images

---

## 🚨 Emergency Procedures

### Website is Down:
1. Check GitHub Pages status: https://www.githubstatus.com/
2. Check repository settings → Pages
3. Check recent commits for errors
4. Rollback if needed (see below)

### Accidental Deletion/Error:

#### Quick Rollback:
```bash
# View recent commits
git log --oneline -10

# Rollback to specific commit
git revert HEAD
git push

# Or reset to previous state
git reset --hard <commit-hash>
git push --force  # Use carefully!
```

#### Restore Deleted File:
```bash
# Find when file was deleted
git log -- path/to/deleted/file.md

# Restore it
git checkout <commit-hash>^ -- path/to/deleted/file.md
git add .
git commit -m "Restore: deleted file"
git push
```

### Student Accidentally Edited Critical File:
1. Reject their PR
2. If already merged:
   ```bash
   git revert <merge-commit>
   git push
   ```
3. Explain the mistake kindly
4. Update permissions if needed

---

## 📊 Batch Operations

### Update Multiple Members:
```python
# Use: utils/batch_update_members.py
import yaml

# Load members
with open('PI_ONLY/_data/authors_master.yml', 'r') as f:
    members = yaml.safe_load(f)

# Batch update (example: add new field)
for member_id, data in members.items():
    if data['type'] == 'member':
        data['office'] = 'Room 123'

# Save
with open('PI_ONLY/_data/authors_master.yml', 'w') as f:
    yaml.dump(members, f)
```

### Archive Old News:
```bash
# Move posts older than 1 year to archive
mkdir -p archives/news/2023
mv collections/_posts/2023-*.md archives/news/2023/
```

### Batch Image Optimization:
```bash
# Compress all images over 500KB
find assets/images -size +500k -type f \( -name "*.jpg" -o -name "*.png" \) -exec convert {} -quality 85% {} \;
```

---

## 🔍 Monitoring & Analytics

### Check Website Performance:
- Google PageSpeed: https://pagespeed.web.dev/
- GTmetrix: https://gtmetrix.com/

### Monitor Git Activity:
```bash
# See who's been active
git shortlog -sn --since="1 month ago"

# Check large files
git ls-files | xargs du -h | sort -rh | head -20
```

### Setup Google Analytics:
```yaml
# In _config.yml
analytics:
  provider: "google-gtag"
  google:
    tracking_id: "G-XXXXXXXXXX"
```

---

## 💡 Pro Tips

1. **Use Drafts for Major Changes:**
   ```bash
   git checkout -b major-update
   # Make changes
   git push origin major-update
   # Test thoroughly before merging
   ```

2. **Schedule Updates:**
   - Use GitHub Actions to auto-publish scheduled posts
   - Keep future-dated posts in `_drafts/`

3. **Backup Before Major Updates:**
   ```bash
   # Create backup branch
   git checkout -b backup-$(date +%Y%m%d)
   git push origin backup-$(date +%Y%m%d)
   ```

4. **Test Locally First:**
   Always run `bundle exec jekyll serve` before pushing

5. **Document Decisions:**
   Keep a CHANGELOG.md for major site changes

---

## 📚 Advanced Customization

### Custom Includes:
```liquid
<!-- _includes/custom-feature.html -->
{% if page.custom_feature %}
  <div class="custom-feature">
    {{ page.custom_feature }}
  </div>
{% endif %}
```

### Override Theme Files:
1. Find file in theme: https://github.com/mmistakes/minimal-mistakes
2. Copy to same path in your repo
3. Modify as needed

### Custom CSS:
```scss
// assets/css/main.scss
@import "minimal-mistakes/skins/{{ site.minimal_mistakes_skin }}";
@import "minimal-mistakes";

// Your custom styles
.lab-special {
  color: #your-color;
}
```

---

## 🆘 When to Get Technical Help

Contact technical support when:
- GitHub Pages build failing repeatedly
- Need custom domain setup
- Database integration needed
- Performance issues persist
- Security concerns arise

Remember: The website is version controlled, so any mistake can be fixed. Don't hesitate to experiment (in a branch)!