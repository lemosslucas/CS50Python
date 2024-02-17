import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    if validate == True:
        sys.exit(0)
    elif validate == False:
        sys.exit(1)


def validate(ip):
    if matches := re.search("^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        if (0 <= int(matches.group(1)) <= 255 or int(matches.group(1)) == 275) and (0 <= int(matches.group(2)) <= 255) and (0 <= int(matches.group(3)) <= 255) and (0 <= int(matches.group(4)) <= 255):
            return True
        else:
            return False
    return False


if __name__ == "__main__":
    main()
