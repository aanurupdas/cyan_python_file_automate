import json

from utility.parse_txt_file import parse_txt_file
from utility.parse_csv_file import parse_csv_file

input_file = input("Enter File : ")
output_file = "./products.json"

def dump_to_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if input_file.endswith(".txt"):
    parsed_data,errors = parse_txt_file(input_file) 
else:
    parsed_data, errors = parse_csv_file(input_file)

if not errors:
    print(parsed_data)
    dump_to_json(parsed_data, output_file)
    print(f"Data from {input_file} has been parsed and dumped to {output_file}")
else:
    print(f"{errors[0]}")