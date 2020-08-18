defcurrency_converter(currency_type, exchange_rate):
    currency = float(input("How many "+ currency_type + " do you have? "))
    dollars = currency / exchange_rate
    dollars = str(round(dollars, 2))
    print("You have USD " + dollars)

menu = """
Welcome to my currency converter 💰💵💸

1 - Bolivian bolivianos
2 - Mexican pesos
3 - Argentinian pesos

Chose an option: 
"""
user_input = int(input(menu))
if user_input == 1:
    currency_converter("bolivianos", 6.86)
elif user_input == 2:
    currency_converter("pesos mexicanos", 23.38)
elif user_input == 3:
    currency_converter("pesos argentinos", 73.04)
else:      
    print("You did not choose a valid option!")  
    print('Bye!')