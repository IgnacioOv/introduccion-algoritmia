def eliminar(lista1, lista2):
    for i in range(len(lista2)):
        if lista2[i] in lista1:
            lista1.remove(lista2[i])
    return lista1


def main():
    lista1 = [10, 20, 30, 40, 50]
    lista2 = [20, 40]
    print(eliminar(lista1, lista2))


main()
