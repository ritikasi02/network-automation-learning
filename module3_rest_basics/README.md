# Module 3: REST API Basics

**Project:** Network API Dashboard (built week by week)
**Duration:** 3–4 weeks (12–16 sessions)
**AUTOCOR mapping:** Domain **1.6** (consume REST APIs: auth, pagination, rate limits, error handling, persistent auth); Domain **2.2** (CML REST API automation); Domain **3.3** (diagnose from logs/output); Domain **3.6** (secrets, not hardcoded)

---

## Philosophy — read this first

Module 2 taught you the **legacy** way: a robot typing CLI commands over SSH and scraping text. That still exists in the field, but it is not where the industry is going.

**REST APIs are the foundation of everything modern** — Catalyst Center, Meraki, CML, AWS, Azure, every SaaS product. This module is the real investment. We will take our time here.

The value for interviews is not "I imported `requests`." It is: *"I understand HTTP as a contract (method + URL + headers + body → status + JSON), I can authenticate, handle failure, and wrap a vendor API in a reusable client."*

---

## What you will build

A Python application that:

1. **Talks HTTP** — GET/POST (later PUT/DELETE) with the `requests` library
2. **Parses JSON** — treat API responses as data (dicts/lists), not blobs of text
3. **Authenticates** — token-based login against a real lab API (CML, or a DevNet sandbox if CML is not up)
4. **Wraps the API in a reusable client class** — you will reuse this pattern in Module 4 (Catalyst Center / Meraki)
5. **Handles failure the way production code must** — timeouts, 401/403/404/429, retries (AUTOCOR 1.6)
6. **Displays data** — a small Flask dashboard of lab topology (nodes, links, status) in week 3

You write the code. `theory_guide.md` teaches the concepts; sessions have you build step by step.

---

## Learning objectives

- HTTP request/response: URL, method, headers, body, status codes
- JSON as the language APIs speak (and why it beats CLI text)
- The `requests` library: `get`/`post`, `.status_code`, `.json()`, timeouts
- Authentication: Basic vs API key vs **token** (the CML / Catalyst Center pattern)
- A reusable **API client class** (base URL, session, token, error handling)
- Pagination, rate limiting, retries — AUTOCOR 1.6
- Flask enough to render live data in a browser
- Why this is the same *job* as Module 2 (get device data) with a completely different *interface*

---

## Session plan

Each session follows: **explain → build → break & fix → recall**.

| Session | Goal |
|---|---|
| **S1** | HTTP mental model; first `requests.get` against a public no-auth API; inspect status + JSON |
| **S2** | Walk nested JSON; pull specific fields; write a small report file (JSON) |
| **S3** | Authenticate to CML (or DevNet sandbox); store a token; call a protected endpoint |
| **S4** | Start the reusable client class (`CmlClient`: login, get labs) |
| **S5** | Expand the client: nodes, links, topology; timeouts + specific HTTP errors |
| **S6** | Pagination + 429/rate-limit handling (even if our lab is small — the *pattern* is the point) |
| **S7–S8** | Flask dashboard: list labs, show node status |
| **S9+** | Polish, README, API reference table, push |

Session 1 does **not** need CML. We start on a public API so HTTP is the only new idea.

---

## Lab options (from Session 3 onward)

| Option | When to use |
|---|---|
| **Your CML** | Best — this is the curriculum's intended target |
| **Cisco DevNet CML sandbox** | If your CML is down or you are away from the lab |
| **Public JSON APIs** | Session 1–2 only (learn HTTP without auth) |

We will pick the live target together before Session 3. Do not put CML passwords in code.

---

## How to set up (Session 1)

```bash
# from repo root — use the same venv as Modules 1 and 2
source .venv/bin/activate
pip install -r module3_rest_basics/requirements.txt

cd module3_rest_basics
```

You will create `first_call.py` in Session 1. Do not copy a finished script.

---

## Security ground rules (same as Module 2)

- **Never** hardcode usernames, passwords, tokens, or API keys in `.py` files
- Read secrets from environment variables or a gitignored `.env`
- Never commit `.env` — only `.env.example` (placeholders, no real values)

---

## Project README template (fill this in later for GitHub)

```markdown
# Network API Dashboard

A Python application that talks to Cisco CML over REST and displays
lab topology in a small local web dashboard.

## What It Does
- Authenticates with the CML REST API
- Retrieves labs, nodes, links, and status
- Displays topology in a Flask dashboard
- Ships a reusable API client class

## Architecture
< Python app -> CML REST API -> browser dashboard >

## API Endpoints Used
< table: method, path, what it returns >

## How to Run
< CML URL, env vars, pip install, flask command >

## What I Learned
< HTTP, JSON, token auth, error handling, reusable client >

## Technologies
Python 3.x, requests, Flask, JSON, REST APIs
```
