"""Desarrolle un algoritmo donde ingreses la cantidad de dinero en soles y convertirlo a dólares. Imprime el mensaje
de la cantidad de dólares calculada"""

cash = float(input("Ingrese el monto a convertir: "))
dollar = 3.36
print(f"La cantidad en dòlares es: {round(cash /dollar,3)}$")
