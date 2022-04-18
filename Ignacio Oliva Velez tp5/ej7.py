def main():
    numero_invertido = 0
    n = int(input("Ingresa numero"))
    while n != 0:
        numero_invertido = 10 * numero_invertido + n % 10
        n //= 10

    print(f"Numero invertido : {numero_invertido}")


main()
