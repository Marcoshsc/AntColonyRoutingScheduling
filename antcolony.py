from random import randint, random
import operator
from funcoes import grafico_linha, grafico_improvement

def fitness(solution, pairsWeight):
  return sum([pairsWeight[s[1]][s[0]] for s in solution])

def antColony(nTrips, nVehicles, nWorkers, durations, depreciation, benefit):

  # nAnts = nTrips
  # nIter = 10
  # pheromonyInfluence = 2
  # weightInfluence = 10
  # amountPheromony = (sum(durations) * 100) / len(durations)
  # evaporationRate = 0.9

  nAnts = nTrips
  nIter = 200
  pheromonyInfluence = 0.1
  weightInfluence = 10
  amountPheromony = (sum(durations) / len(durations)) * 100
  evaporationRate = 0.8

  best = list
  improveAmount = []
  lucros = []
  media = []
  best_solution = []
  pairs = [[i, j] for i in range(nVehicles) for j in range(nWorkers)]
  # pairsWeight = [max([sum([benefit[j][k] - depreciation[i][j] for k in range(nTrips)]), 0]) for i in range(nWorkers) for j in range(nVehicles)]
  # pairsWeight = [sum([benefit[j][k] - depreciation[i][j] for k in range(nTrips)]) for i in range(nWorkers) for j in range(nVehicles)]
  pairsWeight = [[benefit[el[0]][k] - depreciation[el[1]][el[0]] for k in range(nTrips)] for el in pairs]

  # print(len(pairsWeight[0]))
  # print(pairsWeight)
  # pairsWeightSum = (sum(pairsWeight) * weightInfluence) / len(pairsWeight)
  pairsWeightSum = [sum(pairsWeight[i]) for i in range(len(pairsWeight))]
  # greaterPairsWeight = [max(pairsWeight[i]) for i in range(len(pairsWeight))]
  # print(pairsWeightSum)
  pheromony = [[0 for i in range(nTrips)] for j in range(len(pairs))]
  #print(pheromony)
  it = 0
  itNoBetter = 0
  while itNoBetter < nIter:
    solutions = []
      # totalPheromony = sum([sum(p) / pheromonyInfluence for p in pheromony]) / len(pheromony)
    totalPheromony = [sum(p) for p in pheromony]
    # print(totalPheromony)
    # greaterPheromony = [max(p) for p in pheromony]
    for ant in range(nTrips):
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
            currentPair = randint(0, len(pairs) - 1)
            continue
          # print(currentPair, visitedTrips, len(pairsWeight))
          # print(pheromony[currentPair][visitedTrips] * pheromonyInfluence + pairsWeight[currentPair][visitedTrips] * weightInfluence, totalPheromony[currentPair] + pairsWeightSum[currentPair])
          # print(pheromony[currentPair][visitedTrips] * pheromonyInfluence, pairsWeight[currentPair][visitedTrips] * weightInfluence, totalPheromony[currentPair] + pairsWeightSum[currentPair])
          # print(max([greaterPheromony[currentPair] ** pheromonyInfluence, 1]) * (greaterPairsWeight[currentPair] ** weightInfluence))
          # print(max([pheromony[currentPair][visitedTrips] ** pheromonyInfluence, 1]) * (pairsWeight[currentPair][visitedTrips] ** weightInfluence))
          # print('here')
          prob = ((pheromony[currentPair][visitedTrips] * pheromonyInfluence) + (pairsWeight[currentPair][visitedTrips] * weightInfluence)) / ((totalPheromony[currentPair]) + (pairsWeightSum[currentPair]))
          # print('hereafter')
          # if prob < 0.1:
          #   prob = 0.1
          # print(prob)
          realProb = random()
          # print(prob)
          # realProb /= realProb / 10
          #print((prob, realProb))
          if realProb < prob:
            # print(realProb, prob)
            selectedPair = currentPair
            workerTimes[worker] += durations[visitedTrips]
          # print(realProb, prob)
          # amount += 1
          # if(amount % 100 == 0):
          #   print(amount)
          currentPair = (currentPair + 1) % len(pairs)
        solution.append([numberVisited, selectedPair])
        visitedTrips = (visitedTrips + 1) % nTrips
        numberVisited += 1
      solutions.append(solution)
    fitnesses = [fitness(s, pairsWeight) for s in solutions]
    mediaAtual = sum(fitnesses) / len(fitnesses)
    visitedTripAndPairs = set()
    for solution in solutions:
      for unit in solution:
        # pheromony[unit[1]][unit[0]] *= evaporationRate
        pheromony[unit[1]][unit[0]] += amountPheromony / durations[unit[0]]
        visitedTripAndPairs.add(f'{unit[0]}-{unit[1]}')
    for t in range(nTrips):
      for p in range(len(pairs)):
        if f'{t}-{p}' not in visitedTripAndPairs:
          pheromony[p][t] *= evaporationRate

    if it == 0:
      best = max(fitnesses)
      best_0 = best
      improveAmount.append(0)
    else:
      bestResult = max(fitnesses)
      if best < bestResult:
        ratio = (100 * (bestResult / best)) - 100
        best = bestResult
        improveAmount.append(improveAmount[-1] + ratio)
        for c in range(len(solutions)):
          f = fitness(solutions[c], pairsWeight)
          if f == best:
            best_solution = solutions[c]
        itNoBetter = 0
      else:
        improveAmount.append(improveAmount[-1])
        itNoBetter += 1
    it += 1
    media.append(mediaAtual)
    lucros.append(best)
    print(f'Best fitness: {best}')
    print(f'Média: {mediaAtual}')

  print('\n')
  #print('Solução obtida: ')
  #print(best_solution)
  best_final = fitness(best_solution, pairsWeight)
  print(f'Lucro total: {best_final}')
  improvement = (best_final / best_0) - 1
  print(f'Percentual de melhora ao longo das iterações: {improvement*100}%')
  grafico_linha(range(it),media, lucros, 'lucro_total_iteracoes', improvement*100)
  grafico_improvement(range(it), improveAmount, 'improvement_percentage')
  # print(improveAmount)
  return best_final, improvement*100
  #print(pheromony)
