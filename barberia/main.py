import numpy as np
import queue


class Client:

    arrival_t = 0
    service_t = 0

    def __init__(self, at, st):
        self.arrival_t = at
        self.service_t = st


class Barber:
    busy = None
    # busy = True: ocupado
    # busy = False: no ocupado

    def are_busy(self):
        if self.busy:
            return self.busy # ocupado
        else:
            return self.busy # no ocupado

    def set_busy(self, oc):
        self.busy = oc


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
        for cl in range(cls):
            clients.append(Client(hour, service_time()))
        hour += 1

    asientos = queue.Queue(5)  # cola con 5 asientos
    barber = Barber()  # barbero que esta o no ocupado
    barber.set_busy(False)  # el barbero no esta ocupado al principio

    i = 0
    while True:

        if number_clients[i] > 0 or (number_clients == 0 and not asientos.empty()):


        minuto = 0




















"""
def simulacion():
    hour = 0
    clientes = [] # lista de clientes que llegan
    number_clients = arrival_clients_hour(True) # lista de num de clientes x hora
    for cls in number_clients:
        for cl in range(cls):
            clientes.append(Client(hour, service_time()))
        hour += 1

    cc = 1
    print(number_clients)
    for i in clientes:
        print("cliente", cc, "llega en hora ", i.arrival_t, "se atiende en ", i.service_t, "minutos")
        cc += 1

    asientos = queue.Queue(5)  # cola con 5 asientos
    barber = Barber()  # barbero que esta o no ocupado
    barber.set_busy(False)  # el barbero no esta ocupado al principio

    hour_counter = 0  # contador que lleva las horas
    it = 0
    while True:
        if hour_counter < 4:
            if number_clients[it] > 0 or (number_clients[it] == 0 and not asientos.empty()):
                pass

simulacion()
"""
