def main():
	valor = 1
	tope = 0
	suma = 0
	i = 1
	while valor%1000!=0:
		valor = int(input("Ingrese un multiplo de 1000"))
		

	while tope<valor:
		tope = int(input("Ingresar un tope mayor al termino"))

	
	while suma < tope:
			
		print(valor)
		suma = suma + valor
		valor = valor - i
		i = i +1

main()

