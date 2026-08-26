"""Desarrollar un programa que calcule el promedio (debe ingresar 3 notas) de un alumno para evaluar
su rendimiento (Malo 0-10, Regular 11-13, Bueno 14- 17, Excelente 18-20)
"""

nota1 = float(input("Ingrese su nota: "))
nota2 = float(input("Ingrese su nota: "))
nota3 = float(input("Ingrese su nota: "))
promedio = (nota1 + nota2 + nota3) / 3
if promedio <= 10:
    print(f"Su promedio es:{round(promedio,2)}. Categoria:  Malo")
elif promedio <= 13:
    print(f"Su promedio es:{round(promedio,2)}. Categoria: Regular")
elif promedio <= 17:
    print(f"Su promedio es:{round(promedio,2)}. Categoria: Bueno")
elif promedio <= 20:
    print(f"Su promedio es:{round(promedio,2)}. Categoria: Excelente")
else:
    print(
        "El promedio es insuficiente o se ha excedido. Por favor, ingrese notas vàlidas"
    )
