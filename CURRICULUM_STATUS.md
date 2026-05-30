# Curriculum Progress Tracker

**Last Updated:** May 12, 2026
**Overall Progress:** 0% (all modules incomplete)
**Pace:** 20-30 minutes per day, 4 days per week (~1.5-2 hours per week)
**Estimated Completion:** 10-12 months from start

---

## Progress Overview

```
Module 1:   ░░░░░░░░░░░░░░░░░░░░   0%  IN PROGRESS (materials created, learning not started)
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

Total:      ░░░░░░░░░░░░░░░░░░░░   0%
```

---

## Module 1: Python Fundamentals (6-8 weeks)

**Status:** INCOMPLETE - Materials exist, learning not yet done
**GitHub Project:** Network Config Analyzer

### What Exists

The learning materials (theory guide, exercises, sample configs, sample code) were generated previously. However, no independent learning or project building has been done yet.

| Item | Exists | Learned/Built Independently |
|------|--------|-----------------------------|
| theory_guide.md | Yes | Not yet studied |
| exercises.md | Yes | Not yet completed |
| config_parser.py | Yes (sample) | Not yet built independently |
| inventory_manager.py | Yes (sample) | Not yet built independently |
| Sample configs | Yes | Available for use |
| GitHub project (Config Analyzer) | No | Not yet started |

### What Needs to Happen

- [ ] Work through Python basics by building the Config Analyzer project from scratch
- [ ] Learn variables, strings, lists, dicts by writing parsing functions
- [ ] Learn file I/O by reading config files and writing reports
- [ ] Learn regex by parsing CLI output
- [ ] Learn functions and classes by organizing the project
- [ ] Learn error handling by making the tool robust
- [ ] Write a proper README for the project
- [ ] Push the completed project to GitHub

### Completion Criteria

You are done with Module 1 when:
1. You have independently built a config analyzer tool (not copied the sample)
2. You can explain every line of your code
3. Your project is on GitHub with a clear README
4. You have made at least 15-20 commits showing your progress

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
