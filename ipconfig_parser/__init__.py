def parser(filepath):
    adapters = {}
    current = None
    with open(filepath, "r", encoding="utf-16") as file:
        for row in file:
            row = row.strip()
            if "adapter" in row.lower() and row.endswith(":"):
                name = row.replace(":","").strip()
                current = name
                if name not in adapters:
                    adapters[name] = {}
            elif ":" in row and current:
                key, value = row.split(":",1)
                key = key.split(".")[0].strip()
                value = value.strip().split("(")[0].strip()
                adapters[current][key] = value
    return adapters

a = parser("ipconfig_parser/parser_input_a.txt")
b = parser("ipconfig_parser/parser_input_b.txt")
merger = {}
for name in set(a.keys()) | set(b.keys()):
    merger[name] = {}
    if name in a:
        merger[name].update(a[name])
    if name in b:
        merger[name].update(b[name])

def builder(merge):
    result = []
    for name, data in merge.items():
        adapter = {
            "adapter_name": name,
            "description": data.get("Description", ""),
            "physical_address": data.get("Physical Address", ""),
            "dhcp_enabled": data.get("DHCP Enabled", ""),
            "ipv4_address": data.get("IPv4 Address", ""),
            "subnet_mask": data.get("Subnet Mask", ""),
            "default_gateway": data.get("Default Gateway", "")
        }
        result.append(adapter)
    return result

import json
final = builder(merger)
with open("ipconfig_parser/ipconfig.json", "w", encoding="utf-16") as file:
    json.dump(final, file, indent=2)
        