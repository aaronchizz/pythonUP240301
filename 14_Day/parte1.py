
# Ejercicios: Nivel 1


# ejercicio 1
# Explain the difference between map, filter, and reduce.

mapf = "Toma una función y un iterable como parámetros. " 
"Devuelve un iterable con los elementos transformados."
print("map:" , mapf)

filter = "Filtra los elementos de un iterable según una condición (devuelve True o False)." 
" Devuelve un iterable con los elementos que cumplen la condición"
print("filter:" , filter)

reduce = "Acumula o reduce los elementos de un iterable a un solo" 
" valor mediante una función. No devuelve otro iterable, sino un único valor"
print("reduce:" , reduce)


# ejercicio 2
# Explain the difference between higher order function, closure and decorator.

higherOrder = "puede tomar una o mas funciones como parametros," 
"puede ser devuelta como resultado de otra funcion y se puede modifficar,"
"tambiuen se le puede asignar una varaiable"
print("higher order function:" , higherOrder)
closure =" es una funcion que recuerda las variables de su entorno externo incluso" 
"despues de que la funcion externa termine la ejecucuion"
print("closure:" , closure)
decorator = ("patron de diseño qeu permite añadir nuevas funciones a un objeto existente sin modificaer su estructura."
"toma una funcion como argumento,le agrega funcionalidad y devuleve una nueva funcion")
print("decorator:" , decorator)

# ejercicio 3
# Define a call function before map, filter or reduce, see examples.

print("Programa 3")
def double(x):
    return x * 2
numbers = [1, 2, 3, 4, 5]
print("Lista de números:" , numbers)

doubledNumbers = map(double, numbers)
print("Lista del doble de los números:" , list(doubledNumbers))

#ejercicio 4
# Use for loop to print each country in the countries list.

countries =['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
print("paises en la lista:")
for country in countries:
    print(country)

# ejercicio 5
# Use for to print each name in the names list.

names =["asabeneh","lidiya","ermias","abraham"]
print("nombres en la lista:")
for name in names :
    print(name)


# ejercicio 6
# Use for to print each number in the numbers list.

    numbers =[1,2,3,4,5,6,7,8,9,10]
    print ("numeros en la lista:")
    for number in numbers:
        print(number)