"""Desarrolle un algoritmo donde debemos ingresar la cantidad de alumnos a transportar y debemos
 calcular el costo total, sabiendo que por cada alumno el costo de transporte está en el siguiente rango.
Imprime el costo a cobrar."""

print("===Tarifario de Transporte===")
print(
    "De 0 a 19 alumnos = 70$ por alumno\nDe 20 a 49 alumonos = 40$ por alumno\n De 50 a 100 = 35$ por alumno\n De 101 a más = 20$ por alumno"
)
cant = int(input("Ingrese la cantidad de alumons a transportar: "))
if cant <= 19:
    costo = cant * 70
    print(f"El costo total por {cant} alumnos es {costo}$")
elif cant <= 49:
    costo = cant * 40
    print(f"El costo total por {cant} alumnos es {costo}$")
elif cant <= 100:
    costo = cant * 35
    print(f"El costo total por {cant} alumnos es {costo}$")

else:
    costo = cant * 20
    print(f"El costo total por {cant}alumonos es {costo}$")
