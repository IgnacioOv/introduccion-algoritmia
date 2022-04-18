def main():
    # ingreso el numero iniciador
    n = int(input("Ingrese numero"))

    # asigno a n el primer numero antes de ingresar al ciclo
    primer_numero = n

    while n != -1:
        # almaceno en ultimo numero al n antes del input para poder saber el numero final al ingreso del -1
        ultimo_numero = n
        n = int(input("Ingrese numero"))

    # imprimo por pantalla resultados

    print(f"Primer numero: {primer_numero}, ultimo numero: {ultimo_numero}")


main()
