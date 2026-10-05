"""convertir soles a dólares."""

tipo_cambio = 3.75
soles = float(input("Ingrese la cantidad de soles: "))
dolares = soles / tipo_cambio
print("La cantidad en dólares es: " + str(dolares))