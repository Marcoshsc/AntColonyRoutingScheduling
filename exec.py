import json
from antcolony import antColony


data = {}

with open('data.json', 'r') as jsonF:
  data = json.loads(jsonF.read())

antColony(data['numberTrips'], data['numberVehicles'], data['numberWorkers'], data['durations'], data['depreciation'], data['benefit'])