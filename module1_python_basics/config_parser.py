#!/usr/bin/env python3
"""
Network Configuration Parser Module

This module provides functions to parse Cisco IOS configuration files
and extract structured information like interfaces, routing protocols,
hostnames, and other network data.

Author: Network Automation Curriculum
Module: 1 - Python Fundamentals
"""

import re
from typing import Dict, List, Optional, Tuple


class ConfigParser:
    """
    Parse Cisco IOS configuration files and extract structured data.
    """
    
    def __init__(self, config_text: str):
        """
        Initialize parser with configuration text.
        
        Args:
            config_text (str): Raw configuration file content
        """
        self.config_text = config_text
        self.lines = [line.rstrip() for line in config_text.split('\n')]
    
    def get_hostname(self) -> Optional[str]:
        """
        Extract hostname from configuration.
        
        Returns:
            str: Hostname or None if not found
        """
        pattern = r'^hostname\s+(\S+)'
        for line in self.lines:
            match = re.match(pattern, line)
            if match:
                return match.group(1)
        return None
    
    def get_domain_name(self) -> Optional[str]:
        """
        Extract domain name from configuration.
        
        Returns:
            str: Domain name or None if not found
        """
        pattern = r'^ip domain[_-]name\s+(\S+)'
        for line in self.lines:
            match = re.match(pattern, line)
            if match:
                return match.group(1)
        return None
    
    def get_interfaces(self) -> List[Dict[str, str]]:
        """
        Extract all interfaces with their configuration.
        
        Returns:
            list: List of dictionaries containing interface information
        """
        interfaces = []
        current_interface = None
        
        for line in self.lines:
            # Check for interface line
            if line.startswith('interface '):
                # Save previous interface if exists
                if current_interface:
                    interfaces.append(current_interface)
                
                # Start new interface
                interface_name = line.split('interface ')[1].strip()
                current_interface = {
                    'name': interface_name,
                    'description': '',
                    'ip_address': '',
                    'subnet_mask': '',
                    'status': 'up'  # Default, can be overridden
                }
            
            elif current_interface:
                # Parse interface sub-commands
                line = line.strip()
                
                if line.startswith('description '):
                    current_interface['description'] = line.split('description ')[1]
                
                elif line.startswith('ip address '):
                    parts = line.split()
                    if len(parts) >= 3:
                        current_interface['ip_address'] = parts[2]
                        if len(parts) >= 4:
                            current_interface['subnet_mask'] = parts[3]
                
                elif line == 'shutdown':
                    current_interface['status'] = 'shutdown'
                
                elif line.startswith('no shutdown'):
                    current_interface['status'] = 'up'
        
        # Don't forget the last interface
        if current_interface:
            interfaces.append(current_interface)
        
        return interfaces
    
    def get_routing_protocols(self) -> List[Dict[str, any]]:
        """
        Extract routing protocol configurations.
        
        Returns:
            list: List of routing protocol configurations
        """
        protocols = []
        current_protocol = None
        
        for line in self.lines:
            # Check for routing protocol
            if line.startswith('router '):
                # Save previous protocol if exists
                if current_protocol:
                    protocols.append(current_protocol)
                
                # Start new protocol
                parts = line.split()
                if len(parts) >= 2:
                    protocol_name = parts[1]
                    process_id = parts[2] if len(parts) >= 3 else None
                    
                    current_protocol = {
                        'protocol': protocol_name,
                        'process_id': process_id,
                        'networks': []
                    }
            
            elif current_protocol:
                line = line.strip()
                
                if line.startswith('network '):
                    # Extract network statements
                    current_protocol['networks'].append(line)
                
                elif not line.startswith(' ') and line:
                    # End of router config section
                    protocols.append(current_protocol)
                    current_protocol = None
        
        # Don't forget the last protocol
        if current_protocol:
            protocols.append(current_protocol)
        
        return protocols
    
    def get_ip_addresses(self) -> List[str]:
        """
        Extract all IP addresses from configuration.
        
        Returns:
            list: List of IP addresses found
        """
        ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        ip_addresses = set()  # Use set to avoid duplicates
        
        for line in self.lines:
            matches = re.findall(ip_pattern, line)
            ip_addresses.update(matches)
        
        return sorted(list(ip_addresses))
    
    def get_version(self) -> Optional[str]:
        """
        Extract IOS version from configuration.
        
        Returns:
            str: IOS version or None if not found
        """
        pattern = r'^version\s+(\S+)'
        for line in self.lines:
            match = re.match(pattern, line)
            if match:
                return match.group(1)
        return None
    
    def count_interfaces_by_type(self) -> Dict[str, int]:
        """
        Count interfaces by type (GigabitEthernet, FastEthernet, Loopback, etc.).
        
        Returns:
            dict: Dictionary with interface types as keys and counts as values
        """
        interface_counts = {}
        interfaces = self.get_interfaces()
        
        for interface in interfaces:
            # Extract interface type (e.g., 'GigabitEthernet' from 'GigabitEthernet0/0')
            match = re.match(r'^([A-Za-z]+)', interface['name'])
            if match:
                intf_type = match.group(1)
                interface_counts[intf_type] = interface_counts.get(intf_type, 0) + 1
        
        return interface_counts
    
    def get_ssh_config(self) -> Dict[str, any]:
        """
        Extract SSH configuration details.
        
        Returns:
            dict: SSH configuration information
        """
        ssh_config = {
            'enabled': False,
            'version': None,
            'timeout': None,
            'authentication_retries': None
        }
        
        for line in self.lines:
            if 'ip ssh version' in line:
                ssh_config['enabled'] = True
                match = re.search(r'version\s+(\d+)', line)
                if match:
                    ssh_config['version'] = match.group(1)
            
            elif 'ip ssh time-out' in line:
                match = re.search(r'time-out\s+(\d+)', line)
                if match:
                    ssh_config['timeout'] = match.group(1)
            
            elif 'ip ssh authentication-retries' in line:
                match = re.search(r'authentication-retries\s+(\d+)', line)
                if match:
                    ssh_config['authentication_retries'] = match.group(1)
        
        return ssh_config
    
    def get_vlans(self) -> List[int]:
        """
        Extract VLAN IDs from configuration (mainly for switches).
        
        Returns:
            list: List of VLAN IDs
        """
        vlans = set()
        vlan_pattern = r'vlan\s+(\d+)'
        
        for line in self.lines:
            matches = re.findall(vlan_pattern, line, re.IGNORECASE)
            for vlan_id in matches:
                vlans.add(int(vlan_id))
        
        return sorted(list(vlans))
    
    def to_dict(self) -> Dict[str, any]:
        """
        Convert parsed configuration to a comprehensive dictionary.
        
        Returns:
            dict: Complete device configuration as structured data
        """
        return {
            'hostname': self.get_hostname(),
            'domain_name': self.get_domain_name(),
            'version': self.get_version(),
            'interfaces': self.get_interfaces(),
            'interface_counts': self.count_interfaces_by_type(),
            'routing_protocols': self.get_routing_protocols(),
            'ip_addresses': self.get_ip_addresses(),
            'ssh_config': self.get_ssh_config(),
            'vlans': self.get_vlans()
        }


def parse_config_file(filename: str) -> ConfigParser:
    """
    Parse a configuration file and return a ConfigParser object.
    
    Args:
        filename (str): Path to configuration file
    
    Returns:
        ConfigParser: Parser object containing the configuration
    
    Raises:
        FileNotFoundError: If configuration file doesn't exist
        IOError: If file cannot be read
    """
    try:
        with open(filename, 'r') as f:
            config_text = f.read()
        return ConfigParser(config_text)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found: {filename}")
    except IOError as e:
        raise IOError(f"Error reading configuration file: {e}")


def compare_configs(config1: ConfigParser, config2: ConfigParser) -> Dict[str, any]:
    """
    Compare two device configurations and return differences.
    
    Args:
        config1 (ConfigParser): First configuration
        config2 (ConfigParser): Second configuration
    
    Returns:
        dict: Dictionary containing configuration differences
    """
    differences = {
        'hostnames': (config1.get_hostname(), config2.get_hostname()),
        'versions': (config1.get_version(), config2.get_version()),
        'interface_count': (len(config1.get_interfaces()), len(config2.get_interfaces())),
        'common_ips': set(config1.get_ip_addresses()) & set(config2.get_ip_addresses()),
        'unique_ips_1': set(config1.get_ip_addresses()) - set(config2.get_ip_addresses()),
        'unique_ips_2': set(config2.get_ip_addresses()) - set(config1.get_ip_addresses())
    }
    
    return differences


# Example usage and testing
if __name__ == '__main__':
    """
    Example usage of the ConfigParser module.
    Run this script directly to see it in action!
    """
    import os
    
    print("=" * 70)
    print("Network Configuration Parser - Example Usage")
    print("=" * 70)
    print()
    
    # Example 1: Parse a single configuration file
    sample_config = """
hostname TestRouter
!
ip domain-name example.com
!
interface GigabitEthernet0/0
 description WAN Link
 ip address 10.1.1.1 255.255.255.0
 no shutdown
!
interface Loopback0
 ip address 1.1.1.1 255.255.255.255
!
router ospf 1
 network 10.1.1.0 0.0.0.255 area 0
 network 1.1.1.1 0.0.0.0 area 0
!
version 15.7
ip ssh version 2
"""
    
    print("Parsing sample configuration...")
    print("-" * 70)
    
    parser = ConfigParser(sample_config)
    
    print(f"Hostname: {parser.get_hostname()}")
    print(f"Domain Name: {parser.get_domain_name()}")
    print(f"IOS Version: {parser.get_version()}")
    print()
    
    print("Interfaces:")
    for interface in parser.get_interfaces():
        print(f"  - {interface['name']}: {interface['ip_address']}")
        if interface['description']:
            print(f"    Description: {interface['description']}")
    print()
    
    print("Routing Protocols:")
    for protocol in parser.get_routing_protocols():
        print(f"  - {protocol['protocol']} {protocol['process_id']}")
        print(f"    Networks: {len(protocol['networks'])}")
    print()
    
    print("SSH Configuration:")
    ssh = parser.get_ssh_config()
    print(f"  Enabled: {ssh['enabled']}")
    print(f"  Version: {ssh['version']}")
    print()
    
    # Example 2: Parse files from sample_configs directory
    configs_dir = 'sample_configs'
    if os.path.exists(configs_dir):
        print("=" * 70)
        print("Parsing configuration files from sample_configs/")
        print("=" * 70)
        
        for filename in os.listdir(configs_dir):
            if filename.endswith('.txt'):
                filepath = os.path.join(configs_dir, filename)
                print(f"\n📄 File: {filename}")
                print("-" * 70)
                
                try:
                    parser = parse_config_file(filepath)
                    config_dict = parser.to_dict()
                    
                    print(f"Hostname: {config_dict['hostname']}")
                    print(f"Domain: {config_dict['domain_name']}")
                    print(f"Version: {config_dict['version']}")
                    print(f"Total Interfaces: {len(config_dict['interfaces'])}")
                    print(f"Interface Types: {config_dict['interface_counts']}")
                    print(f"Routing Protocols: {len(config_dict['routing_protocols'])}")
                    
                except Exception as e:
                    print(f"Error parsing {filename}: {e}")
    else:
        print(f"\nNote: '{configs_dir}' directory not found.")
        print("Create it and add configuration files to test file parsing!")
    
    print("\n" + "=" * 70)
    print("Module usage complete! Check the code to see how it works.")
    print("=" * 70)

