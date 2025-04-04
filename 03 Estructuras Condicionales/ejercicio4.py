#Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Introduce tu edad: "))

if edad >= 0 and edad <= 12:
    print("Sos un niño.")
elif edad >= 13 and edad <= 17:
    print("Sos un adolescente.")
elif edad >= 18 and edad <= 30:
    print("Sos un adulto joven.")
else:
    print("Sos un adulto mayor.")
