# Storage the camelCase
camelCase = input("camelCase: ")
# Does the loop for to indetificated the upper char
for c in camelCase :
    # If is the Upp char
    if c.isupper():
        # lower the char
        c = c.lower()
        #print the underline, the lower char in the same line
        print("_" + c, end="")
    # If is not the upp char
    else:
        # print the char one per one
        print(c, end="")
# For more beautiful the output
print("")
