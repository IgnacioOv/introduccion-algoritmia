"""
1.ingresar datos
2.emitir ingorme mes a mes cantidad de alumnos
3. leyenda con mayor cantidad de cumples
"""


def alumnos(meses):
    legajo = 0
    while legajo != -1:
        legajo = int(input("ingresa legajo"))
        if legajo != -1:
            d = int(input("ingrese dia"))
            m = int(input("ingrese mes"))
            a = int(input("ingrese anio"))

            if m == 1:
                meses[0].append(legajo)
            elif m == 2:
                meses[1].append(legajo)
            elif m == 3:
                meses[2].append(legajo)

    return meses


def main():
    enero = []
    febrero = []
    marzo = []
    meses = [enero, febrero, marzo]
    print(alumnos(meses))


main()
