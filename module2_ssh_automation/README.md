# Module 2: SSH Automation (Light Introduction)

**Project:** Network Device Backup Script
**Duration:** ~1 week (4 sessions)
**AUTOCOR mapping:** Background knowledge for Domain 1 (legacy automation approach); touches 3.2 (logging), 3.3 (diagnosing from output), 3.6 (secret management)

---

## Philosophy — read this first

SSH/Netmiko is **legacy** technology being steadily replaced by APIs (REST, NETCONF/RESTCONF). You need to know it exists, understand how it works, and be able to explain *why the industry is moving away from it*. **Do not sink weeks here** — one week, one working script, move on to REST (Module 3), which is where the real investment goes.

The value of this module for interviews is not "I can use Netmiko." It's: *"I understand traditional CLI-scraping automation, its failure modes, and why structured APIs are the modern answer."* That framing signals maturity.

---

## What you will build

A Python script that:
- connects to your **CML** lab devices over SSH using **Netmiko**,
- runs `show running-config` (and optionally other `show` commands),
- saves each device's config to a **timestamped** file in an organized `backups/` directory,
- reads device details from an **inventory file** (never hardcoded), with **credentials from environment variables** (never committed),
- logs what it did and handles connection failures gracefully.

You write the script. The `theory_guide.md` teaches the concepts; the guided sessions have you build it step by step.

---

## Learning objectives

- How SSH automation works at a high level (interactive shell vs programmatic session)
- `Paramiko` vs `Netmiko` — what each layer does
- Netmiko core: `ConnectHandler`, the device dictionary, `send_command` vs `send_config_set`, prompt handling
- Turning unstructured CLI text into files (config backup) — and why parsing `show` output is fragile
- **Secret management**: credentials via env vars / gitignored files, never in source (AUTOCOR 3.6)
- **Why APIs are replacing SSH screen-scraping**: structured data, idempotency, versioned models, no prompt fragility

---

## Session plan (4 sessions)

Each session follows the teaching contract: **explain → build → break & fix → recall** (an Anki deck per session).

| Session | Goal |
|---|---|
| **S1** | Explain SSH-automation mental model; connect to ONE CML device with Netmiko and run one `show` command |
| **S2** | Loop over an inventory of devices; back up `show running-config` to timestamped files; organize `backups/` |
| **S3** | Robustness: error handling (unreachable device, auth failure, timeout), logging, secrets from env vars |
| **S4** | Break & fix (diagnose a realistic SSH failure), write the "why SSH is being replaced" section, polish + push |

---

## How to run (once you've built it)

```bash
# from repo root
source .venv/bin/activate
pip install -r module2_ssh_automation/requirements.txt

# provide credentials via environment (never hardcode)
export NET_USER="your_cml_username"
export NET_PASS="your_cml_password"

cd module2_ssh_automation
cp devices.example.yaml devices.yaml   # then edit devices.yaml with your CML device IPs (devices.yaml is gitignored)
python3 backup_configs.py
```

> **CML note:** Devices come from your CML lab. You have CML access via the CML MCP tools — use them to confirm device management IPs / reachability before scripting against them.

---

## Project README template (fill this in for your GitHub project)

```markdown
# Network Device Backup Script

A Python script that backs up running configurations from Cisco devices via SSH using Netmiko.

## What It Does
- Connects to Cisco IOS devices via SSH
- Retrieves running configuration
- Saves configs with timestamps to an organized backup directory

## Why SSH Is Being Replaced
< brief explanation: screen-scraping fragility, unstructured text, no idempotency, prompt/paging issues — vs structured, model-driven APIs >

## How to Run
< instructions including CML lab setup and how credentials are supplied via env vars >

## Technologies
Python 3.x, Netmiko, SSH
```

---

## Security ground rules (non-negotiable)

- **Never hardcode usernames, passwords, or enable secrets** in `.py` files. Read them from environment variables (or a gitignored secrets file).
- **Never commit** `devices.yaml` (if it contains IPs/creds), `.env`, or the `backups/` contents. These are gitignored.
- Configs themselves can contain secrets (SNMP strings, hashed passwords) — treat `backups/` as sensitive.
