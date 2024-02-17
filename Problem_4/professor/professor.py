import random

def main():
    # Storage the level
    level = get_level()
    # define the variables
    times = 0
    correct_t = 0

    while True:
        try:
            # Count the times
            times += 1
            if times <= 10:
                # Storage the x and y of calcule
                x, y = generate_integer(level)
                correct = check_answer(x, y, correct_t)
                correct_t += correct
            else:
                # print the score
                print(f"Score: {correct}")
                break

        except ValueError:
            pass

def get_level():
    while True:
        try:
            # Storage how many digitis are
            level = int(input("Level "))
            if level >= 1 and level <= 3:
                # return the quant of digits
                return level
        except ValueError:
            pass


def generate_integer(level):
    # If this condition, does the random numbers
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        return x, y
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        return x, y
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        return x, y

def check_answer(x, y, correct_t):
    # Define the variables
    incorrect = 0
    correct = correct_t
    correct_input = False

    while correct_input == False:
        # print the calcule
        print(f"{x} + {y} = ", end = "")
        # do the correct answer
        correct_answer = x + y
        # Storage the user answer
        user_answer = int(input(""))
        # Count the correct answer
        if user_answer == correct_answer:
            correct += 1
            incorrect = 0
            return correct
        # Count the incorrect answer
        else :
            # Print the EEE output
            print("EEE")
            incorrect += 1
        # break the loop if incorrect is equal 3
        if incorrect == 3:
            print(f"{x} + {y} = ", correct_answer)
            incorrect = 0
            correct_input = True

if __name__ == "__main__":
    main()
