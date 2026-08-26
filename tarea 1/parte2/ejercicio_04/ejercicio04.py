"""Desarrolla un algoritmo que permita ingresar dos valores distintos y determinar cuál de los dos valores es el mayor y escribirlo"""

a = float(input("Ingrese un número: "))
b = float(input("Ingrese un número: "))
if a > b:
    print(f"{a} es mayor que {b}")
elif b > a:
    print(f"{b} es mayor que {a}")
else:
    print("AMbos números son iguales")
