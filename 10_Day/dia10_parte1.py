#Ejercicios: Level 1




#ejercicio 1
#Iterate 0 to 10 using for loop, do the same using while loop.

count = 0
while count < 10:
    print(count)
    count = count + 1

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,)
for number in numbers:
    print(numbers)

#ejercicio 2
#Iterate 10 to 0 using for loop, do the same using while loop.

count = 10
while count < 0:
    print(count)
    count = count - 1

numbers = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0,)
for number in numbers:
    print(numbers)

 # ejercicio 3
# Write a loop that makes seven calls to print(), 
# so we get on the output the following triangle:

print("Usando foor loop")
for n in range(1,8):
    print("#" * n)
print("Usando while loop")
n = 1
while n <= 7:
    print("#" * n)
    n = n + 1

# ejercicio 4
# Use nested loops to create the following:

m = 8
n = 8
for j in range(m):
    for i in range(n):
        print("#", end=" ")
    print()

# ejercicio 5
# Print the following pattern:

for t in range(11):
    print(t , "x" , t , "=" , t * t)

#ejercicio 6
#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

items = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in items:
    print(item)



#ejercicio 7
#Use for loop to iterate from 0 to 100 and print only even numbers

for i in range (101):
    if i % 2 == 0:
        print(i)

#ejercicio 8
#Use for loop to iterate from 0 to 100 and print only odd numbers

for i in range (101):
    if i % 2 ==1:
        print(i)