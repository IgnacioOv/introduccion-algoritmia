Algoritmo convertir_unidades
	definir medida Como Real
	imprimir "Ingresar medida en metros "
	leer medida
	imprimir "La conversion a centimetros seria ", medida * 100
	imprimir "La conversion a pulgadas seria ", (medida * 100) / 2.54
	imprimir "La conversion a pies seria ", ((medida * 100 ) / 2.54)/12
	imprimir "La conversion a yardas seria ",(((medida * 100 ) / 2.54)/12)/3
FinAlgoritmo
