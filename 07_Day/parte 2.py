
#ejercicio 1
# Join A and B

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(B.union(A))

#ejercicio 2
#Find A intersection B

print(A.intersection(B))

#ejercicio 3
#Is A subset of B

print(A.issubset(B))

#ejercicio 4
#Are A and B disjoint sets
print(A.isdisjoint(B))

#ejercicio 5
#Join A with B and B with A

print(A.union(B))
print(B.union(A))

#ejercicio 6
#What is the symmetric difference between A and B

print(A.symmetric_difference(B) )

#ejercicio 7
#Delete the sets completel

del A
del B

print("revisado")