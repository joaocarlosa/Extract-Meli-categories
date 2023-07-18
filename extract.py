import json
import csv

def find_structure_with_id_name(json_data):
    extracted_data = []

    for category_id, category_info in json_data.items():
        path_from_root = category_info.get("path_from_root", [])
        
        target_content = [
            {"id": "MLB5672", "name": "Acessórios para Veículos"},
            {"id": "MLB22693", "name": "Peças de Carros e Caminhonetes"}
        ]

        if all(item in path_from_root for item in target_content):
            for item in path_from_root:
                id_name = {"id": item["id"], "name": item["name"]}
                extracted_data.append(id_name)

    return extracted_data

file_name = "mlb.json"

with open(file_name, "r") as file:
    json_data = json.load(file)

extracted_data = find_structure_with_id_name(json_data)

csv_file = "mlb_id_name.csv"
with open(csv_file, mode='w', newline='') as file:
    fieldnames = ["id", "name"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for item in extracted_data:
        writer.writerow(item)

print("Dados exportados para o arquivo:", csv_file)
