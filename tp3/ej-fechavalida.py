def main():
    d = int(input("Igrese el dia "))
    m = int(input("Igrese el mes "))
    y = int(input("Igrese el año "))

    # verifico meses pares (tienen 30 dias, excepto febrero)
    if m % 2 == 0:
        if d > 30:
            print(f"Fecha no valida {d}/{m}/{y}")
        else:
            print(f"Fecha valida {d}/{m}/{y}")
    # verifico febrero, incluyendo bisiestos
    elif m == 2:
        if y % 4 == 0 and y % 100 != 0:
            if d <= 29:
                print(f"Fecha valida {d}/{m}/{y}")
            else:
                print(f"Fecha no valida {d}/{m}/{y}")
        elif y % 4 != 0 or y % 100 == 0:
            if d <= 28:
                print(f"Fecha valida {d}/{m}/{y}")
            else:
                print(f"Fecha no valida {d}/{m}/{y}")
    # verifico meses impares (31 dias)
    elif m % 2 != 0:
        if d > 31:
            print(f"Fecha no valida {d}/{m}/{y}")
        else:
            print(f"Fecha valida {d}/{m}/{y}")


main()
