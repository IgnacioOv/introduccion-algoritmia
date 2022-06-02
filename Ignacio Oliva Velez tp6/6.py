def comparar(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


def main():
    print(comparar(4, 2))
    print(comparar(2, 4))
    print(comparar(4, 4))


main()
