# Module 1: Python Fundamentals for Network Automation

Welcome to Module 1! This is your foundation for network automation with Python.

## 📖 Overview

This module teaches Python fundamentals through a practical network automation project. You'll learn to parse device configurations, manage inventory data, and generate reports - all essential skills for network automation.

## 🎯 Learning Objectives

By completing this module, you will be able to:
- Use Python data structures (lists, dicts, sets, tuples) effectively
- Parse network device output using regular expressions
- Read and write files in multiple formats (text, JSON, CSV)
- Create reusable functions and classes
- Handle errors gracefully
- Implement logging in automation scripts
- Organize code into modules

## 📁 Module Contents

```
module1_python_basics/
├── README.md                    # This file
├── theory_guide.md              # Comprehensive theory and examples
├── exercises.md                 # Practice exercises with solutions
├── topology.yaml                # CML lab topology specification
├── config_parser.py             # Configuration parsing module
├── inventory_manager.py         # Main project - inventory system
├── requirements.txt             # Python dependencies
├── sample_configs/              # Sample router configurations
│   ├── R1_config.txt
│   └── R2_config.txt
├── sample_outputs/              # Sample CLI outputs for parsing
│   ├── show_version.txt
│   ├── show_ip_interface_brief.txt
│   └── show_ip_route.txt
├── outputs/                     # Generated reports (created by scripts)
└── tests/                       # Unit tests (optional)
```

## 🚀 Getting Started

### Step 1: Read the Theory
Start by reading through `theory_guide.md`. It covers all Python fundamentals you need with network-specific examples.

### Step 2: Set Up the Lab
Deploy the CML topology specified in `topology.yaml`:
- 2 routers (R1 and R2)
- Basic OSPF configuration
- Management access configured

### Step 3: Explore Sample Configurations
Look at the sample configuration files in `sample_configs/`:
- `R1_config.txt` - Router 1 configuration
- `R2_config.txt` - Router 2 configuration

### Step 4: Study the Code
Examine the two main Python files:

1. **config_parser.py** - Core parsing functionality
   - `ConfigParser` class
   - Methods to extract hostnames, interfaces, routing protocols
   - Utility functions for comparison

2. **inventory_manager.py** - Main application
   - `NetworkInventory` class
   - Device management
   - Report generation
   - Multiple export formats

### Step 5: Run the Project
```bash
# Install dependencies (if any)
pip install -r requirements.txt

# Run the config parser examples
python3 config_parser.py

# Run the inventory manager
python3 inventory_manager.py
```

### Step 6: Complete the Exercises
Work through `exercises.md` to practice what you've learned.

## 💻 Project: Network Device Inventory Manager

### Description
Build a Python application that:
- Parses device configuration files
- Extracts structured information (interfaces, IPs, routing)
- Manages a device inventory database
- Generates reports in multiple formats
- Provides search and filtering capabilities

### Features
- ✅ Parse Cisco IOS configurations
- ✅ Extract interfaces with IP addresses
- ✅ Identify routing protocols
- ✅ Generate text reports
- ✅ Export to JSON
- ✅ Export to CSV
- ✅ Search devices by hostname or IP
- ✅ Filter by routing protocol
- ✅ Logging and error handling

### Usage Examples

#### Basic Usage
```python
from inventory_manager import NetworkInventory

# Create inventory
inventory = NetworkInventory()

# Add devices from directory
inventory.add_devices_from_directory('sample_configs')

# List all devices
devices = inventory.list_all_devices()
print(f"Devices: {devices}")

# Generate report
report = inventory.generate_summary_report()
print(report)

# Export to various formats
inventory.export_to_json('my_inventory.json')
inventory.export_to_csv('my_inventory.csv')
```

#### Advanced Usage
```python
# Search by IP
devices = inventory.search_by_ip('10.1.1.1')

# Get devices running OSPF
ospf_devices = inventory.get_devices_by_routing_protocol('ospf')

# Get specific device
device = inventory.get_device_by_hostname('R1')
if device:
    print(f"Device: {device['hostname']}")
    print(f"Version: {device['version']}")
    for intf in device['interfaces']:
        print(f"  {intf['name']}: {intf['ip_address']}")
```

#### Parsing Configuration Files
```python
from config_parser import parse_config_file

# Parse a config file
parser = parse_config_file('sample_configs/R1_config.txt')

# Get structured data
hostname = parser.get_hostname()
interfaces = parser.get_interfaces()
routing = parser.get_routing_protocols()

# Convert to dictionary
config_dict = parser.to_dict()
print(config_dict)
```

## 📊 Expected Outputs

After running the scripts, you'll find these files in `outputs/`:
- `inventory.json` - Complete inventory in JSON format
- `inventory.csv` - Device summary in CSV
- `interfaces.csv` - Detailed interface information
- `inventory_report.txt` - Human-readable text report

## 🎓 Learning Path

### Week 1: Python Basics
- Days 1-2: Data structures (lists, dicts, sets)
- Days 3-4: String manipulation and regex
- Days 5-7: File I/O and practice exercises

### Week 2: Functions and Classes
- Days 1-3: Writing functions, parameters, return values
- Days 4-5: Object-oriented programming basics
- Days 6-7: Error handling and logging

### Week 3: Project Development
- Days 1-2: Build config_parser module
- Days 3-5: Build inventory_manager application
- Days 6-7: Complete exercises and enhancements

## 🔧 Troubleshooting

### Common Issues

**Import Error**: `ModuleNotFoundError: No module named 'config_parser'`
- Solution: Make sure you're in the module1_python_basics directory
- Run: `cd /path/to/module1_python_basics`

**File Not Found**: `Configuration file not found: sample_configs/R1_config.txt`
- Solution: Ensure sample_configs directory exists with config files
- The scripts will create this directory, but you need to add files

**No Devices Added**: Script runs but no devices in inventory
- Solution: Check that config files end in .txt or .cfg
- Verify files contain valid Cisco IOS configurations

### Getting Help

If you're stuck:
1. Review the theory guide for concepts
2. Check the example code in config_parser.py
3. Run scripts with sample data first
4. Try exercises one at a time
5. Experiment in Python interactive mode (ipython)

## 📚 Additional Resources

### Python Documentation
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Python re Module](https://docs.python.org/3/library/re.html)
- [Python json Module](https://docs.python.org/3/library/json.html)
- [Python csv Module](https://docs.python.org/3/library/csv.html)

### Network Automation
- [Cisco IOS Configuration Fundamentals](https://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/ios-software-releases-122-mainline/15061-config-guide.html)
- [Regular Expression Tutorial](https://regexone.com/)
- [Python for Network Engineers](https://pyneng.readthedocs.io/)

### Practice Sites
- [Python Exercises](https://www.w3resource.com/python-exercises/)
- [RegexOne](https://regexone.com/) - Learn regex interactively
- [HackerRank Python](https://www.hackerrank.com/domains/python)

## ✅ Completion Checklist

Before moving to Module 2, ensure you've:

- [ ] Read the complete theory guide
- [ ] Deployed the CML lab topology
- [ ] Run config_parser.py successfully
- [ ] Run inventory_manager.py successfully
- [ ] Understood how ConfigParser class works
- [ ] Understood how NetworkInventory class works
- [ ] Generated reports in all formats
- [ ] Completed at least 5 exercises
- [ ] Experimented with modifying the code
- [ ] Can explain how regex parsing works
- [ ] Comfortable with file I/O operations
- [ ] Understand error handling basics

## 🎯 Challenge Yourself

Ready for more? Try these enhancements:

1. **Add IPv6 Support**: Parse IPv6 addresses from configurations
2. **Config Validation**: Check for security best practices
3. **Topology Discovery**: Map connections between devices
4. **Historical Tracking**: Track configuration changes over time
5. **Web Interface**: Create a simple web UI for the inventory
6. **Database Integration**: Store inventory in SQLite database
7. **Unit Tests**: Write pytest tests for all functions
8. **CLI Tool**: Create command-line tool with argparse

## 🚀 Next Steps

Once you've mastered Module 1, you're ready for:

**Module 2: SSH Automation with Netmiko**
- Connect to real devices via SSH
- Send commands and retrieve output
- Make configuration changes
- Build automated backup systems

---

**Good luck with your Python learning journey!** 🐍

Remember: The best way to learn is by doing. Type the code, experiment, break things, and learn from your mistakes!




