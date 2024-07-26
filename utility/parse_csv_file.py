import csv

def parse_csv_file(file_path):
    parsed_data = []
    errors = []
    try:
        with open(file_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            header = next(csvreader)

            for row_number, row in enumerate(csvreader, start=2):
                try:
                    # Validate and convert fields
                    # ProductID in int
                    if row[0].__ne__(""):
                        row[0] = int(row[0])
                    else:
                        raise ValueError("Missing ProductID")      

                    # Name in string
                    if row[1].__ne__(""):
                        row[1] = str(row[1])
                    else:
                        raise ValueError("Missing ProductName")     
                    
                    # Price in float
                    if row[2] not in ["","$"]:
                        row[2] = float(row[2].replace("$",""))
                    else:
                        raise ValueError("Missing Price")
                    
                    # Stock in string
                    if row[3] not in ['Yes', 'No']:
                        raise ValueError("InStock must be 'Yes' or 'No'")
                    
                    parsed_data.append(row)

                except ValueError as ve:
                    errors.append(f"ValueError at row {row_number}: {ve}")
                except Exception as e:
                    errors.append(f"Exception at row {row_number}: {e}")

            parsed_data = [{key: value for key, value in zip(header, values)} for values in parsed_data]

    except FileNotFoundError:
        errors.append(f"The file '{file_path}' was not found.")   
    except Exception as e:
                    errors.append(f"An unexpected error occurred: {e}")             
    return parsed_data, errors