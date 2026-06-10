#show_run = "sample_configs/R1_config.txt"
#with open(show_run, "r") as f:
#    for line in f:
#        if line.strip().startswith("hostname"):
#            x = line.strip().split()[1]
#            print(x)

#with open(show_run, "r") as f:
#    y = f.readlines()
#    for i, line in enumerate(y):
#        if line.strip().startswith("interface"):
#            for j in range(i+1, i+10):
#                if "ip address" in y[j] and "no ip address" not in y[j]:
#                    ip = y[j].strip().split()[2]
#                    mask = y[j].strip().split()[3]
#                    print(line.strip(), ip, mask)
#                    break
#                if y[j].strip() == "!":
#                    break

import os
import re
import json
import ipaddress
import logging
from time import asctime

logger = logging.getLogger(__name__) #just grab a logger to talk to, not configured anything yet


def read_confg(filepath):
    with open(filepath, "r") as f:
        return f.readlines()

def get_hostname(lines):
    for line in lines:
        if line.strip().startswith("hostname"):
            parts = line.split()
            if len(parts) >= 2:
                return parts[1]
    return "unknown"
    
def get_interfaces(lines):
    interface = []
    for i, line in enumerate(lines):
        if line.strip().startswith("interface"):
            for j in range(i+1, min(i+10, len(lines))):
                if "ip address" in lines[j] and "no ip address" not in lines[j]:
                    parts = lines[j].strip().split()
                    if len(parts) >= 4 and ipadd(parts[2]):
                        ip = parts[2]
                        mask = parts[3]
                        interface.append({"name": line.strip(),"ip": ip, "mask":mask})
                        break
                if lines[j].strip() == '!':
                    break
    return interface

def ipadd(value):
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False

def get_ospf(lines):
    ospf = []
    for i, line in enumerate(lines):
        if line.strip().startswith("router ospf"):
            for j in range(i+1, min(i+10, len(lines))):
                match = re.search(r"network (\S+) (\S+) area (\d+)", lines[j])
                if match:
                    network_ip = match.group(1)
                    wildcard = match.group(2)
                    area = match.group(3)
                    ospf.append({"network": network_ip, "wildcard": wildcard, "area": area})
                if lines[j].strip() == '!':
                    break
    return ospf


def build_data():    
    data = []
    folder = "sample_configs"
    try:
        config_files = sorted(os.listdir(folder))
    except OSError as e:
        logger.critical(f"cannot read config folder '{folder}': {e}")
        return data
    for filename in config_files:
        if not filename.endswith(".txt"):
            continue
        filepath = os.path.join(folder, filename)
        try:
            lines =read_confg(filepath)
            hostname = get_hostname(lines)
            interface = get_interfaces(lines)
#      print(hostname)
#       for intf in interface:
#           print(f" {intf['name']} {intf['ip']} {intf['mask']}")
            ospf = get_ospf(lines)
            logger.debug(" file %s with hostname %s has %s interfaces and %d OSPF networks", filename, hostname, len(interface), len(ospf))
            data.append({"hostname": hostname, "interfaces": interface, "ospf": ospf})

        except (OSError, UnicodeDecodeError) as e:
            data.append({"file": filename, "error": str(e)})
            logger.error(f"failed to open '{filename}' : {e}")
#       for c in ospf:
#          print(f" network {c['network']} {c['wildcard']} area {c['area']}" )
    return data

if __name__ == "__main__":
    logging.basicConfig(filename="config_analyzer.log",level=logging.INFO,format="%(asctime)s %(levelname)s %(name)s %(message)s")
    logger.info("run started")
    data = build_data()
    with open("output.json", "w") as f:
        json.dump(data, f, indent=2)
    logger.info("run finished")




         
