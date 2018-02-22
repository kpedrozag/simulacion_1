import math


def genera_fpmc():
    a = 7  # semilla inicial
    m = 2147483647  # valor m
    i = 1  # iteraciones
    x = a  # el valor inicial de x es la semilla
    entero = []  # valores full-period modulus compatibility

    while x != 1:
        if ((m % x) < (m / x)) and (math.gcd(i, m-1)):
            # print(math.ceil(x))
            entero.append(math.ceil(x))
        i += 1
        q = m / a
        r = m % a
        g_x = a * (x % q) - r * (x / q)
        if g_x > 0:
            x = g_x
        else:
            x = g_x + m

    f = open("fichero.txt", 'w')
    for x in entero:
        f.write(str(x) + ",")
    f.close()


if __name__ == "__main__":
    genera_fpmc()

    print("FINALIZO")
