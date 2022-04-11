def main():
	rango = 10
	suma = 0

	n = int(input("Ingrese un numero "))

	max_n = n
	max_n_pos = 0
	min_n = n
	min_n_pos = 0

	for i in range(1,rango):
		n = int(input("Ingrese un numero "))
		suma=suma+n

		if n>max_n:
			max_n = n
			max_n_pos = i
		elif n<min_n:
			min_n = n 
			min_n_pos = i

	print(f"Promedio = {suma/rango}, Maximo : {max_n} posicion {max_n_pos},Minimo : {min_n} posicion {min_n_pos}")



main()