# Ejercicios: Nivel 2
from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
print("Lista de países:" , countries)
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
print("Lista de nombres:" , names)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista de números:" , numbers)

# ejercicio 1
#Use map to create a new list by changing each country to uppercase in the countries list
def changeToUpper(country):
    return country.upper()
countriesUpperCased = map(changeToUpper,countries)
print("lista de paises en mayuscula:" , list(countriesUpperCased))
    

# ejercicio 2
#Use map to create a new list by changing each number to its square in the numbers list

# ejercicio 3
#Use map to change each name to uppercase in the names list


# ejercicio 4
#Use filter to filter out countries containing 'land'.


# ejercicio 5
#Use filter to filter out countries having exactly six characters.

# ejercicio 6
#Use filter to filter out countries containing six letters and more in the country list.


# ejercicio 7
#Use filter to filter out countries starting with an 'E'

# ejercicio 8
#Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))


# ejercicio 9
#Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

# ejercicio 10
#Use reduce to sum all the numbers in the numbers list.

# ejercicio 11
#Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries


# ejercicio 12
#Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).


# ejercicio 13
#Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.




# ejercicio 14
#Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.

# ejercicio 15
#Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
