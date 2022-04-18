def main():
    cantidad = 0
    total = 0
    solo_base = 0
    ventas_10 = 0
    while cantidad != -1:
        cantidad = int(input("Ingresar cantidad"))
        if cantidad != -1:
            precio = int(input("Ingresar precio"))

            while cantidad != 0:
                if cantidad > 12:
                    total = total + 12 * precio
                    cantidad = cantidad - 12
                if cantidad > 13:
                    total = total + 100 * (precio * 0.9)
                    cantidad = cantidad - 100
                    ventas_10 = ventas_10 + 1

                if cantidad > 100:
                    total = total + cantidad * (precio * 0.75)

                # if cantidad < 12:
                #     total = total + cantidad * precio
                #     solo_base = solo_base + 1


main()
