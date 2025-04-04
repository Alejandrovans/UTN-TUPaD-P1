#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("En qué hemisferio te estas? (N para Norte / S para Sur): ").upper()
mes = int(input("Ingresa el mes (1-12): "))
dia = int(input("Ingresa el día (1-31): "))

if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
else:
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"

if hemisferio == "N":
    print(f"Estás en {estacion_norte}")
elif hemisferio == "S":
    print(f"Estás en {estacion_sur}")
else:
    print("Hemisferio no válido. Debes ingresar N o S.")