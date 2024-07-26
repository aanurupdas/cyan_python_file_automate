def parse_txt_file(file_path):
    parsed_data = []
    errors = []

    try:
        with open(file_path, 'r') as txtfile:
            content = txtfile.read().strip()
            blocks = content.split('\n\n')
            
            for i, block in enumerate(blocks, start=1):
                try:
                    lines = block.split('\n')
                    data = {}
                    
                    for line in lines:
                        key, value = line.split(': ', 1)
                        data[key] = value
                        
                    # Validate and convert fields
                    # ProductID in int                
                    if data['ProductID'].__ne__(""):
                        data['ProductID'] = int(data['ProductID'])
                    else:
                        raise ValueError("Missing ProductID")
                    
                    # Name in string
                    if data['Name'].__eq__(""):
                        raise ValueError("Missing Name")
                    
                    # Price in float
                    if data['ProductID'].__ne__(""):
                        data['Price'] = float(data['Price'].strip('$'))
                    else:
                        raise ValueError("Missing Price") 
                    
                    # Stock in string      
                    if data['InStock'] not in ['Yes', 'No']:
                        raise ValueError("InStock must be 'Yes' or 'No'")
                    
                    parsed_data.append(data)
                
                except ValueError as ve:
                    errors.append(f"ValueError at block {i}: {ve}")
                except Exception as e:
                    errors.append(f"Exception at block {i}: {e}")

    except FileNotFoundError:
        errors.append(f"The file '{file_path}' was not found.")
    except Exception as e:
        errors.append(f"An unexpected error occurred: {e}")
    return parsed_data, errors