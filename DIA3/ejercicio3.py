"""Clasificador de notas:"""

nota = float(input("Ingrese la nota del estudiante: "))
if nota < 0 or nota > 100:
    print("La nota ingresada no es válida. Debe estar entre 0 y 100.")
elif nota >= 90 and nota <= 100:
    print("La nota es A.")
elif nota >= 80 and nota < 90:
    print("La nota es B.")
elif nota >= 70 and nota < 80:
    print("La nota es C.")
elif nota >= 60 and nota < 70:
    print("La nota es D.")
else:
    print("La nota es F.")