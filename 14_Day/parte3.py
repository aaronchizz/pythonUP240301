#ejercicios dia : 3

# ejercicio 1
#Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:

import countries_data as datac
data = datac.countries

# ejercicio 1.1
#Sort countries by name, by capital, by population

print("by name :")
sortdeByName = sorted(data,key = lambda x: x ["name"])
for country in sortdeByName:
    print(country["name"])

    print("by capital:")
    sortdeByCapital = sorted(data,key = lambda x: x ["capital"])
for country in sortdeByCapital:
    print(country["capital"])

    
    print("by population:")
    sortdeByPopulation = sorted(data,key = lambda x: x ["population"])
for country in sortdeByPopulation:
    print(country["name"] , "poblation:", country["population"] )

# ejercicio 1.2
#Sort out the ten most spoken languages by location.

sortedLanguages = sorted(data ,key=lambda x:x["population"],reverse = True )
print("los 10 idiomas mas hablados por lugar: ")
top105 = sortedLanguages[:10]
for language in top105:
    print(language["languages"] , ({language["name"]}) , "lo hablan:" ,
          language["population"], "habitantes")
    
# ejercicio 1.3
#Sort out the ten most populated countries.

sortedCountries = sorted(data, key =lambda x:x["population"], reverse=True)
top10 = sortedCountries[:10]
print("los 10 mas poblados son:")
for country in top10:
    print(country["name"]) , country["population"]
    
print("Revisado")