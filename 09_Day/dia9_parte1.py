# Ejercicios: Nivel 1

# ejercicio 1 
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. 

age = int(input("Ingresa tu edad "))
if age >= 18:
    print("Tienes edad suficiente para aprender a conducir")
else: 
    print("Necesitas" , 18-age , "años más para aprender a conducir")

# ejercicio 2 
# Compare the values of myAge and yourAge using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if myAge = yourAge.

myAge = 18
print("Mi edad es de" , myAge , "años")
yourAge = int(input("Ingresa tu edad "))
if myAge > yourAge:
    ageDifference = myAge - yourAge
    if ageDifference == 1:
        print("Eres un año menor que yo")
    else:
        print("Eres", ageDifference, "años menor que yo")
elif yourAge > myAge:
    ageDifference = yourAge - myAge
    if ageDifference == 1:
        print("Eres un año mayor que yo")
    else:
        print("Eres", ageDifference, "años mayor que yo")
else:
    print("Tenemos la misma edad")

# ejercicio 3 
# Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.

a = int(input("Ingresa el primer número "))
b = int(input("Ingresa el segundo número "))
if a > b:
    print(a , "es mayor que" , b)
elif a < b:
    print(a , "es menor que" , b)
else:
    print(a , "es igual a" , b) 