def main():
	km = int(input("Ingrese la cantidad de km "))
	viaje_minimo = 150
	viaje_total = 0
	if km <=10:
		viaje_total = viaje_minimo + km*20
	elif km > 10:
		viaje_total = viaje_minimo + km*15

	print(viaje_total)


main()