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

A = 2
B = -2
x_intercept = -B/A
print("pendiente (A):",A) 
print("interseccion en y(B)", B)
print("interseccion en x (A)" , A)

#ejercicio 9
#La pendiente es (m = y2-y1/x2-x1). Halla la pendiente y la distancia euclidiana entre el punto (2, 2) y el punto (6,10)
x1 = 2
x2 = 6
y1 = 2
y2 = 10
xC = (y2-y1)/(x2-x1)
import math
disEuclidiana = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("la pendiente es " , x_intercept)
print("la disentancia e " , disEuclidiana)


#ejercicio 10
# Compara las pendientes de las tareas 8 y 9.

if A == x_intercept: 
    print("las p son iguales")

elif A > x_intercept:
       print("la primera p es mayor")

else:
     print("la segunda p es mayor")   





#ejercicio 11
# Calcula el valor de y (y = x^2 + 6x + 9). Intenta usar diferentes 
# valores de x y averigua en qué valor de x y va a ser 0.
xx= int(input("Ingresar el valor de xx:" ))
yy= ((xx**2)+(6*xx)+9)
print ("El valor de y es :", " ", yy)
if yy==0: 
    print ("yy es igualito a 0.")
else: 
    print ("yy no es igualito a 0.")



#ejercicio 12
# Encuentra la longitud de 'pitón' y 'dragón' y haz una afirmación de comparación falsa.
length_python= len('python')
length_dragon = len('dragon')
print("Longitud de python:", length_python)
print("longitud del dragon:", length_dragon)
#falsa comparacion 
print("longitud de python no es igual a longitud de dragon:", length_python!= length_dragon )



#ejercicio 13
# Use el operador and para verificar si 'on' se encuentra tanto en 'python' como en 'dragon'
union1= "pyton"
union2 = "dragon"
resultado = ("on" in union1 and "on" in union2) 
print (resultado) 
#ejercicio 14
# Espero que este curso no esté lleno de jerga. Úselo en para verificar si hay jerga en la oración.
#ejercicio 15
# No hay 'encendido' tanto en el dragón como en la pitón
#ejercicio 16
# Encuentre la longitud del texto python y convierta el valor en float y conviértalo en string
#ejercicio 17
# Los números pares son divisibles por 2 y el resto es cero. ¿Cómo se comprueba si un número es par o no usando python?
#ejercicio 18
# Compruebe si la división del suelo de 7 por 3 es igual al valor int convertido de 2,7.

