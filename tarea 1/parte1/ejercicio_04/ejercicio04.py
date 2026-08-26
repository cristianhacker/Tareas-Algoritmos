"""Diseñar un diagrama de flujo y programa en python que permita mostrar un mensaje
indicando si un alumno está Aprobado o Desaprobado en el curso de ALGORITMIA PARA EL
DESARROLLO DE PROGRAMAS. Para calcular el promedio final del curso se debe considerar:
Tarea1, Tarea2 y Tarea3. Para aprobar el curso se necesita una nota mínima de 13
"""

print("===CURSO DE ALGORITMIA PARA EL DESARROLLO DE PROGRAMAS===")
tarea1 = float(input("Ingrese su nota: "))
tarea2 = float(input("Ingrese su nota: "))
tarea3 = float(input("Ingrese su nota: "))
promedio = (tarea1 + tarea2 + tarea3) / 3
if promedio >= 13:
    print("APROBADO")
else:
    print("DESAPROBADO")
