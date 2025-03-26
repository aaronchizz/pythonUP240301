#ejercicio 1
#Create an empty dictionary called dog

dog = {}

#ejercicio 2
#Add name, color, breed, legs, age to the dog dictionary

dog = {
    'name':'oslo' ,
    'color':'black' ,
    'breed':'beegle' ,
     'legs':4 ,
     'age' : 1 ,

}
print(dog)

#ejercicio 3
#Create a student dictionary and add first_name, last_name,
#  gender, age, marital status, skills, country, city and address as keys for the dictionary

student = {
    'first_name':'aaron' ,
    'last_name':'jimenez' ,
    'age':20,
    'skills':['rapido','dormilon', 'intuitivo' ,],
    'is_marred':False,
    'country':'Mexico',
    'city':'aguascalientes' ,
    'address':{
        'street':'stage street',
        'zipcode':'99900'
         }
 }
print(student)


#ejercicio 4
#Get the length of the student dictionary

print(len(student))

#ejercicio 5
#Get the value of skills and check the data type, it should be a list

print(student['skills'])
print(type(student['skills']))

#ejercicio 6
#Modify the skills values by adding one or two skills

student['skills'].append('programador')
print(student['skills'])

#ejercicio 7
#Get the dictionary keys as a list

keys = student.keys()
print(keys)

#ejercicio 8
#Get the dictionary values as a list

values = student.values()
print(values)

#ejercicio 9
#Change the dictionary to a list of tuples using items() method

print(student.items())

#ejercicio 10
#Delete one of the items in the dictionary

print(student.clear())
#ejercicio 11
#Delete one of the dictionaries

del student