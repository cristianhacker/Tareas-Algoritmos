"""1. Ingrese dos números, calcule y muestre las operaciones básicas: suma, resta, producto,
división y resto entero de ambos valores"""

num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese un número: "))
print(f"El resultado de la suma es: {num1 + num2}")
print(f"El resultado de la resta es: {num1 - num2}")
print(f"El resultado del producto es: {round(num1* num2 ,2)}")
print(f"El resultado de la divisón es: {round(num1 / num2 , 2)}")
print(f"El resultado del resto entero es: {round(num1 % num2 , 2)}")
