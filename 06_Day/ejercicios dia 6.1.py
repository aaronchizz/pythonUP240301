#Exercises: Level 1



#ejercicio 1
# Create an empty tuple

empty_tuple = ()
empty_tuple = tuple()

#ejercicio 2
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

empty_tuple = ('lizbet'  , 'estefania' , 'yoselin' )
empty_tupler = ("carlos",  'Luis')
print(empty_tuple)
print(empty_tupler)

#ejercicio 3
#Join brothers and sisters tuples and assign it to siblings

tpl = empty_tuple + empty_tupler
print("mis hermanos son : " , tpl)

#ejercicio 4
#How many siblings do you have?

empty_tuple = ('lizbet'  , 'estefania' , 'yoselin' )
empty_tupler = ("carlos",  'Luis')
tpl = empty_tuple + empty_tupler
print('Tengo {} hermanos'.format(len(tpl)))

#ejercicio 5
#Modify the siblings tuple and add the name of your father and mother and assign it to family_members

parents = ('mama' , 'papa' ,)
family = tpl + parents
print ('mi familia esta conformada por',family)





