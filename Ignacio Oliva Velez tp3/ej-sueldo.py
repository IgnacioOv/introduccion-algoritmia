def main():

    # ingreso de daots por el usuario

    sueldo_basico = float(input("Ingrese sueldo basico "))
    antiguedad = int(input("Ingrese años de antiguedad"))
    estado_civil = int(input("Soltero : 1 \n Casado : 2 \n"))

    # inicio variable sueldo total con valor 0

    sueldo_total = 0

    # computo segun el estado civil el sueldo

    if estado_civil == 1:
        sueldo_total = sueldo_basico + sueldo_basico * (0.05 * antiguedad)
        sueldo_total = (
            sueldo_total
            - (sueldo_total * 0.11)
            - (sueldo_total * 0.03)
            - (sueldo_total * 0.03)
        )
    elif estado_civil == 1:
        sueldo_total = sueldo_basico + sueldo_basico * (0.07 * antiguedad)
        sueldo_total = (
            sueldo_total
            - (sueldo_total * 0.11)
            - (sueldo_total * 0.03)
            - (sueldo_total * 0.03)
        )

    print(f"sueldo total : {sueldo_total}")


main()
