Algoritmo ejercicio12
	Escribir '===Tarifario de Transporte==='
	Escribir 'De 0 a 19 alumnos = 70$ por alumno'
	Escribir 'De 20 a 49 alumonos = 40$ por alumno'
	Escribir 'De 50 a 100 = 35$ por alumno'
	Escribir 'De 101 a más = 20$ por alumno'
	Definir cant, costo Como Entero
	Escribir 'Ingrese la cantidad de alumons a transportar: '
	Leer cant
	Si cant<=19 Entonces
		costo <- cant*70
	SiNo
		Si cant<=49 Entonces
			costo <- cant*40
		SiNo
			Si cant<=100 Entonces
				costo <- cant*35
			SiNo
				costo <- cant*20
			FinSi
		FinSi
	FinSi
	Escribir 'El costo total por ', cant, ' Alumnos es ', costo, '$'
FinAlgoritmo
