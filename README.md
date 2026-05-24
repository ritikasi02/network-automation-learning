# Network Automation & Cloud Learning Path

A project-driven curriculum for a senior network engineer transitioning into Solution Engineering / Technical Pre-Sales roles that require Python, REST APIs, Azure, Ansible, and Cloud Automation skills.

---

## About Me

- 12 years at Cisco: 8 years as Network Consulting Engineer, 4 years as Technical Marketing Engineer
- Deep expertise in SD-Access, BGP EVPN VXLAN, Catalyst Center, ISE, SD-WAN
- Familiar with YANG/NETCONF/RESTCONF concepts but no hands-on automation experience
- Using Cursor AI to help write and understand code
- Lab access: CML, Catalyst Center, Cat9300/9500, ISE
- Learning style: build projects, not watch tutorials

## Career Target
**Role:** Solution Engineer / Technical Pre-Sales Engineer at a cloud or networking company (Microsoft, AWS, or similar)

**Required skills:** Python, REST APIs, Terraform, Azure, AWS, Ansible, CI/CD, Docker, Network Automation, Cloud Integration, AI/ML awareness

**Proof of competence:** A GitHub profile with real projects that demonstrate hands-on skills to hiring managers

---

## Curriculum Overview

| # | Module | Duration | GitHub Project | Key Skills |
|---|--------|----------|---------------|------------|
| 1 | Python Fundamentals | 4-5 weeks | Network Config Analyzer | Python, file I/O, regex, data structures |
| 2 | SSH Automation (Light Intro) | 1 week | Device Backup Script | Netmiko, SSH basics |
| 3 | REST API Basics | 3-4 weeks | Network API Dashboard | HTTP, requests, JSON, API design |
| 3.5 | Azure Taster | 2 weeks | Hello-Azure (Function + Bicep deploy) | Azure CLI, Azure Functions, Bicep basics |
| 4 | Controller APIs | 4-5 weeks | Catalyst Center Automation Toolkit | Catalyst Center API, Meraki API, SDKs |
| 4.5 | Azure Cloud Automation (Deep Dive) | 6-8 weeks | Azure Network Automation Platform | Azure Functions, Azure REST APIs, AI Services |
| 5 | NETCONF/YANG (Compressed) | 1-2 weeks | NETCONF Config Manager | ncclient, YANG models, RESTCONF |
| 6 | Ansible (Shrunk) | 2 weeks | Ansible Network Mini-Collection | Playbooks, Jinja2, network modules |
| 6.5 | Terraform + AzureRM | 4-5 weeks | Azure Hub-and-Spoke IaC | Terraform, HCL, AzureRM provider, modules, state |
| 6.6 | AWS Mini-Module (Optional) | 2-3 weeks | Lambda + boto3 Network Tool | AWS Lambda, boto3, AWS CLI, IAM basics |
| 7 | Testing & Validation | 3-4 weeks | Network Test Framework | pytest, pyATS, pre/post validation |
| 7.5 | Docker Basics | 1 week | Containerize Earlier Project | Docker, Dockerfile, docker-compose basics |
| 8 | Orchestration | 3-4 weeks | Network Orchestration Engine | Nornir, event-driven automation |
| 9 | CI/CD with GitHub Actions | 3-4 weeks | Automated Network Pipeline | GitHub Actions, GitOps, linting |
| 10 | Capstone Project (Scoped Down) | 4-6 weeks | Cloud-Integrated Network Automation Platform | Pick 3-4 components, not all |

**Total estimated duration: 14-18 months realistic** at 20-30 minutes per day, 4 days per week (~1.5-2 hours per week)

This is an honest estimate. Some weeks you will move faster, some weeks life happens. The goal is steady forward motion, not speed.

---

## Current Status

- [ ] **Module 1: Python Fundamentals** - IN PROGRESS (material created, learning not completed)
- [ ] Module 2: SSH Automation - Not Started
- [ ] Module 3: REST API Basics - Not Started
- [ ] Module 3.5: Azure Taster - Not Started
- [ ] Module 4: Controller APIs - Not Started
- [ ] Module 4.5: Azure Cloud Automation (Deep Dive) - Not Started
- [ ] Module 5: NETCONF/YANG - Not Started
- [ ] Module 6: Ansible (Shrunk) - Not Started
- [ ] Module 6.5: Terraform + AzureRM - Not Started
- [ ] Module 6.6: AWS Mini-Module (Optional) - Not Started
- [ ] Module 7: Testing & Validation - Not Started
- [ ] Module 7.5: Docker Basics - Not Started
- [ ] Module 8: Orchestration - Not Started
- [ ] Module 9: CI/CD with GitHub Actions - Not Started
- [ ] Module 10: Capstone Project (Scoped Down) - Not Started

**Overall Progress: 0% complete**

---

## Module Details

### Module 1: Python Fundamentals (4-5 weeks)

**Philosophy:** Learn Python by building a real tool, not by reading theory first. You will build a Network Configuration Analyzer from session one. Every Python concept is introduced because you need it for the project, not because it is next in a textbook.

**GitHub Project: Network Config Analyzer**

A command-line tool that reads Cisco IOS configuration files, extracts key data (hostnames, interfaces, IPs, routing protocols, VLANs), detects issues (duplicate IPs, shutdown interfaces, missing descriptions), and generates reports in JSON, CSV, and text formats.

**What you will learn along the way:**
- Variables, strings, lists, dictionaries, sets, file I/O (Week 1 — compressed because you already think in network constructs like interfaces, IPs, and VLANs)
- Regular expressions for parsing CLI output (Week 2)
- Functions for reusable automation logic (Week 3)
- Classes to model network devices, error handling, and logging (Week 4)
- Polish: put it all together, write README, clean up (Week 5 — compressed because you have been documenting as you go)

**Weekly structure (4 sessions of 20-30 min):**
- Session 1: Learn concept by adding a feature to the project
- Session 2: Expand the feature, handle edge cases
- Session 3: Refactor and improve what you built
- Session 4: Write README section for what you built, commit and push

**Time estimate:** 4-5 weeks (16-20 sessions)

**What this teaches an interviewer about you:**
This project proves you can write Python from scratch, parse unstructured data, work with multiple file formats, and build a practical tool that solves a real network operations problem. It shows you understand data structures, error handling, and code organization. For a Solution Engineer role, this demonstrates you can build internal tools and automate repetitive tasks.

**README template for this project:**

```markdown
# Network Config Analyzer

A Python tool that parses Cisco IOS configuration files, extracts network
data, detects configuration issues, and generates multi-format reports.

## What It Does
- Parses Cisco IOS/IOS-XE configuration files
- Extracts hostnames, interfaces, IP addresses, routing protocols, VLANs
- Detects duplicate IPs, shutdown interfaces, missing descriptions
- Generates reports in JSON, CSV, and plain text

## Why I Built This
Learning Python through a practical network engineering use case. Every
feature taught me a new Python concept while solving a real problem.

## How to Run
< step-by-step instructions >

## Sample Output
< screenshot or text showing what the tool produces >

## What I Learned
< list of Python concepts and how they apply to networking >

## Technologies
Python 3.x, regex, JSON, CSV, file I/O
```

---

### Module 2: SSH Automation - Light Introduction (1 week)

**Philosophy:** SSH/Netmiko is legacy technology being replaced by APIs. You need to know it exists and understand the basics, but do not invest weeks here. One week, one script, move on.

**GitHub Project: Device Backup Script**

A simple Python script using Netmiko that connects to CML lab devices via SSH, runs `show running-config`, and saves the output to timestamped backup files.

**What you will learn:**
- How SSH automation works at a high level
- Installing and using the Netmiko library
- Connecting to a device and running commands
- Why the industry is moving away from SSH scraping toward APIs

**Time estimate:** 1 week (4 sessions)

**What this teaches an interviewer about you:**
You understand traditional network automation methods and why they are being replaced. You can work with legacy systems when needed but you prioritize modern approaches. This shows practical awareness of the industry transition.

**README template for this project:**

```markdown
# Network Device Backup Script

A Python script that backs up running configurations from Cisco devices
via SSH using Netmiko.

## What It Does
- Connects to Cisco IOS devices via SSH
- Retrieves running configuration
- Saves configs with timestamps to organized backup directory

## Why SSH Is Being Replaced
< brief explanation of why APIs are preferred over screen scraping >

## How to Run
< instructions including CML lab setup >

## Technologies
Python 3.x, Netmiko, SSH
```

---

### Module 3: REST API Basics (3-4 weeks)

**Philosophy:** REST APIs are the foundation of everything modern: cloud platforms, controllers, SaaS products. This module is your gateway to the cloud and automation world. Invest time here.

**GitHub Project: Network API Dashboard**

A Python application that talks to your CML lab's REST API, retrieves lab topology data (nodes, links, status), and presents it through a simple local web dashboard. Also includes a reusable API client library you will use in later modules.

**What you will learn:**
- HTTP methods (GET, POST, PUT, DELETE) and status codes
- JSON data structures and parsing
- The `requests` library for making API calls
- Authentication methods (Basic, Token, API Key)
- Building a reusable API client class
- Error handling for network requests (timeouts, retries, rate limits)
- Flask basics for building a simple web interface

**Weekly structure:**
- Week 1: HTTP fundamentals, first API calls to CML, JSON handling
- Week 2: Build reusable API client class, authentication, error handling
- Week 3: Build the dashboard with Flask, display live lab data
- Week 4: Polish, add features, write documentation (optional stretch week)

**Time estimate:** 3-4 weeks (12-16 sessions)

**What this teaches an interviewer about you:**
REST API fluency is non-negotiable for Solution Engineer roles. This project proves you understand HTTP, authentication, JSON, error handling, and can build tools that consume APIs. The dashboard component shows you can present data visually, which matters in pre-sales.

**README template for this project:**

```markdown
# Network API Dashboard

A Python application that interacts with Cisco CML REST APIs to retrieve
and display lab topology information through a web dashboard.

## What It Does
- Authenticates with CML REST API
- Retrieves lab topology data (nodes, links, status)
- Displays network topology in a web dashboard
- Includes reusable API client library

## Architecture
< simple diagram showing: Python App -> CML REST API -> Dashboard >

## API Endpoints Used
< table of endpoints, methods, and what they return >

## How to Run
< step-by-step including CML setup >

## What I Learned
< REST concepts, authentication, error handling >

## Technologies
Python 3.x, requests, Flask, JSON, REST APIs
```

---

### Module 3.5: Azure Taster (2 weeks)

**Philosophy:** Keep the cloud muscle warm right after learning REST APIs. You just learned how to call APIs — now call one that provisions real cloud infrastructure. This lightweight module gives you early Azure exposure so Module 4.5 is not a cold start. Two weeks, two small deliverables, move on.

**GitHub Project: Hello-Azure (Function + Bicep deploy)**

Two small pieces in one repo: (1) an HTTP-triggered Azure Function in Python that returns device info from a JSON file, and (2) a Bicep template that deploys a storage account to Azure. Together they prove you can do serverless compute and declarative IaC on Azure.

**What you will learn:**
- Azure free tier account setup and Portal navigation
- Azure CLI basics (`az login`, `az group create`, `az functionapp create`)
- Creating and deploying an HTTP-triggered Azure Function in Python
- Bicep syntax for declaring Azure resources (storage account)
- Deploying infrastructure with `az deployment group create`
- The difference between imperative (CLI/SDK) and declarative (Bicep/Terraform) IaC

**Weekly structure:**
- Week 1: Azure account setup, Azure CLI, build and deploy HTTP-triggered Function
- Week 2: Write Bicep template for a storage account, deploy it, write README

**Time estimate:** 2 weeks (8 sessions)

**What this teaches an interviewer about you:**
You have hands-on Azure experience and understand both serverless compute and Infrastructure as Code at a basic level. This is an early signal that you are cloud-capable, not just network-capable.

**README template for this project:**

```markdown
# Hello-Azure

A starter Azure project: one HTTP-triggered Azure Function in Python
and one Bicep-deployed storage account.

## What It Does
- Azure Function responds to HTTP requests with device info from JSON
- Bicep template deploys a storage account to a resource group

## Why Two Things?
Demonstrates both serverless compute (Azure Functions) and declarative
Infrastructure as Code (Bicep) — the two patterns that dominate cloud
engineering.

## How to Run
< Azure CLI commands for Function deploy and Bicep deploy >

## What I Learned
< Azure CLI, Functions, Bicep, imperative vs declarative IaC >

## Technologies
Python 3.x, Azure Functions, Azure CLI, Bicep
```

---

### Module 4: Controller APIs - Catalyst Center & Meraki (4-5 weeks)

**Philosophy:** You already know Catalyst Center deeply as a user. Now learn to automate it. Combined with Meraki (cloud-managed), this module bridges your existing expertise with your cloud automation goals.

**GitHub Project: Catalyst Center Automation Toolkit**

A collection of Python scripts and a CLI tool that automates common Catalyst Center operations: device inventory, site health monitoring, template deployment, and compliance checks. Includes a Meraki integration that pulls cloud-managed device data alongside on-prem Catalyst Center data.

**What you will learn:**
- Catalyst Center REST API authentication and token management
- Navigating API documentation and Swagger/OpenAPI specs
- SDK vs raw REST: when to use each
- Pagination, filtering, and async task polling
- Meraki Dashboard API basics
- Combining data from multiple API sources
- Building a CLI tool with `argparse`

**Weekly structure:**
- Week 1: Catalyst Center authentication, device inventory API
- Week 2: Site health, command runner, template APIs
- Week 3: Meraki Dashboard API, pulling cloud-managed data
- Week 4: Build CLI tool combining both platforms
- Week 5: Polish, error handling, documentation

**Time estimate:** 4-5 weeks (16-20 sessions)

**What this teaches an interviewer about you:**
You can automate enterprise network controllers via API, work across cloud-managed and on-prem platforms, and build tools that aggregate data from multiple sources. This is directly relevant to Solution Engineer roles at any networking or cloud company.

**README template for this project:**

```markdown
# Catalyst Center Automation Toolkit

A Python toolkit for automating Cisco Catalyst Center and Meraki Dashboard
operations via REST APIs.

## What It Does
- Pulls device inventory from Catalyst Center
- Monitors site health and compliance
- Deploys configuration templates
- Retrieves Meraki cloud-managed device data
- CLI interface for common operations

## Platforms
- Cisco Catalyst Center (on-prem controller)
- Cisco Meraki Dashboard (cloud-managed)

## API Reference
< table of APIs used from each platform >

## How to Run
< instructions for both Catalyst Center and Meraki >

## What I Learned
< controller APIs, SDK usage, multi-platform integration >

## Technologies
Python 3.x, requests, Catalyst Center API, Meraki API, argparse
```

---

### Module 4.5: Azure Cloud Automation - Deep Dive (6-8 weeks)

**Philosophy:** Azure is where your career is heading. This module connects your networking background to cloud automation. You will learn Azure fundamentals, build serverless functions, use Azure REST APIs, integrate Azure with your existing network tools, and get hands-on with Azure AI Services. This is the module that transforms you from a network engineer into a cloud-capable solution engineer.

**Prerequisites:** Complete Modules 1-4. You need Python and REST API skills before starting Azure.

#### Week-by-Week Breakdown

**Week 1-2: Azure Foundation**
- Create Azure free tier account (includes $200 credit for 30 days + 12 months of free services)
- Azure Portal navigation and resource groups
- Azure CLI installation and basic commands
- Understanding subscriptions, resource groups, and regions
- Deploy a simple resource (storage account) via CLI and Portal

**Week 3-4: Azure Functions**
- What serverless computing is and why it matters
- Create your first Azure Function (HTTP trigger) in Python
- Azure Functions Core Tools for local development
- Timer-triggered functions for scheduled automation
- Environment variables and application settings for configuration

**Week 5-6: Azure REST APIs and Integration**
- Azure Resource Manager (ARM) REST API basics
- Authentication with Azure AD (service principals, managed identities)
- Using the Azure SDK for Python (`azure-mgmt-*` packages)
- Build automation that manages Azure resources programmatically
- Connect Azure Functions to Catalyst Center or Meraki API (trigger network actions from cloud events)

**Week 7-8: Azure AI Services and Final Project**
- Azure AI Services overview (Cognitive Services, OpenAI Service)
- Call Azure OpenAI API from Python
- Build an AI-powered network troubleshooting assistant
- Final integration project combining Azure + network automation

**GitHub Project 1: Azure-Triggered Network Compliance Monitor**

An Azure Function that runs on a schedule (timer trigger), calls Catalyst Center or Meraki API to check device compliance, stores results in Azure Table Storage, and sends alerts via email (Azure Communication Services or SendGrid) when compliance violations are found.

**GitHub Project 2: AI-Powered Network Troubleshooter**

A Python application that takes a network problem description as input, uses Azure OpenAI Service to analyze it against your network documentation and common Cisco troubleshooting patterns, and returns structured troubleshooting steps. Demonstrates Azure AI integration with domain-specific network engineering knowledge.

**Time estimate:** 6-8 weeks (24-32 sessions)

**What this teaches an interviewer about you:**
This is the differentiator. Most network engineers cannot demonstrate cloud automation skills. These projects prove you can build serverless applications, work with cloud APIs, integrate on-prem network infrastructure with cloud services, and use AI services. For Microsoft, AWS, or any cloud company, this demonstrates you bridge the gap between traditional networking and modern cloud architecture.

**README template for Azure projects:**

```markdown
# Azure Network Compliance Monitor

An Azure Functions application that monitors network device compliance
by integrating Catalyst Center APIs with Azure cloud services.

## What It Does
- Runs on a schedule via Azure Timer Trigger
- Calls Catalyst Center API to check device compliance
- Stores compliance history in Azure Table Storage
- Sends email alerts when violations are detected

## Architecture
< diagram: Azure Function -> Catalyst Center API -> Azure Storage -> Alerts >

## Azure Services Used
- Azure Functions (serverless compute)
- Azure Table Storage (data persistence)
- Azure Communication Services (email alerts)

## Setup
< Azure account setup, function deployment, environment variables >

## What I Learned
< serverless, cloud APIs, hybrid cloud-network integration >

## Technologies
Python 3.x, Azure Functions, Azure SDK, Catalyst Center API, REST APIs
```

---

### Module 5: NETCONF/YANG - Compressed (1-2 weeks)

**Philosophy:** You already understand YANG models and NETCONF concepts from your Cisco work. This module is about converting that conceptual knowledge into hands-on automation. One focused week of building, not re-learning theory.

**GitHub Project: NETCONF Config Manager**

A Python script using `ncclient` that connects to a CML IOS-XE device via NETCONF, retrieves interface configurations using YANG models, makes configuration changes, and validates the results. Includes RESTCONF examples for comparison.

**What you will learn:**
- Translating YANG model knowledge into working Python code
- Using `ncclient` for NETCONF operations (get, get-config, edit-config)
- XPath and XML filtering for targeted data retrieval
- RESTCONF as the HTTP-based alternative
- When to choose NETCONF vs REST API vs CLI

**Time estimate:** 1-2 weeks (4-8 sessions)

**What this teaches an interviewer about you:**
You understand model-driven programmability, the industry direction for network automation. Combined with your existing YANG expertise, this proves deep technical understanding of modern network management protocols.

**README template for this project:**

```markdown
# NETCONF Config Manager

A Python tool for managing Cisco IOS-XE device configurations using
NETCONF/YANG and RESTCONF.

## What It Does
- Retrieves interface configs via NETCONF using YANG models
- Makes configuration changes with edit-config
- Validates changes with get-config
- Includes RESTCONF examples for comparison

## YANG Models Used
< list of models: ietf-interfaces, Cisco-IOS-XE-native, etc. >

## NETCONF vs RESTCONF vs CLI
< comparison table showing when to use each >

## Technologies
Python 3.x, ncclient, NETCONF, YANG, RESTCONF, XML
```

---

### Module 6: Ansible - Shrunk (2 weeks)

**Philosophy:** Ansible is still useful for config management, but Terraform is the bigger lever for cloud SE roles. Build enough Ansible to speak to it in interviews, then move on. Two focused weeks covering the essentials — inventory, playbooks, network modules, Jinja2, and Vault — so you can say "yes, I have used Ansible" with a real GitHub project behind you.

**GitHub Project: Ansible Network Mini-Collection**

A compact Ansible project with an inventory, two playbooks (backup + deploy), one Jinja2 template for config generation, and Vault-encrypted credentials. Tested against CML.

**What you will learn:**
- Ansible architecture: inventory, playbooks, modules
- Network-specific modules (`ios_config`, `ios_command`, `ios_facts`)
- Jinja2 templates for generating device configurations
- Ansible Vault for secrets management

**Weekly structure:**
- Week 1: Ansible installation, inventory file for CML, first playbook (backup configs), network modules (gather facts, push config)
- Week 2: Jinja2 template for generating a config, Vault for credentials, polish README

**Time estimate:** 2 weeks (8 sessions)

**What this teaches an interviewer about you:**
You have hands-on Ansible experience and can write playbooks, use templates, and manage secrets. You know when Ansible is the right tool (config management, device-level changes) versus when Terraform is better (cloud infrastructure provisioning). That distinction matters in interviews.

**README template for this project:**

```markdown
# Ansible Network Mini-Collection

A compact Ansible collection for Cisco IOS/IOS-XE automation:
backup, config deployment, and templating.

## What It Does
- Backs up running configurations from CML devices
- Deploys baseline configs generated from Jinja2 templates
- Uses Ansible Vault for credential management

## Project Structure
< tree showing playbooks/, templates/, inventory, group_vars/ >

## How to Run
< ansible-playbook commands for backup and deploy >

## Ansible vs Terraform
< brief comparison: when to use each >

## Technologies
Ansible, Jinja2, YAML, Ansible Vault, Cisco IOS modules
```

---

### Module 6.5: Terraform + AzureRM (4-5 weeks)

**Philosophy:** Terraform is the dominant Infrastructure as Code tool in 2026 cloud SE job descriptions. If you only learn one IaC tool deeply, make it Terraform. This module teaches you to declare, plan, and apply cloud infrastructure the way every cloud team works — in HCL, with state management, modules, and workspaces. The project is an Azure hub-and-spoke network built entirely in Terraform, which is a pattern you will see in every enterprise cloud deployment.

**GitHub Project: Azure Hub-and-Spoke IaC**

A Terraform project that builds a hub-and-spoke Azure network: one hub VNet, two spoke VNets, VNet peering, NSGs, and a jumpbox VM. Organized with modules, variables, and remote state.

**What you will learn:**
- HCL syntax: resources, data sources, variables, outputs, locals
- AzureRM provider configuration and authentication
- Terraform workflow: `init`, `plan`, `apply`, `destroy`
- State management: local state, then remote state in Azure Storage
- Modules: writing and consuming reusable modules for VNets and NSGs
- Workspaces for managing dev/prod environments
- `terraform fmt`, `terraform validate`, and `tflint` for code quality

**Weekly structure:**
- Week 1: HCL syntax, install Terraform, deploy your first resource (resource group + VNet)
- Week 2: Providers, variables, outputs, deploy the hub VNet with subnets and an NSG
- Week 3: Modules — refactor VNet into a reusable module, build two spoke VNets, add peering
- Week 4: Remote state in Azure Storage, workspaces for dev/staging, add jumpbox VM
- Week 5: Polish, `tflint`, write README with architecture diagram

**Time estimate:** 4-5 weeks (16-20 sessions)

**What this teaches an interviewer about you:**
Terraform proficiency is the single most valuable IaC skill for cloud SE roles in 2026. This project proves you can design cloud network architecture, write modular IaC, manage state, and work with Azure infrastructure. The hub-and-spoke pattern is real enterprise architecture, not a toy example.

**README template for this project:**

```markdown
# Azure Hub-and-Spoke IaC

A Terraform project that deploys an Azure hub-and-spoke network
architecture with VNet peering, NSGs, and a jumpbox.

## What It Does
- Deploys a hub VNet with shared services subnet
- Deploys two spoke VNets for workloads
- Configures VNet peering between hub and spokes
- Applies NSGs with least-privilege rules
- Provisions a jumpbox VM in the hub for management

## Architecture
< diagram: Hub VNet <-> Spoke1 VNet, Hub VNet <-> Spoke2 VNet >

## Project Structure
< tree showing modules/, environments/, main.tf, variables.tf, etc. >

## How to Run
< terraform init, plan, apply commands >

## State Management
< explanation of remote state in Azure Storage >

## What I Learned
< HCL, modules, state, AzureRM provider, hub-and-spoke networking >

## Technologies
Terraform, HCL, AzureRM provider, Azure VNet, NSG, Azure Storage
```

---

### Module 6.6: AWS Mini-Module (2-3 weeks, optional)

**Philosophy:** If AWS is on your target list, you need at least one AWS project so your resume is not Azure-only. This is a lightweight module: learn enough AWS to be conversant and have one Lambda project on GitHub. If your target is purely Microsoft/Azure, skip this and come back later.

**GitHub Project: Lambda + boto3 Network Tool**

An AWS Lambda function written in Python that uses boto3 to audit VPC security groups (or VPC route tables), identifies overly permissive rules, and writes a JSON report to an S3 bucket. Deployed via AWS CLI.

**What you will learn:**
- AWS account setup and free tier limits
- AWS CLI configuration and IAM basics (users, roles, policies)
- Lambda function creation and deployment
- boto3 SDK for Python (EC2, VPC, S3 clients)
- S3 bucket operations (put object, presigned URLs)
- Key differences between Azure and AWS (naming, structure, auth model)

**Weekly structure:**
- Week 1: AWS account, CLI setup, IAM user, first Lambda function (hello world), boto3 basics
- Week 2: Build the security group auditor with boto3, write results to S3
- Week 3: Polish, add input parameters, write README with Azure vs AWS comparison

**Time estimate:** 2-3 weeks (8-12 sessions)

**What this teaches an interviewer about you:**
You are not locked into a single cloud. You can work across Azure and AWS, understand both platforms' core services (compute, storage, IAM, networking), and can build serverless automation on either. Multi-cloud awareness is a strong signal for SE roles.

**README template for this project:**

```markdown
# Lambda + boto3 Network Tool

An AWS Lambda function that audits VPC security groups for overly
permissive rules and writes a report to S3.

## What It Does
- Scans all security groups in a VPC
- Identifies rules allowing 0.0.0.0/0 on sensitive ports
- Generates a JSON report with findings and recommendations
- Stores the report in an S3 bucket

## AWS Services Used
- AWS Lambda (serverless compute)
- boto3 SDK (EC2, VPC, S3)
- S3 (report storage)
- IAM (least-privilege execution role)

## Azure vs AWS
< comparison table of equivalent services >

## How to Run
< AWS CLI commands for deployment and invocation >

## What I Learned
< Lambda, boto3, IAM, multi-cloud patterns >

## Technologies
Python 3.x, AWS Lambda, boto3, AWS CLI, S3, IAM
```

---

### Module 7: Testing & Validation (3-4 weeks)

**Philosophy:** Writing automation without testing it is dangerous in production networks. This module teaches you to prove your automation works correctly, which is a skill most network engineers skip.

**GitHub Project: Network Test Framework**

A pytest-based testing framework that validates network state before and after changes. Includes tests for reachability, interface status, routing table entries, VLAN configurations, and compliance against expected state. Integrates with pyATS for Cisco-specific testing.

**What you will learn:**
- pytest fundamentals: fixtures, parametrize, markers
- Writing network-specific test cases
- Pre-change and post-change validation patterns
- pyATS for Cisco device testing
- Test-driven development (TDD) approach for network changes
- Generating test reports

**Time estimate:** 3-4 weeks (12-16 sessions)

**What this teaches an interviewer about you:**
Testing is what separates professional automation from hobby scripts. This proves you build reliable, production-grade automation. Hiring managers at cloud companies expect testing discipline.

**README template for this project:**

```markdown
# Network Test Framework

A pytest-based framework for validating network state and changes
with pre/post-change verification.

## What It Does
- Validates device reachability and interface status
- Verifies routing table entries match expected state
- Checks VLAN configurations for compliance
- Runs pre-change and post-change validation suites
- Generates HTML test reports

## Test Categories
< table of test types: reachability, routing, VLAN, compliance >

## How to Run
< pytest commands for different test suites >

## Technologies
Python 3.x, pytest, pyATS, requests
```

---

### Module 7.5: Docker Basics (1 week)

**Philosophy:** Almost every cloud SE job description mentions containers. This is the cheapest gap to close: one week, one Dockerfile, one docker-compose file. You are not trying to become a Kubernetes engineer — you just need to demonstrate you can containerize a Python application.

**GitHub Project: Containerize Earlier Project**

Take your Module 1 Network Config Analyzer (or another earlier project), write a Dockerfile for it, and a docker-compose.yaml to run it. The result is a container image that anyone can pull and run without installing Python or dependencies.

**What you will learn:**
- What containers are and why they matter (vs VMs, dependency isolation)
- Writing a Dockerfile (FROM, COPY, RUN, CMD)
- Building and running a container image
- docker-compose for multi-container setups (even if yours is single-container, learn the syntax)
- Tagging images and pushing to Docker Hub or GitHub Container Registry

**Time estimate:** 1 week (4 sessions)

**What this teaches an interviewer about you:**
You understand containerization, can package applications for reproducible deployment, and are familiar with the Docker toolchain. This checks the "containers" box on job descriptions without requiring a multi-month Kubernetes deep dive.

**README template for this project:**

```markdown
# Containerized Network Config Analyzer

The Module 1 Network Config Analyzer packaged as a Docker container
for portable, dependency-free execution.

## What It Does
- Runs the config analyzer inside a Docker container
- No Python installation required on the host
- Mount config files as a volume, get reports as output

## How to Run
docker build -t config-analyzer .
docker run -v ./configs:/app/configs config-analyzer

## Dockerfile Explained
< line-by-line explanation of the Dockerfile >

## What I Learned
< containers, Docker workflow, image building >

## Technologies
Docker, Dockerfile, docker-compose, Python 3.x
```

---

### Module 8: Orchestration (3-4 weeks)

**Philosophy:** Orchestration is about coordinating automation across multiple devices and systems. This module brings together everything you have learned into a scalable execution framework.

**GitHub Project: Network Orchestration Engine**

A Nornir-based orchestration tool that manages multi-device operations: concurrent configuration deployment, state collection, compliance checks, and automated remediation. Includes an event-driven component that reacts to webhook notifications.

**What you will learn:**
- Nornir framework for concurrent network automation
- Inventory management and filtering
- Task writing and result processing
- Event-driven automation with webhooks
- State management and idempotency
- Error handling across multiple devices

**Time estimate:** 3-4 weeks (12-16 sessions)

**What this teaches an interviewer about you:**
You can build automation that scales beyond single-device scripts. Orchestration skills show you think about production-grade systems, concurrency, and reliability, all critical for Solution Engineering roles.

**README template for this project:**

```markdown
# Network Orchestration Engine

A Nornir-based orchestration tool for managing multi-device network
operations with concurrent execution and event-driven automation.

## What It Does
- Deploys configurations to multiple devices concurrently
- Collects device state and generates reports
- Checks compliance and triggers remediation
- Responds to webhook events for automated workflows

## Architecture
< diagram showing Nornir inventory, tasks, and event flow >

## Technologies
Python 3.x, Nornir, webhooks, concurrent execution
```

---

### Module 9: CI/CD with GitHub Actions (3-4 weeks)

**Philosophy:** CI/CD is how professional teams deploy changes. This module teaches you to automate the testing and deployment of your network automation code using GitHub Actions.

**GitHub Project: Automated Network Pipeline**

A GitHub Actions pipeline that lints your Python code, runs your test suite, validates network configurations, and deploys changes to your CML lab. Includes branch protection rules, pull request workflows, and automated documentation generation.

**What you will learn:**
- Git branching strategies (feature branches, pull requests)
- GitHub Actions workflow syntax (YAML)
- Automated linting and code quality checks
- Running pytest in CI
- Secrets management in GitHub Actions
- Deployment workflows and approval gates
- GitOps principles for network infrastructure

**Time estimate:** 3-4 weeks (12-16 sessions)

**What this teaches an interviewer about you:**
CI/CD experience is expected for any modern engineering role. This project proves you understand DevOps practices, can build automated pipelines, and follow professional software development workflows. This is particularly valued at cloud companies.

**README template for this project:**

```markdown
# Automated Network Pipeline

A CI/CD pipeline using GitHub Actions that automates testing,
validation, and deployment of network automation code.

## What It Does
- Lints Python code on every push
- Runs network test suite automatically
- Validates configuration changes before deployment
- Deploys approved changes to lab environment

## Pipeline Stages
< diagram: Push -> Lint -> Test -> Validate -> Deploy >

## Workflows
< table of GitHub Actions workflows and triggers >

## Technologies
GitHub Actions, Python, pytest, YAML, Git
```

---

### Module 10: Capstone Project - Scoped Down (4-6 weeks)

**Philosophy:** This is your interview piece. A single, polished project that combines a focused subset of what you have learned. **A focused capstone that does 3-4 things well beats a sprawling one that does 8 things poorly. Pick the components that best match the specific role you are applying for.**

**GitHub Project: Cloud-Integrated Network Automation Platform**

Pick 3-4 components from this menu based on your target role:
- Discovers devices via Catalyst Center API
- Collects configurations via NETCONF and REST APIs
- Stores data in a structured format
- Runs compliance checks against defined policies
- Deploys remediation via Ansible
- Tests changes with pytest/pyATS
- Monitors via Azure Functions
- Uses Azure AI for intelligent analysis
- Deploys infrastructure via Terraform
- Containerized with Docker
- Deploys through a GitHub Actions CI/CD pipeline

**Example scoping for a Microsoft Azure SE role:** Azure Functions + Catalyst Center API + Terraform deployment + CI/CD pipeline (4 components, all cloud-relevant).

**Example scoping for a network automation role:** Catalyst Center API + NETCONF + pytest validation + CI/CD pipeline (4 components, all network-relevant).

**This project should include:**
- A clear README with architecture diagram
- Working code with proper error handling
- A test suite with good coverage
- A CI/CD pipeline
- Documentation that explains your design decisions and why you chose these components
- A demo video or screenshots

**Time estimate:** 4-6 weeks (16-24 sessions)

**What this teaches an interviewer about you:**
This is your portfolio centerpiece. It demonstrates system design skills, the ability to integrate multiple technologies, testing discipline, and CI/CD maturity. The scoping exercise itself shows you can make architectural trade-offs, which is a core Solution Engineering skill.

---

## Target Job Skills Map

This table maps each module to the skills that appear in real job descriptions for Solution Engineer and Technical Pre-Sales roles.

| Skill (Job Description Keyword) | M1 | M2 | M3 | M3.5 | M4 | M4.5 | M5 | M6 | M6.5 | M6.6 | M7 | M7.5 | M8 | M9 | M10 |
|----------------------------------|:--:|:--:|:--:|:----:|:--:|:----:|:--:|:--:|:----:|:----:|:--:|:----:|:--:|:--:|:---:|
| **Python / Scripting** | P | x | x | x | x | x | x | | | x | x | | x | | x |
| **REST APIs** | | | P | | P | x | x | | | | | | x | | x |
| **Ansible / IaC** | | | | | | | | P | | | | | x | x | x |
| **Infrastructure as Code (Terraform/Bicep)** | | | | P | | | | | P | | | | | | x |
| **Azure / Cloud Platforms** | | | | P | | P | | | x | | | | | | x |
| **AWS** | | | | | | | | | | P | | | | | x |
| **CI/CD / DevOps** | | | | | | | | | | | | | | P | x |
| **Containers (Docker)** | | | | | | | | | | | | P | | | x |
| **Network Automation** | x | P | x | | P | x | P | P | | | P | | P | x | P |
| **Cloud Integration** | | | | P | x | P | | | x | x | | | | | P |
| **AI/ML Basics** | | | | | | P | | | | | | | | | x |
| **Testing / QA** | | | | | | | | | | | P | | | x | x |
| **API Design** | | | P | | | x | | | | | | | | | x |
| **Git / Version Control** | x | x | x | x | x | x | x | x | x | x | x | x | x | P | x |

**P** = Primary focus of the module | **x** = Practiced or reinforced in the module

### How to Use This in Interviews

When a job description says "experience with REST APIs and Python scripting," you can point to Modules 1, 3, 4, and your GitHub projects. When it says "cloud automation and Azure," point to Modules 3.5 and 4.5. When it says "Terraform" or "Infrastructure as Code," point to Modules 3.5 and 6.5. This map helps you connect your learning directly to job requirements.

---

## CCNP Automation Blueprint Alignment (350-901 AUTOCOR v2.0)

This curriculum also aligns with the Cisco CCNP/CCIE Automation core exam (350-901 AUTOCOR v2.0 — "Designing, Deploying and Managing Network Automation Systems"). The old DEVCOR exam has been retired. AUTOCOR v2.0 has 4 domains focused on network automation, IaC, operations, and AI.

### Blueprint-to-Curriculum Map

| AUTOCOR Domain | Weight | Where Covered | Gaps to Fill |
|----------------|--------|---------------|--------------|
| **1.0 Network Automation** | 30% | | |
| 1.1 Ansible (VLANs, OSPF, ACLs) | | Module 6 | Ensure playbooks cover VLANs, OSPF, ACLs specifically |
| 1.2 Terraform (VLANs, OSPF, ACLs) | | Module 6.5 | Add IOS XE provider examples alongside AzureRM |
| 1.3 RESTCONF with YANG models | | Module 5 | Ensure VLANs, OSPF, ACLs via RESTCONF |
| 1.4 Python automation | | Module 1, all modules | Well covered |
| 1.5 Select automation approach | | Modules 6 vs 6.5 | Add comparison exercise: when Ansible vs Terraform vs Python |
| 1.6 REST APIs (pagination, auth, rate limiting) | | Module 3, 4 | Well covered |
| **2.0 Infrastructure as Code** | 30% | | |
| 2.1 Advanced Git (squash, cherry-pick, reset, revert) | | Module 9, GitHub Workflow | **Add exercises for advanced Git ops** |
| 2.2 CML automation via REST API | | Module 3 (CML API) | **Strengthen: automate CML lab topology with PyCML** |
| 2.2 Docker Compose | | Module 7.5 | Covered |
| 2.2 Source of truth (NetBox/Nautobot) | | Not covered | **GAP: Add awareness in Module 8** |
| 2.2 YANG-to-YAML/JSON payloads | | Module 5 | Add exercise generating payloads from YANG models |
| 2.3 GitLab CE CI/CD pipeline | | Module 9 (GitHub Actions) | **GAP: Note GitLab CE as exam alternative** |
| **3.0 Operations** | 20% | | |
| 3.1 Model-driven telemetry | | Not covered | **GAP: Add to Module 5** |
| 3.2 Logging strategy (syslog, webhooks) | | Module 1 | Well covered |
| 3.3 Diagnose problems from logs | | Module 1, 7 | Well covered |
| 3.4 pyATS change validation | | Module 7 | **Strengthen pyATS CLI tools coverage** |
| 3.5 CA-signed TLS certificates | | Not covered | **GAP: Add brief section in Module 9** |
| 3.6 Secure coding (input validation, secrets) | | Module 4.5 | Covered |
| **4.0 AI in Automation** | 20% | | |
| 4.1 AI-assisted code: benefits and risks | | Not covered | **GAP: Add to Module 4.5** |
| 4.2 Security risks in AI automation | | Not covered | **GAP: Add to Module 4.5** |
| 4.3 MCP server with Python FastMCP | | Not covered | **GAP: Add to Module 4.5** |
| 4.4 Conversational LLM agent for automation | | Module 4.5 (Azure OpenAI) | **Expand: build a proper LLM agent** |
| 4.5 Evaluate AI recommendation accuracy | | Not covered | **GAP: Add to Module 4.5** |

### How Gaps Will Be Closed

The gaps above do NOT require new modules. They will be folded into existing modules as additional exercises or sections:

| Gap | Where to Add | Effort |
|-----|-------------|--------|
| MCP server with FastMCP | Module 4.5, Week 7-8 (add a FastMCP exercise) | 2-3 sessions |
| LLM conversational agent | Module 4.5, Week 7-8 (expand AI project) | 2-3 sessions |
| AI risks and evaluation | Module 4.5, Week 7 (add a theory + exercise section) | 1-2 sessions |
| Model-driven telemetry | Module 5, add Day 3-4 exercise (gRPC dial-out) | 1-2 sessions |
| Advanced Git ops | Module 9, Week 1 (squash merge, cherry-pick, reset lab) | 1 session |
| GitLab CE CI/CD | Module 9, Week 2 (note alongside GitHub Actions) | 1 session |
| Source of truth (NetBox) | Module 8, mention as inventory source | 1 session |
| CML automation with PyCML | Module 3, Week 1 (CML API is already the project) | Already covered, strengthen |
| pyATS CLI tools | Module 7, Weeks 2-3 (expand from mention to hands-on) | 1-2 sessions |
| TLS certificates | Module 9, brief section on cert management | 1 session |

**Total additional effort:** ~12-15 sessions (~3-4 weeks) spread across existing modules. No timeline increase needed — these fit within existing module durations.

---

## Daily Learning Ritual

You have 20-30 minutes per day, 4 days per week. Here is how to make every session count without losing momentum.

### Before You Start (2 minutes)

1. Open your terminal and navigate to your project folder
2. Run `git pull` (in case you made changes from another machine)
3. Open Cursor AI
4. Read your last commit message to remember where you left off: `git log -1`

### During Your Session (15-25 minutes)

- **Build something.** Every session should produce working code, even if it is just 5 lines.
- **Use Cursor AI** to help you understand code you are writing. Ask it to explain concepts as you encounter them.
- **Do not read theory without coding.** If you need to learn a concept, learn it by immediately using it in your project.
- **If you are stuck for more than 5 minutes,** ask Cursor AI for help, simplify the problem, or move to a different part of the project.

### Before You Stop (3-5 minutes)

1. Save all files
2. Stage and commit your work: `git add -A && git commit -m "your message"`
3. Push to GitHub: `git push`
4. Update your README if you completed a feature or milestone
5. Write a one-line note to yourself about what to do next session (in a commit message or in a TODO comment in your code)

### Weekly Rhythm

| Day | Focus |
|-----|-------|
| Session 1 (e.g., Monday) | Build a new feature or start a new concept |
| Session 2 (e.g., Wednesday) | Continue building, handle edge cases |
| Session 3 (e.g., Thursday) | Refactor, clean up, add error handling |
| Session 4 (e.g., Saturday) | Document what you built, update README, review the week |

### Momentum Rules

- **Never skip two sessions in a row.** If you miss a day, do at least a 10-minute session the next available day, even if it is just reading your own code and adding a comment.
- **Commit every session.** Even if you only changed one line, commit it. Your GitHub contribution graph matters.
- **Keep a running README.** Update it as you build, not after you finish. A README written during development is always better than one written from memory.
- **Celebrate small wins.** Parsed your first config? That is a win. Made your first API call? Huge win. Commit it and move on.

---

## GitHub Workflow

This section teaches you how to use GitHub as part of every module. Your GitHub profile is your resume for technical roles.

**For the complete beginner-friendly guide with every command explained, see [GITHUB_WORKFLOW.md](GITHUB_WORKFLOW.md).**

### Quick Reference

**Start of every study session:**
```bash
cd ~/pyme/network_automation_learning
git pull
```

**End of every study session:**
```bash
git add -A
git commit -m "module1: add interface parsing function"
git push
```

**Start a new project (new module):**
```bash
mkdir module3_rest_basics
cd module3_rest_basics
touch README.md
git add -A
git commit -m "module3: initialize project structure"
git push
```

### Commit Frequency

- Commit at the end of every study session
- Commit when you complete a feature or fix a bug
- Commit before you try something risky (so you can undo)
- Do NOT wait until a project is "done" to commit

### Commit Message Format

Use this pattern: `moduleX: what you did`

**Good commit messages:**
- `module1: add function to parse interface configs`
- `module3: fix authentication token refresh logic`
- `module4: add Meraki API device inventory script`
- `module1: update README with sample output screenshots`

**Bad commit messages:**
- `update` (update what?)
- `fixed stuff` (what stuff?)
- `work in progress` (everything is work in progress)
- `asdfasdf` (future you will hate past you)

---

## Directory Structure

```
network_automation_learning/
├── README.md                              # This file
├── GITHUB_WORKFLOW.md                     # Detailed GitHub guide for beginners
├── CURRICULUM_STATUS.md                   # Progress tracking
├── module1_python_basics/                 # Module 1: Python Fundamentals
├── module2_ssh_automation/                # Module 2: SSH with Netmiko (1 week)
├── module3_rest_basics/                   # Module 3: REST API Basics
├── module3_5_azure_taster/                # Module 3.5: Azure Taster (2 weeks)
├── module4_controller_apis/               # Module 4: Controller APIs
├── module4_5_azure_automation/            # Module 4.5: Azure Cloud Automation (Deep Dive)
├── module5_netconf_yang/                  # Module 5: NETCONF/YANG (compressed)
├── module6_ansible/                       # Module 6: Ansible (shrunk)
├── module6_5_terraform/                   # Module 6.5: Terraform + AzureRM
├── module6_6_aws_mini/                    # Module 6.6: AWS Mini-Module (optional)
├── module7_testing/                       # Module 7: Testing & Validation
├── module7_5_docker/                      # Module 7.5: Docker Basics
├── module8_orchestration/                 # Module 8: Orchestration
├── module9_cicd/                          # Module 9: CI/CD with GitHub Actions
├── capstone_project/                      # Module 10: Capstone (scoped down)
└── shared_resources/                      # Shared utilities and templates
```

---

## Tools & Technologies

### You Will Use Throughout

| Tool | Purpose | When You Learn It |
|------|---------|-------------------|
| Python 3.x | Primary language | Module 1 |
| Git / GitHub | Version control, portfolio | Every module |
| Cursor AI | Coding assistant | Every module |
| CML | Network lab | Modules 1-8 |
| VS Code / Cursor | Editor | Every module |

### You Will Learn Per Module

| Technology | Module |
|------------|--------|
| regex, JSON, CSV | Module 1 |
| Netmiko | Module 2 |
| requests, Flask | Module 3 |
| Azure CLI, Bicep, Azure Functions | Module 3.5 |
| Catalyst Center API, Meraki API | Module 4 |
| Azure Functions, Azure SDK, Azure AI | Module 4.5 |
| ncclient, YANG, RESTCONF | Module 5 |
| Ansible, Jinja2, Vault | Module 6 |
| Terraform, HCL, AzureRM provider | Module 6.5 |
| AWS Lambda, boto3, AWS CLI | Module 6.6 |
| pytest, pyATS | Module 7 |
| Docker, Dockerfile, docker-compose | Module 7.5 |
| Nornir | Module 8 |
| GitHub Actions | Module 9 |

---

## Resources (Reference Only)

These are for looking things up when you are stuck. Do not use them as your primary learning method.

- [Python Official Docs](https://docs.python.org/3/) - Look up functions and modules
- [Cisco DevNet](https://developer.cisco.com) - API documentation
- [Catalyst Center API Docs](https://developer.cisco.com/docs/dna-center/) - Controller API reference
- [Meraki API Docs](https://developer.cisco.com/meraki/api/) - Cloud-managed API reference
- [Azure Documentation](https://learn.microsoft.com/en-us/azure/) - Azure service documentation
- [Azure Functions Python Guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python) - Serverless Python
- [Bicep Docs](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/) - Azure declarative IaC
- [HashiCorp Terraform Docs](https://developer.hashicorp.com/terraform/docs) - Terraform reference
- [AzureRM Provider Docs](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs) - Terraform Azure provider
- [AWS Lambda Python Docs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html) - Lambda with Python
- [Docker Docs](https://docs.docker.com/) - Container reference
- [Ansible Network Docs](https://docs.ansible.com/ansible/latest/network/index.html) - Network modules
- [GitHub Actions Docs](https://docs.github.com/en/actions) - CI/CD reference
- [pytest Documentation](https://docs.pytest.org/) - Testing framework

---

**Start here:** [Module 1: Python Fundamentals](module1_python_basics/)

**GitHub workflow guide:** [GITHUB_WORKFLOW.md](GITHUB_WORKFLOW.md)

**Track your progress:** [CURRICULUM_STATUS.md](CURRICULUM_STATUS.md)
