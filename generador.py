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


main()
