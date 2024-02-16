def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Change the "$" for empty
    dollars = d.replace("$", "")
    # Convert a string to float
    dollars = float(dollars)
    # return the float value
    return dollars

def percent_to_float(p):
    # Change the "%" for empty
    p_float = p.replace("%", "")
    # Convert a string to float
    p_float = float(p_float)
    # Calculates the percent of the wanted percentage
    percent = p_float / 100
    # return the float value
    return percent

main()