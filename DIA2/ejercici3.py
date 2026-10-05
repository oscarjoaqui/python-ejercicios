"""Índice de masa corporal."""

peso = float(input("Ingrese el peso del objeto en kg: "))
altura = float(input("Ingrese la altura del objeto en metros: "))

IMT = peso / (altura ** 2)
print("El índice de masa corporal (IMT) es: " + str(IMT))