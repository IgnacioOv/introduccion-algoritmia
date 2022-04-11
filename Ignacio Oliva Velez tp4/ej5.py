def main():
	r = int(input("Ingrese el rango"))
	naturales = 0
	for i in range(1,r+1):
		if i>0:
			naturales = naturales+1

	print(f" Hay {naturales} numeros naturales")

main()