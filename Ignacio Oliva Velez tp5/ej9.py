def main():
    n = -3
    suma = 0
    while n < 0:
        n = int(input("Ingresar un numero"))

    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i)
            suma = suma + i


main()
