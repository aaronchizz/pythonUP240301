
# ejercicio 1
# Filter only negative and zero in the list using list comprehension.

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print("Lista de números:" , numbers)
negativeAndZero = [i for i in numbers if i <= 0]
print("Lista de negativos y cero:" , negativeAndZero)

# ejercicio 2
# Flatten the following list of lists of lists to a one dimensional list.

listOfLists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print("Lista de las listas:" , listOfLists)
flatten = [number for row in listOfLists for number in row]
flatten = [number for row in flatten for number in row]
print("Lista aplanada:" , flatten) 


# ejercicio 3
# Using list comprehension create the following list of tuples:

Tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(0,11)]
print("lista hecha:" , Tuples)

# ejercicio 4
# Flatten the following list to a new list:

paises = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print("lista de listas de países:" , paises)
flatt = [[country.upper(), country[:3].upper(), capital.upper()] 
 for [(country, capital)]in paises]
print("lista de países aplanada:" , flatt)


# ejercicio 5
# Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print("lista de listas de países:" , countries)
listDictionaries = [{'country': item[0][0].upper(), 'city':
 item[0][1].upper()} for item in countries]
print("lista hecha a diccionario:" , listDictionaries)


# ejercicio 6
# Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
print("lista de nombres:" , names)
concanames = [name[0][0] + " " + name[0][1] for name in names]
print("lista de nombres concatenados:" , concanames)


# ejercicio 7
# Write a lambda function which can solve a slope or y-intercept of linear functions.

print("los valores son: 3, 7, 6, 12")
slope = lambda x1, x2, y1, y2: (y2-y1)/(x2-x1)
print("la pendiente es:" , slope(3, 7, 6, 12))