def main():
	n = 0
	while n>=0:
		divisores = 0
		n = int(input("Ingrese un numero "))
		for i in range(1,n+1):
			if n%i==0:
				divisores = divisores+1
				print(i)

		if divisores == 2:
			print("primo")
		else:
			print("No primo")




main()