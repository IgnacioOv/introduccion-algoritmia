def main():
	suma = 0
	ingresos = 0
	while suma<=100:
		n = int(input("Ingrese un numero "))
		if n%2==0:
			suma = suma + n

		ingresos = ingresos + 1

	print(f"ingresos : {ingresos}")

main()