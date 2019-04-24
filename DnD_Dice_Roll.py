import random

def d4 (sides=4):
    num_rolled = random.randint(1, sides)
    return num_rolled

def d6(sides=6):
    num_rolled = random.randint(1, sides)
    return num_rolled

def d8(sides=8):
    num_rolled = random.randint(1, sides)
    return num_rolled

def d10(sides=10):
    num_rolled = random.randint(0, sides)
    return num_rolled

def d12(sides=12):
    num_rolled = random.randint(1, sides)
    return num_rolled

def d20(sides=20):
    num_rolled = random.randint(1, sides)
    return num_rolled


print("Welcome to DnD Dice Roller")

def main():
    rolling = True
    while rolling:
        choose_Die = input("Please choose the number of sides 4, 6, 8, 10, 12, 20 or enter Q/q to exit\n")
        if choose_Die == "4" :
            sides = 4
            num_rolled = d4(sides)
            print("You rolled ", num_rolled)

        elif choose_Die == "6":
            sides = 6
            num_rolled = d4(sides)
            print("You rolled ", num_rolled)

        elif choose_Die == "8":
            sides = 8
            num_rolled = d8(sides)
            print("You rolled ", num_rolled)
        
        elif choose_Die == "10":
            sides = 10
            num_rolled = d10(sides)
            print("You rolled ", num_rolled)
        
        elif choose_Die == "12":
            sides = 12
            num_rolled = d12(sides)
            print("You rolled ", num_rolled)
        
        elif choose_Die == "20":
            sides = 20
            num_rolled = d20(sides)
            print("You rolled ", num_rolled)

        elif choose_Die == "q" or choose_Die == "Q":
            rolling = False
            print("Thankyou for playing")

        else:
            print ("Incorrect value entered, please try again")



main()


