# Ejercicios: Nivel 3


import random

# ejercicio 1
# Call your function shuffle_list, it takes a list as a parameter and it returns 
# a shuffled list.

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista principal:" , num)
def shuffleList (list):
    random.shuffle(list)
    return list
print('Lista al azar:', shuffleList(num))

# ejercicio 2 
# Write a function which returns an array of seven random numbers in a range of 0-9. 
# All the numbers must be unique.

def randomNum ():
    lstRanum = set()
    while (len(lstRanum) < 7):
        randnum = random.choice('123456789')
        lstRanum.add(randnum)
    return list(lstRanum)
print("Numbers al azar :" , randomNum())

