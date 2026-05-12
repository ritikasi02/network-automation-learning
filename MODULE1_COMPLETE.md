# Module 1: Python Fundamentals - Status

**Status:** INCOMPLETE - Materials created, independent learning not yet started
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

- [ ] You have built a config analyzer from scratch (not copied the sample code)
- [ ] You can explain every line of code you wrote
- [ ] Your project reads config files and extracts: hostname, interfaces, IPs, routing protocols
- [ ] Your project exports data to at least 2 formats (JSON + one other)
- [ ] Your project handles errors gracefully (missing files, bad input)
- [ ] Your project has logging
- [ ] Your project is on GitHub with a clear README
- [ ] You have 15+ commits showing your building process
- [ ] You can answer: "What does this line do?" for any line in your code

---

**Start building:** [Module 1 Getting Started](module1_python_basics/GETTING_STARTED.md)
**Main curriculum:** [README.md](README.md)
