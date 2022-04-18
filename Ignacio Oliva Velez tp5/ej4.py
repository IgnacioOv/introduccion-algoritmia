from operator import indexOf


def main():
    cliente = int(input("Ingresar numero de cliente "))
    total = int(input("Total de la factura "))

    print(f"Estado del cliente {cliente}")

    if (total * 0.02) > 200:
        print(
            f"Si paga dentro de los primeros 10 dias, total de {total - (total*0.02) }"
        )
    else:
        print(f"Si paga dentro de los primeros 10 dias, total de  {total - 200}")

    if (total * 0.1) > 200:
        print(f"Si paga dentro del dia 20, total de {total + (total*0.1) }")
    else:
        print(f"Si paga dentro del dia 20, total de  {total + 350}")


main()
