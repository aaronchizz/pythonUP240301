#ejercicio 1
#Find the length of the set it_companies

ty = {"it_companies"}
print(len(ty))

#ejercicio 2
#Add 'Twitter' to it_companies

ty = {"it_companies"}
ty.add ('twitter')
print(ty)

#ejercicio 3
#Insert multiple IT companies at once to the set it_companies

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#ejercicio 4
#Remove one of the companies from the set it_companies

it_companies.remove("Amazon")
print(it_companies)

#ejercicio 5
#What is the difference between remove and discard

#si usando remove () el item no se encuentra en el set ,arrojara error
#en cambio discard no arroja nada
print("revisado")