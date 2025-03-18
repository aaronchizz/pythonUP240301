#Exercises: Level 2

#ejercicio 1
#Unpack siblings and parents from family_members

family = ('lizbet'  , 'estefania' , 'yoselin' ,"carlos",  'Luis','mama' , 'papa' ,)
family = list(family)
print (family)
tpl = family [0:5]
print(f"mis hermanos son {tpl}" )
parents = family [5:]
print(f"mis padres son {parents}")

#ejercicio 2
#Create fruits, vegetables and animal products tuples.
# Join the three tuples and assign it to a variable called food_stuff_tp

fruits = ("manzana" , " pera" , " guayaba" ,)
vegeta = ("apio " , " lechuga " , " rabano" ,)
p_animal = ("jamon " , " salchhicha" , " queso"  ,)
food_stuff_tp = fruits + vegeta + p_animal

print ("mis prdocutos son " , food_stuff_tp)

#ejercicio 3
#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt =list(food_stuff_tp)
print(food_stuff_lt)

#ejercicio 4
#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

mediano =food_stuff_lt[4]
print(mediano)

#ejercicio 5
#Slice out the first three items and the last three items from food_staff_lt list

pf = food_stuff_lt [0:3]
fp = food_stuff_lt [5:8]
print(pf )
print ( fp)

#ejercicio 6
#Delete the food_staff_tp tuple completely

del food_stuff_tp

#ejercicio 7
#Check if an item exists in tuple:

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(nordic_countries)


#Check if 'Estonia' is a nordic country

if "Estonia" in nordic_countries :
    print("estonuia es un pais nordico")
else:
    print("estonia no es un pais nordico")

#Check if 'Iceland' is a nordic country

if "Iceland" in nordic_countries :
    print("iceland es un pais nordico")
else:
    print("iceland no es un pais nordico")

