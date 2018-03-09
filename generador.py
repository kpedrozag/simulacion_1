import math
import random


def main():
    x = 1
    hora = -1
    arrival = []
    service = []
    while hora < 45:
        state, gx = random_x(x)
        x = state
        valor = poisson(0.58, gx)
        print("hora: ", hora)
        if valor < 5:
            print("no. carros:", valor)
            for i in range(valor):
                state, gx = random_x(x)
                x = state
                valor_g = geometric(0.39, gx)
                print("carro:", i, "tiempo servicio: ", valor_g)
                arrival.append(hora)
                service.append(valor_g)
        else:
            print("no. carros:", valor)
        hora += 1
        print("numero de carros:", len(arrival), len(service))
    print(arrival)
    print(service)
    print("fin")

# [7, 49, 343, 2401, 5058, 974, 6817, 1482,
# 9671, 278, 1942, 9656, 2765, 8614, 4445,
# 5448, 7283, 2869, 2269, 895, 6264]


def random_x(x):
    # seed = a
    seed = 1942
    m = 2147483647
    q = m // seed
    r = m % seed

    t = seed * (x % q) - r * (x / q)

    if t > 0:
      x = t
    else:
      x = t + m

    return x, x / m


# ********************************************************
a = 0


def bernoulli(p):
    x = 1
    if random_x(x) < 1.0-p:
        return 0
    else:
        return 1


def equilikely(a, b):
    x = 1
    aux, u = random_x(x)
    return a + math.floor(u * (b - a + 1))


def geometric(p, u):
    a = 1  # valor minimo que puede tomar la variable aleatoria
    return a + math.ceil(math.log(1 - u) / math.log(p))


# ********************************************************
def binomial(n, p):
    x = 0
    for i in range(n):
        x += bernoulli(p)
    return x


def poisson(mean, ra):
    a = 0.0
    x = 0
    while a < mean:
        a += exponential(1.0, ra)
        x += 1
    return x-1


def exponential(ex, u):
    return -ex * math.log(1.0 - u)


def pascal(n, p):
    x = 0
    for i in range(n):
        x += geometric(p)


def get_semilla():
    seed = [7, 49, 343, 2401, 16807, 41924, 118822, 13612, 95279, 19045, 59121, 26905, 61327,
            105367, 1757351, 120260, 43654, 5058, 35400, 52069, 974, 6817, 47713, 118633, 830427,
            194943, 246639, 23781, 207206, 43461, 31780, 34907, 1482, 10370, 81588, 57488, 164975,
            69165, 287212, 41415, 51190, 344093, 612342, 56248, 45764, 70604, 916162, 353903, 9671,
            67697, 254592, 56323, 44530, 263689, 12952, 278, 1942, 13591, 95131, 95168, 83043, 26810,
            19076, 11956, 50239, 14336, 11044, 43012, 140258, 10973, 11885, 83017, 52165, 74726, 76974,
            155232, 87795, 32238, 327560, 17649, 41844, 9656, 67587, 62923, 46909, 2765, 19354, 37326,
            15639, 29573, 46884, 76518, 58772, 88262, 500112, 46782, 2535400, 92932, 15481, 90961, 48414,
            300221, 131256, 417068, 76209, 8614, 348844, 32438, 16773, 30831, 334187, 15690, 19983, 242928,
            139828, 42332, 4445, 31112, 19925, 62133, 71841, 70720, 36931, 258515, 43992, 72835, 60232,
            69035, 5448, 38134, 203476, 13723, 35939, 49719, 58832, 30615, 86154, 36170, 49990, 175749,
            45395, 12879, 122072, 51880, 2886403, 38340, 7283, 50975, 43140, 44743, 61508, 12193, 85350,
            2869, 20082, 27428, 2269, 15880, 34326, 45349, 112505, 202842, 63708, 52944, 60547, 12335, 86342,
            52701, 67374, 21024, 56124, 895, 6264, 43844, 39466, 21842, 76012, 19174, 115270, 49906]
    return random.choice(seed)


main()
