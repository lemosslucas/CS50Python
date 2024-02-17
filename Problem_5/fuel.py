def main():
    fraction = str(input("Fraction: "))
    fraction_convert = convert(fraction)
    fuel = gauge(fraction_convert)
    print(fuel)


def convert(fraction):
    while (True):
        try :
            # Split the string
            fuel_1, fuel_2 = fraction.split("/")
            # Convert str to int
            new_fuel1 = int(fuel_1)
            new_fuel2 = int(fuel_2)
            # The fuel porcentage
            percent = new_fuel1 / new_fuel2
        # Check the exceptions
            if percent <= 1 :
                percentage = int(percent * 100)
                return percentage
            else :
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            # Do a exception
            raise

def gauge(percentage):
    # p < 1, fuel == E
    if percentage <= 1:
        return "E"
    # p > 99, fuel == F
    elif percentage >= 99:
        return "F"
    # print the porent
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
