
while (True):
    fuel = str(input("Fraction: "))
    try :
        # Split the string
        fuel_1, fuel_2 = fuel.split("/")
        # Convert str to int
        new_fuel1 = int(fuel_1)
        new_fuel2 = int(fuel_2)
        # The fuel porcentage
        f = new_fuel1 / new_fuel2
    # Check the exceptions
        if f <= 1 :
            break
    except (ValueError, ZeroDivisionError):
        pass
# Calculate the 100 * p
p = f * 100
# p < 1, fuel == E
if p <= 1:
     print("E")
# p > 99, fuel == F
elif p >= 99:
     print("F")
# print the porcent
else:
     print(f"{p}%")