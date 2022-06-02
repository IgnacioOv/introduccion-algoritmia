def multiplicar(x, y):
    n = 0
    total = 0
    while n < y:
        total = total + x
        n = n + 1
    return total


def main():
    print(multiplicar(4, 4))


main()
