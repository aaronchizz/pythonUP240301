
#ejercicio 1
# Convert the ages to a set and compare the length of the list and the set, 
# which one is bigger?

age = [22, 19, 24, 25, 26, 24, 25, 24]
ages = set(age)
print('len age is :',len(age))
print('len ages is :',len(ages))
if len (age) > len(ages):
    print('el mas largo es age  :',(age))
else:
    print('el mas largo es ages :',(ages))

#ejercicio 2
#  Explain the difference between the following data types: string, list, tuple and set

print('una lista es una estructura de datos no homogenea que almacena los elementos en columnas de varias filas o solamente una y se puede modificar'   , )
print('una tupla es lo mismo que una lista a excepcion que esta no se puede modificar' , )
print('el diccionario tambienes una estructura de datos no homogenea qu ealmacena pares clave-valor'  ,  )
print('la estructura de datos establecida no es homogenea,pero almacena los elementosd en una sola fila')


#ejercicio 3
#I am a teacher and I love to inspire and teach people.
#How many unique words have been used in the sentence? 
#Use the split methods and set to get the unique words.

f = ' i am a teacher and i love to inspire and teach people'
frase =('i am a teacher and i love to inspire and teach people'.split())
set_frase = set(frase)
print ('ahi estan las',len(set_frase),' unicas palabras en la frase: ' , f)