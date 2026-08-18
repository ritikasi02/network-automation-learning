

import ipaddress
import re


class ConfigAnalyzer:
    def __init__(self, lines):
        self.data = lines
    
    def get_hostname(self):
        for line in self.data:
            if line.strip().startswith("hostname"):
                parts = line.split()
                if len(parts) >= 2:
                    return parts[1]
        return "unknown"

    def get_interfaces(self):
        interface = []
        for i, line in enumerate(self.data):
            if line.strip().startswith("interface"):
                for j in range(i+1, min(i+10, len(self.data))):
                    if "ip address" in self.data[j] and "no ip address" not in self.data[j]:
                        parts = self.data[j].strip().split()
                        if len(parts) >= 4 and ipadd(parts[2]):
                            ip = parts[2]
                            mask = parts[3]
                            interface.append({"name": line.strip(),"ip": ip, "mask":mask})
                            break #breaks innermost j loop, outer i keeps running
                    if self.data[j].strip() == '!':
                        break
        return interface

    def get_ospf(self):
        ospf = []
        for i, line in enumerate(self.data):
            if line.strip().startswith("router ospf"):
                for j in range(i+1, min(i+10, len(self.data))):
                    match = re.search(r"network (\S+) (\S+) area (\d+)", self.data[j])
                    if match:
                        network_ip = match.group(1)
                        wildcard = match.group(2)
                        area = match.group(3)
                        ospf.append({"network": network_ip, "wildcard": wildcard, "area": area})
                    if self.data[j].strip() == '!':
                        break
        return ospf
    
    def to_dict(self):
        return {
            "hostname": self.get_hostname(),
            "interfaces": self.get_interfaces(),
            "ospf": self.get_ospf(),
        }
      
def ipadd(value):
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False
