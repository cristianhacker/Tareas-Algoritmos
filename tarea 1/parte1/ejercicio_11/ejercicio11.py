"""Desarrolle un algoritmo donde pida ingresar 2 números y la operación a calcular.
La operación “S” debe realizar la suma.
La operación “R” deber realizar la resta
La operación “M” debe realizar la multiplicación
La operación “D” debe realizar la división
Imprime el resultado calculado.
"""

print("===Escoja la operación a calular===")
print("Ingrese 'S' para realizar  la suma.")
print("Ingrese 'R' para realizar la resta")
print("Ingrese 'M' para realizar la multiplicación")
print("Ingrese  'D' para realizar  la división")
oper = input("Escoja una opción: ").upper()
a = float(input("Ingrese un número: "))
b = float(input("Ingrese un número: "))
if oper == "S":
    result = a + b
    print(f"Ha escogido suma. El resultado es: {result}")
elif oper == "R":
    result = a - b
    print(f"Ha escogido resta . El resultado es: {result}")
elif oper == "M":
    result = a * b
    print(f"Ha escogido multiplicaión. El resultado es: {result}")
elif oper == "D":
    result = a / b
    print(f"Ha escogido división. El resultado es: {result}")
else:
    print(
        "Opción no válida. Escoja sólo 'S', 'R', 'M' o 'D' para poder realizar su operación"
    )
