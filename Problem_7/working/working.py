import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # First format 09:00 AM to 17:00 PM
    #convert to 12 hours format
    if matches := re.search(r"^(([0-9][0-2]*)\:?([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*)\:?([0-5][0-9])*) ([A-P]M)$", s):
        # Storage the tuples
        time = matches.groups()
        # Verify if is a valid date
        if int(time[1]) > 12 or int(time[5]) > 12 :
            raise ValueError
        # Storage the inital time
        initial_time = change_format(int(time[1]), time[2], time[3])
        # Storage the final_time
        final_time = change_format(int(time[5]), time[6], time[7])
        # return the time in new format
        return (f"{initial_time} to {final_time}")
    else :
        raise ValueError


def change_format(hour, minute, period):
    # If minute is empty convert to 00
    if minute == None:
        minute = "00"
    # Change the format of hour when is PM
    if period == "PM" :
        if hour == 12 :
            new_hours = hour
        else:
            new_hours = hour + 12
        return f"{new_hours:02}:{minute:02}"
    elif period == "AM":
        if hour == 12:
            hour -= 12
        return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
