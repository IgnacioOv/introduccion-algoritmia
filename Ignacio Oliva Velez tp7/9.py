import random


def metodo1(n):
    lista = []
    while len(lista) < n:
        r = random.randint(0, 100)
        if r not in lista:
            lista.append(r)

    return lista


def main():
    n = int(input("ingrese tamano"))
    print(metodo1(n))


main()
