def main():
    cantidad_terminos = int(input("Ingresar la cantidad de terminos"))
    termino = 1

    for i in range(1, cantidad_terminos + 1):
        print(termino)
        termino = termino * 2 + 5


main()
