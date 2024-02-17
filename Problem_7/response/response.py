# I know about uses of from, import but this way is more easy syntical for me
import validator_collection

def main():
    email = input("What's your email address? ")
    # Call the fuction
    check_valid(email)

def check_valid(s):
    try:
        Valid = validator_collection.validators.email(s)
        print("Valid")
        # Invalid is a error or empty
    except (validator_collection.errors.InvalidEmailError, validator_collection.errors.EmptyValueError):
        print("Invalid")

if __name__ == "__main__" :
    main()
