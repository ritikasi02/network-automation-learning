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
import json
import logging
import csv
from time import asctime
from classparser import ConfigAnalyzer


logger = logging.getLogger(__name__) #just grab a logger to talk to, not configured anything yet


def read_confg(filepath):
    with open(filepath, "r") as f:
        return f.readlines()




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
            analyzer = ConfigAnalyzer(lines)
            device = analyzer.to_dict()
            logger.debug(" file %s with hostname %s has %s interfaces and %d OSPF networks", filename, device["hostname"], len(device["interfaces"]), len(device["ospf"]))
            data.append(device)

        except (OSError, UnicodeDecodeError) as e:
            data.append({"file": filename, "error": str(e)})
            logger.error(f"failed to open '{filename}' : {e}")
#       for c in ospf:
#          print(f" network {c['network']} {c['wildcard']} area {c['area']}" )
    return data

def export_csv(data,filepath):
    columns = ["hostname", "interface_count", "ospf_count"]
    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f,fieldnames=columns)
        writer.writeheader()
        for device in data:
            if "error" in device:
                continue
            writer.writerow({
                "hostname": device["hostname"],
                "interface_count": len(device["interfaces"]),
                "ospf_count": len(device["ospf"]),
            })

def ospf_networks(device):
    result = set()
    for entry in device["ospf"]:
        result.add((entry["network"], entry["wildcard"], entry["area"]))
    return result

def compare_ospf(dev_a, dev_b):
    a = ospf_networks(dev_a)
    b = ospf_networks(dev_b)
    return {
        "only in a": list(a-b),
        "only in b:": list(b-a),
        "in both": list(a & b),
    }

if __name__ == "__main__":
    logging.basicConfig(filename="config_analyzer.log",level=logging.INFO,format="%(asctime)s %(levelname)s %(name)s %(message)s")
    logger.info("run started")
    data = build_data()
    result = compare_ospf(data[0], data[1])
    print(json.dumps(result, indent=2))
    with open("output.json", "w") as f:
        json.dump(data, f, indent=2)
    export_csv(data,"inventory.csv")
    logger.info("run finished")




         
