def main():

    # input de notas

    nota1 = int(input("Ingresar primera nota"))
    nota2 = int(input("Ingresar segunda nota"))

    # computo segun las dos notas la condicion del alumno

    if nota1 >= 7 and nota2 >= 7:
        print("Promociona")
    elif nota1 > 4 and nota2 > 4:
        print("Aprobado")
    elif nota1 < 4 and nota2 < 4:
        print("Reprueba")
    elif nota1 < 4 or nota2 < 4:
        print("Recupera")


main()
