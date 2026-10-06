"""mayor de 3 numeros"""
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
numero3 = float(input("Ingrese el tercer numero: "))

mayor = numero1

if numero2 > mayor:
    mayor = numero2
elif numero3 > mayor:
    mayor = numero3
print("El mayor es de " + str(numero1) + ", " + str(numero2) + " y " + str(numero3) + " es: " + str(mayor))