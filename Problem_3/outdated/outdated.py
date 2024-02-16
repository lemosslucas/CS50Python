months = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}

def check_bar(date):
    # split the string
    month, day, year = date.split("/")
    # Check if the month and days are in limited
    if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
        print(f"{year}-{int(month):02}-{int(day):02}")
        return 0
    else:
        return -1

def check_comma(date):
    # remove the comma
    date = date.replace(",", "")
    # split the string
    month, day, year = date.split(" ")

    if month in months:
        month = months[month]
    else :
        return -1

    # Check if the month
    if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
        print(f"{year}-{int(month):02}-{int(day):02}")
        return 0
    else:
        return -1

def main():
    while True:
        try:
            # Storage the inpput
            date = input("Date: ")
            # Call the fuction
            check_bar_out = check_bar(date)
            # Check if was return the date exist
            if check_bar_out == -1 :
                pass
            elif check_bar_out == 0:
                break
            # call the fuction after the verify
            check_comma_out = check_comma(date)
            # Check if was return the date exist
            if check_comma_out == -1:
                pass
            elif check_comma_out == 0:
                break
        except:
            pass
if __name__ == "__main__":
    main()