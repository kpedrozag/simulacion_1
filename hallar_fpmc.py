import math


def genera_fpmc():
    a = 48271  # semilla inicial
    m = 2147483647  # valor m
    i = 1  # iteraciones
    x = a  # el valor inicial de x es la semilla
    while x != 1:
        if ((m % x) < (m / x)) and (math.gcd(i, m-1)):
            print(math.ceil(x), end=", ")
        i += 1
        q = m / a
        r = m % a
        g_x = a * (x % q) - r * (x / q)
        if g_x > 0:
            x = g_x
        else:
            x = g_x + m


if __name__ == "__main__":
    genera_fpmc()

    print("FINALIZO")

# 7, 49, 343, 624, 4363, 18, 122, 279, 3378, 748, 367, 499, 442, 396, 57, 379, 598, 103, 3081, 293, 247, 1689,
# 918, 516, 465, 253, 22, 149, 642, 285, 20, 136, 514, 154, 513, 918, 109, 34, 232, 68, 370, 303, 969, 140, 178, 14, 94, 470, 1277, 84, 1940
# , 381, 287, 25, 175, 476, 194, 162, 118, 179, 15, 100, 207, 557, 139, 308, 349, 1904, 265, 2555, 368, 284, 149, 263, 742,
# 831, 17455, 10473, 220, 1540, 447, 285, 624, 616, 371, 383, 330, 2181,
# 441, 385, 239, 225, 635, 385, 299, 201, 406, 330, 3611, 8, 51, 355, 306, 38, 266
# , 18, 120, 838, 298, 50, 348, 14, 98, 680, 184, 935, 137, 222, 7480,
