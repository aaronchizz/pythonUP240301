


# Ejercicios: Nivel 1


import random
import string

 #ejercicio 1
# Write a function which generates a six digit/character random_user_id.

def randomUserId():
    char = string.ascii_letters + string.digits
    user = ''.join((random.choice(char)) for j in  range (6))
    return user
print('Usuario:', randomUserId())


 #ejercicio  2
# Modify the previous task. 
# Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

def userIdGenByUser ():
    char = string.ascii_letters + string.digits
    numchar = int(input("Ingrese el número de caracteres que quieras: "))
    numIDs = int(input("Ingrese el número de ID's que quiera: "))
    def generateRandomUser ():
        return ''.join((random.choice(char))for p in range(numchar ))
    print("Usuarios generados: ")
    for i in range (numIDs):
        print(generateRandomUser())
userIdGenByUser()

 #ejercicio  3
# Write a function named rgb_color_gen. 
# It will generate rgb colors (3 values ranging from 0 to 255 each).

def rgbColorGen ():
    white = random.randint(0,255)
    pink = random.randint(0,255)
    yellow = random.randint(0,255)
    return (white,pink,yellow)
print("Colores RGB:" , rgbColorGen())

print("Revisado")