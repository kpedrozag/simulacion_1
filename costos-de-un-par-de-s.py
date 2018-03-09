def main(s, S):
  # Comienza en t = 0
  # Nivel inicial y final de inventario es 'S'

  # cantidad demandada durante un intervalo
  # d = [0, 30, 15, 25, 15, 45, 30, 25, 15, 20, 35, 20, 30]
  d = [0, 100, 57, 49, 81, 40, 99, 114, 74, 108, 63, 30, 85, 121, 35, 92, 89, 56, 62, 44, 76, 28, 32, 77, 101, 95, 66, 57, 81, 32, 45]

  # niveles de inventario
  # donde l[i-1] es el nivel de inventario al comienzo del intervalo i
  l = [0 for i in range( len(d) )]

  # cantidad ordenada
  # o[i-1] es la cantidad ordenada al proveedor en el tiempo t = i-1 (será >= 0)
  o = [0 for i in range( len(d) )]

  # s, S = 40, 450

  l[0] = S

  i = 0
  while True:

    i = i + 1
    if i == len(d):
      break

    if l[i-1] < s:
      o[i-1] = S - l[i-1]
    else:
      o[i-1] = 0

    l[i] = l[i-1] + o[i-1] - d[i]

  n = i-1
  o[n] = S - l[n]
  l[n] = S

  #for i in range(1, len(d)):
  #  print("En intervalo", i, "inventario inicial:", l[i-1], "se ordenaron", o[i-1], "\n")

  aux = 0
  aux2 = 0

  for i in range(len(d)):
    aux = aux + d[i]
    aux2 = aux2 + o[i]

  d_prom = aux / n
  o_prom = aux2 / n

  #print("Promedio de demandas:\t", round(d_prom, 2), "\nPromedio de ordenes:\t", round(o_prom, 2), "\n")

  l_p = [ 0 for i in range(len(d)) ]
  l_plus = [ 0 for i in range(len(d)) ]
  l_minus = [ 0 for i in range(len(d)) ]

  for i in range(1, len(d)):
    l_p[i-1] = l[i-1] + o[i-1]

  for i in range(1, len(d)):
    l_plus[i] = (l_p[i-1] * l_p[i-1]) / (2 * d[i])
    l_minus[i] = ((d[i] - l_p[i-1]) * (d[i] - l_p[i-1])) / (2 * d[i])

  aux = 0
  aux2 = 0

  for i in range(len(d)):
    aux = aux + l_plus[i]
    aux2 = aux2 + l_minus[i]

  l_plus_prom = aux / n
  l_minus_prom = aux2 / n

  # l_prom = aux - aux2

  aux = 0
  for x in o:
    if not x == 0:
      aux = aux + 1

  u_prom = aux / n

  """
  Se necesita la informacion:
  c_item : costo de cada item en la orden
  c_setup : costo de la orden
  c_hold : holding cost
  c_short : shortage cost
  """
  c_item = 11
  c_setup = 120
  c_hold = 1.5
  c_short = 3

  it_cost = c_item * o_prom
  stp_cost = c_setup * u_prom
  hld_cost = c_hold * l_plus_prom
  shr_cost = c_short * l_minus_prom

  total_cost = round(it_cost + stp_cost + hld_cost + shr_cost, 0)

  # Imprime el costo total
  # print("Con s = " + str(s) + " y S = " + str(S) + "\tEl costo total es", total_cost)
  return total_cost



def valor():
    s, S = 55, 320
    print("Con s = " + str(s) + " y S = " + str(S) + "\tEl costo total es", main(s, S))
    s, S = 70, 200
    print("Con s = " + str(s) + " y S = " + str(S) + "\tEl costo total es", main(s, S))
    s, S = 40, 450
    print("Con s = " + str(s) + " y S = " + str(S) + "\tEl costo total es", main(s, S))


valor()
