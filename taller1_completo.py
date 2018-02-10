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

  gg = 0

  flag = ban;

  suma_r = 0
  suma_s = 0
  suma_d = 0
  suma_w = 0

  for i in range(1,len(a)):
    b[i] = a[i] + d[i]

    if flag:
      g[i] = 49
    else:
      g[i] = 37.4

    if d[i]>2:
      g[i] = g[i] -  5
    if c[i]>12:
      g[i] = g[i] - (c[i] - 12)*10

    gg = gg + g[i]

    print("Lancha " + str(i) + ":\ndi = " + str(d[i]) + "\tb[i] = " + str(b[i]) + "\tc[i] = " + str(c[i]) + "\nGanancia = " + str(g[i]) + "\n")

    suma_r = suma_r + a[i] - a[i - 1]
    suma_s = suma_s + s[i]
    suma_d = suma_d + d[i]
    suma_w = suma_w + d[i] + s[i]


  print("Ganancia neta del dia: " + str(gg))
  gran = gran + gg
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


def main():
  a_grande = [ [0,0,1,4,4,5,7,9], [0,2,3,3,5,6,8,10], [0,0,1,2,3,4,7,8,10], [0,0,1,1,3,3,4,6,8,9], [0,0,0,3,3,5,5,7,7,8,9], [0,1,1,1,3,3,5,6,7,9] ]

  s_grande = [ [0,2,1,2,1,1,3,2], [0,1,2,3,1,2,1, 2], [0,1,2,3,1,2,1,1, 1], [0,1,2,1,1,3,1,1,1,1], [0,1,1,1,1,1,1,1,1,2,1], [0,2,1,1,1,1,1,2,1,2] ]
  grande = 0
  for q in range(len(a_grande)):
    if q in {0, 1, 2}:
      algoritmo(a_grande[q], s_grande[q], True, grande)
      if q == 2:
        print("*************************\nGanancia proceso viejo = " + str(grande) + "\n*************************\n")
        grande = 0
    else:
      algoritmo(a_grande[q], s_grande[q], False, grande)
      if q == 5:
        print("*************************\nGanancia proceso nuevo = " + str(grande) + "\n*************************\n")


main()
