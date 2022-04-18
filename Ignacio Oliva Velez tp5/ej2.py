def main():
    alumnos = 0
    legajo = 0
    aplazo = 0
    aprobado = 0
    desaprobado = 0
    while legajo != -1:
        legajo = int(input("Ingresar legajo "))
        if legajo != -1:
            nota = int(input("Ingresa nota del final "))
            if nota == 1:
                aplazo = aplazo + 1
            elif nota < 4:
                desaprobado = desaprobado + 1
            elif nota >= 4:
                aprobado = aprobado + 1
            else:
                print("Nota invalida")

            alumnos = alumnos + 1

    print(f"Aprobados : {aprobado}")
    print(f"Desaprobados :{desaprobado}")
    print(f"Aplazados en porcentaje: {(aplazo/alumnos)*100} %")


main()
