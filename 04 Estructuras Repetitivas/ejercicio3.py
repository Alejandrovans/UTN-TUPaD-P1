#) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
inicio = min(num1, num2) + 1
fin = max(num1, num2)
suma = sum(range(inicio, fin))
print(f"La suma entre {num1} y {num2}es: {suma}")