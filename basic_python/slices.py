# Example Slices in Python

nombre = "Francisco"
print(nombre) #Show 'Francisco'.

#F r a n c i s
#0 1 2 3 4 5 6

print(nombre[0:3]) #Show 'Fra'.

print(nombre[:3]) # Show 'Fra'. Is like you do 0:3 when you forget the first param.

print(nombre[3:]) # Show 'ncisco'. Is like you do 3:last caracter when you forget the first param.

print(nombre[1:7]) # Show 'rancis'.


print(nombre[1:7:2]) # Show 'rni'. The last parameter is the skip step.This skip: 2(a), 4(c).

print(nombre[::-1]) # Show 'ocsicnarF'. If you not specify the first and last parameter and set the third param to -1: Invert all the string BECAUSE is -1. 