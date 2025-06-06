#Crear una lista con los números del 1 al 100 que sean múltiplos de 4. 
# Utilizar la función range.


multiplos_de_4 = list(range(4, 101, 4)) 
print(multiplos_de_4)

#Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
#indexing con números negativos!

elementos_favoritos = ["juegos", "deportes", "armas", "peliculas", "musica"]

print(elementos_favoritos[-2])

#Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
#pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
#ejemplo: lista_vacia = []

lista_vacia = []

lista_vacia.append("comer") 
lista_vacia.append("correr")
lista_vacia.append("dormir")

print(lista_vacia)

#Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#respectivamente. Imprimir la lista resultante por pantalla.

animales = ["perro", "gato", "conejo", "pez"]

animales[-2] = "loro"
animales[-1] = "oso"

print(animales)

#Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# Explicación: 

""" En la primer línea de código está creada la lista 'numeros' que tiene 5 elementos numéricos, enteros.
    En la segunda línea se busca el número más grande de la lista (con el método max(numeros)).
    Una vez que se obtiene ese valor, se elimina (usando remove()) de la lista 'numeros'.
    Por último, se imprime por pantalla la lista 'numeros' sin el número más grande.
"""

#Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y 
# mostrar por pantalla los dos primeros.

numeros = list(range(10,31,5))
print(numeros[:2])

#Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores 
#cualesquiera. 


autos = ["megane", "duster", "astra", "argos"]
autos[1] = "hilux"
autos[2] = "amarok"

print(autos)

# Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append 
#directamente. Imprimir la lista resultante por pantalla. 

dobles = []
for numero in [5, 10, 15]:
    dobles.append(numero * 2)

print(dobles)


#Dada la lista “compras”, cuyos elementos representan los productos comprados por 
#diferentes clientes: 

#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], 
#["agua"]] 
#a) Agregar "jugo" a la lista del tercer cliente usando append. 
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
#c) Eliminar "pan" de la lista del primer cliente.  
#d) Imprimir la lista resultante por pantalla 

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], 
["agua"]] 

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

 #Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
#● Posición lista_anidada[0]: 15 
#● Posición lista_anidada[1]: True 
#● Posición lista_anidada[2][0]: 25.5 
#● Posición lista_anidada[2][1]: 57.9 
#● Posición lista_anidada[2][2]: 30.6 
#● Posición lista_anidada[3]: False 
#Imprimir la lista resultante por pantalla.

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)