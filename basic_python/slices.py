# Example Slices in Python

nombre = "Francisco"
print(nombre) #Show 'Francisco'.

#F r a n c i s
#0 1 2 3 4 5 6

print(nombre[0:3]) #Show 'Fra'.

print(nombre[:3]) #Is like you do 0:3 when you forget the first param. This print Show 'Fra'.

print(nombre[3:]) #Is like you do 3:last caracter when you forget the first param. This print Show 'ncisco'.

print(nombre[1:7]) #Show 'rancis'.


print(nombre[1:7:2]) #The last parameter is the skip step and show 'rni', this skip: 2(a), 4(c).

print(nombre[::-1]) #If you not specify the first and last parameter and set the third param to -1: Invert all the string BECAUSE is -1.