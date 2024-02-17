import csv
import sys

def main():
    verify_command_line()
    # Created a empty array
    names = []
    try:
        # loop for read the file
        with open(sys.argv[1], "r") as CSVfile :
            # a reader variable
            reader = csv.DictReader(CSVfile)
            # for once row of reader, reoganaze the informations
            for row in reader:
                split_name =  row["name"].split(",")
                # Put the names and houses in the array
                names.append({"first": split_name[1].lstrip(), "last": split_name[0], "house": row["house"]})
        # if not possible to open the file
    except FileNotFoundError:
        sys.exit(f"Could not read invalid_file.csv")

    # open the after.csv
    with open(sys.argv[2], "w") as fileCSV:
        # a writer variable
        writer = csv.DictWriter(fileCSV, fieldnames = ["first", "last", "house"])
        # for write in the file
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        # for once row in the vector
        for row in names:
            # write in the file
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})

def verify_command_line():
    # Verify if has so few argumenst
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    # Verify if has so many arguments
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    #verify is a csv file
    if ".csv" not in sys.argv[1] or not ".csv" in sys.argv[2]:
        sys.exit("Not a CSV file")


main()