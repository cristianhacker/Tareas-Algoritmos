"""Desarrolle un algoritmo donde ingreses los lados de un triángulo y debemos indicar si es triángulo
equilátero (3 lados miden igual), isósceles (2 lados son iguales y el otro mide distinto) o
 escaleno (los 3 miden distinto)"""

lado1 = float(input("Ingrese la longitud para el lado 1: "))
lado2 = float(input("Ingrese la longitud para el lado 2: "))
lado3 = float(input("Ingrese la longitud para el lado 3: "))
if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
    print("No es un triángulo válido")
else:
    if lado1 == lado2 == lado3:
        print("Es un triángulo equilatero")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("Es un triángulo isóceles")
    else:
        print("Es un triángulo escaleno")
