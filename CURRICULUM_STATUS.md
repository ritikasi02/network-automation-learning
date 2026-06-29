# Curriculum Progress Tracker

**Last Updated:** June 20, 2026
**Overall Progress:** ~6% (Module 1 ~65% complete through Session 11; all other modules not started)
**Pace:** 20-30 minutes per day, 4 days per week (~1.5-2 hours per week)
**Estimated Completion:** 10-12 months from start

---

## Progress Overview

```
Module 1:   █████████████░░░░░░░  65%  IN PROGRESS (S11 done; sets/tuples, comprehensions, show-output, modules, CSV, README remain)
Module 2:   ░░░░░░░░░░░░░░░░░░░░   0%  Not Started
Module 3:   ░░░░░░░░░░░░░░░░░░░░   0%  Not Started
Module 4:   ░░░░░░░░░░░░░░░░░░░░   0%  Not Started
Module 4.5: ░░░░░░░░░░░░░░░░░░░░   0%  Not Started (NEW - AWS Cloud Automation)
Module 5:   ░░░░░░░░░░░░░░░░░░░░   0%  Not Started
Module 6:   ░░░░░░░░░░░░░░░░░░░░   0%  Not Started
Module 7:   ░░░░░░░░░░░░░░░░░░░░   0%  Not Started
Module 8:   ░░░░░░░░░░░░░░░░░░░░   0%  Not Started
Module 9:   ░░░░░░░░░░░░░░░░░░░░   0%  Not Started
Module 10:  ░░░░░░░░░░░░░░░░░░░░   0%  Not Started

Total:      █░░░░░░░░░░░░░░░░░░░░  ~6%
```

---

## Module 1: Python Fundamentals (6-8 weeks)

**Status:** IN PROGRESS (~65%) - 11 sessions complete; multiple concept gaps remain (see below)
**GitHub Project:** Network Config Analyzer (`module1_python_basics/config_analyzer.py`)

### Sessions Completed (recall decks written per session)

| Sessions | Topic | Recall Deck |
|----------|-------|-------------|
| S1-S3 | Variables, strings, file reading, refactor into functions | anki_session1_to_3.txt |
| S4-S5 | Multi-file parsing with `os`, OSPF parsing with regex | anki_session4_to_5.txt |
| S6-S7 | File I/O, `open()` modes, JSON output, guardrails | anki_session6_to_7.txt |
| S8 | Control flow: `return` vs `continue`, recoverable vs fatal | anki_session8.txt |
| S9 | Logging strategy (levels, handlers, formatters) | anki_session9.txt |
| S10 | Automated testing with pytest (AAA, parametrize, fixtures) | anki_session10.txt |
| S11 | OOP refactor into `GetConfig` class | anki_session11.txt |

### Learning-Objective Coverage (from theory_guide.md, the authoritative scope)

| Objective / Theory section | Status |
|-----------|--------|
| Data structures: **lists**, **dicts**, nested | Done (used throughout) |
| Data structures: **tuples** | **Partial** — only incidental (`enumerate`, `parametrize`); no focused lesson |
| Data structures: **sets** | **Not covered** — no usage, no recall deck |
| **List/dict comprehensions** (§2.1, 2.2) | **Not covered** — explicit `.append()` loops only |
| Regex on **config files** | Done (Session 4-5) |
| Regex on **`show` command output** (§3.2-3.3) | **Not covered** — `sample_outputs/` never parsed; no `re.findall`/named groups |
| File formats: text, JSON | Done |
| File formats: **CSV** (§4.4) | **Not covered** — only JSON export exists |
| Functions: basics | Done (S1-3) |
| Functions: **defaults, `*args`/`**kwargs`, multi-return** (§5) | **Not covered** |
| Classes: basics (`__init__`, methods) | Done (S11) |
| Classes: **inheritance, `__str__`/`__repr__`** (§6) | **Not covered** |
| Error handling (try/except, multi-exception) | Done (Session 8) |
| Logging (basicConfig, levels, file handler) | Done (Session 9) |
| Logging: **multi-handler / `RotatingFileHandler`** (§8.2) | Not covered (optional) |
| Virtual env / dependency management (§1.2) | Done — uses an activated project venv |
| **Organize code into modules** (§9) | **Not done** — single-file project |
| Practice exercises (criterion: ≥5) | Partially via project (Ex 2, 9, 10); Ex 1/3/5 untouched |

### Completion Criteria — Live Status

| # | Criterion | Status |
|---|-----------|--------|
| 1 | Built config analyzer from scratch (not copied sample) | Done |
| 2 | Can explain every line of own code | Done |
| 3 | Extracts hostname, interfaces, IPs, routing protocols | Done (`get_hostname`, `get_interfaces`, `get_ospf`) |
| 4 | Exports to 2+ formats (JSON + one other) | **Pending** — only JSON (`output.json`) so far |
| 5 | Handles errors gracefully (missing files, bad input) | Done (`try/except`, `ipadd` validation) |
| 6 | Has logging | Done (Session 9) |
| 7 | On GitHub with a clear **project** README | **Pending** — current README is the module template, not the project's own |
| 8 | 15+ commits showing building process | Done (~15 Module-1 commits) |
| 9 | Can answer "what does this line do?" for any line | Done |

### What Remains (~6 sessions)

Sequential plan; **[T1]** = required, **[T2]** = strongly recommended (in theory guide), **[T3]** = optional.

- [ ] **Session 12 — CSV export [T1]:** write parsed data to CSV with the `csv` module (closes file-formats objective + criterion #4); optional `argparse` CLI
- [ ] **Session 13 — Sets & tuples [T1]:** practical network use — set operations (difference/intersection) to compare which interfaces/OSPF networks two devices share; tuples as immutable records + returning multiple values from functions
- [ ] **Session 14 — Parse `show` output + comprehensions [T2]:** parse `sample_outputs/` (e.g. `show ip interface brief`) with `re.findall`/named groups; refactor a loop or two into list/dict comprehensions
- [ ] **Session 15 — Organize into modules [T1]:** split `config_analyzer.py` into a small package (parser / I-O-reporting / main entry) with proper `import`s and `if __name__ == "__main__"`; fold in class depth (inheritance, `__str__`) [T2] where natural
- [ ] **Session 16 — Polish, README & push [T1]:** remove dead commented-out code, write a real project README, push final state to GitHub (wrap-up/recall)
- [ ] **Optional / deferred [T3]:** advanced logging (console+file handlers, `RotatingFileHandler`), custom exceptions / `finally`, decorators (Ex 8C), PEP 8 + docstrings polish; a "Challenge Yourself" stretch goal (IPv6, SQLite, topology) — not required for completion

---

## Module 2: SSH Automation (1 week)

**Status:** Not Started
**GitHub Project:** Device Backup Script

### Deliverables

- [ ] Write a Netmiko script to backup device configs from CML
- [ ] Understand why SSH automation is being replaced by APIs
- [ ] Push to GitHub with README

### Completion Criteria

1. Working backup script tested against CML
2. On GitHub with README explaining SSH vs API approaches

---

## Module 3: REST API Basics (3-4 weeks)

**Status:** Not Started
**GitHub Project:** Network API Dashboard

### Deliverables

- [ ] Understand HTTP methods, status codes, JSON
- [ ] Build a reusable API client class
- [ ] Make API calls to CML REST API
- [ ] Build a simple Flask dashboard
- [ ] Push to GitHub with README

### Completion Criteria

1. Working API client that authenticates and retrieves data from CML
2. Simple web dashboard displaying lab topology
3. On GitHub with README including API reference table

---

## Module 4: Controller APIs (4-5 weeks)

**Status:** Not Started
**GitHub Project:** Catalyst Center Automation Toolkit

### Deliverables

- [ ] Authenticate with Catalyst Center API
- [ ] Pull device inventory, site health, compliance data
- [ ] Integrate Meraki Dashboard API
- [ ] Build CLI tool combining both platforms
- [ ] Push to GitHub with README

### Completion Criteria

1. Working toolkit tested against real Catalyst Center
2. Meraki integration pulling cloud-managed data
3. CLI interface for common operations
4. On GitHub with README

---

## Module 4.5: AWS Cloud Automation (6-8 weeks) -- NEW

**Status:** Not Started
**GitHub Projects:** AWS Network Compliance Monitor + AI-Powered Network Troubleshooter (with MCP Server)

### Deliverables

- [ ] Set up AWS free tier account + billing budget alarm
- [ ] Learn IAM (users, roles, policies, least privilege), Console, AWS CLI profiles
- [ ] Build first Lambda function (HTTP via Function URL or API Gateway)
- [ ] Build EventBridge-scheduled Lambda for timer-based automation
- [ ] Use the boto3 SDK and AWS REST APIs (pagination, retries, rate-limit handling)
- [ ] Integrate a Lambda with Catalyst Center or Meraki API
- [ ] Store results in DynamoDB (or S3); read secrets from Secrets Manager (no hardcoded keys)
- [ ] Set up alerts for compliance violations via SNS/SES
- [ ] Build AI-powered troubleshooter with Amazon Bedrock
- [ ] Build an MCP server (FastMCP) + conversational LLM agent; write up AI risks (AUTOCOR Domain 4)
- [ ] Push both projects to GitHub with READMEs

### Completion Criteria

1. Working Lambda that monitors network compliance, scheduled via EventBridge
2. AI-powered troubleshooter using Amazon Bedrock, exposed to an LLM agent via an MCP server
3. Both projects on GitHub with architecture diagrams in READMEs

---

## Module 5: NETCONF/YANG (1-2 weeks)

**Status:** Not Started
**GitHub Project:** NETCONF Config Manager

### Deliverables

- [ ] Use ncclient to connect to CML IOS-XE device
- [ ] Retrieve and modify configs via NETCONF
- [ ] Add RESTCONF examples for comparison
- [ ] Push to GitHub with README

### Completion Criteria

1. Working NETCONF scripts tested against CML
2. Comparison of NETCONF vs RESTCONF vs CLI in README
3. On GitHub

---

## Module 6: Ansible (4-5 weeks)

**Status:** Not Started
**GitHub Project:** Ansible Network Automation Collection

### Deliverables

- [ ] Set up Ansible with CML inventory
- [ ] Build playbooks for common operations
- [ ] Create roles for reusable automation
- [ ] Use Jinja2 templates for config generation
- [ ] Implement Vault for secrets
- [ ] Push to GitHub with README

### Completion Criteria

1. Working Ansible collection tested against CML
2. Organized with roles, templates, group_vars
3. On GitHub with README showing project structure

---

## Module 7: Testing & Validation (3-4 weeks)

**Status:** Not Started
**GitHub Project:** Network Test Framework

### Deliverables

- [ ] Build pytest test suite for network validation
- [ ] Implement pre/post change verification
- [ ] Add pyATS integration
- [ ] Generate HTML test reports
- [ ] Push to GitHub with README

### Completion Criteria

1. Working test suite validated against CML
2. Pre/post change tests that catch real issues
3. On GitHub with README

---

## Module 8: Orchestration (3-4 weeks)

**Status:** Not Started
**GitHub Project:** Network Orchestration Engine

### Deliverables

- [ ] Build Nornir-based orchestration tool
- [ ] Implement concurrent multi-device operations
- [ ] Add event-driven webhook component
- [ ] Push to GitHub with README

### Completion Criteria

1. Working orchestration tool tested against CML
2. Concurrent operations running successfully
3. On GitHub with README

---

## Module 9: CI/CD with GitHub Actions (3-4 weeks)

**Status:** Not Started
**GitHub Project:** Automated Network Pipeline

### Deliverables

- [ ] Create GitHub Actions workflows
- [ ] Automate linting and testing on push
- [ ] Build deployment pipeline
- [ ] Push to GitHub with README

### Completion Criteria

1. Working CI/CD pipeline on GitHub
2. Automated tests running on every push
3. On GitHub with README showing pipeline stages

---

## Module 10: Capstone Project (4-6 weeks)

**Status:** Not Started
**GitHub Project:** Cloud-Integrated Network Automation Platform

### Deliverables

- [ ] Design architecture combining all modules
- [ ] Build integrated platform
- [ ] Write comprehensive documentation
- [ ] Create demo video or screenshots
- [ ] Add CI/CD pipeline
- [ ] Push to GitHub with README and architecture diagram

### Completion Criteria

1. Working platform combining skills from all modules
2. Professional documentation with architecture diagram
3. CI/CD pipeline
4. Pinned on GitHub profile
5. Ready to discuss in interviews

---

## Time Investment Tracker

| Week | Module | Sessions | Time (est.) | Notes |
|------|--------|----------|-------------|-------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| ... | | | | |

Fill this in as you progress. It helps you see your actual pace vs. estimates.

---

## Milestone Targets

| Milestone | Target Date | Actual Date | Notes |
|-----------|-------------|-------------|-------|
| Module 1 complete, first GitHub project | +8 weeks | | |
| Modules 1-3 complete, 3 GitHub projects | +13 weeks | | |
| Modules 1-4.5 complete, 5+ GitHub projects | +26 weeks | | |
| All modules complete | +48 weeks | | |
| Job applications begin | When Module 4.5 is done | | Can start applying while continuing |

**Note:** You can start applying for jobs after completing Module 4.5. You will have Python, REST API, Controller API, and AWS cloud + AI/MCP projects on GitHub, which covers the core skills most job descriptions require. Continue building modules 5-10 while applying.

---

**Main curriculum:** [README.md](README.md)
**GitHub guide:** [GITHUB_WORKFLOW.md](GITHUB_WORKFLOW.md)
