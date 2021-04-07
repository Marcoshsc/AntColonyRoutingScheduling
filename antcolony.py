<<<<<<< HEAD
from random import randint, random

def fitness(solution, pairsWeight):
  return sum([pairsWeight[s[1]] for s in solution])

def antColony(nTrips, nVehicles, nWorkers, durations, depreciation, benefit):

  nAnts = nTrips
  nIter = 50
  pheromonyInfluence = 0.5
  weightInfluence = 0.5
  amountPheromony = 100000
  evaporationRate = 0.1

  best = list
  pairs = [[i, j] for i in range(nVehicles) for j in range(nWorkers)]
  # pairsWeight = [max([sum([benefit[j][k] - depreciation[i][j] for k in range(nTrips)]), 0]) for i in range(nWorkers) for j in range(nVehicles)]
  pairsWeight = [sum([benefit[j][k] - depreciation[i][j] for k in range(nTrips)]) for i in range(nWorkers) for j in range(nVehicles)]

  # pairsWeightSum = (sum(pairsWeight) * weightInfluence) / len(pairsWeight)
  pairsWeightSum = (sum(pairsWeight)) / len(pairsWeight)
  # print(pairsWeight)

  pheromony = [[0 for i in range(nTrips)] for j in range(len(pairs))]
  # print(pheromony)
  it = 0
  itNoBetter = 0
  while itNoBetter < 50:
    solutions = []
      # totalPheromony = sum([sum(p) / pheromonyInfluence for p in pheromony]) / len(pheromony)
    totalPheromony = sum([sum(p) for p in pheromony]) / len(pheromony)
    for ant in range(nAnts):
      # print(ant)
      workerTimes = [0 for i in range(nWorkers)]
      solution = []
      visitedTrips = 0
      numberVisited = 0
      while numberVisited < nTrips:
        duration = durations[visitedTrips]

        selectedPair = None
        currentPair = randint(0, len(pairs) - 1)
        amount = 0
        while selectedPair is None:
          pair = pairs[currentPair]
          worker = pair[1]
          vehicle = pair[0]
          if workerTimes[worker] + durations[visitedTrips] > 28800:
            print(f'{worker} hours is complete')
            continue
          # print(currentPair, visitedTrips, len(pairsWeight))
          prob = (pheromony[currentPair][visitedTrips] * pheromonyInfluence + pairsWeight[currentPair] * weightInfluence) / (totalPheromony + pairsWeightSum)
          realProb = random()
          if realProb < prob:
            selectedPair = currentPair
            workerTimes[worker] += durations[visitedTrips]
          # print(realProb, prob)
          # amount += 1
          # if(amount % 100 == 0):
          #   print(amount)
          currentPair = (currentPair + 1) % len(pairs)
        
        solution.append([visitedTrips, selectedPair])
        visitedTrips = (visitedTrips + 1) % nTrips
        numberVisited += 1
      solutions.append(solution)
    fitnesses = [fitness(solution, pairsWeight) for s in solutions]
    visitedTripAndPairs = set()
    for solution in solutions:
      for unit in solution:
        pheromony[unit[1]][unit[0]] += amountPheromony / durations[unit[0]]
        visitedTripAndPairs.add(f'{unit[0]}-{unit[1]}')
    for t in range(nTrips):
      for p in range(len(pairs)):
        if f'{t}-{p}' not in visitedTripAndPairs:
          pheromony[p][t] *= evaporationRate

    if it == 0:
      best = max(fitnesses)
    else:
      bestResult = max(fitnesses)
      if best < bestResult:
        best = bestResult
        itNoBetter = 0
      else:
        itNoBetter += 1
    it += 1
    print(f'Best fitness: {best}')

  print(pheromony)
=======
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
>>>>>>> 9c33fe65696da9ee6a40dfd3a8b56e877ed5304e
