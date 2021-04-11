def grafico_linha(x, g, y, name, improvement):
    from matplotlib import pyplot as plt
    plt.rcParams['figure.figsize'] = [12, 8]
    plt.plot(x, y, color='blue',
             label='Evolução ao longo das iterações', linewidth=3)
    plt.plot(x, g, color='red',
             label='Média da função fitness ao longo das iterações', linewidth=3)
    # plt.title(f'Evolução ao longo das iterações\nPercentual de melhora: {improvement}%', size='x-large')
    plt.xlabel('Iterações', size='x-large')
    plt.ylabel('Função lucro', size='x-large')
    plt.legend(loc='best', fontsize='large')
    plt.xticks(size='large')
    plt.yticks(size='large')
    plt.savefig(name)
    plt.close()

def grafico_improvement(x, y, name):
    from matplotlib import pyplot as plt
    plt.rcParams['figure.figsize'] = [12, 8]
    plt.plot(x, y, color='blue',
             label='Evolução da melhora ao longo das iterações', linewidth=3)
    # plt.title(f'Evolução ao longo das iterações\nPercentual de melhora: {improvement}%', size='x-large')
    plt.xlabel('Iterações', size='x-large')
    plt.ylabel('Melhora acumulada (%)', size='x-large')
    plt.legend(loc='best', fontsize='large')
    plt.xticks(size='large')
    plt.yticks(size='large')
    plt.savefig(name)
    plt.close()


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
