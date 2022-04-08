Algoritmo periodo_segundos
	definir periodo,horas,minutos,dias,horas_decimal,segs Como real
	imprimir "Ingresar periodo en segundos"
	leer periodo
	
	dias = trunc(periodo/86400)
	horas =  trunc(((periodo%86400)/86400)*24)
	horas_decimal = ((periodo%86400)/86400)*24 - horas
	minutos = trunc(horas_decimal * 60)
	minutos_decimal = horas_decimal * 60 - minutos
	segs = minutos_decimal*60
	
	imprimir dias, " dias  " , horas, " horas  " , minutos, " minutos  " , segs, " segundos  "
	
	
	
	
FinAlgoritmo
