def promedio(notas):
	promedio = 0
	for i in range(0,len(notas)):
		promedio = promedio + notas[i]

	promedio = promedio / len(notas)


	return promedio



def arriba_promedio(legajos,notas,promedio):
	alumnos_arriba_promedio = []
	for i in range(0,len(legajos)):
		if notas[i] > promedio:
			alumnos_arriba_promedio.append(legajos[i])

	return alumnos_arriba_promedio



def main():
	notas = []
	legajos = []
	legajo = 0
	while legajo != -1:
		legajo = int(input("Ingresa legajo"))
		if legajo != -1:
			if legajo not in legajos:
				nota = int(input("Ingresa nota"))
				legajos.append(legajo)
				notas.append(nota)
			else:
				print("Legajo ya existente")


	promedio = promedio(notas)

	alumnos_arriba_promedio = arriba_promedio(legajos,notas,promedio)



main()