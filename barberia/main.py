import numpy as np
import queue


class Client:

    arrival_t = 0
    service_t = 0

    attended = False
    attending = False

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

    asientos = queue.Queue(5)  # cola con 5 asientos. inicialmente vacia
    barber = Barber()  # barbero
    barber.set_busy(False)  # el barbero no esta ocupado al principio
    desertores_on = []
    desertores_off = []
    minutos = 0
    it_c = 0
    acu_max = 0
    while True:
        hora = int(minutos/60)
        if hora < 4:
            if not barber.are_busy():
                barber.set_busy(True)
                max_service = clients[it_c].service_t
                clients[it_c].attending = True
                acu_max += max_service
            else:
                try:
                    asientos.put(clients[it_c], block=False)
                except queue.Full:
                    desertores_on.append(clients[it_c])
            if barber.are_busy() and minutos == acu_max:
                pass
        else:
            desertores_off.append(clients[it_c])
        minutos += 1









































"""
    minutes = 0  # cuenta minuto por minuto
    hour_lapse = 0
    # current_hour = 0

    while True:
        current_hour = int(minutes / 60)
        if current_hour == hour_lapse:
            hour_lapse += 1




        if current_hour < 4:

            if number_clients[current_hour] > 0 or (number_clients[current_hour] == 0 and not asientos.empty()):

                if (not barber.are_busy()) and asientos.empty():

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
