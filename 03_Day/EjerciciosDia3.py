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
c11= "pyton"
c22 = "dragon"
resultado = ("on" in c11 and "on" in c22) 
print (resultado) 

#ejercicio 14
# Espero que este curso no esté lleno de jerga. 
# Úselo en para verificar si hay jerga en la oración.
sentence = "jerga"
resultado = ("jerga" in sentence)
print(resultado)

#ejercicio 15
# No hay 'encendido' tanto en el dragón como en la pitón
c1 = "dragon"
c2= "python"
resultado = ("no 'on' " in c1 and " no 'on'" in c2 )
print (resultado)


#ejercicio 16
# Encuentre la longitud del texto python 
# y convierta el valor en float y conviértalo en string

texto = "python"
lt = len("python")
longitud_float = float (lt)
longitud_string = str (longitud_float)
print("python: , python ")
print("longitud: , longitud")
print ("longitud(float):", longitud_float)
print("longitud (string):", longitud_string) 

#ejercicio 17
# Los números pares son divisibles por 2 y el resto es cero.
#  ¿Cómo se comprueba si un número es par o no usando python?
print("el numero es par")
number = int(input("define el numero"))
par = number % 2 == 0
print (f"el numero {number} es par:{par} ")



#ejercicio 18
# Compruebe si la división del suelo de 7 por 3 
# es igual al valor int convertido de 2,7.

division = 7/3
safe = float (7/3)
iguana = safe == division
if iguana:
     print("7/3 es igual a float(7/3)")
else:
     print("el numero no es igual :")

#ejercicio 19
# Check if type of '10' is equal to type of 10

type = int("10")
A=(10)
C=type==A
print("tipo '10' es igual a 10:",C)

#ejercicio 20
# Check if int('9.8') is equal to 10

checar = float('9.8')
case = int (checar)
diferenciar = 10 
com= case==diferenciar
print("int('9.8') es igual a 10:", com )

#ejercicio 21
#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

horas = float(input("escribe las horas de trabajo:"))
salario = float(input("escribe cuanto te pagan por hora: " ))
pago = horas*salario 
print ("tu pago es de :",pago  )

#ejercicio 22
#Write a script that prompts the user to enter number of years
# . Calculate the number of seconds a person can live. Assume a person can live hundred years

Años = int(input("ingrese el numero de años: "))
segundos_por_año = 60 * 60 * 24 * 365 
segundos_totales = Años * segundos_por_año 
print (f"una persona puede vivir aproximadamente:{ segundos_totales } segundos en {Años} años.")

#ejercicio 23
#Write a Python script that displays the following table

print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")

print("revisado")