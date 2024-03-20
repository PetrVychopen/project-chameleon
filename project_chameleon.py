import json

# Define mapping JSON 1 : JSON 2
def get_vehicle_type_string(code):
  code_map = {
    10: "TRUCK"
    # Add other code mappings here
  }
  return code_map.get(code, "UNKNOWN")

# Define of JSON 1 (old structure)
json_1 = {
  "vehicle": {
    "type": 10,
    "manufacturerModelId": "054700",
    "manufacturer": "Iveco",
    "model": "Magirus",
    "code": 5,
    "usePurpose": 1,
    "manufactureYear": 1999,
    "countPlace": 2,
    "maxWeight": 26000,
    "enginePower": 221,
    "engineDisplacement": 9500,
    "leadinDate": "1999-01-06",
    "vin": "WJME2NMT00C057419",
    "fuelType": 1,
    "securityLevel": 0,
    "registrationPlate": "LNH9785",
    "registrationBookNumber": ""
  }
}

# Define JSON 2 (new structure)
json_2 = {
  "vehicle": {
    "registrationPlate": "7J8755",
    "type": "PERSONAL_VEHICLE",
    "category": "M1",
    "enginePower": 110,
    "engineDisplacement": 750,
    "maxWeight": 380,
    "actualValueVATIncluded": True,
    "usePurposeCode": "COMMON",
    "securityLevel": [
      "NO_SECURITY"
    ],
    "registrationBookNumber": "UI560344",
    "vin": "JS1CW111100101065",
    "countPlace": 5,
    "fuelTypeCode": "BENZINE",
    "leadinDate": "2009-04-30",
    "leadinDateInFuture": False,
    "manufacturerModelCode": "SUZUKI_OTHER",
    "model": "GSX-R750",
    "manufacturer": "Suzuki"
  }
}

# Restructure data to match JSON 2 format
json_2["vehicle"]["type"] = json_1["vehicle"]["type"]

# Do mapping JSON 1 : JSON 2
vehicle_type_code = json_1["vehicle"]["type"]
vehicle_type_string = get_vehicle_type_string(vehicle_type_code)
json_2["vehicle"]["type"] = vehicle_type_string

# Print the restructured JSON 2 data
print(json.dumps(json_2, indent=2))