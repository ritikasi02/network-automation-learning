# GitHub Workflow Guide

A complete beginner's guide to using GitHub as part of your daily learning. Every command is explained in plain English.

---

## Part 1: Understanding Git and GitHub

**Git** is a tool that tracks changes to your files. Think of it as an unlimited "undo" system that also keeps a history of everything you ever did.

**GitHub** is a website where you store your Git history online. It is your portfolio. Hiring managers will look at your GitHub profile to see what you have built.

**Repository (repo)** is a project folder that Git is tracking. Each module in this curriculum will live in this one repository.

**Commit** is a snapshot of your files at a point in time, with a message describing what changed. Think of it as saving a checkpoint in a video game.

**Push** means uploading your local commits to GitHub so they are visible online.

**Pull** means downloading the latest changes from GitHub to your local machine.

---

## Part 2: One-Time Setup

You only need to do this once on your machine.

### Check if Git is installed

```bash
git --version
```

This prints the version of Git installed on your machine. If you see a version number, you are good. If you see an error, install Git from https://git-scm.com.

### Tell Git who you are

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

This tells Git your name and email so every commit is tagged with your identity. Use the same email you used to create your GitHub account.

### Create a GitHub account

Go to https://github.com and create a free account if you do not have one. Choose a professional username (your real name or a clean handle, not something like `xXhacker420Xx`).

### Set up authentication

GitHub no longer accepts passwords for Git operations. You need either SSH keys or a personal access token.

**Option A: SSH key (recommended, one-time setup)**

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

This creates a pair of cryptographic keys on your machine. When it asks where to save, press Enter to accept the default location. When it asks for a passphrase, you can press Enter for no passphrase (simpler) or type one (more secure).

```bash
cat ~/.ssh/id_ed25519.pub
```

This prints your public key. Copy the entire output. Then go to GitHub > Settings > SSH and GPG keys > New SSH key, paste it there, and save.

**Option B: Personal Access Token**

Go to GitHub > Settings > Developer settings > Personal access tokens > Tokens (classic) > Generate new token. Select the `repo` scope. Copy the token and use it as your password when Git asks.

---

## Part 3: Creating Your First Repository on GitHub

### Step 1: Create the repo on GitHub

1. Go to https://github.com
2. Click the **+** button in the top right, then **New repository**
3. Repository name: `network-automation-learning`
4. Description: `Network automation and cloud learning curriculum with hands-on projects`
5. Set it to **Public** (hiring managers need to see it)
6. Do NOT check "Add a README file" (you already have one locally)
7. Click **Create repository**

### Step 2: Connect your local folder to GitHub

Navigate to your project folder and run these commands:

```bash
cd ~/pyme/network_automation_learning
```

**What this does:** Changes your terminal's working directory to your project folder.

```bash
git init
```

**What this does:** Turns this folder into a Git repository. Git starts tracking changes in this folder. This creates a hidden `.git` folder that stores all the history. You only run this once per project.

```bash
git add -A
```

**What this does:** Stages ALL files in the folder for your first commit. "Staging" means marking files to be included in the next snapshot. The `-A` flag means "add everything, including new files, modified files, and deleted files."

```bash
git commit -m "initial commit: curriculum structure and module 1 materials"
```

**What this does:** Creates a snapshot of all your staged files with the message "initial commit: curriculum structure and module 1 materials." The `-m` flag lets you write the commit message inline. Every commit needs a message explaining what changed.

```bash
git branch -M main
```

**What this does:** Renames your default branch to `main`. This is the standard branch name used by GitHub.

```bash
git remote add origin git@github.com:YOUR_USERNAME/network-automation-learning.git
```

**What this does:** Tells Git where your GitHub repository is. Replace `YOUR_USERNAME` with your actual GitHub username. The word `origin` is a nickname for the remote URL. If you used a personal access token instead of SSH, use the HTTPS URL instead: `https://github.com/YOUR_USERNAME/network-automation-learning.git`

```bash
git push -u origin main
```

**What this does:** Uploads your commit to GitHub. The `-u` flag sets `origin main` as the default destination so future pushes only need `git push`. After this, go to your GitHub repo URL in a browser and you should see all your files.

---

## Part 4: Your Daily Ritual

### START of every study session (1 minute)

```bash
cd ~/pyme/network_automation_learning
git pull
```

**What `git pull` does:** Downloads any changes from GitHub. This matters if you ever edit from another machine or if GitHub Actions makes changes. Even if nothing changed, it is a good habit.

Then open Cursor and read your last commit message:

```bash
git log -1 --oneline
```

**What this does:** Shows your most recent commit message in one line. This reminds you where you left off.

### END of every study session (2-3 minutes)

```bash
git status
```

**What this does:** Shows you which files have changed since your last commit. Red files are modified but not staged. Green files are staged and ready to commit. New files show as "untracked."

```bash
git add -A
```

**What this does:** Stages all changes (new files, modified files, deleted files) for the next commit.

```bash
git commit -m "module1: add interface parsing with regex"
```

**What this does:** Creates a new commit with your staged changes. Replace the message with a description of what you actually did in this session.

```bash
git push
```

**What this does:** Uploads your new commit to GitHub. After this, your work is safely backed up and visible on your profile.

---

## Part 5: Writing Good Commit Messages

Your commit messages are part of your portfolio. Hiring managers who look at your repos will read them.

### The Format

```
moduleX: short description of what you did
```

Keep it under 72 characters. Use present tense ("add" not "added"). Start with the module name so your history is organized.

### Good Examples

```
module1: add function to extract interface IP addresses
module1: fix regex pattern for parsing OSPF neighbors
module1: add JSON export to config analyzer
module3: implement CML API authentication
module4: add Meraki device inventory endpoint
module4.5: create Lambda function for compliance check
module6: add Jinja2 template for VLAN configuration
module9: add GitHub Actions workflow for pytest
module1: update README with setup instructions
```

### Bad Examples and Why

| Bad Message | Problem |
|-------------|---------|
| `update` | Update what? This tells nobody anything. |
| `fixed it` | Fixed what? Where? How? |
| `WIP` | Every commit is work in progress. Be specific. |
| `changes` | Every commit is changes. Describe WHAT changed. |
| `stuff` | Your future self will not remember what "stuff" means. |
| `asdf` | Just no. |
| `added code to parse interfaces and also fixed the bug with file reading and updated the README and changed the requirements` | Too long, doing too many things. Split into multiple commits. |

### When You Cannot Think of a Good Message

Use this formula: `module[X]: [verb] [what] [where/why]`

Verbs to use: add, fix, update, remove, refactor, rename, move, implement, create, configure

---

## Part 6: How Often to Commit

### Commit every study session

Even if you only changed one line, commit it. This does two things:
1. Keeps your GitHub contribution graph active (green squares)
2. Creates a safety net you can return to

### Commit at natural breakpoints

- Finished a function? Commit.
- Fixed a bug? Commit.
- Added error handling? Commit.
- Updated the README? Commit.

### Commit before trying something risky

About to rewrite a big section of code? Commit first. If the rewrite goes badly, you can undo:

```bash
git checkout -- filename.py
```

**What this does:** Throws away your changes to that file and restores the last committed version.

### Do NOT wait until the project is "done"

A repo with 50 small commits over 6 weeks is far more impressive than a repo with 1 giant commit of all the final code. Hiring managers want to see your learning process.

---

## Part 7: Keeping Your README Updated

### Update as you build, not after you finish

Every time you complete a feature or milestone, update your README immediately. A README written during development is always more accurate and useful than one written from memory after the project is done.

### What to update and when

| When | What to add to README |
|------|-----------------------|
| Start of a module | Project title, "What It Does" section, "Technologies" section |
| After first working code | "How to Run" section |
| After completing a feature | Add it to the features list |
| After learning something | Add it to "What I Learned" section |
| After generating output | Add sample output or screenshot |
| Project complete | Final review, clean up, add any missing sections |

### README commits are real commits

Updating your README is not busywork. It is a skill. Write clear documentation, commit it, and push it. This shows hiring managers you communicate well, which is critical for Solution Engineer roles.

---

## Part 8: Common Beginner Mistakes

### Mistake 1: Forgetting to commit before trying something new

**What happens:** You break your code and cannot remember what it looked like before.

**How to avoid:** Commit before any major change. Use `git stash` if you want to temporarily save uncommitted changes:

```bash
git stash
```

**What this does:** Saves your uncommitted changes and restores the last clean state. To get your changes back: `git stash pop`

### Mistake 2: Committing sensitive data

**What happens:** You commit a file with passwords, API keys, or tokens. Even if you delete it later, it stays in Git history forever.

**How to avoid:** Create a `.gitignore` file in your project root:

```bash
# .gitignore
*.env
.env
secrets.yaml
**/credentials.json
__pycache__/
*.pyc
.DS_Store
venv/
*.log
```

Store sensitive values in environment variables, not in code. If you accidentally commit a secret, rotate it immediately (change the password or regenerate the API key).

### Mistake 3: Making one giant commit with everything

**What happens:** Your commit history is useless. You cannot undo one change without undoing everything.

**How to avoid:** Commit small and often. Each commit should do ONE thing.

### Mistake 4: Editing files on GitHub directly

**What happens:** Your local copy and GitHub get out of sync, causing merge conflicts.

**How to avoid:** Always edit files locally in Cursor, then commit and push. If you must edit on GitHub (like fixing a typo in README), run `git pull` before your next local session.

### Mistake 5: Panicking when you see a merge conflict

**What happens:** Git shows scary-looking conflict markers in your files.

**How to fix:** This is normal. Open the file, look for `<<<<<<<` and `>>>>>>>` markers, decide which version you want to keep, delete the markers, save, then commit.

### Mistake 6: Not using .gitignore from the start

**What happens:** You commit junk files like `__pycache__/`, `.DS_Store`, or `venv/` that clutter your repo.

**How to avoid:** Create `.gitignore` before your first commit. The template above covers the common Python/macOS files.

---

## Part 9: Making Your GitHub Profile Professional

Your GitHub profile is your technical resume. Here is how to make it stand out.

### Pin your best repositories

Go to your GitHub profile page and click "Customize your pins." Select the 6 repos that best demonstrate your skills. As you complete modules, pin the most impressive projects.

**Ideal pinned repos for your target roles:**
1. Network Config Analyzer (Module 1) - shows Python skills
2. Catalyst Center Automation Toolkit (Module 4) - shows API skills
3. AWS Network Compliance Monitor (Module 4.5) - shows cloud + AI/MCP skills
4. Ansible Network Automation Collection (Module 6) - shows IaC skills
5. Automated Network Pipeline (Module 9) - shows CI/CD skills
6. Cloud-Integrated Network Automation Platform (Module 10) - shows everything

### Create a profile README

Create a repo with the same name as your GitHub username (e.g., `yourusername/yourusername`). Add a `README.md` to it and it will appear on your profile page.

**Example profile README:**

```markdown
# Hi, I'm [Your Name]

Network automation engineer transitioning from 12 years at Cisco
into Solution Engineering and Cloud Automation.

## What I'm Building

- Python automation tools for Cisco Catalyst Center and Meraki
- AWS Lambda functions integrating cloud services with network infrastructure
- Ansible collections for network device management
- CI/CD pipelines with GitHub Actions

## Skills

Python | REST APIs | AWS | Azure | Ansible | Cisco Catalyst Center | Meraki |
NETCONF/YANG | Bedrock | MCP | GitHub Actions | pytest

## Background

- 8 years Network Consulting Engineer at Cisco
- 4 years Technical Marketing Engineer at Cisco
- Expertise: SD-Access, BGP EVPN VXLAN, SD-WAN, ISE

## Currently Learning

< whatever module you are currently working on >
```

### Keep your contribution graph green

Commit every study session. Four commits per week means four green squares per week. Over 10-12 months, your graph will show consistent, sustained effort, which is exactly what hiring managers want to see.

### Write good repo descriptions

Every repo should have a one-line description on GitHub. Go to each repo's settings and add it. Examples:
- "Python tool for parsing and analyzing Cisco IOS configurations"
- "AWS Lambda app for monitoring network device compliance"
- "Ansible collection for automating Cisco IOS/IOS-XE operations"

### Add topics to your repos

On each repo page, click "About" (gear icon) and add topics like: `python`, `network-automation`, `cisco`, `rest-api`, `aws`, `azure`, `ansible`, `devops`. This helps your repos appear in GitHub search results.

---

## Part 10: Quick Command Reference

| What you want to do | Command |
|---------------------|---------|
| See what changed | `git status` |
| See exact line changes | `git diff` |
| Stage all changes | `git add -A` |
| Stage one file | `git add filename.py` |
| Commit staged changes | `git commit -m "your message"` |
| Push to GitHub | `git push` |
| Pull from GitHub | `git pull` |
| See commit history | `git log --oneline -10` |
| Undo changes to a file | `git checkout -- filename.py` |
| See what is in .gitignore | `cat .gitignore` |
| Create a new branch | `git checkout -b feature-name` |
| Switch branches | `git checkout main` |
| Stash uncommitted changes | `git stash` |
| Restore stashed changes | `git stash pop` |

---

## Part 11: Creating a .gitignore File

Create this file in your project root before your first commit:

**File: `.gitignore`**

```
# Python
__pycache__/
*.pyc
*.pyo
*.egg-info/
dist/
build/
venv/
.venv/

# Environment and secrets
.env
*.env
secrets.yaml
credentials.json

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Output files that can be regenerated
outputs/

# AWS
.aws-sam/
samconfig.toml
.aws/

# Azure
local.settings.json
.python_packages/
```

After creating this file:

```bash
git add .gitignore
git commit -m "add .gitignore for Python project"
git push
```

---

**Return to main curriculum:** [README.md](README.md)
