#Example of Python Functions in Strings.

name = input('Type your name: ') 

if len(name) == 0:  #If user not type your name 
    name = 'francisco' #Set name 'Francisco'

    # f r a n c i s c o - Each letter is a character.
    # 0 1 2 3 4 5 6 7 8 - Total 9 Characters.

print('You typed: ', name) # Show 'francisco'

print('Length: ', len(name)) # Count the number of characters. In this case is 9.

print('Capitalize: ',name.capitalize()) # Show 'Francisco'. Only convert the first character in Upper Case.

print('Upper Case: ',name.upper()) # Show 'FRANCISCO'. Convert the string in Upper Case.

print('Lower Case: ',name.lower()) # Show 'francisco'. Convert the string in Lower Case.

print('Replace: ',name.replace('o', 'a')) # Show 'francisca'. Remplace al character 'o' with 'a'.

print('Find: ',name.find('a')) # Show the indice of the character. Find in the string the caracter 'a'.

print('Count: ',name.count('r')) # Show the number of the character 'r' in string 'francisco' 

name = f'My name is {name}' # For the next example
print(name) # Show 'My name is francisco'
print(name.split(' ')) # Show '['My', 'name', 'is', 'francisco']' Split string when find the character ' ' you can try with other character for example 'a'. 

