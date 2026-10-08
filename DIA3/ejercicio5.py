"""cajero automatico"""

print("--BIENVENIDO AL CAJERO AUTOMATICO--")
print("1. Consultar saldo")
print("2. Retirar dinero")
print("3. Depositar dinero")
print("4. Salir")

opcion = int(input("Ingrese una opción: "))
saldo = 1000  # Saldo inicial del usuario

match opcion:
    case 1:
        print("Su saldo es: $" + str(saldo))
    case 2:
        retiro = float(input("Ingrese la cantidad a retirar: "))
        if retiro > saldo:
            print("No tiene suficiente saldo para realizar el retiro.")
        else:
            saldo -= retiro
            print("Retiro exitoso. Su nuevo saldo es: $" + str(saldo))
    case 3:
        deposito = float(input("Ingrese la cantidad a depositar: "))
        saldo += deposito
        print("Depósito exitoso. Su nuevo saldo es: $" + str(saldo))
    case 4:
        print("Gracias por usar el cajero automático.")
    case _:
        print("Opción no válida.")