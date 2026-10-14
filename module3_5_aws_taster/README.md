# Module 3.5: AWS Taster

**Project:** Hello-AWS (one Lambda + one CloudFormation stack)
**Duration:** about 2 weeks (8 sessions)
**AUTOCOR mapping:** Domain 2.0 (Infrastructure as Code, via CloudFormation); Domain 1.6 (calling a cloud API / CLI); Domain 3.6 (no hardcoded keys, least privilege). The exam is cloud-agnostic. AWS is the curriculum's primary cloud, not an exam requirement.

---

## Why this module exists

Module 3 taught you to call someone else's API (CML). This module starts the other direction, but not by jumping to a function.

Order inside this module: **what the cloud is, the bill, then IAM and the CLI.** Lambda and CloudFormation are the last two sessions, a small proof that you can place code and declare one bucket. They are not the opening topic.

A separate 12-week AWS architect course (VPC, EC2, load balancers, databases, containers, the Solutions Architect exam) is real and useful. It is not this two-week module. The networking half of that course is taught as labs in Module 4.5, after controller APIs, so the REST you just learned does not go cold. Terraform is Module 6.5.

Two deliverables, at the end of the taster:

1. **Lambda** — a Python function AWS runs for you when an HTTP request arrives. No server to patch, no SSH.
2. **CloudFormation** — a YAML file that declares an S3 bucket. AWS creates it. You do not click it into existence, and you do not write a Python loop that calls "create bucket" by hand.

Those are the two habits of cloud work: **code that runs on an event**, and **a template that is the source of truth for what exists**. Terraform (Module 6.5) is the second habit with a different language. The deep AWS module (4.5) adds IAM roles, boto3, EventBridge, Secrets Manager, and Bedrock. This module is the on-ramp so 4.5 is not a cold start.

---

## What you will not do here

- No VPC design, no Transit Gateway, no production account strategy.
- No boto3 pagination project. You will see the idea; Module 4.5 builds it.
- No Bedrock, MCP, or agents. Those are Module 4.5, Domain 4.

---

## Session plan

| Session | Goal |
|---|---|
| **S1** | What an account, region, and bill actually are. Create the account. Turn on a budget alarm before any resource exists. |
| **S2** | IAM: user vs role vs policy. Least privilege. CLI profile. No access keys in git. |
| **S3** | Lambda mental model. First function, run it in the console. |
| **S4** | HTTP Function URL. Function reads a small device JSON and returns it. |
| **S5** | Imperative vs declarative. CloudFormation template for one S3 bucket. |
| **S6** | `aws cloudformation deploy`. Change the template, deploy again, see an update instead of a duplicate. |
| **S7** | Break and fix: a too-broad IAM policy, or a stack that fails on a bad property. Read the error. |
| **S8** | README: what you built, what IAM allowed, how to tear the stack down. |

---

## Security rules

- Never commit AWS access keys, secret keys, or account IDs you treat as sensitive. `.gitignore` in this folder ignores common key filenames.
- Prefer a named CLI profile. Do not paste keys into Python files.
- The IAM user for this module gets only what the lab needs, not `AdministratorAccess`, once you know which actions you are calling.
- A budget alarm is part of the lab, not optional. Free tier is not a promise that the bill stays at zero.
