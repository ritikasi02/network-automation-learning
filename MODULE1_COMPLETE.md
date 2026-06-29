# Module 1: Python Fundamentals - Status

**Status:** IN PROGRESS (~65%) - 11 sessions complete; several concept gaps remain (see "concepts still to cover" below)
**Last Updated:** June 20, 2026
**Estimated Duration:** 6-8 weeks at 20-30 min/day, 4 days/week

---

## What Exists

Learning materials (theory guide, exercises, sample code, sample configs) were generated as reference material. These are resources to consult when building the project, not the project itself.

| Item | Status |
|------|--------|
| theory_guide.md | Reference material (consult as needed) |
| exercises.md | Practice problems (do after building project) |
| config_parser.py | Sample code (study for ideas, build your own) |
| inventory_manager.py | Sample code (study for ideas, build your own) |
| Sample configs (R1, R2) | Ready to use as test data |
| Sample CLI outputs | Ready to use as test data |

## What Needs to Happen

The goal is NOT to read the theory guide cover to cover. The goal is to build a **Network Config Analyzer** project from scratch, learning Python concepts as you need them.

### Project-Driven Learning Path

**Week 1-2: Read a file and extract data**
- Learn: variables, strings, `open()`, `for` loops
- Build: a script that reads `R1_config.txt` and prints the hostname

**Week 2-3: Work with structured data**
- Learn: lists, dictionaries, f-strings
- Build: a function that returns all interfaces as a list of dictionaries

**Week 3-4: Parse unstructured text**
- Learn: `re` module, regex patterns
- Build: regex patterns to extract IPs, subnet masks, OSPF config

**Week 4-5: Write output files**
- Learn: JSON, CSV, file writing
- Build: export parsed data to JSON and CSV reports

**Week 5-6: Organize code with functions and classes**
- Learn: functions, classes, `__init__`, methods
- Build: a `ConfigAnalyzer` class that encapsulates all parsing logic

**Week 6-7: Make it robust**
- Learn: try/except, logging, edge cases
- Build: error handling for missing files, bad data, unexpected formats

**Week 7-8: Polish and document**
- Learn: README writing, code cleanup
- Build: a professional README, clean up code, add comments where needed

### How to Use the Existing Materials

- **theory_guide.md**: Look up specific topics when you need them. Do NOT read it cover to cover before coding.
- **exercises.md**: Do these AFTER you have built part of the project, as reinforcement.
- **config_parser.py**: Study this to understand one approach, then build your own version differently.
- **inventory_manager.py**: Same as above. Build your own, do not copy this.
- **sample_configs/**: Use these as your test data. Parse these files with your code.

## Completion Criteria

You are done with Module 1 when:

- [x] You have built a config analyzer from scratch (not copied the sample code)
- [x] You can explain every line of code you wrote
- [x] Your project reads config files and extracts: hostname, interfaces, IPs, routing protocols
- [ ] Your project exports data to at least 2 formats (JSON + one other) — **only JSON done; CSV pending (Session 12)**
- [x] Your project handles errors gracefully (missing files, bad input)
- [x] Your project has logging
- [ ] Your project is on GitHub with a clear README — **needs a project-specific README (Session 13)**
- [x] You have 15+ commits showing your building process
- [x] You can answer: "What does this line do?" for any line in your code

### Python concepts from the theory guide still to cover

**Tier 1 — required:**
- [ ] **Sets** — not covered at all (no usage, no recall deck)
- [ ] **Tuples** — only incidental so far (`enumerate`, `parametrize`); needs a focused lesson on immutability + multi-return
- [ ] **CSV export** — only JSON export exists
- [ ] **Organize code into modules** — project is still a single file; only the test imports across files
- [x] **Virtual environment / dependency management** — confirmed: uses an activated project venv (theory §1.2)

**Tier 2 — strongly recommended (in theory guide):**
- [ ] **Parsing `show` command output** — `sample_outputs/` (show version, show ip interface brief, show ip route) is never parsed; needs `re.findall`/`finditer` + named groups
- [ ] **List/dict comprehensions** — currently explicit `.append()` loops only
- [ ] **Function depth** (default args, `*args`/`**kwargs`, returning tuples) and **class depth** (inheritance, `__str__`/`__repr__`)

**Tier 3 — optional/advanced:** advanced logging (multi-handler, `RotatingFileHandler`), custom exceptions/`finally`, decorators, PEP 8 + docstrings polish.

**Remaining: ~5-6 sessions** — S12 (CSV), S13 (sets & tuples via config comparison), S14 (parse show-output + comprehensions), S15 (split into modules), S16 (cleanup + project README + push); optional stretch session.

---

**Start building:** [Module 1 Getting Started](module1_python_basics/GETTING_STARTED.md)
**Main curriculum:** [README.md](README.md)
