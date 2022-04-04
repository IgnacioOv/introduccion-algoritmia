def main():
	year = int(input("Ingrese el año "))
	if (year%4 != 0) or (year%4==0 and year%100==0):
		print("No bisiesto")
	else:
		print("Bisiesto")	


main()