from pyfiglet import Figlet
import sys
import random
# A variable to call the fuction
figlet = Figlet()
# Check if the user set a font
if len(sys.argv) == 1:
    is_random_font = True
elif len(sys.argv) == 3 and sys.argv[1] == ("-f" or sys.argv[1] == "--font") :
    is_random_font = False
else:
    sys.exit(-1)
# Fonts of the library
figlet.getFonts()
# Storage the string
string = input("Input: ")
# if not random font uses the wanted user font
if is_random_font == False:
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(string))
# Else uses a random(libray(random)) font
else:
    font = random.choice(figlet.getFonts())
    print(figlet.renderText(string))
