# 1. Función imprimir_hola_mundo
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Función saludar_usuario
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# 3. Función informacion_personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4. Funciones para círculo
def calcular_area_circulo(radio):
    return 3.1416 * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * 3.1416 * radio

# 5. Conversión de segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Tabla de multiplicar
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

# 8. Cálculo de IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 9. Conversión de temperatura
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 10. Cálculo de promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3