# ejercicio 1
#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 
# 'Thirty Days Of Python'.

uno = "thirty "
dos =  "days "
tres = "of "
cuatro = "python "
print (uno,)
print(dos,)
print(tres,)
print(cuatro,)
orden = uno + "" ""  + dos + "" "" +  tres + "" "" + cuatro
print (orden)

#ejercicio 2
#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

cinco = "coding "
seis =  "for "
siete = "all "

print (cinco,)
print(seis,)
print(siete,)

orden = cinco + "" ""  + seis + "" "" +  siete
print (orden)

#ejercicio 3
#Declare a variable named company and assign it to an initial value "Coding For All".


compañia = "coding for all"

#ejercicio 4
#Print the variable company using print().

print(compañia)


#ejercici0 5
#Print the length of the company string using len() method and print().

L = len(compañia)
print(L)

#ejercicio 6
#Change all the characters to uppercase letters using upper() method.

print (compañia.upper())

#ejercicio 7
#Change all the characters to lowercase letters using lower() method.

print (compañia.lower())

#ejrcicio 8
#Use capitalize(), title(), swapcase() methods to format the value of the string 
# Coding  For All.

print(compañia.capitalize() )
print(compañia.swapcase() )
print(compañia.title() )

#ejercicio 9
#Cut(slice) out the first word of Coding For All string.

print (compañia [0:6]  )
print (compañia [7:14]  )

#ejercicio 10
#Check if Coding For All string contains a word Coding using the method index
# , find or other methods.

compañia = "coding for all"

if "coding" in compañia :
    print("coding esta en la palabra")

#ejercicio 11
#Replace the word coding in the string 'Coding For All' to Python.

compañia = "coding for all"
print (compañia.replace("coding", "phyton"))

#ejercicio 12
# Change Python for Everyone to Python for All using the replace method or other methods.

print(compañia.replace("Coding For All" , "Python for Everyone"))

#ejercicio 13
#Split the string 'Coding For All' using space as the separator (split()) .

print(compañia.split( ))

#ejercicio 14
#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

programas = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(programas.split(", "))

#ejercicio 15
#What is the character at index 0 in the string Coding For All.

print("El caracter en el índice 0 de la cadena es" , compañia[0])

# ejercicio 16
# What is the last index of the string Coding For All.

print("El último índice de la cadena es" , compañia[-1])

#ejercicio 17
#What character is at index 10 in "Coding For All" string.

print("El caracter en el índice 10 es" , compañia[10])
print("(El caracter 10 es un espacio)")

#ejercicio 18
#Create an acronym or an abbreviation for the name 'Python For Everyone'.

nombre = 'Python For Everyone'
acronimo = nombre.split()
print(acronimo[0][0] + acronimo[1][0] + acronimo[2][0])

#ejercicio 19
#Create an acronym or an abbreviation for the name 'Coding For All'.

compañia = 'Coding For All'
acronimo2 = compañia.split()
print(acronimo2[0][0] + acronimo2[1][0] + acronimo2[2][0])

#ejercicio 20
#Use index to determine the position of the first occurrence of C in Coding For All.

print(compañia.index("C"))

#ejercicio 21
#Use index to determine the position of the first occurrence of F in Coding For All.


print(compañia.index("F"))

#ejercicio 22
#Use rfind to determine the position of the last occurrence of l in Coding For All People.

frase = "Coding For All People"
print(frase.rfind("l"))

#ejercicio 23
#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'

sentence = 'You cannot end a sentence with because because because is a conjunction'
sentenceSplit = sentence.split( )
print(sentenceSplit.index("because"))

#ejercicio 24
#Use rindex to find the position of the last occurrence of the word because in the following sentence:
#  'You cannot end a sentence with because because because is a conjunction'

print(sentence.rindex("because"))

#ejercicio 25
#Slice out the phrase 'because because because' in the following sentence: '
# You cannot end a sentence with because because because is a conjunction'

print("Programa 25")
print(sentence[0:30] + sentence[54:71])

#ejercicio 26
#Find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'

print("Programa 26")
print(sentenceSplit.index("because"))

#ejercicio 27
#Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'

print(sentenceSplit.index("because"))

#ejercicio 28
#Does ''Coding For All' start with a substring Coding?

print(compañia.startswith("Coding"))

#ejercicio 29
#'Does 'Coding For All' end with a substring coding?

print(compañia.endswith("Coding"))

#ejercicio 30
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.

string = ' Coding For All '
print(string.strip( ))

#ejercicio 31
# Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python

variable1 = "30DaysOfPython"
variable2 = "thirty_days_of_python"
print(variable1.isidentifier())
print(variable2.isidentifier())

#ejercicio 32
#The following list contains the names of some of python libraries:
#  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("#".join(libraries))

#ejercicio 33
# Use the new line escape sequence to separate the following sentences.
#I am enjoying this challenge.
#I just wonder what is next.

print("I am enjoying this challenge.\nI just wonder what is next.")

#ejercicio 34
#Use a tab escape sequence to write the following lines.
#Name      Age     Country   City
#Asabeneh  250     Finland   Helsinki

print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinky')

#ejercicio 35
# Use the string formatting method to display the following:
#radius = 10
#area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.

radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius %s is %s meters square"%(radius, area))

#ejrcicio 36
#Make the following using string formatting methods:

a = 8
b = 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))

print("revisado")