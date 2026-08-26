"""Desarrolle un algoritmo que permita calcular la indemnización
correspondiente a un empleado que ha sido despedido de manera injustificada,
conforme a las normas laborales vigentes. La indemnización se calculará con base en los
años de servicio completos del empleado, teniendo en cuenta que por cada año de servicio
completo se debe pagar 1.5 veces su última remuneración mensual. El cálculo debe considerar un
límite máximo de 12 años de servicio para efectos de indemnización,
para ello debe solicitar al usuario que ingrese la última emuneración mensual y el número de años trabajados
y debes imprimir el monto total de la indemnización correspondiente"""

print("=" * 5, "INDEMNIZACIÓN", "=" * 5)
while True:
    entrada_years = input("Ingrese la cantidad de años completos de servicio: ")
    if entrada_years.isdigit():
        years_service = int(entrada_years)
        break
    else:
        print("Error: Ingrese solo números enteros (sin decimales).")

last = float(input("Ingrese su última remuneración mensual: "))
if years_service > 12:
    years_service = 12

remu = last * 1.5 * years_service
print(f"La indemnización por sus {years_service} años de servicio es: {remu}$")
