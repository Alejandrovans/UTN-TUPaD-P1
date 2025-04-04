import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    sesgo = "tiene un sesgo positivo o a la derecha"
elif media < mediana and mediana < moda:
    sesgo = "tiene un sesgo negativo o a la izquierda"
else:
    sesgo = "no tiene un sesgo"

print(f"""
Lista generada: {numeros_aleatorios}

Media: {media}
Mediana: {mediana}
Moda: {moda}

La distribución {sesgo}.
""")