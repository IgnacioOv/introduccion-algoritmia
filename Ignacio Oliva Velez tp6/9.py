def dias_fin_mes(d, m, a):
    if m == 2:
        if a % 400 == 0 and a % 100 == 0:
            faltante = 29 - d
        else:
            faltante = 28 - d

    elif m % 2 == 0:
        faltante = 30 - d

    elif m == 8:
        faltante = 31 - d
    else:
        faltante = 31 - d

    print(faltante)


def main():
    dias_fin_mes(27, 2, 2020)


main()
