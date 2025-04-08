# Ejercicios: Nivel 2



import random

#ejercicio 1
# Write a function list_of_hexa_colors.
# Iteturns any number of hexadecimal colors in an array
#  (six hexadecimal numbers written after #. 
# Hexadecimal numeral system is made out of 16 symbols, 
# 0-9 and first 6 letters of the alphabet, a-f. 

def listOfHexaColors (num):
    hexc = []
    for j in range(num):
        rColor = '#' + ''.join(random.choices('0123456789ABCDEF' , k = 6))
        hexc.append(rColor)
    return hexc
print("Números de colores hexadecimales: ")
print(listOfHexaColors(5))

# #ejercicio 2
# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

def listOfRgbColors (num):
    lisRGB = [] 
    for c in range(num):
        green = random.randint(0,255)
        pink = random.randint(0,255)
        blue = random.randint(0,255)
        lisRGB.append(('rgb', pink, green, blue))
    return lisRGB
print("Número de colores RGB en una matriz:" , listOfRgbColors(5))


 #ejercicio 3
# Write a function generate_colors which can generate any number of hexa or rgb colors.

def generateColors (type, num):
    col = []
    if type == 'hexa':
        for j in range(num):
            randomColor = '#' + ''.join(random.choices('0123456789ABCDEF', k = 6))
            col.append(randomColor)
        return col
    else:
        for j in range(num):
            green = random.randint(0,255)
            pink = random.randint(0,255)
            blue = random.randint(0,255)
            col.append(('rgb', pink, green, blue))
        return col
print('Colores hexadecimales:', generateColors('hexa', 3))
print('Colores RGB:', generateColors('rgb', 2))

print("Revisado")