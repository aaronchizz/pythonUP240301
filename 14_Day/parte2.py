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
print("lista de paises en mayus:" , list(countriesUpperCased))

# ejercicio 2
#Use map to create a new list by changing each number to its square in the numbers list

def square (x):
    return x **2
numbersSquared = map (square,numbers)
print("lista de numeros cuadrados :", list(numbersSquared))

# ejercicio 3
#Use map to change each name to uppercase in the names list

def changeNamesTOUpper(name):
    return name.upper()
namesUpperCases = map(changeNamesTOUpper,names)
print("lista en mayus :", list(namesUpperCases))

# ejercicio 4
#Use filter to filter out countries containing 'land'.

def containsLnad(country):
    if "land" in country:
        return True
    return False
countriesLand = filter(containsLnad,countries)
print("paises con 'land'" , list (countriesLand))

# ejercicio 5
#Use filter to filter out countries having exactly six characters.

def  isCountryLong(country):
    if len (country) == 6:
        return True
    return False
longCountries = filter(isCountryLong,countries)
print("lis de paises con 6 caracteres :", list(longCountries))

# ejercicio 6
#Use filter to filter out countries containing six letters and more in the country list.

def countryLong(country):
    if len(country) >= 6:
        return True
    return False
longCountries2 = filter(countryLong,countries)
print ("lista de 6 o mas letras :" , list(longCountries2))

# ejercicio 7
#Use filter to filter out countries starting with an 'E'

countriesStarwithE = list(filter(lambda country : country.startswith("E"),countries))
print("paises que comienzan con E:" , countriesStarwithE)

# ejercicio 8
#Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
chainedList = list(map(str.upper,filter(lambda country :'land' in country.lower(),countries)))
print("paises que contienen la palabra land en dicha lista de paises en mayusculas :", chainedList)

# ejercicio 9
#Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

numbersAndFood = ("soup","meat",4,27,"nuts",18)
print("lista:",numbersAndFood)
def getStringLists(list):
    return [item for item in list if isinstance(item,str)]
print("los elementos de cadena son :",getStringLists(numbersAndFood))

# ejercicio 10
#Use reduce to sum all the numbers in the numbers list.

result = reduce (lambda x, y: x+ y,numbers)
print("la suma de los numeros de la lista es:",result)

# ejercicio 11
#Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

concatenatedCountries = reduce(lambda x,y: x +","+ y,countries)
print(concatenatedCountries,"are north european countries " )

# ejercicio 12
#Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).

import countries as c
countries2 = c.countries

def categorizeCountries(countries2,pattern):
    return list(filter(lambda country : pattern in country.lower(),countries2))
print("paises con patron comun:",categorizeCountries(countries2,"land"))

# ejercicio 13
#Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.

def letterCount(countries2):
    dictionary ={}
    for country in countries2:
        initial = country[0]
        dictionary[initial] = dictionary.get(initial,0) + 1
        return dictionary
    print("la cantidad de paises de cada inicial es :",letterCount(countries2))

# ejercicio 14
#Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.

def getFirstCountries(lst):
    return lst[:10]
print("los primeros 10 paises son :" , list(getFirstCountries(countries2)))

# ejercicio 15
#Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

def getLastTenCountries(lst):
    return lst[-10:]
print("los ultimos 10 paises son:",list(getLastTenCountries(countries2)))