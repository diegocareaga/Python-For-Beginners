import random

def run():
    numerorandom = random.randint(1, 100)
    numeroelegido = int(input("Put a number: "))
    vidas = 5
    while numerorandom != numeroelegido :
        if numerorandom < numeroelegido : 
            print("Put a number less than " + str(numeroelegido))
            vidas -= 1
        elif numerorandom > numeroelegido : 
            print("Put a number bigger than " + str(numeroelegido))
            vidas -= 1
        if vidas == 0 :
            print("GAME OVER")
            break
        print("Have ", vidas, "intents")
        numeroelegido = int(input("Put a number: "))
    if numerorandom == numeroelegido : 
        print("You Won! Congratulatons!")


if __name__ == "__main__" : 
    run()