def main():
    ACERO_PASEO = 1.5
    ACERO_MONTANA = 2

    ACERO_DISPONIBLE = 80

    paseo = 0
    montana = 0

    while paseo == 0 or montana == 0:
        paseo = int(input("Ingresar cantidad de bicicletas de paseo"))
        montana = int(input("Ingresar cantidad de bicicletas de montana"))

    acero_necesitado = paseo * ACERO_PASEO + montana * ACERO_MONTANA
    if acero_necesitado > ACERO_DISPONIBLE:
        print(
            f"No hay suficiente acero, faltan {acero_necesitado-ACERO_DISPONIBLE}kgs de acero"
        )
    else:
        print("Hay acero suficiente")


main()
