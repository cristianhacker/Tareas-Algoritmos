"""Ingresar el sueldo de una persona, si supera los S/. 3,000 soles mostrar un
mensaje en pantalla indicando que debe abonar impuestos."""

sueldo = float(input("Ingrese el monto de su sueldo: "))
if sueldo > 3000:
    print("Debe abonar impuestos")
