def main():
	paginas = int(input("Ingresar numero de paginas"))

	costo_basico = 500

	costo_por_pagina = 3.20

	costo_total = 0

	if paginas <= 300:
		costo_total = costo_basico + paginas*costo_por_pagina
	elif paginas <=600:
		costo_total = costo_basico + paginas*costo_por_pagina + 200
	elif paginas > 600:
		costo_total = costo_basico + paginas*costo_por_pagina + 336


	print(costo_total)


main()