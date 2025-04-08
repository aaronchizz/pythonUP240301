#ejercicios :level 2

# ejercicio 1 
# Use for loop to iterate from 0 to 100 and print the sum of all numbers

num = 0
sum = 0
while num <= 100:
    sum = sum + num
    num += 1
print("La suma de todos los números es:" , sum)

# ejercicio 2 
# Use for loop to iterate from 0 to 100
# Print the sum of all evens and the sum of all odds

evens = 0
odds = 0
for n in range(101):
    if n%2==0:
        evens = evens + n
    else:
        odds = odds + n
print("La suma de todos los pares es de:" , evens)
print("La suma de todos los impares es de:" , odds)
print("Revisado")