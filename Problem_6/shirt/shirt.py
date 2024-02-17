# Import the fuctions of library
import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    # Call the fuctions
    verify_command_line()
    edited_image()

def edited_image():
    # Open the shirt image and verify if exist
    try:
        shirt = Image.open("shirt.png")
    # If doesnt exist do a exception error
    except FileNotFoundError:
        sys.exit("Input does not exist")
    # Get the size of the shirt
    size_shirt = shirt.size
    # Open the muppets_image and verify if exist
    try:
        muppets_image = Image.open(sys.argv[1])
    # If doesnt exist do a exception error
    except FileNotFoundError:
        sys.exit("Input does not exist")
    # Resize the width and height for fill in the shirt
    muppets = ImageOps.fit(muppets_image, size_shirt)
    # Paste the shirt image in muppets_image
    muppets.paste(shirt, shirt)
    # Save the new foto with the name of the file
    muppets.save(sys.argv[2])


def verify_command_line():
    # Verify if has so few argumenst
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    # Verify if has so many arguments
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # split the string in two (name, extension)
    type_file1 = splitext(sys.argv[1])
    # Call the fuction and verify if is valid
    if check_type(type_file1[1]) == False:
        sys.exit("Invalid output")
    # Same thing
    type_file2 = splitext(sys.argv[2])
    # Same thing
    if check_type(type_file2[1]) == False:
        sys.exit("Invalid output")
    # Verify if has the type of file
    if type_file1[1] != type_file2[1]:
        sys.exit("Input and output have different extensions")

def check_type(arg):
    # verify if the arg is one of this extensions
    if arg in [".jpg", ".png", ".jpeg"]:
        # return true if has
        return True
    # return false if not 
    return False

if __name__ == "__main__" :
    main()