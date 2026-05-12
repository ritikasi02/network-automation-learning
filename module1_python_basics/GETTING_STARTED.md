# Module 1: Getting Started - Build a Network Config Analyzer

You will learn Python by building a real tool. Not by reading theory first. Open Cursor, open this file, and start your first session.

---

## Your Project: Network Config Analyzer

A command-line tool that reads Cisco IOS configuration files, extracts key data, and generates reports. You will build this from an empty file, adding features session by session. Every feature teaches you a new Python concept.

**By the end of Module 1, your tool will:**
- Read Cisco IOS config files from a directory
- Extract hostnames, interfaces, IP addresses, routing protocols, VLANs
- Detect issues (duplicate IPs, shutdown interfaces, missing descriptions)
- Export data to JSON and CSV
- Handle errors gracefully
- Log its operations

---

## Session 1: Your First Python Script (20-30 minutes)

**Goal:** Read a config file and print the hostname.

**What you will learn:** variables, strings, `open()`, `for` loops, `if` statements.

### Step 1: Create your project file

```bash
cd ~/pyme/network_automation_learning/module1_python_basics
touch config_analyzer.py
```

This is YOUR file. You will build it from scratch across all sessions. The existing `config_parser.py` and `inventory_manager.py` are reference samples. Do not copy them.

### Step 2: Write your first code

Open `config_analyzer.py` in Cursor and write this:

```python
config_file = "sample_configs/R1_config.txt"

with open(config_file, "r") as f:
    for line in f:
        if line.strip().startswith("hostname"):
            hostname = line.strip().split()[1]
            print(f"Found hostname: {hostname}")
```

Run it:

```bash
python3 config_analyzer.py
```

You should see: `Found hostname: R1`

### Step 3: Understand what you wrote

Ask Cursor AI: "Explain each line of this code to me like I have never programmed before."

Key concepts you just used:
- **Variable:** `config_file` stores the file path
- **`with open()`:** Opens a file safely (closes it automatically when done)
- **`for line in f`:** Loops through each line in the file
- **`.strip()`:** Removes whitespace from the beginning and end of a string
- **`.startswith()`:** Checks if a string starts with specific text
- **`.split()`:** Breaks a string into a list of words
- **`f"..."`:** An f-string that lets you put variables inside text

### Step 4: Commit your work

```bash
cd ~/pyme/network_automation_learning
git add -A
git commit -m "module1: create config analyzer, extract hostname from config file"
git push
```

You just completed your first session. You wrote Python, ran it, and committed it.

---

## Session 2: Extract Interfaces (20-30 minutes)

**Goal:** Find all interfaces and their IP addresses.

**What you will learn:** lists, dictionaries, more string methods.

### Step 1: Add interface extraction to your script

Add this below your hostname code:

```python
interfaces = []

with open(config_file, "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.strip().startswith("interface "):
        interface_name = line.strip().replace("interface ", "")
        ip_address = "none"

        for j in range(i + 1, min(i + 10, len(lines))):
            if "ip address" in lines[j]:
                parts = lines[j].strip().split()
                ip_address = parts[2]
                break
            if lines[j].strip().startswith("interface ") or lines[j].strip() == "!":
                break

        interfaces.append({"name": interface_name, "ip": ip_address})

print(f"\nFound {len(interfaces)} interfaces:")
for intf in interfaces:
    print(f"  {intf['name']}: {intf['ip']}")
```

Run it and check the output.

### Step 2: Understand the new concepts

- **List:** `interfaces = []` creates an empty list you add items to
- **Dictionary:** `{"name": ..., "ip": ...}` stores key-value pairs for each interface
- **`enumerate()`:** Gives you both the line number and the line content
- **`.append()`:** Adds an item to the end of a list
- **`range()`:** Creates a sequence of numbers for looping

### Step 3: Commit

```bash
git add -A
git commit -m "module1: add interface and IP address extraction"
git push
```

---

## Session 3: Turn It Into a Function (20-30 minutes)

**Goal:** Organize your code into reusable functions.

**What you will learn:** functions, parameters, return values.

Refactor your code so it looks like this:

```python
def get_hostname(lines):
    for line in lines:
        if line.strip().startswith("hostname"):
            return line.strip().split()[1]
    return "unknown"

def get_interfaces(lines):
    interfaces = []
    for i, line in enumerate(lines):
        if line.strip().startswith("interface "):
            interface_name = line.strip().replace("interface ", "")
            ip_address = "none"
            for j in range(i + 1, min(i + 10, len(lines))):
                if "ip address" in lines[j]:
                    parts = lines[j].strip().split()
                    ip_address = parts[2]
                    break
                if lines[j].strip().startswith("interface ") or lines[j].strip() == "!":
                    break
            interfaces.append({"name": interface_name, "ip": ip_address})
    return interfaces

def read_config(filepath):
    with open(filepath, "r") as f:
        return f.readlines()

if __name__ == "__main__":
    lines = read_config("sample_configs/R1_config.txt")
    hostname = get_hostname(lines)
    interfaces = get_interfaces(lines)

    print(f"Device: {hostname}")
    print(f"Interfaces: {len(interfaces)}")
    for intf in interfaces:
        print(f"  {intf['name']}: {intf['ip']}")
```

Commit:

```bash
git add -A
git commit -m "module1: refactor into functions for hostname and interface parsing"
git push
```

---

## Session 4: Parse Both Config Files (20-30 minutes)

**Goal:** Process multiple config files and compare results.

**What you will learn:** `os` module, loops over files, printing formatted output.

Add code to parse both R1 and R2 configs and print a summary table. This is a good time to update your README:

```bash
git add -A
git commit -m "module1: parse multiple config files, add summary output"
git push
```

---

## What Comes Next

After Session 4, continue adding features to your config analyzer:

| Session | Feature | Python Concept |
|---------|---------|----------------|
| 5-6 | Add regex for parsing OSPF, BGP config | `re` module, regex patterns |
| 7-8 | Export data to JSON file | `json` module, file writing |
| 9-10 | Export data to CSV file | `csv` module |
| 11-12 | Detect duplicate IPs across devices | sets, nested loops |
| 13-14 | Add a `ConfigAnalyzer` class | classes, `__init__`, methods |
| 15-16 | Add error handling for missing files | try/except, exceptions |
| 17-18 | Add logging | `logging` module |
| 19-20 | Write the README, clean up code | documentation skills |

Each pair of sessions follows the same pattern:
1. First session: Build the feature
2. Second session: Improve it, handle edge cases, commit

---

## Reference Materials

When you get stuck or need to learn a concept:

- **theory_guide.md** - Look up the specific topic you need. Do not read cover to cover.
- **exercises.md** - Extra practice after you have built the feature in your project.
- **config_parser.py** - Study this for ideas, but build your own version differently.
- **Ask Cursor AI** - "How do I [specific thing] in Python?" is always a good question.

---

## Rules for Module 1

1. **Build first, read theory second.** Only look up concepts when you need them for your project.
2. **Type the code yourself.** Do not copy-paste from the sample files.
3. **Commit every session.** Your commit history is proof of your learning.
4. **It is okay to write ugly code first.** You will refactor it later. Working code beats perfect code.
5. **If you are stuck for more than 5 minutes,** ask Cursor AI or simplify the problem.
6. **Your config_analyzer.py is YOUR code.** It should look different from the sample files.

---

**You are ready. Open Cursor, create `config_analyzer.py`, and start Session 1.**
