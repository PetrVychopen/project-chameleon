import json

# Code maps
vehicle_type_map = {
    1: "PERSONAL_VEHICLE",
    # Add other vehicle type mappings here
}

fuel_type_map = {
    1: "PETROL",
    # Add other fuel type mappings here
}

def get_mapped_value(code, mapping_dict):
    """Maps a code to its corresponding string value using a specified 
    mapping dictionary."""
    return mapping_dict.get(code, "UNKNOWN")

# Define JSON data
json_1_data = {
    "vehicle": {
        "type": 1,
        "fuelType": 1
    }
}

json_2_template = {
    "vehicle": {
        "type": "string",
        "fuelTypeCode": "string"
    }
}

# Restructure JSON 1 data to match JSON 2 format with error handling
json_2_data = json_2_template.copy() # To avoid modifying the original template
try:
    json_2_data["vehicle"]["type"] \
      = get_mapped_value(json_1_data["vehicle"]["type"], vehicle_type_map)
    json_2_data["vehicle"]["fuelTypeCode"] \
      = get_mapped_value(json_1_data["vehicle"]["fuelType"], fuel_type_map)
except KeyError as e:
    print(f"Error: Missing key in JSON 1 data: {e}")

# Print the restructured JSON 2 data
print(f"JSON 2 Request with JSON 1 data:")
print(json.dumps(json_2_data, indent=2))