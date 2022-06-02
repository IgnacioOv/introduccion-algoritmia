def mcd(x, y):
    mc = 0
    if x > y:
        for i in range(1, y + 1):
            if x % i == 0 and y % i == 0:
                mc = i
    elif x < y:
        for i in range(1, x + 1):
            if y % i == 0 and x % i == 0:
                mc = i
    else:
        mc = x

    return mc


def main():
    print(mcd(8, 2))
    print(mcd(8, 16))
    print(mcd(2, 2))


main()
