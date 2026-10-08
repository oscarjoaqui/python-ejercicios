
import random

print("--BIENVENIDO--")
print("1. JUGAR:")
print("2. CREDITOS:")
print("3. SALIR:")

op = int(input("Ingrese una opción: "))

match op:
    case 1:
        usuario = int(input("Ingrese 1 para piedra, 2 para papel y 3 para tijera: "))
        computadora = random.randint(1, 3)
        print("La computadora eligió: " + str(computadora))
        if usuario == computadora:
            print("Empate!")
        elif (usuario == 1 and computadora == 3) or (usuario == 2 and computadora == 1) or (usuario == 3 and computadora == 2):
            print("¡Ganaste!")
        else:
            print("¡Perdiste!")
    case 2:
        print("Juego desarrollado por: [ANDER GJ 07]")
    case 3:
        print("Gracias por jugar. ¡Hasta luego!")
        

    