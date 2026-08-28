"""Desarrolle un algoritmo y muestra la solución en pseudocódigo, diagrama de flujo y ejecución en Python,
 que permita ingresar una clave. Si la clave es senati$2025, muestra
como resultado los mensajes: “Clave correcta” y “Usuario autorizado”"""

print("===INGRESE SU CLAVE DE SENATI===")
clave = "senati$2025"

while True:
    user = input("Digite su constraseña: ")

    if user == clave:
        print("Clave correcta")
        print("Usuario autorizado")
        break
    else:
        print("Clave incorrcta")
        print("Vuelva a intentarlo")
