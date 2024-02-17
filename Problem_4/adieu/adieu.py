import inflect
# Create a empty array
peoples = []
# use a variable to call the library function
p = inflect.engine()

while (True):
    try:
        # Storage the user input
        name = input()
        # Append the name(user input) in the array of names
        peoples.append(name)

    except EOFError:
        # Closed the loop
        break
# Use the fuction of library
output = p.join(peoples)
# Print the msg with all names
print("Adieu, adieu, to", output) 
