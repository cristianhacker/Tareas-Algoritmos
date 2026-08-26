Algoritmo tipo_categoria
	Definir empleado Como Cadena
	Escribir '====TIPOS DE CATEGORIA===='
	Escribir 'CATEGORIA A            | 90 $ por hora'
	Escribir 'CATEGORIA B o C        | 70 $ por hora'
	Escribir 'CATEGORIA D          | 50 $ por hora'
	Leer empleado
	empleado <- mayusculas(empleado)
	Si empleado='A' Entonces
		tarifa <- 90
		Escribir 'Su tarifa es ', tarifa, ' $ por hora'
	SiNo
		Si empleado='B' O empleado='C' Entonces
			tarifa <- 70
			Escribir 'Su tarifa es ', tarifa, ' $ por hora'
		SiNo
			Si empleado='D' Entonces
				tarifa <- 50
				Escribir 'Su tarifa es ', tarifa, ' $ por hora'
			SiNo
				Escribir 'Esa opción no es válida'
			FinSi
		FinSi
	FinSi
FinAlgoritmo
