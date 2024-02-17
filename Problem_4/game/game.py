import random

while True:
    try:
        # Storage the range of the random numbers
        n = int(input("Level: "))
        # make a condition if the number has bellow 0
        if n >= 0 :
            break
    except ValueError:
        # Continued the loop until the user digit a valid input
        pass
# Storage the random number
machine_number = random.randint(0, n)
# Bool variable
found = False

while (found == False):
    try:
        # Storage the guess user
        guess = int(input("Guess: "))
        # make a condition if the number has bellow 0

        if guess == machine_number:
            print("Just right!")
            found = True
        elif guess < machine_number:
            print("Too small!")
            found = False
        elif guess > machine_number:
            print("Too large!")
            found = False
    except ValueError:
        # Continued the loop until the user digit a valid input
        pass
