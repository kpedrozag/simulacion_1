def algoritmo(a, s, ban, gran):
  c = [ 0.0 for i in range(len(a)) ]
  d = [ 0.0 for i in range(len(a)) ]
  g = [ 0.0 for i in range(len(a)) ]
  b = [ 0.0 for i in range(len(a)) ]

  i = 0

  while True:
    i += 1
    if i == len(a):
      break
    ai = a[i]
    if ai < c[i-1]:
      d[i] = c[i-1]-ai
    else:
      d[i] = 0.0
    si = s[i]
    c[i] = ai + d[i] + si
  n = i

  suma_r = 0
  suma_s = 0
  suma_d = 0
  suma_w = 0

  for i in range(1,len(a)):
    # print("Lancha " + str(i) + ":\ndi = " + str(d[i]) + "\tb[i] = " + str(b[i]) + "\tc[i] = " + str(c[i]))
    suma_r = suma_r + a[i] - a[i - 1]
    suma_s = suma_s + s[i]
    suma_d = suma_d + d[i]
    suma_w = suma_w + d[i] + s[i]


  print("\n")
  print("-----------------------------------------------------------")
  print("Promedio de tiempo entre llegada: " + str(suma_r / (n-1)) + "\n")

  print("Promedio de tiempo de servicio: " + str(suma_s / (n-1)) + "\n")

  print("Promedio de tiempo de espera: " + str(suma_d / (n-1)) + "\n")

  print("Promedio de tiempo de espera en el sistema: " + str(suma_w / (n-1)) + "\n")

  print("Para validar el modelo, los sgtes valores deben ser iguales: " + str(suma_w/(n-1)) + " = " + str(round((suma_d/(n-1)) + (suma_s/(n-1)), 1 )) + "\n")

  print("PROMEDIOS POR TIEMPO.\n\n")
  print("Numero de trabajos promedio en el sistema: " + str(round(suma_w/c[n-1], 3)) + "\n")

  print("Numero de trabajos promedio en la cola: " + str( round(suma_d/c[n-1], 3) ) + "\n")

  print("Numero de trabajos promedio en servicio: " + str(round(suma_s/c[n-1], 3)) + "\n")
  print("-----------------------------------------------------------")

def main():

  arrivals = [[1, 1, 1, 4, 4, 6, 6, 9, 10, 11, 11, 11, 11, 13, 13, 13, 13, 14, 22, 25, 25, 31, 33, 33, 34, 34, 35, 35, 37, 37, 37, 37, 38, 39, 39, 40], [1, 3, 4, 5, 5, 10, 10, 11, 11, 11, 11, 18, 18, 18, 18, 22, 25, 25, 25, 26, 27, 28, 39, 39, 39, 39, 41], [2, 9, 9, 10, 10, 10, 10, 11, 11, 14, 14, 20, 20, 21, 22, 23, 24, 25, 26, 28, 28, 29, 35, 36, 36, 36, 36, 38, 39, 42, 42, 42, 43, 43, 44], [1, 3, 4, 5, 5, 10, 10, 11, 11, 11, 15, 15, 15, 15, 16, 16, 16, 16, 19, 22, 22, 22, 23, 24, 25, 33, 33, 33, 33, 39], [7, 9, 13, 14, 14, 14, 14, 16, 18, 18, 19, 23, 28, 29, 32, 34, 34, 34, 35, 43, 43, 43], [10, 10, 11, 11, 11, 12, 17, 17, 21, 21, 21, 21, 24, 25, 26, 27, 28, 30, 31, 38, 39, 39, 39, 42, 43]]

  services = [[2, 2, 2, 2, 3, 2, 2, 2, 8, 2, 2, 2, 4, 2, 2, 2, 2, 3, 2, 2, 4, 2, 2, 2, 5, 3, 3, 2, 2, 2, 2, 2, 3, 2, 3, 2], [2, 4, 2, 4, 2, 2, 3, 2, 3, 2, 2, 2, 3, 2, 2, 2, 2, 3, 5, 4, 2, 3, 3, 3, 4, 7, 2], [3, 4, 2, 3, 2, 2, 2, 3, 4, 3, 3, 2, 2, 4, 3, 3, 3, 4, 2, 3, 2, 2, 4, 2, 4, 2, 4, 3, 3, 4, 2, 4, 5, 3, 2], [2, 4, 2, 4, 2, 2, 4, 2, 3, 2, 3, 3, 3, 2, 3, 2, 2, 2, 2, 3, 3, 5, 5, 2, 3, 3, 2, 2, 3, 3], [2, 4, 7, 2, 4, 3, 2, 3, 2, 2, 2, 2, 2, 4, 4, 2, 3, 2, 2, 2, 3, 2], [5, 2, 3, 2, 2, 2, 3, 4, 3, 2, 2, 2, 4, 3, 4, 4, 2, 4, 2, 4, 2, 4, 2, 3, 3] ]

  grande = 0
  print(len(arrivals), len(services))
  # for q in range(len(a_grande)):
  #   if q in {0, 1, 2}:
  algoritmo(arrivals[5], services[5], True, grande)

main()


"""
if q == 2:
        print("*************************\nGanancia proceso viejo = " + str(grande) + "\n*************************\n")
        grande = 0
    else:
      algoritmo(a_grande[q], s_grande[q], False, grande)
      if q == 5:
        print("*************************\nGanancia proceso nuevo = " + str(grande) + "\n*************************\n")
b[i] = a[i] + d[i]

    if flag:
      g[i] = 49
    else:
      g[i] = 37.4

    if d[i]>2:
      g[i] = g[i] -  5
    if c[i]>12:
      g[i] = g[i] - (c[i] - 12)*10


"""
