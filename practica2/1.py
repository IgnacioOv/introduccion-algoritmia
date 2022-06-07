def main():
	suma = 0
	menor = 1000000
	mayor = 0
	numeros = [10,20,5,40,50]

	for i in range(0,len(numeros)):
		if numeros[i] < menor:
			menor = numeros[i]
		elif numeros [i] > mayor:
			mayor = numeros[i]

		suma = suma + numeros[i]

	promedio = suma/len(numeros)

	print(f"El numero menor es {menor}")
	print(f"El numero mayor es  {mayor}")
	print(f"El promedio de la lista es {promedio}")



main()