"""Cierta empresa asigna la tarifa por hora según la categoría en la cual se encuentra el empleado, tal
como se muestra en la siguiente tabla:
Elabora un algoritmo que permita ingresar la categoría de un empleado, luego que determine y muestre la
 tarifa que le corresponde
"""

print("====TIPOS DE CATEGORIA====")
print("CATEGORIA 'A'            | 90 $ por hora")
print("CATEGORIA 'B o C'        | 70 $ por hora")
print("CATEGORIA 'D'            | 50 $ por hora")
empleado = input("Ingrese su categoria por favor: ").upper()
if empleado == "A":
    tarifa = 90
    print(f"Su tarifa es {tarifa} $ por hora")
elif empleado == "B" or empleado == "C":
    tarifa = 70
    print(f"Su tarifa es {tarifa} $ por hora")
elif empleado == "D":
    tarifa = 50
    print(f"Su tarifa es {tarifa} $ por hora")
else:
    print("Esa opción no es válida")
