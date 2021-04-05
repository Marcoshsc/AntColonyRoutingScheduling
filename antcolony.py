import json
import random
from funcoes import objective

data = dict

with open('data.json', 'r') as jsFile:
    data = json.loads(jsFile.read())

beta = data['beta']
alpha = data['alpha']
p = data['p']
n_max = data['n_max']
vehicles = []

for trip in data['trips']:
    if trip['vehicle'] not in vehicles:
        vehicles.append(trip['vehicle'])

vehicleTrips = [[] for v in vehicles]

trips = [t for t in data['trips']]

for trip in data['trips']:
    vehicleTrips[trip['vehicle'] - 1].append(trip)

workers = [w for w in data['workers']]


#print(trips)
#print(vehicles)
#print(workers)

n_iter = 0
n_ants = len(trips)
while n_iter < n_max:
    solutions = []
    for i in range(n_ants):
        solution = [] # solucao da formiga
        vehicleStatus = [False for v in vehicles]
        workerStatus = [False for w in workers]
        attendedRoutes = [False for t in trips]

        for w in workers:
            vehicle = getFreeVehicle(vehicleStatus)
            if vehicle is None: # Sem veiculo livre
                continue

            trip = vehicleTrips[vehicle][random.randint(0, len(vehicleTrips[vehicle]))]
            
            if attendedRoutes[trip['sequencial']]:   
                continue
                
            attendedRoutes[trip] = True
            workerStatus[trip] = True
            solution.append(trip)
            print(solution)

            

            
        

    n_iter += 1
