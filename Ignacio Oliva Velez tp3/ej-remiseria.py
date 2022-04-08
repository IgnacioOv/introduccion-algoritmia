def main():
    # defino constantes

    VIAJE_MINIMO = 150

    # input de los kilometros
    km = int(input("Ingrese la cantidad de km "))

    # inicio variable viaje total con valor 0

    viaje_total = 0

    # proceso segun los km el precio

    if km <= 10:
        viaje_total = VIAJE_MINIMO + km * 20
    elif km > 10:
        viaje_total = VIAJE_MINIMO + km * 15

    print(viaje_total)


main()
