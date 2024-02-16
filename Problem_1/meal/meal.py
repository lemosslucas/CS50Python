def main():
    # Storage the time
    time = convert(input("What time is it? "))
    # If the time is beewten 7 and 8
    if 7.0 <= time <= 8:
        print("Breakfast time")
    # If the time is beewten 12 and 13
    elif 12.0 <= time <= 13.0:
        print("Lunch time")
    # If the time is beewten 18 and 19
    elif 18.0 <= time <= 19.0:
        print("Dinner time")

def convert(time):
    # Change the char for a point
    hours, minutes = time.split(":")
    # Convert to float
    hours = float(hours)
    minutes = float(minutes)
    # Convert the time to float
    float_time = hours + minutes / 60.0
    # return the time
    return float_time


if __name__ == "__main__":
    main()
