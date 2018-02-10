#Proceso viejo
#dia 1
a = [0,0,1,4,4,5,7,9]
s = [0,2,1,2,1,1,3,2]

# dia 2
#a = [0,2,3,3,5,6,8,10]
#s = [0,1,2,3,1,2,1, 2]

#dia 3
#a = [0,0,1,2,3,4,7,8,10]
#s = [0,1,2,3,1,2,1,1, 1]

#proceso nuevo
#dia 1
#a = [0,0,1,1,3,3,4,6,8,9]
#s = [0,1,2,1,1,3,1,1,1,1]

#dia 2
#a = [0,0,0,3,3,5,5,7,7,8,9]
#s = [0,1,1,1,1,1,1,1,1,2,1]

#dia 3
#a = [0,1,1,1,3,3,5,6,7,9]
#s = [0,2,1,1,1,1,1,2,1,2]


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

for i in range(1,len(a)):
  print("Trabajo " + str(i) + " di = " + str(d[i]) + "\n  se fue a las " + str(c[i]))
  b[i] = a[i] + d[i]
print()
for i in range(1,len(a)):
  print("Lancha " + str(i) + " es atendida a las " + str(b[i]))
print()
gg = 0
"""
Cambiar valor de la ganancia para 
proceso viejo = 49
proceso nuevo = 37.4
"""
for i in range(1,len(a)):
  g[i] = 49
  if d[i]>2:
    g[i] = g[i] -  5
  if c[i]>12:
    g[i] = g[i] - (c[i] - 12)*10
  print("Ganancia de lancha " + str(i) + ":" + str(g[i]))
  gg = gg + g[i]
print("ganancia neta del dia: " + str(gg))
print()
suma_r = 0
suma_s = 0
suma_d = 0
suma_w = 0
for i in range(1,len(a)):
  suma_r = suma_r + a[i] - a[i - 1]
  suma_s = suma_s + s[i]
  suma_d = suma_d + d[i]
  suma_w = suma_w + d[i] + s[i]

print("Promedio de tiempo entre llegada: " + str(suma_r / (n-1)) + "\n")

print("Promedio de tiempo de servicio (si): " + str(suma_s / (n-1)) + "\n")

print("Promedio de tiempo de espera (di): " + str(suma_d / (n-1)) + "\n")

print("Promedio de tiempo de espera en el sistema (wi): " + str(suma_w / (n-1)) + "\n")

print("Para validar el modelo, los sgtes valores deben ser iguales: " + str(suma_w/(n-1)) + " = " + str(round((suma_d/(n-1)) + (suma_s/(n-1)), 1 )) + "\n")

print("PROMEDIOS POR TIEMPO.\n\n")
print("Numero de trabajos promedio en el sistema: " + str(round(suma_w/c[n-1], 3)) + "\n")

print("Numero de trabajos promedio en la cola: " + str( round(suma_d/c[n-1], 3) ) + "\n")

print("Numero de trabajos promedio en servicio: " + str(round(suma_s/c[n-1], 3)) + "\n")
