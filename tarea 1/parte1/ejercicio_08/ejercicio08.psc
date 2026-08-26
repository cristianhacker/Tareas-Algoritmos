Algoritmo ejercicio08
	Definir fotos Como Entero
	Definir precio, importe Como Real
	Escribir 'ingrese la cantidad de fotos: '
	Leer fotos
	Si fotos<=10 Entonces
		precio <- 1.5
	SiNo
		Si fotos<=30 Entonces
			precio <- 1.0
		SiNo
			precio <- 0.5
		FinSi
	FinSi
	importe <- fotos*precio
	Escribir 'Su precio es: ', precio
	Escribir 'Su importe es: ', importe
FinAlgoritmo
