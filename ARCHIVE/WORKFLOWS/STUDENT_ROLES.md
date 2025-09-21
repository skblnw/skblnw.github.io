# 👥 Student Role-Based Collaboration System

## Student Permission Levels

### 🟢 Level 1: Observer (New Students - First Month)
**GitHub Permission:** Read  
**What they can do:**
- View all repository content
- Clone repository locally
- Learn from existing content
- Prepare their first contributions offline

**Cannot do:**
- Create branches or PRs
- Make any changes

**Duration:** First 4 weeks

---

### 🟡 Level 2: Contributor (Active Students)
**GitHub Permission:** Write  
**What they can do:**
- Create branches from main
- Edit files in `STUDENT_ZONE/`
- Submit pull requests
- Add news posts about their achievements
- Update their own profile
- Upload event photos
- Suggest publications

**Cannot do:**
- Merge pull requests
- Edit `PI_ONLY/` content
- Modify site configuration
- Edit other students' profiles

**Requirements to advance:**
- Complete 3 successful news posts
- 2+ months as active contributor
- Demonstrate understanding of workflow

---

### 🟠 Level 3: Senior Contributor (Advanced Students/Postdocs)
**GitHub Permission:** Write + Review Rights  
**What they can do:**
- Everything from Level 2
- Review other students' PRs (non-binding)
- Help train new students
- Suggest workflow improvements
- Create batch updates for events

**Additional Responsibilities:**
- Mentor new students
- Help with technical issues
- Participate in quarterly reviews

**Requirements:**
- 6+ months as Level 2
- 10+ successful contributions
- PI recommendation

---

### 🔴 Level 4: Content Manager (PhD students/Postdocs only)
**GitHub Permission:** Maintainer (limited)  
**What they can do:**
- Everything from Level 3
- Merge non-critical PRs after PI review
- Manage image assets
- Coordinate group updates
- Handle routine maintenance

**Cannot do:**
- Edit critical configuration
- Merge without PI approval
- Change permissions

**Requirements:**
- 1+ year as Level 3
- Demonstrated leadership
- PI designation

---

## 📋 Permission Matrix

| Action | L1 | L2 | L3 | L4 | PI |
|--------|----|----|----|----|----| 
| View content | ✅ | ✅ | ✅ | ✅ | ✅ |
| Create branches | ❌ | ✅ | ✅ | ✅ | ✅ |
| Edit STUDENT_ZONE | ❌ | ✅ | ✅ | ✅ | ✅ |
| Submit PRs | ❌ | ✅ | ✅ | ✅ | ✅ |
| Review PRs | ❌ | ❌ | ✅ | ✅ | ✅ |
| Merge routine PRs | ❌ | ❌ | ❌ | ✅* | ✅ |
| Edit PI_ONLY | ❌ | ❌ | ❌ | ❌ | ✅ |
| Manage permissions | ❌ | ❌ | ❌ | ❌ | ✅ |

*With PI approval

---

## 🔄 Advancement Process

### Automatic Advancement Triggers:
- **L1 → L2:** Complete onboarding checklist + PI approval
- **L2 → L3:** Metrics-based (see requirements above) + peer nomination
- **L3 → L4:** PI invitation only

### Quarterly Review Process:
1. **Self-Assessment:** Students evaluate their contributions
2. **Peer Feedback:** L3+ students provide input on L2 candidates
3. **PI Decision:** Final advancement decisions
4. **Goal Setting:** New objectives for next quarter

---

## 🎯 Student Contribution Targets

### Level 2 Students (Monthly):
- 1-2 news posts
- 1 profile update
- 5+ GitHub interactions

### Level 3 Students (Monthly):
- 2-3 news posts
- 2+ PR reviews
- 1 new student mentoring session

### Level 4 Students (Monthly):
- Coordinate 1 group update
- Merge 5+ routine PRs
- Lead 1 improvement initiative

---

## 🏆 Recognition System

### Monthly Recognition:
- **Most Active Contributor:** Most successful PRs
- **Best Content Creator:** Highest quality posts
- **Helpful Reviewer:** Most thorough PR reviews
- **Technical Champion:** Best troubleshooting help

### Quarterly Awards:
- **Website MVP:** Overall best contributor
- **Innovation Award:** Best workflow improvement
- **Mentorship Award:** Best help to new students

Recognition posted on website news section and lab social media.

---

## 📊 Tracking & Metrics

### Individual Metrics:
- PRs submitted/merged
- Review quality scores
- Response time to feedback
- Help provided to others

### Lab Metrics:
- Student engagement rate
- Content freshness
- Error rate in submissions
- Time from submission to publication

### Dashboard Location:
Internal tracking in `WORKFLOWS/student_metrics.yml` (PI access only)

---

## 🔧 Implementation Timeline

### Week 1-2: Setup
- Configure GitHub permissions
- Assign initial levels
- Set up tracking systems

### Week 3-4: Training
- Level-specific training sessions
- Pair new students with mentors
- Practice workflows

### Month 2: First Review
- Assess initial performance
- Adjust levels as needed
- Gather feedback

### Quarterly: Full Review
- Comprehensive performance review
- Level advancements
- System improvements

---

This role-based system ensures safe, progressive collaboration while maintaining website quality and providing clear growth paths for students.