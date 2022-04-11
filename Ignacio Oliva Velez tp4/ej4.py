def main():
	par = 0
	impar = 0
	for i in range(42,176+1):
		if i%2==0:
			par = par+1
		else:
			impar = impar+1

	print(f"Impares = {impar}, Pares = {par}")


main()