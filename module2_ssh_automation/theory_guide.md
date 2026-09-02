# Module 2 Theory Guide — SSH Automation with Netmiko

This is the authoritative concept scope for Module 2. Read a section before you build the
matching part of the script. Everything here is explained from first principles — assume no
prior networking or SSH knowledge.

---

## 1. What problem are we solving?

A network engineer logs into a router, types `show running-config`, and copy-pastes the output
into a file to keep a backup. Doing that by hand for 5 devices is tedious; for 500 it's
impossible. **SSH automation** means writing a program that logs in *for you*, runs the command,
and saves the output — the same keystrokes, done by code.

That's the whole idea, and also the whole limitation: the program is essentially a **robot typing
at a terminal and reading back the text** that scrolls past. Hold onto that mental model — it
explains every strength and every weakness of this approach.

---

## 2. SSH in one paragraph

**SSH (Secure Shell)** is an encrypted way to open a command-line session on a remote device over
the network (TCP port 22). It replaced **Telnet** (port 23), which sent everything — including
passwords — in plaintext. When you `ssh user@10.0.0.1`, SSH authenticates you (password or key),
then gives you an interactive shell where you type commands and see output. Network automation
just drives that session programmatically instead of by hand.

**Rule of thumb:** Telnet is plaintext and effectively banned in production; SSH is the encrypted
standard. If you ever see Telnet automation, that's a red flag.

---

## 3. The two libraries: Paramiko vs Netmiko

- **Paramiko** is the low-level Python SSH library. It gives you a raw SSH channel: send bytes,
  receive bytes. It knows *nothing* about Cisco, prompts, or `enable` mode. Using it directly for
  network devices means you hand-manage prompts, paging, and timing — painful.
- **Netmiko** is built *on top of* Paramiko, specifically for **network devices**. It knows how to:
  - detect and wait for the device **prompt** (`R1#`),
  - handle **`--More--` paging** (it disables paging with `terminal length 0`),
  - enter **enable / config mode**,
  - normalize behavior across many vendors via a **`device_type`** (e.g. `cisco_ios`).

**Mental model:** Paramiko = "a phone line to the device." Netmiko = "a phone line *plus* someone
who speaks fluent Cisco CLI and knows when the other side has finished talking." You'll use
**Netmiko**.

> **Interview Q:** *"Why Netmiko over Paramiko for network automation?"*
> **A:** Paramiko is a generic SSH transport; Netmiko adds network-device intelligence — prompt
> detection, paging disable, enable/config mode, per-vendor `device_type` handling — so you don't
> re-implement all that fragile terminal-handling yourself.

---

## 4. Netmiko core concepts

### 4.1 The device dictionary
You describe a device as a dict and hand it to `ConnectHandler`:

```python
device = {
    "device_type": "cisco_ios",   # tells Netmiko how to talk to this platform
    "host": "10.10.20.48",        # management IP (from your CML lab)
    "username": NET_USER,          # from environment, NOT hardcoded
    "password": NET_PASS,          # from environment, NOT hardcoded
    # "secret": NET_ENABLE,       # only if the device needs enable mode
}
```

### 4.2 Opening and closing the connection
`ConnectHandler(**device)` opens the SSH session and returns a connection object. Always close it.
The clean pattern is a context manager so it closes even on error:

```python
from netmiko import ConnectHandler
with ConnectHandler(**device) as conn:
    output = conn.send_command("show running-config")
# connection auto-closed here
```

### 4.3 `send_command` vs `send_config_set`
- **`send_command("show ...")`** — for **read/`show`** commands. Returns the output as a string.
  Netmiko waits for the prompt to know the command finished.
- **`send_config_set([...])`** — for **making changes**. You pass a *list* of config lines;
  Netmiko enters config mode, sends them, and exits. (You won't change configs in the backup
  project, but know this exists.)

### 4.4 Structured output (preview of the pain point)
`send_command(..., use_textfsm=True)` can turn some `show` outputs into lists of dicts using
TextFSM templates. This is a *band-aid* over the core problem: CLI output is unstructured text
that a human designed for eyeballs, not machines. It's the seam where SSH automation starts to
hurt — and exactly what APIs fix.

---

## 5. The backup pattern (what you're building)

Conceptually:
1. Load an **inventory** of devices (from `devices.yaml`) — hostnames + IPs + device_type.
2. Pull **credentials from environment variables** (`NET_USER`, `NET_PASS`).
3. For each device: connect → `send_command("show running-config")` → save to a file.
4. Name the file so backups don't overwrite each other and you can tell *when* each was taken:
   `backups/<hostname>_<YYYYMMDD-HHMMSS>.cfg`.
5. Log successes and failures; don't let one dead device kill the whole run.

**Timestamps:** use `datetime.now().strftime("%Y%m%d-%H%M%S")`. Sortable, filename-safe, and tells
you the backup's age at a glance.

**Rule of thumb:** a backup you can't date is barely a backup. Always timestamp.

---

## 6. Secret management (AUTOCOR 3.6 — do this right)

**Never** put usernames/passwords in your `.py` file. Anyone who reads the code (or your Git
history) gets your credentials. Instead:

```python
import os
NET_USER = os.environ["NET_USER"]   # set via: export NET_USER="..."
NET_PASS = os.environ["NET_PASS"]
```

- Credentials come from **environment variables** (or a **gitignored** `.env` / secrets file).
- `devices.yaml` (with real IPs) and `backups/` are **gitignored** — device configs can contain
  SNMP community strings and password hashes.
- If a required env var is missing, fail loudly with a clear message rather than connecting with
  blanks.

> **Interview Q:** *"Where do automation credentials live?"*
> **A:** Never in source. Environment variables for local/dev, a secrets manager (Vault, AWS
> Secrets Manager) for production. Source control is treated as public and untrusted.

---

## 7. Why SSH automation is being replaced (the point of this module)

You're driving a **human interface** with a robot. That creates fundamental problems that
structured APIs (REST, NETCONF/RESTCONF) don't have:

| Problem with SSH/CLI scraping | Why APIs are better |
|---|---|
| **Unstructured text** — you regex/TextFSM the output; a formatting change breaks your parser | APIs return **structured JSON/XML** with stable fields |
| **No idempotency** — sending config lines twice can error or duplicate | APIs/model-driven config are **declarative & idempotent** |
| **Prompt & paging fragility** — `--More--`, banners, enable mode, hostname changes | APIs have **no prompt** — it's request/response |
| **No schema / contract** — you guess what output looks like | NETCONF/YANG and RESTCONF have a **formal data model** |
| **Hard to detect partial failure** — did the command really apply? | APIs return **status codes / errors** you can check |
| **Screen-scraping is version-brittle** across IOS releases | Models are **versioned** and vendor-documented |

**The one-liner to remember:** *SSH automation scrapes a human interface; APIs consume a machine
interface. Scraping is fragile because CLI output was designed for people, not programs.*

This is why the curriculum spends **one week** here and then invests heavily in REST (M3),
controller APIs (M4), and NETCONF/YANG (M5).

---

## 8. Common failure modes (you'll diagnose these in S4 — AUTOCOR 3.3)

- **`NetmikoTimeoutException`** — can't reach the device: wrong IP, device down, no route, port 22
  filtered. (TCP-level problem.)
- **`NetmikoAuthenticationException`** — reached the device but username/password rejected.
  (Credentials problem.)
- **Hang / read timeout** — command produced a prompt Netmiko didn't expect (e.g. a `[confirm]`),
  or paging wasn't disabled.
- **Wrong `device_type`** — Netmiko mis-handles prompts/paging for the platform.

**Diagnostic rule of thumb:** *Timeout = network/reachability. Auth exception = credentials.* That
split alone resolves most SSH automation tickets.

---

## 9. Things to remember (quick reference)

- Netmiko sits on Paramiko; you use Netmiko for network gear.
- `send_command` for `show`; `send_config_set` for changes.
- Always close the connection (use `with`).
- Credentials from env vars; `devices.yaml` and `backups/` gitignored.
- Timestamp every backup file.
- One dead device shouldn't abort the whole run — wrap per-device work in try/except.
- The real lesson of the module: **know why we're leaving SSH behind.**
