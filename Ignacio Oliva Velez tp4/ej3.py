def main():
	n = int(input("Ingrese un numero"))
	nmin = n 
	nmax = n
	while n!=-1:
		n = int(input("Ingrese un numero"))
		if n<nmin and n!=-1:
			nmin=n
		elif n>nmax and n!=-1:
			nmax=n

	print(f"Minimo numero : {nmin}, Maximo numero : {nmax}")

main()