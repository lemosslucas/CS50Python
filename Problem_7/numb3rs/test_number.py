# Import the fuctions in bank.py
import numb3rs

def main():
    # Call the fuctions
    test_validate()

def test_validate():
    # Test if the program return 0
    assert numb3rs.validate("255.255.255.255") == True
    assert numb3rs.validate("512.512.512.512") == False
    assert numb3rs.validate("512.512.512.512") == False
    assert numb3rs.validate("1.2.3.1000") == False
    assert numb3rs.validate("cat") == False


if __name__ == "__main__":
    main()
