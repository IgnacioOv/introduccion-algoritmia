"""
1. usuario ingresa numeros entre a y b hasta que el numero ingresado sea = a -1
2
. meterlos en la lista
3.
"""

"""
while 
for
if
"""
"""
lista :  4,5,6
"""


def lista(a, b):
    lista = []
    n = 0
    while n != -1:
        n = int(input("pone un numero gorreado"))
        if n > a and n < b:
            lista.append(n)
        else:
            print(" otro numero,trolo")

    return lista


def calcular_suma(lista):
    resultado = 0
    for i in range(0, len(lista)):
        resultado = resultado + lista[i]
    return resultado


def es_capicua(array):
    array_invertido = array[::-1]
    if array == array_invertido:
        print("es capicua")
    else:
        print("no es capicua")


def busqueda_valor(n, array):
    valor = 0
    posicion = 0
    repeticiones = 0
    for i in range(0, len(array)):
        if n == array[i] and repeticiones == 0:
            valor = array[i]
            posicion = i
            repeticiones = repeticiones + 1
    if valor == n:
        return posicion


def lista_posiciones(n, array):
    posiciones = []
    for i in range(0, len(array)):
        if n == array[i]:
            posiciones.append(i)

    return posiciones





def main():
    array = lista(10, 100)
    suma = calcular_suma(array)
    es_capicua(array)
    print(busqueda_valor(20, array))
    print(lista_posiciones(20, array))


main()
