## Ejercicios: Nivel 1

# ejercicio 1
#  Declarar una lista vacía

emptyList = list()
print(len(emptyList))

#ejercicio 2 
# Declarar una lista con más de 5 elementos

drinks = ["cerveza" , "vino" , "Agua" , "tequila" , "jugo" , "chocolate" , "tepache"]

# ejercicio 3
#  Encuentra la longitud de tu lista
print(len(drinks))

# ejercicio 4 
# Obtener el primer elemento, el elemento del medio y el último elemento de la lista

print(drinks[0])
print(drinks[3])
print(drinks[6])

# ejercicio 5
#  Declara una lista llamada mixedDataTypes, pon tu(nombre, edad, altura, estado civil, dirección)

mixedDataTypes = ["Aaron" , "30" , "1.73" , "divorciado" , "peñol la villita"]

# ejercicio 6 
# Declare una variable de lista llamada itCompanies y asigne los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon

itCompanies = ["Facebook" , "Google" , "Microsoft" , "Apple" , "IBM" , "Oracle" , "Amazon"]

# ejercicio 7 
# Imprima la lista usando print()

print("Programa 7")
print(itCompanies)

# ejercicio 8 
# Imprima el número de empresas en la lista

print(len(itCompanies))

# ejercicio 9 
# Imprima la primera, la segunda y la última empresa

print(itCompanies[0])
print(itCompanies[1])
print(itCompanies[6])

# ejercicio 10 
# Imprima el listado después de modificar una de las empresas

print(itCompanies)
itCompanies[0] = "Meta"
print(itCompanies)

# ejercicio 11 Añadir una empresa de TI a itCompanies

itCompanies.append("Tesla")
print(itCompanies)

# ejercicio 12
#  Insertar una empresa de TI en el medio de la lista de empresas

itCompanies.insert(4, "Intel")
print(itCompanies)

# ejercicio 13
#  Cambie uno de los nombres de itCompanies a mayúsculas

itCompanies[2] = itCompanies[2].upper()
print(itCompanies)

# ejercicio 14 Unir itCompanies con una cadena '#;'

print("#;".join(itCompanies))

# ejercicio 15 
# Comprueba si una determinada empresa existe en la lista itCompanies

doesExist = "Oracle" in itCompanies
print(doesExist)

# ejercicio 16 
# Ordenar la lista usando el método sort()

itCompanies.sort()
print(itCompanies)

# ejercicio 17 
# Invierta la lista en orden descendente utilizando el método reverse()

itCompanies.reverse()
print(itCompanies)

# ejercicio 18 
# Separa las primeras 3 empresas de la lista

print(itCompanies[3:9])

# ejercicio 19 
# Elimina las últimas 3 empresas de la lista

del itCompanies[6:9]
print(itCompanies)

# ejercicio 20 
# Elimina de la lista las empresas de TI intermedias
 
itCompanies.remove("Meta")
itCompanies.remove("MICROSOFT")
print(itCompanies)

# ejercicio 21 
# 21 Eliminar la primera empresa de TI de la lista

itCompanies.pop(0)
print(itCompanies)

# ejercicio 22 
# Eliminar la o las empresas de TI intermedias de la lista

itCompanies.pop(1)
print(itCompanies)

# ejercicio 23 
# Eliminar la última empresa de TI de la lista

del itCompanies[-1]
print(itCompanies)

# ejercicio 24 
# Eliminar todas las empresas de TI de la lista

del itCompanies[0]
print(itCompanies)

# ejercicio 25 
# Destruir la lista de empresas de TI

itCompanies.clear()
print(itCompanies)

# ejercicio 26 
# Une las listas

frontEnd = ['HTML', 'CSS', 'JS', 'React', 'Redux']
backEnd = ['Node','Express', 'MongoDB']
join = frontEnd + backEnd
print(join)

# ejercicio 27 
# Copie la lista unida y asígnela a una variable fullStack, luego inserte Python y SQL después de Redux

fullStack = join.copy()
fullStack.insert(5, "Python")
fullStack.insert(6, "SQL")
print(fullStack)



## Ejercicios: Nivel 2
# ejercicio 0 lista de edades 

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# ejercicio 0.1 
# Ordena la lista y encuentra la edad mínima y máxima

ages.sort()
print(ages)
print(ages[0], "," ,ages[len(ages)-1])

# ejercicio 0.2 Agregue la edad mínima y la edad máxima nuevamente a la lista

ages.insert(0, 19)
ages.insert(-1, 26)
print(ages)

# ejercicio 0.3 Encuentra la edad media (un elemento intermedio o dos elementos intermedios divididos por dos)

medianAge = (ages[5] + ages[6]) / 2
print("La edad media es:" , medianAge)

#ejercicio 0.4 
# Encuentra la edad promedio (suma de todos los elementos dividida por su número)

average = sum(ages) / len(ages)
print("El promedio es:" , average)

# ejercicio 0.5 
# Encuentra el rango de edades (máximo menos mínimo)

range = ages[-1] - ages[0]
print("El rango de edades es de:" , range)

# ejercicio 0.6
#  Compare el valor de (mín - promedio) y (máx - promedio), use el método abs()

min = abs(ages[0] - average)
max = abs(ages[-1] - average)
print(min)
print(max)
comparison = (min and max)
print("El resultado de la comparación es:" , comparison)

#ejercicio 2.1
#Find the middle country(ies) in the countries list

import paises as p
print(len(p.countries))
media = int(len(p.countries)/2)
print(media )
print(p.countries[media]+ "  , "+p.countries[media+1])
if 'México' in p.countries:
    print('Mexico esta en: ', p.countries.index('Mexico'))
else: 
    print('No esta')
#ejercicio 2.2
# Divide the countries list into two equal lists if it is even if not one more country for the first half.

print(int(len(p.countries)/2))
list1 = p.countries [0:96] 
list2 = p.countries[96:193]
print("longitud de la primera lista:" , len(list1))
print("primera lista :" , list1)
print("longitud de la segunda lista:" , len(list2))
print("segunda lista :" , list2)
#ejercicio 2.3
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
sepcoun = countries [3:]
print(sepcoun)

print("revisado")










