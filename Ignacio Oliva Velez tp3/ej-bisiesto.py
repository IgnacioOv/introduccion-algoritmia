def main():

    # ingreso el dato

    year = int(input("Ingrese el año "))

    # proceso si es bisiesto

    if (year % 4 != 0) or (year % 4 == 0 and year % 100 == 0):
        print("No bisiesto")
    else:
        print("Bisiesto")


main()
