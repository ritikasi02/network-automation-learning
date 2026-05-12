#!/usr/bin/env python3
"""
Network Device Inventory Manager

This is the main project for Module 1: Python Fundamentals.
It demonstrates practical use of Python for network automation by:
- Parsing device configurations
- Building structured inventory
- Generating reports in multiple formats
- Managing device data

Author: Network Automation Curriculum
Module: 1 - Python Fundamentals
"""

import os
import json
import csv
import logging
from datetime import datetime
from typing import List, Dict, Optional
from config_parser import ConfigParser, parse_config_file


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('inventory_manager.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class NetworkInventory:
    """
    Manage network device inventory with configuration parsing,
    reporting, and data management capabilities.
    """
    
    def __init__(self):
        """Initialize empty network inventory."""
        self.devices = []
        self.statistics = {
            'total_devices': 0,
            'total_interfaces': 0,
            'routing_protocols': set(),
            'unique_ips': set()
        }
        logger.info("Network Inventory initialized")
    
    def add_device_from_config(self, config_file: str) -> bool:
        """
        Add a device to inventory by parsing its configuration file.
        
        Args:
            config_file (str): Path to device configuration file
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            logger.info(f"Adding device from config file: {config_file}")
            
            # Parse configuration
            parser = parse_config_file(config_file)
            device_data = parser.to_dict()
            
            # Add metadata
            device_data['config_file'] = config_file
            device_data['added_at'] = datetime.now().isoformat()
            
            # Add to inventory
            self.devices.append(device_data)
            
            # Update statistics
            self._update_statistics(device_data)
            
            logger.info(f"Successfully added device: {device_data['hostname']}")
            return True
            
        except Exception as e:
            logger.error(f"Error adding device from {config_file}: {e}")
            return False
    
    def add_devices_from_directory(self, directory: str) -> int:
        """
        Add all devices from configuration files in a directory.
        
        Args:
            directory (str): Path to directory containing config files
        
        Returns:
            int: Number of devices successfully added
        """
        if not os.path.exists(directory):
            logger.error(f"Directory not found: {directory}")
            return 0
        
        added_count = 0
        logger.info(f"Scanning directory: {directory}")
        
        for filename in os.listdir(directory):
            if filename.endswith('.txt') or filename.endswith('.cfg'):
                filepath = os.path.join(directory, filename)
                if self.add_device_from_config(filepath):
                    added_count += 1
        
        logger.info(f"Added {added_count} devices from {directory}")
        return added_count
    
    def _update_statistics(self, device_data: Dict) -> None:
        """
        Update inventory statistics with new device data.
        
        Args:
            device_data (dict): Device configuration data
        """
        self.statistics['total_devices'] += 1
        self.statistics['total_interfaces'] += len(device_data['interfaces'])
        
        # Update routing protocols
        for protocol in device_data['routing_protocols']:
            self.statistics['routing_protocols'].add(protocol['protocol'])
        
        # Update unique IPs
        for ip in device_data['ip_addresses']:
            self.statistics['unique_ips'].add(ip)
    
    def get_device_by_hostname(self, hostname: str) -> Optional[Dict]:
        """
        Retrieve device information by hostname.
        
        Args:
            hostname (str): Device hostname to search for
        
        Returns:
            dict: Device data or None if not found
        """
        for device in self.devices:
            if device['hostname'] == hostname:
                return device
        return None
    
    def list_all_devices(self) -> List[str]:
        """
        Get list of all device hostnames in inventory.
        
        Returns:
            list: List of hostnames
        """
        return [device['hostname'] for device in self.devices]
    
    def search_by_ip(self, ip_address: str) -> List[Dict]:
        """
        Find all devices containing a specific IP address.
        
        Args:
            ip_address (str): IP address to search for
        
        Returns:
            list: List of devices containing the IP
        """
        matching_devices = []
        for device in self.devices:
            if ip_address in device['ip_addresses']:
                matching_devices.append(device)
        return matching_devices
    
    def get_devices_by_routing_protocol(self, protocol: str) -> List[Dict]:
        """
        Get all devices running a specific routing protocol.
        
        Args:
            protocol (str): Routing protocol name (e.g., 'ospf', 'bgp')
        
        Returns:
            list: List of devices running the protocol
        """
        matching_devices = []
        for device in self.devices:
            for rp in device['routing_protocols']:
                if rp['protocol'].lower() == protocol.lower():
                    matching_devices.append(device)
                    break
        return matching_devices
    
    def generate_summary_report(self) -> str:
        """
        Generate a text-based summary report of the inventory.
        
        Returns:
            str: Formatted report text
        """
        report_lines = []
        report_lines.append("=" * 70)
        report_lines.append("NETWORK INVENTORY SUMMARY REPORT")
        report_lines.append("=" * 70)
        report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append("")
        
        # Overall statistics
        report_lines.append("OVERALL STATISTICS")
        report_lines.append("-" * 70)
        report_lines.append(f"Total Devices: {self.statistics['total_devices']}")
        report_lines.append(f"Total Interfaces: {self.statistics['total_interfaces']}")
        report_lines.append(f"Routing Protocols in Use: {', '.join(sorted(self.statistics['routing_protocols']))}")
        report_lines.append(f"Unique IP Addresses: {len(self.statistics['unique_ips'])}")
        report_lines.append("")
        
        # Device details
        report_lines.append("DEVICE DETAILS")
        report_lines.append("-" * 70)
        
        for device in self.devices:
            report_lines.append(f"\nDevice: {device['hostname']}")
            report_lines.append(f"  Domain: {device['domain_name']}")
            report_lines.append(f"  IOS Version: {device['version']}")
            report_lines.append(f"  Interfaces: {len(device['interfaces'])}")
            
            # Interface summary
            for intf in device['interfaces']:
                status_symbol = "✓" if intf['status'] == 'up' else "✗"
                ip_info = f"{intf['ip_address']}" if intf['ip_address'] else "no IP"
                report_lines.append(f"    [{status_symbol}] {intf['name']}: {ip_info}")
                if intf['description']:
                    report_lines.append(f"        Description: {intf['description']}")
            
            # Routing protocols
            if device['routing_protocols']:
                report_lines.append(f"  Routing Protocols:")
                for rp in device['routing_protocols']:
                    report_lines.append(f"    - {rp['protocol']} {rp['process_id']}")
        
        report_lines.append("\n" + "=" * 70)
        report_lines.append("END OF REPORT")
        report_lines.append("=" * 70)
        
        return "\n".join(report_lines)
    
    def export_to_json(self, filename: str = 'inventory.json') -> bool:
        """
        Export inventory to JSON format.
        
        Args:
            filename (str): Output filename
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            output_dir = 'outputs'
            os.makedirs(output_dir, exist_ok=True)
            filepath = os.path.join(output_dir, filename)
            
            export_data = {
                'generated_at': datetime.now().isoformat(),
                'statistics': {
                    'total_devices': self.statistics['total_devices'],
                    'total_interfaces': self.statistics['total_interfaces'],
                    'routing_protocols': list(self.statistics['routing_protocols']),
                    'unique_ips': list(self.statistics['unique_ips'])
                },
                'devices': self.devices
            }
            
            with open(filepath, 'w') as f:
                json.dump(export_data, f, indent=2)
            
            logger.info(f"Inventory exported to JSON: {filepath}")
            return True
            
        except Exception as e:
            logger.error(f"Error exporting to JSON: {e}")
            return False
    
    def export_to_csv(self, filename: str = 'inventory.csv') -> bool:
        """
        Export inventory to CSV format (device summary).
        
        Args:
            filename (str): Output filename
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            output_dir = 'outputs'
            os.makedirs(output_dir, exist_ok=True)
            filepath = os.path.join(output_dir, filename)
            
            with open(filepath, 'w', newline='') as f:
                writer = csv.writer(f)
                
                # Header
                writer.writerow([
                    'Hostname', 'Domain', 'Version', 'Total Interfaces',
                    'Active Interfaces', 'Routing Protocols', 'IP Count'
                ])
                
                # Data rows
                for device in self.devices:
                    active_intfs = sum(1 for i in device['interfaces'] if i['status'] == 'up')
                    routing_protos = ', '.join([rp['protocol'] for rp in device['routing_protocols']])
                    
                    writer.writerow([
                        device['hostname'],
                        device['domain_name'],
                        device['version'],
                        len(device['interfaces']),
                        active_intfs,
                        routing_protos,
                        len(device['ip_addresses'])
                    ])
            
            logger.info(f"Inventory exported to CSV: {filepath}")
            return True
            
        except Exception as e:
            logger.error(f"Error exporting to CSV: {e}")
            return False
    
    def export_interfaces_to_csv(self, filename: str = 'interfaces.csv') -> bool:
        """
        Export detailed interface information to CSV.
        
        Args:
            filename (str): Output filename
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            output_dir = 'outputs'
            os.makedirs(output_dir, exist_ok=True)
            filepath = os.path.join(output_dir, filename)
            
            with open(filepath, 'w', newline='') as f:
                writer = csv.writer(f)
                
                # Header
                writer.writerow([
                    'Device', 'Interface', 'IP Address', 'Subnet Mask',
                    'Status', 'Description'
                ])
                
                # Data rows
                for device in self.devices:
                    for intf in device['interfaces']:
                        writer.writerow([
                            device['hostname'],
                            intf['name'],
                            intf['ip_address'],
                            intf['subnet_mask'],
                            intf['status'],
                            intf['description']
                        ])
            
            logger.info(f"Interface details exported to CSV: {filepath}")
            return True
            
        except Exception as e:
            logger.error(f"Error exporting interfaces to CSV: {e}")
            return False
    
    def save_report_to_file(self, filename: str = 'inventory_report.txt') -> bool:
        """
        Save the summary report to a text file.
        
        Args:
            filename (str): Output filename
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            output_dir = 'outputs'
            os.makedirs(output_dir, exist_ok=True)
            filepath = os.path.join(output_dir, filename)
            
            report = self.generate_summary_report()
            
            with open(filepath, 'w') as f:
                f.write(report)
            
            logger.info(f"Report saved to: {filepath}")
            return True
            
        except Exception as e:
            logger.error(f"Error saving report: {e}")
            return False


def main():
    """
    Main function - demonstrates the inventory manager functionality.
    """
    print("\n" + "=" * 70)
    print("NETWORK DEVICE INVENTORY MANAGER")
    print("Module 1: Python Fundamentals - Main Project")
    print("=" * 70 + "\n")
    
    # Create inventory instance
    inventory = NetworkInventory()
    
    # Add devices from sample_configs directory
    configs_directory = 'sample_configs'
    
    if os.path.exists(configs_directory):
        print(f"📁 Loading devices from '{configs_directory}'...")
        added = inventory.add_devices_from_directory(configs_directory)
        print(f"✓ Successfully added {added} device(s)\n")
        
        if added > 0:
            # Display summary report
            print("📊 INVENTORY SUMMARY:")
            print(inventory.generate_summary_report())
            print()
            
            # List all devices
            print("📋 Devices in inventory:")
            for hostname in inventory.list_all_devices():
                print(f"  - {hostname}")
            print()
            
            # Export to various formats
            print("💾 Exporting inventory...")
            inventory.export_to_json()
            inventory.export_to_csv()
            inventory.export_interfaces_to_csv()
            inventory.save_report_to_file()
            print("✓ All exports completed! Check the 'outputs/' directory.\n")
            
            # Demonstrate search functionality
            devices = inventory.list_all_devices()
            if devices:
                hostname = devices[0]
                print(f"🔍 Example: Searching for device '{hostname}':")
                device = inventory.get_device_by_hostname(hostname)
                if device:
                    print(f"   Found: {device['hostname']}")
                    print(f"   Version: {device['version']}")
                    print(f"   Interfaces: {len(device['interfaces'])}")
                print()
            
            # Search by routing protocol
            print("🔍 Devices running OSPF:")
            ospf_devices = inventory.get_devices_by_routing_protocol('ospf')
            for device in ospf_devices:
                print(f"   - {device['hostname']}")
            print()
            
        else:
            print("⚠️  No devices were added. Check the configuration files.\n")
    else:
        print(f"⚠️  Configuration directory '{configs_directory}' not found!")
        print(f"   Please create it and add device configuration files (.txt or .cfg)\n")
        print("📝 Example usage:")
        print("   1. Create 'sample_configs/' directory")
        print("   2. Add router/switch configuration files")
        print("   3. Run this script again\n")
    
    print("=" * 70)
    print("INVENTORY MANAGER COMPLETE")
    print("=" * 70)
    print("\n💡 Tips:")
    print("   - Check 'outputs/' directory for exported files")
    print("   - Review 'inventory_manager.log' for detailed logs")
    print("   - Modify this script to add custom functionality\n")


if __name__ == '__main__':
    main()




