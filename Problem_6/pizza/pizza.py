import csv
import sys
from tabulate import tabulate

def main():
    verify_command_line()
    read_CSV()

def read_CSV():
    # create a empty array
    products = []
    try :
        # Open a file
        with open(sys.argv[1], "r") as CSVfile:
            # A variable for storage the line of file
            reader = csv.reader(CSVfile)
            # input the line in the array
            for row in reader:
                products.append(row)
    # Verify if the file exists
    except FileNotFoundError:
        sys.exit("File does not exist")
    # Print all informations in a file in a table design
    print(tabulate(products[1:], headers = products[0], tablefmt= "grid"))

def verify_command_line():
    # Verify if has so few argumenst
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    # Verify if has so many arguments
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

main()
