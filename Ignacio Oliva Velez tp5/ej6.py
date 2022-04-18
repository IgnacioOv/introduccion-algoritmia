def main():
    n = int(input("Ingresa un numero:"))

    digitos = 0
    while n > 0:
        digitos = digitos + 1
        n = n // 10
    print(f"Digitos:{digitos}")


main()
