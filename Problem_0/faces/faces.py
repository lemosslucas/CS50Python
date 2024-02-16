def main():
    # Storage a string
    string = input()
    # Call the fuction
    change_emoji(string)

def change_emoji(string):
    # Declared the substring
    sub_string = ":)"
    sub_string2 = ":("
    # Check if has the subtring in string
    if sub_string in string :
        # Change for emoji
        string = string.replace(":)", "🙂")
    if sub_string2 in string :
        # Change for emoji
        string = string.replace(":(", "🙁")
    print(string)


main()