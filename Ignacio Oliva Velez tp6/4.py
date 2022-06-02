def multiplo(x, y):
    if x % y == 0:
        return True
    else:
        return False


def main():
    print(multiplo(40, 8))
    print(multiplo(50, 3))


main()
