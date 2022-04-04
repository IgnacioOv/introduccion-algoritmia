def main():
	d = int(input("Igrese el dia"))
	m = int(input("Igrese el mes"))
	y = int(input("Igrese el año"))

	if d>=1 and d<=31 and m==1 and m<=12:
		print(f"Fecha valida {d}/{m}/{y}")
	elif m==2 and d>28:
		print(f"Fecha no valida {d}/{m}/{y}")
	else:
		print("Fecha no valida")

main()