# Module 2 — Exercises (incremental)

You write all the code. The guide gives hints and pseudocode; you type the real solution.
Work these roughly in order — each builds on the last toward the full backup script.

## Warm-up (concepts, no code)
1. In one sentence each, explain the difference between Paramiko and Netmiko, and when you'd use
   `send_command` vs `send_config_set`.
2. Predict: if you `export NET_USER` but forget `NET_PASS`, and your code does
   `os.environ["NET_PASS"]`, what happens at runtime and why? (Hint: `[]` vs `.get()` on a dict.)

## Core build (the project, session by session)
3. **S1 — one device:** connect to a single CML device with `ConnectHandler`, run
   `show version`, and print the output. Use a `with` block so it auto-closes.
4. **S1 — read a secret:** replace the hardcoded username/password with values from
   `os.environ`. Make it fail loudly if a variable is missing.
5. **S2 — inventory:** load `devices.yaml` with `yaml.safe_load`, loop over the devices, and
   run `show running-config` on each.
6. **S2 — timestamped backups:** write each device's config to
   `backups/<hostname>_<YYYYMMDD-HHMMSS>.cfg`. Confirm re-running doesn't overwrite old backups.
7. **S3 — resilience:** wrap per-device work in try/except so one unreachable device doesn't
   abort the run; catch `NetmikoTimeoutException` and `NetmikoAuthenticationException`
   separately and log a clear message for each.
8. **S3 — logging:** add `logging` (file + level) instead of bare `print`; log start, per-device
   success/failure, and finish.

## Stretch (optional)
9. Add a summary at the end: "N devices backed up, M failed" (dict-as-counter pattern from M1).
10. Try `send_command("show ip interface brief", use_textfsm=True)` and inspect the structured
    result — then write two sentences on why that structure is still more fragile than a REST API.
11. Compare backups across two runs with a diff to detect config drift (reuse set/tuple ideas
    from Module 1's OSPF diff).

## Recall
After each session, the coach builds `anki_session<N>.txt` grounded in what you actually did.
