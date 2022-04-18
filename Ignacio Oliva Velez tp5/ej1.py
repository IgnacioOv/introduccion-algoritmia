def main():
	edad = 0
	mayores = 0
	menores = 0
	acumulado_menores = 0
	acumulado_mayores = 0

	while edad !=-1:
		edad = int(input("Ingresar edad "))
		if edad > 0 and edad<100:
			if edad>=18:
				mayores = mayores + 1
				acumulado_mayores = acumulado_mayores + edad
			elif edad < 18:
				menores = menores + 1
				acumulado_menores = acumulado_menores + edad
		else:
			print("Edad invalida")


	print(f"Cantidad de mayores: {mayores}, Promedio de mayores : {acumulado_mayores/mayores}")
	print(f"Cantidad de mayores: {menores}, Promedio de mayores : {acumulado_menores/menores}")





main()