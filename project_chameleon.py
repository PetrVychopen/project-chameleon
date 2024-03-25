import json

# Define mapping JSON 1 : JSON 2
def get_vehicle_type_string(code):
  vehicle_type_map = {
    1: "MOTORCYCLE",
    2: "MOTORCYCLE",
    3: "MOTORCYCLE",
    4: "PERSONAL_VEHICLE",
    5: "MOTOR_CARAVAN",
    6: "AMBULANCE",
    7: "SEMITRAILER_TRUCK",
    8: "TBD",
    9: "TBD",
    10: "TBD",
    11: "TRACTOR",
    12: "SINGLE_WHEEL_TRACTOR",
    13: "13	PUBLIC_TRANSPORT_BUS",
    14: "TROLLEY_BUS",
    15: "BUS",
    16: "BUS",
    17: "TRAILER",
    18: "TRAILER",
    19: "SEMITRAILER",
    20: "TRUCK",
    21: "TBD",
    # Add other code mappings here
  }
  return vehicle_type_map.get(code, "UNKNOWN")

def get_use_purpose_string(code):
  use_purpose_map = {
    0:"COMMON",
    1:"SPECIAL",
    2:"TAXI",
    3:"RENT",
    4:"BUSINESS",
    5:"ADR",
    6:"HISTORICAL",
    7:"DRIVING_SCHOOL",
    8:"OTHER",
    # Add other code mappings here
  }

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
json_2["vehicle"]["fuelTypeCode"] = json_1["vehicle"]["fuelType"]

# Do mapping JSON 1 : JSON 2
vehicle_type_code = json_1["vehicle"]["type"]
use_purpose_code = json_1["vehicle"]["fuelType"]

vehicle_type_string = get_vehicle_type_string(vehicle_type_code)
use_purpose_string = get_vehicle_type_string(vehicle_type_code)

json_2["vehicle"]["type"] = vehicle_type_string
json_2["vehicle"]["fuelTypeCode"] = use_purpose_string

# Print the restructured JSON 2 data
print(f"JSON 2 Request with JSON 1 data:")
print(json.dumps(json_2, indent=2))