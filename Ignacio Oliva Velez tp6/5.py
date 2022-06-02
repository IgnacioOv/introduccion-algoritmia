def signo(x):
    if x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        return 1


def main():
    print(signo(0))
    print(signo(-2))
    print(signo(4))


main()
