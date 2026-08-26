Algoritmo ejercicio10
	Definir lado1, lado2, lado3 Como Real
	Escribir 'Ingrese la longitud para el lado 1: '
	Leer lado1
	Escribir 'Ingrese la longitud para el lado 2: '
	Leer lado2
	Escribir 'Ingrese la longitud para el lado 3: '
	Leer lado3
	Si lado1+lado2<=lado3 O lado1+lado3<=lado2 O lado2+lado3<=lado1 Entonces
		Escribir 'Esas medidas no corresponden a un triángulo válido'
	SiNo
		Si lado1==lado2 Y lado1==lado3 Y lado2==lado3 Entonces
			Escribir 'Es un triángulo equilatero'
		SiNo
			Si lado1==lado2 O lado2==lado3 O lado1==lado3 Entonces
				Escribir 'Es un triángulo isóceles'
			SiNo
				Escribir 'Es un triangulo escaleno'
			FinSi
		FinSi
	FinSi
FinAlgoritmo
