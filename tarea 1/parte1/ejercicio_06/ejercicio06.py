"""Diseñar un algoritmo que permita ingresar un número entero. Se desea saber si es “Par” o “Impar” (Par: var_numero%2==0)"""

num = int(input("Escriba un número entero: "))
if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
