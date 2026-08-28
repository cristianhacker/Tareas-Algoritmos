Algoritmo imdemnizacion
	Definir años_servicio Como Entero
	Definir last_remu, indemnizacion Como Real
	Escribir 'Ingrese la cantidad de años completos de  servicio : '
	Leer años_servicio
	Escribir 'Ingrese su última remuneración  mensual: '
	Leer last_remu
	Si años_servicio<=12 Entonces
		indemnizacion <- last_remu*1.5*años_servicio
		Escribir 'La indemnización por sus ', años_servicio, ' años de servicio es:', indemnizacion, '$'
	SiNo
		Escribir 'Usted ha excedido la cantidad de años máxima permitida. Se le pondrá 12 años por defecto'
		indemnizacion <- last_remu*1.5*12
		Escribir 'La indemnización por sus 12 años de servicio es:', indemnizacion, '$'
	FinSi
FinAlgoritmo
