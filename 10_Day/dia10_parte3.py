#ejercicios :level 3

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
fruits = ['bananas', 'oranges', 'mango', 'lemon'] 
for fruits in reversed(fruits):
    print(fruits)
    
# ejercicio 3
# Go to the data folder and use the countries_data.py file.

import paii as datac
data = datac.country

#  ejercicio 3.1
#What are the total number of languages in the data

countryLanguage = []
for country in data:
    for language in country['languages']:
        countryLanguage.append(language)
numberOfLanguages = len(countryLanguage)
print('La cantidades de lenguajes  es: ', numberOfLanguages)

#  ejercicio 3.2
# Find the ten most spoken languages from the data

setLanguages = set(countryLanguage)
dictLanguages = {}
for language in setLanguages:
    dictLanguages[language] = 0
for language in dictLanguages:
    for country in data:  
         if language in country['languages']:
             dictLanguages[language] = country['population'] + dictLanguages[language]
sortValuesLanguagesPopulation = sorted(dictLanguages.values(), reverse = True)
sorfKeysLanguagesPopulation = sorted(dictLanguages, key = dictLanguages.get, reverse = True)
print('Los 10 idiomas mas hablados en el mundo son (orden decreciente):')
for i in range(10):
    print("Idioma:" , sorfKeysLanguagesPopulation[i] , "Cantidad de personas que lo hablan:" , sortValuesLanguagesPopulation[i])

#  ejercicio 3.3
# Find the 10 most populated countries in the world

countryPopulation = []
setPopulation = set(countryPopulation)
dictPopulation = {}
for country in data:
    dictPopulation[country["name"]] = country["population"]
sortedCountries = sorted(dictPopulation.items(), key = lambda x: x[1], reverse = True)
print("Los 10 países más poblados son:")
for i in range(min(10, len(sortedCountries))):
    country, population = sortedCountries[i]
    print(f"{country}: {population}")

print("Revisado")
