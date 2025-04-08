
#Ejercicios: Level 1

#ejercicio 1 
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def addTwoNumbers():
    num1 = 56
    num2 = 78
    total = num1 + num2
    print(f'La suma es {total}')
addTwoNumbers()

#ejercicio 2 
# Area of a circle is calculated as follows: area = π x r x r.
#  Write a function that calculates area_of_circle.

def areaCircle():
    p = 3.1416
    r = 12
    area = p * r *r
    print(f'el area de el circulo es de  {area}')
areaCircle()

#ejercicio 3 
# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
#  Check if all the list items are number types. If not do give a reasonable feedback.

def addAllNumbers(*args):
    return sum(args) if all(isinstance(i, (int, float))for i in args) else 'Only number values'
print(addAllNumbers(1,2,3,4.5))
print(addAllNumbers(8,'hola',89)) 

#ejercicio 4
#  Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convertCtoF (celsius):
    fahr= (celsius * 9/5) + 32
    return f'{celsius} los grados fahrenheit son  {fahr}'
print(convertCtoF(35))

#ejercicio 5 
# Write a function called check-season, it takes a month parameter and returns the season: 
# Autumn, Winter, Spring or Summer.

month = input('month: ')
yesmonth= month.capitalize()
aut = ['September', 'October', 'November']
win = ['December', 'January', 'February']
spr = ['March', 'April', 'May']
sume= ['June', 'July', 'August']

def chekcSeason(yesmonth):
    if yesmonth in aut:
        return 'The season is Autumn'
    elif yesmonth in win:
        return 'The season is Winter'
    elif yesmonth in spr:
        return 'The season is Spring'
    else:
        return 'The season is Summer'
print(chekcSeason(yesmonth))

#ejercicio 6 
# Write a function called calculate_slope which return the slope of a linear equation.

x1= int(input('Enter x1: '))
y1= int(input('Enter y1: '))
x2= int(input('Enter x2: '))
y2= int(input('Enter y2: '))
def calSlope(x1, y1, x2, y2):
    m=(y2-y1)/(x2-x1)
    return f'la pendiente es {m}'
print(calSlope(x1, y1, x2, y2))

# ejercicio 7 
# Quadratic equation is calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

b =int(input('Enter the value of b: '))
a =int(input('Enter the value of a: '))
c =int(input('Enter the value of c: '))
def solveQEqn(a,b,c):
    x1= (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    x2= (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    return f'The solution set of the quadratic equation is {x1} and {x2}'
print(solveQEqn(a,b,c))

# ejercicio 8
#  Declare a function named print_list. It takes a list as a parameter and it prints 
# out each element of the list.

Lista = ['pera','mango','manzana','uva']
def printList(list):
    for i in list:
        print(i)
print(printList(Lista))

#ejercicio 9 
# Declare a function named reverse_list. It takes an array as a parameter and it 
# returns the reverse of the array (use loops).

pedro = [1,2,3,4,5]
li=['A','B','C','D']
def reverseList(pedro):
    for val in reversed(pedro):
        print(val)
print(reverseList(pedro))
print(reverseList(li))

# ejercicio 10 
# Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns a capitalized list of items

def capitalizeListItems(bob):
    for b in bob:
        print(b.capitalize())
print(capitalizeListItems(['lluvia','pintura','celular','agua','papel']))

#ejercicio 11
#  Declare a function named add_item. It takes a list and an item parameters. 
# It returns a list with the item added at the end.

def addItem(pop,item):
    pop.append(item)
    return pop
print(addItem(['miel','loop','heart'],'pain'))

# ejercicio 12
#  Declare a function named remove_item. It takes a list and an item parameters.
# It returns a list with the item removed from it.

def removeItem(lst,item):
    if item in lst:
        lst.remove(item)
    return lst
numbers= [1,2,3,2,4]
food=['mango','grapes','banana','lemon','piña']
print(removeItem(numbers, 2))
print(removeItem(food, 'banana'))

# ejercicio 13
#  Declare a function named sum_of_numbers. 
# It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(n):
    return sum(range(1, n + 1))
num = int(input("ingresa un numero :"))
print("la suma de los numeros es : ",sum_of_numbers(num)) 

#  ejercicio 14 
# Declare a function named sum_of_odds. 
# It takes a number parameter and it adds all the odd numbers in that range.
def sumOfOdds(o):
    return sum(num for num in range(1,o+1)if num %2!=0)
print(sumOfOdds(10)) 

# ejercicio 15 
# Declare a function named sum_of_even. 
# It takes a number parameter and it adds all the even numbers in that - range.

def sumOfEven(e):
    return sum(num for num in range(1,e+1)if num %2==0)
print(sumOfEven(10)) 

print("Revisado")
