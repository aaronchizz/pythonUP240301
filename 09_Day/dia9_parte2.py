# Ejercicios: Nivel 2


# ejercicio 1 
# Write a code which gives grade to students according to theirs scores:
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

score = int(input("Ingresa la puntuación del alumno "))
if 80 <= score <= 100:
    grade = "A"
    print("La calificación del alumno es" , grade)
elif 70 <= score <=89:
    grade = "B"
    print("La calificación del alumno es" , grade)
elif 60 <= score <= 69:
    grade = "C"
    print("La calificación del alumno es" , grade)
elif 50 <= score <= 59:
    grade = "D"
    print("La calificación del alumno es" , grade)
else:
    grade = "F"
    print("La calificación del alumno es" , grade)

# ejercicio 2
#   Check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. 
# December, January or February, the season is Winter. 
# March, April or May, the season is Spring June, July or August, the season is Summer.

month = input("Ingresa un mes (iniciando con mayúscula): ")
if month in ("Septiembre", "Octubre", "Noviembre"):
    season = "Otoño"
    print("La estación para", month, "es", season)
elif month in ("Diciembre", "Enero", "Febrero"):
    season = "Invierno"
    print("La estación para", month, "es", season)
elif month in ("Marzo", "Abril", "Mayo"):
    season = "Primavera"
    print("La estación para", month, "es", season)
else:
    month in ("Junio", "Julio", "Agosto")
    season = "Verano"
    print("La estación para", month, "es", season)

# ejercicio 3 
# The following list contains some fruits: 
# fruits = ['banana', 'orange', 'mango', 'lemon']
# If the fruit exists print('That fruit already exist in the list')
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 

fruits = ['platano', 'naranja', 'mango', 'limon']
fruitToAdd = input("Ingresa una fruta (iniciando con minúscula): ")
if fruitToAdd in fruits:
    print('Esa fruta ya existe en la lista')
else:
    fruits.append(fruitToAdd)
    print("Lista modificada: ", fruits)