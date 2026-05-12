# Module 1: Python Fundamentals for Network Automation

## 🎯 Learning Objectives

By the end of this module, you will be able to:
- Use Python data structures effectively for network data
- Parse CLI output using regular expressions
- Read and write configuration files
- Create reusable functions and classes
- Handle errors gracefully in automation scripts
- Manage dependencies with virtual environments
- Apply logging best practices

## 📚 Prerequisites

- Python 3.8+ installed on your system
- Basic understanding of networking concepts (IPs, VLANs, routing)
- Text editor or IDE (VS Code recommended)
- Terminal/command line familiarity

## 1. Python Basics for Network Automation

### 1.1 Why Python for Network Automation?

Python is the de facto language for network automation because:
- **Readable syntax**: Easy to learn and maintain
- **Rich ecosystem**: Libraries for SSH (Netmiko), APIs (requests), NETCONF (ncclient)
- **Community support**: Large network automation community
- **Cross-platform**: Works on Windows, Mac, Linux
- **Integration**: Works with Ansible, REST APIs, databases

### 1.2 Setting Up Your Environment

```bash
# Create a virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install basic packages
pip install ipython
```

**Why virtual environments?**
- Isolate project dependencies
- Avoid version conflicts
- Easy to reproduce environments
- Clean project structure

## 2. Data Structures for Network Data

### 2.1 Lists - Sequential Device Data

Lists store ordered collections, perfect for device lists, interfaces, routes.

```python
# List of devices
devices = ['Router1', 'Router2', 'Switch1', 'Switch2']

# List of interfaces
interfaces = [
    'GigabitEthernet0/0',
    'GigabitEthernet0/1',
    'GigabitEthernet0/2'
]

# Accessing elements
first_device = devices[0]        # 'Router1'
last_device = devices[-1]        # 'Switch2'

# Slicing
first_two = devices[0:2]         # ['Router1', 'Router2']

# Adding items
devices.append('Firewall1')
devices.extend(['AP1', 'AP2'])
devices.insert(0, 'Core-Switch')

# Removing items
devices.remove('Router1')        # Remove by value
popped = devices.pop()           # Remove last item
del devices[0]                   # Remove by index

# Iterating
for device in devices:
    print(f"Connecting to {device}")

# List comprehension (powerful!)
uppercase_devices = [d.upper() for d in devices]
routers_only = [d for d in devices if 'Router' in d]
```

**Network Use Cases**:
- Store device inventories
- Manage interface lists
- Track IP addresses
- Handle routing table entries

### 2.2 Dictionaries - Key-Value Network Config

Dictionaries store key-value pairs, ideal for device properties, configurations.

```python
# Device information
router1 = {
    'hostname': 'R1',
    'ip': '192.168.1.1',
    'model': 'ISR4331',
    'ios_version': '17.3.1',
    'interfaces': 4,
    'location': 'HQ'
}

# Accessing values
hostname = router1['hostname']                    # 'R1'
ip = router1.get('ip')                           # Safer: returns None if missing
mgmt_ip = router1.get('mgmt_ip', '10.0.0.1')    # Default value

# Adding/updating
router1['serial_number'] = 'FDO12345678'
router1['ios_version'] = '17.4.1'  # Update existing

# Removing
del router1['location']
popped_value = router1.pop('interfaces', 0)

# Checking keys
if 'hostname' in router1:
    print(router1['hostname'])

# Iterating
for key, value in router1.items():
    print(f"{key}: {value}")

# Dictionary comprehension
ip_map = {device['hostname']: device['ip'] 
          for device in device_list}
```

**Network Use Cases**:
- Device configurations
- Interface details
- Routing protocols
- VLANs and trunks
- API responses

### 2.3 Sets - Unique Network Elements

Sets store unique, unordered elements. Great for VLAN IDs, IP addresses.

```python
# VLANs on Switch 1
switch1_vlans = {10, 20, 30, 40, 50}
switch2_vlans = {30, 40, 50, 60, 70}

# Set operations
common_vlans = switch1_vlans & switch2_vlans        # {30, 40, 50}
all_vlans = switch1_vlans | switch2_vlans           # Union
unique_to_sw1 = switch1_vlans - switch2_vlans       # {10, 20}
symmetric_diff = switch1_vlans ^ switch2_vlans      # Not in both

# Adding/removing
switch1_vlans.add(100)
switch1_vlans.remove(10)        # Error if not exists
switch1_vlans.discard(200)      # No error if not exists

# Membership testing (very fast!)
if 30 in switch1_vlans:
    print("VLAN 30 exists")
```

**Network Use Cases**:
- Find duplicate VLANs
- Compare configurations
- Unique IP addresses
- ACL rule deduplication

### 2.4 Tuples - Immutable Network Data

Tuples are like lists but immutable (can't be changed).

```python
# Immutable device info
device_info = ('Router1', '192.168.1.1', 'IOS-XE')

# Unpacking
hostname, ip, os_type = device_info

# Multiple return values from functions
def get_device_info(device_id):
    return ('R1', '10.1.1.1', 'active')  # Returns tuple

name, ip, status = get_device_info(1)

# Tuples as dictionary keys
interface_status = {
    ('R1', 'Gi0/0'): 'up',
    ('R1', 'Gi0/1'): 'down',
    ('R2', 'Gi0/0'): 'up'
}
```

**Network Use Cases**:
- Return multiple values from functions
- Dictionary keys for complex lookups
- Configuration that shouldn't change

### 2.5 Nested Data Structures - Real Network Inventory

```python
# Complex network inventory
network_inventory = {
    'routers': [
        {
            'hostname': 'R1',
            'ip': '192.168.1.1',
            'interfaces': {
                'GigabitEthernet0/0': {
                    'ip': '10.1.1.1',
                    'mask': '255.255.255.0',
                    'status': 'up'
                },
                'GigabitEthernet0/1': {
                    'ip': '10.1.2.1',
                    'mask': '255.255.255.0',
                    'status': 'up'
                }
            },
            'routing': ['OSPF', 'BGP']
        }
    ],
    'switches': [
        {
            'hostname': 'SW1',
            'ip': '192.168.2.1',
            'vlans': [10, 20, 30],
            'trunk_ports': ['Gi1/0/1', 'Gi1/0/2']
        }
    ]
}

# Accessing nested data
first_router = network_inventory['routers'][0]
router_hostname = first_router['hostname']
interface_ip = first_router['interfaces']['GigabitEthernet0/0']['ip']

# Iterating nested structures
for router in network_inventory['routers']:
    print(f"Router: {router['hostname']}")
    for intf_name, intf_data in router['interfaces'].items():
        print(f"  {intf_name}: {intf_data['ip']}")
```

## 3. String Manipulation for Network Data

### 3.1 String Basics

```python
hostname = "Router1"
description = "Core router at HQ"

# String methods
upper = hostname.upper()                      # ROUTER1
lower = hostname.lower()                      # router1
title = description.title()                   # Core Router At Hq

# String formatting (modern way)
device_name = "R1"
ip_address = "10.1.1.1"
message = f"Device {device_name} has IP {ip_address}"
message = "Device {} has IP {}".format(device_name, ip_address)  # Old way

# Multi-line strings
config = """
interface GigabitEthernet0/0
 ip address 10.1.1.1 255.255.255.0
 no shutdown
"""

# String operations
config_lines = config.strip().split('\n')     # Split into lines
clean_lines = [line.strip() for line in config_lines if line.strip()]

# Joining
commands = ['enable', 'configure terminal', 'interface Gi0/0']
full_command = '\n'.join(commands)

# String searching
if 'shutdown' in config:
    print("Interface is shutdown")

if config.startswith('interface'):
    print("Interface configuration")
```

### 3.2 Regular Expressions for Parsing CLI Output

Regex is essential for parsing unstructured CLI output.

```python
import re

# Example: Parse interface status
show_int_output = """
GigabitEthernet0/0 is up, line protocol is up
  Hardware is ISR4331-3x1GE, address is 0011.2233.4455
  Internet address is 10.1.1.1/24
GigabitEthernet0/1 is down, line protocol is down
  Hardware is ISR4331-3x1GE, address is 0011.2233.4466
  Internet address is 10.1.2.1/24
"""

# Extract interface names and status
pattern = r'(\w+/\d+/\d+|\w+/\d+) is (up|down)'
matches = re.findall(pattern, show_int_output)
# Result: [('GigabitEthernet0/0', 'up'), ('GigabitEthernet0/1', 'down')]

# Extract IP addresses
ip_pattern = r'Internet address is (\d+\.\d+\.\d+\.\d+)/(\d+)'
ip_matches = re.findall(ip_pattern, show_int_output)
# Result: [('10.1.1.1', '24'), ('10.1.2.1', '24')]

# Named groups (cleaner)
pattern = r'(?P<interface>\S+) is (?P<status>up|down)'
for match in re.finditer(pattern, show_int_output):
    print(f"Interface {match.group('interface')}: {match.group('status')}")
```

**Common Regex Patterns for Network**:

```python
# IP Address
ip_regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

# MAC Address
mac_regex = r'[0-9a-fA-F]{4}\.[0-9a-fA-F]{4}\.[0-9a-fA-F]{4}'

# Interface names
interface_regex = r'(GigabitEthernet|FastEthernet|Ethernet)\d+/\d+(?:/\d+)?'

# VLAN IDs
vlan_regex = r'VLAN(\d+)'

# More specific IP (with validation groups)
ip_octet = r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
ip_address = rf'{ip_octet}\.{ip_octet}\.{ip_octet}\.{ip_octet}'
```

### 3.3 Practical Parsing Example

```python
def parse_show_version(output):
    """
    Parse 'show version' output
    Returns dict with version, uptime, model
    """
    version_pattern = r'Version (\S+)'
    model_pattern = r'cisco (\S+) .* bytes of memory'
    uptime_pattern = r'uptime is (.+)'
    
    version = re.search(version_pattern, output)
    model = re.search(model_pattern, output)
    uptime = re.search(uptime_pattern, output)
    
    return {
        'version': version.group(1) if version else 'Unknown',
        'model': model.group(1) if model else 'Unknown',
        'uptime': uptime.group(1) if uptime else 'Unknown'
    }
```

## 4. File I/O for Configuration Management

### 4.1 Reading Configuration Files

```python
# Read entire file
with open('router_config.txt', 'r') as f:
    config = f.read()

# Read line by line
with open('router_config.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith('interface'):
            print(line)

# Read all lines into list
with open('router_config.txt', 'r') as f:
    lines = f.readlines()

# Better: strip whitespace
with open('router_config.txt', 'r') as f:
    lines = [line.strip() for line in f]
```

**Why `with` statement?**
- Automatically closes file
- Handles errors gracefully
- Best practice

### 4.2 Writing Configuration Files

```python
# Write string to file
config = """
hostname R1
interface GigabitEthernet0/0
 ip address 10.1.1.1 255.255.255.0
"""

with open('output_config.txt', 'w') as f:
    f.write(config)

# Write list of lines
commands = [
    'interface GigabitEthernet0/0',
    ' description WAN Link',
    ' ip address 10.1.1.1 255.255.255.0',
    ' no shutdown'
]

with open('commands.txt', 'w') as f:
    f.write('\n'.join(commands))

# Append to file
with open('log.txt', 'a') as f:
    f.write('New log entry\n')
```

### 4.3 Working with JSON

JSON is the standard format for APIs and structured data.

```python
import json

# Dictionary to JSON file
device_inventory = {
    'routers': [
        {'hostname': 'R1', 'ip': '10.1.1.1', 'model': 'ISR4331'},
        {'hostname': 'R2', 'ip': '10.1.1.2', 'model': 'ISR4331'}
    ]
}

# Write JSON
with open('inventory.json', 'w') as f:
    json.dump(device_inventory, f, indent=2)

# Read JSON
with open('inventory.json', 'r') as f:
    loaded_inventory = json.load(f)

# JSON string conversions
json_string = json.dumps(device_inventory, indent=2)
data = json.loads(json_string)
```

### 4.4 Working with CSV

CSV is great for spreadsheet-compatible data.

```python
import csv

# Write CSV
devices = [
    ['Hostname', 'IP', 'Model', 'Location'],
    ['R1', '10.1.1.1', 'ISR4331', 'HQ'],
    ['R2', '10.1.1.2', 'ISR4331', 'Branch1'],
]

with open('devices.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(devices)

# Read CSV
with open('devices.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)  # Skip header row
    for row in reader:
        hostname, ip, model, location = row
        print(f"{hostname}: {ip}")

# DictReader (better for named fields)
with open('devices.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Hostname']}: {row['IP']}")
```

## 5. Functions - Reusable Automation

### 5.1 Function Basics

```python
def connect_to_device(ip, username, password):
    """
    Connect to network device
    
    Args:
        ip (str): Device IP address
        username (str): SSH username
        password (str): SSH password
    
    Returns:
        dict: Connection status
    """
    print(f"Connecting to {ip}")
    # Connection logic here
    return {'status': 'connected', 'ip': ip}

# Call function
result = connect_to_device('10.1.1.1', 'admin', 'cisco')
```

### 5.2 Default Arguments

```python
def send_command(device, command, timeout=30, verbose=False):
    """Send command with optional timeout and verbosity"""
    if verbose:
        print(f"Sending: {command}")
    
    # Command logic
    return f"Output from {device}"

# Use defaults
output = send_command('R1', 'show version')

# Override defaults
output = send_command('R1', 'show version', timeout=60, verbose=True)
```

### 5.3 Variable Arguments

```python
def configure_interfaces(*interfaces):
    """Configure multiple interfaces"""
    for intf in interfaces:
        print(f"Configuring {intf}")

configure_interfaces('Gi0/0', 'Gi0/1', 'Gi0/2')

def build_config(**kwargs):
    """Build config from keyword arguments"""
    config = []
    if 'hostname' in kwargs:
        config.append(f"hostname {kwargs['hostname']}")
    if 'domain' in kwargs:
        config.append(f"ip domain-name {kwargs['domain']}")
    return '\n'.join(config)

config = build_config(hostname='R1', domain='cisco.com')
```

### 5.4 Return Multiple Values

```python
def parse_interface(interface_output):
    """Parse interface output, return multiple values"""
    # Parsing logic
    status = 'up'
    protocol = 'up'
    ip_address = '10.1.1.1'
    
    return status, protocol, ip_address

# Unpack return values
status, protocol, ip = parse_interface(output)
```

## 6. Classes - Object-Oriented Network Automation

### 6.1 Basic Class Structure

```python
class NetworkDevice:
    """Represents a network device"""
    
    def __init__(self, hostname, ip, device_type):
        """Initialize device"""
        self.hostname = hostname
        self.ip = ip
        self.device_type = device_type
        self.is_connected = False
    
    def connect(self):
        """Connect to device"""
        print(f"Connecting to {self.hostname} at {self.ip}")
        self.is_connected = True
    
    def disconnect(self):
        """Disconnect from device"""
        print(f"Disconnecting from {self.hostname}")
        self.is_connected = False
    
    def send_command(self, command):
        """Send command to device"""
        if not self.is_connected:
            raise Exception("Not connected to device")
        print(f"Sending '{command}' to {self.hostname}")
        return f"Output from {self.hostname}"
    
    def __str__(self):
        """String representation"""
        return f"Device({self.hostname}, {self.ip}, {self.device_type})"

# Using the class
router = NetworkDevice('R1', '10.1.1.1', 'router')
print(router)
router.connect()
output = router.send_command('show version')
router.disconnect()
```

### 6.2 Inheritance

```python
class Router(NetworkDevice):
    """Specialized Router class"""
    
    def __init__(self, hostname, ip, routing_protocols=None):
        super().__init__(hostname, ip, 'router')
        self.routing_protocols = routing_protocols or []
    
    def show_routing_table(self):
        """Show routing table"""
        if not self.is_connected:
            raise Exception("Not connected")
        return self.send_command('show ip route')

class Switch(NetworkDevice):
    """Specialized Switch class"""
    
    def __init__(self, hostname, ip, vlan_count=0):
        super().__init__(hostname, ip, 'switch')
        self.vlan_count = vlan_count
    
    def show_vlan(self):
        """Show VLAN information"""
        return self.send_command('show vlan')

# Using inherited classes
router = Router('R1', '10.1.1.1', ['OSPF', 'BGP'])
switch = Switch('SW1', '10.1.2.1', vlan_count=10)
```

## 7. Error Handling

### 7.1 Try-Except Basics

```python
def connect_to_device(ip):
    """Connect with error handling"""
    try:
        # Simulated connection
        if ip == '0.0.0.0':
            raise ValueError("Invalid IP address")
        
        print(f"Connected to {ip}")
        return True
        
    except ValueError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
    finally:
        print("Connection attempt finished")

# Try connection
success = connect_to_device('10.1.1.1')
```

### 7.2 Multiple Exceptions

```python
def parse_config_file(filename):
    """Parse config with comprehensive error handling"""
    try:
        with open(filename, 'r') as f:
            content = f.read()
        
        # Parse content
        if not content:
            raise ValueError("File is empty")
        
        return content
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
```

### 7.3 Custom Exceptions

```python
class DeviceConnectionError(Exception):
    """Custom exception for device connection failures"""
    pass

class ConfigurationError(Exception):
    """Custom exception for configuration issues"""
    pass

def configure_device(device, config):
    """Configure device with custom exceptions"""
    if not device.is_connected:
        raise DeviceConnectionError(f"Not connected to {device.hostname}")
    
    if not config:
        raise ConfigurationError("Configuration is empty")
    
    # Apply configuration
    return True

# Usage
try:
    configure_device(my_device, config_string)
except DeviceConnectionError as e:
    print(f"Connection error: {e}")
except ConfigurationError as e:
    print(f"Config error: {e}")
```

## 8. Logging Best Practices

### 8.1 Basic Logging

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='automation.log'
)

logger = logging.getLogger(__name__)

def connect_device(ip):
    """Connect with logging"""
    logger.info(f"Attempting connection to {ip}")
    
    try:
        # Connection logic
        logger.debug(f"Connection details: {ip}")
        logger.info(f"Successfully connected to {ip}")
        return True
    except Exception as e:
        logger.error(f"Failed to connect to {ip}: {e}")
        return False

# Different log levels
logger.debug("Detailed debugging information")
logger.info("General informational message")
logger.warning("Warning message")
logger.error("Error occurred")
logger.critical("Critical error!")
```

### 8.2 Advanced Logging Configuration

```python
import logging
from logging.handlers import RotatingFileHandler

# Create logger
logger = logging.getLogger('network_automation')
logger.setLevel(logging.DEBUG)

# Console handler (INFO and above)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_format = logging.Formatter('%(levelname)s: %(message)s')
console_handler.setFormatter(console_format)

# File handler (DEBUG and above, rotating)
file_handler = RotatingFileHandler(
    'automation.log',
    maxBytes=1024*1024,  # 1MB
    backupCount=5
)
file_handler.setLevel(logging.DEBUG)
file_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(file_format)

# Add handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Use logger
logger.debug("Debug message - only in file")
logger.info("Info message - console and file")
logger.error("Error message - console and file")
```

## 9. Modules and Code Organization

### 9.1 Creating Modules

**File: device_manager.py**
```python
"""
Device Manager Module
Handles network device operations
"""

class Device:
    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = ip
    
    def connect(self):
        print(f"Connecting to {self.hostname}")

def parse_config(config_string):
    """Parse configuration string"""
    return config_string.split('\n')

# Constants
DEFAULT_TIMEOUT = 30
DEFAULT_PORT = 22
```

**File: main.py**
```python
# Import entire module
import device_manager

device = device_manager.Device('R1', '10.1.1.1')
timeout = device_manager.DEFAULT_TIMEOUT

# Import specific items
from device_manager import Device, parse_config

device = Device('R1', '10.1.1.1')
config_lines = parse_config(config_string)

# Import with alias
from device_manager import Device as NetworkDevice

device = NetworkDevice('R1', '10.1.1.1')
```

### 9.2 Package Structure

```
my_automation/
├── __init__.py
├── devices/
│   ├── __init__.py
│   ├── router.py
│   └── switch.py
├── parsers/
│   ├── __init__.py
│   ├── config_parser.py
│   └── show_parser.py
└── utils/
    ├── __init__.py
    ├── logger.py
    └── validators.py
```

## 10. Best Practices Summary

### Code Style
- Follow PEP 8 style guide
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions small and focused
- Comment complex logic

### Error Handling
- Use try-except appropriately
- Don't catch generic exceptions unless necessary
- Log errors properly
- Provide helpful error messages

### Security
- Never hardcode passwords
- Use environment variables or config files
- Don't commit credentials to version control
- Validate all user input

### Performance
- Use list comprehensions for simple iterations
- Avoid unnecessary copies of large data
- Close file handles and connections
- Use generators for large datasets

## 📝 Practice Exercises

See `exercises.md` for hands-on practice problems.

## 🎯 Next Steps

Once you've mastered these fundamentals, you're ready to:
1. Build the Network Device Inventory Manager project
2. Practice with the exercises
3. Move on to Module 2: SSH Automation with Netmiko

## 📚 Additional Resources

- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/)
- [Python for Network Engineers](https://pyneng.readthedocs.io/)
- [Cisco DevNet Learning Labs](https://developer.cisco.com/learning/)

---

**Remember**: The best way to learn is by doing. Type all the code examples, experiment with them, and build the project!




