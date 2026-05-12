# Module 1: Python Fundamentals - Practice Exercises

These exercises will help you practice and reinforce the concepts learned in Module 1. Work through them at your own pace, and don't hesitate to experiment!

## 📝 Exercise Guidelines

- Try to solve each exercise on your own first
- Use the theory guide and examples as reference
- Test your solutions with different inputs
- Solutions are provided at the end, but try not to peek!
- Modify the exercises to make them more challenging

---

## Exercise 1: Data Structures Basics

### Part A: Device Lists
Write Python code to:
1. Create a list of 5 network devices (routers and switches)
2. Add 2 more devices to the list
3. Sort the devices alphabetically
4. Print only the routers (devices containing 'Router')
5. Remove all switches from the list

### Part B: Device Dictionary
Create a dictionary for a network device with the following information:
- Hostname
- IP address
- Device type (router/switch)
- Number of interfaces
- Location

Then:
1. Add a new key 'serial_number' with a value
2. Update the location
3. Print all keys and values
4. Check if 'mgmt_ip' key exists

### Part C: VLAN Set Operations
Given two switches with these VLANs:
- Switch1: 10, 20, 30, 40, 50
- Switch2: 30, 40, 50, 60, 70

Use set operations to find:
1. VLANs common to both switches
2. VLANs only on Switch1
3. VLANs only on Switch2
4. All unique VLANs across both switches

**Expected Output:**
```
Common VLANs: {30, 40, 50}
Switch1 only: {10, 20}
Switch2 only: {60, 70}
All VLANs: {10, 20, 30, 40, 50, 60, 70}
```

---

## Exercise 2: String Manipulation

### Part A: Configuration Parsing
Given this interface configuration:
```
interface GigabitEthernet0/0
 description WAN Link to Branch Office
 ip address 10.1.1.1 255.255.255.0
 duplex auto
 speed auto
 no shutdown
```

Write code to:
1. Extract the interface name
2. Extract the description
3. Extract the IP address and subnet mask
4. Determine if the interface is shutdown

### Part B: Hostname Formatting
Write a function that:
- Takes a hostname as input
- Converts it to uppercase
- Removes any spaces
- Adds a prefix "RTR-" or "SW-" based on device type
- Returns the formatted hostname

Example:
```python
format_hostname("router 1", "router")  # Returns: "RTR-ROUTER1"
format_hostname("switch 2", "switch")  # Returns: "SW-SWITCH2"
```

### Part C: Configuration Template
Create a function that generates interface configurations using f-strings:
```python
def generate_interface_config(interface_name, ip_address, subnet_mask, description):
    # Your code here
    pass
```

Expected output:
```
interface GigabitEthernet0/0
 description Management Interface
 ip address 192.168.1.1 255.255.255.0
 no shutdown
```

---

## Exercise 3: Regular Expressions

### Part A: IP Address Extraction
Write regex patterns to extract:
1. All IP addresses from a configuration file
2. Only private IP addresses (10.x.x.x, 172.16-31.x.x, 192.168.x.x)
3. IP addresses with their subnet masks (e.g., "10.1.1.1 255.255.255.0")

Test with this text:
```
interface Gi0/0
 ip address 10.1.1.1 255.255.255.0
interface Gi0/1
 ip address 8.8.8.8 255.255.255.0
interface Gi0/2
 ip address 192.168.1.1 255.255.255.252
```

### Part B: Interface Parsing
Write a function that uses regex to parse this "show ip interface brief" output:

```
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0     10.1.1.1        YES NVRAM  up                    up
GigabitEthernet0/1     192.168.1.1     YES NVRAM  up                    up
GigabitEthernet0/2     unassigned      YES NVRAM  administratively down down
GigabitEthernet0/3     unassigned      YES NVRAM  administratively down down
```

Return a list of dictionaries with interface name, IP, and status.

### Part C: MAC Address Validation
Write a function that:
- Takes a MAC address as input
- Validates it's in correct format (xxxx.xxxx.xxxx)
- Returns True if valid, False otherwise

Test cases:
```python
is_valid_mac("0011.2233.4455")  # True
is_valid_mac("00:11:22:33:44:55")  # False (wrong format)
is_valid_mac("001122334455")  # False (no dots)
is_valid_mac("xyz.abc.def")  # False (not hex)
```

---

## Exercise 4: File Operations

### Part A: Configuration File Reader
Write a function that:
1. Reads a router configuration file
2. Extracts all interface configurations
3. Saves each interface config to a separate file

Example:
- Input: `router_config.txt`
- Output: `interface_gi0_0.txt`, `interface_gi0_1.txt`, etc.

### Part B: Configuration Backup
Create a script that:
1. Reads multiple configuration files from a directory
2. Creates a backup directory with timestamp
3. Copies all configs to the backup directory
4. Generates a backup summary file with date and file count

### Part C: Configuration Comparison
Write a function that:
- Reads two configuration files
- Compares them line by line
- Returns a list of differences
- Saves differences to a report file

---

## Exercise 5: Functions

### Part A: IP Subnet Calculator
Write functions to:
```python
def ip_to_binary(ip_address):
    """Convert IP address to binary"""
    pass

def calculate_network_address(ip, subnet_mask):
    """Calculate network address from IP and mask"""
    pass

def calculate_broadcast_address(ip, subnet_mask):
    """Calculate broadcast address"""
    pass

def calculate_usable_hosts(subnet_mask):
    """Calculate number of usable host addresses"""
    pass
```

### Part B: Interface Name Parser
Write a function that:
- Takes an interface name (any format)
- Returns a dictionary with type, module, and port
- Handles: GigabitEthernet, FastEthernet, Ethernet, Loopback, etc.

Example:
```python
parse_interface("GigabitEthernet0/0/1")
# Returns: {'type': 'GigabitEthernet', 'module': '0/0', 'port': '1'}

parse_interface("Loopback0")
# Returns: {'type': 'Loopback', 'module': None, 'port': '0'}
```

### Part C: Configuration Validator
Write functions to validate:
```python
def validate_hostname(hostname):
    """Ensure hostname follows naming rules"""
    # No spaces, special chars, starts with letter
    pass

def validate_ip_address(ip):
    """Validate IP address format and ranges"""
    # Check octets are 0-255
    pass

def validate_subnet_mask(mask):
    """Validate subnet mask"""
    # Check it's a valid subnet mask
    pass

def validate_vlan_id(vlan):
    """Validate VLAN ID range"""
    # Check 1-4094, excluding reserved
    pass
```

---

## Exercise 6: Classes

### Part A: Interface Class
Create an `Interface` class with:
- Properties: name, ip_address, subnet_mask, description, status
- Methods: 
  - `is_up()`: returns True if status is 'up'
  - `get_network()`: calculates and returns network address
  - `__str__()`: returns formatted string representation

### Part B: Switch Class
Create a `Switch` class with:
- Properties: hostname, mgmt_ip, vlans (list), interfaces (list)
- Methods:
  - `add_vlan(vlan_id, name)`: add a VLAN
  - `remove_vlan(vlan_id)`: remove a VLAN
  - `get_vlan_count()`: return number of VLANs
  - `add_interface(interface)`: add an Interface object
  - `get_trunk_ports()`: return interfaces with multiple VLANs

### Part C: Device Inventory Class
Extend the NetworkInventory class from the main project to add:
- Method to find devices by model
- Method to generate a topology map (which devices connect to which)
- Method to calculate total interface count by type
- Method to export to XML format

---

## Exercise 7: Error Handling

### Part A: Safe File Reader
Write a function that safely reads a configuration file:
```python
def safe_read_config(filename):
    """
    Safely read config file with comprehensive error handling
    Handle: FileNotFoundError, PermissionError, empty files
    Return: (success: bool, content: str, error_msg: str)
    """
    pass
```

### Part B: IP Address Parser with Validation
Create a function that:
- Parses IP address from a string
- Validates each octet is 0-255
- Raises custom exception for invalid IPs
- Handles various input formats

```python
class InvalidIPError(Exception):
    pass

def parse_and_validate_ip(ip_string):
    """Parse and validate IP address"""
    # Raise InvalidIPError if invalid
    pass
```

### Part C: Configuration Applier
Write a function that:
```python
def apply_config_safely(device, commands):
    """
    Apply configuration commands with rollback on error
    - Try each command
    - If any fails, rollback previous commands
    - Log all actions
    - Return success status and applied commands
    """
    pass
```

---

## Exercise 8: Logging

### Part A: Multi-Level Logger
Create a logging configuration that:
- Logs DEBUG and above to file
- Logs WARNING and above to console
- Uses custom format with timestamp, level, function name
- Rotates log files when they reach 1MB

### Part B: Audit Trail Logger
Create a function that logs all inventory changes:
```python
def log_inventory_change(action, device, details):
    """
    Log inventory changes with detailed information
    action: 'ADD', 'UPDATE', 'DELETE'
    device: device hostname
    details: dictionary of what changed
    """
    pass
```

### Part C: Performance Logger
Create a decorator that:
- Logs function execution time
- Logs function parameters
- Logs return value (or error)

```python
def log_performance(func):
    """Decorator to log function performance"""
    pass

@log_performance
def parse_large_config(filename):
    # Your code
    pass
```

---

## Exercise 9: Integration Challenge

Build a complete script that:

1. **Reads** all configuration files from a directory
2. **Parses** each configuration and extracts:
   - Hostname, version, interfaces, routing protocols
3. **Validates** the data:
   - Check for duplicate IPs
   - Identify shutdown interfaces
   - Find devices without routing protocols
4. **Reports** issues found:
   - Generate summary report
   - Create detailed CSV of all issues
   - Log warnings for problematic configurations
5. **Exports** the inventory:
   - JSON format with all data
   - CSV summary
   - HTML dashboard (bonus!)

---

## Exercise 10: Advanced Challenge

Create a **Network Configuration Analyzer** that:

### Requirements:
1. Parse multiple device configurations
2. Build a network topology map
3. Identify potential issues:
   - Duplicate IP addresses
   - Inconsistent OSPF areas
   - Unused interfaces
   - Missing descriptions
   - Security issues (no passwords, old IOS versions)
4. Generate recommendations for improvements
5. Create visual report with statistics
6. Export findings in multiple formats

### Bonus Features:
- Compare current config with "golden config" template
- Suggest configuration optimizations
- Calculate network utilization
- Identify single points of failure

---

## Solutions

<details>
<summary>Click to reveal Exercise 1 solutions</summary>

### Exercise 1 Solutions

#### Part A: Device Lists
```python
# 1. Create list
devices = ['Router1', 'Switch1', 'Router2', 'Switch2', 'Router3']

# 2. Add devices
devices.append('Router4')
devices.append('Switch3')

# 3. Sort alphabetically
devices.sort()
print(f"Sorted: {devices}")

# 4. Print only routers
routers = [d for d in devices if 'Router' in d]
print(f"Routers: {routers}")

# 5. Remove switches
devices = [d for d in devices if 'Switch' not in d]
print(f"After removing switches: {devices}")
```

#### Part B: Device Dictionary
```python
device = {
    'hostname': 'R1',
    'ip_address': '10.1.1.1',
    'device_type': 'router',
    'interfaces': 4,
    'location': 'HQ'
}

# Add serial number
device['serial_number'] = 'FDO12345678'

# Update location
device['location'] = 'Data Center'

# Print all keys and values
for key, value in device.items():
    print(f"{key}: {value}")

# Check for key
if 'mgmt_ip' in device:
    print("Has mgmt_ip")
else:
    print("No mgmt_ip key")
```

#### Part C: VLAN Set Operations
```python
switch1_vlans = {10, 20, 30, 40, 50}
switch2_vlans = {30, 40, 50, 60, 70}

common = switch1_vlans & switch2_vlans
switch1_only = switch1_vlans - switch2_vlans
switch2_only = switch2_vlans - switch1_vlans
all_vlans = switch1_vlans | switch2_vlans

print(f"Common VLANs: {common}")
print(f"Switch1 only: {switch1_only}")
print(f"Switch2 only: {switch2_only}")
print(f"All VLANs: {all_vlans}")
```

</details>

<details>
<summary>Click to reveal Exercise 2 solutions</summary>

### Exercise 2 Solutions

#### Part A: Configuration Parsing
```python
config = """interface GigabitEthernet0/0
 description WAN Link to Branch Office
 ip address 10.1.1.1 255.255.255.0
 duplex auto
 speed auto
 no shutdown"""

import re

# Extract interface name
intf_match = re.search(r'interface (\S+)', config)
interface_name = intf_match.group(1) if intf_match else None

# Extract description
desc_match = re.search(r'description (.+)', config)
description = desc_match.group(1) if desc_match else None

# Extract IP and mask
ip_match = re.search(r'ip address (\S+) (\S+)', config)
if ip_match:
    ip_address = ip_match.group(1)
    subnet_mask = ip_match.group(2)

# Check if shutdown
is_shutdown = 'shutdown' in config and 'no shutdown' not in config

print(f"Interface: {interface_name}")
print(f"Description: {description}")
print(f"IP: {ip_address}/{subnet_mask}")
print(f"Shutdown: {is_shutdown}")
```

#### Part B: Hostname Formatting
```python
def format_hostname(hostname, device_type):
    # Remove spaces and convert to uppercase
    clean_name = hostname.replace(' ', '').upper()
    
    # Add prefix based on type
    prefix = "RTR-" if device_type.lower() == "router" else "SW-"
    
    return prefix + clean_name

# Test
print(format_hostname("router 1", "router"))  # RTR-ROUTER1
print(format_hostname("switch 2", "switch"))  # SW-SWITCH2
```

#### Part C: Configuration Template
```python
def generate_interface_config(interface_name, ip_address, subnet_mask, description):
    config = f"""interface {interface_name}
 description {description}
 ip address {ip_address} {subnet_mask}
 no shutdown"""
    return config

# Test
print(generate_interface_config("GigabitEthernet0/0", "192.168.1.1", "255.255.255.0", "Management Interface"))
```

</details>

---

## 📚 Additional Practice

Want more practice? Try these:

1. **Extend the inventory manager**: Add features like device grouping, location-based filtering, or compliance checking
2. **Create a config generator**: Build templates for common configurations
3. **Build a diff tool**: Compare configurations and highlight differences
4. **Network calculator**: Create subnet calculator with CIDR support
5. **Topology mapper**: Parse configs and create a visual network map

---

## 🎯 Self-Assessment

Before moving to Module 2, ensure you can:

- [ ] Confidently use lists, dictionaries, sets, and tuples
- [ ] Parse strings with regular expressions
- [ ] Read from and write to files in various formats
- [ ] Create reusable functions with appropriate parameters
- [ ] Design and implement classes with methods
- [ ] Handle errors gracefully with try-except
- [ ] Implement logging in your scripts
- [ ] Organize code into modules

If you're comfortable with all of these, you're ready for Module 2: SSH Automation with Netmiko!

---

**Remember**: The key to mastering Python is practice. Work through these exercises, experiment with the code, and don't be afraid to make mistakes!




