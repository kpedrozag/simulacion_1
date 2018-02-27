import math


def main():
    x = 1
    while True:
        state, gx = random_x(x)
        x = state
        print(gx)
        res = int(input("\nDesea continuar? [0 -> no | 1 -> si]\n"))
        if not res:
            break
    print("fin")


def random_x(x):
    a = 48271
    m = 2147483647
    q = m // a
    r = m % a

    t = a * (x % q) - r * (x / q)

    if t > 0:
      x = t
    else:
      x = t + m

    return x, x / m


a = 0
# ********************************************************


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


def geometric(p):
    x = 1
    aux, u = random_x(x)
    return a + math.ceil(math.log(1 - u) / math.log(p))


# ********************************************************
def binomial(n, p):
    x = 0
    for i in range(n):
        x += bernoulli(p)
    return x


def poisson(mean, a):
    x = 0
    while a < mean:
        a += math.e
        x += 1
    return x-1

# aa


def pascal(n, p):
    x = 0
    for i in range(n):
        x += geometric(p)
"""
Si n es gigante, el algoritmo es lento
def F_ast_u(u, a):
    x = a
    while random_x(x) <= u:
        x += 1
"""

main()
