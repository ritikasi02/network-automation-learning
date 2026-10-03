# Module 3 — Exercises (incremental)

You write all the code. Hints and shape only — type the real solution yourself.
Work roughly in order.

## Warm-up (concepts, no code) — Session 1

1. In Module 2 your script sent `show ip int brief` and got a blob of text. If
   the same device exposed a REST API that returned interface data as JSON,
   what would change about (a) how you *ask* for the data, and (b) how you
   would print only the interfaces that are down?
2. A call returns status `200` with a JSON body. Another returns status `401`
   with a JSON body that says `{"error": "unauthorized"}`. Both bodies are
   valid JSON. Which one do you treat as success, and what do you look at
   *first* to decide?

## Core build

3. **S1 — first GET:** create `first_call.py`. Use `requests.get` against
   `https://jsonplaceholder.typicode.com/users` with `timeout=10`. Print
   `status_code` and then `response.json()`. Confirm you see a Python list
   of dicts, not a string.
4. **S1 — walk one record:** from that list, print each user's `name` and
   `address.city` (nested dict). If you get `TypeError` or `KeyError`, draw
   the path before you change code.
5. **S2 — write a report:** save a trimmed list (`id`, `name`, `city`) to
   `outputs/users_report.json` using `json.dump`. Same idea as Module 1's
   `output.json`.
6. **S2 — local JSON (no network):** load `sample_responses/labs.json` and
   print only labs whose `state` is `STARTED`.
7. **S3 — authenticate:** POST to the CML (or sandbox) login URL using
   credentials from `os.environ` / `.env`. Print only "login ok" / "login
   failed" — never print the token.
8. **S3 — use the token:** GET the labs list with
   `headers={"Authorization": "Bearer " + token}`. Print lab titles/ids.
9. **S4 — class:** move login + get_labs into a `CmlClient` class. `self`
   holds `base_url` and `token`. Call it from `if __name__ == "__main__"`.
10. **S5 — more resources + errors:** add `get_nodes(lab_id)`. Catch
    `Timeout` and `ConnectionError`. If status is 401/404/429, print a
    specific message (do not use a bare `except:`).
11. **S6 — pagination / 429 pattern:** write a helper that follows a
    `next` link (or loops pages) and a retry-on-429 with a sleep. Test
    the *logic* even if the live API fits in one page.
12. **S7–S8 — Flask:** a single page that lists labs and node states by
    calling your client.

## Stretch

13. Compare: Module 2 backup (SSH text file) vs Module 3 labs JSON. Write
    four bullet points in your project README on why the JSON path is
    easier to query and safer to retry.
14. Add `logging` (from Module 1) — log method, URL, status. Never log
    tokens or passwords (AUTOCOR 3.6).

## Recall

After each session the coach builds `anki_session<N>.txt` from what you
actually did.
