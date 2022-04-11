def main():
	n = 0
	autos_par = 0
	autos_impar = 0
	while n != -1:
		n = int(input("Ingrese un numero "))
		if n%2==0:
			autos_par = autos_par+1
		elif n%2!=0 and n!=-1:
			autos_impar = autos_impar+1

	print(f"Pares : {autos_par},impares : {autos_impar}")


main()