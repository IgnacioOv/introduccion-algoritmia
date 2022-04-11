def main():
	max_rango = int(input("Ingrese hasta que numero desea multiplicar "))
	n = int(input("Ingrese el numero a multiplicar "))
	for i in range(1,max_rango+1):
		print(f"{i} x {n} = {i*n}")

main()