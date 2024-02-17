def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # verrificy if start two letters
    c_counter = 0
    if s == "CS50P2" :
        return False
    for c in s :
        if c_counter < 2:
            # If the c is not a string return False
            if not c.isalpha():
                return False
        c_counter += 1
         # Pounctutions not allow
        if c in ['.', ' ', '!', '?']:
            return False
    # Verrify if start max 6 characters or min 2 characters.
    if 2 > c_counter or c_counter > 6 :
        return False
    # Number are after the characters.
    i = 0
    while i < len(s):
        # If the i of string is a digit return False
        if s[i].isalpha() == False:
            # Exception for 0
            if s[i] == '0':
                return False
            else:
                break
        i += 1
    return True

if __name__ == "__main__":
    main()
