

from unittest import result
from config_analyzer import build_data

def count_ospf_by_area(data):
    a = {}
    for device in data:
        if "error" in device:
            continue
        for entry in device["ospf"]:
            area = entry["area"]
            a[area] = a.get(area, 0) + 1
    
    return a

result = count_ospf_by_area(build_data())
print(result)


