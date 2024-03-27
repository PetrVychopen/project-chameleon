import json

# Define mapping JSON 1 : JSON 2
def get_vehicle_type_string(code):
  vehicle_type_map = {
    1: "PERSONAL_VEHICLE",
    # Add other code mappings here
  }
  return vehicle_type_map.get(code, "UNKNOWN")

def get_fuel_type_string(code):
  fuel_type_map = {
    1:"PETROL",
    # Add other code mappings here
  }
  return fuel_type_map.get(code, "UNKNOWN")

# Define of JSON 1 (old structure)
json_1 = {
  "vehicle": {
    "type": 1,
    "fuelType": 1
  }
}

# Define JSON 2 (new structure)
json_2 = {
  "vehicle": {
    "type": "string",
    "fuelTypeCode": "string"
  }
}

# Restructure data to match JSON 2 format
json_2["vehicle"]["type"] = json_1["vehicle"]["type"]
json_2["vehicle"]["fuelTypeCode"] = json_1["vehicle"]["fuelType"]

# Do mapping JSON 1 : JSON 2
vehicle_type_code = json_1["vehicle"]["type"]
fuel_type_code = json_1["vehicle"]["fuelType"]

vehicle_type_string = get_vehicle_type_string(vehicle_type_code)
fuel_type_string = get_fuel_type_string(fuel_type_code)

json_2["vehicle"]["type"] = vehicle_type_string
json_2["vehicle"]["fuelTypeCode"] = fuel_type_string

# Print the restructured JSON 2 data
print(f"JSON 2 Request with JSON 1 data:")
print(json.dumps(json_2, indent=2))