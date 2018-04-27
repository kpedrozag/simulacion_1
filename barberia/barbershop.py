import numpy
from Services import Services
#import scipy.stats as stats

# Para las llegadas se generaran numeros aleatorios que se comporten con una distribucion Poisson con lambda 5

chairs = 5
horas = 4


def getArrivals():
    data = []
    for i in range(horas):
        data.append(numpy.random.poisson(3))

    return data


def getServices():
    data2 = []
    for i, clientes in enumerate(data):
        c2 = []
        for c in range(clientes):
            c2.append(int(numpy.random.normal(20, 2.4)))
        servicio = Services()
        servicio.save_servicio(c2)
        # print(servicio.tiempo_llegada, servicio.tiempo_servicio)
    return servicio


def checkChairs(array):
    count1 = 0
    count2 = 0
    # Ciclo para recorrer cada hora del sistema
    for i in range(len(array)):

        if (array[i] >= 5):

            count1 += array[i] - 5
            if (count1 > chairs):
                count2 = count1 - chairs

        # print("checkChairs", count2, count1 - count2)
    return count2, count1 - count2


def meanGetter(array):
    sum = 0.0
    for i in range(len(array)):
        sum = sum + array[i]

    return sum / len(array)


def make_queue(queue):
    c = [0.0 for i in range(len(queue))]
    tp = []
    l = []
    acum = 0
    j = 0
    while j < len(queue):
        tp = l.copy()
        l.clear()
        if sum(tp) <= 60:
            s = True
            for k in queue[j]:
                acum += k
                if acum <= 60:
                    tp.append(k)
                else:
                    if s:
                        h = acum - 60
                        tp.append(k - h)
                        l.append(h)
                        s = False
                    else:
                        l.append(k)
        else:
            acum = 0
            g = tp.copy()
            tp.clear()
            s = True
            for k in g:
                acum += k
                if acum <= 60:
                    tp.append(k)
                else:
                    if s:
                        h = acum - 60
                        tp.append(k - h)
                        l.append(h)
                        s = False
                    else:
                        l.append(k)

        if len(l) == 0:
            c[j] = tp.copy()
        elif j == len(queue) - 1:
            c[j] = tp.copy() + l.copy()
        else:
            c[j] = tp.copy()

        acum = acum - sum(tp)
        tp.clear()
        j += 1

    return c
#-------------------------------------------------------------------------------------------------------------


promDelay = []
promServices = []
promWaits = []
promInter = []

for i in range(1):

    print("Llegada de Clientes")
    data = getArrivals()

    print(data)

    print("Servicios: ")
    data2 = getServices()
    print(data2.servicios)
    cola = make_queue(data2.servicios)
    print(cola)
    ultimos = make_queue([cola[len(cola)-1]] + [[0] for PP in range(len(cola)-1)])
    print(ultimos)
    a = []  # Arreglo de llegadas para usar en el algoritmo
    s = []  # Arreglo de servicios para usar en el algoritmo
    c = []  # arreglo de partida de las personas
    d = []  # arreglo de delays
    r = []  # arreglo de interarrivals

    cola = numpy.zeros(5)
    sobran = []

    for j,num_clientes in enumerate(data):
        atendidos = 0
        en_cola = 0
        si = 0.0  # Variable that collects services sum
        di = 0.0  # Variable that collects delays sum
        w = 0.0  # Variable that collects wait sum
        ri = 0.0  # Variable that collects r sum
        sum_temp = 0.0

        if num_clientes > 6:
            c.append(num_clientes - 5)
            cola = data2.servicios[j][:6:1]
            sobran = data2.servicios[j][7:]
        else:
            cola = data2.servicios[j]

        tam_cola = len(cola)
        temp_cola = cola[:]
        sobrantes = []
        for k,tiempo_servicio in enumerate(temp_cola):
            print("Hay " + str(tam_cola - k) + " clientes a atender")
            sum_temp = si + tiempo_servicio
            print("sump_temp", sum_temp)
            if sum_temp < 60.0:
                si += tiempo_servicio
                atendidos += 1
                print("se atendió el cliente y nos demoramos: " + str(tiempo_servicio))
                print("hemos atendido: " + str(atendidos) + " y faltan " + str(tam_cola - atendidos))
                print("en total nos demoramos " + str(si) + " y nos falta " + str(60.0 - si))
                print("podemos quitar", cola[k])
                # del cola[k]
            else:
                en_cola += 1
                print("ya pasó la hora y quedan " + str(en_cola) + " en cola")
                print("queda en cola", cola[k])
                # print("else", en_cola)

                print(j,num_clientes,k,tiempo_servicio, si, cola, atendidos, en_cola)
        print("-----------------------")
