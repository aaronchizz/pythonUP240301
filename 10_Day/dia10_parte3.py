#Exercises: Level 3



#ejercicio 1
#Go to the data folder and use the countries.py file. 
# Loop through the countries and extract all the countries containing
#  the word land.2

from paises import paises
print("paises que contienen la palabra land al final")
for paises in paises :
    if "land" in paises :
        print(paises)


#ejercicio 2
#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

print("Orden invertido:")
fruits = ['banana', 'orange', 'mango', 'lemon'] 
for fruits in reversed(fruits):
    print(fruits)

   #ejercicio 3
   # Go to the data folder and use the countries_data.py file

import paii as datac
data = datac.paises

#ejercicio 3.1
#What are the total number of languages in the data