def main():

    # defino constantes

    COSTO_BASICO = 500

    COSTO_POR_PAGINA = 3.20

    # ingreso de paginas

    paginas = int(input("Ingresar numero de paginas"))

    # inicio la variable costo total con valor inicial 0

    costo_total = 0

    # proceso segun la cantidad de paginas que haya ingresado el usuario, el costo del libro

    if paginas <= 300:
        costo_total = COSTO_BASICO + paginas * COSTO_POR_PAGINA
    elif paginas <= 600:
        costo_total = COSTO_BASICO + paginas * COSTO_POR_PAGINA + 200
    elif paginas > 600:
        costo_total = COSTO_BASICO + paginas * COSTO_POR_PAGINA + 336

    # muestro en pantalla el coste total

    print(costo_total)


main()
