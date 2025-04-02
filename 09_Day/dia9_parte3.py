# Ejercicios: Nivel 3


#ejercicio 1
# Here we have a person dictionary. Feel free to modify it!

person={
    'firstName': 'Asabeneh',
    'lastName': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'isMarred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

# ejercicio 1.1
# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if "skills" in person:
    middleSkill = person["skills"][len(person["skills"]) // 2]
    print("La skill (habilidad) que está en el centro es:" , middleSkill)

# ejercicio  1.2
# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

if "skills" in person:
    if "Python" in person['skills']:
        print("La persona tiene skills (habilidades) en 'Python")
    else:
        print("La persona no tiene skills (habilidades) en 'Python")

#ejercicio 1.3
# If a person skills has only JavaScript and React, print('He is a front end developer')
# If the person skills has Node, Python, MongoDB, print('He is a backend developer')
# If the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') 
# For more accurate results more conditions can be nested!

if 'skills' in person:
    if set(['JavaScript' , 'React']) == set(person['skills']):
        print('Él es un desarrollador front end')
    elif set(['Node' , 'Python' , 'MongoDB']) == set(person['skills']):
        print('Él es un desarrollador backend')
    elif set(['React' , 'Node' , 'MongoDB']) == set(person['skills']):
        print('Él es un desarrollador fullstack')
    else:
        print('Título desconocido')

# ejercicio 1.4
# If the person is married and if he lives in Finland, print the information in the following format:

if person['isMarred'] and person['country'] == 'Finland':
    print(person['firstName'] , person['lastName'] , "está casado y vive en Finlandia")