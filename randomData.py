import json
from random import randint

nVehicles = 3
nWorkers = 4
nTrips = 10
upperBoundBenefit = 70
lowerBoundBenefit = 30
upperBoundDepretiation = 30
upperBoundDuration = 3600
lowerBoundDuration = 900


trips = [randint(lowerBoundDuration, upperBoundDuration) for i in range(nTrips)]

benefit = [[randint(lowerBoundBenefit, upperBoundBenefit) for i in range(nTrips)] for j in range(nVehicles)]

depreciation = [[randint(0, upperBoundDepretiation) for i in range(nVehicles)] for j in range(nWorkers)]

workerHours = [[randint(0, 57600)] for i in range(nWorkers)]
for hours in workerHours:
  hours.append(hours[0] + 28800)



with open('data.json', 'w') as jsonF:
  json.dump({
    'numberTrips': nTrips,
    'numberWorkers': nWorkers,
    'numberVehicles': nVehicles,
    'durations': trips,
    'benefit': benefit,
    'depreciation': depreciation,
    'workerHours': workerHours
  }, jsonF)