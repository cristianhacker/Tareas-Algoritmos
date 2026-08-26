"""Desarrolle un algoritmo en Pseudocódigo, que permita ingresar tres valores. El algoritmo
debe imprimir cual es el mayor y cuál es el menor.
 Asegúrate que los tres valores introducidos por el teclado sean valores distintos,
caso contrario muestra un mensaje de advertencia"""

a = float(input("Ingrese un número: "))
b = float(input("Ingrese un número: "))
c = float(input("Ingrese un número: "))
# Verifica que la entrada no se repita
if a == b or a == c or b == c:
    print("Advertencia: Los números no pueden repetirse")
# Verifica que número es mayor
else:
    if a > b and a > c:
        print(f"El mayor es: {a}")
    elif b > a and b > c:
        print(f"El mayor es: {b}")
    else:
        (f"El mayor es: {c}")

    # verifica que número es menor
    if a < b and a < c:
        print(f"El menor es: {a}")
    elif b < a and b < c:
        print(f"El menor es: {b}")
    else:
        print(f"El menor es: {c}")
