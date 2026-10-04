
import os
from datetime import datetime
import yaml
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException


username = os.environ["NET_USER"]
password = os.environ["NET_PASS"]

with open("devices.yaml") as f:
    inventory = yaml.safe_load(f)

for entry in inventory["devices"]:

    device = {
    "device_type": entry["device_type"],
    "host": entry["host"],
    "username": username,
    "password": password,
    }

    try:
        with ConnectHandler(**device) as conn:
            hostname = conn.find_prompt().strip("#>")
            output = conn.send_command("show ip int brief")
            ts = datetime.now().strftime("%Y%m%d-%H%M%S")
            path = os.path.join("backups", f"{hostname}_{ts}.cfg")
            with open(path,"w") as f:
                f.write(output)
            print(f"backed up {hostname} -> {path}")
    except NetmikoTimeoutException:
        print(f"TIMEOUT: cannot reach {entry['host']}")
    except NetmikoAuthenticationException:
        print(f"Invalid credentials {entry['host']}")