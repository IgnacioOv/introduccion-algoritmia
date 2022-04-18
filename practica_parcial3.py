def main():
	compras = 0
	monto = 0
	while monto!=-1:
		monto = int(input("Ingresar monto de la compra"))
		if monto != -1:
			if monto>=2000:
				monto = monto * 0.8
			elif monto>=1000:
				monto = monto * 0.85

		print(f"Total: {monto}")


main()