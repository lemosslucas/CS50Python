from datetime import date
import inflect
import sys
# Initialize the inflect
p = inflect.engine()

class Dates :
    # initialize the birth variable
    def __init__(self, birth):
        self.birth = birth
    # Convert the days in minutes and say the number in word
    def calculed_minutes(self):
        try :
            year, month, day = self.birth.split("-")
            date_birth = date(int(year), int(month), int(day))
            # find the actual date
            now_date = date.today()
            # does the diff in the dates
            diff = now_date - date_birth
            minutes = diff.days * 24 *60
            # convert the number in words
            minutes_extense = p.number_to_words(minutes, andword = "")
            # return the final minutes
            return minutes_extense.capitalize()
        except ValueError :
            raise ValueError

def main():
    minute = minutes_quant()

def minutes_quant():
    dates = input("Date of Birth: ")
    class_date = Dates(dates)
    try :
        print(f"{class_date.calculed_minutes()} minutes")
    except ValueError:
        sys.exit(ValueError)

if __name__ == "__main__":
    main()
