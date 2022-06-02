def elevador(x, y):
    n = 0
    total = 1

    while n < y:
        total = total * x
        n = n + 1
    return total


def main():
    print(elevador(2, 2))


main()
