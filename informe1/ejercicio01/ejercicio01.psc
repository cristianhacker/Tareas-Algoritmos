Algoritmo tarifrio_fotos
	Definir cant Como Entero
	Definir monto Como Real
	Escribir '====Tarifario de fotos===='
	Escribir 'Menos de 10 fotos    | 1.0 $'
	Escribir 'De 10 a 30 fotos     | 0.8 $'
	Escribir 'Más de 30 fotos      | 0.5 $'
	Escribir 'Ingrese la cantidad de fotos:'
	Leer cant
	Si cant<10 Entonces
		monto <- cant*1
	SiNo
		Si cant<=30 Entonces
			monto <- cant*0.8
		SiNo
			monto <- cant*0.5
		FinSi
	FinSi
	Escribir 'El precio total por ', cant, ' es: ', monto
FinAlgoritmo
