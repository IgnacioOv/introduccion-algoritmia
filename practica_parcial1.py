def main():
	monto_mayor = 0
	mayor_cliente = 0
	numero_cliente = 0
	total = 0
	while numero_cliente!=-1:
		numero_cliente = int(input("Ingresar numero de cliente: ")) 
		if numero_cliente != -1:
			precio = 1
			while precio != 0:
				precio = int(input("Ingresa precio unitario "))
				if precio>0:
					cantidad = int(input("Ingresa cantidad de unidades "))
					monto = cantidad * precio
						
					total = total + monto

				else:
					print("Ingrese de nuevo un valor")

				if total>1000:
					total = total*0.9

				if total>monto_mayor:
					monto_mayor = total
					mayor_cliente = numero_cliente
				elif total == monto_mayor:
					pass
				total = 0	


	print(f"Monto mayor : {monto_mayor} Numero de cliente : {mayor_cliente}")

main()