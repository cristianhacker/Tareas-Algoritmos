Algoritmo ejercicio11
	Definir oper Como Cadena
	Definir a, b, result Como Real
	Escribir '===Escoja la operación a calular==='
	Escribir 'Ingrese S para realizar  la suma.'
	Escribir 'Ingrese R para realizar la resta'
	Escribir 'Ingrese M para realizar la multiplicación'
	Escribir 'Ingrese  D para realizar  la división'
	Escribir 'Escoja una opción: '
	Leer oper
	Escribir 'Ingrese un número: '
	Leer a
	Escribir 'Ingrese un número: '
	Leer b
	Si oper=='S' Entonces
		result <- a+b
		Escribir 'Ha escogido suma. El resultado es:', result
	SiNo
		Si oper=='R' Entonces
			result <- a-b
			Escribir 'Ha escogido resta. El resultado es:', result
		SiNo
			Si oper=='M' Entonces
				result <- a*b
				Escribir 'Ha escogido multiplicion. El resultado es:', result
			SiNo
				Si oper=='D' Entonces
					result <- a/b
					Escribir 'Ha escogido división. El resultado es:', result
				SiNo
					Escribir 'Opción no válida. Escoja sólo S,  R, M o D para poder realizar su operación'
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
