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


#ejercicio 13
#Split the string 'Coding For All' using space as the separator (split()) .

#ejercicio 14
#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

#ejercicio 15
#What is the character at index 0 in the string Coding For All.
