# ejercicio 1
#declare your age as integer variable
edad = 19
print(type(edad))

#ejercicio 2
#Declare your height as a float variable

altura = 1.72
print(type(altura))


#ejercicio 3
#Declare a variable that store a complex number
n = 5 + 3j
print(type(n))

# ejercicio 4
## write a script that prompts the user to enter base and height of the triangle
#calculate an area  of this 
#triangle (area =0.5 x b x h)

base = float(input("ingresa la base de el triangulo: "))
altura = float(input("ingresa la altura de el tranigulo: "))
area = 0.5 * base * altura
print ( "la area de el triangulo es de  ", area)

#ejercicio 5
#Write a script that prompts the user to enter side a, side b, and side c of the triangle.
#  Calculate the perimeter of the triangle (perimeter = a + b + c).

A = float(input("lado a: "))
B = float(input("lado b: "))
C = float(input("lado c: "))
perimetro = A + B + C
print ("el perimetro es",perimetro)

# ejercicio 6
#Get length and width of a rectangle using prompt. 
# Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

largo = float (input("ingresa el largo:"))
ancho = float (input("ingresa el ancho:"))

area = largo * ancho 
perimeter = 2 * (ancho + largo)
print ("la area de el trangulo es",area)
print ("el perimetro  de el trangulo es",perimeter)

# ejercicio 7 
#Get radius of a circle using prompt. 
# Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

pi = 3.14
radio = float (input("ingresa el radio:"))

area = pi * radio * radio 
circun = 2 * pi * radio

print ("la area de el circulo es",area)
print ("el perimetro de el cirulo   es",circun)

# ejercicio 8
#Calculate the slope, x-intercept and y-intercept of y = 2x -2


