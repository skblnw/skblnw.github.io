# 🏗️ Lab Website Collaborative Management System

## System Architecture Overview

This document describes the collaborative content management system for the CC Lab website, designed to enable safe student contributions while maintaining PI control over critical content.

---

## 📊 System Design Principles

1. **Separation of Concerns**: Critical content is physically separated from student-editable content
2. **Fail-Safe Design**: Even if students make mistakes, core website remains intact
3. **Progressive Validation**: Multiple checks at different stages catch errors early
4. **Clear Boundaries**: Visual and structural cues show what can be edited
5. **Automated Assistance**: Scripts and workflows reduce manual oversight burden

---

## 🗂️ Directory Structure

```
skblnw.github.io/
│
├── 🔒 PI_ONLY/                 # Protected content (PI access only)
│   ├── README.md               # Explains restrictions
│   ├── _pages/                 # Critical pages
│   │   ├── home.md            # Homepage
│   │   ├── research.md        # Research directions
│   │   └── contact.md         # Contact info
│   └── _data/
│       ├── navigation.yml     # Site navigation
│       └── authors_master.yml # Complete member database
│
├── 🎓 STUDENT_ZONE/            # Student workspace (safe to edit)
│   ├── README.md              # Student instructions
│   ├── news_drafts/           # Draft news posts
│   ├── photos/                # Event photos
│   ├── my_profile/            # Individual profiles
│   ├── publication_drafts/   # Suggested publications
│   └── TEMPLATES/             # Copy-paste templates
│       ├── news_template.md
│       ├── paper_news_template.md
│       ├── event_news_template.md
│       ├── profile_update.yml
│       └── publication_template.txt
│
├── 📋 WORKFLOWS/               # Documentation & guides
│   ├── STUDENT_GUIDE.md      # Simple student instructions
│   ├── PI_GUIDE.md           # Advanced PI management
│   ├── ONBOARDING_CHECKLIST.md # New student setup
│   └── checklists/           # Task-specific guides
│
├── 🔧 utils/                   # Automation scripts
│   ├── validate_student_pr.py # Validates student submissions
│   ├── generate_people.py    # Generates people pages
│   └── import_publications.py # Imports publications
│
├── 🤖 .github/workflows/       # GitHub Actions
│   └── validate-student-pr.yml # Automated PR validation
│
└── 📁 [Standard Jekyll Dirs]   # Regular website files
    ├── _data/                 # Data files
    ├── _pages/                # Website pages
    ├── collections/           # Posts and people
    └── assets/                # Images and styles
```

---

## 🔄 Content Flow Diagram

```
Student Creates Content
        ↓
[STUDENT_ZONE/drafts]
        ↓
Creates Pull Request
        ↓
Automated Validation ←─── [GitHub Actions]
        ↓
    ✓ Pass / ✗ Fail
        ↓
PI Review (if passed)
        ↓
    Approve / Request Changes
        ↓
Merge to Production
        ↓
[Website Updates]
```

---

## 🛡️ Safety Mechanisms

### Layer 1: Physical Separation
- `PI_ONLY/` directory for critical files
- `STUDENT_ZONE/` for student contributions
- Clear README files explaining boundaries

### Layer 2: Template System
- Pre-formatted templates with `[REPLACE]` markers
- Students copy templates, not create from scratch
- Reduces formatting errors

### Layer 3: Automated Validation
- Python script checks file locations
- YAML/Markdown syntax validation
- Image size verification
- Template marker detection

### Layer 4: GitHub Protections
- Branch protection on main branch
- Required PR reviews
- Automated checks must pass
- CODEOWNERS file enforcement

### Layer 5: Human Review
- PI reviews all student PRs
- Can request changes
- Final approval before merge

---

## 👥 Permission Levels

| Role | GitHub Permission | Can Do | Cannot Do |
|------|------------------|--------|-----------|
| **New Student** | Read | View code, learn | Make changes |
| **Active Student** | Write | Create PRs, edit STUDENT_ZONE | Merge PRs, edit PI_ONLY |
| **Senior Student** | Write+ | Help review PRs | Merge without PI approval |
| **PI** | Admin | Everything | N/A |

---

## 📝 Content Types & Workflows

### Type A: Student-Generated (Low Risk)
- **Content**: News posts, event photos, profile updates
- **Location**: `STUDENT_ZONE/`
- **Process**: Template → Draft → PR → Auto-check → PI review → Publish
- **Frequency**: Weekly
- **Risk Level**: Low

### Type B: Student-Assisted (Medium Risk)
- **Content**: Publication entries, member photos
- **Location**: `STUDENT_ZONE/` → PI processes
- **Process**: Student suggests → PI verifies → PI adds
- **Frequency**: Monthly
- **Risk Level**: Medium

### Type C: PI-Only (High Risk)
- **Content**: Homepage, research, navigation, config
- **Location**: `PI_ONLY/` and root config files
- **Process**: PI edits directly
- **Frequency**: Quarterly
- **Risk Level**: High

---

## 🚀 Implementation Checklist

### Initial Setup (One Time)
- [x] Create directory structure
- [x] Set up templates
- [x] Write documentation
- [x] Create validation scripts
- [x] Configure GitHub Actions
- [ ] Set up branch protection (on GitHub)
- [ ] Add students as collaborators
- [ ] Initial training session

### Ongoing Maintenance
- [ ] Weekly: Review student PRs
- [ ] Monthly: Update member list
- [ ] Quarterly: Review permissions
- [ ] Annually: Update documentation

---

## 📈 Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Student contribution rate | 2+ posts/month | GitHub insights |
| Error rate | <10% of PRs | Failed validations |
| Review turnaround | <3 days | PR metrics |
| Student satisfaction | High | Surveys |
| Website uptime | 99.9% | GitHub Pages status |

---

## 🔧 Troubleshooting Guide

### Common Issues

1. **Student edited wrong file**
   - Solution: Reject PR, explain correct location
   
2. **Validation script fails**
   - Check Python version
   - Ensure YAML module installed
   
3. **Images too large**
   - Provide compression instructions
   - Share online tools
   
4. **Merge conflicts**
   - PI resolves manually
   - Usually from simultaneous edits

---

## 📚 Training Materials

1. **For Students**:
   - `WORKFLOWS/STUDENT_GUIDE.md` - Primary reference
   - `WORKFLOWS/ONBOARDING_CHECKLIST.md` - Getting started
   - `STUDENT_ZONE/README.md` - Quick reference

2. **For PI**:
   - `WORKFLOWS/PI_GUIDE.md` - Advanced management
   - This document - System overview
   - GitHub documentation - Technical reference

---

## 🎯 Key Benefits

### For PI:
- ✅ Reduced maintenance burden
- ✅ Protected critical content
- ✅ Automated validation
- ✅ Clear audit trail

### For Students:
- ✅ Safe learning environment
- ✅ Clear guidelines
- ✅ Quick feedback
- ✅ Portfolio building

### For Lab:
- ✅ Fresh content
- ✅ Shared ownership
- ✅ Professional presence
- ✅ Knowledge transfer

---

## 📅 Rollout Plan

### Phase 1: Setup (Week 1)
- Configure repository structure
- Set up GitHub protections
- Test validation systems

### Phase 2: Pilot (Week 2-3)
- Train 2-3 senior students
- Test workflows
- Refine documentation

### Phase 3: Full Launch (Week 4)
- Train all students
- Begin regular contributions
- Monitor and adjust

### Phase 4: Optimization (Ongoing)
- Gather feedback
- Improve automation
- Update documentation

---

## 📞 Support Contacts

- **Technical Issues**: Check documentation first, then ask PI
- **Content Questions**: Senior grad students
- **Emergency**: Direct message/email to PI

---

## ✅ Summary

This collaborative system enables **safe**, **scalable**, and **sustainable** website management by:

1. **Separating** critical and student content
2. **Automating** validation and checks
3. **Providing** clear templates and guides
4. **Enforcing** review processes
5. **Documenting** everything clearly

The result is a website that stays **fresh** with student contributions while maintaining **professional** standards under PI oversight.