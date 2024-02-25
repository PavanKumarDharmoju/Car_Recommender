import json


def convert_to_krf(data, entity_type):
    krf_lines = []
    for record in data["RECORDS"]:
        if entity_type == "automobile":
            krf_lines.append(f"(isa {record['id']} Automobile)")
            krf_lines.append(f"(hasBrand {record['id']} {record['brand_id']})")
            krf_lines.append(f"(hasName {record['id']} \"{record['name']}\")")
        elif entity_type == "brand":
            krf_lines.append(f"(isa {record['id']} Brand)")
            krf_lines.append(f"(hasLogo {record['id']} \"{record['logo']}\")")
            krf_lines.append(f"(hasName {record['id']} \"{record['name']}\")")
        elif entity_type == "engine":
            krf_lines.append(f"(isa {record['id']} Engine)")
            krf_lines.append(f"(belongsToAutomobile {record['id']} {record['automobile_id']})")
            krf_lines.append(f"(hasname {record['id']} \"{record['name']}\")")
    return krf_lines

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def write_krf_file(krf_lines, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in krf_lines:
            file.write(line + "\n")

# Convert and save the automobiles data
automobiles_data = read_json_file('data/json/automobiles.json')
automobiles_krf = convert_to_krf(automobiles_data, 'automobile')
write_krf_file(automobiles_krf, 'data/krf/automobiles.krf')

# Convert and save the brands data
brands_data = read_json_file('data/json/brands.json')
brands_krf = convert_to_krf(brands_data, 'brand')
write_krf_file(brands_krf, 'data/krf/brands.krf')

# Convert and save the engines data
engines_data = read_json_file('data/json/engines.json')
engines_krf = convert_to_krf(engines_data, 'engine')
write_krf_file(engines_krf, 'data/krf/engines.krf')
