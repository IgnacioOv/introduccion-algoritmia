def raiz(n):
    a = n / 2
    while (n - a) > 0.11:
        a = (n / a + a) / 2

    return a


def main():
    print(raiz(9))


main()
