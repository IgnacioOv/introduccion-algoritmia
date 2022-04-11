def main():
	n = 0
	par = False
	while n!=-1:
		if par==True:
			par=False
		else:
			par=True
			
		n = int(input("Ingrese un numero"))

	if par==True:
		print("par")
	else:
		print("impar")

main()