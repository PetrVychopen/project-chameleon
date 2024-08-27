import json

# Code maps
vehicle_type_map = {
    "0": "PERSONAL_VEHICLE",
    4: "MOTORCYCLE",
    2: "VAN",
    # You can add more vehicle type mappings here
}

fuel_type_map = {
    0: "BENZINE",
    1: "DIESEL",
    2: "ELETRIC",
    # You can add more fuel type mappings here
}

def map_value(code, mapping_dict):
    """Retrieves the string value associated with the given code from a mapping dictionary.
    
    Args:
        code (str): The code to look up in the mapping dictionary.
        mapping_dict (dict): A dictionary containing code-string value mappings.
    
    Returns:
        str: The string value associated with the code, or 'MISSING_MAPPING' if not found.
    """
    return mapping_dict.get(code, "MISSING_MAPPING")

# Define JSON data
json_1_data = {
    "vehicle": {
        "type": "0",
        "fuelType": 1
    }
}

# Define a template for the JSON structure we want to create
json_2_template = {
    "vehicle": {
        "type": "string",
        "fuelTypeCode": "string"
    }
}

# Restructure JSON 1 data to match JSON 2 format with error handling
json_2_data = json_2_template.copy() # To avoid modifying the original template
try:
    # Map the vehicle type code to its corresponding string value
    json_2_data["vehicle"]["type"] = map_value(json_1_data["vehicle"]["type"], vehicle_type_map)
    # Map the fuel type code to its corresponding string value
    json_2_data["vehicle"]["fuelTypeCode"] = map_value(json_1_data["vehicle"]["fuelType"], fuel_type_map)
except KeyError as e:
    print(f"Error: Missing key in JSON 1 data: {e}")

# Print the restructured JSON 2 data
print("JSON 2 Request with JSON 1 data:")
print(json.dumps(json_2_data, indent=2))
