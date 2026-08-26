Algoritmo MayorYMenorDeTres
	Definir a,b,c Como Real
    Escribir "Ingrese el primer número: "
    Leer a
	
    Escribir "Ingrese el segundo número: "
    Leer b
	
    Escribir "Ingrese el tercer número: "
    Leer c
	
    Si a = b O a = c O b = c Entonces
        Escribir "Advertencia: Los tres valores deben ser distintos."
    Sino
		
        Si a > b Y a > c Entonces
			
            Escribir "El mayor es: ", a
        Sino
			Si b > a Y b > c Entonces
				Escribir "El mayor es: ", b
			Sino
				Escribir "El mayor es: ", c
			FinSi
		FinSi
		
			
		Si a < b Y a < c Entonces
				Escribir "El menor es: ", a
		Sino
				Si b < a Y b < c Entonces
					Escribir "El menor es: ", b
				Sino
					Escribir "El menor es: ", c
				FinSi
				
			
		FinSi
	FinSI
	
			
FinAlgoritmo

	
	
	
