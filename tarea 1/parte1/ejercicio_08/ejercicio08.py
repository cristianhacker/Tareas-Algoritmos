"""Dado el siguiente Diagrama de Flujo, elabora el correspondiente Pseudocódigo Y PYTHON"""

fotos = int(input("Indique la cantidad de fotos: "))
if fotos <= 10:
    precio = 1.5
else:
    if fotos <= 30:
        precio = 1.0
    else:
        precio = 0.5
importe = fotos * precio
print(f"Su precio es: {precio}")
print(f"Su importe es: {importe}")
