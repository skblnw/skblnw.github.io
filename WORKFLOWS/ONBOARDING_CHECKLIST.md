# 🎓 New Student Onboarding Checklist

Welcome to CC Lab! This checklist will help you get set up to contribute to the lab website.

---

## Week 1: Account Setup

### Day 1-2: Accounts
- [ ] **GitHub Account**
  - Sign up at: https://github.com
  - Username suggestion: firstnamelastname
  - Send username to PI
- [ ] **Added to Lab Repository**
  - PI will add you as collaborator
  - Accept invitation email from GitHub
- [ ] **Install Git**
  - Mac: Already installed or use `brew install git`
  - Windows: Download from https://git-scm.com
  - Linux: `sudo apt-get install git`

### Day 3-4: Local Setup
- [ ] **Clone Repository**
  ```bash
  git clone https://github.com/skblnw/skblnw.github.io.git
  cd skblnw.github.io
  ```
- [ ] **Configure Git**
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your.email@xjtlu.edu.cn"
  ```
- [ ] **Test Local Build** (Optional but recommended)
  ```bash
  bundle install
  bundle exec jekyll serve
  # View at http://localhost:4000
  ```

### Day 5: Familiarization
- [ ] **Read Documentation**
  - Read: `WORKFLOWS/STUDENT_GUIDE.md`
  - Skim: `LAB_WEBSITE_GUIDE.md`
  - Review: `STUDENT_ZONE/README.md`
- [ ] **Explore Structure**
  - Look at `STUDENT_ZONE/TEMPLATES/`
  - Check existing posts in `collections/_posts/`
  - Review other student profiles

---

## Week 2: First Contributions

### First PR: Your Profile
- [ ] **Create Your Profile**
  1. Copy template:
     ```bash
     cp STUDENT_ZONE/TEMPLATES/profile_update.yml \
        STUDENT_ZONE/my_profile/firstname_lastname.yml
     ```
  2. Edit your file (replace all [REPLACE] markers)
  3. Add your photo to `assets/images/people/bio-lastname.jpg`

- [ ] **Submit Profile**
  ```bash
  git checkout -b add-my-profile
  git add STUDENT_ZONE/my_profile/firstname_lastname.yml
  git add assets/images/people/bio-lastname.jpg
  git commit -m "Add profile: Firstname Lastname"
  git push origin add-my-profile
  ```
  
- [ ] **Create Pull Request**
  1. Go to GitHub repository
  2. Click "Compare & pull request"
  3. Add description
  4. Submit PR

### Second PR: Welcome News
- [ ] **Write Welcome Post**
  1. Copy template:
     ```bash
     cp STUDENT_ZONE/TEMPLATES/news_template.md \
        STUDENT_ZONE/news_drafts/YYYY-MM-DD-welcome-yourname.md
     ```
  2. Write brief introduction
  3. Include your research interests

- [ ] **Submit News**
  ```bash
  git checkout -b welcome-news
  git add STUDENT_ZONE/news_drafts/YYYY-MM-DD-welcome-yourname.md
  git commit -m "Add news: Welcome Firstname Lastname"
  git push origin welcome-news
  ```

---

## Week 3: Regular Workflow

### Understanding the Process
- [ ] **Practice Workflow**
  - Make small edit to your profile
  - Create PR
  - Wait for review
  - Address feedback if any

### Learn Common Tasks
- [ ] **News Posts**
  - When to post: conferences, papers, awards
  - How often: As events happen
  - Review process: PI approves within 2-3 days

- [ ] **Photo Uploads**
  - Event photos: `STUDENT_ZONE/photos/`
  - Naming: `YYYY-MM-DD-event-description.jpg`
  - Size: Keep under 2MB

---

## Week 4: Advanced Tasks

### Optional Skills
- [ ] **Learn Markdown**
  - Tutorial: https://www.markdownguide.org/basic-syntax/
  - Practice in your posts

- [ ] **Image Editing**
  - Resize photos before uploading
  - Tools: ImageMagick, GIMP, or online tools

- [ ] **Git Branches**
  - One branch per task
  - Clear branch names
  - Delete after merging

---

## 📋 Quick Reference Card

Save this for easy reference:

```bash
# Start new task
git checkout gh-pages
git pull
git checkout -b task-name

# Make changes
# (edit files in STUDENT_ZONE only)

# Submit changes
git add .
git commit -m "Clear description"
git push origin task-name

# Then create PR on GitHub
```

---

## 🚨 Common Mistakes to Avoid

1. **Don't edit outside STUDENT_ZONE**
2. **Don't forget date format: YYYY-MM-DD**
3. **Don't commit large images (>2MB)**
4. **Don't edit other people's profiles**
5. **Don't merge your own PRs**

---

## 📞 Getting Help

### Quick Questions
- Slack: #lab-website channel
- Ask senior grad students

### Technical Issues
- Check error messages first
- Google the error
- Ask PI if stuck

### Emergency
- Accidentally deleted something: Don't panic, Git has history
- Website is broken: Contact PI immediately
- Can't push/pull: Check internet and GitHub status

---

## ✅ Onboarding Complete!

Once you've completed all items above:
1. You can contribute to the website
2. You understand the workflow
3. You know where to get help

**Congratulations! You're ready to help maintain the lab website!**

---

## 📅 Ongoing Responsibilities

As a lab member, you should:
- Update your profile each semester
- Post news about your achievements
- Share conference/event photos
- Help new students with onboarding