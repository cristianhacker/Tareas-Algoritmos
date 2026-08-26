"""Elabora un algoritmo que permita ingresar el número de fotos a imprimir,
luego que determine y muestre el precio total."""

print("====Tarifario de fotos====")
print("Menos de 10 fotos    | 1.0 $")
print("De 10 a 30 fotos     | 0.8 $")
print("Más de 30 fotos      | 0.5 $")
cant = int(input("Ingrese la cantidad de fotos: "))
if cant < 10:
    monto = cant * 1

elif cant <= 30:
    monto = cant * 0.8

else:
    monto = cant * 0.5

print(f"El precio total por {cant} fotos es: {monto}")
