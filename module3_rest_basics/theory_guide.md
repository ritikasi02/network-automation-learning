# Module 3 Theory Guide — REST APIs

Read the section that matches the session you are in. Do not try to memorize this
file. Use it as the concept map; you will *feel* each idea when you write the code.

---

## 1. Same job as Module 2 — different interface

In Module 2 you asked a device: "what do your interfaces look like?" The path was:

```
your Python  --SSH-->  device CLI  --text-->  your script
```

The device answered in **human language** (`show ip int brief` scrolling in a
terminal). You saved that text to a file. If you wanted "only the down
interfaces," you would have had to parse that text with string splits or regex —
the same pain as Module 1.

A **REST API** is the device (or controller, or cloud) exposing a **machine
door** for the same question:

```
your Python  --HTTP-->  API  --JSON-->  your script
```

You still "ask for interface data." You just send an **HTTP request** to a URL
instead of typing a CLI command, and you get **JSON** (structured data) instead
of a paragraph of text.

**Real-world picture:** Catalyst Center, Meraki, CML, AWS, ServiceNow — every
one of them is "a program you talk to over HTTP." Your job as an automation
engineer is to become fluent in that conversation.

**The one-liner:** SSH scrapes a human interface; REST consumes a machine
interface.

---

## 2. HTTP in one mental model

**HTTP (HyperText Transfer Protocol)** is the language browsers and APIs both
use. A web page load *is* HTTP. An API call is the same protocol, aimed at a
machine instead of a human-looking page.

Every HTTP conversation has two halves:

1. **Request** (you send): "I want this thing, this way."
2. **Response** (the server sends back): "Here is the result, and a status
   telling you how it went."

### 2.1 The request has four parts

| Part | What it is | Example |
|---|---|---|
| **URL** | The address of the resource | `https://cml.lab/api/v0/labs` |
| **Method** | The *verb* — what you want to *do* | `GET` (read), `POST` (create/login) |
| **Headers** | Metadata about the request | `Authorization: Bearer <token>` |
| **Body** | Optional payload (usually JSON) | `{"username": "...", "password": "..."}` |

### 2.2 The response has three parts you will use constantly

| Part | What it is | Example |
|---|---|---|
| **Status code** | A number meaning success / fail / auth / missing | `200`, `401`, `404`, `429` |
| **Headers** | Metadata about the response | `Content-Type: application/json` |
| **Body** | The payload — for APIs, almost always JSON | `{"id": "lab-1", "state": "STARTED"}` |

**Rule of thumb:** always look at the **status code first**, then the body.
A body that looks like JSON does not mean the call succeeded — a `401` error
page can still be JSON.

---

## 3. HTTP methods (the verbs)

Think of a **resource** as a noun (a lab, a device, a VLAN). The method is the
verb.

| Method | Meaning | Network example |
|---|---|---|
| **GET** | Read. Must not change state. | Get the list of labs; get interface status |
| **POST** | Create, or trigger an action | Log in (get a token); start a lab |
| **PUT** | Replace the whole resource | Replace an ACL with a full new list |
| **PATCH** | Change part of a resource | Shut one interface |
| **DELETE** | Remove the resource | Delete a lab / a VLAN |

**Rule of thumb:** if you are only *looking*, it should be GET. If a GET
changes something, the API is poorly designed (and you should treat it as
dangerous).

> **Interview Q:** *"Idempotent — what does that mean for HTTP?"*
> **A:** Doing the same request twice has the same effect as doing it once.
> GET, PUT, and DELETE are expected to be idempotent. POST often is not
> (two POSTs can create two labs). This is why retries are safer on GET
> than on POST.

---

## 4. Status codes you must know by heart

Grouped by the first digit:

| Range | Meaning | What you do |
|---|---|---|
| **2xx** | Success | Use the body |
| **3xx** | Redirect | Follow or refuse (APIs rarely need this) |
| **4xx** | **Your** request is wrong | Fix URL, auth, or payload — retrying blindly will not help |
| **5xx** | **Server** failed | Retry with backoff; the API may be overloaded |

Specific codes you will hit in this module:

| Code | Name | Typical cause |
|---|---|---|
| **200** | OK | GET succeeded |
| **201** | Created | POST created a resource |
| **204** | No Content | Success, empty body (common on DELETE) |
| **400** | Bad Request | Your JSON is malformed or a field is missing |
| **401** | Unauthorized | No token, bad token, or expired token |
| **403** | Forbidden | Token is valid but you are not allowed |
| **404** | Not Found | Wrong URL or the lab/device id does not exist |
| **429** | Too Many Requests | You are being **rate limited** — wait and retry |
| **500** | Internal Server Error | Bug or crash on their side |
| **503** | Service Unavailable | Lab/controller is down or restarting |

**Diagnostic split (AUTOCOR 3.3):** *4xx = look at your request. 5xx = look
at the server / retry. 401 vs 403 = "who are you?" vs "you may not do that."*

---

## 5. JSON — the body language of APIs

**JSON (JavaScript Object Notation)** is text that maps almost 1:1 onto Python:

| JSON | Python |
|---|---|
| `{ "hostname": "R1" }` | `dict` — `data["hostname"]` |
| `[1, 2, 3]` | `list` |
| `"STARTED"` | `str` |
| `42` / `true` / `null` | `int` / `True` / `None` |

You already did this in Module 1 (`output.json`, `to_dict()`). An API response
*is* that same idea, arriving over the network instead of from a file.

**Nested JSON** is the normal case. A lab list looks like:

```json
{
  "labs": [
    {"id": "lab-aa11", "title": "Campus Core", "state": "STARTED"},
    {"id": "lab-bb22", "title": "WAN Edge", "state": "STOPPED"}
  ]
}
```

In Python, after `data = response.json()`:

- `data` is a dict
- `data["labs"]` is a list
- `data["labs"][0]` is a dict
- `data["labs"][0]["state"]` is the string `"STARTED"`

**Rule of thumb:** draw the path from the outer key to the field you want
*before* you write the loop. Wrong path → `KeyError` or `TypeError` (list vs
dict). Same bugs you already debugged in Module 1.

`sample_responses/` in this folder is saved JSON that looks like CML. Practice
walking it with no network involved.

---

## 6. The `requests` library

Python's standard library *can* do HTTP (`urllib`), but the industry standard
is **`requests`**. Three methods you will live in:

```python
import requests

response = requests.get(url, timeout=10)
print(response.status_code)   # int, e.g. 200
data = response.json()        # dict or list — ONLY if the body is JSON
```

| Piece | Meaning |
|---|---|
| `requests.get(url)` | Send a GET, get back a `Response` object |
| `response.status_code` | The number from section 4 |
| `response.text` | Body as a raw string (CLI-like; last resort) |
| `response.json()` | Parse body as JSON → dict/list |
| `timeout=10` | Give up after 10 seconds — **always set this** |

**Why timeout is non-negotiable:** without it, a dead server can hang your
script forever. In production that means a stuck automation job. AUTOCOR 1.6
expects you to handle this.

**POST** (you will use this to log in):

```python
response = requests.post(
    url,
    json={"username": user, "password": password},  # requests encodes JSON
    timeout=10,
)
```

`json=...` sets the body *and* the `Content-Type: application/json` header.
Do not build the JSON string yourself.

---

## 7. Authentication — how an API knows who you are

APIs do not let strangers change labs. This section is the concept spine of the
module, so it is longer. Read it before Session 3.

### 7.0 The idea that explains everything: REST is stateless

REST's defining property is **statelessness**: the server does **not** remember
anything about you between requests (AWS, *What is an API?*; and the original
definition in Roy Fielding's REST dissertation, ch. 5). Every request must
carry, by itself, everything the server needs to handle it.

Contrast with Module 2's SSH: there you opened a **session** and logged in
**once**; the device remembered you for the whole conversation because the
open channel *held* your identity. That memory is **state**.

REST throws that away. **Every request is a stranger walking up to the counter.**
That design is why REST scales to millions of clients — but it forces one
consequence:

> Because the server remembers nothing, **you must prove who you are on every
> single request.** That single fact is the reason API keys and tokens both
> ride along on *each* call. Everything below follows from it.

### 7.1 Authentication vs Authorization (do not blur these)

- **Authentication (authN)** — *"Who are you?"* Proving identity (login).
- **Authorization (authZ)** — *"What are you allowed to do?"* Permissions.

Mapped onto status codes you already met:

- **401 Unauthorized** = authN failed — "I don't know who you are" (missing /
  bad / expired credential).
- **403 Forbidden** = authN succeeded, authZ failed — "I know you, and you may
  **not** do this."

> **Interview one-liner:** *401 is "I don't know you"; 403 is "I know you, and no."*

### 7.2 Mechanism A — API key (identifies an *application*)

A single long secret string, issued once, sent in a header on **every** request:

```
X-Cisco-Meraki-API-Key: <the key>
```

Per AWS, an API key *"verifies the program or application making the call"* — it
identifies an **application**, not a person, and there is no login step.

- **Strengths:** dead simple; nothing to refresh; lets the provider monitor
  usage per account.
- **Weaknesses (AWS: "not as secure as tokens"):** the key is **long-lived**
  (often never expires), so a leak = full access until a human revokes it; it is
  **coarse** (usually all-or-nothing); and the real secret travels on **every**
  request.
- **Network example:** Meraki Dashboard API.

### 7.3 Mechanism B — auth token / Bearer (identifies a *user*, the modern default)

Per AWS, tokens *"check that the users are who they claim to be"* and appear when
you *"log in."* Two phases:

**Phase 1 — trade credentials for a token (once):**

```
POST /authenticate
{ "username": "...", "password": "..." }      →   { "token": "eyJ..." }
```

**Phase 2 — send the token on every later request:**

```
GET /api/v0/labs
Authorization: Bearer eyJ...
```

`Bearer` means *"the bearer of this token"* — whoever holds it is treated as you
(see the HTTP `Authorization` header, RFC 7235; Bearer scheme, RFC 6750). That is
why a token is as sensitive as a password.

**Why a token is "more secure" than a key even though both can be stolen —
one word: expiry.**

- Tokens are **short-lived** (Catalyst Center ≈ 60 min). A leaked token is a key
  that self-destructs — blast radius is an hour, not "forever."
- Your **password is exposed only once** (Phase 1); afterward only the disposable
  token rides along. An API key puts the permanent secret on every request.
- Tokens can carry **fine-grained scope** (read vs delete), so authZ can be
  tighter than a blanket key.

The cost is handling expiry. Two strategies:

- **Reactive (default):** use the token until a request returns **401**, then
  log in again and retry that request. Simple; you never refresh early.
- **Proactive:** track issue time and renew shortly before the known limit.

> **Token lifecycle (CML, Catalyst Center, AWS STS — memorize this shape):**
> 1. `POST` credentials → receive token.
> 2. Store the token **in memory / on the client object** — not on disk, not in git.
> 3. Send `Authorization: Bearer <token>` on every request.
> 4. On a sudden **401**, the token expired → log in again → retry.
>
> Reusing one token across many calls (instead of logging in every time) is what
> AUTOCOR 1.6 calls **persistent auth**.

### 7.4 Basic auth (older APIs — know it, don't build on it)

Username + password, Base64-encoded, in the `Authorization` header. `requests`
does it for you with `auth=(user, password)`. Base64 is **encoding, not
encryption** — it protects nothing on its own; it only rides safely because of
HTTPS/TLS. You will see it on legacy gear.

### 7.5 The golden rule for all of them

The secret — API key, password, or token — **never** goes in source code or git.
Environment variable or secrets manager only (same reflex as `NET_PASS` in
Module 2; AUTOCOR 3.6). Source control is treated as public and permanent, and a
leaked credential *is* a leaked identity. Never `print()` a token.

**Sources:** AWS, *What is an API?* (statelessness; auth tokens vs API keys;
401/403 framing echoed in HTTP); Roy Fielding, REST dissertation ch. 5
(statelessness constraint); MDN Web Docs, *HTTP authentication* and *HTTP
response status codes*; RFC 7235 (`Authorization` header), RFC 6750 (Bearer
tokens).

---

## 8. The reusable client (the Module 3 project shape)

A one-off script that copies `requests.get(...)` ten times will rot. The
professional pattern — and what Module 4 will need — is a **class** that owns:

- the **base URL** (`https://cml.example.com`)
- a **`requests.Session`** (keeps headers/cookies; connection reuse)
- the **token** after login
- helpers: `_url(path)`, `_headers()`, `_raise_for_status()`

Sketch (you will write the real one — this is the shape, not the solution):

```
CmlClient
  __init__(base_url, username, password)
  login()            -> store token
  get_labs()         -> GET /api/v0/labs
  get_nodes(lab_id)  -> GET /api/v0/labs/{id}/nodes
```

**Why a class?** Same reason as `ConfigAnalyzer` in Module 1: the token and
base URL are *state* that many methods share. `self.token` is the sticky note
every method can read.

`requests.Session` vs bare `requests.get`: a Session lets you set
`Authorization` **once** and have every call carry it. That is persistent
auth in one object.

---

## 9. Failure modes you must handle (AUTOCOR 1.6 + 3.3)

| Symptom | Likely cause | What the code should do |
|---|---|---|
| `requests.exceptions.Timeout` | Server slow or unreachable | Log; skip or retry that call |
| `requests.exceptions.ConnectionError` | DNS, network, TLS, host down | Same — do not crash the whole run |
| `401` after it used to work | Token expired | Re-login, retry **once** |
| `404` | Bad id or typo in the path | Fail that item; continue others |
| `429` | Rate limit | Wait (`Retry-After` header if present), then retry |
| `5xx` | Their side | Retry with **exponential backoff** (1s, 2s, 4s…) |

**Exponential backoff:** wait 1 second, retry; if it fails, wait 2; then 4.
Do not hammer a sick API. Real controllers (Catalyst Center) will 429 you
if you poll too hard.

**Pagination:** large inventories do not come in one response. The API
returns a *page* plus a "next" link or offset. You loop until there is no
next page. Small CML labs may fit in one page — you still write the loop
so the pattern is in your muscle memory (AUTOCOR 1.6).

---

## 10. CML REST API — the target (from Session 3)

CML (Cisco Modeling Labs) is itself a web app. The GUI you click is just a
client of the **same REST API** you will call.

Typical flow (paths can vary slightly by CML version — we will confirm live):

1. `POST /api/v0/authenticate` with username/password → token
2. `GET /api/v0/labs` → list of lab ids
3. `GET /api/v0/labs/{lab_id}` → lab details
4. `GET /api/v0/labs/{lab_id}/nodes` → nodes (routers, switches)
5. `GET /api/v0/labs/{lab_id}/topology` → nodes + links together

**Real-world use:** spin up a lab overnight, check which nodes booted, collect
management IPs, feed those IPs into later automation. AUTOCOR 2.2 tests
exactly this idea (automate CML via REST / PyCML). We will use raw `requests`
first so you understand the HTTP; PyCML is a wrapper we can mention later.

If CML is unreachable, we will use a Cisco DevNet sandbox with the same
ideas (login → token → GET resources). The **client class** stays the same;
only `base_url` changes.

---

## 11. Flask (week 3 — skip until then)

**Flask** is a tiny Python web framework. Your script becomes a **server**:
a browser hits `http://127.0.0.1:5000/`, Flask runs your Python, your Python
calls CML, Flask returns HTML.

Mental model:

```
Browser  --GET /-->  Flask  --GET /api/v0/labs-->  CML
Browser  <--HTML--  Flask  <--JSON labs----------  CML
```

You do not need Flask to *learn* REST. We add it so you can *show* the data —
useful in pre-sales and interviews.

---

## 12. Things to remember

- HTTP = request (method + URL + headers + body) and response (status + body).
- Status first, then body. 4xx is you; 5xx is them; 401 vs 403 are different.
- JSON ↔ Python dict/list. Walk keys one level at a time.
- Always set `timeout=` on `requests` calls.
- Tokens live on the client object, not in git. Refresh on 401.
- A reusable client class is the deliverable that Module 4 will reuse.
- Pagination, 429, retries = AUTOCOR 1.6 — we will write them even on a small lab.

> **Interview Q:** *"REST vs SSH for network automation — when would you still
> use SSH?"*
> **A:** When the device has no API, or you need a show command the API does
> not expose. Default to API when it exists. Never prefer screen-scraping
> for inventory/compliance if a controller API (Catalyst Center, Meraki)
> already has the structured data.
