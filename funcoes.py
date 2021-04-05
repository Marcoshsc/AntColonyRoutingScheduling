def objective(solucao, tripInfo):
    maior = -1
    for s in solucao:
        rota = solucao[0]
        inicio = solucao[2]
        duracao = tripInfo[rota] + inicio
        if duracao > maior:
            maior = duracao
    return maior


def getFreeVehicle(vehicles):
    for v in range(vehicles):
        if vehicles[v] == True:
            return v
    return None


def getFreeWorker(workers):
    for w in range(workers):
        if workers[w] == True:
            return w
    return None