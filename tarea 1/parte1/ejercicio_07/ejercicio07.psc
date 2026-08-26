Algoritmo ejercicio07
	Definir nota1, nota2, nota3, promedio Como Real
	Escribir 'Ingrese su nota: '
	Leer nota1
	Escribir 'Ingrese su nota: '
	Leer nota2
	Escribir 'Ingrese su nota: '
	Leer nota3
	promedio <- (nota1+nota2+nota3)/3
	Si promedio<=10 Entonces
		Escribir 'Su promedio es: ', promedio, ' Su rendimiento es MALO'
	SiNo
		Si promedio<=13 Entonces
			Escribir 'Su promedio es: ', promedio, ' Su rendimiento es REGULAR'
		SiNo
			Si promedio<=17 Entonces
				Escribir 'Su promedio es: ', promedio, ' Su rendimiento es BUENO'
			SiNo
				Si promedio<=20 Entonces
					Escribir 'Su promedio es: ', promedio, ' Su rendimiento es EXCELENTE'
				SiNo
					Escribir 'El promedio es insuficiente o se ha excedido. Por favor, ingrese notas vàlidas'
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
