"""Desarrolle un algoritmo que permita calcular la indemnización
correspondiente a un empleado que ha sido despedido de manera injustificada,
conforme a las normas laborales vigentes. La indemnización se calculará con base en los
años de servicio completos del empleado, teniendo en cuenta que por cada año de servicio
completo se debe pagar 1.5 veces su última indemnizacionneración mensual. El cálculo debe considerar un
límite máximo de 12 años de servicio para efectos de indemnización,
para ello debe solicitar al usuario que ingrese la última emuneración mensual y el número de años trabajados
y debes imprimir el monto total de la indemnización correspondiente"""

print("=" * 5, "INDEMINIZACIÓN", "=" * 5)
años_servicio = int(input("Ingrese la cantidad de años completos de  servicio : "))
last_remu = float(input("Ingrese su última remuneración  mensual: "))

if años_servicio <= 12:
    indemnizacion = last_remu * 1.5 * años_servicio
    print(
        f"La indemnización por sus {años_servicio} años de servicio es: {indemnizacion}$"
    )
else:
    print(
        "Usted ha excedido la cantidad de años máxima permitida. Se le pondrá 12 años por defecto"
    )
    indemnizacion = last_remu * 1.5 * 12
    print(f"La indemnización por sus 12 años de servicio es: {indemnizacion}$")
