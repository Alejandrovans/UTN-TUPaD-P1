#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

numero = int(input("Ingrese un número entero: "))
print(f"El número tiene {len(str(abs(numero)))} dígitos")