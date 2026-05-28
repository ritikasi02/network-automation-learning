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

def read_confg(filepath):
    with open(filepath, "r") as f:
        return f.readlines()

def get_hostname(lines):
    for line in lines:
        if line.strip().startswith("hostname"):
            return line.split()[1]
    
def get_interfaces(lines):
    interface = []
    for i, line in enumerate(lines):
        if line.strip().startswith("interface"):
            for j in range(i+1, i+10):
                if "ip address" in lines[j] and "no ip address" not in lines[j]:
                    ip = lines[j].strip().split()[2]
                    mask = lines[j].strip().split()[3]
                    interface.append({"name": line.strip(),"ip": ip, "mask":mask})
                    break
                if lines[j].strip() == '!':
                    break
    return interface

if __name__ == "__main__":
    folder = "sample_configs"
    config_files = os.listdir(folder)
    for filename in config_files:
        filepath = os.path.join(folder, filename)
        lines =read_confg(filepath)
        hostname = get_hostname(lines)
        interface = get_interfaces(lines)
        print(hostname)
        for intf in interface:
            print(f" {intf['name']} {intf['ip']} {intf['mask']}")



         
