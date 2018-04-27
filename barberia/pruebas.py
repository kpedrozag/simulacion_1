import numpy as np


def arrival_clients_hour(x):
    # x = true -> jornada de la mañana 7-11
    # x = false -> jornada de la tarde 2-5
    return np.random.poisson(3, 4) if x else np.random.poisson(3, 3)


def service_time():
    return int(round(np.random.normal(20, 2.4), 0))


def simulacion():
    hour = 0
    clients = []  # lista de clientes que llegan

    number_clients = arrival_clients_hour(True)  # lista de num de clientes x hora
    for cls in number_clients:
        aux = []
        for cl in range(cls):
            aux.append(service_time())
        clients.append(aux)
        hour += 1
    for k, v in enumerate(clients):
        print(k, v, end="\t")
    print()
    ac = 0
    aux = []
    pasan = []
    pos = 0
    for i, valor in enumerate(clients):
        flag = False
        ac = 0
        for j in valor:
            ac += j
            if ac > 60:
                pos = valor.index(j)
                flag = True
                break
        if flag:
            actual = valor[pos:]
            sobrante = valor[:pos]
            div = 60 - sum(actual)
            actual.append(div)
            sobrante[0] = sobrante[0] - div
            clients[i] = actual
            if not i+1 == len(clients):
                clients[i+1] = sobrante + clients[i+1]
            else:
                pasan = sobrante
            print(clients)

    print(clients, pasan)


simulacion()
